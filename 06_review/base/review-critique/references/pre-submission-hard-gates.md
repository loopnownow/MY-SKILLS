# Pre-submission hard gates

Use this reference for a final submission audit, rejected-paper rescue, or any manuscript meant for a high-level imaging/Nature-family venue. The purpose is to prevent the team from polishing around a fatal weakness.

## Gate logic

Each gate is `PASS`, `CONDITIONAL`, or `FAIL`.

- `PASS`: evidence is present and manuscript text/figures report it clearly.
- `CONDITIONAL`: acceptable only if the limitation is explicitly bounded and unlikely to decide the editorial outcome.
- `FAIL`: do not submit until fixed, unless the author intentionally chooses a lower-scope venue and states the risk.

## Hard gates

| Gate | What to check | Route if failed |
|---|---|---|
| Contribution map | The paper has a specific clinical/methodological contribution, not just "we built a model" | `05-write-manuscript`, `03-design-experiment` |
| Data integrity | Patient-level split, no leakage, correct labels/reference standard, exclusions documented | `02-radiomics-habitat`, `02-imaging-qc` |
| Validation | Internal/temporal/external/multicenter/prospective validation matches the claim level | `03-design-experiment`, `04-stats-guide` |
| Results-as-validation | Every major claim maps to a result/figure/table and does not exceed evidence | `05-write-manuscript`, `04-stats-guide` |
| Statistical completeness | CIs, calibration, DCA/clinical utility when relevant, multiplicity, survival assumptions, sample-size/event limits | `04-stats-guide` / `04-model-eval` |
| Reporting stack | CLAIM/TRIPOD+AI/CLEAR/STARD/IBSI/RQS/Nature Reporting Summary items are materially satisfied | `05-write-reporting` |
| Figure/data crosswalk | Figures match data and manuscript claims; no render/overlap defects | `04-fig-plot` / `04-fig-flow` |
| Citation verification | Key background, novelty, comparison, and guideline claims are supported by a fixed two-pass claim audit | `03-lit-cite` / `05-write-manuscript` radiology-citation |
| Ethics/data availability | IRB/consent/de-identification/data availability/code availability are consistent | `05-write-manuscript` radiology-ethics |
| Reviewer objection register | Likely objections are anticipated with evidence or bounded language | relevant skill |

## Two-pass claim audit gate

Before final submission, run or request `../../05-manuscript/write-manuscript/radiology-citation/claim-verification-gate.md` for the abstract, Key Results, figure legends, tables, Discussion comparison claims, novelty claims, and graphical abstract text.

| Pass | Requirement | Failure mode |
|---|---|---|
| Extraction | Fixed list of claims with IDs and locations | hidden unchecked claims |
| Verification | Each claim has source/manuscript-data support status | unsupported or numerically wrong claims |

Do not declare a paper ready if an abstract or figure/table claim is unsupported, even when the prose sounds polished.

## Reviewer objection register

Create this table before submission:

| Likely reviewer objection | Evidence already in manuscript | Current weakness | Preventive fix | Severity |
|---|---|---|---|---|
| No external validation | Temporal validation only | claim says generalizable | soften claim / add external cohort | Blocker/Major |
| Calibration absent | none | risk model reports only AUC | add calibration plot/Brier or remove risk claim | Major |

This register turns pre-review into an action plan, not just criticism.

## Readiness verdict

Use one of these:

- **Ready**: all hard gates pass; only minor polish remains.
- **Ready with declared risk**: one or more conditional gates, with bounded claims and target venue adjusted.
- **Major revision before submission**: one or more major gates fail but are fixable.
- **Not ready**: fatal design/data/reporting gap cannot be fixed without new analysis/data.

## Output table

| Gate | Status | Evidence/location | Risk if ignored | Required fix |
|---|---|---|---|---|
| Validation | FAIL | no external/temporal validation | major revision or rejection | revise claim or add validation |

Do not let good language, attractive figures, or a strong topic compensate for a failed hard gate.
