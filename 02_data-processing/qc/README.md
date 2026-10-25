# 02_data-processing / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** First-pass and 02 re-loops use `base/` and `personal/`; they do not invoke `qc/` themselves.
First-pass stats/figures stay in `base/` and `personal/analysis/` (pipeline, methods, figures).

| File | Gate(s) |
|---|---|
| `coding-qc.md` | **G-CODE** — deep code QC standards for release-ready processing scripts |
| `phi-exit.md` | **G-PHI** — thin checklist pointer to gates.md PHI pass criteria (no new policy) |
| `experiment-log-minima.md` | Experiment/acquisition log hygiene (no guess; ID + raw locus; no Feishu runtime) |
| `report-checks.md` | Report / stats consistency standards used with **G-FACT** / pre-submit classes |
| `html-results.md` | **G-STATS** — HTML results pass criteria extracted from `00_orchestrator/gates.md` |
| `ml-experiment-checklist.md` | ML ablation / baseline / seed minima (AutoResearchClaw distill; domain-gated) |
| `uncertainty-units-minima.md` | Units / ± meaning / plausibility soft-checks (K-Dense distill; no runtime) |
| `method-validation-gate.md` | Analytical method-validation pass/fail (domain-gated; default `NOT_APPLICABLE` for imaging-ML) |

Capability packs that stay in `base/` (e.g. `base/preprocess-imaging`) are not QC standards and are not listed here.
