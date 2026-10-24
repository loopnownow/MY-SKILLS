# Multicenter

Use this file when the user asks about multicenter imaging datasets, external
validation, scanner/vendor/protocol differences, center effects, harmonization,
domain shift, temporal validation, or generalizability.

## Core goal

Goal: turn “data from several hospitals” into credible generalization validation — not simply pooling to inflate n.

## First questions

- How many centers? Patients, positives/events, and time span per center?
- Are scanner vendor, model, slice thickness, reconstruction kernel, MRI sequences, and contrast phases consistent across centers?
- Are case mix, treatment strategy, follow-up, and label definitions consistent across centers?
- Which centers train, which externally validate?
- Is there temporal or geographic validation?
- Plan for harmonization, domain adaptation, federated learning, or external test only?

## Multicenter design patterns

| Pattern | Use when | Interpretation |
|---|---|---|
| pooled training + internal split | early model development | weak evidence if no center-held-out validation |
| train on center A, test on center B | true external validation | strong but may be underpowered |
| train on multiple centers, hold out one center | generalizability test | useful for center robustness |
| temporal validation | same hospital, later patients | tests time drift, not geography |
| geographic validation | different hospital/region | stronger external validity |
| federated learning | data cannot leave centers | requires strong engineering and governance |

## Center-aware split

Prefer:

1. patient-level grouping always
2. center-level external validation when possible
3. temporal holdout within major centers if enough cases
4. no same-patient leakage across centers or timepoints
5. locked preprocessing and threshold before external validation

Avoid:

- random split after pooling all centers as the only validation
- center imbalance hidden inside aggregate AUC
- tuning model based on external center performance
- reporting only average performance without center-specific failure analysis

## Harmonization and domain shift

Check:

- scanner vendor and field strength
- CT slice thickness, reconstruction kernel, contrast phase
- MRI sequence parameters and vendor-specific differences
- PET reconstruction and SUV normalization
- ultrasound operator and equipment variability
- segmentation protocol consistency

Possible approaches:

- standardize acquisition inclusion criteria
- resampling and intensity normalization
- ComBat or related harmonization for radiomics features
- domain adaptation for deep learning
- center-stratified cross-validation
- center as covariate or random effect when appropriate
- sensitivity analysis with and without harmonization

Warnings:

- Fit harmonization without leaking outcome or test information.
- Do not use external validation data to choose harmonization strategy.
- Report performance before and after harmonization if it materially changes results.

## Reporting

Methods should include:

- center names or anonymized center IDs
- patient counts and event counts per center
- acquisition parameter summary per center
- split logic by center and time
- preprocessing and harmonization details
- whether model selection used any external center information
- center-specific and pooled validation metrics

Results should include:

- overall performance
- center-specific performance
- heterogeneity or subgroup analysis
- failure center discussion
- calibration and DCA in external cohorts when possible

## Output format

```text
Multicenter framing
- Center count and distribution:
- Main sources of difference:
- Target validation type:

Recommended split
- Train:
- Internal validation:
- External / temporal validation:

Handling center differences
- Image parameters:
- Labels / treatment:
- Harmonization / domain shift:

Reporting suggestions
- Tables:
- Figures:
- Methods text:

High-risk issues
- [pooled random split, center imbalance, test-center tuning]
```

## Red lines

- Do not call a pooled random split “external validation.”
- Do not hide center-specific poor performance behind a pooled AUC.
- Do not assume harmonization solves all scanner and protocol differences.
- Do not tune models on the external center and still claim independent validation.
- Do not ignore different label definitions, treatment protocols, or follow-up rules across centers.
