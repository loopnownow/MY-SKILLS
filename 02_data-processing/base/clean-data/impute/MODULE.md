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

Thin contract for clean-data `impute/` (nested under `clean-data`): when to impute, which method class, and the iron rules. The house working method and the revision authority live in `02_data-processing/advanced/`; the engines live in `{code_stats}` and are not copied into the skill tree.

**Prose SSOT — the analysis code lives in `stats-analysis`.** This pack says when to impute, which method, and what to check; `{code_stats}` runs it:

```text
{code_model_validation}\impute_excel.py   # CLI: backup, per-sheet run, impute_qc
{code_model_validation}\mi_impute.py      # multiple imputation draw/pool
{code_modules}\utils\u_impute.py          # z_impute core + decimal alignment
{code_modules}\utils\u_outlier_detection.py
```

Do not copy these engines back into the skill tree, and do not treat a project-local fork as SSOT. Header / ID / cohort QC before fill → parent [`../MODULE.md`](../MODULE.md). Formula recalc on a hand-built workbook → `{code_model_validation}\recalc_xlsx.py`. Not an analysis-domain pack.

## Mission

Fill or flag missing cells on a clinical table without breaking the group structure, the observed decimals, or the leakage boundary; leave an auditable backup and a QC sheet.

Out of scope: modelling, LASSO, AUC/calibration (`stats-analysis` / `model-evaluation`); drop-column policy (modelling pipeline); header and ID QC (parent).

## Input

Minimum: one Excel/CSV table + a group column (cohort or split) + the intended use of the filled table. If the group column is missing, **ask**; a dummy group is a discouraged fallback. Never fill silently with a grand mean across outcome groups.

## Workflow (decision nodes)

1. **Inspect**: shape, sheets, group levels and n, missingness pattern (block vs scattered), overwrite vs new file, backup. Detail: [`references/checklist.md`](references/checklist.md).
2. **Decide single vs multiple** — this decides whether a CI is honest. Single fill for a completed table going into feature work; multiple imputation + Rubin pooling when a β/OR/HR/mean difference with CI is reported. `iterative` alone is single imputation; `mice` is its legacy alias and is **not** multiple imputation.
3. **Pick the single-table method**: default `iterative`; `median` for fast / block-missing / interpretable; `missForest` only if the paper specified it; `mean` only for a symmetric near-normal univariate. Detail and knobs: [`references/methods.md`](references/methods.md).
4. **Run** with an explicit group column (an explicitly named group always stratifies, whatever its name). CLI/Python entries: `{code_model_validation}\impute_excel.py`, `z_impute` in `{code_modules}\utils\u_impute.py`.
5. **Accept** only when the QC block passes: numeric missing cells → 0 (or residual low-information columns only), observed cells changed = 0, backup exists, `impute_qc` present.
6. **Hand off** filled table + QC to `stats-analysis`; post-split imputation fits on training rows only.

## Constraints (never)

- Never fill across groups without declaring it; independent strata only.
- Never change an observed cell; compare against the backup.
- Never round new values away from the observed decimal places (`align_decimals=True` default).
- Never skip the backup (default `<stem>_pre_impute.xlsx`).
- Never impute Name/ID, and never use the group column as a numeric feature.
- Never put drop-column thresholds in this pack; they belong to the modelling pipeline.
- **Leakage**: after a train/test split, fit the imputer on training and transform test. Do not impute the pooled table and then split; do not impute test rows from a model fitted on both.
- **MI reporting**: a Methods sentence that says only "MICE" or "multiple imputation" while the numbers came from one table is wrong. Say how many imputations and that they were pooled. For a model metric (e.g. AUC from a selection pipeline), do not attach a Rubin-pooled CI; run the whole pipeline inside each imputation and report the mean with the range or 2.5th-97.5th percentile across imputations.

## Output and handoff

- Imputed table (+ backup) and an `impute_qc` block: column / n_miss_before / n_miss_after / n_filled / ndigits_mean_obs.
- For MI: the `mi/` set, the estimates table, pooled estimates with FMI, and a Methods sentence naming `m` and pooling.
- Handoff: to `stats-analysis` for modelling; to `clean-data` parent when the problem was header/ID/cohort, not fill.
