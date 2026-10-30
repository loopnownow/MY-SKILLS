---
name: "impute"
domain: "02_data-processing"
trigger: ["插补", "补缺失", "MICE", "按组填"]
inputs: ["excel_or_csv", "group_column"]
outputs: ["imputed_table", "impute_qc", "backup"]
tools: ["Python"]
quality_control: "group-stratified; observed cells unchanged; align_decimals"
owner: "02_data-processing/base/clean-data/impute/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Group-stratified missing-value imputation

Contract only for clean-data impute: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/pipeline.md`; pack data (`references/`, `scripts/`) stays beside it as data.

**Prose only — the code lives in `stats-analysis`.** This pack says when to impute, which
method, and what to check; `{code_stats}` runs it.

```text
{code_model_validation}\impute_excel.py   # CLI: backup, per-sheet run, impute_qc
{code_modules}\utils\u_impute.py          # z_impute core + decimal alignment
{code_modules}\utils\u_outlier_detection.py
```

`stats-analysis` is the script half of seat 02 (`MY-SKILLS` is prose only); do not copy these
files back into the skill tree, and do not edit the copy in a project.

Nested under `clean-data`. Not an analysis-domain pack.
Header / ID / cohort QC before fill → parent [`../MODULE.md`](../MODULE.md).
Formula recalc on a hand-built workbook → `{code_model_validation}\recalc_xlsx.py`. Do not treat this nested pack as modelling.

## When to use

| Trigger | Action |
|------|------|
| Excel/CSV + impute / fill missing / fill by group | Run the CLI or call `z_impute` |
| Block missingness (whole feature block NA) | Prefer `median` or `iterative` |
| missForest too slow | `iterative` / `median` or faster knobs |
| Imputed values should look like original decimals | keep `align_decimals=True` |

## Required references

| File | Content |
|------|------|
| [references/methods.md](references/methods.md) | Method choice, speed, missForest knobs |
| [references/checklist.md](references/checklist.md) | Before/after checks, Methods wording |

## STEP 0 — inspect (before imputing)

1. Read table: `shape`, sheets, group column levels and n
2. Missingness: n columns, total cells, block vs scattered
3. Confirm group column, method, overwrite vs new file, backup

Missing group column → **ask** or (discouraged) a dummy group. Do not silently fill with the grand mean.

## STEP 1 — method (default iterative)

**First decide: single or multiple imputation?** This is the choice that decides whether your
confidence interval is honest, and `iterative` alone does not make it for you.

| Your goal | Use | Why |
|---|---|---|
| Fill a table for downstream feature work (radiomics matrix, cohort table) | single, `iterative` / `median` | one completed table is what the modeller expects |
| Report an estimate with a CI (β, OR, HR, mean difference) | **multiple imputation + Rubin pooling** | single imputation under-states the SE and biases the point estimate |
| Report a model's AUC / calibration | MI, but see the caveat below | selection is inside the pipeline |

Single imputation treats filled values as observed, so the reported SE is too small and the
estimate is pulled toward the imputation model's fit. Measured on a 40-replication simulation
(n=150, 30 % MCAR in two predictors, β₁ true = 0.30):

```text
single (iterative)  bias +0.057  (+18.2 %, p = 0.002)   RMSE 0.121
multiple (m = 20)   bias +0.002  ( +0.6 %, p = 0.85)    RMSE 0.063
mean fraction of missing information (FMI) 0.33
```

That is why the lab rule is: **a Methods section that says "missing values were imputed" and then
reports a CI must say how many imputations and that they were pooled.** If it says only "MICE" or
"multiple imputation" while the numbers came from one table, the sentence is wrong.

Multiple imputation:

```bash
python "{code_model_validation}\mi_impute.py" draw --input data.xlsx --group Group -m 20 --out-dir mi/
# fit your model in each mi/imputed_XX.csv, collect term/estimate/variance rows, then:
python "{code_model_validation}\mi_impute.py" pool --table estimates.csv --n-complete 150
```

`pool` applies Rubin's rules with Barnard-Rubin degrees of freedom and reports FMI; FMI above
about 0.5 means the result still leans on the imputation model and should be stated as such.
`m = 20` is the usual floor; more is needed when FMI is high.

For the single-table case, method choice:

| Scene | method |
|------|--------|
| Default / many continuous features | **`iterative`** (alias `mice`) |
| Fast / block missing / interpretable | **`median`** |
| Paper specified missForest | `missForest` (accelerated defaults) |
| Symmetric approx. normal univariate | `mean` |

`mice` is a legacy alias for `iterative` — for **single** chained imputation. It is not multiple
imputation and must not be described as MICE / Rubin pooling in a paper.

## STEP 2 — run

### A. CLI

```bash
python "{code_model_validation}\impute_excel.py" \
  --input PATH/data.xlsx \
  --sheet cln \
  --group Group \
  --method iterative
```

| Flag | Default | Meaning |
|------|------|------|
| `--output` | overwrite input | output path |
| `--all-sheets` | off | every sheet with the group column |
| `--backup` | `<stem>_pre_impute.xlsx` | backup; `--no-backup` disables |
| `--no-align-decimals` | off | disable decimal alignment |
| `--n-nearest` | 32 | `0` = all features (slower) |
| `--mf-trees` | 30 | missForest only |
| `--include-categorical` | off | encode categoricals |

**An explicitly named group column always stratifies**, including one called `Group` or `outcome`.
The CLI passes `--group` through as an explicit name, so it always stratifies.

The outcome guard only applies when you name **no** column: `z_impute(df)` looks for a `Group`
column and skips it if the name looks outcome-like, because that column is usually `y` and
stratifying on the outcome writes it into the predictors. If your `Group` is a cohort label and the
outcome lives elsewhere, either name the column explicitly or pass `outcome_cols=["<outcome>"]`:

| Call | Behaviour |
|---|---|
| `z_impute(df, group_col="Group")` | stratifies — explicit wins, whatever the name |
| `z_impute(df)` | one pool if `Group` looks outcome-like, else stratifies |
| `z_impute(df, group_col=None)` | one pool, explicitly |
| `z_impute(df, outcome_cols=["Outcome"])` | `Group` is a cohort, not the outcome → stratifies |

### B. Python

```python
from modules.utils.u_impute import z_impute

out = z_impute(
    df,
    group_col="Group",
    method="iterative",      # median | mean | iterative (alias mice) | missForest
    align_decimals=True,
    # An explicit group_col always stratifies. To fill as one pool, pass group_col=None.
    verbose=True,
)
```

## STEP 3 — iron rules

1. **By group** — independent strata; no undeclared cross-group fill
2. **Observed cells unchanged** vs backup
3. **Decimals** — round new values to mean observed decimal places (`align_decimals=True`)
4. **Backup first** — default `*_pre_impute.xlsx`
5. **Write QC** — column / n_miss_before / n_miss_after / n_filled / ndigits_mean_obs
6. **Do not impute Name/ID**; group column is not a numeric feature
7. **Drop-column thresholds** belong to the modelling pipeline, not this CLI

## STEP 4 — accept

```text
numeric missing cells: N → 0 (or residual low-info cols only)
observed cells changed: 0
backup exists
impute_qc present
```

## Relation to modelling

Impute after merging clinical+features and **before** LASSO. After a train/test split, fit the
imputer on train and transform test (the CLI imputes the whole table by group; post-split use
needs a custom call). Modelling → `meta-analysis` / `stats-analysis`.

**Leakage note for multiple imputation.** The same train-only rule applies: fit the imputation
model on the training rows and draw from it for the test rows. Do not impute the pooled table and
then split — that leaks test-set distributions into training.

**Caveat when the number is a model metric.** Rubin's rules assume the within-imputation variance
is a complete-data variance. For a regression coefficient, mean, difference, OR or HR that holds.
For an AUC from a pipeline that runs LASSO and then evaluates, it does not: the between-imputation
variance would also have to carry the selection step, so a "pooled AUC" from Rubin's rules is not a
valid standard error. Options, in order of preference:

1. Run the **whole** pipeline (selection + fit + evaluate) inside each imputed dataset, then report
   the mean metric with its **range or 2.5th-97.5th percentile across imputations**, and say that
   is what you did. This is the Marshall et al. (2009) recommendation for prognostic modelling.
2. Report the metric from each imputation in a supplementary table and do not attach a CI.
3. Do not run MI for the model metric at all; keep MI for the coefficients you report alongside it.

Never average the AUCs and quote a Rubin-pooled CI for the average — that understates uncertainty
and is not what Rubin's rules estimate.
