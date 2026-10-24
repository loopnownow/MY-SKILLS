# 06_review / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** A06 first-pass review engines stay in `base/`; post-QC re-review uses `personal/` under 00 gate authority.

QC **standards only** (pass/fail + fail→rollback station). Capability bodies stay in personal/base.

| File | Gate(s) |
|---|---|
| `cross-manuscript-qc.md` | **G-06** — sister-paper / statement-then-data consistency (annotate only) |
| `disclaimer-comment-only.md` | **G-06** / Integrity · pre-06 — disclaimer/CYA/未做-class → 批注 only + 建议修改后内容 (compose AL-5) |
| `editorial-decision-matrix.md` | **G-06** — Accept / Minor / Major / Reject (no hard score threshold) |
| `rr-re-review.md` | **G-06** / `P06r` — R&R verification enum → `00_orchestrator/templates/rr-traceability.md` |
| `stats-reporting-spotcheck.md` | **G-06** — short radiology/prediction stats spot list |
| `stats-failure-modes.md` | **G-06** / Integrity · pre-06 — P0/P1 taxonomy; compose with G-FACT |
| `forensic-consistency.md` | **G-06** / Integrity · pre-06 — arithmetic↔figure layers; HARD with G-FACT |
| `technical-concern-coverage.md` | **G-06** — 12-axis coverage router |
| `review-release-gates.md` | **G-06** — isolation / grounding / severity / release rule |
| `experiment-integrity-audit.md` | Integrity · pre-06 / G-FACT — Layer 1 eval honesty |
| `kill-argument-preflight.md` | **G-06** / pre-submit — Layer 5 strongest-rejection self-check |
| `assurance-audit-chain.md` | Index — 5 layers → paths → seats |
| `review-loop-state.md` | Internal QC / G-06 · review→fix→re-review + REVIEW_STATE resume |
| `appraisal-tool-route.md` | **G-06** — RoB/GRADE/QUADAS/PROBAST+AI **routing only** (when appraisal applies) |

Reporting-guideline **router** lives under 05: `05_manuscript/qc/reporting-guideline-route.md` + `reporting-guidelines-router.json` (Integrity · pre-06).

### Attribution (P0 absorb 2026-10-19)

- Yuan1z0825/nature-skills (`nature-statistics`, `nature-reviewer`) — Apache-2.0 — failure modes, forensic, coverage, release gates
- See also root `NOTICE`

### Attribution (P1 absorb 2026-10-19)

- K-Dense-AI/scientific-agent-skills (`scientific-critical-thinking`) — MIT — appraisal tool router only
- See also root `NOTICE`

### Attribution (ARIS P0 absorb 2026-10-19)

- wanshuiyin/Auto-claude-code-research-in-sleep — experiment-audit / kill-argument / assurance chain — lab rewrite
- Contract: `06_review/qc/assurance-verdicts.md`

### Attribution (ARIS P1 absorb 2026-10-19)

- wanshuiyin/Auto-claude-code-research-in-sleep — auto-review-loop / resumable-runs — lab rewrite; Lee seat + assurance-audit-chain
