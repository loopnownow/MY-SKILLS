# Imputation task checklist

## Before run

- [ ] Confirm input path and sheet name (`cln` / `rad` / single table)
- [ ] Confirm group column (default `Group`) and levels (e.g. HC / SSD)
- [ ] Preview missingness: column count, total missing cells, block missing?
- [ ] Choose method (default `mice`; block missing may use `median`)
- [ ] Plan backup path (default `<stem>_pre_impute.xlsx`)

## During run

- [ ] Run CLI or in-project `z_impute` / `scripts/impute_*.py`
- [ ] Log shows per-group n, filled cell count, method params

## After run

- [ ] Numeric missing-cell count dropped (ideally 0; low-variance columns may remain)
- [ ] **Observed values unchanged** (non-missing positions match the backup)
- [ ] New values’ decimal places ≈ mean decimal places of that column’s observed values
- [ ] `impute_qc` (or equivalent table) has: column, miss_before/after, ndigits
- [ ] Do not narrate ID / label / group columns as predictors in a leakage write-up

## Methods-ready example sentence

> Missing values were imputed within outcome groups using [group-wise median / MICE with Bayesian ridge / missForest]. Observed values were left unchanged. Imputed continuous values were rounded to the mean number of decimal places of non-missing observations in the same variable.

## Forbidden

- Fill outcome-related missingness with the global mean across Group (unless the user explicitly asks)
- Impute on the test set using information outside the training set (if train/test already split, **fit the imputer on train only** then transform test — current CLI is “whole table by group”; post-split needs an extra script)
- Overwrite the only original file with no backup
