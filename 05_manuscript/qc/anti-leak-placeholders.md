# Anti-leak / placeholders (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06. Capability bodies stay in personal/base.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Standard

Missing material → **Word 批注 only**. Never invent filler in body prose. Never add "not tested" / "we did not examine…" **negation lists** (owner de-AI ban).

## Must-check

| id | Check | Fail → |
|---|---|---|
| AL-1 | No placeholder tokens in body (`TODO`, `TBD`, `??`, `XX`, lorem) | 05 Aitee — comment + remove |
| AL-2 | Gaps flagged as Word comments with owner, not invented sentences | 05 |
| AL-3 | No negation-list padding for unrun analyses | 05 — delete / comment |
| AL-4 | No leaked prompt/instruction text in manuscript | 05 |

**PASS:** AL-1…4 clean.
**FAIL:** body leak or negation-list → rollback **05** (comment-only fix; do not auto-fill).
