# Reporting guideline route (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06. Capability bodies stay in `05_manuscript/personal/` and `base/`.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Route table

| Study type | Primary guideline | Official |
|---|---|---|
| Prediction / prognostic model | **TRIPOD** + **TRIPOD+AI** when ML/AI | https://www.tripod-statement.org/ · https://www.equator-network.org/reporting-guidelines/tripod-statement/ |
| Diagnostic accuracy | **STARD** (+ **STARD-AI** when AI) | https://www.equator-network.org/reporting-guidelines/stard/ |
| Observational (cohort/case-control/cross-sectional) | **STROBE** | https://www.strobe-statement.org/ · https://www.equator-network.org/reporting-guidelines/strobe/ |
| Systematic review / meta-analysis | **PRISMA** | https://www.prisma-statement.org/ · https://www.equator-network.org/reporting-guidelines/prisma/ |

Do **not** paste full official checklists here. Record which guideline this manuscript chose, then apply a **must-check subset** only.

## Ambiguity

If study type is unclear or mixed → **ask / escalate**. Do **not** force the nearest guideline.

## Must-check subset (record pass/fail)

Record: `guideline_chosen:` (TRIPOD[+AI] | STARD[+AI] | STROBE | PRISMA | other+URL).

| id | Check | Fail → |
|---|---|---|
| RG-1 | Chosen guideline named in Methods or cover note | 05 Aitee (name) / user (pick) |
| RG-2 | Primary outcome / reference standard / analysis set stated | 05 / 04 as responsible |
| RG-3 | Flow of participants or samples described (or figure cited) | 05 / 04 Figure 1 |
| RG-4 | Discrimination and/or accuracy metric matches study type (e.g. AUC for prediction) | 04 Loopnow / 05 prose |
| RG-5 | Missing-data / exclusions handled or declared | 02/04/05 per source |

**PASS:** RG-1 done + applicable RG-2…5 clean or Word-commented with owner.
**FAIL:** missing guideline choice or silent skip of applicable subset → rollback station **05** (or escalate if ambiguous).
