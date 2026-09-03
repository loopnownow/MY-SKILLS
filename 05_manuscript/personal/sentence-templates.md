# Sentence Templates — Ying Li Style

Purpose / methods / results templates refreshed 2026-08-28 from 389 unique drafts (324 English). Do not collapse the three purpose-sentence families below. Do not vendor unpublished full texts, title dumps, or patient identifiers.

**Split wording (body vs Figure 1):** manuscript BODY internal split is **training / test** (training cohort / test cohort). Only an other-hospital cohort is **external validation**. Figure 1 (mounted `04-fig-flow`) uses published **Training Cohort / Validation Cohort** — do not rewrite `04-fig-flow` from this file. Never `Development set`. Never call a same-hospital random split external validation.

**Do not use (0 hits in 389 unique drafts):** `suggesting its potential`; `demonstrated good performance`. See `forbidden-phrases.md`.

## Abstract Templates

### Objective sentence — keep THREE families (do not collapse to one)

Harvest 2026-08-28, 324 English unique drafts, full-text grep:

| Family | Hits | Papers | Status |
|---|---:|---:|---|
| This study aimed to … | 45 | 44 | family 1 |
| To explore/investigate/evaluate/determine/assess/compare/develop … | 35 | 34 | family 2 |
| The aim of this study was to … | 22 | 14 | family 3 |
| The purpose of this study was to … | 12 | 12 | minority |
| We aimed to / We sought to … | 5 | 5 | rare |

- **"This study aimed to [objective] using [method] in [population]."**
- **"The aim of this study was to [objective]."**
- **"To [investigate/explore/evaluate/determine/assess/compare/develop] whether [technique] could [outcome] in [population]."**
- "The purpose of this study was to [develop/evaluate/compare] [model] for [task]." — minority; not a fourth default family.

### Methods sentence
- "A total of N patients with [condition] who underwent [imaging] were retrospectively enrolled."
- "Patients were randomly divided into a training cohort (n = N) and a test cohort (n = N)."
- "Radiomics features were reduced using LASSO, and a radiomics nomogram was constructed."
- "A total of N [subjects] were divided into [N] subgroups: [Group A] (n = N), [Group B] (n = N), [Group C] (n = N), and [Group D] (n = N)."
- Radiomics / prediction papers default to **training/test + LASSO + nomogram**. BODY split is training/test; Figure 1 labels stay Training Cohort / Validation Cohort (published). Other-hospital only = external validation.

### Results sentence
Default: report **AUC of X (95% CI: X–X)** for **both** training and test.
- "The AUC of the [model] was X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort."
- "The nomogram exhibited good discrimination in the training cohort (AUC X [95% CI, X–X]) and the test cohort (AUC X [95% CI, X–X])."
- Direct side-by-side AUCs are more common than `outperformed` (12 hits / 7 papers).
- "Significant [differences/elevations/reductions] were observed in [Group A] and [Group B], but not in [Group C]."

### Conclusion sentence
Do **not** use `demonstrated good performance` or `suggesting its potential` (0 hits in 389 unique drafts; see `forbidden-phrases.md`).
- "The radiomics nomogram could improve [clinical decision/patient selection] for [treatment/procedure] in [population]."
- "In conclusion, the [model] achieved an AUC of X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort."
- "Both [A] and [B] play roles in [pathophysiology], with [specific conclusion]."

---

## Introduction Templates

### Opening sentences
- "[Condition X] refers to [definition], [epidemiological context] [1]."
- "[Condition X] is the [Nth] most common [tumor/disease] in [population], with an incidence of approximately X per 100,000 [2,3]."
- "[Condition X] is a [clinical challenge] because [reason], affecting approximately N patients annually worldwide [1]."

### Gap identification
- "However, the pathogenesis of [X] remains unclear."
- "Currently, [standard approach] remains the gold standard; however, it is limited by [limitation]."
- "The accurate [preoperative/non-invasive] [prediction/diagnosis] of [X] remains challenging."
- "Although [approach A] has been widely used, [limitation], which may lead to [adverse outcome]."

### Proposed approach
- "Recently, radiomics — a method for high-throughput extraction of quantitative features from medical images — has been applied to [task] and shown promising results [X–X]."
- "[Technique] has been proposed as a [non-invasive/functional] method for assessing [biomarker], enabling [clinical benefit] without [limitation of current approach]."
- "Intravoxel incoherent motion (IVIM) imaging can simultaneously reflect the [diffusion and perfusion] properties of tissue, providing additional [physiological] information beyond conventional DWI."

### Closing aim
Keep the same three purpose-sentence families as the abstract (do not collapse to one).
- "This study aimed to [objective] using [method] in [population]."
- "Therefore, the aim of this study was to [develop/evaluate/compare] [a radiomics nomogram/a combined model] for [task] in [population]."
- "To [investigate/evaluate] whether [technique] could [outcome] in [population]."
- "Thus, we hypothesized that [technique] could serve as a useful non-invasive tool for [task]." — hypothesis-framed variant, not a fourth family.

---

## Methods Templates

### Ethics statement
- "This [retrospective/prospective] study was approved by the Institutional Review Board of Jinshan Hospital of Fudan University (No. XXX), and the requirement for informed consent was waived due to the retrospective nature of the study."
- "Written informed consent was obtained from all patients prior to enrollment."
- "All experimental procedures were approved by the Animal Ethics Committee of [institution] (No. XXX) and conducted in accordance with institutional guidelines."

### Patient selection
- "Inclusion criteria were as follows: (1) [criterion 1]; (2) [criterion 2]; (3) [criterion 3]."
- "Patients were excluded if: (1) [criterion 1]; (2) [criterion 2]."
- "Patients were randomly divided into a training cohort (n = N) and a test cohort (n = N) at a ratio of X:X."  BODY: training/test. Figure 1: Training Cohort / Validation Cohort. Other-hospital only = external validation.

### Imaging protocol
- "All MRI examinations were performed on a X.X-T MRI scanner ([Manufacturer, Model]) using a [body/pelvic/head] coil."
- "DWI was performed with b values of 0 and 1,000 s/mm², and the corresponding ADC maps were automatically generated by the scanner's built-in software."
- "4D flow MRI was acquired with the following parameters: voxel size X×X×X mm³, temporal resolution X ms, VENC X cm/s."

### ROI delineation
- "Regions of interest (ROIs) were manually delineated on [sequence] images by two radiologists with X and X years of experience in [subspecialty] imaging, blinded to [clinical information]."
- "Inter-observer and intra-observer reproducibility were assessed using the intraclass correlation coefficient (ICC); ICC > 0.75 was considered good agreement."

### Radiomics pipeline
- "Radiomics features were extracted using pyradiomics (version X.X, https://pyradiomics.readthedocs.io) following the Image Biomarker Standardisation Initiative (IBSI) guidelines."
- "A total of N features were initially extracted, comprising first-order statistical features, shape-based features, and texture features (GLCM, GLRLM, GLSZM, and NGTDM)."
- "The least absolute shrinkage and selection operator (LASSO) regression with 10-fold cross-validation was used to select the most informative features and reduce dimensionality."
- "A radiomics score (rad-score) was calculated for each patient as a linear combination of selected features weighted by their respective LASSO coefficients."

### Statistical analysis
- "Continuous variables are presented as mean ± standard deviation (SD) or median (interquartile range [IQR]) according to the results of the Shapiro-Wilk normality test."
- "Categorical variables are expressed as frequencies and percentages."
- "Comparisons between groups were performed using the independent-samples t-test or Mann-Whitney U test for continuous variables, and the chi-square test or Fisher's exact test for categorical variables."
- "Receiver operating characteristic (ROC) curve analysis was performed to assess diagnostic performance, and areas under the ROC curves (AUCs) were compared using the DeLong method."
- "Decision curve analysis (DCA) was performed to evaluate the net clinical benefit of the predictive models."
- "All statistical analyses were performed using R software (version X.X; R Foundation for Statistical Computing, Vienna, Austria) and Python (version X.X). Differences with a P-value less than 0.05 were considered statistically significant."

---

## Results Templates

### Baseline characteristics
- "The clinical characteristics of the study population are summarized in Table 1. There were no significant differences in age, sex, or [variable] between the training and test cohorts (all P > 0.05)."

### Feature selection
- "After LASSO feature selection, N features with non-zero coefficients were retained and used to construct the radiomics signature (Figure X)."

### Model performance
Radiomics default: **training/test + LASSO + nomogram**. Report AUC of X (95% CI: X–X) for **both** training and test.
- "The AUC of the radiomics nomogram was X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort, with sensitivity of X% and specificity of X% in the training cohort."
- "The combination model was compared with the clinical model alone in the training cohort (AUC: X vs. X; P < 0.001 by DeLong test) and in the test cohort (AUC: X vs. X)."
- "The Hosmer-Lemeshow test indicated good calibration of the nomogram (P = X)."
- "Decision curve analysis showed that the radiomics nomogram provided greater net benefit than either the clinical model or the treat-all/treat-none strategies across a wide range of threshold probabilities (Figure X)."

### Negative findings
- "No significant difference was observed in [variable] between [group A] and [group B] (P = X)."
- "Significant [X] were observed in [Group A] and [Group B] rats, but not in [Group C] rats."

---

## Discussion Templates

### Opening summary
- "In this study, we demonstrated that [technique/model] could accurately [predict/differentiate/identify] [outcome] in [population], with AUC values of X–X across independent cohorts."
- "The main finding of this study was that [key result], suggesting that [clinical implication]."

### Literature comparison
- "This result is consistent with the findings of [Author et al.] [X], who reported [similar finding] in [similar population]."
- "In contrast, [Author et al.] [X] found [different result], which may be attributed to differences in [patient population/imaging protocol/feature selection method]."

### Mechanistic interpretation
- "The elevated [metabolite/parameter] in [group] may reflect [underlying pathophysiology], which is consistent with the known role of [pathway] in [condition]."
- "The higher ADC values observed in [group] might be related to [biological mechanism], suggesting [interpretation]."
- "Enrichment analysis indicated that abnormal metabolism of [pathway] in [condition] might be affected by [factor]."

### Clinical implications
- "The proposed nomogram could be used to guide individualized treatment decisions, potentially reducing unnecessary [procedures] in low-risk patients while ensuring appropriate management for high-risk cases."
- "Decision curve analysis showed that the radiomics nomogram provided a greater net benefit than the clinical model alone, supporting its potential clinical utility in [context]."
- "This non-invasive imaging-based approach could serve as a preoperative tool for [task], thereby optimizing clinical workflows and reducing the burden of [invasive procedure]."

### Limitations paragraph
- "This study has several limitations. First, the retrospective design may have introduced selection bias. Second, all patients were recruited from a single center, which may limit the generalizability of our findings. Third, the sample size was relatively small, and external validation in larger, multicenter cohorts is needed. Fourth, the manual delineation of ROIs is time-consuming and subject to interobserver variability; automated segmentation methods may improve reproducibility in future studies. **Future research should focus on larger, multicenter, prospective studies to validate and further refine the proposed model.**"
- Closing-sentence default is **"Future research should…" / "Future studies should…"** (18/96 and 9/96 respectively — corpus-dominant), not "…are warranted…" (a minority form, 14/96 total across *any* use of "warrant," not specific to this slot).

### Conclusion sentence
Do **not** close with `demonstrated good performance` or `suggesting its potential`.
- "In conclusion, the radiomics nomogram achieved an AUC of X (95% CI: X–X) in the training cohort and X (95% CI: X–X) in the test cohort and could assist [clinical application] in [population]."
- "In summary, both [A] and [B] play roles in [condition], with [specific mechanistic conclusion], providing new insights into the pathogenesis of [disease]."
