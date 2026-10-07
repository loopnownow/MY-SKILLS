---
name: medical-data-processing
description: >
  Raw-data to analysis-ready-data. Use for clinical Excel/CSV, CT/MRI (DICOM/NIfTI/NII),
  pictures (TIFF/PNG/JPG/PDF-as-image), fMRI, radiomics/habitat preparation,
  leakage/split checks, clinical extraction, coding principles, and the user's MATLAB/Python scripts.
  No feature selection or statistical modeling — hand off to 04_analysis. Literature → 03. Writing → 05.
---

# Data Processing

## Purpose

Convert raw clinical, imaging, picture, and fMRI data into **analysis-ready** data with traceable QC.

## Scope

- clinical tables: Excel/CSV, cleaning, missing/outlier (`clean-data` / `batch-cohort`)
- CT/MRI I/O: DICOM / NIfTI / NII (`imaging-io`)
- CT/MRI QC: ROI / reader (`preprocess-imaging`)
- radiomics / habitat preparation (`radiomics-ml`; modelling → 04)
- leakage and split-integrity checks
- maintained personal MATLAB/Python scripts
- clinical text / HIS / pathology **extraction** (`clinical-data-extraction/`)
- coding principles / soft-coding / dry-run (`code-refactoring/`)
- raw numeric table QC signals (`table-qc/`)

Never perform feature selection or statistical model fitting here.

## Personal layer (this repo)

| Task | Path |
|---|---|
| 0RAD workspace (folder names, `exc`, false-classification) | `0rad-workspace.md` |
| Lab MATLAB preprocess | `D:\0Grok\0script\data-processing\preprocess-imaging\fmri\parallel_preprocess.m`, `D:\0Grok\0script\data-processing\preprocess-imaging\fmri\run_preprocess.m` |
| Leakage / split / radiology audit | `D:\0Grok\0script\stats-analysis\model-validation\split_leakage_check.py`, `D:\0Grok\0script\stats-analysis\model-validation\radiology_audit.py` |
| Clinical / HIS extraction | `D:\0Grok\0script\data-processing\clinical-data-extraction\`（`extract_patient_data.py`、`extract_docx.py`） |
| Soft-coding / dry-run / CONFIG on top | `D:\0Grok\0script\_templates\soft_code_template.py`（说明在 `code-refactoring/`） |
| Raw table digit / smoothness QC | `table-qc/` (`references/`) |

Personal scripts are not replaced by a mounted pack.

## Mounted capability ids (generic; not present until mounted)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

Call mounted ids from 01 (`01_skill-discovery-integration/MOUNTED_SKILLS.md` menu + `01_skill-discovery-integration/mounts/README.md` board / `registry.yaml`), not historical pack paths. Personal scripts stay local:

- `clean-data` / `batch-cohort` — 临床表 Excel / CSV（含缺失/异常值）；脚本库：`D:\0Grok\0script\data-processing\clean-data\`
- `imaging-io` — CT / MRI 读写，DICOM / NIfTI / NII
- `preprocess-imaging` — CT / MRI QC，ROI / 阅片；脚本库：`D:\0Grok\0script\data-processing\preprocess-imaging\`
- `radiomics-ml` — IBSI/habitat prep; fine id routes to 04 (paper modelling → 04)

Archived ids stay off the menu (registry `archived:`).

## Workflow

raw files → integrity/IDs → preprocessing → QC → derived features → analysis-ready table → **handoff to `04_analysis`**.

## Coding conventions

When writing batch scripts, follow `code-refactoring/` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility
