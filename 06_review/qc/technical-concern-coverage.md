# Technical concern coverage router (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06.
**Distill of:** Yuan1z `nature-reviewer` → twelve-axis technical-concern taxonomy (Apache-2.0). **Coverage** router only — ensure the review addresses applicable axes; not a full essay or mock-review package.

## Twelve axes (mark each)

For every axis record: `applicable` | `not applicable` | `not assessable`. Absence of evidence ≠ automatic defect.

| Axis | Coverage question (one line) |
|---|---|
| novelty-significance | Advance vs prior work supported, not merely asserted? |
| mechanism-evidence | Mechanistic claims have discriminating evidence? |
| experimental-design | Controls, replication unit, sampling support inference? |
| statistical-rigor | Estimands, uncertainty, multiplicity, units adequate? |
| reproducibility | Methods/data/code detail enough for scrutiny? |
| clinical-validity | Cohort/endpoint/validation support clinical claims (if any)? |
| ethical-governance | Approvals/consent/privacy reported when required? |
| data-resource-quality | Provenance/QC/accessibility credible (if resource paper)? |
| figures-and-tables | Labels, denominators, uncertainty, legends accurate? |
| writing-clarity | Argument and abstract/body consistency understandable? |
| claim-moderation | Strength/scope language ≤ evidence? |
| causal-vs-correlative | Association vs causation distinguished by design? |

## Gate

| id | Check | Fail → |
|---|---|---|
| TC-1 | All 12 axes marked applicable / N/A / not assessable | 06 |
| TC-2 | Every `applicable` axis has at least a brief address or explicit “none identified” | 06 |
| TC-3 | Emitted concerns carry axis + severity (major/minor) + evidence pointer | 06 |
| TC-4 | No invented concerns to fill quotas; empty tier allowed | 06 |

**PASS:** TC-1–4 clean.
**FAIL:** silent skip of clearly applicable axes (esp. statistical-rigor / claim-moderation / causal-vs-correlative on prediction papers) → re-run 06 coverage pass.

*Attribution: distilled from Yuan1z0825/nature-skills `nature-reviewer` (Apache-2.0).*
