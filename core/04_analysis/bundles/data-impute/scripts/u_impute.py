"""
u_impute.py — 分组分层缺失值插补
═══════════════════════════════════════════════════════════════════
功能：对数据框按 Group 分层执行缺失值插补。支持：
      - 数值列：直接参与插补
      - 分类列（可选）：先整数编码 → 插补 → 就近取整还原类别
      方法（由快到慢）：
        * median / mean — 组内中位数/均值（秒级）
        * mice           — IterativeImputer + BayesianRidge（数秒～十余秒）
        * missForest     — IterativeImputer + RandomForest（可调快/慢）

加速要点（missForest）：
      - n_nearest_features：每列只用最相关的 k 个预测变量（默认 32）
      - skip_complete：完整列不做目标建模
      - 更少树 / 更浅树 / 更少迭代（见 §1 默认参数）

独立运行：
    python -m modules.u_impute
═══════════════════════════════════════════════════════════════════
"""

from __future__ import annotations
from typing import Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge

# ═════════════════════════════════════════════════════════════════
# §1  顶层可调参数（速度优先的默认值；要更高质量可加大）
# ═════════════════════════════════════════════════════════════════
IMPUTE_GROUP_COL = "Group"       # 分组列名
IMPUTE_SEED = 66                 # 随机种子
IMPUTE_MAX_ITER = 10             # 迭代次数（原 20；10 通常足够）
IMPUTE_MF_N_TREES = 30           # missForest 树数（原 100；30 通常 3–5× 加速）
IMPUTE_MF_MAX_DEPTH = 8          # RF 最大深度（None=不限，更慢）
IMPUTE_MF_MAX_FEATURES = "sqrt"  # RF 每次分裂考虑特征子集
IMPUTE_N_NEAREST = 32            # 每列只用 |corr| 最大的 k 个预测变量；None=全部
IMPUTE_MIN_NONMISSING = 2        # 每列建模所需最少非缺失值数
IMPUTE_MIN_UNIQUE = 2            # 每列建模所需最少不同取值数
# 分类列：唯一值超过该比例/频数时视为 ID 类，不参与插补
IMPUTE_CAT_MAX_UNIQUE = 50
IMPUTE_CAT_MAX_UNIQUE_RATIO = 0.5

# 合法 method 别名
_METHOD_ALIASES = {
    "missforest": "missForest",
    "miss_forest": "missForest",
    "rf": "missForest",
    "mice": "mice",
    "bayesianridge": "mice",
    "median": "median",
    "mean": "mean",
}


def _normalize_method(method: str) -> str:
    key = str(method).strip().lower().replace("-", "_")
    if key in _METHOD_ALIASES:
        return _METHOD_ALIASES[key]
    if method in ("missForest", "mice", "median", "mean"):
        return method
    raise ValueError(
        f"method must be one of missForest / mice / median / mean, got {method!r}"
    )


def _is_id_like(series: pd.Series, name: str) -> bool:
    """启发式：几乎全唯一的 object 列（如 patient_id）不参与插补。"""
    n = name.lower()
    if any(k in n for k in ("patient_id", "pat_id", "subject_id", "sample_id")):
        return True
    non_na = series.dropna()
    if len(non_na) == 0:
        return True
    nuniq = non_na.nunique()
    if nuniq >= IMPUTE_CAT_MAX_UNIQUE and nuniq / len(non_na) >= IMPUTE_CAT_MAX_UNIQUE_RATIO:
        return True
    if nuniq == len(non_na) and len(non_na) > 10:
        return True
    return False


def _detect_categorical_cols(df: pd.DataFrame, group_col: str,
                             explicit: Optional[Sequence[str]] = None) -> List[str]:
    """选取可编码插补的分类列（object / category / bool）。"""
    if explicit is not None:
        missing = [c for c in explicit if c not in df.columns]
        if missing:
            raise ValueError(f"categorical_cols not in data: {missing}")
        return list(explicit)

    cats: List[str] = []
    for c in df.columns:
        if c == group_col:
            continue
        s = df[c]
        if pd.api.types.is_bool_dtype(s) or isinstance(s.dtype, pd.CategoricalDtype):
            cats.append(c)
            continue
        if pd.api.types.is_object_dtype(s) or pd.api.types.is_string_dtype(s):
            if not _is_id_like(s, c):
                cats.append(c)
    return cats


def _encode_categoricals(
    df: pd.DataFrame, cat_cols: Sequence[str]
) -> Tuple[pd.DataFrame, Dict[str, Dict[int, object]]]:
    """
    将分类列编码为 float（缺失保持 NaN）。
    返回 (工作副本, {col: {code: label}})。
    """
    work = df.copy()
    code_to_label: Dict[str, Dict[int, object]] = {}
    for c in cat_cols:
        s = work[c]
        labels = sorted(s.dropna().unique(), key=lambda x: str(x))
        label_to_code = {lab: i for i, lab in enumerate(labels)}
        code_to_label[c] = {i: lab for lab, i in label_to_code.items()}
        work[c] = s.map(label_to_code).astype("float64")
    return work, code_to_label


def _decode_categoricals(
    df: pd.DataFrame, code_to_label: Dict[str, Dict[int, object]]
) -> pd.DataFrame:
    """插补后的浮点编码 → 就近整数 → 原类别标签。"""
    out = df.copy()
    for c, mapping in code_to_label.items():
        if c not in out.columns:
            continue
        max_code = max(mapping.keys()) if mapping else 0
        vals = pd.to_numeric(out[c], errors="coerce")
        rounded = vals.round().clip(lower=0, upper=max_code)
        decoded = rounded.map(lambda x: mapping.get(int(x)) if pd.notna(x) else np.nan)
        out[c] = decoded
    return out


def _decimal_places(x: object, max_places: int = 12) -> int:
    """
    有效小数位数：能在浮点容差内还原该值的最少小数位；整数为 0。
    上限 max_places，避免 float64 二进制噪声被算成 15 位。
    """
    if x is None or (isinstance(x, float) and np.isnan(x)) or pd.isna(x):
        return 0
    try:
        fv = float(x)
    except (TypeError, ValueError):
        return 0
    if not np.isfinite(fv):
        return 0
    tol = max(1e-12, abs(fv) * 1e-12)
    if abs(fv - round(fv)) <= tol:
        return 0
    for d in range(1, max_places + 1):
        if abs(fv - round(fv, d)) <= tol:
            return d
    return max_places


def mean_decimal_places(series: pd.Series, max_places: int = 12) -> int:
    """非缺失观测小数位数的均值，四舍五入为整数 ndigits。无观测时返回 0。"""
    obs = series.dropna()
    if len(obs) == 0:
        return 0
    decs = [_decimal_places(v, max_places=max_places) for v in obs.to_numpy()]
    return int(round(float(np.mean(decs))))


def apply_decimal_alignment(
    original: pd.DataFrame,
    imputed: pd.DataFrame,
    num_cols: Sequence[str],
    verbose: bool = False,
) -> Tuple[pd.DataFrame, Dict[str, int]]:
    """
    仅对「原表缺失、插补后非缺失」的格子 round 到该列观测小数位数均值；
    原非缺失格保持 original 原值。
    返回 (对齐后的 DataFrame, {col: ndigits})。
    """
    out = imputed.copy()
    ndigits_map: Dict[str, int] = {}
    for c in num_cols:
        if c not in original.columns or c not in out.columns:
            continue
        miss = original[c].isna()
        if not miss.any():
            ndigits_map[c] = mean_decimal_places(original[c])
            continue
        nd = mean_decimal_places(original[c])
        ndigits_map[c] = nd
        out.loc[~miss, c] = original.loc[~miss, c]
        filled = miss & out[c].notna()
        if filled.any():
            vals = pd.to_numeric(out.loc[filled, c], errors="coerce")
            out.loc[filled, c] = vals.round(nd)
        if verbose and filled.any():
            print(f"    decimal align {c}: ndigits={nd}, n_filled={int(filled.sum())}")
    return out, ndigits_map


def _simple_group_impute(
    work: pd.DataFrame,
    g_mask: pd.Series,
    cols: Sequence[str],
    how: str,
) -> None:
    """组内 median/mean 就地填充（仅填缺失）。"""
    g = work.loc[g_mask, list(cols)]
    if how == "median":
        fill = g.median(numeric_only=True)
    else:
        fill = g.mean(numeric_only=True)
    for c in cols:
        if c not in fill.index:
            continue
        miss = g_mask & work[c].isna()
        if miss.any() and pd.notna(fill[c]):
            work.loc[miss, c] = fill[c]


def _build_estimator(
    method: str,
    seed: int,
    mf_n_trees: int,
    mf_max_depth: Optional[int],
    mf_max_features: Union[str, float, int, None],
):
    if method == "mice":
        return BayesianRidge()
    # missForest
    return RandomForestRegressor(
        n_estimators=mf_n_trees,
        max_depth=mf_max_depth,
        max_features=mf_max_features,
        random_state=seed,
        n_jobs=-1,
    )


def z_impute(data: Union[str, pd.DataFrame], sheet: Optional[str] = None,
             group_col: str = IMPUTE_GROUP_COL, method: str = "mice",
             seed: int = IMPUTE_SEED, max_iter: int = IMPUTE_MAX_ITER,
             mf_n_trees: int = IMPUTE_MF_N_TREES, output: Optional[str] = None,
             verbose: bool = True,
             include_categorical: bool = False,
             categorical_cols: Optional[Sequence[str]] = None,
             align_decimals: bool = True,
             n_nearest_features: Optional[int] = IMPUTE_N_NEAREST,
             mf_max_depth: Optional[int] = IMPUTE_MF_MAX_DEPTH,
             mf_max_features: Union[str, float, int, None] = IMPUTE_MF_MAX_FEATURES,
             skip_complete: bool = True) -> Optional[pd.DataFrame]:
    """
    对 DataFrame 中每个 Group 内的列执行缺失值插补，各组独立处理。

    参数
    ----
    data                 : DataFrame 或 Excel 文件路径
    sheet                : 当 data 为文件路径时必须提供的工作表名
    group_col            : 分组列名（各组独立插补）
    method               : "median" | "mean" | "mice"（默认，快）| "missForest"（慢、非线性）
    include_categorical  : True 时对分类列先编码再插补再还原
    categorical_cols     : 显式指定分类列；None 时自动检测 object/category
    align_decimals       : True 时，新插补值小数位 = 该列非缺失观测小数位均值
    n_nearest_features   : missForest/mice 每列预测变量数；None=用全部列（更慢）
    mf_n_trees           : missForest 树数（默认 30）
    mf_max_depth         : RF 深度上限（默认 8）
    mf_max_features      : RF max_features（默认 "sqrt"）
    skip_complete        : True 时完整列不做迭代目标（加速）
    output               : 可选，插补结果写出的 Excel 路径
    """
    method = _normalize_method(method)

    if isinstance(data, str):
        if sheet is None:
            raise ValueError("'sheet' must be provided when 'data' is a file path.")
        df = pd.read_excel(data, sheet_name=sheet)
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise TypeError("'data' must be a DataFrame or a file path.")

    if group_col not in df.columns:
        raise ValueError(f"group_col '{group_col}' not found in columns: {list(df.columns)}")

    if verbose:
        print(f"=== {method} Imputation ===\nData: {df.shape[0]} rows x {df.shape[1]} cols")
        print(f"Group column: {group_col}")
        if method in ("mice", "missForest"):
            print(
                f"  max_iter={max_iter}, n_nearest={n_nearest_features}, "
                f"skip_complete={skip_complete}"
                + (
                    f", trees={mf_n_trees}, max_depth={mf_max_depth}"
                    if method == "missForest"
                    else ""
                )
            )

    # —— 数值列 ——
    num_cols = [c for c in df.columns
                if pd.api.types.is_numeric_dtype(df[c]) and c != group_col]

    # —— 分类列（可选）——
    cat_cols: List[str] = []
    code_to_label: Dict[str, Dict[int, object]] = {}
    work = df.copy()
    if include_categorical or categorical_cols is not None:
        cat_cols = _detect_categorical_cols(work, group_col, categorical_cols)
        if cat_cols:
            work, code_to_label = _encode_categoricals(work, cat_cols)
            if verbose:
                print(f"Categorical columns encoded: {cat_cols}")

    impute_cols = num_cols + cat_cols
    if not impute_cols:
        if verbose:
            print("No imputable columns, nothing to do.")
        return None

    if verbose:
        before_miss = {c: int(work[c].isna().sum()) for c in impute_cols if work[c].isna().any()}
        print(f"Impute columns: {len(impute_cols)} "
              f"(numeric={len(num_cols)}, categorical={len(cat_cols)})")
        if before_miss:
            # 避免刷屏：只打印缺失列数与总缺失格
            n_cells = sum(before_miss.values())
            print(f"Missing before: {len(before_miss)} cols, {n_cells} cells")

    groups = sorted(work[group_col].dropna().unique(), key=str)
    if verbose:
        print(f"Groups: {len(groups)} → {groups}")

    for gi, gv in enumerate(groups):
        g_mask = work[group_col] == gv
        g_data = work.loc[g_mask, impute_cols]
        n_miss = int(g_data.isna().sum().sum())
        if n_miss == 0:
            if verbose:
                print(f"  Group={gv} (n={int(g_mask.sum())}): no missing, skip")
            continue

        valid_cols = [c for c in impute_cols
                      if g_data[c].notna().sum() >= IMPUTE_MIN_NONMISSING
                      and g_data[c].dropna().nunique() >= IMPUTE_MIN_UNIQUE]
        if not valid_cols:
            if verbose:
                print(f"  Group={gv}: {n_miss} missing, insufficient variance")
            continue

        skipped = [c for c in impute_cols if c not in valid_cols and g_data[c].isna().any()]
        if verbose:
            msg = (
                f"  Group={gv} (n={int(g_mask.sum())}): "
                f"imputing {n_miss} values in {len(valid_cols)} cols"
            )
            if skipped:
                msg += f" (skip low-info: {len(skipped)} cols)"
            print(msg)

        # —— 快速路径：组内 median / mean ——
        if method in ("median", "mean"):
            _simple_group_impute(work, g_mask, valid_cols, how=method)
            continue

        # —— mice / missForest ——
        n_feat = len(valid_cols)
        nn = n_nearest_features
        if nn is not None and n_feat > 1:
            nn = int(min(nn, n_feat - 1))
            if nn < 1:
                nn = None

        estimator = _build_estimator(
            method, seed + gi, mf_n_trees, mf_max_depth, mf_max_features
        )
        imputer = IterativeImputer(
            estimator=estimator,
            max_iter=max_iter,
            random_state=seed + gi,
            n_nearest_features=nn,
            skip_complete=skip_complete,
            # 放宽 tol 可略早停；不改变算法主路径
            tol=1e-3,
        )
        try:
            imputed_vals = imputer.fit_transform(g_data[valid_cols])
            work.loc[g_mask, valid_cols] = imputed_vals
        except Exception as e:
            if verbose:
                print(f"    {method} error: {e}")
                print("    fallback → group median")
            _simple_group_impute(work, g_mask, valid_cols, how="median")

    # 还原分类列标签
    if code_to_label:
        work = _decode_categoricals(work, code_to_label)

    # 小数位对齐
    if align_decimals and num_cols:
        if verbose:
            print("Aligning imputed decimals to mean of observed decimal places…")
        work, _nd_map = apply_decimal_alignment(df, work, num_cols, verbose=False)
        if verbose:
            sample = {c: _nd_map[c] for c in list(_nd_map)[:8]}
            print(f"  ndigits sample (first cols): {sample}")

    result = work

    if verbose:
        after_miss = {c: int(result[c].isna().sum()) for c in impute_cols if result[c].isna().any()}
        if after_miss:
            print("Missing after:", after_miss)
        else:
            print("Missing after: none in imputable columns")

    if output is not None:
        result.to_excel(output, index=False)
        if verbose:
            print(f"Done → {output}")

    return result

# =============================================================================
# Standalone: use impute_excel.py CLI
# =============================================================================
if __name__ == "__main__":
    print(
        "Use: python impute_excel.py --input data.xlsx --sheet cln --group Group --method mice\n"
        "Or:  from u_impute import z_impute"
    )
