#!/usr/bin/env python3
"""u_outlier_detection.py - outlier detection (template)
Purpose: Detect outliers from clinical reference ranges + SD
Deps: pandas, numpy
Usage: edit config, then run
"""

import os

import pandas as pd
import numpy as np

# ==================== Config (soft-coded, top) ====================
DATA_FILE = os.environ.get("DATA_FILE", r"path/to/data.xlsx")  # input data
OUTPUT_FILE = os.environ.get("OUTPUT_FILE", r"path/to/data_outliers.xlsx")  # output
GROUP_COL = "Group"                              # group column (optional, may be empty)
START_COL = "E1"                                 # start column (Excel cell)
END_COL = "BD1"                                  # end column (Excel cell)
OUTLIER_METHOD = "both"                          # clinical / sd / both
SD_THRESHOLD = 3                                 # SD threshold
# ================================================================

# clinical reference ranges (marker -> (lo, hi))
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
    """Excel cell (e.. E1) → column index"""
    import re
    m = re.match(r"([A-Z]+)(\d+)", cell)
    col = 0
    for ch in m.group(1):
        col = col * 26 + (ord(ch) - ord("A") + 1)
    return col - 1


def detect_clinical(df, cols):
    """Detect outliers from clinical reference ranges"""
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    for col in cols:
        if col in CLINICAL_RANGES:
            lo, hi = CLINICAL_RANGES[col]
            flags[col] = (df[col] < lo) | (df[col] > hi)
    return flags


def detect_sd(df, cols, threshold=3):
    """Detect outliers from SD"""
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    for col in cols:
        mean = df[col].mean()
        std = df[col].std()
        if std > 0:
            flags[col] = (df[col] - mean).abs() > threshold * std
    return flags


def main():
    # load data
    df = pd.read_excel(DATA_FILE) if DATA_FILE.endswith(".xlsx") else pd.read_csv(DATA_FILE)

    # resolve column range
    start = excel_col_to_index(START_COL)
    end = excel_col_to_index(END_COL) + 1
    cols = df.columns[start:end]

    # detect outliers
    flags = pd.DataFrame(False, index=df.index, columns=cols)
    if OUTLIER_METHOD in ("clinical", "both"):
        flags |= detect_clinical(df, cols)
    if OUTLIER_METHOD in ("sd", "both"):
        flags |= detect_sd(df, cols, SD_THRESHOLD)

    # mark outliers (red=high, green=low)
    result = df.copy()
    for col in cols:
        if col in CLINICAL_RANGES:
            lo, hi = CLINICAL_RANGES[col]
            result.loc[df[col] > hi, col] = f"↑{df[col]}"  # high
            result.loc[df[col] < lo, col] = f"↓{df[col]}"  # low

    # output
    result.to_excel(OUTPUT_FILE, index=False)
    n_outliers = int(flags.sum().sum())
    print(f"✅ detection done; {n_outliers} outliers; wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()