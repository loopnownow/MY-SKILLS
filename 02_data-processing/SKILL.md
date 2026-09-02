---
name: medical-data-processing
description: >
  Raw-data to analysis-ready-data. Use for Excel/CSV, 0RAD workspace, cleaning,
  missing/outlier handling, imaging preprocessing/QC, radiomics/habitat preparation,
  leakage/split checks, clinical extraction, coding principles, ethics form packs
  (temporary parking), and the user's MATLAB/Python scripts. No feature selection
  or statistical modeling — hand off to 04_analysis. Literature → 03. Writing → 05.
---

# Data Processing

## Purpose

Convert raw clinical, imaging, and table data into **analysis-ready** data with traceable QC.

## Scope

- Excel/CSV/table batch processing (mounted `02-xlsx`)
- ID alignment, cleaning, missingness and outlier handling (mounted `02-impute`)
- imaging preprocessing and QC (mounted `02-imaging-qc`)
- radiomics / habitat preprocessing and feature-extraction **preparation** (mounted `02-radiomics-habitat`)
- generic imaging/data docs (mounted `02-generic-docs`)
- leakage and split-integrity checks
- maintained personal MATLAB/Python scripts
- clinical text / HIS / pathology **extraction** (`clinical-data-extraction/`)
- coding principles / soft-coding / dry-run (`code-refactoring/`)
- ethics application form packs (`ethics-application-forms/` — **temporary parking**; true home is 03 ethics design)

Never perform feature selection or statistical model fitting here.

## Personal layer (this repo)

| Task | Path |
|---|---|
| 0RAD workspace (folder names, `exc`, false-classification) | `0rad-workspace.md` |
| Lab MATLAB preprocess | `scripts/parallel_preprocess.m`, `scripts/run_preprocess.m` |
| Leakage / split / radiology audit | `scripts/split_leakage_check.py`, `scripts/radiology_audit.py` |
| Clinical / HIS extraction | `clinical-data-extraction/` |
| Soft-coding / dry-run / CONFIG on top | `code-refactoring/` |
| Ethics form packs (**temp**; true home is 03 ethics design) | `ethics-application-forms/` |

Personal scripts are not replaced by a mounted pack.

## Mounted capability ids (generic; not present until mounted)

Until `registry.yaml` `mounts:` is non-empty, 02 still uses personal scripts plus any local notes here. After mount, call by **id**, not by deleted `bundles/` paths:

- `02-xlsx` — Excel/CSV automation
- `02-imaging-qc` — lesion/mask/reader/reproducibility QC
- `02-radiomics-habitat` — IBSI/habitat prep (paper modelling → 04)
- `02-impute` — missing/outlier processing
- `02-generic-docs` — annotation/data/checklists/reproducibility/mechanism/radiomics/deep-learning notes

## Workflow

raw files → integrity/IDs → preprocessing → QC → derived features → analysis-ready table → **handoff to `04_analysis`**.

## Coding conventions

When writing batch scripts, follow `code-refactoring/` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility
