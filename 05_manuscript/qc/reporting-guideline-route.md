# Reporting guideline route (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06. Capability bodies other than `05_manuscript/qc/check-reporting/` stay in `05_manuscript/advanced/` and `base/`.
Inspired by ARS topology/checklists (short original text; no ARS copy).
**Router metadata:** `05_manuscript/qc/reporting-guidelines-router.json` (K-Dense peer-review catalog, MIT — ids / study_types / official URLs only; **no checklist item text**).

## How Gate · 05 / Integrity · pre-06 use this

1. Classify study type (or escalate if ambiguous).
2. Lookup primary `id` in the JSON sidecar (and keep the short table below for common radiology/prediction routes).
3. Record `guideline_chosen:` + official URL; apply **must-check subset** only.
4. Do **not** paste EQUATOR/CONSORT/PRISMA/TRIPOD item bodies into the manuscript or this folder.

## Common route table (lab default)

| Study type | Primary guideline | Official |
|---|---|---|
| Prediction / prognostic model | **TRIPOD** + **TRIPOD+AI** when ML/AI | https://www.tripod-statement.org/ |
| Diagnostic accuracy | **STARD** (+ **STARD-AI** when AI) | https://www.equator-network.org/reporting-guidelines/stard/ |
| Observational (cohort/case-control/cross-sectional) | **STROBE** | https://www.strobe-statement.org/ |
| Systematic review / meta-analysis | **PRISMA** | https://www.prisma-statement.org/ |

## Extended catalog (JSON)

~23 entries in `reporting-guidelines-router.json`: ARRIVE, CARE, CHEERS, CONSORT-2025, CONSORT-AI, COREQ, PRISMA, PRISMA-P, SPIRIT-2025, SPIRIT-AI, SQUIRE, SRQR, STARD, STARD-AI, STROBE, TRIPOD+AI, TRIPOD-LLM, plus domain metadata standards (MIAME, MIAPE, MIAPPE, MIFlowCyt, MINSEQE, MIxS). Fields: `id`, `name`, `version`, `status`, `study_types`, `report_kinds`, `required_features`, `url`.


## Relation to check-reporting

**Gate SSOT** for Integrity · pre-06 / Gate · 05 must-check subset = this file (`05_manuscript/qc/reporting-guideline-route.md` + JSON sidecar). **Writing / audit stack** (CLAIM, CLEAR, PROBAST-AI, METRICS/RQS, IBSI, FUTURE-AI, …) = `05_manuscript/qc/check-reporting/radiology-reporting/guideline-router.md`. Do **not** substitute the check-reporting stack for the gate subset, or the gate subset for a full writing audit.

Also-check when imaging AI / radiomics (record if applicable; not a substitute for the table above):
- **CLAIM 2024** — DL/AI imaging methods reporting.
- **CLEAR** (+ METRICS/RQS + IBSI as needed) — hand-crafted radiomics.
- Full stacks and Nature Reporting Summary logistics → `05_manuscript/qc/check-reporting/radiology-reporting/guideline-router.md`.

## Ambiguity

If study type is unclear or mixed — **ask / escalate**. Do **not** force the nearest guideline.

## Must-check subset (record pass/fail)

Record: `guideline_chosen:` (TRIPOD[+AI] | STARD[+AI] | STROBE | PRISMA | other+id+URL from JSON).

| id | Check | Fail → |
|---|---|---|
| RG-1 | Chosen guideline named in Methods or cover note | 05 Aitee (name) / user (pick) |
| RG-2 | Primary outcome / reference standard / analysis set stated | 05 / 02 as responsible |
| RG-3 | Flow of participants or samples described (or figure cited) | 05 / 02 Figure 1 |
| RG-4 | Discrimination and/or accuracy metric matches study type (e.g. AUC for prediction) | 02 Loopnow / 05 prose |
| RG-5 | Missing-data / exclusions handled or declared | 02/05 per source |

**PASS:** RG-1 done + applicable RG-2–5 clean or Word-commented with owner.
**FAIL:** missing guideline choice or silent skip of applicable subset → rollback station **05** (or escalate if ambiguous).

*Attribution: short must-check original; extended id→URL table metadata from K-Dense-AI/scientific-agent-skills `peer-review` (MIT).*
