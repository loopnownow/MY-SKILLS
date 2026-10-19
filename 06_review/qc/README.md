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
