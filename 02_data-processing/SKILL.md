---
name: medical-data-processing
description: >
 Advanced data-processing and analysis top layer: raw clinical/imaging/picture/fMRI to analysis-ready,
 then valid statistics, prediction, survival, diagnostic accuracy, and publication figures.
 Triggers: Excel/CSV clean, DICOM/NIfTI, radiomics prep, extraction, coding, leakage checks,
 stats, AUC, DeLong, DCA, KM, calc-sample-size, plot-figures, draw-flowchart.
 Capability bodies for 02 fine ids live in 02_data-processing/base/.
 Literature -> 03. Writing -> 05. Review -> 06. Response -> 07.
---

# Data Processing & Analysis -- advanced top layer

**Route:** `advanced/route.md`. **Handoff:** `advanced/handoff.md`.
**Analysis route:** `advanced/analysis/route.md`. **Analysis handoff:** `advanced/analysis/handoff.md`.

## Purpose

Convert raw clinical, imaging, picture, and fMRI data into **analysis-ready** data with traceable QC,
then transform analysis-ready data into valid statistical results, predictive-model results, and publication-ready figures.

**02 is the advanced top layer** (like 03/05/06): route, handoff, post-QC triggers, and post-QC authority for lab numbers/figures.
Capability **bodies** for clean/imaging/stats/figures fine ids all live in **`02_data-processing/base/`** (analysis packs merged 2026-10-25). Fine IDs are not renamed.

Live lab modules are the lab default (`{code_modules}`; version SSOT is `modules/__init__.py`). Nested CV, multivariate Cox, lifelines, and DeLong *intervals* are **not** implemented as lab defaults -- say so if asked; never write them as what the lab ran. Imaging / stats hard rules live in `advanced/analysis/pipeline.md`, not in this seat SKILL.

## Layer model

Base / advanced / qc roles: `00_orchestrator/references/base-vs-advanced-top-loops.md`. Do not restate the layer table here.

## Advanced assets (top layer)

| Task | Path |
|---|---|
| Route / which advanced file | `advanced/route.md` |
| Handoff (raw->analysis-ready; then results) | `advanced/handoff.md` |
| Lab workspace (folder names, `exc`, false-classification) | `{RULES}/workspace-layout.md` |
| Clinical / HIS / pathology extraction | `advanced/extract.md` |
| Soft-coding / dry-run / complexity ladder | `advanced/coding.md` |
| Deep code QC standards (00 / G-CODE) | `qc/coding-qc.md` |
| Raw table digit / smoothness QC | `advanced/table-signals.md` |
| Summary table -> subject-level synthetic rows (pooled-analysis input) | `advanced/restore-from-summary.md` |
| Analysis route | `advanced/analysis/route.md` |
| Analysis handoff | `advanced/analysis/handoff.md` |
| Lab pipeline (hard rules, `VAL_MODE`, live modules) | `advanced/analysis/pipeline.md` |
| Console UI / results HTML / figure switches | `advanced/analysis/console-ui.md` |
| Radiology-grade stats index | `advanced/analysis/module-notes.md` + `advanced/analysis/methods.md` |
| Lab figure palettes / claim planning | `advanced/analysis/figures.md` |
| Stats checklist / reported consistency (00 gate standards) | `qc/report-checks.md` |
| Pre-submit check ids (writing actions; 05 owns prose) | `05_manuscript/qc/manuscript-local-qc.md` |
| Visualization IR + rebuild scripts | `advanced/visualization/` |
| Lab MATLAB preprocess | `{code_data_processing}\preprocess-imaging\fmri\parallel_preprocess.m`, `{code_data_processing}\preprocess-imaging\fmri\run_preprocess.m` |
| Leakage / split / radiology audit | `{code_model_validation}\split_leakage_check.py`, `{code_model_validation}\radiology_audit.py` |
| Clinical / HIS extraction scripts | `{code_clean_data}\clinical-data-extraction\` |
| Soft-coding / dry-run / CONFIG on top | `{code_data_processing}\templates\soft_code_template.py` (see `advanced/coding.md`) |

Advanced scripts are not replaced by a live pack.
A base pack that grows a long procedure has drifted: the procedure belongs in `02_data-processing/advanced/` (per-pack digest or the analysis pipeline files) and the base pack keeps scope, bans, and the pointer.

## Live capability ids (bodies under `NN_slug/base/`; fine IDs unchanged)

**This-run pick:** wait for the 00 session fine-id pick (`00_orchestrator/references/session-pick.md`). Registry fine-id menu (SSOT) = pick list.

- `clean-data` -- clinical Excel/CSV cleaning and cohort tables (`02_data-processing/base/clean-data/`); `batch-cohort` resolves here as a retired alias
- `db-library` -- `_DataBase` family SQLite library (`<family>\_PHI\<family>db`) + loose-table merge (`02_data-processing/base/db-library/`)
- `preprocess-imaging` -- Imaging I/O and ROI/reader QC (`02_data-processing/base/preprocess-imaging/`); absorbed retired `imaging-io`
- `stats-analysis` -- test selection / assumptions / Bayesian notes (`02_data-processing/base/stats-analysis/`); absorbed retired `meta-analysis`
- `calc-sample-size` -- sample size / power (`02_data-processing/base/calc-sample-size/`)
- `model-evaluation` -- calibration / DCA / external validation + leakage gates (`02_data-processing/base/model-evaluation/`)
- `draw-flowchart` -- STROBE / patient-flow (`02_data-processing/base/draw-flowchart/`)
- `plot-figures` -- statistical plots / imaging panels (`02_data-processing/base/plot-figures/`)
- Radiomics / habitat **prep** -- via `stats-analysis` / `preprocess-imaging` (former `radiomics-ml` absorbed into `stats-analysis`; no live radiomics-habitat path)

Neither `plot-figures` nor `draw-flowchart` may be duplicated as a second figure stack inside 05.

Retired ids stay off the menu; they are not runtime ids (see `tests/retired_ids.py`).

## Precedence

Three axes. Do not mix them into one ranked list.

**Rule authority:** 02 advanced > 02 generic > external capability

**Tool choice:** advanced already implemented -> use advanced; else live; else 02 generic

**Fact authority:** executed results HTML / project `settings.ini` > any skill text

Do not invent numbers the HTML does not contain.

## Workflows

**Data processing**

raw files -> integrity/IDs -> preprocessing -> QC -> derived features -> analysis-ready table.

**Analysis**

1. Confirm analysis-ready inputs from the data-processing flow. Do not silently repair upstream data.
2. Define outcome, predictors, estimand, population, time origin.
3. Match model to design/outcome; fit on training only.
4. Report effect + 95% CI + P when appropriate.
5. Generate figures here (live `plot-figures` / `draw-flowchart`, + `advanced/analysis/figures.md`). Caption prose -> `05_manuscript`. Figure 1 labels follow `05_manuscript/advanced/Aitor-format.md` over the live fig-flow Validation Cohort default.

## Coding conventions

When writing batch scripts, follow `advanced/coding.md` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Boundaries

- Data cleaning / Excel / imaging I/O -> this skill (`advanced/extract.md`, `base/clean-data`, `base/preprocess-imaging`)
- Feature selection / model fitting / NHST / figures -> this skill (`base/stats-analysis`, `base/model-evaluation`, `advanced/analysis/`)
- Literature -> `03_research`
- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Exit QC -> `00_orchestrator`

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility · effect with 95% CI and P · figure/legend consistency
