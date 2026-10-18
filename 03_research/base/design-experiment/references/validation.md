# 验证

Use this file whenever model credibility, performance, data leakage, metrics, or
generalizability is being discussed.

## Leakage checks

Block or flag the study if:

- the same patient appears in train and test
- slices, lesions, phases, or follow-up scans from one patient are split across sets
- feature selection, normalization, harmonization, imputation, or augmentation is fit
  before the train/test split
- test data are used for threshold selection, model selection, or early stopping
- external validation is from the same source population without clear independence

Use `scripts/split_leakage_check.py` when a CSV with patient and split columns is available.

## Validation levels

| Level | Meaning |
|---|---|
| resubstitution | training performance only; not valid evidence |
| internal CV | useful for development, limited generalizability |
| internal holdout | better than CV if untouched |
| temporal validation | tests time shift within setting |
| external validation | tests site/scanner/population shift |
| prospective validation | strongest for clinical workflow claims |

## Metrics by task

| Task | Primary metrics | Add when claiming clinical utility |
|---|---|---|
| Classification | AUC, sensitivity, specificity, PR-AUC, CI | calibration, DCA, threshold analysis |
| Prognosis/survival | C-index, time-dependent AUC, calibration, HR | decision impact, subgroup checks |
| Segmentation | Dice, HD95, surface Dice, volume difference | reader comparison, failure cases |
| Detection | sensitivity, FROC, false positives per scan | lesion size and subgroup analysis |
| Regression | MAE, RMSE, R2, calibration | clinical error bands |

## Output

```text
Validation verdict
- Split unit:
- Leakage risk:
- Internal validation:
- External validation:
- Metrics:
- Calibration/utility:
- Required fixes:
```
