#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
impute_excel.py — 分组缺失值插补 CLI（data-impute skill）

用法示例:
    python impute_excel.py --input data.xlsx --sheet cln --group Group --method mice
    python impute_excel.py --input data.xlsx --sheet 0 --method median --output out.xlsx
    python impute_excel.py --input data.xlsx --all-sheets --method mice

依赖: pandas, openpyxl, numpy, scikit-learn
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import List, Optional

import pandas as pd

# 同目录 u_impute
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from u_impute import mean_decimal_places, z_impute  # noqa: E402


def _resolve_sheets(path: Path, sheet: Optional[str], all_sheets: bool) -> List[str]:
    xl = pd.ExcelFile(path)
    if all_sheets:
        return list(xl.sheet_names)
    if sheet is None:
        return [xl.sheet_names[0]]
    # numeric index
    if sheet.isdigit():
        idx = int(sheet)
        return [xl.sheet_names[idx]]
    if sheet not in xl.sheet_names:
        raise ValueError(f"sheet {sheet!r} not in {xl.sheet_names}")
    return [sheet]


def _qc_frame(original: pd.DataFrame, imputed: pd.DataFrame, group_col: str) -> pd.DataFrame:
    num_cols = [
        c
        for c in original.columns
        if pd.api.types.is_numeric_dtype(original[c]) and c != group_col
    ]
    rows = []
    for c in num_cols:
        nb = int(original[c].isna().sum())
        na = int(imputed[c].isna().sum()) if c in imputed.columns else -1
        if nb == 0 and na == 0:
            continue
        rows.append(
            {
                "column": c,
                "n_miss_before": nb,
                "n_miss_after": na,
                "n_filled": nb - na if na >= 0 else None,
                "ndigits_mean_obs": mean_decimal_places(original[c]),
            }
        )
    if not rows:
        return pd.DataFrame(
            columns=["column", "n_miss_before", "n_miss_after", "n_filled", "ndigits_mean_obs"]
        )
    return pd.DataFrame(rows).sort_values(
        ["n_miss_before", "column"], ascending=[False, True]
    ).reset_index(drop=True)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Group-stratified missing-value imputation")
    p.add_argument("--input", "-i", required=True, help="Input Excel path")
    p.add_argument("--output", "-o", default=None, help="Output Excel (default: overwrite input)")
    p.add_argument("--sheet", "-s", default=None, help="Sheet name or 0-based index (default: first)")
    p.add_argument("--all-sheets", action="store_true", help="Impute every sheet that has group_col")
    p.add_argument("--group", "-g", default="Group", help="Group column name (default: Group)")
    p.add_argument(
        "--method",
        "-m",
        default="mice",
        choices=["median", "mean", "mice", "missForest"],
        help="Imputation method (default: mice)",
    )
    p.add_argument("--seed", type=int, default=66)
    p.add_argument("--max-iter", type=int, default=10)
    p.add_argument("--mf-trees", type=int, default=30, help="missForest n_estimators")
    p.add_argument("--n-nearest", type=int, default=32, help="n_nearest_features; 0 = all")
    p.add_argument("--no-align-decimals", action="store_true", help="Disable decimal alignment")
    p.add_argument("--include-categorical", action="store_true")
    p.add_argument(
        "--backup",
        default=None,
        help="Backup path for original file (default: <stem>_pre_impute.xlsx beside input)",
    )
    p.add_argument("--no-backup", action="store_true")
    p.add_argument("--no-qc", action="store_true", help="Do not write impute_qc sheet(s)")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args(argv)

    src = Path(args.input).resolve()
    if not src.exists():
        print(f"ERROR: not found: {src}", file=sys.stderr)
        return 1

    out = Path(args.output).resolve() if args.output else src
    sheets = _resolve_sheets(src, args.sheet, args.all_sheets)
    nn = None if args.n_nearest == 0 else args.n_nearest
    verbose = not args.quiet

    # backup
    if not args.no_backup:
        bak = Path(args.backup) if args.backup else src.with_name(f"{src.stem}_pre_impute{src.suffix}")
        if not bak.exists():
            bak.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, bak)
            if verbose:
                print(f"backup → {bak}")
        elif verbose:
            print(f"backup exists (kept): {bak}")

    # load all original sheets to preserve non-target sheets
    xl = pd.ExcelFile(src)
    all_raw = {name: pd.read_excel(src, sheet_name=name) for name in xl.sheet_names}

    written = {}
    qc_frames = {}
    for sh in sheets:
        df = all_raw[sh]
        if args.group not in df.columns:
            if verbose:
                print(f"skip sheet {sh!r}: no group col {args.group!r}")
            continue
        n_miss0 = int(df.isna().sum().sum())
        if n_miss0 == 0:
            if verbose:
                print(f"skip sheet {sh!r}: no missing")
            written[sh] = df
            continue

        if verbose:
            print(f"\n--- sheet {sh!r} miss_cells={n_miss0} ---")

        imputed = z_impute(
            df,
            group_col=args.group,
            method=args.method,
            seed=args.seed,
            max_iter=args.max_iter,
            mf_n_trees=args.mf_trees,
            n_nearest_features=nn,
            align_decimals=not args.no_align_decimals,
            include_categorical=args.include_categorical,
            verbose=verbose,
        )
        if imputed is None:
            print(f"ERROR: z_impute returned None for sheet {sh}", file=sys.stderr)
            return 2
        written[sh] = imputed
        if not args.no_qc:
            qc_frames[sh] = _qc_frame(df, imputed, args.group)

    # merge: updated sheets + untouched sheets
    final = dict(all_raw)
    final.update(written)

    out.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(out, engine="openpyxl") as w:
        for name, frame in final.items():
            # Excel sheet name max 31 chars
            safe = str(name)[:31]
            frame.to_excel(w, sheet_name=safe, index=False)
        if not args.no_qc and qc_frames:
            if len(qc_frames) == 1:
                next(iter(qc_frames.values())).to_excel(w, sheet_name="impute_qc", index=False)
            else:
                for sh, qc in qc_frames.items():
                    qname = f"qc_{sh}"[:31]
                    qc.to_excel(w, sheet_name=qname, index=False)

    if verbose:
        print(f"\nDone → {out}")
        for sh, frame in written.items():
            print(f"  {sh}: shape={frame.shape}, miss={int(frame.isna().sum().sum())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
