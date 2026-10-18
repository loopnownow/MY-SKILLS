---
name: "stats-guide"
domain: "04_analysis"
trigger: ["选检验", "Mann-Whitney", "t-test"]
inputs: ["outcome_type", "n_groups", "paired_flag", "normality"]
outputs: ["named_test"]
tools: ["decision_tree"]
quality_control: "two independent groups + continuous non-normal -> Mann-Whitney U"
owner: "04-analysis/stats-guide/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Statistical test selection

Choose an appropriate test and check the assumptions that justify it. This pack does **not**
teach sample-size/power (→ `04-stats-power`), Bayesian/model implementation (→ `04-stats-models`),
or the `assumption_checks.py` script (that file lives in `04-stats-models`).

Lab stats policy stays in A personal.

## When to use

- Which test matches the outcome, grouping, pairing, and normality?
- What to do when an assumption fails (Welch, non-parametric, transform)
- How to report the chosen test (APA-style templates in `references/reporting_standards.md`)

## Open these files

| File | Open when |
|---|---|
| [references/test_selection_guide.md](references/test_selection_guide.md) | Choosing the test |
| [references/assumptions_and_diagnostics.md](references/assumptions_and_diagnostics.md) | Assumption violations and remedies |
| [references/reporting_standards.md](references/reporting_standards.md) | Result sentences |

Power / effect-size planning → `../stats-power/references/effect_sizes_and_power.md`.
Bayesian notes and the assumption script → `../stats-models/`.

## Quick reference

**Two groups**

- Independent, continuous, normal → Independent t-test
- Independent, continuous, non-normal → Mann-Whitney U
- Paired, continuous, normal → Paired t-test
- Paired, continuous, non-normal → Wilcoxon signed-rank
- Binary → Chi-square or Fisher exact

**3+ groups**

- Independent, continuous, normal → One-way ANOVA
- Independent, continuous, non-normal → Kruskal-Wallis
- Paired, continuous, normal → Repeated-measures ANOVA
- Paired, continuous, non-normal → Friedman

**Relationships**

- Two continuous → Pearson (normal) or Spearman
- Continuous outcome + predictors → Linear regression
- Binary outcome + predictors → Logistic regression

## Assumption rule

Always state which assumptions were checked and what was done if they failed. Mild normality
violations with n > 30 per group may still support a parametric test; otherwise use the
non-parametric alternative or Welch variants (`assumptions_and_diagnostics.md`).

Do **not** import `scripts.assumption_checks` from this pack — that module is under
`04-stats-models/scripts/`.

## Handoffs

- n / power / Riley → `04-stats-power`
- Bayesian / regression implementation → `04-stats-models`
- Calibration / DCA / external validation → `04-model-eval`
- Plots → `04-fig-plot`
