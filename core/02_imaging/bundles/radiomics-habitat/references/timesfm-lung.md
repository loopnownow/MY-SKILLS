# TimesFM-Based Lung Cancer Imaging Pipeline (RECIST Response Prediction)

## Purpose

Predicts RECIST-based tumor response (e.g. CR/PR/SD/PD, or continuous target-lesion size trajectory)
from longitudinal lung imaging using TimesFM (validated with TimesFM 2.5-200M) as a time-series
foundation model over sequential per-timepoint tumor measurements/features rather than a traditional
per-timepoint classifier.

## Design considerations specific to this domain

- **Input representation**: decide explicitly whether TimesFM operates on raw target-lesion size
  time series (simplest, most RECIST-native), on a richer per-timepoint radiomics feature time series,
  or a mix — this choice should be a config-level decision, documented, not buried in the data-loading
  code.
- **Irregular timepoint spacing**: clinical follow-up intervals are rarely uniform; confirm how TimesFM
  is meant to handle irregular sampling (padding/interpolation convention) and make the handling
  explicit and configurable rather than assuming evenly-spaced scans.
- **RECIST category derivation**: if the pipeline needs to output discrete RECIST categories (not just
  raw size predictions), the size-change thresholds that define CR/PR/SD/PD should be config values
  (they are standardized but still worth keeping soft-coded, e.g. for sensitivity analysis or
  non-standard variants like iRECIST).
- **Statistical validation modules**: full statistical validation (not just point predictions) has been
  a requirement in this pipeline previously — plan for calibration/accuracy metrics appropriate to a
  forecasting task (e.g. per-timepoint prediction error, category-level confusion matrix at each
  follow-up), not only end-of-study accuracy.
- **Model versioning**: TimesFM checkpoint version (e.g. 2.5-200M) should be a config value — foundation
  model versions change, and pipeline outputs should record which checkpoint produced them for
  reproducibility.

## Module split (apply the shared conventions)

Following this skill's shared conventions, split into: `config.py` (checkpoint version, input
representation choice, RECIST thresholds, paths), `data_loader.py` (per-patient longitudinal series
construction, irregular-spacing handling), `inference.py` (TimesFM forecasting), `recist_mapping.py`
(size-series → RECIST category, kept separate from inference so threshold changes don't require
re-running the model), and `validation.py` (statistical validation/metrics, decoupled so it can be
re-run against saved predictions).
