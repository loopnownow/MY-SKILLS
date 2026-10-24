# model-evaluation — thin standing digest (2026-10-24)

Corpus proposal source: Downloads `Grok会话-技能草案-20261024.md` → `{doc_root}\skill-harvest\by-fine-id\`. Cap stays `base/model-evaluation` (covers former `model-validation`). Lab detail SSOT: `methods.md` (Model evaluation) + `pipeline.md`.

## elements
- **Metric family:** AUC (+ paired DeLong **p**), calibration (curve / slope), NRI/IDI, DCA when decision-support is claimed.
- **Output set:** `ROC summary — train & test` (side-by-side + between-model p), reclassification table, DCA curves; mediation panel only when claimed (DAG + mediation results).
- **Leakage gates (former model-validation):** patient-level split locked; feature selection / tuning on train only; refuse slice-level “external”; no test peeking before metrics.

## process
- Lock panel order before render: **ROC → calibration → DCA → NRI/IDI → mediation** (skip unused).
- Every metric reported separately for development and validation sets.
- Reclassification viz = clip/band style, not stacked bars.
- Plots hand off to `plot-figures` / `figures.md`.

## cautions
- **No VIF on `Combined model covariates`.** VIF belongs to development-set Multivariate only (2026-08-04 · 019fca80).
- Do not emit Edge list; DAG keeps mediation-relevant edges highlighted; group nodes use real class names.
- Merge duplicate correlation panels; delete threshold-source columns that carry no meaning.
- Do not invent CIs; lab AUC 95% CI = 1000 bootstrap (`_boot_auc_ci`), never DeLong analytic CI. Detail: `methods.md`, `pipeline.md`, `base/model-evaluation/MODULE.md`.
