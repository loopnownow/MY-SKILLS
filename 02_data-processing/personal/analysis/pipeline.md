# Lab clinical + radiomics pipeline rules

**Owner:** `02_data-processing`. Implementation lives in gold `{code_modules}` (projects point at it; do not keep a per-project `modules` copy — see `sync_modules` in `{RULES}/workspace-layout.md`). Coding conventions → `stats-analysis` + `02_data-processing/personal/coding.md`.

Do **not** re-select features on the test set. Train-only LASSO / clinical selection. Patient-level split.

## Test-set scoring (`VAL_MODE`)

Features stay locked. Three options, no new screening:

| Mode | What is locked | Test-set threshold | When |
|------|----------------|--------------------|------|
| `refit` (default) | Feature list | Refit coefficients on the evaluation layer; Youden on that layer | Default lab run |
| `apply_formula` | Feature list + coefficients | Recalculate Youden on the evaluation layer | Transport the linear predictor; allow a new cut |
| `lock_threshold` | Feature list + coefficients + **training** Youden | Apply the training cut and training calibration | Prospective-style lock |

Calibration plots for `lock_threshold` / `refit` use the layer's predicted probabilities directly (`plot_calibration(..., recalibrate=False)`). Do not refit a display-only logistic on those layers; `apply_formula` may still recalibrate for display. HL uses the same quantile bins as the curve.

General threshold doctrine (never tune the cut on the test set to maximise accuracy) is in `02_data-processing/personal/analysis/methods.md`. These three modes are how the lab implements it.

## Live lab modules (v4.3.0; rules aligned 2026-09-12)

Do **not** vendor `{code_root}` Python into this skill. Implementation stays in `modules/`.
Paper numbers come from `python -m modules.pipeline` → `Results{subproject}.html` (e.g. `Resultsperfusion.html`). Manuscript numbers come only from that page. Old `{endpoint}-results.html` and `results.html` are still recognized for reading; newly written files use the new name. Habitat-tree `LassoCV` is a coding helper, **not** the paper primary.

| Topic | Live behavior | Not the lab |
|-------|---------------|-------------|
| AUC 95% CI | 1000-replicate bootstrap (`_boot_auc_ci`) | DeLong *intervals* |
| DeLong | Paired model-comparison **p** (Sun & Xu 2014 midranks). `ROC_METRICS` columns `DeLong vs {model}`. Added 2026-08-28. | CI method; unpaired DeLong; pROC as the lab runner |
| LASSO | StratifiedKFold **AUC path on TRAIN only** | Nested CV (not implemented) |
| Survival | KM + log-rank always. Optional univariable Cox: `statsmodels` `PHReg`, Breslow. Library default `DO_COX = False`. Contrasts: High vs Low at **train-median** cut, and **per 1 SD**. Report HR, 95% CI, P, N, Events, Schoenfeld `PH_p`. | lifelines / `CoxPHFitter`; multivariate Cox (not implemented); Cox on by default |
| Hosmer–Lemeshow | Quantile bins matching the calibration curve (`DEFAULT_N_BINS = 8`). χ² with **df = G−2**; empty/0–1 expectation bins out of G. Written to `HL_METRICS` + results HTML (`_hl_metrics_html`); **not** drawn on the plot. Added by 2026-09-06 harvest (overrides older “no HL in modules”). | HL as the sole calibration claim; HL *intervals*; claiming modules have no HL |
| Calibration `recalibrate` | `plot_calibration(..., recalibrate=True)` default refits a display logistic on that layer then bins (legacy). For `lock_threshold` / `refit` validation layers set **`recalibrate=False`** (use the layer probabilities as-is). | Always recalibrating the locked / refit layer for the figure |
| Primary model | **Combined** (named primary; nomogram in manuscript prose) | Habitat-tree `LassoCV` as the headline model |
| ICC | Radiomics keep if **ICC(A,1) ≥ 0.75** | Unspecified ICC model |
| Clinical selection | Non-empty `FORCE_MODEL_FEATURES` → Selected / Clinical score / Combined clinical cols / single-clinical ROC. Empty → candidate-pool multivariate p < `ROC_MV_P_THRESHOLD`. Candidate pool: univariate Logistic p < `TABLE1_P_THRESHOLD`, drop complete separation, drop univariate VIF ≥ `VIF_THRESHOLD_HIGH`. Table 1 between-group p does not decide pool entry. AIC stepwise is informational only and does not enter the model. Univariate Logistic includes **VIF**. | Nested CV; stepwise as the fitted model |
| Youden | **Per split** on `refit` / `apply_formula`; training Youden only under `lock_threshold` | Cut tuned to maximise test accuracy |

Nested CV and multivariate Cox may be named as *not implemented*. Never write them as lab defaults.


## Multi-group sheets

A Group column may have 3, 4, or more levels (e.g. `dll_OV`). Modes:

- all groups (no row filter) — **lab default for every project except `dll_OV`**
- pick any two levels (positive / negative)
- all pairwise (every unordered pair)

Default lock: `GROUP_KEEP = []` (no row filter), `PAIRWISE_GROUPS = []`, `PAIRWISE_ALL = false`. Do not invent a two-group keep list or turn on pairwise. The only standing exception is `dll_OV` (multi-level Group, pairwise on). User must explicitly ask before screening or pairwise on any other project.

Not limited to three groups. Console keys: `GROUP_KEEP`, `PAIRWISE_GROUPS`, `PAIRWISE_ALL`.

Pairwise is the same pagination case as multiple outcomes:

- ≥3 pairs → second tab row: Public | Each pair. Each pair page picks positive / negative.
- Multiple outcomes **and** ≥3 pairs → outcome row first; pair row only after entering an outcome
- Output dirs are `{outcome}/{pos_display}_vs_{neg_display}` (single endpoint still uses the outcome column name as the parent). Pairwise PNG/QC live only in the pair folder — do not leave `{outcome}/PNG`
- Per-pair overrides: `PAIRWISE_OVERRIDES[outcome][pos_value_vs_neg_value]`; folder name follows display names. Missing keys inherit that outcome, then public
- `GROUP_LEVEL_DISPLAY` maps Group-column values to short labels (e.g. `Clear Cell Carcinoma` → `CCC`). Pair folders and legends default to these names. Table 1 group headers and legends use short display names (`GROUP_LEVEL_DISPLAY` when a level is mapped; otherwise `GROUP_DISPLAY_POS` / `GROUP_DISPLAY_NEG`). Positive/negative are chosen on the pair page, not the public group card.
- Do not infer groups from ID prefixes in the console (`GROUP_FROM_ID` stays off unless an old ini still sets it)

## IDs and columns

- `CLIN_ID_COL` may be the same as `LABEL_COL`.
- Radiomics ID columns stay as aligned; do not rename the feature matrix.
- `record_id` and every column to its left stay out of models.
- Outcomes listed in `OUTCOME_COLS` are never used as predictors of each other.
- Clinical column roles, skip first: `SKIP_CLIN_FEATURES` (ID / outcome / marker — no Table 1, no nomogram) outranks `FORCE_REMOVE_FEATURES` (Table 1 yes, nomogram no). Overlap stays in skip. Implicit locked skip is `CLIN_ID_COL`, `LABEL_COL`, `Patient_ID`, `Group`, `OUTCOME_COLS`. Do not hardcode `Name`.
- Clinical Table 1 types apply to every lab project / subproject: a raw column that is all numbers (including integer 0–6 such as `Reproductive_History`) is **continuous** by default. English labels and roman/ordinal tokens stay categorical. `CLIN_FORCE_CATEGORICAL` / `CLIN_FORCE_CONTINUOUS` override. `ORDINAL_MAX_LEVELS` no longer reclassifies raw integer columns as counts.
- User-facing endpoints are `OUTCOME_COLS` only (single endpoint = one-item list). `GROUP_SOURCE_COL` is a runtime slot written by `set_outcome`, not a console key. Output dirs are `{outcome}` or `{outcome}/{pos_display}_vs_{neg_display}` when pairwise; `SUBPROJECT_BY_OUTCOME` still remaps the parent. `OUT_DIR_BASE` is retired.
- Sub-outcome grouping comes from that outcome column: running `response_6m` uses `response_6m` levels (then collapsed to 0/1 via `OUTCOME_BINARIZE`). Even if the sheet already has `Group`, do not use it or another outcome column as this sub-outcome's grouping. Fall back to `Group` / `GROUP_COL_KEYWORD` only when the current outcome column is missing.
- `SUBGROUP_COL`: when different from the outcome column, **evaluate only — do not retrain**. Train the primary model on the full cohort by outcome (nomogram / RadScore / Clinical); then apply the locked formula to each level of this column (ROC, calibration, DCA). `GROUP_KEEP` / pairwise lists only decide which strata to evaluate — they do not filter training rows and do not trigger pairwise retrain. Empty or equal to the current outcome = no stratified evaluation.
- Public page has three independent dropdowns (do not follow each other): `VAL_MODE` internal validation, `SUBGROUP_VAL_MODE` subgroup validation, `EXTERNAL_VAL_MODE` external validation. Options are always `refit` (refit) / `apply_formula` (apply formula) / `lock_threshold` (lock threshold). None re-select features (不重筛). Subgroup blank = `apply_formula`. External blank = `refit`. Neither follows internal `VAL_MODE`. If the console copy says blank follows internal validation, these two sentences win.
- External validation evaluates the whole cohort (no further subgroup split). Requires `EXTERNAL_FILE` + dual sheets; multiple rows concatenate horizontally, a single row does not. List key `EXTERNAL_TESTS` (start page may hold several).
- `FORCE_INTER_FEATURES`: key kept for compatibility, **no longer participates in selection**. Missing key inherits public/ini; one outcome's override does not write into others. With multi-outcome console, edit only on each outcome page (public page does not draw it).
- `FORCE_MODEL_FEATURES`: when non-empty, is the sole clinical selection source (Selected / Clinical score / Combined clinical cols / single-clinical ROC). When empty, use candidate-pool multivariate p < `ROC_MV_P_THRESHOLD`. Candidate pool: univariate Logistic p < `TABLE1_P_THRESHOLD`, drop complete separation, drop univariate VIF ≥ `VIF_THRESHOLD_HIGH`. Table 1 between-group p does not decide pool entry. Skip cols and force-remove cols cannot be selected. Missing key inherits public; per-outcome overrides do not affect each other. Console “nomogram variables” = this manual list.
- `FORCE_CLIN_FOR_ROC`: draws extra ROC/NRI/DCA lines only; **must not** drop columns already in `FORCE_MODEL` from the nomogram/Combined.
- **Nomogram / Combined:** clinical cols = `FORCE_MODEL_FEATURES`; when radiomics is present add **RadScore** (literal `RadScore` in `FORCE_MODEL` is the radiomics score, not a clinical col). Dropdown must include RadScore when a rad sheet exists. Figure **must not** draw right-side `max … pts` / `OR=` / `β=` side notes.
- **External validation:** requires `EXTERNAL_FILE` + clinical sheet + radiomics sheet; default sheet names with no file = **no external validation** (do not pass the main-table input off as external); when disabled the report omits the locked-nomogram external block.
- **Advanced-analysis report gates:** when `DO_NRI` / `DO_DAG` / `DO_MEDIATION` are off, omit those report blocks (default False).
- **Sample exclusion:** `DO_EXCLUDE_*` / `EXCLUDE_*` are **project-level**, not outcome overrides; blank-option copy is “blank = default …”.

## Radiomics Logistic and preprocess

`DO_RAD_LOGISTIC` defaults off. Off, that run stays on the LASSO path. On, that run screens radiomics with logistic regression and skips LASSO. RadScore stays the shared score for ROC, the combined model, the nomogram, and SHAP.

Radiomics logistic uses its own keys: `RAD_LOGIT_UNI_P`, `RAD_LOGIT_MV_P`, `RAD_LOGIT_VIF`, and `DO_RAD_FIRTH` (default off). Do not borrow clinical `TABLE1_P_THRESHOLD`, `ROC_MV_P_THRESHOLD`, `VIF_THRESHOLD_HIGH`, or `DO_FIRTH`. Numeric defaults for these keys stay in `config/defaults.py`.

The funnel has the same shape as clinical selection: univariate p, drop complete separation, drop high univariate VIF, then multivariate p. Thresholds come from `RAD_LOGIT_*`. This path does not call `select_clinical` and does not build Table 1. `FORCE_MODEL_FEATURES` stays clinical-only.

Preprocess is fit on the training set. Validation layers reuse that imputation and standardization. `refit` re-estimates coefficients only. It does not redo ICC, standardization, or the correlation filter.

Radiomics preprocess (ICC, correlation filter, prefix strip) sits above LASSO and is shared by both radiomics paths. There is no master switch. Clinical preprocess (force continuous, force count, skip columns) sits above clinical selection. There is no master switch.

Validation modes keep the clinical meanings: `refit` locks the feature list and re-estimates coefficients; `apply_formula` locks coefficients and recalculates Youden on that layer; `lock_threshold` locks coefficients and the training Youden.

## Missingness and HTML

- Drop columns above the missingness cutoff **before** imputation (`02_data-processing/base/clean-data/impute/`; default >50%).
- Results HTML: if a survival curve is drawn twice (sidebar + main), keep the **main** pane only.

## Run

From the project folder, after the console or `settings.ini` is set:

```text
python -m modules.pipeline
```

One `Results{subproject}.html` per subproject. Numbers in the manuscript come only from that page. Old `{endpoint}-results.html` and `results.html` are still recognized for reading; newly written files use the new name.

## HTML Logistic tables

- Multivariate Logistic tables (candidate-pool and Selected) use the **same column order** as Univariate: Variable, OR, 95% CI, P value, VIF, Significance (`***` p<0.001, `**` p<0.01, `*` p<0.05).

## Figures (panels)

- **Survival:** horizontally combine `km_overall` and `km_by_combined_risk` into `panel_survival.png` (A = overall cohort | B = Combined high/low risk). Panel letters follow `FIGURE_PANEL_LABEL_POS` (lab default: lower-left). The results-page Survival section embeds **only** this panel — do not place two single KMs side by side.
- **Nomogram & Calibration panel:** trim near-white margins, then scale panel A width to equal B+C (including the gap) so A's left edge aligns with B's outer edge and A's right edge aligns with C's outer edge.

## Console keys (display)

- `DO_VIF` — §4 switches / ICC.
- `DO_FIGURE_PANELS` — §5b figures / display.
- `DO_NOMOGRAM` — nomogram / combined model control (UI shows one switch). `DO_COMBINED_MODEL` remains ini-compat only; do not expose a second UI control.
- `DO_QC_REPORT` — left pane Data preview / QC.

UI density, choice persistence, no-Chinese results HTML, external-validation same schema, and switch-gated optional figures: see `personal/console-ui-and-report-rules.md`.

