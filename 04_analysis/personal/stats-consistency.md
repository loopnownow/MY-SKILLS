# Stats consistency (reported results)

Use when polishing or reviewing **already reported** numbers (Table 1, NHST lines, HR/OR with CI).  
Raw measurement tables → `02_data-processing/table-qc/`.

## Division of labor

| Mechanism | Owns |
|---|---|
| G-FACT (00) | Pipeline number drift across 02→04→05→06 |
| This note | Academic reporting consistency signals |
| `table-qc` (02) | Raw measurement tables |
| `stats-checklist.md` | Lab reporting style (body/figures) |
| `05_manuscript/personal/pre-submit-consistency.md` | Writing actions for the same check ids |
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
- Nested CV is not a lab default (`0rad-pipeline-rules.md`). Do not write that it was run unless the user confirms it
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
