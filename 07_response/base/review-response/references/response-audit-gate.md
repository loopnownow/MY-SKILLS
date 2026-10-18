# Reviewer response audit gate

Use this reference after drafting a point-by-point response, before sending the revision to the journal, or when reviewer comments are numerous, conflicting, or analysis-heavy.

## Three hard gates (must all pass before final)

If any gate fails, do **not** call the letter final.

### 1. Provenance gate

Every factual statement in the letter maps to one of:

| Source tag | Allowed content |
|---|---|
| `paper` | Already in the (revised) manuscript / tables / figures |
| `review` | Quoting or characterizing the reviewer's own text |
| `user_confirmed_result` | Analysis/result the user explicitly confirmed |
| `future_work` | Explicitly framed as future work, not as done |

No source = blocked. No fabrication.

### 2. Commitment gate

Every promise maps to one of:

| Tag | Meaning |
|---|---|
| `already_done` | Change is in the manuscript (Track Changes / location known) |
| `approved` | User approved this commitment for this round |
| `future_work_only` | Deferred; must not read as completed |

Not approved = blocked. Every paper-edit promise must appear on the revision checklist (and vice versa — no orphan checklist rows).

### 3. Coverage gate

Every atomized concern ends as one of:

| Status | Meaning |
|---|---|
| `answered` | Response + location/evidence present |
| `deferred` | Explicit deferral with reason |
| `needs_user_input` | Blocked on author data/decision |

Nothing silently disappears.

## Response ledger

Every reviewer/editor comment receives a row:

| ID | Comment summary | Category | Action | Manuscript location | Evidence artifact | Provenance | Commitment | Coverage | Status |
|---|---|---|---|---|---|---|---|---|---|
| R1-1 | External validation concern | validation | SOFTEN_CLAIM / ADD_ANALYSIS | Abstract, Discussion | new Table S2 | user_confirmed_result | approved | answered | resolved / pending |
| R2-3 | Calibration requested | statistics/figure | ADD_RESULT | Results, Fig 3 | calibration script/output | needs_user_input | — | needs_user_input | pending author input |

Status options:

- `RESOLVED`: action is completed and location is known.
- `PARTIAL`: action is partly completed; limitation is disclosed.
- `PENDING_AUTHOR_INPUT`: cannot answer without author data/decision.
- `SCIENTIFIC_DISAGREEMENT`: respectful disagreement with evidence and scope reasoning.
- `NOT_FEASIBLE`: request cannot be done; reason and mitigation are explicit.

## Factuality lock

Before finalizing each response, verify:

- The claimed analysis/experiment was actually performed (or tagged future_work).
- Reported numbers match the revised manuscript, tables, and figures.
- Page/line/figure/table locations exist or are marked as placeholders.
- Added citations are verified.
- No response says "we revised accordingly" without describing what changed.
- A limitation is not presented as solved unless it truly is solved.
- Letter claims match Word Track Changes.

After number-changing revisions: hand off to `06_review/base/review-critique/paper-claim-audit.md`.

## Tone rules

- Start with appreciation only when it is natural; do not over-apologize.
- State the action first, then the evidence/location.
- If disagreeing, acknowledge the concern, define the scope, and cite data/guidance.
- Do not make reviewer-facing promises that the manuscript does not fulfill.
- Personal phrasing → A personal (not this pack).

## Conflict handling

When reviewers ask for incompatible changes:

| Conflict | Resolution |
|---|---|
| One reviewer asks to shorten; another asks for detail | Put key text in manuscript, full detail in supplement |
| One asks for stronger claim; another flags overclaim | Keep bounded claim and explain evidence boundary |
| New analysis requested but data unavailable | Explain infeasibility, add limitation, provide sensitivity/negative control if possible |

## Final audit output

| Audit item | Pass? | Notes |
|---|---|---|
| Provenance gate | yes/no | ... |
| Commitment gate | yes/no | ... |
| Coverage gate | yes/no | ... |
| Every comment has a stable ID | yes/no | ... |
| Every response has action + location | yes/no | ... |
| All claimed new analyses verified | yes/no | ... |
| Numbers match revised manuscript | yes/no | ... |
| Unresolved items are explicit | yes/no | ... |
| Tone is cooperative and evidence-forward | yes/no | ... |

If any audit item fails, return the response letter with a fix list rather than calling it final.
