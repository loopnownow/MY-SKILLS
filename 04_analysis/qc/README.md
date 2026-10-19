# 04_analysis / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** First-pass stats/figures stay in `base/` and `personal/` (pipeline, methods, figures).

| File | Gate(s) |
|---|---|
| `report-checks.md` | Report / stats consistency standards used with **G-FACT** / pre-submit classes |
| `html-results.md` | **G-04** — HTML results pass criteria extracted from `00_orchestrator/gates.md` |
| `ml-experiment-checklist.md` | ML ablation / baseline / seed minima (AutoResearchClaw distill; domain-gated) |
| `uncertainty-units-minima.md` | Units / ± meaning / plausibility soft-checks (K-Dense distill; no runtime) |
| `method-validation-gate.md` | Analytical method-validation pass/fail (domain-gated; default N/A for imaging-ML) |
