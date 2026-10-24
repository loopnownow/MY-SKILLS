#!/usr/bin/env python3
"""u_impute.py - missing-value imputation (template)
Purpose: Impute missing clinical values (mice / mean / median)
Deps: pandas, numpy
Usage: edit config, then run
"""

import os

import pandas as pd
import numpy as np

# ==================== Config (soft-coded, top) ====================
DATA_FILE = os.environ.get("DATA_FILE", r"path/to/data.xlsx")  # input data
OUTPUT_FILE = os.environ.get("OUTPUT_FILE", r"path/to/data_imputed.xlsx")  # output
GROUP_COL = "Group"                              # group column (optional)
IMPUTE_METHOD = "mice"                           # mice / mean / median
IMPUTE_COLS = None                               # columns (None=all numeric)
START_COL = 0                                    # start column index
END_COL = None                                   # end column index (None=end)
# ================================================================


def impute_mean_median(df, method="median"):
    """mean/median imputation"""
    if method == "mean":
        return df.fillna(df.mean())
    elif method == "median":
        return df.fillna(df.median())
    return df


def impute_mice(df):
    """Simplified mice (prefer fancyimpute / miceforest in production)"""
    try:
        from fancyimpute import IterativeImputer
    except ImportError:
        print("⚠️ fancyimpute not installed; falling back to median")
        return impute_mean_median(df, "median")

    # keep non-numeric columns
    num_cols = df.select_dtypes(include=[np.number]).columns
    non_num = df.drop(columns=num_cols)
    num_df = df[num_cols]

    imputer = IterativeImputer(max_iter=10, random_state=42)
    imputed = imputer.fit_transform(num_df)
    result = pd.DataFrame(imputed, columns=num_cols, index=df.index)
    return pd.concat([result, non_num], axis=1)


def main():
    # load data
    if DATA_FILE.endswith(".xlsx"):
        df = pd.read_excel(DATA_FILE)
    else:
        df = pd.read_csv(DATA_FILE)

    # select column range
    if IMPUTE_COLS is not None:
        cols = IMPUTE_COLS
    else:
        num_cols = df.select_dtypes(include=[np.number]).columns
        cols = num_cols[START_COL:END_COL]

    # impute by group if GROUP_COL set
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

    # output
    result.to_excel(OUTPUT_FILE, index=False)
    print(f"✅ imputation done; wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()