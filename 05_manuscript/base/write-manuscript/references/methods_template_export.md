# Methods section template

Fill-in skeleton for a reproducible Methods section. Do not invent ethics IDs, scanner
models, or software versions. Personal title-page defaults are not in this pack.

Suggested order (adapt if the venue mandates another):

1. Ethics
2. Study design and sample size
3. Patients
4. Inclusion and exclusion
5. Diagnostic and treatment criteria
6. Outcomes and endpoints
7. Laboratory tests
8. Imaging examinations
9. Image processing (segmentation / preprocess / registration / habitat / features)
10. Model building
11. Statistical analysis (software, normality, correlation, model evaluation, multiplicity, *P*)

---

## 2.1 Study population

This [retrospective/prospective] study included patients with [disease] who underwent
[exam/treatment] at [centre(s)] between [dates]. Inclusion: (1) …; (2) …. Exclusion: (1) …;
(2) …. The analysis set comprised [N] patients ([group1] n = [n1]; [group2] n = [n2]).

## 2.2 Image acquisition

Images were acquired on [scanner]. Parameters: TR = [X] ms, TE = [X] ms, slice thickness =
[X] mm, matrix = [X]×[X], FOV = [X] mm.

## 2.3 Image preprocessing

Preprocessing used [software, version]: (1) [step]; (2) [step]; (3) [step].

## 2.4 Radiomics feature extraction

Features were extracted with [software, version] from [images], n = [N] features (first-order,
shape, texture). ROI: [n] readers, [method]. IBSI statement: [compliant / not tested].

## 2.5 Feature selection and model construction

Selection used [method] **on the training set only**. The test set was used only for evaluation.
[RadScore definition if applicable.]

## 2.6 Statistical analysis

Software [name, version]. [Normality test]. Discrimination: AUC with 95% CI. Calibration and
decision-curve analysis [if done]. Two-sided *P* < 0.05 [or the pre-specified alpha].
