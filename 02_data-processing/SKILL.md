---
name: medical-data-processing
description: >
  Personal data-processing top layer: raw clinical/imaging/picture/fMRI to analysis-ready.
  Triggers: Excel/CSV clean, DICOM/NIfTI, radiomics prep, extraction, coding, leakage checks.
  Capability bodies stay in B. No feature selection or statistical modeling -- hand off to 04.
  Literature -> 03. Writing -> 05. Review -> 06. Response -> 07.
---

# Data Processing -- personal top layer

**Route:** `personal/route.md`. **Handoff:** `personal/handoff.md`.

## Purpose

Convert raw clinical, imaging, picture, and fMRI data into **analysis-ready** data with traceable QC.
**A02 is the personal top layer** (like A03/A05/A06): route, handoff, and post-QC triggers.
Capability **bodies** for clean/imaging mounts stay in **B**.

## Layer model (2026-10-17)

**Flow:** B data-processing fine-ID **first-pass** -> **00 QC** -> **A02** top-layer re-loops
(personal coding/extract/workspace protocols; may re-trigger B mounts when 00 says needed).

| Layer | Owns |
|---|---|
| B | `clean-data`, `batch-cohort`, `imaging-io`, `preprocess-imaging`, tables/impute, radiomics-habitat prep bodies under `02-data-processing/` |
| 00 | QC gate; decides whether A02 re-triggers B mounts |
| A02 | Personal route/handoff/authority; workspace/extract/coding/coding-qc/table-signals; Loopnow seat |

## Personal assets (top layer)

| Task | Path |
|---|---|
| Route / which personal file | `personal/route.md` |
| Handoff (raw->analysis-ready; Loopnow -> 04) | `personal/handoff.md` |
| 0RAD workspace (folder names, `exc`, false-classification) | `personal/workspace.md` |
| Clinical / HIS / pathology extraction | `personal/extract.md` |
| Soft-coding / dry-run / complexity ladder | `personal/coding.md` |
| Deep code QC | `personal/coding-qc.md` |
| Raw table digit / smoothness QC | `personal/table-signals.md` |
| Lab MATLAB preprocess | `{script_data_processing}\preprocess-imaging\fmri\parallel_preprocess.m`, `{script_data_processing}\preprocess-imaging\fmri\run_preprocess.m` |
| Leakage / split / radiology audit | `{script_model_validation}\split_leakage_check.py`, `{script_model_validation}\radiology_audit.py` |
| Clinical / HIS extraction scripts | `{script_data_processing}\clinical-data-extraction\` |
| Soft-coding / dry-run / CONFIG on top | `{script_root}\_templates\soft_code_template.py` (see `personal/coding.md`) |

Personal scripts are not replaced by a mounted pack.
Do not rewrite mounted B data-processing capability bodies inside these files.

## Mounted capability ids (bodies in B)

**This-run pick:** wait for 01 session-mount pick. Registry MOUNTED = menu.

- `clean-data` / `batch-cohort` -- clinical Excel/CSV (B `02-data-processing/tables/`)
- `imaging-io` -- CT/MRI I/O DICOM/NIfTI (B `02-data-processing/imaging-io/`)
- `preprocess-imaging` -- ROI / reader QC (B `02-data-processing/imaging-qc/`)
- Radiomics / habitat **prep** -- B `02-data-processing/radiomics-habitat/` (reachable via `analyze-stats` / `preprocess-imaging` after radiomics-ml absorb; modelling belongs to 04)

Archived ids stay off the menu (registry `archived:`).

## Workflow

raw files -> integrity/IDs -> preprocessing -> QC -> derived features -> analysis-ready table -> **handoff to `04_analysis`**.

## Coding conventions

When writing batch scripts, follow `personal/coding.md` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Boundaries

- Feature selection / model fitting / NHST -> `04_analysis`
- Literature -> `03_research`
- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Exit QC -> `00_orchestrator`

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility
