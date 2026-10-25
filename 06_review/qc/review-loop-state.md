# Review loop state (review → fix → re-review · standards only)

**Owner:** `00_orchestrator` at **G-06** / internal QC loops / Integrity · pre-06 when a multi-round review loop runs.
**Seat:** Lee (06) owns marks & loop ledger; Aitee (05) Track Changes; Loopnow (02) data/stats repairs; Victor (03) cites. Lee does **not** draft response letters (→ **07**).
**Distill of:** ARIS `auto-review-loop` state + `resumable-runs` (host-agnostic). **No** Codex/MCP/runtime install.
**Compose:** `assurance-audit-chain.md` · `rr-re-review.md` · `review-release-gates.md` · `06_review/qc/assurance-verdicts.md`.

## Loop shape

```
init / resume → Phase A Review → Phase B Parse → (stop?) → Phase C Fix → Phase D Results → Phase E Document → next round
```

| Phase | Lab action | Seat |
|---|---|---|
| A Review | Independent / dual-isolated review artifacts | Lee (+ live engines) |
| B Parse | Score / verdict / MUST-FIX list; no silent drop | Lee |
| C Fix | Implement only agreed fixes | Aitee (prose) / Loopnow (stats) / Victor (cites) |
| D Results | Re-read HTML / claims after fix | Loopnow / Aitee |
| E Document | Append round ledger; refresh state file | Lee / 00 |

Stop when policy-approved positive assessment **or** `MAX_ROUNDS` (lab default: re-review cap **2** then escalate like `defects[].rounds`). External R&R verification stays `rr-re-review.md` (frozen Round-1 ids).

## Resumable `REVIEW_STATE` (minimal fields)

Persist after each round (overwrite latest; keep `run_id` stable). Path suggestion: project `review-stage/REVIEW_STATE.json` (or equivalent under lab project root).

| Field | Required | Notes |
|---|---|---|
| `run_id` | yes | Stable for the whole loop |
| `round` | yes | Integer; resume at `round + 1` when `in_progress` |
| `status` | yes | `in_progress` \| `completed` \| `failed` |
| `last_verdict` / `last_score` | yes | Opaque to 00; must be recorded |
| `pending_experiments` | if any | Open Loopnow work |
| `timestamp` | yes | ISO-8601; stale >24h → treat as fresh start unless user overrides |
| `assurance` | recommended | `draft` \| `polished` \| `conference-ready` \| `submission` |

Host-specific reviewer backend / MCP thread ids are **optional** and must not lock the lab to one vendor. Independence still required for Type-B ACCEPT (`assurance-verdicts.md`).

**Resume rule:** if `status=in_progress` and timestamp fresh → continue next round; if `completed` → do not accidentally resume. Executor may mark round work `done`; only independent / deterministic path may `accepted`-acquit a quality gate.

## Pass / fail

| State | When |
|---|---|
| `PASS` | Loop completed with documented rounds; mandatory assurance layers emitted (no silent skip at submission) |
| `WARN` | Soft issues remain; disclosed in ledger |
| `FAIL` | Open MUST-FIX / Layer FAIL unresolved at stop |
| `BLOCKED` | Review inputs missing; cannot start Phase A |
| `ERROR` | Loop crashed mid-round without durable state |

## Fail → rollback

- FAIL / open MUST-FIX → responsible repair seat (table above); Lee re-marks; do not invent numbers.
- BLOCKED → fix paths / fine ids; re-enter G-06.
- Cap internal re-review loops at **2**, then escalate to user (same spirit as `rr-re-review.md`).

## Link, don’t duplicate

- 5-layer audits → `assurance-audit-chain.md`
- Isolation / release → `review-release-gates.md`
- External R&R verify enum → `rr-re-review.md`
- Stage map W1→W3 → `03_research/qc/research-stage-artifacts.md`

*Attribution: ARIS auto-review-loop + resumable-runs; lab G-06 / Lee seat remain authoritative.*
