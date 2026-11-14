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

Thin contract for clean-data: scope, bans, phase names, and pointers. The house working method and the revision authority live in `02_data-processing/advanced/`; pack data (`references/`, `scripts/`) stays beside it as data.

**clean-data** front: research **clinical Excel/CSV** — headers, missingness, ID integrity, and cohort columns. Nested `impute/` points at the fill/outlier code in `{code_model_validation}`. Writing the workbook itself (formulas, styling, formatting) is ordinary `openpyxl` work — do it in the analysis script, not here.

Imaging data-availability statements live in `preprocess-imaging` [`data.md`](../preprocess-imaging/references/data.md), not here. Column semantics for ingest — 22 core columns, measured alias table, value enums, the six per-sheet questions — live in [`references/column-dictionary.md`](references/column-dictionary.md); the gates stay in this MODULE.

Tables that report **only aggregates** (n, mean(SD), AUC, sens/spec, P) are not clean-data input: reconstruct subject-level **synthetic** rows per [`restore-from-summary.md`](../../advanced/restore-from-summary.md).

## Mission

Turn one clinical workbook into an analysis-ready table whose header, ID, cohort and missingness are proven, not assumed; write the QC note that later stages rely on. It does not model, select, or report.

Out of scope: LASSO / nomogram / ROC / DCA (`stats-analysis`); fill/outlier implementation (`impute/`); formulas/styling; HIS/EMR credentials; reporting checklists.

## Input

Minimum: the workbook (xlsx/csv) + which sheet + the analysis unit (usually patient). The three required columns below must exist or be mapped by the user. If the split column exists but its semantics are unclear (training/test vs external validation), ask before touching it.

## Required columns

1. **Patient ID** — one identifier per analysis unit. Keep as text (`dtype={id_col: str}`) so leading zeros survive.
2. **Split / cohort** — `training` / `test`. **Validation = external only** (another centre, time, or device). Never carve a random slice of the same pool and call it validation. Never label the training set "Development set".
3. **Outcome** — the endpoint column used later. Do not recode it after seeing test AUC.

Optional but usual: site, timepoint, visit date, exclusion flag. Group-stratified impute also needs a group column ([`impute/`](impute/)).

## Workflow (decision nodes)

1. **Identify** file, sheet, analysis unit and the three required columns.
2. **Header pass**: header = raw first data row after dropping title/spacer rows; unique non-empty names; units recorded; normalise before judging (`\xa0`/spaces, full-width, peel units off the name, Chinese name wins on variants); never merge semantically different columns; name empty cells explicitly (`col_<i>`). Check the 22-column dictionary.
3. **Missingness inventory before imputing**: columns with NA, total missing cells, block vs scattered; missing rate first, cause second (a fixable block layout is not missing data).
4. **ID pass**: unique at the declared unit; duplicates stop and are resolved, never averaged; joins on ID (+timepoint), never row index; name alone is never a key.
5. **Split / leakage pass**: split patients, not rows/lesions/slices; after the split, every data-dependent step fits on training only; validation means external.
6. **Write the QC note** (shape, dtypes, missingness table, ID verdict, split verdict), then hand off: fill/outliers → `impute/`; modelling → `02_data-processing`.

## Constraints (never)

- **No LASSO / paper model fitting** here — preparation only.
- **No HIS login** and no hospital-system passwords, tokens, or VPN secrets in this pack or in table files.
- Never invent or "repair" a missing value, ID, or cohort membership to make the table tidy.
- Never force a person onto every row; the person-ID column may legitimately be NULL in most sheets.
- Never drop or fill columns on a modeller's NA threshold here; that decision belongs to the modelling pipeline.
- Never treat imaging `data.md` as this fine id's body.
- Formula recalc / error scan on a hand-built workbook goes to `{code_model_validation}\recalc_xlsx.py`, not a manual recheck.

## Output and handoff

- Analysis-ready table + short QC note: sheet/shape/dtypes, header verdict, units, missingness table (block vs scattered), ID uniqueness, split semantics.
- Handoff: missing/outlier implementation → `clean-data` `impute/`; radiomics/leakage audit on feature matrices → `stats-analysis`; imaging I/O + availability statements → `preprocess-imaging`; reporting checklists → `05_manuscript/qc/check-reporting/`.
