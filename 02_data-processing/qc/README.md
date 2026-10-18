# 02_data-processing / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** First-pass and A02 re-loops use `base/` and `personal/`; they do not invoke `qc/` themselves.

| File | Gate(s) |
|---|---|
| `coding-qc.md` | **G-CODE** — deep code QC standards for release-ready processing scripts |
| `phi-exit.md` | **G-PHI** — thin checklist pointer to gates.md PHI pass criteria (no new policy) |

Capability packs that stay in `base/` (e.g. `base/imaging-qc`) are not QC standards and are not listed here.