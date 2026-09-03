---
name: medical-statistics-analysis-and-visualization
description: >
  Statistics, prediction, survival, diagnostic accuracy, and figure generation.
  Use after data are analysis-ready. Cleaning/imputation → 02_data-processing.
  Figure captions and manuscript prose → 05_manuscript. Literature → 03.
---

# Analysis & Visualization

## Purpose

Transform analysis-ready data into valid statistical results, predictive-model results, and publication-ready figures.

Live 0RAD modules **v4.3.0** (2026-08-28) are the lab default. Nested CV, multivariate Cox, lifelines, and DeLong *intervals* are **not** implemented as lab defaults — say so if asked; never write them as what the lab ran.

## Personal layer (this repo)

| Task | Path |
|---|---|
| Lab 0RAD pipeline (`VAL_MODE`, live modules v4.3.0) | `personal/0rad-pipeline-rules.md` |
| Radiology-grade stats (DeLong p, DCA, ICC, MRMC, sample size) | `personal/` (`MODULE.md` + diagnostic/survival/sample-size notes) |
| Imaging statistics notes (lab) | `personal/statistics.md` |
| Lab figure palettes | `personal/lab-palettes.md` |
| Stats checklist | `personal/stats-checklist.md` |

Do **not** copy `personal/` (lab radiology-stats + 0RAD rules) into the capabilities pack. Lab numbers: `python -m modules.pipeline` → `*-results.html`.

## Mounted capability ids (generic; not present until mounted)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

- `04-stats-guide` — test selection / effect sizes
- `04-stats-power` — sample size / power
- `04-model-eval` — calibration / DCA / external validation
- `04-stats-models` — implementation; 0RAD personal still wins
- `04-fig-flow` — STROBE / patient-flow
- `04-fig-plot` — statistical plots / imaging panels
- `04-explainability` — imaging-model XAI (Grad-CAM etc.). MedSci-only. Not in B. Does not replace `personal/` 0RAD rules.

Retired: `04-stats-generic`, `04-figure-engine`.

Until `04-fig-plot` / `04-fig-flow` is mounted, do not invent a second figure stack inside 05.

## Imaging hard rules (non-negotiable)

- Patient-level splits; never treat slice-level random split as external validation.
- AUC 95% CI = **1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals.
- Paired model-comparison **p** = DeLong (Sun & Xu 2014 midranks). DeLong is a p, not a CI.
- **Combined** is the named primary model. Youden is **per split**; `lock_threshold` keeps the training Youden.
- Radiomics reproducibility filter: **ICC(A,1) ≥ 0.75**.
- Clinical model: Table 1 then **AIC backward** (unless `FORCE_MODEL_FEATURES`).
- LASSO: **StratifiedKFold AUC path on TRAIN only**. The lab does **not** use nested CV.
- Survival: KM + log-rank. Optional univariable Cox. Not multivariate; not lifelines.
- Do not invent p/AUC/event counts; do not fake a priori power for pure retrospective work.
- 0RAD test-set scoring: `VAL_MODE` ∈ {`refit`, `apply_formula`, `lock_threshold`} — **never re-select features**. Details: `personal/0rad-pipeline-rules.md`.

## Workflow

1. Confirm analysis-ready inputs from `02_data-processing`. Do not silently repair upstream data.
2. Define outcome, predictors, estimand, population, time origin.
3. Match model to design/outcome; fit on training only.
4. Report effect + 95% CI + P when appropriate.
5. Generate figures here (mounted `04-fig-plot` / `04-fig-flow` + `personal/lab-palettes.md`). Caption prose → `05_manuscript`.

## Boundaries

- Data cleaning / Excel → `02_data-processing` (id `02-tables`)
- Literature → `03_research`
- Manuscript wording → `05_manuscript`
- Reviewer response → `06_review`
