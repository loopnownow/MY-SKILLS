# Sole official runtime map

**Machine source of truth (edit only this diagram):** [`runtime-flow.mmd`](runtime-flow.mmd)

Sub-flows (writing chain, review chain, lab stats, R&R triage) are **branches** on that diagram — do not maintain a second master map. When updating entry / QC / rollback rules, revise only the `.mmd`.

00 = control layer (entry, dispatch, Gate, rollback). Domain work lives in 02–07; the routing index lives in **00**; skill-evolution policy is in `references/skill-evolution.md` — observe and propose only; do not execute flows there.



## Base / personal layering

**Main loop:** base fine-ID **first-pass** capability loops -> **00 QC gate** -> personal/top **re-loops**.

| Layer | Repo | Owns |
|---|---|---|
| **base** | MY-SKILLS `NN_slug/base/` | Capability bodies / fine-ID loops |
| **00** | MY-SKILLS `00_orchestrator` | QC gate between base first-pass and personal/top re-loop |
| **personal / top** | MY-SKILLS | Personal top-layer route/handoff/authority (03-07). Capability bodies for 02–07 live under `NN_slug/base/` |

Post-QC A re-loops (as needed):

- **03** -- may trigger `verify-refs` + `retraction-watcher` (bodies under `NN_slug/base/`)
- **05** -- `humanize` (report-only lint, then de-AI pass) alongside Aitor-format/voice; vocab on first write
- **06** -- post-QC **re-review only**
- **07** -- **final authority for response** (`revise`/`tighten-response` source my-skills (in-repo base); tone-polish is on-demand inside tighten-response)

Do not change fine IDs for stats-analysis / figures / data-processing / study-design.


## Seats on the map (2026-10-17 tidy)

| Coarse | Seat | On-map role |
|---|---|---|
| 02 | Loopnow | data / stats / figures |
| 03 | Victor | research / lit / journal selection / citation-verify |
| 05 | Aitee | manuscript prose + Track Changes |
| **06** | **Lee** | **review / pre-review / re-review only** |
| **07** | **Aitee** | **response letter final authority** |
| 00 | Aitor | QC / gates / chain |
| (off-loop) | **Bai** | ethics forms (`03_research/base/fill-protocol`) + portal submit |

**Response → 07 / Aitee. Review → 06 / Lee.** Do not route response letters to 06. Gate ids (`G0`, `G-PHI`, `G-FACT`, `G-LIT`, `G-CODE`, `Gate · STATS/05/06/07`) stay stable.


## How to read the map

1. **Detect locks entry and exit** — if HTML already exists you may stop at 05; do not force 06. If stats already exist you may mid-enter 05; if a manuscript already exists you may mid-enter 06; do not re-run from 02. When a results page and a reviewer letter are both present and no entry was named, ask which station to enter. Multi-node / new capability / fine ids needed → grilling + Plan card + flowchart approval first. `结束` (end), or this run’s file is on disk and the last gate PASS → `pipeline.stage: done`. Pause, or stop after the results page / before pre-review: leave `stage` at the current station. **Same defect** `defects[].rounds` still failing on round 3 → `unresolved`; stage does not advance (not global `qc.rounds`). Inside one already-approved run, later station passes report one line; PHI, results-page numbers, pre-review entry, and the review gate still stop. **Any writing or review (including mid-entry)** must pass 03 `citation-verify` before Gate · 05 done and inside 06 (claim→ref table + spot-check strong claims against full text). A 05 verify does not waive 06. Aitee and Lee must not self-certify literature. Lee still does statement consistency first, then data consistency; literature accuracy is joint with Victor. Ownership: see `00_orchestrator/references/ownership-contract.md`.
2. **Advance only on PASS** — every node has an exit Gate; if not at the destination, enter the downstream node.
3. **00 / G0 = pre-execution dependency** — every independent run needs one fine-id pick. When `session_picked_fine_ids` already covers this task’s fine ids, reuse the session lock; do not re-ask. Otherwise enter the 00 registry pick. Single-node personal layer with no fine id dependency does not ask (e.g. polish one sentence). Not a decorative master gate.
4. **QC loop** — FAIL → locate → impact (local vs roll back to earliest affected node) → re-enter the failed node within budget → Gate again; never re-run the whole chain from Start. Local recovery reuses the session fine-id lock and returns to the failed node. Re-enter 01 only when a dependency is missing, provenance is stale, or a new capability is needed.
5. **Budget exhausted** — Escalate → wait for the user; after authorization, reset **that defect’s** `defects[].rounds`.
6. **Naming** — diagram `Gate · NN` ↔ `gates.md` `G-NN` (e.g. `Gate · STATS` = `G-STATS`). `G0` / `G-PHI` / `G-FACT` / `G-LIT` / `G-CODE` share the same names.

## Gate selection (source of truth `gates.md`)

Diagram `Gate · NN` = the set chosen from the table below (detail and failure columns follow `gates.md`).

| Task / node | Applicable gates |
| --- | --- |
| 00 external Skill / Fine id | G0. Enter only when this run needs a new fine-id pick |
| 02 data processing | Exit is G0 + G-PHI (when applicable) + artifact exists, then enter 02. No separate 02 gate id and no 02-local G-FACT. N2 = PHI stop |
| 02 personal/coding.md / deep code review | G-CODE |
| 03 literature research | Exit is G0 + G-LIT + evidence/citation artifacts. No separate 03 gate id and no 03-local G-FACT |
| 02 stats / figures | G0 + G-FACT (fact chain after 02 HTML) + G-STATS. Numbers and figures come from HTML / settings; reporting-guideline checklists are not G-STATS. N3 WRITE = stop at HTML or enter writing |
| 05 manuscript writing | G0 + G-FACT (re-check after 05 house.docx) + G-LIT + G-05 (includes style-lint sub-check). Before Gate · 05 / done, 03 citation-verify must PASS (semantic label **G-CIT-1**, draft evidence verify; `03_research/personal/citation-verify.md`). N4 PREVIEW = enter 06 or stop |
| 07 reply to reviewers | G0 + response resolution + G-LIT when cites appear; 07 final authority; revise/tighten-response stay source my-skills (in-repo base); tone-polish is on-demand inside tighten-response |
| 06 review / R&R | G0 + G-LIT + G-05 + G-06; also run G-FACT when numbers are cited (`gates.md`: before 06 if numbers cited). Inside 06, citation-verify semantic label **G-CIT-2** (post-revision / inside 06) is mandatory; G-CIT-1 does not waive G-CIT-2. Lee owns statement then data consistency; literature accuracy is joint with Victor. Ownership: see `00_orchestrator/references/ownership-contract.md` |
| Full 02→05→06 | Each node exit per the table above; G-FACT only after 02 HTML, after 05 house.docx, and when 06 cites numbers |

Personal layers (writing voice / review frame) = `05_manuscript/personal`, `06_review/personal`. Sentence authority and verdicts sit in the personal layer; capability bodies live under `NN_slug/base/`.

## Dispatch conflict (summary)

User-specified → controlling Skill → required upstream → required external packs → personal layer → helpers → QC.
Conflict: A personal layer beats an external pack; one source per fine ID. **QC rollback beats normal dispatch order.**

- G-05 includes the `style-lint` sub-check (see gates.md). No new gate ID. Do not add a 02-only or 03-only gate id. Citation-verify is a branch on `runtime-flow.mmd` (Lit05 / semantic label G-CIT-1 before Gate · 05; Lit06 / semantic label G-CIT-2 inside 06). G-CIT-1 does not waive G-CIT-2. These labels are not new gate ids.

## Integrity · pre-06 / post-re-review (named nodes, not new gate ids)

**Inspired by ARS pipeline topology** (short original text only; no ARS copy).

| Node | Where | Reuses (existing gates/checks) | On FAIL |
|---|---|---|---|
| **Integrity · pre-06** (`I25`) | After Gate · 05 / N4→06, and mid-entry Need06 (Fine id→Ready→…→Dispatch→I25→P06) | **G-FACT** (when numbers cited) + **G-CIT-1** / **G-LIT** (Must run citation-verify even on mid-entry Need06 when Gate · 05 was skipped) + **05 reporting-guideline subset** + short AI-failure / manuscript-local-qc spot checklist (`05_manuscript/qc/manuscript-local-qc.md`) | HARD-style block before Lee 06 (same recovery as G-FACT / G-CIT) |
| **Integrity · post-re-review lite** (`I45`) | After `P06r` 06 re-review | G-FACT spot + AI-fail lite (not full first-pass) | Locate / local rework |

Do **not** invent a new `G-*` id for these stations. They are compositions documented in `gates.md`.

P1 05 qc pointers (Gate · 05 / Integrity · pre-06): `refs-verified.md`, `venue-compliance-minima.md`, `venue-currency.md`, `data-code-availability.md`. 07 routing: `07_response/base/routing.md` (Aitee; Lee does not draft responses). 06 appraisal router when needed: `06_review/qc/appraisal-tool-route.md`.


## Review ↔ revise topology (R&R)

After 06 first-pass findings that need fix:

1. **Rev** decision → **05** (body Track Changes, Aitee) and/or **07** (response letter, Aitee).
2. Body fixes return to **`P06r` 06 re-review** (Lee): **verification only**; Round-1 findings frozen; fill R&R traceability (`00_orchestrator/templates/rr-traceability.md`).
3. **I45** integrity-lite → optional second revise (same Rev) → final out.
4. **Cap:** re-review loops ≤ **2**; then escalate / `unresolved` like `defects[].rounds`.

Seats unchanged: **Lee = 06 review/re-review**; **Aitee = 05 + 07**. Do **not** route response to 06.


## Checkpoint tiers (FULL / SLIM / MANDATORY)

| Tier | When | Behavior |
|---|---|---|
| **FULL** | Decision points (entry/plan, N2/N3/N4, gate FAIL needing user choice, budget escalate) | Show options; wait for explicit decision |
| **SLIM** | User already said continue / same approved run next station | One-line status; do not re-grill |
| **MANDATORY** | Integrity FAIL (I25/I45), review decision (Rev / re-review verdict), before `stage: done` | Must stop for user (or recorded PASS) |

**Rule:** after **≥4 consecutive SLIM continues**, force the next checkpoint to **FULL**.


## Domain QC standards (not capability bodies)

Pass/fail checklists live under domain `qc/` only: `05_manuscript/qc/` (Gate · 05 / Integrity · pre-06) and `06_review/qc/` (Gate · 06 / `P06r` re-review). 00 loads them at gate time; specialists do not self-certify via `qc/`. See `gates.md` Manuscript local QC + Integrity compositions. P0 absorb also loads `05_manuscript/qc/figure-stats-legend.md`, `figure-qa-minima.md`, `reporting-guidelines-router.json` and `06_review/qc/stats-failure-modes.md`, `forensic-consistency.md`, `technical-concern-coverage.md`, `review-release-gates.md` (see `gates.md`).

## Before skills / fine ids (standing)

When the user requests skills or external fine ids for a concrete task: show this official map in full, highlight the run path, and **wait for approval** before the 00 pick or specialist execution. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse that lock after approval instead of asking again. A single-node personal-layer task with no live dependency does not ask (example: polish one sentence). Do not invent a second master diagram — only highlight branches on `runtime-flow.mmd`.

Personal layers also include `07_response/personal` (response final authority). Flow: base fine-ID first-pass -> 00 QC -> personal/top re-loop.
