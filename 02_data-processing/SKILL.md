---
name: medical-data-processing
description: >
  Personal data-processing top layer: raw clinical/imaging/picture/fMRI to analysis-ready.
  Triggers: Excel/CSV clean, DICOM/NIfTI, radiomics prep, extraction, coding, leakage checks.
  Capability bodies for 02 mounts live in 02_data-processing/base/ (pilot). No feature selection or statistical modeling -- hand off to 04.
  Literature -> 03. Writing -> 05. Review -> 06. Response -> 07.
---

# Data Processing -- personal top layer

**Route:** `personal/route.md`. **Handoff:** `personal/handoff.md`.

## Purpose

Convert raw clinical, imaging, picture, and fMRI data into **analysis-ready** data with traceable QC.
**A02 is the personal top layer** (like A03/A05/A06): route, handoff, and post-QC triggers.
Capability **bodies** for clean/imaging mounts live in **A `02_data-processing/base/`** (pilot 2026-10-17; was B; B repo retained).

## Layer model (2026-10-17)

**Flow:** data-processing fine-ID **first-pass** (A `base/` bodies) -> **00 QC** -> **A02** top-layer re-loops

**QC standards:** live in `qc/` and are invoked only by `00_orchestrator` at Gate time (not by the specialist during first-pass). See `qc/README.md`.
(personal coding/extract/workspace protocols; may re-trigger B mounts when 00 says needed).

| Layer | Owns |
|---|---|
| A `base/` (pilot) | `clean-data`, `batch-cohort`, `imaging-io`, `preprocess-imaging`, tables/impute under `02_data-processing/base/` (was B; B repo retained; radiomics-habitat prep still B if present) |
| 00 | QC gate; decides whether A02 re-triggers B mounts |
| A02 | Personal route/handoff/authority; workspace/extract/coding/table-signals; Loopnow seat (QC standards in `qc/`, 00-only) |

## Personal assets (top layer)

| Task | Path |
|---|---|
| Route / which personal file | `personal/route.md` |
| Handoff (raw->analysis-ready; Loopnow -> 04) | `personal/handoff.md` |
| 0RAD workspace (folder names, `exc`, false-classification) | `personal/workspace.md` |
| Clinical / HIS / pathology extraction | `personal/extract.md` |
| Soft-coding / dry-run / complexity ladder | `personal/coding.md` |
| Deep code QC standards (00 / G-CODE) | `qc/coding-qc.md` |
| Raw table digit / smoothness QC | `personal/table-signals.md` |
| Lab MATLAB preprocess | `{script_data_processing}\preprocess-imaging\fmri\parallel_preprocess.m`, `{script_data_processing}\preprocess-imaging\fmri\run_preprocess.m` |
| Leakage / split / radiology audit | `{script_model_validation}\split_leakage_check.py`, `{script_model_validation}\radiology_audit.py` |
| Clinical / HIS extraction scripts | `{script_data_processing}\clinical-data-extraction\` |
| Soft-coding / dry-run / CONFIG on top | `{script_root}\_templates\soft_code_template.py` (see `personal/coding.md`) |

Personal scripts are not replaced by a mounted pack.
Do not rewrite mounted data-processing capability bodies (now under `base/`) inside these personal files.

## Mounted capability ids (bodies in A base/ — pilot)

**This-run pick:** wait for 01 session-mount pick. Registry MOUNTED = menu.

- `clean-data` / `batch-cohort` -- clinical Excel/CSV (A `02_data-processing/base/tables/`)
- `imaging-io` -- CT/MRI I/O DICOM/NIfTI (A `02_data-processing/base/imaging-io/`)
- `preprocess-imaging` -- ROI / reader QC (A `02_data-processing/base/imaging-qc/`)
- Radiomics / habitat **prep** -- still B `02-data-processing/radiomics-habitat/` if present (reachable via `analyze-stats` / `preprocess-imaging` after radiomics-ml absorb; modelling belongs to 04; not in this pilot)

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
