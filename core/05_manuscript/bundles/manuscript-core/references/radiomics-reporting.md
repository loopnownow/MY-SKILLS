# Radiomics / habitat reporting (must-have text)

## Habitat

Must state:

1. Habitat definition (multiparametric intensity + local texture + gradient, or project-specific).  
2. **Clustering centers fitted on the training set only.**  
3. Same centers applied to the test set without update.  
4. K selection: candidates, WCSS, silhouette, consensus (bootstrap n, subsample %, **ARI threshold**).  
5. Selected K and why.  
6. **Nodule-level** fallback rule and rate (if used).  

Do not invent silhouette/WCSS decimals without pipeline logs. Protocol thresholds (e.g. ARI ≥ 0.70) may be stated as design rules.

## LASSO and RadScore

Results (or Methods + Results) must include:

1. Number of features retained.  
2. **No LASSO-feature table** (`Aitor-format.md`).  
3. **Full RadScore formula** with numeric coefficients in Results prose.  
4. Statement that the test set used **identical** coefficients without reselection.  
5. Feature source filter (e.g. FBS_16 for CT) and IBSI compliance mention. If no IBSI test was run, write that it is not reported.

Example lead-in:

> LASSO with 10-fold cross-validation retained nine habitat radiomics features on the training set.  
> The RadScore was calculated as: RadScore = …

## Primary combined model (nomogram)

Always name **combined model / nomogram as primary** when that is the intended main product.

Report **both sets**:

| Metric | Training | Test |
|--------|-------------|------------|
| AUC (95% CI) | required | required |
| ACC / SEN / SPE at training Youden (if locked) or split-specific Youden | required | required |
| NRI (events, nonevents, total) | required | required |
| IDI (95% CI) | required | required |
| Calibration | figure + one sentence | figure + one sentence |
| DCA | figure + one sentence | figure + one sentence |

Clinical model and RadScore alone are comparators, not substitutes for primary combined reporting.

## QC (Supplementary)

From pipeline summary (e.g. `u_QC.py` on `lung_xlm_summary.csv`):

- Full pipeline success n / rate  
- Habitat mode (global)  
- K verification / non-empty habitats  
- Nodule-level fallback n / rate  
- Mean habitat volume fractions  
- Feature count consistency  

Main text one-sentence pointer to Supplementary Material.

## Patient-level split QA

Before writing “no cross-set multi-nodule assignment”:

1. Verify code or data actually enforces patient-level split.  
2. If leakage exists, **fix split and recompute metrics**, or do not claim no leakage.  
3. Report nodule n and patient n when available.
