# Plan card & decision nodes (00)

Load from `00_orchestrator/SKILL.md` when the run is multi-node, a new capability, or high risk.

**Grilling policy SSOT:** MY-RULES `My rule.md` §2.1 (grilling). Do not duplicate full grill text here. 00 only owns Plan card, flowchart approval, Q0–Q3, and N1–N4.

## Question policy

- **Q0** — single-node task: do not grill.
- **Q1** — one critical unknown: one question.
- **Q2** — multi-node, a new capability, or high risk: grilling is allowed (follow MY-RULES `My rule.md` §2.1).
- **Q3** — if a file or the web can answer, look it up; do not ask.

## Flow chart approval (skills)

When the user asks to **use skills for a specific multi-node task**, before specialist dispatch:

1. Show a **complete** flowchart from [`runtime-flow.mmd`](../runtime-flow.mmd) (read [`runtime-flow.md`](../runtime-flow.md)).
2. Highlight the path this run will take (entry → nodes → gates → QC loop).
3. Wait for **explicit approval**. Do not start 02–07 until they agree.
4. After approval, proceed with the 00 session pick / G0 as on the map. (One-off package adoption retired 2026-10-20; no adoption approval.)

## Plan card (before dispatch)

Default is **interactive**. Before the first specialist runs a multi-node job, or before 00 evaluates a new external capability, run **grilling** per MY-RULES `My rule.md` §2.1 (`grill-me` mode): one batched clarify round, numbered questions with recommended defaults, find facts yourself first.

Then show the plan: candidate fine ids · SOP · node order · risk gates. Wait for a nod. Do not invent `--e2e`.

Loop shape: `clarify round (grilling) → plan → execute node → file check → integrity gate → (repair broken node only) → execute`.

After that plan is approved, later crossings in the **same run** are one line: file present, gate passed, continue or pause. Still stop and wait at N2 (PHI), G-FACT on the results page, N4 (preview entry), and G-06.

## Decision nodes (one at a time)

After a pick, echo `Locking: …` then invoke the specialist. `back` / `pause` allowed.

| Node | When | Options |
|---|---|---|
| N1 SOP | "full-pipeline" / multi-stage with no lock | `statistics` / `sci-manuscript` / `research-exploration-loop` / no SOP (single skill) |
| N2 PHI | before 02 tables or clinical extraction | PHI present → de-identify / stop; none → proceed |
| N3 WRITE | `*-results.html` exists after 02 | stop at HTML / enter `sci-manuscript` |
| N4 PREVIEW | house.docx exists | enter 06 / stop |

Never `--e2e`. Session pick reuses the session lock when `session_picked_fine_ids` already covers this task, then passes G0. Otherwise enter 01. A single-node personal-layer task with no extra dependency does not ask.
