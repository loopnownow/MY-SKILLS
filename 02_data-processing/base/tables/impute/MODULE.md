---
name: "impute"
domain: "02_data-processing"
trigger: ["插补", "补缺失", "MICE", "按组填"]
inputs: ["excel_or_csv", "group_column"]
outputs: ["imputed_table", "impute_qc", "backup"]
tools: ["Python"]
quality_control: "group-stratified; observed cells unchanged; align_decimals"
owner: "02-data-processing/tables/impute/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Group-stratified missing-value imputation

Reusable CLI + library for **group-stratified imputation + decimal alignment + backup/QC**.
Nested under `02-tables`. Not an analysis-domain pack.

Header / ID / cohort QC before fill → parent [`../MODULE.md`](../MODULE.md).
Spreadsheet XML packing → [`../xlsx-office/`](../xlsx-office/). Do not treat this nested pack as modelling.

Lab pipeline copies of the imputer stay in **A personal**. Prefer this pack's `scripts/` unless
the user points at a project-local module.

## When to use

| Trigger | Action |
|------|------|
| Excel/CSV + 插补 / 补缺失 / 按组填 | Run CLI or `z_impute` |
| Block missingness (whole feature block NA) | Prefer `median` or `mice` |
| missForest too slow | `mice` / `median` or faster knobs |
| Imputed values should look like original decimals | keep `align_decimals=True` |

## Required references

| File | Content |
|------|------|
| [references/methods.md](references/methods.md) | Method choice, speed, missForest knobs |
| [references/checklist.md](references/checklist.md) | Before/after checks, Methods wording |

## Tools in this pack

```text
impute/
  MODULE.md
  scripts/u_impute.py      # z_impute core
  scripts/impute_excel.py  # Excel CLI
  scripts/u_outlier_detection.py
  scripts/export_u_impute.py
  references/
```

## STEP 0 — inspect (before imputing)

1. Read table: `shape`, sheets, group column levels and n
2. Missingness: n columns, total cells, block vs scattered
3. Confirm group column, method, overwrite vs new file, backup

Missing group column → **ask** or (discouraged) a dummy group. Do not silently fill with the grand mean.

## STEP 1 — method (default mice)

| Scene | method |
|------|--------|
| Default / many continuous features | **`mice`** |
| Fast / block missing / interpretable | **`median`** |
| Paper specified missForest | `missForest` (accelerated defaults) |
| Symmetric approx. normal univariate | `mean` |

## STEP 2 — run

### A. CLI

```bash
python scripts/impute_excel.py \
  --input PATH/data.xlsx \
  --sheet cln \
  --group Group \
  --method mice
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

### B. Python

```python
from u_impute import z_impute

out = z_impute(
    df,
    group_col="Group",
    method="mice",          # median | mean | mice | missForest
    align_decimals=True,
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
imputer on train and transform test (current CLI imputes the whole table by group; post-split
use needs a custom call). Modelling → `04-stats-models` / `02-radiomics-habitat`.
