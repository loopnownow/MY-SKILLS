---
name: "stats-analysis"
domain: "02_data-processing"
trigger: ["选检验", "Mann-Whitney", "t-test", "Bayesian", "回归实现", "statsmodels"]
inputs: ["outcome_type", "n_groups", "paired_flag", "normality"]
outputs: ["named_test", "model_notes"]
tools: ["decision_tree"]
quality_control: "two independent groups + continuous non-normal -> Mann-Whitney U"
owner: "02_data-processing/base/stats-analysis/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Statistical test selection (plus Bayesian / assumption notes)

Contract only for stats-analysis: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/stats-analysis-digest.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Choose an appropriate test and check the assumptions that justify it. Absorbed former fine id `meta-analysis` (Bayesian notes + `assumption_checks.py`; alias in `00_orchestrator/legacy_aliases.yaml`). This pack does **not** teach sample-size/power (use `calc-sample-size`) or calibration / DCA / external validation (use `model-evaluation`).

Lab stats policy stays in `02_data-processing/advanced/analysis/`.

## When to use

- Which test matches the outcome, grouping, pairing, and normality?
- What to do when an assumption fails (Welch, non-parametric, transform)
- How to report the chosen test (APA-style templates in `references/reporting_standards.md`)
- Bayesian re-analysis, priors, credible intervals, or a reviewer Bayesian sensitivity check
- Running the in-pack assumption-check helper

## Open these files

| File | Open when |
|---|---|
| [references/test_selection_guide.md](references/test_selection_guide.md) | Choosing the test |
| [references/assumptions_and_diagnostics.md](references/assumptions_and_diagnostics.md) | Assumption violations and remedies |
| [references/reporting_standards.md](references/reporting_standards.md) | Result sentences |
| [references/bayesian_statistics.md](references/bayesian_statistics.md) | Bayesian re-analysis, priors, credible intervals, sensitivity |
| `{code_stats}\tools\stats-analysis\assumption_checks.py` | Programmatic normality / variance / outlier checks |

Power / effect-size planning - `../calc-sample-size/references/effect_sizes_and_power.md`.

## Quick reference

**Two groups**

- Independent, continuous, normal - Independent t-test
- Independent, continuous, non-normal - Mann-Whitney U
- Paired, continuous, normal - Paired t-test
- Paired, continuous, non-normal - Wilcoxon signed-rank
- Binary - Chi-square or Fisher exact

**3+ groups**

- Independent, continuous, normal - One-way ANOVA
- Independent, continuous, non-normal - Kruskal-Wallis
- Paired, continuous, normal - Repeated-measures ANOVA
- Paired, continuous, non-normal - Friedman

**Relationships**

- Two continuous - Pearson (normal) or Spearman
- Continuous outcome + predictors - Linear regression
- Binary outcome + predictors - Logistic regression

## Assumption rule

Always state which assumptions were checked and what was done if they failed. Mild normality
violations with n > 30 per group may still support a parametric test; otherwise use the
non-parametric alternative or Welch variants (`assumptions_and_diagnostics.md`).

The checker lives in `{code_stats}\tools\stats-analysis\`; this pack keeps the pointer `scripts/README.md` (moved 2026-11-01, t1521u P3-A).

Import the helper from `{code_stats}\tools\stats-analysis\assumption_checks.py` (module name `assumption_checks`); this pack keeps the pointer `scripts/README.md`.

## Handoffs

- n / power / Riley - `calc-sample-size`
- Calibration / DCA / external validation - `model-evaluation`
- Plots - `plot-figures`
