# Survival & prognostic modelling

Use when the endpoint is **time-to-event** (OS, PFS, recurrence). Common in radiogenomics
(imaging/omics signature → prognosis).

## Lab 0RAD (v4.3.0) — what actually runs

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

Do not vendor `D:\0Grok\0RAD` Python.

```python
# Optional univariable Cox — statsmodels PHReg, Breslow. Not lifelines.
# Lab library default: DO_COX = False.
from statsmodels.duration.hazard_regression import PHReg
# High vs Low uses the training-set median cut; also fit per 1 SD.
# Export HR, 95% CI, P, N, Events, Schoenfeld PH_p. Univariable only.
```

## Journal-grade extras (not lab defaults)

- **C-index** (Harrell's) and **time-dependent AUC** at a horizon; **calibration** at fixed
  time points (e.g. 1/3/5-yr).
- **Competing risks** — if non-event deaths compete, use cumulative incidence
  (Aalen-Johansen) and **Fine-Gray**, not naive KM.
- Multivariate Cox. Not implemented in the lab pipeline.

## Assumptions & pitfalls

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

## Reporting sentence

*"High versus low Combined score (train-median cut) was associated with overall survival
(HR 2.1; 95% CI: 1.4, 3.2; P = .001; N = 180; events = 62; Schoenfeld PH_p = .34). Per 1 SD,
HR was 1.6 (95% CI: 1.2, 2.1). Log-rank P = .002. Multivariate Cox was not run."*

Fill only from pipeline output; if `DO_COX` was False, report KM + log-rank only.

## Reviewer hot-spots

Optimal cut-point on the same cohort; PH not tested; competing risks ignored; HR reported
without CI; Cox claimed as default when `DO_COX` is False; lifelines/`CoxPH` named as the lab
library; signature overfit (Cox on raw high-dimensional features); nested CV claimed; no
external validation.
