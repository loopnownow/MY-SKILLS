# Bot route (coarse id → bot, LIVE fine id → bot)

Human-readable routing table: which bot answers for a coarse id, and which bot answers for each LIVE fine id. Aitor reads this at dispatch; specialists read it to know who takes the next handoff.

**Three layers, no overlap:**

- A **coarse id is the execution seat** and equals the fine id's `a_domain`. A fine id carries no coarse field, so its bucket can never drift from its seat.
- `specialist_hint` on each row of `coarse_ids` in [`../registry.yaml`](../registry.yaml) is the **default bot** for that seat. It is the machine-side default, not a full route.
- **This file is the bot-route SSOT** for bot names in prose. [`../registry.yaml`](../registry.yaml) remains the **id SSOT**: ids, paths, statuses and counts are settled there, never here.

Ids themselves are governed by [`id-rules.md`](id-rules.md). Ownership policy (who may revise what) is governed by [`ownership-contract.md`](ownership-contract.md). Neither is restated here.

**Rules layer (every bot).** Aitor, every specialist bot (Loopnow, Victor, Aitee, Lee, Bai) and CloudAgent carry and obey `{RULES}`; `{RULES}\My rule.md` is authoritative. Skills attach only on concrete work. This table routes the work and never restates Rules text.

## Coarse id → bot

| Coarse id | Bot |
|---|---|
| 00_orchestrator | Aitor · 总调度 (control plane; not one of the five domain coarse_ids) |
| 02_data-processing | Loopnow · 码农 |
| 03_research | Victor · 检索者 (default) |
| 05_manuscript | Aitee · 科研狗 |
| 06_review | Lee · 审稿人 |
| 07_response | Aitee · 科研狗 |

Two seats share one bot: **Aitee** owns both `05_manuscript` (prose) and `07_response` (response letters). They stay separate seats because the fine ids, paths and gates differ.

`03_research` has one seat but two bots. **Victor** is the default for the seat; the single ethics-form fine id is served by **Bai** as a deliberate exception (next section and the fine-id table).

**Coding is on-seat 02, not off-loop.** Coding, scripts, and `MY-CODES` work default to **Loopnow · 码农** and stay inside the `02_data-processing` seat. Loopnow is the default coding executor. This opens no new coarse id and no new fine id. The executor changes, the seat does not.

## Off-loop / external

These are real executors that are **not** seats in the 00 main loop. They are routed by explicit handoff, never by a coarse-id default.

| Role | Bot / pack | Notes |
|---|---|---|
| ethics forms + portal submit + `{doc_root}` _Docs lookup/search/inventory | Bai · 打杂的 | fill-protocol body under 03; off 00 main loop |
| tidying / extraction / form-fill / in-repo IDE work | Cursor IDE | only when owner says 「交给cursor」 and approved; bots do not call Cline. Coding / scripts / `MY-CODES` are **not** here; they go to Loopnow on 02 |

Bai's work arrives in two shapes. Ethics forms are reached through a fine id (`fill-protocol`) whose body sits under `03_research/base/`, so the seat stays 03 while the executor is Bai. Portal submit and the `{doc_root}` lookup/search/inventory asks carry no fine id at all; Aitor routes them directly and does not self-search for general lookup asks.

Cursor is an external pack, not a seat and not a bot. It is not the default coding seat. Coding, scripts and `MY-CODES` are Loopnow on 02. A handoff to Cursor happens only when the owner says 「交给cursor」 plus approval, for tidying, extraction, form-fill, or IDE work; a bot never calls Cline on its own.

## LIVE fine id → bot

Must match the tip of [`../registry.yaml`](../registry.yaml) on `main`; currently **20** LIVE fine ids. Each id appears exactly once. Rewritten whenever the registry changes (see «Keeping this table in sync»).

| Coarse id | Fine id | Bot |
|---|---|---|
| 02_data-processing | `clean-data` | Loopnow |
| 02_data-processing | `preprocess-imaging` | Loopnow |
| 02_data-processing | `stats-analysis` | Loopnow |
| 02_data-processing | `model-evaluation` | Loopnow |
| 02_data-processing | `calc-sample-size` | Loopnow |
| 02_data-processing | `draw-flowchart` | Loopnow |
| 02_data-processing | `plot-figures` | Loopnow |
| 03_research | `verify-refs` | Victor |
| 03_research | `lit-search` | Victor |
| 03_research | `lit-fulltext` | Victor |
| 03_research | `design-study` | Victor |
| 03_research | `find-journal` | Victor |
| 03_research | `fill-protocol` | Bai (exception) |
| 05_manuscript | `write-paper` | Aitee |
| 06_review | `peer-review` | Lee |
| 06_review | `track-changes` | Lee |
| 06_review | `self-review` | Lee |
| 06_review | `simulate-reviewers` | Lee |
| 07_response | `revise` | Aitee |
| 07_response | `tighten-response` | Aitee |

Per-seat tally: 02 = 7 · 03 = 6 (5 Victor + 1 Bai) · 05 = 1 · 06 = 4 · 07 = 2.

### Fine-id notes

- **`fill-protocol` is the only Bai exception.** Its `a_domain` is `03_research` and its body is `03_research/base/fill-protocol/`, but the executor is Bai. Do not hand ethics form filling to Victor; do not move the body out of 03 to express the exception.
- **`track-changes` sits on 06 (Lee) for mechanical validate/pack.** Unpacking, validating and repacking a `.docx` so every change is tracked is a Word-format job, not a review judgement. **Manuscript Track Changes application stays with Aitee** under the ownership contract. Route the mechanical pack to Lee, the applied revision to Aitee.
- **Response letters never route to Lee or 06.** `revise` and `tighten-response` are 07/Aitee, and a response letter that arrives as input is an 07 entry, not a review.
- **`local_packs` `vocab` → Aitee / 05.** It is a local pack (lab vocabulary layers under `05_manuscript/base/vocab/`), not a fine id, so it is never a session fine-id pick. Load it as the writing-time vocabulary layer when 05 writes.

## Keeping this table in sync

1. Read the registry on `main` before editing the fine-id table. Do not copy from a branch or from memory.
2. Add or retire a row in the same change that touches `fine_ids`; the row count must equal `meta.fine_id_count_canonical` and the number of LIVE rows.
3. A new seat (`coarse_ids`) needs a bot before it needs a fine id. If no bot is named yet, stop and ask the owner rather than guessing.
4. `specialist_hint` and this file may differ in wording, never in substance. A seat whose bot changes is edited in both places.
5. Keep the tables here and link to them. Do not paste these tables into `SKILL.md`, `runtime-flow.md`, or the ownership contract; those files point here instead.
