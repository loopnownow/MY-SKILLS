# Clinical + Radiomics ML Pipeline (R → Python ports and beyond)

## Separator (read this first)

| Job | Where |
|---|---|
| Habitat / delta **in-pipeline** selection | `radiomics.select_features` — sklearn **LassoCV only** (`selection-modelling.md`) |
| Paper LASSO, nomogram, ROC/DCA/calibration, NRI, ICC, `VAL_MODE` | **`python -m modules.pipeline`** (modules under the 0RAD clinical stack) |

Do **not** promote `delta_habitat_pipeline/utility/LASSO.py` (or habitat-tree copies of it) as
the stats library. Do not import that utility when the user asks for a paper nomogram / locked
formula / HTML report.

ICC lives in **`modules/utils/u_icc.py`**, not in the habitat trees (`leakage-audit.md`).

## Reference module set

A 14-script R pipeline has been ported to Python under this skill's conventions. Use this as the
canonical module list when building or extending a clinical+radiomics prediction pipeline — either
in Python from scratch, or when porting from R. Orchestrate with `python -m modules.pipeline`:

| Module | Purpose |
|---|---|
| `0_config.py` | Centralized soft-coded config: file paths, variable/column names, train/test split, model hyperparameters, random seed, plotting style |
| `clin_select.py` | Clinical variable selection |
| `correlation.py` | Correlation analysis between features |
| `u_outlier_detection.py` | Outlier detection |
| `u_impute.py` | Missing-value imputation |
| `u_icc.py` | Inter/intra-class correlation for radiomics feature reproducibility |
| `radiomics.py` | Radiomics feature handling (paper LASSO-based selection etc.) |
| `false_class.py` | Misclassification analysis |
| `curves_roc.py` | ROC curve generation |
| `curves_dca.py` | Decision curve analysis (DCA) |
| `curves_calibration.py` | Calibration curve generation |
| `nomogram.py` | Nomogram construction |
| `nri_cir.py` | Net reclassification improvement (NRI) + circos plot |
| `results_html.py` | HTML report assembly of all results |
| `pipeline.py` | Orchestrates all modules; the only file that imports and runs everything together |

Each module should remain independently runnable on its own inputs/outputs, per the shared conventions
in `MODULE.md` — this was an explicit requirement for the original port and should carry forward
to any extension of this pipeline.

## R → Python port-specific caveats to check and flag

When converting from R (this pipeline was originally in R using packages like `rms`, `survival`,
`glmnet`, `pROC`, `rmda`, `circlize`), watch for and explicitly flag to the user:

- **Indexing**: R is 1-indexed, Python/NumPy/pandas is 0-indexed — audit every manual index, not just
  loop bounds.
- **Factor handling**: R's implicit factor releveling has no direct pandas equivalent — categorical
  reference levels must be set explicitly in Python (`pd.Categorical` with explicit `categories`/
  ordering, or explicit dummy-encoding reference group).
- **glmnet vs. Python LASSO**: `glmnet`'s cross-validation and lambda selection (`lambda.min` vs
  `lambda.1se`) doesn't map 1:1 onto `sklearn`/`glmnet-python` defaults — confirm which lambda rule the
  user wants and make it a config parameter, not a hard-coded choice. This paper-level LASSO is
  **not** the in-pipeline habitat `LassoCV`.
- **rms::nomogram vs. Python nomogram construction**: Python has no drop-in equivalent; nomograms are
  typically hand-built from the fitted model's coefficients — the visual layout logic needs its own
  careful review against the original R output.
- **DCA/calibration curve libraries**: R's `rmda`/`ggplot2`-based curves and Python plotting
  (matplotlib/statsmodels-based DCA implementations) can differ in default smoothing/binning — validate
  numerically against the R output on the same data before trusting the port.
- **RNG differences**: R and Python/NumPy random number generators are not seed-compatible — exact
  reproduction of R's specific train/test split or bootstrap resamples from a shared seed is not
  possible; note this explicitly rather than implying the two are numerically identical.
- **Statistical package parity**: NRI computation and circos plotting in particular have no single
  standard Python library equivalent to R's ecosystem — confirm the intended output format before
  implementation, since the visual conventions differ significantly (e.g. `circlize` vs
  `pycirclize`/custom matplotlib).

## Lab 0RAD rules (do not fork)

`VAL_MODE` (refit / apply_formula / lock_threshold), n-group pairwise compare, `CLIN_ID_COL`=`LABEL_COL`, drop high-missing columns, ID columns out of models, HTML survival once: **`04_analysis/references/0rad-pipeline-rules.md`**.

Workspace / `exc` / false-classification: **`01_automation/references/0rad-workspace.md`**.

## Deliverable format

`results_html.py` — the HTML report module — should aggregate outputs from the other modules (tables,
figures) into a single self-contained report; keep it decoupled so it can be re-run after any single
upstream module changes without re-running the entire pipeline.
