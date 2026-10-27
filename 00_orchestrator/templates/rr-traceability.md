# R&R traceability (review ↔ revise)

Fill during **06 re-review** (`P06r`). Verification only — Round-1 findings stay frozen; do not open a new full pre-review.

| item_id | reviewer_finding | author_claim | verified | residual |
|---|---|---|---|---|
| R1-01 | | | FULLY / PARTIALLY / NOT_ADDRESSED / MADE_WORSE / CANNOT_VERIFY | |
| R1-02 | | | | |

**verified** enum: `FULLY` | `PARTIALLY` | `NOT_ADDRESSED` | `MADE_WORSE` | `CANNOT_VERIFY`

## Rules

- Lee (06) owns re-review rows; Aitee (05) owns body claims; Aitee (07) owns response claims (response is **not** routed into 06).
- Cap re-review loops at **2**, then escalate / `unresolved` like `defects[].rounds`.
- Pointers: `runtime-flow.md` (Review ↔ revise), `06_review/advanced/handoff.md`.
