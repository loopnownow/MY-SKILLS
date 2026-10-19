# R&R re-review verification (06 qc · standards only)

**Owner:** `00_orchestrator` at `P06r` / Gate · 06 re-review. Lee = verification only; Round-1 findings frozen.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Template

Fill `00_orchestrator/templates/rr-traceability.md`:

| column | meaning |
|---|---|
| item_id | Stable Round-1 id |
| reviewer_finding | Frozen finding text |
| author_claim | What 05/07 asserts was done |
| verified | see enum |
| residual | What remains |

## verified enum

`FULLY` | `PARTIALLY` | `NOT_ADDRESSED` | `MADE_WORSE` | `CANNOT_VERIFY`

## Rules

- Re-review = **verification only** — do not open a new full pre-review.
- Response letter stays in **07** (Aitee); do not route 回复 into 06.
- Cap re-review loops at **2**, then escalate like `defects[].rounds`.

**PASS:** every open Round-1 item has a verified row; no MADE_WORSE without escalate note.
**FAIL:** missing R&R rows or new-scope review → rollback **06** (re-fill template) / escalate.
