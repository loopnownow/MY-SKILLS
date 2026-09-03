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

- clinical tables: Excel/CSV, cleaning, missing/outlier (`02-tables`)
- CT/MRI I/O: DICOM / NIfTI / NII (`02-imaging-io`)
- CT/MRI QC: ROI / reader (`02-imaging-qc`)
- pictures: TIFF / TIF / PNG / JPG / PDF-as-image (`02-pictures`)
- fMRI: DICOM / NIfTI (`02-fmri`)
- radiomics / habitat preparation (`02-radiomics-habitat`; modelling → 04)
- leakage and split-integrity checks
- maintained personal MATLAB/Python scripts
- clinical text / HIS / pathology **extraction** (`clinical-data-extraction/`)
- coding principles / soft-coding / dry-run (`code-refactoring/`)

Never perform feature selection or statistical model fitting here.

## Personal layer (this repo)

| Task | Path |
|---|---|
| 0RAD workspace (folder names, `exc`, false-classification) | `0rad-workspace.md` |
| Lab MATLAB preprocess | `scripts/parallel_preprocess.m`, `scripts/run_preprocess.m` |
| Leakage / split / radiology audit | `scripts/split_leakage_check.py`, `scripts/radiology_audit.py` |
| Clinical / HIS extraction | `clinical-data-extraction/` (`scripts/`) |
| Soft-coding / dry-run / CONFIG on top | `code-refactoring/` (`scripts/`) |

Personal scripts are not replaced by a mounted pack.

## Mounted capability ids (generic; not present until mounted)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

Call mounted ids from 01 (`mounts/README.md` / `registry.yaml`), not deleted `bundles/` paths. Personal scripts stay local:

- `02-tables` — 临床表 Excel / CSV（含缺失/异常值；B `tables/impute/`）
- `02-imaging-io` — CT / MRI 读写，DICOM / NIfTI / NII
- `02-imaging-qc` — CT / MRI QC，ROI / 阅片
- `02-pictures` — TIFF / PNG / JPG / PDF(图)
- `02-fmri` — 功能磁共振，DICOM / NIfTI
- `02-radiomics-habitat` — IBSI/habitat prep (paper modelling → 04)

Retired: `02-xlsx`, `02-imaging` (umbrella), `02-impute`, `02-generic-docs`.

## Workflow

raw files → integrity/IDs → preprocessing → QC → derived features → analysis-ready table → **handoff to `04_analysis`**.

## Coding conventions

When writing batch scripts, follow `code-refactoring/` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility
