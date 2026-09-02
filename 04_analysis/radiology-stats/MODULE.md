---
name: "radiology-stats"
domain: "04_analysis"
trigger: ["AUC", "DeLong", "DCA", "统计"]
inputs: ["design", "endpoint", "metrics"]
outputs: ["test_plan", "reporting_sentences"]
tools: ["Python", "modules.pipeline"]
quality_control: "estimate+95% CI; bootstrap AUC CI; no nested CV as lab default; no fabricated p/AUC"
owner: "04_analysis/radiology-stats/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Imaging Biostatistics for _Radiology_

Use this skill to choose the right test, run it correctly, and **report it the way
_Radiology_ wants** — estimates with 95% CIs, exact p-values, named tests, and multiplicity
handled. It covers the statistics that imaging-AI, radiomics, and reader studies live or die
on.

**Lab vs journal-grade.** 0RAD live modules are **v4.3.0** (2026-08-28). Primary run is
`python -m modules.pipeline`. Nested CV, multivariate Cox, lifelines, and DeLong *intervals*
are not lab defaults (say “not implemented” if asked). Full lock: `../personal/0rad-pipeline-rules.md`.

## Core stance

- **Estimate + uncertainty, not just p.** Every primary result gets a 95% CI. Report exact
  p-values (e.g. `P = .03`, not `P < .05`); use `P < .001` only below that floor.
- **The test must match the design.** Paired data → paired test (same patients/cases read by
  both methods); clustered data (multiple lesions per patient) → account for clustering;
  multiple readers → MRMC, not a naive average.
- **Discrimination is not enough for a clinical model.** Report **calibration** and
  **clinical utility (decision-curve)** alongside AUC. Lab primary model = **Combined**.
- **Control multiplicity honestly.** Thousands of radiomic/omic features ⇒ FDR or stronger;
  pre-specify primary vs exploratory.
- **No fishing, no fabrication.** Pre-specify the primary analysis; never invent a number,
  a CI, or a p-value. If data are insufficient, say what is needed.
- **Reproducible.** Return runnable code (Python first; R where it is the field standard)
  with the software/version and the exact method for CIs. Do not vendor `D:\0Grok\0RAD` Python.

## When to use

- Diagnostic accuracy: sensitivity/specificity/PPV/NPV/accuracy/likelihood ratios + CIs.
- Comparing models: lab **DeLong p** (paired, Sun & Xu 2014 midranks; `DeLong vs {model}` in
  `ROC_METRICS`). AUC **95% CI is 1000 bootstrap** (`_boot_auc_ci`), not a DeLong interval.
  McNemar for paired sensitivity/specificity. Reader studies → **MRMC**, not plain DeLong.
- Reader studies: **kappa / weighted kappa / Fleiss / ICC / Bland-Altman**; **MRMC** design
  and analysis. Lab radiomics filter: **ICC(A,1) ≥ 0.75**.
- Prediction models: ROC, **calibration**, **DCA**, Youden **per split** unless
  `lock_threshold`. `VAL_MODE` = `refit` | `apply_formula` | `lock_threshold`.
- Radiomics/omics: ICC(A,1) ≥ 0.75, then **train-only** LASSO (StratifiedKFold AUC path).
  Nested CV is **not implemented**. Habitat-tree `LassoCV` ≠ paper primary.
- Survival/prognosis: Kaplan-Meier + log-rank. Optional univariable Cox (`statsmodels` PHReg,
  Breslow; `DO_COX` default **False**). Not multivariate; not lifelines. C-index /
  time-dependent ROC / competing risks are journal-grade, not lab defaults.
- Planning: **sample size** for accuracy / AUC; **EPV** and **Riley** minimum sample size
  for prediction models.
- Clinical selection: Table 1 + **AIC backward**.

## When to open extra files

| File | Open when |
|---|---|
| [references/diagnostic-accuracy.md](references/diagnostic-accuracy.md) | Sensitivity/specificity/PPV/NPV/LR, the right CI method, paired comparison (McNemar) |
| [references/model-evaluation.md](references/model-evaluation.md) | ROC/AUC, bootstrap CI vs DeLong p, thresholds, calibration, Brier, decision-curve analysis |
| [../personal/0rad-pipeline-rules.md](../personal/0rad-pipeline-rules.md) | 0RAD `VAL_MODE` / live modules v4.3.0 / pairwise groups / ID columns |
| [references/agreement-mrmc.md](references/agreement-mrmc.md) | Cohen/weighted/Fleiss kappa, ICC(A,1) lab filter, Bland-Altman, MRMC (Obuchowski-Rockette / DBM) |
| [references/high-dimensional-omics.md](references/high-dimensional-omics.md) | Multiple testing, train-only LASSO (not nested CV), leakage, ICC filter |
| [references/survival-prognostic.md](references/survival-prognostic.md) | Kaplan-Meier, optional univariable Cox (PHReg), Schoenfeld; what is not implemented |
| [references/sample-size.md](references/sample-size.md) | Sample-size for sensitivity/specificity/AUC; EPV; Riley minimum sample size for prediction models |

## Workflow

1. **Restate the design** — unit of analysis (patient/lesion/slice), paired vs unpaired,
   number of readers, prevalence, primary vs secondary endpoints.
2. **Pick the estimand and test** using the reference files. Name it explicitly.
3. **Choose the CI method** (Wilson/Clopper-Pearson for proportions; **1000 bootstrap** for
   lab AUC via `_boot_auc_ci` — not DeLong intervals).
4. **Handle multiplicity** — declare the primary analysis; correct the rest (method + family).
5. **Run it** — lab numbers from `python -m modules.pipeline`. Do not treat habitat-tree
   `LassoCV` as the paper primary.
6. **Write the result** — a _Radiology_-style sentence (estimate, CI, p, n) plus a Methods
   sentence (test, software/version, CI method, multiplicity).
7. **Sanity-check** — does the CI width match n? is the test paired if the data are? is
   calibration reported for a clinical model? are subgroups pre-specified? did you claim
   nested CV or DeLong CI by mistake?

## Reporting templates (fill from real output — never fabricate)

- Accuracy: *"Sensitivity was 0.87 (95% CI: 0.81, 0.92; 130/149) and specificity 0.79 (95%
  CI: 0.72, 0.85; 158/200)."*
- AUC comparison: *"The Combined model AUC (0.88; 95% CI: 0.84, 0.92; 1000 bootstrap)
  exceeded the clinical model (0.81; 95% CI: 0.76, 0.86; P = .004, DeLong)."*
- Agreement: *"Features with ICC(A,1) < 0.75 were excluded. Inter-reader agreement was
  substantial (ICC, 0.82; 95% CI: 0.75, 0.87; two-way mixed, absolute agreement, single
  rater)."*
- Multiplicity: *"Of 1218 features, 47 differed after Benjamini-Hochberg control at FDR <
  0.05."*

## Output contract

1. **`Design read`** — unit, pairing, readers, prevalence, endpoints.
2. **`Recommended analysis`** — estimand, test, CI method, multiplicity plan. Label lab vs
   not-implemented (nested CV, multivariate Cox).
3. **`Code`** — point to `python -m modules.pipeline` for lab runs; do not vendor 0RAD Python.
4. **`Results sentence`** — _Radiology_-style, with placeholders only where the user must
   supply data.
5. **`Methods sentence`** — for the statistical-analysis paragraph.
6. **`Caveats`** — assumptions, when the test breaks, what the reviewer may ask.

## Integrity & handoffs

- Never invent numbers, CIs, or p-values; compute from supplied data or mark as needed.
- Reporting-guideline alignment of the statistics → `radiology-reporting`.
- Plotting the result (ROC, calibration, DCA, forest, KM) → mounted `04-figure-engine`.
- High-dimensional study design (leakage, batch effects in radiogenomics) →
  `radiology-radiogenomics`.
- Sample-size numbers feeding a grant's feasibility section → `radiology-grant`.
- Analysis plan is locked and results are in; want a harsh pre-submission read → `radiology-prereview`.
- This skill is statistical guidance, not a substitute for a qualified biostatistician on
  high-stakes or regulatory work.
