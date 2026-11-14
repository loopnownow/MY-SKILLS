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

Contract only for stats-analysis: scope, bans, phase names, and pointers. The house working method and the revision authority live in `02_data-processing/advanced/analysis/stats-analysis-digest.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Choose an appropriate test and check the assumptions that justify it. Absorbed former fine id `meta-analysis` (Bayesian notes + `assumption_checks.py`; alias in `00_orchestrator/legacy_aliases.yaml`). This pack does **not** teach sample-size/power (use `calc-sample-size`) or calibration / DCA / external validation (use `model-evaluation`).

Lab stats policy stays in `02_data-processing/advanced/analysis/`.

Do not start formal tests until `ref/design-study.md` exists and `ref/design-lock.md` has been owner-accepted (see `03_research/base/design-study/` pre-stats lock). If the lock is missing or unaccepted, stop and return to `design-study`.

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

Choose by design first (outcome type, grouping, pairing, events per variable), then check assumptions; normality is an input, not the decision rule. Full decision guidance: `02_data-processing/base/stats-analysis/references/test_selection_guide.md`. Report the test, the assumption check, and the effect size.

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
