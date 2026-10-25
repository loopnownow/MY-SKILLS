# Methods handbook (02)

Merged 2026-10-16 from personal topic files. Use with `module-notes.md` as thin index.


---

## General statistics index

## Statistics

Use this file when the user asks about statistical analysis plans, sample size,
feature selection, modeling, metrics, survival analysis, calibration, decision curve
analysis, confidence intervals, or statistical reporting for radiomics and medical
imaging AI studies.

### Core goal

The stats module turns “AUC looks high” into designs, analyses, and reports that can be audited. Prefer checking
data unit, event counts, validation scheme, where feature selection ran, metric completeness, and claim strength.

### First questions

- Is the task diagnosis, subtyping, staging, prognosis, recurrence, treatment response, segmentation, or detection?
- Is the analysis unit patient, lesion, slice, scan, time point, or patch?
- What are sample size, positive/negative counts, events, censoring rate, and follow-up time?
- How are train / validation / test / external validation split? Patient-level and center-level?
- Inside which dataset did feature selection, scaling, imputation, ComBat, and threshold choice run?
- Which models: clinical, radiomics, deep learning, combined?
- What are the primary metrics and the prespecified primary endpoint?
- Are calibration, DCA, CIs, sensitivity analyses, and subgroups present?

### Study type to analysis route

| Task | Core model families | Main metrics | Must check |
|---|---|---|---|
| Binary classification | logistic regression, SVM, RF, XGBoost, neural net | AUC, sensitivity, specificity, PPV, NPV, calibration, DCA | threshold selection and leakage |
| Multiclass classification | multinomial models, tree ensembles, deep learning | macro/micro AUC, F1, balanced accuracy, confusion matrix | class imbalance |
| Prognosis | Cox, penalized Cox, RSF, DeepSurv | C-index, time-dependent AUC, calibration, KM | events per variable and censoring |
| Treatment response | logistic/Cox, delta-radiomics, longitudinal models | AUC, ORR/pCR metrics, PFS/OS metrics | response definition and time window |
| Segmentation | U-Net variants, nnU-Net, SAM-style models | Dice, IoU, Hausdorff, surface Dice | test-set independence and small lesions |
| Detection | detection networks, CAD pipelines | FROC, sensitivity per lesion, false positives per scan | lesion-level vs patient-level reporting |

### Sample size and events

- Start from number of patients, not number of images or slices.
- For binary prediction, report class counts and event fraction.
- For survival analysis, report number of events, median follow-up, censoring rate.
- For radiomics feature models, high-dimensional features require aggressive internal validation and shrinkage.
- Avoid many predictors with few events; if events are limited, prefer simpler models, fewer features, penalization, or prespecified features.
- Do not claim adequate power without a study-specific calculation or rationale.

### Leakage-sensitive pipeline

Every preprocessing or selection step must be fit inside training data only:

1. Split by patient first.
2. Fit imputation on training data.
3. Fit scaling/normalization on training data.
4. Fit harmonization parameters without leaking test labels; be cautious with ComBat.
5. Run feature stability filtering using training data or prespecified reproducibility data.
6. Run univariable screening, correlation filtering, LASSO/mRMR/RFE only inside training folds.
7. Tune hyperparameters inside validation or inner cross-validation.
8. Lock the final model before touching the test set.
9. Use external validation only once for final assessment.

### Feature selection

Common options:

- Variance or near-zero variance filter.
- Reproducibility filter by ICC.
- Correlation filter for redundancy.
- mRMR or mutual information.
- LASSO or elastic net.
- Recursive feature elimination.
- Tree-based importance.
- Clinical-prior feature set.

Warnings:

- Do not run feature selection on the full dataset before splitting.
- Do not report selected features as biologically important without stability or external evidence.
- Do not select features based on test-set performance.
- Repeat selection inside every resampling fold when reporting cross-validation performance.

### Metrics and reporting

#### Classification

Minimum:

- AUC with 95% CI
- sensitivity, specificity, PPV, NPV
- threshold selection method
- confusion matrix
- calibration curve or calibration slope/intercept
- decision curve analysis when clinical utility is claimed

Optional:

- PR-AUC for imbalanced data
- Brier score
- net reclassification improvement only when justified
- subgroup analysis by center, scanner, stage, sex, age, treatment

#### Survival

Minimum:

- C-index with 95% CI
- time-dependent AUC at clinically meaningful time points
- calibration at fixed time points
- hazard ratio with CI if risk groups are used
- Kaplan-Meier curves with number at risk
- proportional hazards assumption check when using Cox

Do not dichotomize risk score by an optimized full-cohort cut-off. If a cut-off is used,
derive it in training data and apply unchanged to validation data.

#### Segmentation and detection

- Report patient-level and lesion-level metrics separately when both are relevant.
- Include confidence intervals or bootstrap uncertainty.
- Report failure cases and small-lesion performance if clinically important.
- Do not use validation data for model selection and then call it an independent test set.

### Output format

```text
Stats framing
- Task type:
- Analysis unit:
- Sample size / events:
- Current models:

Main risks
- [leakage, low events, class imbalance, missing calibration, weak validation]

Recommended stats route
- Data split:
- Feature selection:
- Models:
- Metrics:
- Sensitivity / subgroups:

Methods/Results still need
- [specific missing details]

Needs author confirmation
- [numbers and analysis facts]
```

### Red lines

- Do not equate image/slice count with independent sample size.
- Do not allow feature selection, scaling, imputation, or threshold tuning on test data.
- Do not treat AUC alone as sufficient evidence of clinical value.
- Do not fabricate p-values, confidence intervals, event counts, cut-offs, or sample-size calculations.
- Do not recommend complex models when event count and validation design cannot support them.


---

### Diagnostic accuracy

## Diagnostic accuracy — estimates, CIs, paired comparison

### The 2×2 and its metrics
From TP, FP, FN, TN against a reference standard:
- **Sensitivity** = TP/(TP+FN); **Specificity** = TN/(TN+FP).
- **PPV/NPV** depend on **prevalence** — report the prevalence; if the sample is enriched
  (e.g. 1:1), compute PPV/NPV at a realistic prevalence using Bayes, and say so.
- **Accuracy** is prevalence-dependent and usually uninformative alone.
- **Likelihood ratios**: LR+ = sens/(1−spec); LR− = (1−sens)/spec. Prevalence-independent;
  reviewers like them.

### Confidence intervals (do not use plain Wald for proportions)
- Proportions (sens, spec, PPV, NPV): **Wilson** (good default) or **Clopper-Pearson**
  (exact, conservative). Avoid Wald near 0/1.
- Likelihood ratios: log-based CI (or bootstrap).
- Lab AUC 95% CI (when an ROC is run) is 1000 bootstrap (`_boot_auc_ci`), not a DeLong interval. See model-evaluation.md.
- Report counts with each estimate (e.g. `0.87 (130/149)`).

```python
import numpy as np
from statsmodels.stats.proportion import proportion_confint

def diag_metrics(tp, fp, fn, tn, method="wilson"):
    sens = tp/(tp+fn); spec = tn/(tn+fp)
    sens_ci = proportion_confint(tp, tp+fn, method=method)
    spec_ci = proportion_confint(tn, tn+fp, method=method)
    ppv = tp/(tp+fp); npv = tn/(tn+fn)
    ppv_ci = proportion_confint(tp, tp+fp, method=method)
    npv_ci = proportion_confint(tn, tn+fn, method=method)
    lr_pos = sens/(1-spec); lr_neg = (1-sens)/spec
    return dict(sens=(sens,sens_ci), spec=(spec,spec_ci),
                ppv=(ppv,ppv_ci), npv=(npv,npv_ci),
                lr_pos=lr_pos, lr_neg=lr_neg)
```

### Comparing two tests on the SAME patients (paired)
- **Sensitivity/specificity** (binary calls): **McNemar's test** on the discordant pairs
  (within the diseased subset for sensitivity, non-diseased for specificity).
- Do **not** use a chi-square for independent groups when the same cases were read twice.

```python
from statsmodels.stats.contingency_tables import mcnemar
# table = [[both_correct, A_correct_B_wrong],[A_wrong_B_correct, both_wrong]]
print(mcnemar(table, exact=True))   # exact for small discordant counts
```

### Clustered data (multiple lesions per patient)
Lesions within a patient are correlated. Use cluster-robust / GEE / mixed-effects, or
analyse at the patient level. Reporting per-lesion accuracy as if independent **inflates
significance** — a common reviewer catch.

### Reporting sentence
*"At the pre-specified threshold, sensitivity was 0.87 (95% CI: 0.81, 0.92; 130/149) and
specificity 0.79 (95% CI: 0.72, 0.85; 158/200); disease prevalence was 0.27. The model and
radiologists differed in sensitivity (P = .02, McNemar)."*

### Reviewer hot-spots
Threshold chosen on the test set; PPV/NPV quoted from an enriched sample as if clinical;
independence assumed for clustered lesions; missing CIs; "accuracy" headline hiding poor
sensitivity at clinical prevalence.


---

### Model evaluation

## Model evaluation — ROC/AUC, DeLong p, calibration, decision-curve

A clinical prediction model needs **three** things reported: **discrimination**,
**calibration**, and **clinical utility**. AUC alone is not enough (TRIPOD+AI, PROBAST).

Lab pipeline **v4.3.0** (2026-08-28): Combined = named primary. Numbers from
`python -m modules.pipeline`, not habitat-tree `LassoCV`. Details:
`02_data-processing/personal/analysis/pipeline.md`.

### Discrimination — ROC/AUC

- **AUC 95% CI = 1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals. Do not quote
  a DeLong analytic CI as what the lab ran.
- Report sensitivity/specificity at the operating point the lab actually used: **Youden per
  split** on `VAL_MODE` `refit` / `apply_formula`; **training** Youden only under
  `lock_threshold`. Never pick the cut that maximises test-set accuracy.

### Comparing AUCs (DeLong is a p, not a CI)

- **Paired** (same cases, lab default): DeLong test, Sun & Xu (2014) midranks. Added
  2026-08-28. Columns `DeLong vs {model}` in `ROC_METRICS`. Use this p for Combined vs
  RadScore / Clinical / other named models on the same split.
- DeLong does **not** supply the lab AUC interval — that stays 1000 bootstrap.
- Unpaired DeLong and bootstrap-of-the-difference are journal-grade options, **not** lab
  defaults.
- For models vs readers in a reader study → use **MRMC** (see agreement-mrmc.md), not a plain
  DeLong, because both readers and cases are random.

Do not vendor `{code_root}` Python. Do not `pip install delong` / call R `pROC` as if that
were the lab runner.

### Calibration (frequently missing → reviewer flag)

- **Calibration plot**: predicted probability (x) vs observed frequency (y), with a loess/
  binned curve; ideal = diagonal. Lab: `modules.stats.curves_calibration.plot_calibration`.
- **Calibration slope** (ideal 1) and **intercept / calibration-in-the-large** (ideal 0).
- **Brier score** (lower better); decompose if useful.
- **Hosmer–Lemeshow (lab)**: quantile bins matching the calibration curve (default **8**),
  χ² with **df = G−2**, table in `*-results.html` via `HL_METRICS` — **not** drawn on the
  figure. Still do **not** report HL alone; always show the curve. Do not claim the lab has
  “no HL”.
- `VAL_MODE` `lock_threshold` / `refit`: call calibration with **`recalibrate=False`**.

```python
from sklearn.calibration import calibration_curve
import numpy as np
frac_pos, mean_pred = calibration_curve(y_true, y_prob, n_bins=8, strategy="quantile")
brier = np.mean((y_prob - y_true)**2)
```

### Clinical utility — decision-curve analysis (DCA)

- Plots **net benefit** vs threshold probability against "treat all"/"treat none".
- Answers "is using this model better than default strategies across plausible thresholds?"
- Lab DCA is produced by `modules.pipeline`. Python `dcurves` / R `rmda` are not the lab runner.

### Threshold selection — say where it came from

Pre-specify (clinical target sensitivity), or derive on training. **Never** pick the
threshold that maximises test-set accuracy.

Lab pipeline implements this as `VAL_MODE` = `refit` | `apply_formula` | `lock_threshold`
(features never re-selected). Youden is **per split** unless locked. Definitions:
`02_data-processing/personal/analysis/pipeline.md`.

### Reporting sentence

*"The Combined model discriminated well (AUC 0.88; 95% CI: 0.84, 0.92; 1000 bootstrap) and
was well calibrated (slope 0.96, intercept 0.02; Brier 0.11). Decision-curve analysis showed
positive net benefit across threshold probabilities of 0.10–0.40. Versus the clinical model,
DeLong P = .004."*

### Reviewer hot-spots

AUC-only; DeLong quoted as the AUC CI; threshold tuned on test set; no calibration;
optimistic (no external/independent test); nested CV claimed when the lab used train-only
LASSO; class imbalance ignored (report PR-AUC/sensitivity at clinical prevalence too).


---

### Survival & prognostic

## Survival & prognostic modelling

Use when the endpoint is **time-to-event** (OS, PFS, recurrence). Common in radiogenomics
(imaging/omics signature → prognosis).

### Lab pipeline (v4.3.0) — what actually runs

- **Always:** Kaplan–Meier curves + **log-rank** for group comparison. Report median
  survival with 95% CI and numbers-at-risk under the x-axis (a _Radiology_ figure
  expectation). HTML: if a curve is drawn twice (sidebar + main), keep the **main** pane only.
- **Optional Cox (off by default):** univariable Cox via `statsmodels.duration.hazard_regression.PHReg`,
  Breslow ties. Library default **`DO_COX = False`**. Not lifelines, not `CoxPHFitter`.
- Contrasts, when Cox is on: **High vs Low** at the **train-median** cut of the score, and
  **per 1 SD**. Report **HR, 95% CI, P, N, Events, Schoenfeld `PH_p`**.
- **Not implemented / not lab default:** multivariate Cox, C-index, time-dependent AUC,
  competing-risks (Fine-Gray), RMST. You may say these are not implemented. Never write them
  as what the lab ran.

Do not vendor `{code_root}` Python.

```python
# Optional univariable Cox — statsmodels PHReg, Breslow. Not lifelines.
# Lab library default: DO_COX = False.
from statsmodels.duration.hazard_regression import PHReg
# High vs Low uses the training-set median cut; also fit per 1 SD.
# Export HR, 95% CI, P, N, Events, Schoenfeld PH_p. Univariable only.
```

### Journal-grade extras (not lab defaults)

- **C-index** (Harrell's) and **time-dependent AUC** at a horizon; **calibration** at fixed
  time points (e.g. 1/3/5-yr).
- **Competing risks** — if non-event deaths compete, use cumulative incidence
  (Aalen-Johansen) and **Fine-Gray**, not naive KM.
- Multivariate Cox. Not implemented in the lab pipeline.

### Assumptions & pitfalls

- **Proportional hazards** — lab Cox reports Schoenfeld `PH_p`. If violated, do not silently
  quote the HR; say PH failed. Journal-grade remedies (time-varying coefficients,
  stratification, RMST) are not lab defaults.
- **Dichotomising a continuous score** at an "optimal" cutpoint inflates significance. The
  lab cut is **train-median**, not an outcome-optimised Youden cut on the same survival data.
  Also report the per-1-SD HR (keeps the score continuous).
- **EPV** for Cox = events per variable (aim ≥ 10–15, or use Riley). Imaging/omics
  signatures: build the signature on TRAIN, then optional univariable Cox on that score — not
  800 raw features.
- **Immortal-time / lead-time bias** — define time-zero and exposure carefully.
- **Independent validation** of a prognostic signature is expected.

### Reporting sentence

*"High versus low Combined score (train-median cut) was associated with overall survival
(HR 2.1; 95% CI: 1.4, 3.2; P = .001; N = 180; events = 62; Schoenfeld PH_p = .34). Per 1 SD,
HR was 1.6 (95% CI: 1.2, 2.1). Log-rank P = .002. Multivariate Cox was not run."*

Fill only from pipeline output; if `DO_COX` was False, report KM + log-rank only.

### Reviewer hot-spots

Optimal cut-point on the same cohort; PH not tested; competing risks ignored; HR reported
without CI; Cox claimed as default when `DO_COX` is False; lifelines/`CoxPH` named as the lab
library; signature overfit (Cox on raw high-dimensional features); nested CV claimed; no
external validation.


---

### Agreement & MRMC

## Agreement & multi-reader multi-case (MRMC)

### Pick the agreement statistic by data type
| Data | Statistic |
|---|---|
| 2 readers, nominal categories | **Cohen's kappa** |
| 2 readers, **ordered** categories (e.g. BI-RADS, Likert) | **weighted kappa** (linear or quadratic — state which) |
| ≥ 3 readers, nominal | **Fleiss' kappa** |
| Continuous (size, SUV, volume) | **ICC** + **Bland-Altman** |
| Ordinal/continuous, rank concordance | Kendall's W |

- Report **kappa with 95% CI** and an interpretation band, but note kappa depends on
  prevalence/marginal distributions (report observed agreement too).
- For continuous measurements, **kappa is wrong** — use ICC and Bland-Altman.

### ICC — you must specify the model
Report the full specification (McGraw & Wong / Koo & Li form), e.g. *"ICC(A,1), two-way
mixed-effects, absolute agreement, single rater."* Choices:
- **Model**: one-way random / two-way random (raters are a sample) / two-way mixed (these
  specific raters).
- **Type**: absolute agreement vs consistency.
- **Unit**: single rater vs mean of k raters.
Using "consistency" when you need "absolute agreement" silently hides systematic bias.

Lab pipeline radiomics filter: keep features with **ICC(A,1) ≥ 0.75**. Do not write an
unspecified "ICC > 0.75" as the lab rule.

```python
import pingouin as pg          # pip install pingouin
icc = pg.intraclass_corr(data=long_df, targets="case", raters="reader", ratings="value")
# Lab radiomics filter uses ICC(A,1) ≥ 0.75 (absolute agreement, single rater).
# pingouin ICC2 / ICC3-style rows must be matched to that McGraw & Wong label — do not pick ICC(C,k).
```

### Bland-Altman (continuous, two methods/readers)
Plot mean vs difference; report **bias** (mean difference) and **95% limits of agreement**
(bias ± 1.96·SD). Check for proportional bias (trend vs magnitude). Hand the plot to
live `plot-figures`.

### MRMC — the right framework for reader studies
When **multiple readers** each read **multiple cases** (e.g. AI-vs-no-AI, or comparing
modalities), both readers and cases are random effects. Averaging readers and running a
plain DeLong **underestimates variance** and overstates significance.

- **Designs**: fully crossed (every reader reads every case) is most powerful; report the
  design.
- **Analysis**: **Obuchowski-Rockette (OR)** and **Dorfman-Berbaum-Metz (DBM)** (now unified,
  "OR-DBM") for AUC/figure-of-merit differences; **iMRMC** (FDA) or R **`RJafroc`**.
- **Endpoints**: ROC AUC, or location-specific (JAFROC/wAFROC) when localisation matters
  (detection tasks).
- **Reader-averaged** estimate with CI; conclusion about the **reader population**, not just
  these readers.
- **Power/sample size** before the study (number of readers × cases) — see sample-size.md.

```r
# R, FDA-endorsed:
library(RJafroc)
result <- StSignificanceTesting(dataset, FOM = "Wilcoxon", method = "OR")
```

### Reporting sentences
*"Radiomic features with ICC(A,1) < 0.75 were excluded. Inter-reader agreement was
substantial (ICC(A,1) = 0.82; 95% CI: 0.75, 0.87; two-way mixed, absolute agreement, single
rater)."*
*"In the MRMC analysis (6 readers, 300 cases, fully crossed), reader-averaged AUC improved
from 0.81 to 0.87 with AI assistance (difference 0.06; 95% CI: 0.02, 0.10; P = .005;
Obuchowski-Rockette)."*

### Reviewer hot-spots
ICC model unspecified (lab rule is ICC(A,1) ≥ 0.75); kappa used for continuous data; readers averaged then DeLong'd;
fixed-reader conclusion generalised to all radiologists; no pre-study power for the reader
study.


---

### Sample size & power

## Sample size & power for imaging studies

Pre-specify and **justify** sample size (CLAIM, TRIPOD+AI, STARD all ask). Below are the
common cases. A retrospective cohort whose N is already fixed still uses one of the four
approaches in the next section. It does not get an observed-power number.

### Retrospective study with a fixed N

Do not compute post-hoc power, or observed power, from the p value already obtained.
That number restates the p value. BMJ/JAMA-style statistical review rejects it. In a
response letter the anchor is Hoenig & Heisey 2001. Do not add other citations for this point.

Use one of these four. Methods names which one. Do not add a fill-in manuscript sentence
that invents n, an effect size, or a power.

1. **Pre-study power.** Take the effect size from the literature or a pilot, then show
   that the enrolled N meets it. Alpha 0.05, two-sided; power 0.80 or 0.90. Tools:
   G*Power, PASS, or R `pwr` (`pwr.t.test`, `pwr.2p.test`).
2. **Events, not a two-group formula.** Multivariable logistic or Cox, radiomics, and
   prediction models use events-per-variable **10–15**, and Riley / R `pmsampsize` when
   the journal expects a minimum sample size. A classical two-group formula does not
   cover these.
3. **Minimum detectable effect (N already fixed).** Report the MDES at 80% power and
   set it next to a clinical difference. Do not call that observed power. Same tools as
   (1), with the enrolled n supplied and the effect size solved for.
4. **Precision.** When the aim is an estimate rather than a test, size N from the CI
   half-width. The sensitivity formula below is this case.

A **10–20%** drop-out allowance is only a planned exclusion (some enrolled cases will
not enter the analysis). It is not a new gate, and it is not added after the fact to a
retrospective cohort whose N is already the analysis N.

### Reviewer response

If asked for post-hoc power, refuse it. Offer the CI width, or the MDES at 80% power
against a clinical difference. Small N goes in Limitations as a possible type II error,
not as a calculated observed power.

### Diagnostic accuracy (sensitivity/specificity)
Sensitivity is estimated only in **diseased** patients, specificity in **non-diseased** — so
prevalence drives how many *total* patients you need. The half-width formula is approach 4.
Powering a hypothesis (sensitivity ≥ a target) is approach 1, or approach 3 when N is
already fixed.

- To estimate a sensitivity `Se` with half-width `w` at 95%:
  `n_diseased ≈ 1.96² · Se(1−Se) / w²`, then `n_total ≈ n_diseased / prevalence`.
- Tools: R `presize`, `MKpower`, `pwr`.

```python
import math
def n_for_sensitivity(se=0.90, half_width=0.05, prevalence=0.15, z=1.96):
    n_dis = (z**2 * se*(1-se)) / half_width**2
    return math.ceil(n_dis), math.ceil(n_dis / prevalence)
# e.g. Se 0.90, ±0.05, prev 0.15 -> diseased and total n
```

### AUC
Power to detect an AUC vs 0.5, or a difference between two AUCs (Hanley-McNeil / Obuchowski).
Inputs: expected AUCs, correlation (paired), allocation, prevalence. R `pROC::power.roc.test`,
`MCPmod`, or Obuchowski formulas. That is approach 1. With N already fixed, report the
MDES on the AUC difference (approach 3). Do not report observed power.

### Prediction models — EPV and Riley
Approach 2. Rule of thumb: **events-per-variable (EPV) 10–15** (development) — still crude.
- Use **Riley et al. minimum sample size** for prediction models when the journal expects
  it: targets small optimism, precise overall risk, and a calibration-slope ~1. R
  **`pmsampsize`** (dev) and **`pmvalidsize`** (validation). For **external validation**,
  target enough **events** (often ≥ 100 events and ≥ 100 non-events) for stable calibration.
- Do not substitute a classical two-group formula.

```r
library(pmsampsize)
pmsampsize(type="b", cstatistic=0.80, prevalence=0.2, parameters=20)
```

### MRMC reader studies
Power depends on **#readers × #cases**, the AUC difference, and variance components
(between-reader, within-reader). Use **OR/DBM** power tools: R `RJafroc::SsPowerGivenJK` or
FDA **iMRMC**. Pilot variance estimates make this far more reliable. Same split as above:
pre-study power (approach 1) or, if the reader×case grid is already fixed, the MDES
(approach 3). Not observed power.

### High-dimensional radiomics/omics
No single n powers thousands of features. Pre-specify the **primary** comparison and power
that (approach 1 or 3); size a prediction model with approach 2. Treat the feature scan as
FDR-controlled discovery; plan an **independent validation** cohort rather than relying on
one small cohort.

### Methods wording
Name which of the four approaches was used, the inputs that are real (literature or pilot
effect, alpha, target power, event count, or the CI half-width / MDES), and whether the
enrolled N met that target. Numbers come from that calculation or from the enrolled
cohort. Do not invent them.

### Reviewer hot-spots
No sample-size justification; EPV below 10; post-hoc / observed power from the obtained p;
a two-group formula on a prediction model; an MDES written up as observed power; a 10–20%
drop-out tacked on after N is fixed; reader study with too few readers; test / validation
set with too few events for calibration.


---

### High-dimensional / omics

## High-dimensional statistics — radiomics & multi-omics

The defining problem: **features ≫ samples**. Matched imaging+omics cohorts are small
(often n < 100), while features run to thousands (radiomics) or tens of thousands (genes).
This breaks naive analysis in three ways: multiplicity, overfitting/optimism, and leakage.

### Lab pipeline (v4.3.0) — what actually runs

- Radiomics reproducibility filter: keep features with **ICC(A,1) ≥ 0.75**.
- **LASSO:** StratifiedKFold **AUC path on TRAIN only**. Coefficients lock; test set is not
  re-screened.
- Clinical covariates: non-empty `FORCE_MODEL_FEATURES` is the model. Empty list uses candidate-pool multivariate p < `ROC_MV_P_THRESHOLD`.
- Primary model = **Combined**. Primary numbers: `python -m modules.pipeline` →
  `*-results.html`.
- Habitat-tree **`LassoCV` ≠ paper primary.** Do not quote tree-script coefficients or AUCs
  as the manuscript result.
- **Nested CV is not implemented.** Do not write that the lab used nested CV, 10×10 nested
  CV, or nested selection inside outer performance folds. You may say nested CV is not
  implemented.
- Harrell bootstrap optimism correction is **not** a lab default.

Do not vendor `{code_root}` Python. Full lock: `02_data-processing/personal/analysis/pipeline.md`.

### 1. Multiple testing

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

### 2. Overfitting & optimism

- With p ≫ n, in-sample performance is meaningless. The lab honest-validation path is a
  **patient-level train/test split** plus train-only LASSO (StratifiedKFold AUC path) and
  held-out / external scoring under `VAL_MODE`.
- **Nested cross-validation** (outer loop estimates performance; inner loop does feature
  selection + tuning) is textbook honest validation — **not implemented** in the lab
  pipeline. Single-loop CV with selection on all data is still **optimistically biased**;
  do not do that either, and do not relabel train-only LASSO as nested CV.
- **Dimensionality control**: pre-filter by ICC(A,1) ≥ 0.75, then LASSO on TRAIN.
- Watch **events-per-variable** — see sample-size.md (Riley).

### 3. Leakage (the silent killer)

Everything data-dependent must be fit on the **training set only**, then applied to
validation/test:

- feature scaling/normalisation, **discretisation** choices, **ComBat harmonisation**,
  feature selection, class-balancing (SMOTE), imputation, and threshold selection.
- **Patient-level** splits; never let the same patient (or augmented copies) span folds.
- Temporal/site leakage: prefer temporal or external validation for the headline claim.

### 4. Batch / scanner effects (radiomics & sequencing)

- Radiomic features and gene-expression both carry strong **batch/scanner** signal.
- **ComBat** (and `neuroCombat`/`ComBatHarmonization`; for RNA-seq, `sva::ComBat_seq`)
  removes batch while **preserving biological covariates** — include the biology in the model
  so it is not removed. Fit on training, transform test.
- Always test whether your "signal" is actually scanner/site: stratify, adjust, or show the
  effect survives harmonisation.

### 5. Correlation, not causation; and stability

- Report **effect sizes + CIs**, not just stars.
- Show **feature stability** when it was actually computed. Do not invent bootstrap
  selection frequencies. A feature picked in 5% of bootstraps is not a biomarker.

### Reporting sentence

*"Of 1218 IBSI-compliant features (ICC(A,1) ≥ 0.75), LASSO with a StratifiedKFold AUC path
on the training set retained k coefficients for the RadScore. The Combined (primary) model
was evaluated on the held-out test set without reselection (AUC …; 95% CI …; 1000 bootstrap).
Nested CV was not used."*

Do not write a 10×10 nested-CV sentence as if it were the lab run.

### Reviewer hot-spots

Selection/harmonisation on all data; nested CV claimed when the lab used train-only LASSO;
habitat-tree `LassoCV` quoted as the paper model; thousands of tests with no correction;
SMOTE before the split; "AUC 0.99" on n = 40 with 800 features; batch effect not addressed.
