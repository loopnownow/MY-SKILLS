---
name: medical-statistics-analysis-and-visualization
description: >
  Statistics, prediction, survival, diagnostic accuracy, and figure generation.
  Triggers: 统计, 出图, 样本量, AUC, DeLong, DCA, KM, 生存分析, calc-sample-size,
  plot-figures, draw-flowchart.
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
| Figure claim planning (pick the plot from the Discussion claim before drawing) | `personal/figure-claim-planning.md` |
| Stats checklist | `personal/stats-checklist.md` |
| Reported stats consistency (GRIM / NHST / CI vs p; threshold, implied *n*, multiplicity, relative units, circular *P*, inclusion scale) | `personal/stats-consistency.md` |
| Pre-submit check ids (writing actions; 05 owns prose) | `05_manuscript/personal/pre-submit-consistency.md` |

Do **not** copy `personal/` (lab radiology-stats + 0RAD rules) into the capabilities pack. Lab numbers: `python -m modules.pipeline` → `*-results.html`.

## Mounted capability ids (generic; not present until mounted)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

- `analyze-stats` — test selection / effect sizes
- `calc-sample-size` — sample size / power; `statistical-power` is PROPOSED
- `model-evaluation` / `model-validation` — calibration / DCA / external validation；脚本库：`D:\0Grok\0script\stats-analysis\model-validation\`
- `meta-analysis` (`analyze-survival` is PROPOSED) — implementation; 0RAD personal still wins
- `radiomics-ml` — radiomics modelling pipeline audit
- `draw-flowchart` — STROBE / patient-flow
- `plot-figures` — statistical plots / imaging panels

Until `plot-figures` / `draw-flowchart` is mounted, do not invent a second figure stack inside 05.

## Imaging hard rules (non-negotiable)

- Patient-level splits; never treat slice-level random split as external validation.
- AUC 95% CI = **1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals.
- Paired model-comparison **p** = DeLong (Sun & Xu 2014 midranks). DeLong is a p, not a CI.
- **Combined** is the named primary model. Youden is **per split**; `lock_threshold` keeps the training Youden.
- Radiomics reproducibility filter: **ICC(A,1) ≥ 0.75**.
- Clinical model: non-empty `FORCE_MODEL_FEATURES` is the model. Empty list selects candidate-pool multivariate p < `ROC_MV_P_THRESHOLD`. AIC stepwise stays informational and does not enter the model.
- LASSO: **StratifiedKFold AUC path on TRAIN only**. The lab does **not** use nested CV.
- Survival: KM + log-rank. Optional univariable Cox. Not multivariate; not lifelines.
- Do not invent p/AUC/event counts; do not fake a priori power for pure retrospective work.
- 0RAD test-set scoring: `VAL_MODE` ∈ {`refit`, `apply_formula`, `lock_threshold`} — **never re-select features**. Details: `personal/0rad-pipeline-rules.md`.

## Precedence

Three axes. Do not mix them into one ranked list.

**规则权威：** A 个人层 > 04 通用 > 外挂能力

**工具选择：** 个人已实现则用个人；否则外挂；再否则 04 通用

**事实权威：** 已执行结果 HTML / 项目 `settings.ini` > 任何 skill 文本

Do not invent numbers the HTML does not contain.

## Workflow

1. Confirm analysis-ready inputs from `02_data-processing`. Do not silently repair upstream data.
2. Define outcome, predictors, estimand, population, time origin.
3. Match model to design/outcome; fit on training only.
4. Report effect + 95% CI + P when appropriate.
5. Generate figures here (mounted `plot-figures` / `draw-flowchart`, + `personal/lab-palettes.md`). Before drawing, load `personal/figure-claim-planning.md` (claim → plot type, evidence manifest, three-round render QC). Caption prose → `05_manuscript`. Figure 1 labels, downsample vs eligibility, and PDF (Times New Roman 12 pt) follow `05_manuscript/personal/Aitor-format.md` over the mounted fig-flow Validation Cohort default.

## Boundaries

- Data cleaning / Excel → `02_data-processing` (`clean-data` / `batch-cohort`)
- Literature → `03_research`
- Manuscript wording → `05_manuscript`
- Reviewer response → `06_review`
