# Stats / reporting spot-check (06 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 06. Stats definitions live in `04_analysis`; this is a short review spot list.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Radiology / prediction spot list

| id | Check | Fail → |
|---|---|---|
| SR-1 | Point estimate with **CI** where inference is claimed | 04 / 05 |
| SR-2 | **Multiplicity** acknowledged or avoided (no silent p-hacking list) | 04 / 05 |
| SR-3 | **Discrimination** (e.g. AUC) and **calibration** (or explicit absence) for prediction models | 04 / 05 |
| SR-4 | Participant **flow** / diagram cited where applicable (Figure 1 / STROBE-like) | 05 / 04 |
| SR-5 | Train/test (or internal validation) split stated; no "Development set" wording | 04 / 05 |

**PASS:** applicable SR-* clean or Word-commented.
**FAIL:** silent omission of CI/discrimination when model claims made → annotate (06) + responsible station rollback.
