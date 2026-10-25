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
cohort columns. Nested `impute/` implements fill/outlier. Nested `xlsx-office/` is spreadsheet
XML packing (Anthropic office/xlsx skill). This file is **not** that financial-model skill.

Imaging data-availability statements live in `imaging-io` [`data.md`](../imaging-io/references/data.md),
not here.

## Scope

| In | Out |
|---|---|
| Header QC, units, duplicate/empty column names | LASSO, nomogram, ROC/DCA (`meta-analysis` / `model-evaluation`) |
| Missingness inventory (block vs scattered) | Fill/outlier **implementation** → [`impute/`](impute/) |
| Patient ID uniqueness and join keys | HIS login, HIS passwords, EMR credentials |
| Cohort / split columns (training / test; validation = external only) | Naming the training set "Development set" |
| Patient-level leakage check on the table | Radiomics extraction (`analyze-stats`) |
| | Financial-model color scale as a lab default → [`xlsx-office/`](xlsx-office/) |
| | OOXML pack/unpack / LibreOffice recalc → [`xlsx-office/`](xlsx-office/) |
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
  `analyze-stats` (preparation only).
- **No HIS login** and no hospital-system passwords, tokens, or VPN secrets in this pack or in
  table files.
- **No financial-model color convention as the lab default** (blue RGB 0,0,255 inputs, yellow
  assumption cells, 10-K source comments). Those belong only to nested
  [`xlsx-office/`](xlsx-office/) when the user is actually building a financial workbook.
- Do not treat nested `xlsx-office/` or imaging `data.md` as this mount's body.

## Nested packs

| Path | Role |
|---|---|
| [`impute/`](impute/) | Group-stratified missing/outlier **implementation** |
| [`xlsx-office/`](xlsx-office/) | Spreadsheet XML packing, LibreOffice recalc, Anthropic xlsx skill (LICENSE.txt there) |

## Workflow

1. Identify the file (xlsx/csv), sheet, and the three required columns.
2. Header QC + ID uniqueness + missingness inventory. Write a short QC note.
3. Confirm split column semantics (training/test; validation only if external).
4. If fill/outliers are requested → `impute/`. If OOXML pack/recalc/financial model → `xlsx-office/`.
5. Hand modelling to `02_data-processing`. Do not fit LASSO here.

## Handoffs

- Missing/outlier implementation → `clean-data` `impute/`
- Spreadsheet XML packing / recalc / financial xlsx → `clean-data` `xlsx-office/`
- Imaging I/O + availability statements → `imaging-io` (including `data.md`)
- Radiomics / leakage audit on feature matrices → `analyze-stats`
- Modelling / calibration / DCA → `meta-analysis` / `model-evaluation`
- Reporting checklists → `check-reporting`
