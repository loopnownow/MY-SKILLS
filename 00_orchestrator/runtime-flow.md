# Runtime flow (legend)

**Sole official picture:** [`runtime-flow.mmd`](runtime-flow.mmd). Edit only that diagram. This file is a short legend, not a second rulebook.

Gate detail SSOT: [`gates.md`](gates.md). Diagram nodes use gate ids directly (`G0`, `G-PHI`, `G-FACT`, `G-STATS`, `G-05`, `G-06`, `G-07`, `G-LIT`, `G-CODE`).

00 is the control layer (entry, dispatch, gates, rollback, R&R loop). Domain work lives in seats 02 / 03 / 05 / 06 / 07. Ownership: see `00_orchestrator/references/ownership-contract.md`. Skill-evolution policy is in `references/skill-evolution.md` — observe and propose only.

Layer duties, the normative run order, post-QC revise via `advanced/`, and drift rules live in [`references/base-vs-advanced-top-loops.md`](references/base-vs-advanced-top-loops.md).

## How to read the diagram

1. **Entry.** Detect materials and intent, then enter the named station. mid-entry is allowed (existing HTML → 05; existing manuscript → 06); do not re-run from 02. If a results page and a reviewer letter are both present and no entry was named, ask. Multi-node / new capability / fine ids needed → grilling + Plan card + flowchart approval first.
2. **G0.** Every independent run needs one fine-id pick (ask-each-run). Reuse `session_picked_fine_ids` when it already covers this task. Empty set → notify and re-ask; never silent fallback. A single-node advanced-layer task with no fine-id dependency does not ask.
3. **Advance only on PASS.** FAIL → locate the minimal responsible node → local rework or roll back to the earliest affected node. The rework budget is per same defect: `defects[].rounds` ≤ 3, then `unresolved` (written once here and on the diagram; see also `gates.md`). Do not restart the whole chain from Start.
4. **Design lock (seat 03).** `ref/design-study.md` plus owner-accepted `ref/design-lock.md` are required before formal statistics. If missing or unaccepted, stop; do not run **G-STATS**. Responsible seat is 03 until the owner accepts. See `gates.md`.
5. **Literature.** Writing or review must pass 03 `verify-refs` (**G-LIT**) before G-05 is done and inside 06. Mid-entry does not waive it. A 05 pass does not waive the 06 pass. 05 and 06 do not self-certify lit.
6. **R&R.** 00 controls the loop. 05 applies body Track Changes. 07 writes the response letter. 06 re-reviews (verification only) and does not write letters. Loop cap and recovery are on the diagram / `gates.md`.
7. **Done.** `结束`, or this run's file is on disk and the last gate PASS → `pipeline.stage: done`. Pause, or stop after the results page / before pre-review, leaves `stage` at the current station.

The current manuscript file is 当前稿（按 `{RULES}/project-ref-layout`）, not a hardcoded `Manuscript_*_house.docx` trigger.

## SOP entry points

00 calls these SOP bodies directly (`workflows/`):

| SOP | When |
|-----|------|
| `statistics` | image/ROI/features → 02 HTML |
| `sci-manuscript` | HTML → 当前稿（按 `{RULES}/project-ref-layout`）→ pre-review / response |
| `research-exploration-loop` | research gaps / topic exploration |
| `question-to-reference` | question → evidence → design → data → brief (**R1–R5**) |
| `review-isolation` | review isolation / simulate→self/peer |

`question-to-reference` stages: **R1** question, **R2** evidence, **R3** design, **R4** data requirement, **R5** research brief. Details stay in the SOP files.

Seats 00 / 02 / 03 / 05 / 06 / 07 are stable ids, not a sequence. The specialist roster is `registry.yaml`; record only exceptions (fill-protocol → Bai). Other files write seat numbers.
