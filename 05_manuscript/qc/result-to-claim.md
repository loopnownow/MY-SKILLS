# Result → claim gate (05 qc · Layer 2)

**Owner:** `00_orchestrator` (composes **G-FACT** / Integrity · pre-06).
**Seat:** Aitee (05) drafts claim language; **independent reviewer** judges support. Loopnow (04) if more experiments needed. Victor (03) if claim needs lit framing.
**Distill of:** ARIS `result-to-claim` + `evidence-precheck.md`.
**Link, don’t duplicate:** number alignment → `claim-number-align.md`; forensic arithmetic → `06_review/qc/forensic-consistency.md`.

## Purpose

Does the **scientific claim** follow from the reported result (scope, direction, strength)? Distinct from “did we type the number correctly” (Layer 3).

## When

- After Layer 1 (or when `EXPERIMENT_AUDIT` `NOT_APPLICABLE`) and primary numbers exist.
- Before freezing abstract/Conclusions for Lee / submit.
- Mandatory emit at `assurance: submission` / `conference-ready`.

## Inputs

- Intended claims list (id, text, cited value, source path)
- Primary results (`*-results.html`, tables)
- Optional: `EXPERIMENT_AUDIT.json` (integrity_status)
- Deterministic pre-check: value exists in source file before any merit judgment

## Checklist

| id | Check | Notes |
|---|---|---|
| RC-1 | Evidence **exists** (path + value found) | Fail closed → `claim_supported: no` / integrity `evidence_not_found` |
| RC-2 | `claim_supported`: yes / partial / no | Independent judge; executor does not round up |
| RC-3 | What data supports vs does not | Record gaps |
| RC-4 | Suggested claim revision if overstated | Scope / hedge / reframe |
| RC-5 | Attach Layer-1 integrity_status | fail → confidence low; tag `[INTEGRITY CONCERN]` |
| RC-6 | Single-dataset / pilot ≠ general claim | Partial or no |

## Pass / fail

- **PASS:** All load-bearing claims `yes` (or `partial` with revised wording already applied); integrity ≠ fail.
- **WARN:** Partial with disclosed gaps; integrity warn.
- **FAIL:** Load-bearing claim `no`, or integrity fail with claim still strong-worded.
- **BLOCKED:** Claims cite numbers but sources missing (after pre-check).
- **NOT_APPLICABLE:** No empirical claims (methods/editorial only).
- **ERROR:** Judge unavailable — do **not** substitute executor yes.

## Fail → rollback

| Verdict | Rollback |
|---|---|
| FAIL | 05 weaken/delete claim (Aitee) and/or 04 more evidence (Loopnow) |
| BLOCKED | Supply results files or drop claim |
| ERROR | `verdict: REVIEW_UNAVAILABLE`; stop Type-B; escalate |

## Verdict artifact

- `RESULT_TO_CLAIM.json` (+ optional `CLAIMS_FROM_RESULTS.md`)
- Per-claim: `id`, `claim_supported`, `confidence`, `integrity_status`, `missing_evidence`
- Overall `verdict` uses six-state schema in `06_review/qc/assurance-verdicts.md`

*Attribution: ARIS result-to-claim / evidence-precheck (wanshuiyin/Auto-claude-code-research-in-sleep).*
