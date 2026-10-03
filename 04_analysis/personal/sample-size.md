# Sample size & power for imaging studies

Pre-specify and **justify** sample size (CLAIM, TRIPOD+AI, STARD all ask). Below are the
common cases. A retrospective cohort whose N is already fixed still uses one of the four
approaches in the next section. It does not get an observed-power number.

## Retrospective study with a fixed N

Do not compute post-hoc power, or observed power, from the p value already obtained.
That number restates the p value. BMJ/JAMA-style statistical review rejects it. In a
response letter the anchor is Hoenig & Heisey 2001. Do not add other citations for this point.

Use one of these four. Methods names which one. Do not add a fill-in manuscript sentence
that invents n, an effect size, or a power.

1. **Pre-study power.** Take the effect size from the literature or a pilot, then show
   that the enrolled N meets it. Alpha 0.05, two-sided; power 0.80 or 0.90. Tools:
   G*Power, PASS, or R `pwr` (`pwr.t.test`, `pwr.2p.test`).
2. **Events, not a two-group formula.** Multivariable logistic or Cox, radiomics, and
   prediction models use events-per-variable **10–15**, and Riley / R `pmsampsize` when
   the journal expects a minimum sample size. A classical two-group formula does not
   cover these.
3. **Minimum detectable effect (N already fixed).** Report the MDES at 80% power and
   set it next to a clinical difference. Do not call that observed power. Same tools as
   (1), with the enrolled n supplied and the effect size solved for.
4. **Precision.** When the aim is an estimate rather than a test, size N from the CI
   half-width. The sensitivity formula below is this case.

A **10–20%** drop-out allowance is only a planned exclusion (some enrolled cases will
not enter the analysis). It is not a new gate, and it is not added after the fact to a
retrospective cohort whose N is already the analysis N.

## Reviewer response

If asked for post-hoc power, refuse it. Offer the CI width, or the MDES at 80% power
against a clinical difference. Small N goes in Limitations as a possible type II error,
not as a calculated observed power.

## Diagnostic accuracy (sensitivity/specificity)
Sensitivity is estimated only in **diseased** patients, specificity in **non-diseased** — so
prevalence drives how many *total* patients you need. The half-width formula is approach 4.
Powering a hypothesis (sensitivity ≥ a target) is approach 1, or approach 3 when N is
already fixed.

- To estimate a sensitivity `Se` with half-width `w` at 95%:
  `n_diseased ≈ 1.96² · Se(1−Se) / w²`, then `n_total ≈ n_diseased / prevalence`.
- Tools: R `presize`, `MKpower`, `pwr`.

```python
import math
def n_for_sensitivity(se=0.90, half_width=0.05, prevalence=0.15, z=1.96):
    n_dis = (z**2 * se*(1-se)) / half_width**2
    return math.ceil(n_dis), math.ceil(n_dis / prevalence)
# e.g. Se 0.90, ±0.05, prev 0.15 -> diseased and total n
```

## AUC
Power to detect an AUC vs 0.5, or a difference between two AUCs (Hanley-McNeil / Obuchowski).
Inputs: expected AUCs, correlation (paired), allocation, prevalence. R `pROC::power.roc.test`,
`MCPmod`, or Obuchowski formulas. That is approach 1. With N already fixed, report the
MDES on the AUC difference (approach 3). Do not report observed power.

## Prediction models — EPV and Riley
Approach 2. Rule of thumb: **events-per-variable (EPV) 10–15** (development) — still crude.
- Use **Riley et al. minimum sample size** for prediction models when the journal expects
  it: targets small optimism, precise overall risk, and a calibration-slope ~1. R
  **`pmsampsize`** (dev) and **`pmvalidsize`** (validation). For **external validation**,
  target enough **events** (often ≥ 100 events and ≥ 100 non-events) for stable calibration.
- Do not substitute a classical two-group formula.

```r
library(pmsampsize)
pmsampsize(type="b", cstatistic=0.80, prevalence=0.2, parameters=20)
```

## MRMC reader studies
Power depends on **#readers × #cases**, the AUC difference, and variance components
(between-reader, within-reader). Use **OR/DBM** power tools: R `RJafroc::SsPowerGivenJK` or
FDA **iMRMC**. Pilot variance estimates make this far more reliable. Same split as above:
pre-study power (approach 1) or, if the reader×case grid is already fixed, the MDES
(approach 3). Not observed power.

## High-dimensional radiomics/omics
No single n powers thousands of features. Pre-specify the **primary** comparison and power
that (approach 1 or 3); size a prediction model with approach 2. Treat the feature scan as
FDR-controlled discovery; plan an **independent validation** cohort rather than relying on
one small cohort.

## Methods wording
Name which of the four approaches was used, the inputs that are real (literature or pilot
effect, alpha, target power, event count, or the CI half-width / MDES), and whether the
enrolled N met that target. Numbers come from that calculation or from the enrolled
cohort. Do not invent them.

## Reviewer hot-spots
No sample-size justification; EPV below 10; post-hoc / observed power from the obtained p;
a two-group formula on a prediction model; an MDES written up as observed power; a 10–20%
drop-out tacked on after N is fixed; reader study with too few readers; test / validation
set with too few events for calibration.
