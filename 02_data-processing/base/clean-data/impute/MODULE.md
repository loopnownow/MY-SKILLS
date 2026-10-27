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

| Scene | method |
|------|--------|
| Default / many continuous features | **`iterative`** (alias `mice`) |
| Fast / block missing / interpretable | **`median`** |
| Paper specified missForest | `missForest` (accelerated defaults) |
| Symmetric approx. normal univariate | `mean` |

`mice` is a legacy alias for `iterative` — it is **single** chained imputation, not multiple
imputation with Rubin pooling. Say so if the Methods section claims MICE.

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

The CLI passes `allow_outcome_stratify=True`, so an explicitly named `--group` is honored even
when the column is called `Group` / `outcome`. Calling `z_impute` directly does not — pass the
flag yourself.

### B. Python

```python
from modules.utils.u_impute import z_impute

out = z_impute(
    df,
    group_col="Group",
    method="iterative",      # median | mean | iterative (alias mice) | missForest
    align_decimals=True,
    allow_outcome_stratify=True,   # explicit stratum, not an outcome to strip
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
