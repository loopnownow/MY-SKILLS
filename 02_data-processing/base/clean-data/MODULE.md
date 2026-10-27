---
name: "clean-data"
domain: "02_data-processing"
trigger: ["Excel", "CSV", "临床数据", "表头", "缺失值", "ID", "队列"]
inputs: ["clinical_table"]
outputs: ["qc_notes", "analysis_ready_table"]
quality_control: "headers; missingness inventory; unique patient ID; patient-level split"
owner: "02_data-processing/base/clean-data/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Clinical tables (Excel / CSV)

**clean-data** front: research **clinical Excel/CSV** — headers, missingness, ID integrity, and
cohort columns. Nested `impute/` points at the fill/outlier code in `{code_model_validation}`.
Writing the workbook itself (formulas, styling, formatting) is ordinary `openpyxl` work — do it in
the analysis script, not here.

Imaging data-availability statements live in `imaging-io` [`data.md`](../imaging-io/references/data.md),
not here.

## Scope

| In | Out |
|---|---|
| Header QC, units, duplicate/empty column names | LASSO, nomogram, ROC/DCA (`meta-analysis` / `model-evaluation`) |
| Missingness inventory (block vs scattered) | Fill/outlier **implementation** → [`impute/`](impute/) |
| Patient ID uniqueness and join keys | HIS login, HIS passwords, EMR credentials |
| Cohort / split columns (training / test; validation = external only) | Naming the training set "Development set" |
| Patient-level leakage check on the table | Radiomics extraction (`stats-analysis`) |
| | Formula recalc / error scan on a hand-built workbook → `{code_model_validation}\recalc_xlsx.py` |
| | Reporting checklists CLAIM/TRIPOD/CLEAR → `check-reporting` |

## Required columns

Every analysis table must name (or the user must map) these three:

1. **Patient ID** — one identifier per analysis unit (usually one row per patient). Keep as text.
2. **Split / cohort** — `training` / `test`. **Validation = external only** (another centre, time,
   or device). Do not carve a random slice of the same pool and call it validation. Never label
   the training set **Development set**.
3. **Outcome** — the endpoint column used later in `04-*`. Do not recode it after seeing test AUC.

Optional but usual: site, timepoint, visit date, exclusion flag. Group-stratified impute also
needs a group column (see [`impute/`](impute/)).

## Header QC

Before any fill or model:

1. Row 1 is the header. No stacked/merged title rows that `pandas` will treat as data.
2. Headers unique and non-empty. Rename collisions (`x`, `x.1`) explicitly.
3. Units in the header or a documented units row — do not silently mix mg/dL and mmol/L.
4. Read IDs as string (`dtype={id_col: str}`) so leading zeros survive.
5. Record sheet name, `shape`, dtypes, and a 5-row preview.

## Missingness

Inventory **before** imputing:

- n columns with any NA, total missing cells, block vs scattered (whole modality missing vs holes).
- Do not drop columns here because a modeller's NA threshold lives in the modelling pipeline.
- Do not fill from the grand mean across outcome groups.

Handoff implementation (group-stratified mice/median/missForest, decimal alignment, backup/QC)
→ [`impute/MODULE.md`](impute/MODULE.md).

## ID integrity

- IDs unique at the declared unit (patient, or patient×timepoint if longitudinal and documented).
- Duplicate IDs → stop and resolve; do not average rows unless the user asks.
- Do not use Name/ID as a numeric feature. Do not impute ID.
- Joins to imaging or feature tables are on patient ID (and timepoint if needed), never on row
  index.

## Leakage / split integrity (patient-level)

1. Split **patients**, not rows/lesions/slices. The same patient must not appear in training and
   test.
2. After the split is locked, any data-dependent step (impute, scaler, selection) fits on
   **training** only, then transforms test. The current impute CLI fills the whole table by group;
   post-split use needs a custom call (see impute MODULE).
3. `validation` in this pack means **external** (held-out site/time/device), not a third random
   fold of the development pool.
4. Do not rename training as Development set in column values, filenames, or Methods.

## What not to do

- **No LASSO / paper model fitting** here — that is `meta-analysis` / `model-evaluation` /
  `stats-analysis` (preparation only).
- **No HIS login** and no hospital-system passwords, tokens, or VPN secrets in this pack or in
  table files.
- **No financial-model color convention as the lab default** (blue RGB 0,0,255 inputs, yellow
  assumption cells, 10-K source comments). This is a clinical-table pack; those conventions came
  from a corporate-finance template and were removed on 2026-10-27.
- Do not treat imaging `data.md` as this fine id's body.

## Nested packs

| Path | Role |
|---|---|
| [`impute/`](impute/) | Group-stratified missing/outlier contract; code in `{code_model_validation}` |

## Workflow

1. Identify the file (xlsx/csv), sheet, and the three required columns.
2. Header QC + ID uniqueness + missingness inventory. Write a short QC note.
3. Confirm split column semantics (training/test; validation only if external).
4. If fill/outliers are requested → `impute/`. If a hand-built workbook has formulas, recalculate and scan it with `{code_model_validation}\recalc_xlsx.py`.
5. Hand modelling to `02_data-processing`. Do not fit LASSO here.

## Handoffs

- Missing/outlier implementation → `clean-data` `impute/`
- Formula recalc / error scan on a hand-built workbook → `{code_model_validation}\recalc_xlsx.py`
- Imaging I/O + availability statements → `imaging-io` (including `data.md`)
- Radiomics / leakage audit on feature matrices → `stats-analysis`
- Modelling / calibration / DCA → `meta-analysis` / `model-evaluation`
- Reporting checklists → `check-reporting`
