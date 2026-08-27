#!/usr/bin/env python3
"""u_outlier_detection.py - 异常值检测（模板）
功能：基于临床参考范围 + SD 检测异常值
依赖：pandas, numpy
用法：修改配置后运行
"""

import pandas as pd
import numpy as np

# ==================== 配置区（软编码，置顶） ====================
DATA_FILE = r"F:\Paper\SCH_barin\data.xlsx"     # 输入数据
OUTPUT_FILE = r"F:\Paper\SCH_barin\data_outliers.xlsx"  # 输出
GROUP_COL = "Group"                              # 分组列（可选，可为空）
START_COL = "E1"                                 # 起始列（Excel 单元格）
END_COL = "BD1"                                  # 结束列（Excel 单元格）
OUTLIER_METHOD = "both"                          # clinical / sd / both
SD_THRESHOLD = 3                                 # SD 阈值
# ================================================================

# 临床参考范围库（指标名 -> (下限, 上限)）
CLINICAL_RANGES = {
    "White Blood Cell Count WBC (10^9/L)": (3.5, 9.5),
    "Hemoglobin Hb (g/L)": (130, 175),
    "Platelet Count PLT (10^9/L)": (125, 350),
    "Alanine Aminotransferase ALT (U/L)": (9, 50),
    "Aspartate Aminotransferase AST (U/L)": (15, 40),
    "Creatinine Cr (umol/L)": (57, 111),
    "Urea Nitrogen BUN (mmol/L)": (3.1, 8.0),
    "Glucose Glu (mmol/L)": (3.9, 6.1),
    "Total Cholesterol TC (mmol/l)": (2.8, 5.2),
    "Triglycerides TG (mmol/l)": (0.4, 1.7),
    "C-Reactive Protein CRP (mg/L)": (0, 10),
}


def excel_col_to_index(cell):
    """Excel 单元格（如 E1）转列索引"""
    import re
    m = re.match(r"([A-Z]+)(\d+)", cell)
    col = 0
    for ch in m.group(1):
        col = col * 26 + (ord(ch) - ord("A") + 1)
    return col - 1


def detect_clinical(df, cols):
    """基于临床参考范围检测异常值"""
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    for col in cols:
        if col in CLINICAL_RANGES:
            lo, hi = CLINICAL_RANGES[col]
            flags[col] = (df[col] < lo) | (df[col] > hi)
    return flags


def detect_sd(df, cols, threshold=3):
    """基于 SD 检测异常值"""
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    for col in cols:
        mean = df[col].mean()
        std = df[col].std()
        if std > 0:
            flags[col] = (df[col] - mean).abs() > threshold * std
    return flags


def main():
    # 读取数据
    df = pd.read_excel(DATA_FILE) if DATA_FILE.endswith(".xlsx") else pd.read_csv(DATA_FILE)

    # 确定列范围
    start = excel_col_to_index(START_COL)
    end = excel_col_to_index(END_COL) + 1
    cols = df.columns[start:end]

    # 检测异常值
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    if OUTLIER_METHOD in ("clinical", "both"):
        flags |= detect_clinical(df, cols)
    if OUTLIER_METHOD in ("sd", "both"):
        flags |= detect_sd(df, cols, SD_THRESHOLD)

    # 标记异常值（红色升高，绿色降低）
    result = df.copy()
    for col in cols:
        if col in CLINICAL_RANGES:
            lo, hi = CLINICAL_RANGES[col]
            result.loc[df[col] > hi, col] = f"↑{df[col]}"  # 升高
            result.loc[df[col] < lo, col] = f"↓{df[col]}"  # 降低

    # 输出
    result.to_excel(OUTPUT_FILE, index=False)
    n_outliers = int(flags.sum().sum())
    print(f"✅ 检测完成，共 {n_outliers} 个异常值，已写入 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()