# Stats failure-mode taxonomy (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06 / Integrity · pre-06 (composition with G-FACT when numbers cited).
**Distill of:** Yuan1z `nature-statistics` → `common-failure-modes` + severity from `reviewer-checklist` (Apache-2.0). Original short taxonomy; state risk + rollback, do not accuse authors.

## Severity

| Level | Meaning | Typical rollback |
|---|---|---|
| **P0** | Likely undermines a central claim | **04** analysis and/or **05** claim wording; HARD with G-FACT if numbers contradict |
| **P1** | Important reporting/interpretation risk | **05** / **04** revise; annotate if review-time |
| **P2** | Clarity/presentation | **05** legend/prose polish |

## P0 taxonomy (HARD when central)

| Mode | Signal (short) | Fail → |
|---|---|---|
| Pseudoreplication | `n` = cells/fields/technical wells while claim needs animal/patient/culture/donor/batch | 04 / 05 |
| Uncorrected multiplicity | Many contrasts; selected significances only; family undefined | 04 / 05 |
| Wrong interaction inference | “A sig, B not ⇒ A differs from B” without interaction/effect contrast | 04 / 05 |
| Analysis-unit mismatch | Paired/nested/longitudinal design analyzed as independent | 04 |

## P1 taxonomy

| Mode | Signal (short) | Fail → |
|---|---|---|
| Significance-only conclusion | Stars/thresholds without effect size or uncertainty | 05 / 04 |
| Small-sample overclaim | Tiny `n`, strong language, no interval | 05 |
| Unsupported parametric assumptions | Small/skewed data; no rationale | 04 / 05 |
| Unclear outlier/exclusion handling | Vague removals; post-hoc risk | 04 / 05 |
| Association written as mechanism/causality | Design does not support | 05 |

## P2 (spot only)

Undefined error bars; panel-specific `n` missing; star legend undefined; software/version omitted; `ns` hiding exact *p*.


## Soft-check Hook D — lab extreme / exclusion

| Id | When | Fail → comment |
|---|---|---|
| **Hook D** (`LAB-EXTREME-REVIEW`) | Outlier / exclusion review of extreme lab covariates | `LAB-EXTREME-REVIEW`: list value vs soft ceiling and nearest cohort quote `record_id`; request human check of unit and inclusion criteria. |

Lab-ref soft-check contract (detect only; **never** auto-edit manuscript numbers): `D:\0Grok\0doc\04-lab-reference\lab-ref-ranges\qc\gate-hooks.md` (wrap mirror: `/workspace/lab-ref-ranges-wrap-20261019/qc/gate-hooks.md`). Soft only; `confidence=gap` analytes → NOT_APPLICABLE.

## Cross-link

- Spot list: `06_review/qc/stats-reporting-spotcheck.md`
- Legend minima: `05_manuscript/qc/figure-stats-legend.md`
- Forensic layers: `06_review/qc/forensic-consistency.md`

**PASS:** no open P0 on central claims; P1 commented or fixed.
**FAIL:** open P0 on central claim → rollback **04**/**05**; compose with **G-FACT** if arithmetic/lineage also broken.

*Attribution: distilled from Yuan1z0825/nature-skills `nature-statistics` (Apache-2.0).*
