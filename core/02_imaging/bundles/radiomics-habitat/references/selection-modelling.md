# Feature selection, modelling & the signature/score

The single rule: **every data-dependent step is fit inside training only.** Selection on the
whole cohort is the most common radiomics leak.

## Two stacks (do not mix)

| Stack | What it is | Entry |
|---|---|---|
| **In-pipeline (habitat / delta trees)** | Feature **filter** after radiomics flatten | `radiomics.select_features` → sklearn **`LassoCV` only** (cv=5, `SelectFromModel` threshold `1e-8`) |
| **Paper LASSO / nomogram / `VAL_MODE`** | Clinical+radiomics modelling, curves, nomogram, lock/apply | **`python -m modules.pipeline`** |

Do **not** promote `delta_habitat_pipeline/utility/LASSO.py` as the stats library. That file is a
utility sketch, not the paper pipeline.

## In-pipeline selection (`select_features`, both trees)

All of this runs on the **training** split after `StandardScaler.fit(train)`
(`run_cohort_aggregation`; `leakage-audit.md`):

1. Near-zero variance — `FEATURE_SELECTION["near_zero_var_threshold"]` (live `0.01`).
2. Pearson redundancy — `|r| > FEATURE_SELECTION["correlation_threshold"]` (live `0.90`); keep
   the member more correlated with `y`.
3. **LassoCV** — only supervised selector in these trees. Not elastic net, not mRMR, not Boruta.

There is **no ICC step here**. If ICC is required, call `modules/utils/u_icc.py` before this
stack, on training/reproducibility scans only.

> Wrong: rank features on the full dataset, then cross-validate the chosen set.
> Right: re-run selection inside each training fold; report selection stability.

## Paper modelling (`python -m modules.pipeline`)

Use this stack when the user wants a Rad-score, nomogram, ROC/DCA/calibration, NRI, or
`VAL_MODE` (`refit` / `apply_formula` / `lock_threshold`). Details:
`clinical-ml-pipeline.md` and `04_analysis/references/0rad-pipeline-rules.md`.

- Match the model to n/EPV: penalised regression for small n; tree ensembles/SVM when justified.
- Tune hyperparameters with **nested CV** (inner loop) — never on the test set.
- Pre-specify the **primary** model; others are exploratory.
- Combine selected features into a score (LASSO linear predictor → "Rad-score").
- Optionally a **nomogram** combining Rad-score with clinical variables — report both the
  combined and component models.
- Report the formula/coefficients (supplement).

## Validation & reporting (hand computation to radiology-stats)

- Internal: nested CV or bootstrap optimism correction.
- External/temporal/geographic: pipeline frozen (needs persisted scaler / selected names — see
  the `feature_scaler.joblib` gap in `leakage-audit.md`).
- Metrics: discrimination (AUC/C-index + CI), **calibration** (slope/intercept, Brier),
  **decision-curve** — not AUC alone.
- Report selection stability and per-center performance where relevant.

## Reporting sentence

*"Within training, habitat/delta features were filtered (near-zero variance, correlation |r| <
0.9) and selected by in-pipeline LassoCV. Paper-level LASSO, nomogram, and VAL_MODE were run via
python -m modules.pipeline with the pipeline frozen; discrimination, calibration, and
decision-curve analysis are reported with 95% CIs."*
