---
name: rebuttal-protocol
description: >
  Journal-first point-by-point rebuttal protocol: atomize concerns, provenance /
  commitment / coverage gates, analysis triad, revision checklist. Tone defers
  to `07_response/advanced/`. No auto new experiments.
owner: "07_response/base/revise/MODULE.md"
---

# Rebuttal protocol (journal point-by-point)

Extends [mode-3-response.md](mode-3-response.md). Default venue shape is **journal point-by-point**, not ICML/OpenReview character-budget paste.

Advanced opening banks and the advanced letter voice stay in `advanced/` — do not invent a separate voice.

## Keep (hard)

1. **Atomize** every reviewer concern (stable IDs: R1-1, R2-3, …).
2. **Provenance gate** — every factual statement maps to one of:
   `paper` | `review` | `user_confirmed_result` | `future_work`
   No source → do not put in the letter.
3. **Commitment gate** — every promise maps to:
   `already_done` | `approved` | `future_work_only`
   Not approved → blocked from final letter.
4. **Coverage gate** — every concern ends as:
   `answered` | `deferred` | `needs_user_input`
   Nothing silently disappears.
5. **No fabrication.** No invented numbers, citations, or unrun experiments.
6. **No auto new experiments.** Analysis gaps go to the user; only `user_confirmed_result` enters the letter.
7. **Optional `QUICK_MODE`** — issue board + strategy only (no full letter).
8. **Optional stress-test** — when `06_review/base/simulate-reviewers` is available, use it on the draft; never invent a Codex/MCP-only path as required.

## Default output shape (journal)

For each item:

```text
Reviewer #N
Comment #M
[quoted or paraphrased comment]

Response:
[what we did / why / evidence]

Manuscript change: [section / Track Changes location / Table X]
```

- Body edits: **Word Track Changes**.
- Response letter claims **must match** TC (same numbers, same locations).
- Map every item into the ledger in [response-audit-gate.md](response-audit-gate.md).

Conference venues (ICML / OpenReview character budgets, paste-ready plain text) are **optional overrides**, not the default path.

## Analysis requests — status triad

| Status | Meaning | Letter? |
|---|---|---|
| Existing result (已有结果) | User-confirmed existing result | Yes, with location |
| Needs new work (需补做) | Needs new analysis | Ask user; do not invent |
| Decline + reason (不采纳 + 理由) | Decline with scientific reason | Yes, with scope/limitation |

Only **user-confirmed** results enter the letter as done work.

## Workflow

1. Normalize reviews → atomize → issue board (IDs, severity, type).
2. Strategy: themes, response mode per issue, blockers → user.
3. If `QUICK_MODE`: stop after board + strategy.
4. Draft point-by-point letter + **revision checklist** (every promised edit is a checklist row; map to audit-gate ledger).
5. Run the three hard gates ([response-audit-gate.md](response-audit-gate.md)).
6. Optional: stress-test via simulate-reviewers.
7. Deliver **final letter + checklist** (not draft-only for items that already have commitment).
8. **Handoff:** after the letter changes numbers, run `06_review/base/self-review/references/paper-claim-audit.md` on the revised manuscript.

## Cut from upstream (not in this pack)

- `AUTO_EXPERIMENT` / GPU experiment-bridge
- render-html as required step
- Venue paste character counting as the **required** path
- Codex / Manual-Review MCP specifics as the only stress-test backend

## Key rules

- Evidence > rhetoric. Concede narrowly when the reviewer is right.
- Do not stop at “draft only” when commitment is already `already_done` / `approved` — finish letter + checklist.
- Tone / phrasing banks → `07_response/advanced/`.
