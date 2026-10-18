# AI + public-data / imaging peer-review checklist

Short gate list for manuscripts that train or evaluate AI (especially imaging) on public corpora. Use beside `MODULE.md` / dealbreakers; cite items with `[B:06-review-peer]` when they drive a Major/Minor.

## Framing

- [ ] **Dual-path / multimodal wording** — If pathways use different corpora or units (e.g. patient-level clinical vs image-level morphology) and are never joint-evaluated on the same subjects, reject “dual pathway assessment / unified framework” framing; prefer parallel secondary analyses / methodological stress-testing.
- [ ] **External validation language** — Reserve “external validation/evaluation” for true transport of the development model to an independent cohort. Within-corpus holdouts after decontamination are **not** external validation.
- [ ] **No joint nomogram on heterologous data** — Do not imply individualized multimodal prediction / joint nomogram when pathways share no patients.

## Labels & circularity

- [ ] **Label circularity** — Criterion/proxy features that reconstruct the label (including near-criterion signs) must be justified, sensitivity-tested, or removed; do not claim “criterion-free” without that audit.
- [ ] **Phenotype / subgroup endpoints** — When diagnosis is a composite rule (e.g. Rotterdam ≥2/3), missing phenotype-subgroup analyses are often a Major limitation; morphology markers already used in the rule (e.g. follicle count for PCOM) must not be treated as the diagnostic endpoint inside that same subgroup.
- [ ] **Morphology ≠ clinical diagnosis** — Imaging positives labeled as morphology (e.g. PCO) must not be silently treated as adjudicated clinical disease (e.g. PCOS) in objectives, conclusions, or translational claims.

## Statistics

- [ ] **VIF / multicollinearity** — Report VIFs (and threshold) when claiming collinearity is not problematic; keep that claim in Results, not Methods.
- [ ] **Multiple comparisons** — State multiplicity correction for Table-1–style between-group batteries, or justify unadjusted p-values.
- [ ] **DeLong / pairwise AUC p** — Ranking CV or test AUCs by point estimate alone is insufficient; provide paired comparison p-values when claiming superiority.

## Leakage & metadata

- [ ] **Leakage / patient-level splits** — Image-level splits, duplicate test folders, or missing patient/exam IDs are lower bounds only; primary claims must rest on duplicate-aware / group-wise designs and must not overstate independence.
- [ ] **Metadata-only baseline** — For imaging AI on public sets, require a metadata/shortcut baseline; near-perfect metadata AUC collapses diagnostic claims.
- [ ] **Outlier rules by distribution** — Condition IQR vs parametric outlier rules on normality/distribution assessment; report which rule applied to which variables.

## Reporting

- [ ] **TRIPOD+AI / CLAIM** — Imaging AI classification should map CLAIM (or justify coverage inside TRIPOD+AI), including partitions, overfitting controls, failure analysis.
- [ ] **Code/data availability consistency** — Methods “repository included” vs “upon request” must match; prefer a persistent identifier.
