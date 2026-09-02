# Section templates (short-sentence English)

Use with 李瀛 voice. Prefer clauses and periods over dashes.

## Introduction (4 paragraphs)

**P1 stakes**

Lung cancer remains a leading cause of cancer death worldwide [1].  
Chest CT frequently detects indeterminate small pulmonary nodules [2].  
Guideline pathways exist, but individualized timing of intensified follow-up remains uncertain [3].

**P2 prior tools**

Serial size and attenuation change define growth in practice [4].  
Clinical morphology provides incomplete risk separation [5].  
Whole-nodule radiomics can predict two-year growth [6].

**P3 gap**

Whole-nodule features average voxels across the lesion.  
Intra-nodular habitats may encode growth-related heterogeneity [7].  
Few studies apply habitat radiomics to short-term growth of small indeterminate nodules.

**P4 purpose**

Therefore, the purpose of this study was to develop a combined clinical and habitat radiomics model on the training set only and to evaluate it for two-year growth prediction under TRIPOD guidance.

## Methods snippets

**Training-only fitting**

All habitat clustering centers, feature selection steps, and model coefficients were estimated exclusively on the training set.  
The test set was used only for performance evaluation.

**Patient-level split**

Patients were allocated in a stratified ratio at the patient level.  
When one patient contributed multiple nodules, all nodules remained in the same set.

**Primary model**

The primary model was a multivariable logistic combined model that integrated the habitat RadScore with clinical covariates.  
The combined model was displayed as a nomogram.

**K selection**

Candidate K values of 3 and 4 were compared on a training-set multiparametric subsample.  
Selection used the WCSS elbow, the maximum average silhouette coefficient, and consensus clustering stability with ARI of at least 0.70.  
K of 3 was stable and was locked for all analyses.

## Results snippets

**RadScore formula lead-in**

The training-set RadScore was calculated as: RadScore = …

**Combined dual-set**

In the training set, the combined model achieved an AUC of X.XXX (95% CI: X.XXX–X.XXX).  
In the test set, the combined model achieved an AUC of X.XXX (95% CI: X.XXX–X.XXX).  
NRI total was X.XXX in the training set and X.XXX in the test set.  
IDI was X.XXX (95% CI: X.XXX–X.XXX) in the training set and X.XXX (95% CI: X.XXX–X.XXX) in the test set.

## Discussion openers

In this TRIPOD-aligned study, we demonstrated that…  
Among clinical predictors, larger diameter was associated with growth [n].  
Habitat modeling was the main methodological focus.  
Comparison with related studies requires caution because populations and endpoints differ.  
The nomogram is the operational form of the primary combined model.  
This study has several limitations. First,… Second,…

## Conclusion

A combined clinical and habitat radiomics model fitted on the training set predicted [endpoint].  
The model was displayed as a nomogram and evaluated on a patient-level internal test set.  
If no external cohort exists, put *A validation set is required* in a Word comment (author A) — never in this section.
