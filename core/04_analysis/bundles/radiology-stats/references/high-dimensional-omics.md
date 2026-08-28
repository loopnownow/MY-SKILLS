# High-dimensional statistics — radiomics & multi-omics

The defining problem: **features ≫ samples**. Matched imaging+omics cohorts are small
(often n < 100), while features run to thousands (radiomics) or tens of thousands (genes).
This breaks naive analysis in three ways: multiplicity, overfitting/optimism, and leakage.

## Lab 0RAD (v4.3.0) — what actually runs

- Radiomics reproducibility filter: keep features with **ICC(A,1) ≥ 0.75**.
- **LASSO:** StratifiedKFold **AUC path on TRAIN only**. Coefficients lock; test set is not
  re-screened.
- Clinical covariates: Table 1 then **AIC backward** (unless `FORCE_MODEL_FEATURES`).
- Primary model = **Combined**. Primary numbers: `python -m modules.pipeline` →
  `*-results.html`.
- Habitat-tree **`LassoCV` ≠ paper primary.** Do not quote tree-script coefficients or AUCs
  as the manuscript result.
- **Nested CV is not implemented.** Do not write that the lab used nested CV, 10×10 nested
  CV, or nested selection inside outer performance folds. You may say nested CV is not
  implemented.
- Harrell bootstrap optimism correction is **not** a lab default.

Do not vendor `D:\0Grok\0RAD` Python. Full lock: `04_analysis/references/0rad-pipeline-rules.md`.

## 1. Multiple testing

- **Family-wise error (FWER)**: Bonferroni (strict), **Holm** (uniformly better than
  Bonferroni). Use when any false positive is costly / few tests.
- **False discovery rate (FDR)**: **Benjamini-Hochberg** (independent/positively dependent),
  Benjamini-Yekutieli (arbitrary dependence), Storey **q-values**. Use for discovery across
  many features/genes.
- **Pre-specify** the primary hypothesis (escapes correction); treat the feature-wide scan as
  exploratory and FDR-controlled.
- Report the **family** (how many tests) and the method.

```python
from statsmodels.stats.multitest import multipletests
rej, q, _, _ = multipletests(pvals, alpha=0.05, method="fdr_bh")
```

## 2. Overfitting & optimism

- With p ≫ n, in-sample performance is meaningless. The lab honest-validation path is a
  **patient-level train/test split** plus train-only LASSO (StratifiedKFold AUC path) and
  held-out / external scoring under `VAL_MODE`.
- **Nested cross-validation** (outer loop estimates performance; inner loop does feature
  selection + tuning) is textbook honest validation — **not implemented** in the lab
  pipeline. Single-loop CV with selection on all data is still **optimistically biased**;
  do not do that either, and do not relabel train-only LASSO as nested CV.
- **Dimensionality control**: pre-filter by ICC(A,1) ≥ 0.75, then LASSO on TRAIN.
- Watch **events-per-variable** — see sample-size.md (Riley).

## 3. Leakage (the silent killer)

Everything data-dependent must be fit on the **training set only**, then applied to
validation/test:

- feature scaling/normalisation, **discretisation** choices, **ComBat harmonisation**,
  feature selection, class-balancing (SMOTE), imputation, and threshold selection.
- **Patient-level** splits; never let the same patient (or augmented copies) span folds.
- Temporal/site leakage: prefer temporal or external validation for the headline claim.

## 4. Batch / scanner effects (radiomics & sequencing)

- Radiomic features and gene-expression both carry strong **batch/scanner** signal.
- **ComBat** (and `neuroCombat`/`ComBatHarmonization`; for RNA-seq, `sva::ComBat_seq`)
  removes batch while **preserving biological covariates** — include the biology in the model
  so it is not removed. Fit on training, transform test.
- Always test whether your "signal" is actually scanner/site: stratify, adjust, or show the
  effect survives harmonisation.

## 5. Correlation, not causation; and stability

- Report **effect sizes + CIs**, not just stars.
- Show **feature stability** when it was actually computed. Do not invent bootstrap
  selection frequencies. A feature picked in 5% of bootstraps is not a biomarker.

## Reporting sentence

*"Of 1218 IBSI-compliant features (ICC(A,1) ≥ 0.75), LASSO with a StratifiedKFold AUC path
on the training set retained k coefficients for the RadScore. The Combined (primary) model
was evaluated on the held-out test set without reselection (AUC …; 95% CI …; 1000 bootstrap).
Nested CV was not used."*

Do not write a 10×10 nested-CV sentence as if it were the lab run.

## Reviewer hot-spots

Selection/harmonisation on all data; nested CV claimed when the lab used train-only LASSO;
habitat-tree `LassoCV` quoted as the paper model; thousands of tests with no correction;
SMOTE before the split; "AUC 0.99" on n = 40 with 800 features; batch effect not addressed.
