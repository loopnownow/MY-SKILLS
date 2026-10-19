# Paper claim audit gate (05 qc · Layer 3)

**Owner:** `00_orchestrator` at G-05 / G-FACT / Integrity · pre-06.
**Seat:** Independent cold-reader (prefer Lee session or fresh thread). Aitee (05) repairs prose; Loopnow (04) if evidence wrong.
**Capability body:** `06_review/base/review-critique/references/paper-claim-audit.md` (medical/Word workflow).
**Also compose:** `claim-number-align.md` (CN-1…4). Do **not** re-copy forensic layers — link `06_review/qc/forensic-consistency.md`.

## Purpose

Does the manuscript **report** numbers/comparisons/scope **truthfully** at display precision? (Not “is the science strong” — that is Layer 2.)

## When

- After house.docx / frozen tables; before Lee pre-review when numbers cited.
- Re-run if numbers edited after a prior PASS.
- Mandatory emit at `assurance: submission` / `conference-ready`.

## Inputs (zero-context)

- Manuscript only (docx→md with recorded track-changes view) + primary evidence globs
- **Exclude:** chat, narrative reports, prior audit “expected” answers, executor summaries

## Checklist (gate layer)

| id | Check | Status vocabulary |
|---|---|---|
| PC-1 | Every quantitative / scope claim extracted | location + quote + value |
| PC-2 | Trace to primary file | exact_match / rounding_ok / mismatch / missing_evidence / … |
| PC-3 | Medical failure modes from capability body | inflation, cherry-pick, split mismatch, N staircase, arithmetic, caption, scope |
| PC-4 | Same number across abstract / body / tables | compose CN-* |
| PC-5 | Artifact always written | even if no numeric claims → `NOT_APPLICABLE` |

## Pass / fail

| Input state | Verdict | reason_code example |
|---|---|---|
| No numeric claims | `NOT_APPLICABLE` | `no_numeric_claims` |
| Claims but no primary evidence | `BLOCKED` | `no_raw_evidence` |
| All reconcile | `PASS` | `all_numbers_match` |
| Display-precision drift only | `WARN` | `rounding_drift` |
| Material mismatch / cherry-pick / scope overclaim | `FAIL` | `claim_mismatch` |
| Reviewer/tool failed | `ERROR` | `reviewer_error` |

## Fail → rollback

- FAIL/BLOCKED → G-FACT HARD; 04/05 local rework; do not enter 06 as clean.
- WARN → comment + fix before submit if assurance ≥ conference-ready.
- ERROR → re-run; never invent PASS.

## Verdict artifact

- `PAPER_CLAIM_AUDIT.json` (+ `.md`)
- Schema: `00_orchestrator/qc/assurance-verdicts.md`
- Full medical checklist stays in the capability file above — this gate only adds six-state emit + wiring.

*Attribution: ARIS paper-claim-audit (wanshuiyin/Auto-claude-code-research-in-sleep) + lab medical adaptation already in base.*
