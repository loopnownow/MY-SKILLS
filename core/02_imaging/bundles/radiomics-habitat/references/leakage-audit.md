# Radiomics leakage audit

The checklist reviewers (and METRICS/RQS) use. Each item is pass/fail with a fix. One failure can
sink the paper.

## Habitat / delta trees — fit-on-training-only (live behaviour)

Both `habitat_pipeline` and `delta_habitat_pipeline` `run_cohort_aggregation`:

- `train_test_split` first (patient-level rows after flatten).
- `StandardScaler` **`fit` on train only**, `transform` test.
- `select_features(X_train, y_train, …)` **train only** (near-zero variance → Pearson redundancy
  → **LassoCV**). Test columns are sliced with the selected names afterwards.

`delta_habitat_pipeline.radiomics.compute_delta_features` computes absolute / relative / rate
deltas **without Z-score**. Scaling happens later in `run_cohort_aggregation` on the train split
only. Do not z-score inside `compute_delta_features`.

## Gap: `feature_scaler.joblib`

Training `pipeline.py` **may not write** `06_selected/feature_scaler.joblib` (scaler is fitted in
memory and discarded). `delta_habitat_pipeline/utility/validate_delta_habitat.py`
(`load_train_artifacts`) **expects** that file. Flag this when wiring validation: persist the
scaler explicitly if a frozen apply-on-new-cohort path is required. Do not refit the scaler on
validation/test.

## ICC is not in these trees

Neither habitat tree implements ICC filtering. Point to **`modules/utils/u_icc.py`** in the
clinical / `python -m modules.pipeline` stack. Do not invent an in-tree ICC step or imply
`select_features` already dropped low-ICC features.

## Partition hygiene

- [ ] Split made at the **patient level** (not slice/lesion). Habitat flatten is already one row
      per patient — do not split on habitat rows.
- [ ] No patient's lesions/slices/sequences/phases/timepoints span train and test.
- [ ] Test set untouched until final evaluation (no peeking).

## Fit-on-training-only

- [ ] **Feature selection** (`select_features`) inside CV/training folds, not on the full cohort.
- [ ] **Normalisation / standardisation** (`StandardScaler`) fit on training, applied to test.
- [ ] **Missing-value imputation** fit on training.
- [ ] **Harmonisation (ComBat)** fit on training (biology preserved), applied to test.
- [ ] **Augmentation** never crosses the split.
- [ ] **Delta Z-score** not computed in `compute_delta_features`.

## Tuning hygiene

- [ ] Hyperparameters tuned by **nested CV** / a separate validation set, not on test.
      In-pipeline LassoCV uses 5-fold CV on **train** (`select_features`).
- [ ] **Threshold / operating point** chosen on training/derivation, not on test.
- [ ] No early stopping / model selection on the test set.

## Reproducibility / stability

- [ ] Non-reproducible (low-ICC) features removed before modelling — **via `u_icc.py`**, not
      these trees.
- [ ] Discretisation (FBN32 + FBS16) fixed and reported (IBSI).
- [ ] Software + version + Pictologics config names recorded and shareable.
- [ ] Frozen validation has `feature_scaler.joblib` (or the gap is acknowledged).

## Evaluation honesty

- [ ] Real prevalence reported (no silent 1:1 resampling claimed as the clinical setting).
- [ ] Discrimination **and** calibration **and** decision-curve for clinical models.
- [ ] CIs everywhere; external/temporal validation stated honestly.
- [ ] Selection stability / per-center results where relevant.

## Output

```
Leakage audit:
  Partition:        PASS / FAIL — [detail + fix]
  Fit-on-training:  PASS / FAIL — [detail + fix]
  Tuning:           PASS / FAIL — [detail + fix]
  Reproducibility:  PASS / FAIL — [detail + fix]
  Evaluation:       PASS / FAIL — [detail + fix]
Overall: [Blocker(s) / Should-fix / Clean]
```

Hand paper-level statistical modelling to `python -m modules.pipeline` / `radiology-stats`, and
the reporting-guideline mapping to `radiology-reporting`. Do not send that work to
`utility/LASSO.py`.
