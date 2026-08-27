# 写作

Use this file for radiology AI manuscript sections.

## Methods structure

Recommended order:

1. study design and participants
2. imaging acquisition and preprocessing
3. labels/reference standard
4. segmentation/annotation
5. radiomics feature extraction or deep learning model
6. train/validation/test split
7. statistical analysis and metrics
8. reporting, code, and data availability

## Results structure

Report:

- cohort flow and baseline characteristics
- development and validation sets
- primary performance with confidence intervals
- calibration and clinical utility when relevant
- subgroup or external validation
- failure cases or limitations in performance

## Claim control

Use:

- "showed discrimination" for AUC-like findings
- "was associated with" for observational relationships
- "may support" for cautious clinical implications

Avoid:

- "accurately diagnoses" without diagnostic workflow validation
- "can be used clinically" without calibration, threshold, utility, and external validation
- "proves" for association or retrospective models

## Chinese-to-English writing

Translate intent, not word order. Convert vague Chinese claims into explicit study facts:

- "模型效果很好" -> performance metric, validation set, confidence interval
- "外部验证" -> independent center/population/time split details
- "影像组学特征筛选" -> exact sequence inside training data only
