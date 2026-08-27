# 组学

Use this file for handcrafted radiomics and feature-based imaging biomarkers.

## Workflow

1. Define clinical question and endpoint.
2. Define cohort, inclusion/exclusion, scanner/protocol range, and split strategy.
3. Specify image preprocessing: resampling, intensity normalization, discretization,
   interpolation, filtering, and harmonization.
4. Specify ROI/mask source: manual, semi-automatic, automatic, readers, consensus,
   inter-reader reliability, and segmentation stability.
5. Extract IBSI-aware features with documented software and version.
6. Reduce features inside the training data only.
7. Fit models with nested or properly separated validation.
8. Report discrimination, calibration, clinical utility, confidence intervals, and
   external validation when available.

## Minimum reporting

- patient count and analysis unit
- imaging modality and acquisition protocol
- segmentation source and reliability
- feature extractor and version
- preprocessing parameters
- feature selection sequence
- model algorithm and hyperparameter tuning
- split unit and split timing
- internal and external validation
- calibration and decision curve when claiming clinical use

## High-risk patterns

- Feature selection before train/test split.
- Slice-level or lesion-level random split with patient overlap.
- Reporting only AUC without confidence interval or calibration.
- No details on bin width, resampling, normalization, or feature definitions.
- Claiming generalizability from one center.
- Using many features with few patients and no stability check.

## Recommended output

For an audit, lead with:

```text
Blocking radiomics risks
- Leakage:
- Segmentation:
- Feature reproducibility:
- Validation:

Required fixes
- [specific manuscript or analysis changes]
```
