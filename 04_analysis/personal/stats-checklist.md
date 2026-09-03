# Statistical Reporting Checklist — Ying Li Style

Use this checklist when polishing Results and Methods sections.

---

## Before submitting: verify each item

### General
- [ ] All P values reported as exact values when ≤ 0.05 (e.g., P = 0.002), and as comparison when > 0.05 (e.g., P = 0.12 or P > 0.05)
- [ ] P is italicized: *P* (adjust per journal house style)
- [ ] All CIs reported as 95% CI: X–X (en-dash, no spaces around dash)
- [ ] All AUCs reported with 95% CI in parentheses
- [ ] Sensitivity, specificity, NPV, PPV all reported as percentages with 1 decimal place
- [ ] Effect sizes reported (OR, HR, RR) with 95% CI when applicable
- [ ] ICC values reported for inter/intra-observer agreement (threshold: ICC > 0.75 = good)

### Continuous variables
- [ ] Normality test reported (Shapiro-Wilk or Kolmogorov-Smirnov)
- [ ] Normal → mean ± SD
- [ ] Non-normal → median (IQR)
- [ ] Normal groups → independent t-test
- [ ] Non-normal groups → Mann-Whitney U test (not "Wilcoxon rank-sum" unless two related groups)
- [ ] Two related normal groups → paired t-test
- [ ] Two related non-normal groups → Wilcoxon signed-rank test (always spelled out fully)

### Categorical variables
- [ ] Reported as N (%)
- [ ] Chi-square test for large samples (expected count ≥ 5 in each cell)
- [ ] Fisher's exact test for small samples (expected count < 5)

### Split wording (body vs Figure 1)
- [ ] Manuscript **BODY** internal split is **training / test** (training cohort / test cohort)
- [ ] Figure 1 (mounted `04-fig-flow`) uses published **Training Cohort / Validation Cohort** — do not rewrite mounted `04-fig-flow` from this checklist
- [ ] **External validation** only for an other-hospital cohort; never a same-hospital random split
- [ ] Never `Development set`; never `hold-out` as the test-set name

### Diagnostic performance
- [ ] Default: `AUC of X (95% CI: X–X)` reported for **both** training and test
- [ ] ROC curve AUC with 95% CI (en-dash, `95% CI: X–X`)
- [ ] AUC comparison via DeLong method (paired *P*, not the CI)
- [ ] Optimal threshold reported (typically Youden index; disclose per split)
- [ ] Sensitivity + specificity + PPV + NPV at threshold
- [ ] Calibration: Hosmer-Lemeshow P value reported (P > 0.05 = good calibration)
- [ ] DCA performed and net benefit described qualitatively

### Radiomics-specific
- [ ] Default narrative: **training/test + LASSO + nomogram**
- [ ] LASSO lambda selected by 10-fold CV on the **training** set (minimum criteria; not nested CV)
- [ ] Number of features before and after selection both stated
- [ ] Rad-score formula in prose (no LASSO-feature table)
- [ ] Training **and** test AUC of X (95% CI: X–X) both reported
- [ ] Feature stability: ICC or CV < 10% (if reported)

### Survival analysis (when applicable)
- [ ] HR (95% CI) reported, not just P value
- [ ] Kaplan-Meier curves with log-rank P value
- [ ] Cox multivariate: covariates listed, HRs all reported

### Metabolomics-specific
- [ ] Multivariate model type stated (sPLS-DA, PLS-DA, OPLS-DA)
- [ ] VIP threshold stated (typically VIP > 1.0)
- [ ] Metabolite changes: direction (increase/decrease) + group comparison explicit
- [ ] Enrichment analysis: database cited (KEGG, MetaboAnalyst)
- [ ] Pathway names italicized if gene names involved

---

## Common statistical errors to correct

| Error | Correction |
|---|---|
| "P < 0.05" for all significant results | Report exact P (P = 0.003) |
| "Wilcoxon test" | "Wilcoxon signed-rank test" (paired) or "Mann-Whitney U test" (unpaired) |
| "95%CI: 0.80-0.93" | "95% CI: 0.80–0.93" (en-dash, space before/after %) |
| "AUC=0.86" (one set only) | "AUC of X (95% CI: X–X)" in training **and** test |
| Missing normality justification | Add Shapiro-Wilk result or note |
| HR/OR without CI | Always add "(95% CI: X–X)" |
| SD vs SEM confusion in figure legends | Clarify: "error bars represent SD" or "error bars represent SEM" |
| "Significant difference" without test | Name the test and report statistic |
| p value without effect size | Add Cohen's d / AUC / OR depending on context |

---

## Software citation templates

- R: *"R software (version X.X; R Foundation for Statistical Computing, Vienna, Austria)"*
- Python: *"Python (version X.X; Python Software Foundation)"*
- pyradiomics: *"pyradiomics (version X.X; https://pyradiomics.readthedocs.io)"*
- ITK-SNAP: *"ITK-SNAP (version X.X; www.itksnap.org)"*
- SPSS: *"SPSS Statistics software (version X.X; IBM Corp., Armonk, NY, USA)"*
- MedCalc: *"MedCalc Statistical Software (version X.X; MedCalc Software, Ostend, Belgium)"*
