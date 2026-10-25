# Figures

Use this file when the user asks how to design manuscript figures, tables, graphical
abstracts, workflow diagrams, performance plots, radiomics pipeline figures, deep
learning architecture figures, mechanism diagrams, or figure legends for imaging AI
studies.

If the user names a target journal family, load [MODULE.md](../MODULE.md) and `nature-figure-spec.md`.
Radiology-family and Nature/npj-family figures differ in panel-letter case, column
widths, display-item limits, Source Data expectations, and legend conventions.

## Core goal

The figures module makes charts serve the paper's argument — not a pile of ROCs. Decide what each figure answers, then pick the chart type.

## First questions

- What is the paper's core conclusion?
- Is the study radiomics, deep learning, multimodal, mechanism, treatment response, or clinical translation?
- What results exist already: AUC, C-index, Dice, calibration, DCA, KM, SHAP, Grad-CAM, mechanism analyses?
- Are external validation, multi-center validation, subgroups, and failure cases present?
- What is the target journal or article type?
- Need main figures, supplements, or a pre-submission figure review?
- Target Radiology/RSNA, Nature/npj, Lancet, Cell Reports Medicine, European Radiology,
  or still undecided?

## Recommended figure set

### Core clinical prediction manuscript

| Figure/Table | Purpose | Contents |
|---|---|---|
| Figure 1 | study design | Patient-selection Figure 1 is `draw-flowchart` (STROBE type A). Do not draw enrolment flow here. |
| Table 1 | cohort description | demographics, clinical variables, endpoints by split |
| Figure 2 | model pipeline | segmentation, feature extraction/modeling, validation |
| Table 2 | model performance | AUC/C-index, CI, sensitivity, specificity, calibration |
| Figure 3 | discrimination | ROC/PR or time-dependent AUC across cohorts |
| Figure 4 | calibration and utility | calibration curves and DCA |
| Figure 5 | interpretation | feature importance, SHAP, saliency, or mechanism evidence |
| Supplement | robustness | subgroup, sensitivity, failure cases, checklist |

### Radiomics manuscript

- ROI examples with overlay on representative images.
- Radiomics workflow: image acquisition -> segmentation -> preprocessing -> feature extraction -> feature selection -> model -> validation.
- Feature selection path: optional LASSO coefficient path or selected feature heatmap.
- Model comparison: clinical, radiomics, combined model.
- Nomogram only when clinically justified and calibrated.
- Calibration and DCA if clinical prediction is claimed.

### Deep learning manuscript

- Architecture overview without unnecessary layer-by-layer clutter.
- Data split and augmentation workflow.
- Representative saliency/Grad-CAM/attention maps only after checking plausibility.
- Uncertainty/OOD/robustness plots when the model claims trustworthy or deployment-grade use.
- Failure-case and high-uncertainty examples, not only best-looking examples.
- Segmentation examples: best, typical, and failure cases.
- External validation performance and center subgroup performance.

### Mechanism manuscript

- Evidence chain diagram: imaging phenotype -> molecular pathway -> cell type/spatial niche -> clinical endpoint.
- Heatmap or pathway enrichment for radscore-associated modules.
- Single-cell dot plot/violin/UMAP only if it answers the mechanism question.
- Spatial map linking pathway/cell state to image habitat.
- Avoid decorative omics plots disconnected from the radiomics score.

## Table standards

### Table 1

Include:

- patient count by split and center
- age, sex, disease stage or grade
- key laboratory/clinical variables
- treatment information when relevant
- endpoint distribution and follow-up
- missing values and test used for comparison

Do not overinterpret p-values comparing train/test baseline variables. The table describes
cohort balance, not causal differences.

### Model performance table

Include:

- cohort name and patient count
- model type
- AUC/C-index/Dice with 95% CI
- sensitivity, specificity, PPV, NPV at locked threshold
- calibration metric if available
- clinical model and combined model comparison
- external validation results separately

### Supplementary tables

- image acquisition parameters
- radiomics extraction parameters
- selected features and coefficients
- hyperparameters
- full checklist compliance
- excluded cases and reasons

## Figure legend checklist

Each legend should state:

- cohort or dataset
- sample size and event count
- model or feature being shown
- metric definition
- confidence interval method if plotted
- statistical test if used
- abbreviation definitions

## Common missing figures

- Patient flow diagram (→ `draw-flowchart`, not this pack).
- External validation performance.
- Calibration curve.
- Decision curve analysis.
- Failure-case visualization.
- Center-specific performance.
- Figure showing how ROI was drawn.
- Supplementary table of image acquisition parameters.
- Reproducibility materials table.
- Venue-specific figure QA: panel letters, widths, legends, Source Data/Extended Data,
  and graphical abstract requirements.

## Output format

```text
Figure framing
- Article type:
- Core conclusion:
- Existing figures:

Recommended main figures
| Fig # | Purpose | Content | Data needed | Risks |

Recommended tables
| Table # | Purpose | Content |

Supplements
- [parameter tables, robustness figures, checklist]

Figure legend draft
[only when figure facts are supplied]
```

## Red lines

- Do not design figures around unsupported claims.
- Do not let ROC be the only model-evaluation figure when clinical prediction is claimed.
- Do not use saliency maps as proof of mechanism.
- Do not invent performance values or sample sizes for figure legends.
- Do not place patient-identifiable images in figures.
