# Clinical data extraction

## Purpose

Extract clinical data from txt/docx, labs, and pathology text already exported off the hospital machine. Use for lab extraction, pathology full text, clinical data extraction, discharge-summary extract. Dash/阴性 = Negative, not missing. Do not invent labs. HIS login clients stay on the hospital machine, never in git.

Personal layer: `02_data-processing/personal/extract.md` (moved from `clinical-data-extraction/SKILL.md`). Scripts stay under `{code_clean_data}\clinical-data-extraction\`, not in this repo.

## When it applies
- Extract patient info from .txt / .docx (name, sex, age, outpatient ID)
- Extract lab markers (CBC, liver/renal panels, glucose/lipids, tumor markers, etc.)
- Discharge summary / admission-note content extract
- Clinical merge, dedupe, formatting

HIS / PACS login and query clients run only on the hospital machine and **must not enter this repo**. This skill only handles text/docs already exported locally.

## Core workflow

### 1. Text/document extract
```
[Step 1] Walk all .txt / .docx under the directory
[Step 2] Match markers with the LAB_DICT keyword dictionary
[Step 3] Extract patient basics and lab results
[Step 4] Strip units; column names = English full name + abbreviation + (unit)
[Step 5] Write CSV / Excel
```

### 2. HIS client (not in A)

HIS login automation must not live in A. Hospital-system clients stay on the hospital machine and are never committed to git. Do not add Selenium/HIS URLs, usernames, or passwords here. Feed this skill exported txt/docx/CSV only.

## Key rules
1. **LAB_DICT**: all lab-marker keywords in one place for easy add/remove
2. **Soft-coding**: paths, keywords, and output files as top-level config
3. **Units**: strip units from values; put them in the column name
4. **Checkpoint resume**: after a query/extract interrupt, continue from the last position
5. **Maximize extraction**: prefer complete extract; report omissions to the user for decision
6. **Dedupe merge**: merge same-patient rows; record repeated content once
7. **IHC**: pull from pathology **full text** (`marker (result)`). If structured `病理_ER`-style columns trip the workspace missingness cutoff (see `workspace.md`), do not write the whole column — parse from full text instead.
8. **Negative is not missing**: parenthetical `-` / `－` / `—` / `阴性` encode as `Negative`; never drop as empty.
9. **Full marker-name match**: `ER` must not hit `HER2`; require a non-letter (or word boundary) before the marker name. For `P16`, mottled/patchy → `Mosaic` alone; do not fold into `Positive`.
10. Category labels in English (`Positive`/`Negative`); rules in `workspace.md` — do not write a second set here.

## Bundled scripts
- `{code_clean_data}\clinical-data-extraction\extract_patient_data.py` — patient info + lab markers
- `{code_clean_data}\clinical-data-extraction\extract_docx.py` — batch docx extract
