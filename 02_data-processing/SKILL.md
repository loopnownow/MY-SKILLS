---
name: medical-data-processing
description: >
 Personal data-processing and analysis top layer: raw clinical/imaging/picture/fMRI to analysis-ready,
 then valid statistics, prediction, survival, diagnostic accuracy, and publication figures.
 Triggers: Excel/CSV clean, DICOM/NIfTI, radiomics prep, extraction, coding, leakage checks,
 stats, AUC, DeLong, DCA, KM, calc-sample-size, plot-figures, draw-flowchart.
 Capability bodies for 02 mounts live in 02_data-processing/base/ (pilot).
 Literature -> 03. Writing -> 05. Review -> 06. Response -> 07.
---

# Data Processing & Analysis -- personal top layer

**Route:** `personal/route.md`. **Handoff:** `personal/handoff.md`.
**Analysis route:** `personal/analysis/route.md`. **Analysis handoff:** `personal/analysis/handoff.md`.

## Purpose

Convert raw clinical, imaging, picture, and fMRI data into **analysis-ready** data with traceable QC,
then transform analysis-ready data into valid statistical results, predictive-model results, and publication-ready figures.

**02 is the personal top layer** (like 03/05/06): route, handoff, post-QC triggers, and post-QC authority for lab numbers/figures.
Capability **bodies** for clean/imaging/stats/figures mounts all live in **`02_data-processing/base/`** (pilot 2026-10-17; analysis packs merged 2026-10-25). Fine IDs are not renamed.

Live lab modules **v4.3.0** (2026-08-28) are the lab default. Nested CV, multivariate Cox, lifelines, and DeLong *intervals* are **not** implemented as lab defaults -- say so if asked; never write them as what the lab ran.

## Layer model (2026-10-17)

**Flow:** fine-ID **first-pass** (`base/` bodies) -> **00 QC** -> **02** top-layer re-loops

**QC standards:** live in `qc/` and are invoked only by `00_orchestrator` at Gate time (not by the specialist during first-pass). See `qc/README.md`.
(personal coding/extract/workspace protocols + analysis pipeline/figures personal; may re-trigger base mounts when 00 says needed).

| Layer | Owns |
|---|---|
| `base/` (pilot) | `clean-data`, `imaging-io`, `preprocess-imaging`, `analyze-stats`, `calc-sample-size`, `model-evaluation`, `meta-analysis`, `draw-flowchart`, `plot-figures` under `02_data-processing/base/` |
| 00 | QC gate (G-PHI / G-CODE / G-FACT / G-STATS); decides whether 02 re-triggers base mounts |
| 02 | Personal route/handoff/authority; workspace/extract/coding/table-signals; analysis pipeline/console-ui/methods/figures; Loopnow seat (QC standards in `qc/`, 00-only); visualization (IR to HTML) under `personal/visualization/` |

## Personal assets (top layer)

| Task | Path |
|---|---|
| Route / which personal file | `personal/route.md` |
| Handoff (raw->analysis-ready; then results) | `personal/handoff.md` |
| Lab workspace (folder names, `exc`, false-classification) | `{RULES}/workspace-layout.md` |
| Clinical / HIS / pathology extraction | `personal/extract.md` |
| Soft-coding / dry-run / complexity ladder | `personal/coding.md` |
| Deep code QC standards (00 / G-CODE) | `qc/coding-qc.md` |
| Raw table digit / smoothness QC | `personal/table-signals.md` |
| Analysis route | `personal/analysis/route.md` |
| Analysis handoff | `personal/analysis/handoff.md` |
| Lab pipeline (`VAL_MODE`, live modules v4.3.0) | `personal/analysis/pipeline.md` |
| Console UI / results HTML / figure switches | `personal/analysis/console-ui.md` |
| Radiology-grade stats index | `personal/analysis/module-notes.md` + `personal/analysis/methods.md` |
| Lab figure palettes / claim planning | `personal/analysis/figures.md` |
| Lab analysis rules (personal, pre-computed) | `personal/analysis/report-checks.md` |
| Stats checklist / reported consistency (00 gate standards) | `qc/report-checks.md` |
| Pre-submit check ids (writing actions; 05 owns prose) | `05_manuscript/qc/manuscript-local-qc.md` |
| Visualization IR + rebuild scripts | `personal/visualization/` |
| Lab MATLAB preprocess | `{code_data_processing}\preprocess-imaging\fmri\parallel_preprocess.m`, `{code_data_processing}\preprocess-imaging\fmri\run_preprocess.m` |
| Leakage / split / radiology audit | `{code_model_validation}\split_leakage_check.py`, `{code_model_validation}\radiology_audit.py` |
| Clinical / HIS extraction scripts | `{code_clean_data}\clinical-data-extraction\` |
| Soft-coding / dry-run / CONFIG on top | `{code_root}\_infra\_templates\soft_code_template.py` (see `personal/coding.md`) |

Personal scripts are not replaced by a mounted pack.
Do not rewrite mounted data-processing capability bodies (now under `base/`) inside these personal files.

## Mounted capability ids (bodies under `NN_slug/base/`; fine IDs unchanged)

**This-run pick:** wait for 01 session-mount pick. Registry mount menu (SSOT) = pick list.

- `clean-data` -- clinical Excel/CSV cleaning and cohort tables (`02_data-processing/base/clean-data/`); the former `batch-cohort` entry point is an archived alias to this body
- `imaging-io` -- CT/MRI I/O DICOM/NIfTI (`02_data-processing/base/imaging-io/`)
- `preprocess-imaging` -- ROI / reader QC (`02_data-processing/base/preprocess-imaging/`)
- `analyze-stats` -- test selection / effect sizes (`02_data-processing/base/analyze-stats/`)
- `calc-sample-size` -- sample size / power (`02_data-processing/base/calc-sample-size/`)
- `model-evaluation` -- calibration / DCA / external validation + leakage gates (`02_data-processing/base/model-evaluation/`)
- `meta-analysis` -- implementation (`02_data-processing/base/meta-analysis/`); lab personal still wins
- `draw-flowchart` -- STROBE / patient-flow (`02_data-processing/base/draw-flowchart/`)
- `plot-figures` -- statistical plots / imaging panels (`02_data-processing/base/plot-figures/`)
- Radiomics / habitat **prep** -- via `analyze-stats` / `preprocess-imaging` (radiomics-ml absorb; no live radiomics-habitat path)

Until `plot-figures` / `draw-flowchart` is mounted, do not invent a second figure stack inside 05.

Archived ids stay off the menu (registry `archived:`).

## Imaging hard rules (non-negotiable)

- Patient-level splits; never treat slice-level random split as external validation.
- AUC 95% CI = **1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals.
- Paired model-comparison **p** = DeLong (Sun & Xu 2014 midranks). DeLong is a p, not a CI.
- **Combined** is the named primary model. Youden is **per split**; `lock_threshold` keeps the training Youden.
- Radiomics reproducibility filter: **ICC(A,1) >= 0.75**.
- Clinical model: non-empty `FORCE_MODEL_FEATURES` is the model. Empty list selects candidate-pool multivariate p < `ROC_MV_P_THRESHOLD`. AIC stepwise stays informational and does not enter the model.
- LASSO: **StratifiedKFold AUC path on TRAIN only**. The lab does **not** use nested CV.
- Survival: KM + log-rank. Optional univariable Cox. Not multivariate; not lifelines.
- Do not invent p/AUC/event counts; do not fake a priori power for pure retrospective work.
- lab test-set scoring: `VAL_MODE` in {`refit`, `apply_formula`, `lock_threshold`} -- **never re-select features**. Details: `personal/analysis/pipeline.md`.

## Precedence

Three axes. Do not mix them into one ranked list.

**Rule authority:** A personal > 02 generic > external capability

**Tool choice:** personal already implemented -> use personal; else mounted; else 02 generic

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
5. Generate figures here (mounted `plot-figures` / `draw-flowchart`, + `personal/analysis/figures.md`). Caption prose -> `05_manuscript`. Figure 1 labels follow `05_manuscript/personal/Aitor-format.md` over the mounted fig-flow Validation Cohort default.

## Coding conventions

When writing batch scripts, follow `personal/coding.md` (CONFIG on top, dry-run). Soft-coding is a capability of this skill, not a standalone archive pack.

## Boundaries

- Data cleaning / Excel / imaging I/O -> this skill (`personal/extract.md`, `base/clean-data`, `base/imaging-io`)
- Feature selection / model fitting / NHST / figures -> this skill (`base/analyze-stats`, `base/model-evaluation`, `personal/analysis/`)
- Literature -> `03_research`
- Manuscript prose -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Exit QC -> `00_orchestrator`

## Final QC

file integrity · IDs · row/subject counts · missingness · geometry · preprocessing parameters · exclusions · output existence · reproducibility · effect with 95% CI and P · figure/legend consistency
