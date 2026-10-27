# Anti-leak / placeholders (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06. Capability bodies stay in advanced/base.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Standard

Missing material → **Word 批注 only**. Never invent filler in body prose. Never add "not tested" / "we did not examine…" **negation lists** (owner de-AI ban).

**Process-negation / disclaimer / CYA / incompleteness (owner 2026-10-21; reinforce 2026-10-23):** Language that flags work not done (agent hedges or CYA; e.g. 「未做」/ *we did not* / *not performed*) **must not appear in 正文**. It may appear **only** in Word 批注, and every such 批注 **must** include **建议修改后内容**—not a bare flag. Empirical negative findings that are study results are allowed in 正文. Fail → remove from body / move to comment with suggested rewrite.

## Must-check

| id | Check | Fail → |
|---|---|---|
| AL-1 | No placeholder tokens in body (`TODO`, `TBD`, `??`, `XX`, lorem) | 05 Aitee — comment + remove |
| AL-2 | Gaps flagged as Word comments with owner, not invented sentences | 05 |
| AL-3 | No negation-list padding for unrun analyses | 05 — delete / comment |
| AL-4 | No leaked prompt/instruction text in manuscript | 05 |
| AL-5 | Body has no process-negation / disclaimer / CYA / incompleteness hedges (e.g. 「某某未做」「我们未做」「未进行…」; *not performed* / *we did not* / *was not done* / *not examined*). Empirical negative findings that are study results are OK. If the process point must be recorded: **Word 批注 only**, and the comment **must** include suggested revised body wording (建议修改后内容). Bare flags fail. | 05 — strip from 正文; comment with rewrite |

**PASS:** AL-1…5 clean.
**FAIL:** body leak, negation-list, or disclaimer/未做-class in body (or a bare disclaimer comment without suggested rewrite) → rollback **05** (comment-only fix; do not auto-fill).

Shared compose pointer for 06/07: `disclaimer-comment-only.md` under those domains' `qc/`.
