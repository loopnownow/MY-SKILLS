---
name: "meta-analysis"
domain: "02_data-processing"
trigger: ["Bayesian", "回归实现", "statsmodels"]
outputs: ["model_notes"]
owner: "02_data-processing/base/meta-analysis/MODULE.md"
---

# Statistical / ML implementation notes

Contract only for meta-analysis: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/methods.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Generic Bayesian notes and assumption-check script. Not the lab radiomics pipeline. sklearn/pymc implementations are Scientific backups, not this pack.

## On-demand references

| File | Open when |
|---|---|
| `references/bayesian_statistics.md` | Bayesian re-analysis, priors, credible intervals, or a reviewer asks for a Bayesian sensitivity check |
