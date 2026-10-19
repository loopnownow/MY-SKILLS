# 06_review / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** A06 first-pass review engines stay in `base/`; post-QC re-review uses `personal/` under 00 gate authority.

QC **standards only** (pass/fail + fail→rollback station). Capability bodies stay in personal/base.

| File | Gate(s) |
|---|---|
| `cross-manuscript-qc.md` | **G-06** — sister-paper / statement-then-data consistency (annotate only) |
| `editorial-decision-matrix.md` | **G-06** — Accept / Minor / Major / Reject (no hard score threshold) |
| `rr-re-review.md` | **G-06** / `P06r` — R&R verification enum → `00_orchestrator/templates/rr-traceability.md` |
| `stats-reporting-spotcheck.md` | **G-06** — short radiology/prediction stats spot list |
| `stats-failure-modes.md` | **G-06** / Integrity · pre-06 — P0/P1 taxonomy; compose with G-FACT |
| `forensic-consistency.md` | **G-06** / Integrity · pre-06 — arithmetic↔figure layers; HARD with G-FACT |
| `technical-concern-coverage.md` | **G-06** — 12-axis coverage router |
| `review-release-gates.md` | **G-06** — isolation / grounding / severity / release rule |

Reporting-guideline **router** lives under 05: `05_manuscript/qc/reporting-guideline-route.md` + `reporting-guidelines-router.json` (Integrity · pre-06).

### Attribution (P0 absorb 2026-10-19)

- Yuan1z0825/nature-skills (`nature-statistics`, `nature-reviewer`) — Apache-2.0 — failure modes, forensic, coverage, release gates
- See also root `NOTICE`
