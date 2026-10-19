# Figure stats legend minima (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06.
**Distill of:** Yuan1z `nature-statistics` → `figure-statistics` (Apache-2.0). Original short minima; no Nature prose dump.

## Per quantitative panel (PASS required when panel supports a claim)

| Must state | Fail → |
|---|---|
| What points / bars / boxes / lines / shaded regions represent | 05 legend |
| Exact definition of `n` (independent unit named) | 04 / 05 |
| Center + spread convention (mean±s.d. / mean±s.e.m. / median+IQR / CI / model estimate) | 05 |
| Test or model used (or “descriptive only”) | 04 / 05 |
| Multiple-comparison correction status when several contrasts shown | 04 / 05 |
| Exact *p* or defined star thresholds | 05 |

## Plot-type minima

| Type | Extra PASS | Fail → |
|---|---|---|
| Bar | Prefer independent points; if bars only, error-bar definition + panel `n` | 05 / 04 |
| Box | Median, box bounds, whisker rule, outlier rule, `n` | 05 |
| Violin | Point meaning + independent-unit definition (cell-level ≠ experiment-level) | 04 / 05 |
| Time course | Same units over time; repeated-measures / mixed model when inference uses all times | 04 |
| Heat map / omics | Scaling/normalization; FDR or multiplicity for highlighted features; post-hoc selection disclosed | 04 / 05 |
| Regression / correlation | Coefficient, `n`, independence of points; association vs causal wording | 04 / 05 |

## Cross-link

- Failure taxonomy: `06_review/qc/stats-failure-modes.md`
- Spot list: `06_review/qc/stats-reporting-spotcheck.md`
- Figure image/layout minima: `05_manuscript/qc/figure-qa-minima.md`

**PASS:** applicable rows clean or Word-commented with owner.
**FAIL:** silent missing `n`/spread/test on claim-bearing panels → rollback **05** (prose/legend) or **04** (analysis).

*Attribution: distilled from Yuan1z0825/nature-skills `nature-statistics` (Apache-2.0).*
