# Imputation method choice

## Speed and use (rule-of-thumb, ~41×170 scale)

| method | Typical time | Mechanism | When |
|--------|--------------|-----------|------|
| `median` | ~0.2 s | Within-group median | Block missing (whole modality gone), need speed, interpretability |
| `mean` | ~0.2 s | Within-group mean | Near-symmetric continuous variables |
| `mice` | ~seconds | IterativeImputer + BayesianRidge | **Default**; joint modeling of continuous features |
| `missForest` | tens of seconds–minutes | IterativeImputer + RandomForest | Strong nonlinearity/interactions; when the paper method name requires it |

## missForest speed knobs

| Param | Default | Notes |
|------|---------|-------|
| `mf_n_trees` / `--mf-trees` | 30 | Often 100 historically; 30 usually enough |
| `max_iter` / `--max-iter` | 10 | Was 20 |
| `n_nearest_features` / `--n-nearest` | 32 | Per column, use only the k strongest predictors; `0`/`None`=all (slower) |
| `mf_max_depth` | 8 | Cap tree depth |
| `skip_complete` | True | Complete columns are not iteration targets |

Ultra-fast (quality second):

```text
--method missForest --mf-trees 10 --max-iter 5 --n-nearest 16
```

## Grouping rules

- **Must** stratify by outcome/cohort (`Group` / SSD·HC / case·control); do not fill missingness from the opposite group’s distribution.
- Within a group, if a column has < 2 non-missing or < 2 unique values → skip that column×group (or later median fallback).
- Whole column missing inside a group → cannot learn within-group; keep NaN or switch to a global strategy (this skill defaults to no cross-group fill).

## Block missing (e.g. DTI-only / IVIM-only)

Prefer `median` or `mice`. missForest gains little on “whole modality missing” and is slow.

## Categorical variables

- Default: impute numeric columns only.
- When needed: `--include-categorical` or `include_categorical=True` (encode → impute → nearest-round decode).
- ID-like columns (almost all unique) are skipped automatically.

## Decimal alignment (on by default)

For newly filled cells:

```text
ndigits = round(mean(effective decimal places of non-missing observations in that column))
imputed_cell = round(value, ndigits)
```

Original non-missing cells **keep their values**. Off: `--no-align-decimals`.
