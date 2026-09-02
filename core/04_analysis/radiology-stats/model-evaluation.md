# Model evaluation — ROC/AUC, DeLong p, calibration, decision-curve

A clinical prediction model needs **three** things reported: **discrimination**,
**calibration**, and **clinical utility**. AUC alone is not enough (TRIPOD+AI, PROBAST).

Lab 0RAD **v4.3.0** (2026-08-28): Combined = named primary. Numbers from
`python -m modules.pipeline`, not habitat-tree `LassoCV`. Details:
`04_analysis/references/0rad-pipeline-rules.md`.

## Discrimination — ROC/AUC

- **AUC 95% CI = 1000 bootstrap** (`_boot_auc_ci`). **Not** DeLong intervals. Do not quote
  a DeLong analytic CI as what the lab ran.
- Report sensitivity/specificity at the operating point the lab actually used: **Youden per
  split** on `VAL_MODE` `refit` / `apply_formula`; **training** Youden only under
  `lock_threshold`. Never pick the cut that maximises test-set accuracy.

## Comparing AUCs (DeLong is a p, not a CI)

- **Paired** (same cases, lab default): DeLong test, Sun & Xu (2014) midranks. Added
  2026-08-28. Columns `DeLong vs {model}` in `ROC_METRICS`. Use this p for Combined vs
  RadScore / Clinical / other named models on the same split.
- DeLong does **not** supply the lab AUC interval — that stays 1000 bootstrap.
- Unpaired DeLong and bootstrap-of-the-difference are journal-grade options, **not** lab
  defaults.
- For models vs readers in a reader study → use **MRMC** (see agreement-mrmc.md), not a plain
  DeLong, because both readers and cases are random.

Do not vendor `D:\0Grok\0RAD` Python. Do not `pip install delong` / call R `pROC` as if that
were the lab runner.

## Calibration (frequently missing → reviewer flag)

- **Calibration plot**: predicted probability (x) vs observed frequency (y), with a loess/
  binned curve; ideal = diagonal.
- **Calibration slope** (ideal 1) and **intercept / calibration-in-the-large** (ideal 0).
- **Brier score** (lower better); decompose if useful.
- Avoid relying on **Hosmer-Lemeshow** alone (low power, binning-dependent); show the curve.

```python
from sklearn.calibration import calibration_curve
import numpy as np
frac_pos, mean_pred = calibration_curve(y_true, y_prob, n_bins=10, strategy="quantile")
brier = np.mean((y_prob - y_true)**2)
```

## Clinical utility — decision-curve analysis (DCA)

- Plots **net benefit** vs threshold probability against "treat all"/"treat none".
- Answers "is using this model better than default strategies across plausible thresholds?"
- Lab DCA is produced by `modules.pipeline`. Python `dcurves` / R `rmda` are not the lab runner.

## Threshold selection — say where it came from

Pre-specify (clinical target sensitivity), or derive on training. **Never** pick the
threshold that maximises test-set accuracy.

Lab 0RAD implements this as `VAL_MODE` = `refit` | `apply_formula` | `lock_threshold`
(features never re-selected). Youden is **per split** unless locked. Definitions:
`04_analysis/references/0rad-pipeline-rules.md`.

## Reporting sentence

*"The Combined model discriminated well (AUC 0.88; 95% CI: 0.84, 0.92; 1000 bootstrap) and
was well calibrated (slope 0.96, intercept 0.02; Brier 0.11). Decision-curve analysis showed
positive net benefit across threshold probabilities of 0.10–0.40. Versus the clinical model,
DeLong P = .004."*

## Reviewer hot-spots

AUC-only; DeLong quoted as the AUC CI; threshold tuned on test set; no calibration;
optimistic (no external/independent test); nested CV claimed when the lab used train-only
LASSO; class imbalance ignored (report PR-AUC/sensitivity at clinical prevalence too).
