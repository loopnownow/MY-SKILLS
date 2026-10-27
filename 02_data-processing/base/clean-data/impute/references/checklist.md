# Imputation task checklist

## Before run

- [ ] Confirm input path and sheet name (`cln` / `rad` / single table)
- [ ] Confirm group column (default `Group`) and levels (e.g. HC / SSD)
- [ ] Preview missingness: column count, total missing cells, block missing?
- [ ] Choose method (default `iterative`, alias `mice`; block missing may use `median`)
- [ ] Plan backup path (default `<stem>_pre_impute.xlsx`)

## During run

- [ ] Run `{code_model_validation}\impute_excel.py`, or call `z_impute` from `{code_modules}\utils\u_impute.py`
- [ ] Log shows per-group n, filled cell count, method params

## After run

- [ ] Numeric missing-cell count dropped (ideally 0; low-variance columns may remain)
- [ ] **Observed values unchanged** (non-missing positions match the backup)
- [ ] New values’ decimal places ≈ mean decimal places of that column’s observed values
- [ ] `impute_qc` (or equivalent table) has: column, miss_before/after, ndigits
- [ ] Do not narrate ID / label / group columns as predictors in a leakage write-up

## Methods-ready example sentence

Pick the one that matches what actually ran. They are not interchangeable.

**Single imputation** (one completed table; fine for feature work, not for a reported CI):

> Missing values were imputed within outcome groups using [group-wise median / chained equations with Bayesian ridge / missForest]. Observed values were left unchanged. Imputed continuous values were rounded to the mean number of decimal places of non-missing observations in the same variable.

**Multiple imputation** (m completed datasets, pooled — required when a CI is reported):

> Missing values were imputed within outcome groups using chained equations with Bayesian ridge, generating m = [20] completed datasets. Each model was fitted separately in every completed dataset and estimates were combined using Rubin's rules; the mean fraction of missing information was [0.33].

**Pipeline metric under MI** (AUC and similar) — say it plainly, do not quote a Rubin CI:

> Predictive performance was estimated by repeating the full modelling pipeline in each of the m = [20] completed datasets; we report the mean [AUC] with the range across imputations.

## Forbidden

- Fill outcome-related missingness with the global mean across Group (unless the user explicitly asks)
- Impute on the test set using information outside the training set (if train/test already split, **fit the imputer on train only** then transform test — current CLI is “whole table by group”; post-split needs an extra script)
- Overwrite the only original file with no backup
- Write “multiple imputation” or “MICE” while the numbers came from a single completed table
- Average AUCs across imputations and attach a Rubin-pooled CI to the average (Rubin's rules do not cover a pipelined metric; report the range instead)

## Forbidden

- Fill outcome-related missingness with the global mean across Group (unless the user explicitly asks)
- Impute on the test set using information outside the training set (if train/test already split, **fit the imputer on train only** then transform test — current CLI is “whole table by group”; post-split needs an extra script)
- Overwrite the only original file with no backup
