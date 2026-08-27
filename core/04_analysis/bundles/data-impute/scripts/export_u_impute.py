#!/usr/bin/env python3
"""u_impute.py - 缺失值插补（模板）
功能：对临床数据执行缺失值插补（mice / mean / median）
依赖：pandas, numpy
用法：修改配置后运行
"""

import pandas as pd
import numpy as np

# ==================== 配置区（软编码，置顶） ====================
DATA_FILE = r"F:\Paper\SCH_barin\data_outliers.xlsx"  # 输入数据
OUTPUT_FILE = r"F:\Paper\SCH_barin\data_imputed.xlsx" # 输出
GROUP_COL = "Group"                              # 分组列（可选）
IMPUTE_METHOD = "mice"                           # mice / mean / median
IMPUTE_COLS = None                               # 指定列（None=全部数值列）
START_COL = 0                                    # 起始列索引
END_COL = None                                   # 结束列索引（None=末尾）
# ================================================================


def impute_mean_median(df, method="median"):
    """均值/中位数插补"""
    if method == "mean":
        return df.fillna(df.mean())
    elif method == "median":
        return df.fillna(df.median())
    return df


def impute_mice(df):
    """简化版 mice 插补（实际应使用 fancyimpute / miceforest）"""
    try:
        from fancyimpute import IterativeImputer
    except ImportError:
        print("⚠️ fancyimpute 未安装，使用中位数插补代替")
        return impute_mean_median(df, "median")

    # 保存非数值列
    num_cols = df.select_dtypes(include=[np.number]).columns
    non_num = df.drop(columns=num_cols)
    num_df = df[num_cols]

    imputer = IterativeImputer(max_iter=10, random_state=42)
    imputed = imputer.fit_transform(num_df)
    result = pd.DataFrame(imputed, columns=num_cols, index=df.index)
    return pd.concat([result, non_num], axis=1)


def main():
    # 读取数据
    if DATA_FILE.endswith(".xlsx"):
        df = pd.read_excel(DATA_FILE)
    else:
        df = pd.read_csv(DATA_FILE)

    # 选择列范围
    if IMPUTE_COLS is not None:
        cols = IMPUTE_COLS
    else:
        num_cols = df.select_dtypes(include=[np.number]).columns
        cols = num_cols[START_COL:END_COL]

    # 按组插补（如果指定 GROUP_COL）
    result = df.copy()
    if GROUP_COL and GROUP_COL in df.columns:
        for group in df[GROUP_COL].unique():
            mask = df[GROUP_COL] == group
            subset = df.loc[mask, cols]
            if IMPUTE_METHOD == "mice":
                imputed = impute_mice(subset)
            else:
                imputed = impute_mean_median(subset, IMPUTE_METHOD)
            result.loc[mask, cols] = imputed[cols]
    else:
        if IMPUTE_METHOD == "mice":
            result = impute_mice(df)
        else:
            result[cols] = impute_mean_median(df[cols], IMPUTE_METHOD)

    # 输出
    result.to_excel(OUTPUT_FILE, index=False)
    print(f"✅ 插补完成，已写入 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()