---
name: medical-statistics-analysis-and-visualization
description: >
 Personal analysis top layer: statistics, prediction, survival, diagnostic accuracy, figures.
 Triggers: stats, AUC, DeLong, DCA, KM, calc-sample-size, plot-figures, draw-flowchart.
 Capability bodies live in A `04_analysis/base/`. Cleaning/imputation -> 02. Captions/prose -> 05.
 Literature -> 03. Review -> 06. Response -> 07.
---

# Analysis & Visualization -- personal top layer

**Route:** `personal/route.md`. **Handoff:** `personal/handoff.md`.

## Purpose

Transform analysis-ready data into valid statistical results, predictive-model results, and publication-ready figures.
**A04 is the personal top layer** (like A03/A05/A06): route, handoff, and post-QC authority for lab numbers/figures.
Capability **bodies** for stats/figures mounts live in **A `04_analysis/base/`** (merged 2026-10-17). Fine IDs are not renamed.

Live 0RAD modules **v4.3.0** (2026-08-28) are the lab default. Nested CV, multivariate Cox, lifelines, and DeLong *intervals* are **not** implemented as lab defaults -- say so if asked; never write them as what the lab ran.

## Layer model (2026-10-17)

**Flow:** stats/figures fine-ID **first-pass** (A `base/` bodies) -> **00 QC** -> **A04** top-layer re-loops

**QC standards:** live in `qc/` and are invoked only by `00_orchestrator` at Gate time (not by the specialist during first-pass). See `qc/README.md`.
(0RAD pipeline / figures personal; report-checks live in `qc/` for 00; may re-trigger mounts when 00 says needed).

| Layer | Owns |
|---|---|
| A `base/` | `analyze-stats`, `calc-sample-size`, `model-evaluation`, `meta-analysis`, `draw-flowchart`, `plot-figures` under `04_analysis/base/` |
| 00 | QC gate (G-FACT / G-04); decides whether A04 re-triggers mounts |
| A04 | Personal route/handoff/authority; pipeline/console-ui/methods/figures; Loopnow seat (QC standards in `qc/`, 00-only); visualization (IR to HTML) under `personal/visualization/` |

Do **not** copy `personal/` (lab radiology-stats + 0RAD rules) into the capabilities pack.

## Personal assets (top layer)

| Task | Path |
|---|---|
| Route | `personal/route.md` |
| Handoff | `personal/handoff.md` |
| Lab 0RAD pipeline (`VAL_MODE`, live modules v4.3.0) | `personal/pipeline.md` |
| Console UI / results HTML / figure switches | `personal/console-ui.md` |
| Radiology-grade stats index | `personal/module-notes.md` + `personal/methods.md` |
| Lab figure palettes / claim planning | `personal/figures.md` |
| Stats checklist / reported consistency (00 gate standards) | `qc/report-checks.md` |
| Pre-submit check ids (writing actions; 05 owns prose) | `05_manuscript/qc/manuscript-local-qc.md` |
| Visualization IR + rebuild scripts | `personal/visualization/` |

Lab numbers: `python -m modules.pipeline` -> `*-results.html`.

## Mounted capability ids (bodies under `NN_slug/base/`; fine IDs unchanged)

**This-run pick:** wait for 01 session-mount pick. Registry MOUNTED = menu.

- `analyze-stats` -- test selection / effect sizes (A `04_analysis/base/analyze-stats/`)
- `calc-sample-size` -- sample size / power (A `04_analysis/base/calc-sample-size/`)
- `model-evaluation` -- calibration / DCA / external validation + leakage gates (A `04_analysis/base/model-evaluation/`)
- `meta-analysis` -- implementation (A `04_analysis/base/meta-analysis/`); 0RAD personal still wins
- `draw-flowchart` -- STROBE / patient-flow (A `04_analysis/base/draw-flowchart/`)
- `plot-figures` -- statistical plots / imaging panels (A `04_analysis/base/plot-figures/`)

Until `plot-figures` / `draw-flowchart` is mounted, do not invent a second figure stack inside 05.

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
- 0RAD test-set scoring: `VAL_MODE` in {`refit`, `apply_formula`, `lock_threshold`} -- **never re-select features**. Details: `personal/pipeline.md`.

## Precedence

Three axes. Do not mix them into one ranked list.

**Rule authority:** A personal > 04 generic > external capability

**Tool choice:** personal already implemented -> use personal; else mounted; else 04 generic

**Fact authority:** executed results HTML / project `settings.ini` > any skill text

Do not invent numbers the HTML does not contain.

## Workflow

1. Confirm analysis-ready inputs from `02_data-processing`. Do not silently repair upstream data.
2. Define outcome, predictors, estimand, population, time origin.
3. Match model to design/outcome; fit on training only.
4. Report effect + 95% CI + P when appropriate.
5. Generate figures here (mounted `plot-figures` / `draw-flowchart`, + `personal/figures.md`). Caption prose -> `05_manuscript`. Figure 1 labels follow `05_manuscript/personal/Aitor-format.md` over the mounted fig-flow Validation Cohort default.

## Boundaries

- Data cleaning / Excel -> `02_data-processing`
- Literature -> `03_research`
- Manuscript wording -> `05_manuscript`
- Review -> `06_review`; Response -> `07_response`
- Exit QC -> `00_orchestrator`
