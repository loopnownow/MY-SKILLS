---
name: medical-statistical-and-predictive-analysis
description: >
  Clinical/imaging statistics and prediction models. Use for 统计, 插补, AUC, DeLong,
  DCA, LASSO, 列线图, 两两比较, Table 1.
  Integrates radiology-stats, statistical-analysis, and data-impute. Do not use for 写论著, 图像处理, 评阅, or 回复审稿人.
---

# Medical Statistical and Predictive Analysis (integrated)

## Purpose

Prioritize estimands, effect sizes, uncertainty, assumptions, validation, and reproducibility
over isolated P values.

Live 0RAD modules **v4.3.0** (2026-08-28) are the lab default. Nested CV, multivariate Cox,
lifelines, and DeLong *intervals* are **not** implemented as lab defaults — say so if asked;
never write them as what the lab ran.

## Capability map

| Task | Path |
|------|------|
| **Radiology-grade** AUC/CI, DeLong p, kappa/ICC, MRMC, calibration, DCA, survival, sample size, high-dim | `bundles/radiology-stats/` |
| Test selection / APA-style reporting / power | `bundles/statistical-analysis/` |
| Group-stratified missing-value imputation | `bundles/data-impute/MODULE.md` |
| **0RAD pipeline rules** (`VAL_MODE`, live modules v4.3.0, 全部组/不筛, 子结局分组, `SUBGROUP_COL`, `FORCE_INTER`) | `references/0rad-pipeline-rules.md` |
| **Lab clinical stats pipeline** (Table 1 / LASSO / ROC HTML) | `python -m modules.pipeline` (not habitat-tree `LassoCV`; not `statistical-analysis/scripts/`) |
| Export impute/outlier scripts (alongside data-impute) | `bundles/data-impute/scripts/export_*` |

## Analysis workflow

1. Define outcome, predictors, estimand, population, time origin.
2. Inspect types, missingness, distributions, structure.
3. Match model to design/outcome.
4. Check assumptions; fit primary model.
5. Report effect + 95% CI + P when appropriate.
6. Performance + uncertainty; pre-specified sensitivity/subgroup.
7. Validate (held-out / external); document software, seeds, exclusions.

## Imaging hard rules (non-negotiable)

- Patient-level splits; never treat slice-level random split as external validation.
- AUC 95% CI = **1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals.
- Paired model-comparison **p** = DeLong (Sun & Xu 2014 midranks); `ROC_METRICS` columns `DeLong vs {model}` (added 2026-08-28). DeLong is a p, not a CI.
- **Combined** is the named primary model. Youden is **per split** (`refit` / `apply_formula`); `lock_threshold` keeps the training Youden.
- Radiomics reproducibility filter: **ICC(A,1) ≥ 0.75**.
- Clinical model: Table 1 then **AIC backward** (unless `FORCE_MODEL_FEATURES`).
- LASSO: **StratifiedKFold AUC path on TRAIN only**. The lab does **not** use nested CV.
- Survival: KM + log-rank. Optional univariable Cox (`statsmodels` PHReg, Breslow; `DO_COX` library default **False**). Not multivariate; not lifelines.
- Habitat-tree `LassoCV` ≠ paper primary. Primary numbers: `python -m modules.pipeline` → `*-results.html`.
- Do not invent p/AUC/event counts; do not fake a priori power for pure retrospective work.
- 0RAD test-set scoring: `VAL_MODE` ∈ {`refit`, `apply_formula`, `lock_threshold`} — **never re-select features**. Details: `references/0rad-pipeline-rules.md`.

## Core modes

Descriptive/group comparison · Regression · Survival · Prediction/diagnostic · Feature selection · Sensitivity · Imputation (`data-impute`)

### ML leakage rule

data split → preprocess fit on train → LASSO / clinical selection on **train only** → fit → validate/test.

Never select features on the full dataset. Never describe lab LASSO as nested CV.

## Output

analysis rationale · assumptions/diagnostics · code if requested · effects + uncertainty · performance · QC · interpretation tied to actual data

## Progressive disclosure

Only this top-level skill is auto-discovered. `data-impute` is a nested module, not a separate skill. Load `bundles/*/MODULE.md` as needed.
