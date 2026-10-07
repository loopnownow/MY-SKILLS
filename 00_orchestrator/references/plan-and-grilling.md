# Plan card, grilling, flowchart approval (00)

Load from `00_orchestrator/SKILL.md` when the run is multi-node, a new capability, or will use mounts.

## Question policy

- **Q0** — single-node task: do not grill.
- **Q1** — one critical unknown: one question.
- **Q2** — multi-node, a new capability, or high risk: grilling is allowed.
- **Q3** — if a file or the web can answer, look it up; do not ask.

## Flow chart approval (skills / mounts)

When the user asks to **use skills or mount packs for a specific task**, before session mount pick or specialist dispatch:

1. Show a **complete** flowchart from [`runtime-flow.mmd`](../runtime-flow.mmd) (read [`runtime-flow.md`](../runtime-flow.md)).
2. Highlight the path this run will take (entry → nodes → gates → QC loop).
3. Wait for **explicit approval**. Do not load mounts or start 02–06 until they agree.
4. After approval, proceed with 01 session mount pick / G0 as on the map.

## Plan card (before dispatch)

Default is **interactive**. Before the first specialist runs a multi-node job, or before 01 evaluates a new external capability, run **grilling** (`../grilling/SKILL.md`, `grill-me` mode): one batched clarify round, numbered questions with recommended defaults, find facts yourself first.

Then show the plan: candidate mount ids · SOP · node order · risk gates. Wait for a nod. Do not invent `--e2e`.

Loop shape: `clarify round (grilling) → plan → execute node → file check → integrity gate → (repair broken node only) → execute`.

After that plan is approved, later crossings in the **same run** are one line: file present, gate passed, continue or pause. Still stop and wait at N2 (PHI), G-FACT on the results page, N4 (preview entry), and G-06.

## Decision nodes (one at a time)

After a pick, echo `Locking: …` then invoke the specialist. `back` / `pause` allowed.

| Node | When | Options |
|---|---|---|
| N1 SOP | 「全线」 / multi-stage with no lock | `radiomics-study` / `sci-manuscript` / `research-exploration-loop` / no SOP (single skill) |
| N2 PHI | before 02 tables or clinical extraction | PHI present → de-identify / stop; none → proceed |
| N3 WRITE | `*-results.html` exists after 04 | stop at HTML / enter `sci-manuscript` |
| N4 PREVIEW | house.docx exists | enter 06 / stop |

Never `--e2e`. MountQ reuses the session lock when `session_picked_fine_ids` already covers this task, then passes G0. Otherwise enter 01. A single-node personal-layer task with no mounted dependency does not ask.
