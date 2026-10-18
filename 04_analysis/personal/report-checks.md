# Report checks (checklist + consistency)

## Part A — Statistical reporting checklist

# Statistical Reporting Checklist — Aitor Style

Use this checklist when polishing Results and Methods sections.

---

## Before submitting: verify each item

### General
- [ ] All P values reported as exact values when ≤ 0.05 (e.g., P = 0.002), and as comparison when > 0.05 (e.g., P = 0.12 or P > 0.05)
- [ ] P is italicized: *P* (adjust per journal house style)
- [ ] All CIs reported as 95% CI: X–X (en-dash, no spaces around dash)
- [ ] **Decimals:** Table 1 continuous/% cells → **1 or 2** places; *P*, AUC (+ 95% CI bounds), NRI/IDI, correlation (*r*/ρ and their *P*) → **3** places
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
- [ ] Manuscript **BODY** internal split is **training / test** (training set / test set)
- [ ] Figure 1 is the study flowchart read from Materials and Methods (not an enrollment-only figure). Cohort row: **Training Cohort / Test Cohort**, plus **Validation Cohort** only when Methods states an external cohort. Training-set downsampling is not an eligibility exclusion.
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


### Stats consistency audit (reported numbers)
- [ ] Table 1 continuous means checked against N where GRIM applies — see `report-checks.md` (this file)
- [ ] In-text NHST lines (t/F/chi-square/r) recomputed or flagged vs reported *P*
- [ ] HR/OR/RR 95% CI directionally consistent with reported *P*
- [ ] Raw assay tables (if in scope) pointed to `02_data-processing/personal/table-signals.md`, not handled only here
- [ ] **stat_vs_threshold** — printed *t*/*F*/*z* meets the stated voxel-wise or cluster-forming threshold
- [ ] **correlation_implied_n** — *n* implied by *r* and *P* matches the stated analysis *n*
- [ ] **multiplicity_disclosure** — ROI or voxel correlation family names a correction or an exploratory label
- [ ] **relative_denominator** — "relative" / normalized measures name the denominator and the units
- [ ] **no_confirmatory_p_same_cohort** — selection + threshold + group test on one cohort is not written as a confirmatory *P*
- [ ] **nested_roi_collinearity** — nested ROIs are not treated as independent tests
- [ ] **score_transform_identity** — a score that transforms one metric says so
- [ ] **cutoff_vs_included_distribution** — included-group median, Q1, and minimum sit on the included side of the cutoff
- [ ] **iqr_scale_sanity** — IQR lies inside the instrument range
- [ ] **sister_paper_p_reconciliation** — conflicting *P* on the same biomarker across sister papers is flagged, not averaged


---

## Part B — Stats consistency (reported results)

# Stats consistency (reported results)

Use when polishing or reviewing **already reported** numbers (Table 1, NHST lines, HR/OR with CI).  
Raw measurement tables → `02_data-processing/personal/table-signals.md`.

## Division of labor

| Mechanism | Owns |
|---|---|
| G-FACT (00) | Pipeline number drift across 02→04→05→06 |
| This note | Academic reporting consistency signals |
| `personal/table-signals.md` (02) | Raw measurement tables |
| `stats-checklist.md` | Lab reporting style (body/figures) |
| `00_orchestrator/references/manuscript-local-qc.md` | Writing actions for the same check ids |
| `06_review/personal/cross-manuscript-qc.md` | Review: annotate conflicts; do not invent numbers |

## Checks

### GRIM / Table 1 mean vs N
- See skill-library extract / scrutiny: https://github.com/lorenz-walthert/scrutiny
- Flag means that cannot arise from integer sum / N at the reported decimals
- Integer-sum models only; not every continuous physical mean

### NHST vs reported p
- Upstream: https://github.com/hplisiecki/statcheck_python
- Consistency error: statistic and p disagree
- Decision error: significance call flips after recompute

### Effect size 95% CI vs p
- Log-scale SE ≈ (ln U − ln L) / (2×1.96); Z ≈ ln(effect)/SE
- Signal if CI crosses null while p is called significant (or magnitude mismatch)
- Rounding / one-sided / adjusted p can explain mild gaps

### Optional batch p-curve
- Pile-up of significant p near 0.04–0.05 is a selective-reporting **risk signal** in a batch
- Not a default gate for a single small study

### Statistic vs threshold (`stat_vs_threshold`)
- A printed *t*, *F*, or *z* must meet the voxel-wise or cluster-forming α named in Methods at the stated df
- A statistic that only reaches a looser α contradicts the threshold sentence
- Flag both loci. Do not replace either number. A critical-value note in a comment is an estimate

### Correlation *n* (`correlation_implied_n`)
- Recompute the two-sided *P* from the reported *r* (or ρ) and the stated analysis *n*
- *t* = *r* √((*n*−2) / (1−*r*²)), df = *n*−2. Disagreement beyond rounding means that *n* is not the analysis *n*
- The enrollment *n* of one group is not automatically the correlation *n*
- Flag. Do not invent a complete-case *n*

### Multiplicity (`multiplicity_disclosure`)
- Many ROI-wise or voxel-wise correlations need a named family and a named correction, or an explicit uncorrected / exploratory label
- Silence is a fail. Do not run a correction the paper did not run

### Relative units (`relative_denominator`)
- "Relative", normalized, ratio, or scaled measures name the denominator (global mean, reference region, or the real divisor) and the units
- An undefined denominator is not interpretable. Do not guess it from the variance

### Circular analysis (`no_confirmatory_p_same_cohort`)
- Feature or ROI selection, threshold selection, and the group or performance test on the same participants, without nested CV or a bootstrap optimism correction, do not support a confirmatory *P*
- Report the *P* as descriptive / apparent
- Nested CV is not a lab default (`pipeline.md`). Do not write that it was run unless the user confirms it
- Do not invent an adjusted *P*

### Nested ROIs and score identity (`nested_roi_collinearity`, `score_transform_identity`)
- A parent region and its subregions in one model or one uncorrected family are dependent. Name that
- A score that is a linear (or other) transform of a single metric is that metric under a new label. State the transform. It is not a second biomarker

### Inclusion vs scale (`cutoff_vs_included_distribution`, `iqr_scale_sanity`)
- Median, Q1, and minimum of an included group must fall on the included side of the entry cutoff
- IQR (Q3−Q1) must lie inside the instrument's possible range
- Flag the contradiction. Do not rewrite the cutoff or the quartile

### Sister-paper *P* (`sister_paper_p_reconciliation`)
- The same biomarker and contrast with a conflicting *P* across related papers is a conflict to annotate
- Do not average *P* values. Reconciliation text belongs to 05; the review comment belongs to 06

## Into 06

Self-review / peer-review: cite this note; do not restate algorithms in 06.
Runnable helpers stay with Loopnow/Build — not A repo scripts.
On conflict, annotate only. Never invent the replacement number.


Cross-manuscript / sister-paper: `00_orchestrator/references/cross-manuscript-qc.md`.
Manuscript local QC: `00_orchestrator/references/manuscript-local-qc.md`.
