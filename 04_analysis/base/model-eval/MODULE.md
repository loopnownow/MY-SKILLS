---
name: "model-eval"
domain: "04_analysis"
trigger: ["校准", "DCA", "外验证", "模型评价", "泄漏门禁", "leakage", "model-validation"]
outputs: ["eval_report"]
owner: "04-analysis/model-eval/MODULE.md"
---

# Model evaluation (calibration / DCA / external validation + leakage gates)

Umbrella fine id: **`model-evaluation`** (covers former `model-validation`).

Not test selection (`04-stats-guide`) and not model fitting (`04-stats-models`).
Lab 0RAD / DeLong / Cox policy stays in A `04_analysis/personal/`.

## Workflow

1. **Confirm the split is locked** — patient-level; test untouched during fitting.
2. **Deterministic leakage gates** (former model-validation) — refuse slice-level random split as external;
   confirm feature selection / tuning used train only; flag any test-set peeking before metrics.
3. **Discrimination** — AUC (or C-index) with 95% CI on each named set. Do not invent CIs.
4. **Calibration** — plot + slope/intercept or a named calibration metric when supplied.
5. **Clinical utility** — decision-curve analysis **only** if the paper claims decision support.
6. **External / temporal / geographic** validation when generalisability is claimed; otherwise bound the claim.
7. **Plots** — `04-fig-plot`. Reporting checklists — `05-write-reporting`.

Legacy alias: `model-validation` → `model-evaluation` (2026-10-17 round 3).
