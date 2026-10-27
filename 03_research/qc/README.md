# 03_research / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** Citation-verify **execution** stays in `03_research/advanced/citation-verify.md`; this folder only states what 00 checks.

| File | Gate(s) |
|---|---|
| `lit-verify-gate.md` | **G-LIT** (and G-05/G-06 lit sub-checks) — citation-verify was run; claim→ref table exists |
| `research-stage-artifacts.md` | W1→W3 stage map and per-stage artifact contract (00 calls at long research loops) |
| `grants-proposal-pack.md` | Grants / 开题 / proposal writing pack pointer (funding drafts only; not 05/06 paper QC) |

Do not move `03_research/advanced/citation-verify.md` into `qc/`.

Capability routers (not qc self-certify): `03_research/base/lit-pipeline-router.md`; DOI field audit under `03_research/base/verify-refs/references/doi-crossref-field-audit.md` (pairs `05_manuscript/qc/refs-verified.md`).
