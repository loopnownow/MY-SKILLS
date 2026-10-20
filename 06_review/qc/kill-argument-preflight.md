# Kill-argument preflight (06 qc · Layer 5)

**Owner:** `00_orchestrator` at G-06 / pre-submit when assurance ≥ conference-ready.
**Seat:** Lee (06) runs adversarial preflight; Aitee (05) applies Track Changes after user decision. Not a substitute for external peer review.
**Distill of:** ARIS `kill-argument`. Host-agnostic: two fresh independent reads (attack → adjudicate); no MCP binding.
**Do not duplicate:** balanced weakness lists live in `self-review` / `simulate-reviewers`; this is the **single strongest rejection** self-check.

## Purpose

Write the strongest ~200-word rejection memo, then adjudicate point-by-point against **current** manuscript text. Surface still-unresolved critical attacks before Lee packet / Bai submit.

## When

- After 1+ internal review rounds when headline is stable.
- Before external review or portal submit at `assurance: submission` / `conference-ready`.
- Skip early drafts with unstable title/abstract → `NOT_APPLICABLE` (`headline_unstable`).

## Inputs

- Current manuscript (+ optional compiled PDF)
- **Exclude:** prior review scores, fix lists, executor “we already fixed X” summaries

## Protocol (short)

1. **Attack (fresh):** one coherent rejection paragraph (~200 words), commit to the most damaging line (scope, methods, claim–evidence, assumptions).
2. **Adjudicate (fresh, independent):** decompose into 3–7 points; each → `answered_by_current_text` | `partially_answered` | `still_unresolved` + severity.
3. **Skill maps** counts → six-state verdict (adjudicator does not self-grade overall).

## Clinical / radiology axes (pick most damaging)

- Design / reference-standard / leakage
- Overclaim vs single-center / retrospective evidence
- Stats reporting / multiple testing / calibration gaps (compose `stats-failure-modes.md` — do not re-list)
- Claim vs table/figure evidence gap
- Title/abstract broader than body

## Pass / fail

| Verdict | Trigger |
|---|---|
| `FAIL` | ≥1 `still_unresolved` at **critical** |
| `WARN` | unresolved major/minor, or partial at critical/major with no unresolved |
| `PASS` | no unresolved; at most minor partials |
| `NOT_APPLICABLE` | no scope/generality claims and no quantitative headline to attack; or headline unstable |
| `BLOCKED` | manuscript source missing / unreadable |
| `ERROR` | attack or adjudication failed to produce parseable points |

## Fail → rollback

- FAIL/WARN critical → Lee comments + Aitee TC after user decision; do not mark submission-ready.
- Detect-only by default — no auto-edit of manuscript.
- Compose `review-release-gates.md` before releasing packet as clean.

## Verdict artifact

- `KILL_ARGUMENT.json` (+ `.md`)
- `details`: attack_memo, decomposed_points[], counts, top_action_items (max 3)

*Attribution: ARIS kill-argument (wanshuiyin/Auto-claude-code-research-in-sleep). Lab seat mapping + clinical axes added.*
