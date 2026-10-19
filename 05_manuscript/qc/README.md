# 05_manuscript / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** A05 first-pass and polish use `base/` and `personal/`; they do not self-certify lit or pre-submit via `qc/`.

QC **standards only** (pass/fail + fail→rollback station). Capability bodies stay in personal/base.

| File | Gate(s) |
|---|---|
| `manuscript-local-qc.md` | **G-05** — writing-seat scorecard + pre-submit check ids |
| `reporting-guideline-route.md` | **G-05** / **Integrity · pre-06** — TRIPOD/STARD/STROBE/PRISMA + JSON router |
| `reporting-guidelines-router.json` | **G-05** / Integrity · pre-06 — id→study_type→URL metadata only (MIT upstream) |
| `claim-number-align.md` | **G-05** / **G-FACT** — claim↔number/table/figure align |
| `anti-leak-placeholders.md` | **G-05** / Integrity · pre-06 — 批注-only gaps; no negation lists |
| `style-spotcheck.md` | **G-05** — Vancouver+DOI / Aitor-format spot (not APA-primary) |
| `figure-stats-legend.md` | **G-05** / Integrity · pre-06 — legend minima by plot type |
| `figure-qa-minima.md` | **G-05** — image-integrity + pre-submission figure pass/fail |

### Attribution (P0 absorb 2026-10-19)

- Yuan1z0825/nature-skills (`nature-statistics`, `nature-figure`) — Apache-2.0 — figure legend/QA minima
- K-Dense-AI/scientific-agent-skills (`peer-review` reporting_guidelines.json) — MIT — router metadata only
- See also root `NOTICE`
