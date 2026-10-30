---
name: "model-evaluation"
domain: "02_data-processing"
trigger: ["校准", "DCA", "外验证", "模型评价", "泄漏门禁", "leakage", "model-validation"]
outputs: ["eval_report"]
owner: "02_data-processing/base/model-evaluation/MODULE.md"
---

# Model evaluation (calibration / DCA / external validation + leakage gates)

Contract only for model-evaluation: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/model-evaluation-digest.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Umbrella fine id: **`model-evaluation`** (covers former `model-validation`).

Not test selection or Bayesian notes (`stats-analysis`). Model fitting recipes stay in `02_data-processing/advanced/analysis/`.
Lab pipeline / DeLong / Cox policy stays in `02_data-processing/advanced/analysis/`.

## Workflow

1. **Confirm the split is locked** — patient-level; test untouched during fitting.
2. **Deterministic leakage gates** (former model-validation) — refuse slice-level random split as external;
   confirm feature selection / tuning used train only; flag any test-set peeking before metrics.
3. **Discrimination** — AUC (or C-index) with 95% CI on each named set. Do not invent CIs.
4. **Calibration** — plot + slope/intercept or a named calibration metric when supplied.
5. **Clinical utility** — decision-curve analysis **only** if the paper claims decision support.
6. **External / temporal / geographic** validation when generalisability is claimed; otherwise bound the claim.
7. **Plots** — `plot-figures`. Reporting checklists — `check-reporting`.

Legacy alias: `model-validation` → `model-evaluation` (2026-10-17 round 3).
