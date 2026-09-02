# 0RAD clinical + radiomics pipeline rules

**Owner:** `04_analysis`. Implementation lives in `D:\0Grok\0RAD\modules` (and copies under each project). Workspace / file layout → `02_data-processing/0rad-workspace.md`. Coding conventions → mounted `02-radiomics-habitat` + `02_data-processing/code-refactoring`.

Do **not** re-select features on the test set. Train-only LASSO / clinical selection. Patient-level split.

## Test-set scoring (`VAL_MODE`)

Features stay locked. Three options, no new screening:

| Mode | What is locked | Test-set threshold | When |
|------|----------------|--------------------|------|
| `refit` (default) | Feature list | Refit coefficients on the evaluation layer; Youden on that layer | Default lab run |
| `apply_formula` | Feature list + coefficients | Recalculate Youden on the evaluation layer | Transport the linear predictor; allow a new cut |
| `lock_threshold` | Feature list + coefficients + **training** Youden | Apply the training cut and training calibration | Prospective-style lock |

Calibration plots for `lock_threshold` / `refit` use the layer's predicted probabilities directly (do not refit a display-only logistic unless `apply_formula`).

General threshold doctrine (never tune the cut on the test set to maximise accuracy) is in `radiology-stats/model-evaluation.md`. These three modes are how the lab implements it.

## Live lab modules (v4.3.0, 2026-08-28)

Do **not** vendor `D:\0Grok\0RAD` Python into this skill. Implementation stays in `modules/`.
Paper numbers come from `python -m modules.pipeline` → `*-results.html`. Habitat-tree `LassoCV` is a coding helper, **not** the paper primary.

| Topic | Live behavior | Not the lab |
|-------|---------------|-------------|
| AUC 95% CI | 1000-replicate bootstrap (`_boot_auc_ci`) | DeLong *intervals* |
| DeLong | Paired model-comparison **p** (Sun & Xu 2014 midranks). `ROC_METRICS` columns `DeLong vs {model}`. Added 2026-08-28. | CI method; unpaired DeLong; pROC as the lab runner |
| LASSO | StratifiedKFold **AUC path on TRAIN only** | Nested CV (not implemented) |
| Survival | KM + log-rank always. Optional univariable Cox: `statsmodels` `PHReg`, Breslow. Library default `DO_COX = False`. Contrasts: High vs Low at **train-median** cut, and **per 1 SD**. Report HR, 95% CI, P, N, Events, Schoenfeld `PH_p`. | lifelines / `CoxPHFitter`; multivariate Cox (not implemented); Cox on by default |
| Primary model | **Combined** (named primary; nomogram in manuscript prose) | Habitat-tree `LassoCV` as the headline model |
| ICC | Radiomics keep if **ICC(A,1) ≥ 0.75** | Unspecified ICC model |
| Clinical selection | Table 1 then **AIC backward** (`FORCE_MODEL_FEATURES` bypasses) | Nested CV for clinical covariates |
| Youden | **Per split** on `refit` / `apply_formula`; training Youden only under `lock_threshold` | Cut tuned to maximise test accuracy |

Nested CV and multivariate Cox may be named as *not implemented*. Never write them as lab defaults.


## Multi-group sheets

A Group column may have 3, 4, or more levels (e.g. `dll_OV`). Modes:

- all groups (no row filter) — **lab default for every project except `dll_OV`**
- pick any two levels (positive / negative)
- all pairwise (every unordered pair)

Default lock: `GROUP_KEEP = []`（不筛行）, `PAIRWISE_GROUPS = []`, `PAIRWISE_ALL = false`. Do not invent a two-group keep list or turn on pairwise. The only standing exception is `dll_OV` (multi-level Group, pairwise on). User must explicitly ask before screening or pairwise on any other project.

Not limited to three groups. Console keys: `GROUP_KEEP`, `PAIRWISE_GROUPS`, `PAIRWISE_ALL`.

Pairwise is the same pagination case as multiple outcomes:

- ≥3 pairs → second tab row: 公共 | 各对。Each pair page picks positive / negative.
- Multiple outcomes **and** ≥3 pairs → outcome row first; pair row only after entering an outcome
- Output dirs are `{outcome}/{阳性展示名}_vs_{阴性展示名}` (single endpoint still uses the outcome column name as the parent). Pairwise PNG/QC live only in the pair folder — do not leave `{outcome}/PNG`
- Per-pair overrides: `PAIRWISE_OVERRIDES[outcome][列值阳_vs_列值阴]`; folder name follows display names. Missing keys inherit that outcome, then public
- `GROUP_LEVEL_DISPLAY` maps Group-column values to short labels (e.g. `Clear Cell Carcinoma` → `CCC`). Pair folders and legends default to these names. Positive/negative are chosen on the pair page, not the public group card.
- Do not infer groups from ID prefixes in the console (`GROUP_FROM_ID` stays off unless an old ini still sets it)

## IDs and columns

- `CLIN_ID_COL` may be the same as `LABEL_COL`.
- Radiomics ID columns stay as aligned; do not rename the feature matrix.
- `record_id` and every column to its left stay out of models.
- Outcomes listed in `OUTCOME_COLS` are never used as predictors of each other.
- Clinical column roles, skip first: `SKIP_CLIN_FEATURES` (ID / outcome / marker — no Table 1, no nomogram) outranks `FORCE_REMOVE_FEATURES` (Table 1 yes, nomogram no). Overlap stays in skip. Implicit locked skip is `CLIN_ID_COL`, `LABEL_COL`, `Patient_ID`, `Group`, `OUTCOME_COLS`. Do not hardcode `Name`.
- Clinical Table 1 types apply to every 0RAD project / 子工程: a raw column that is all numbers (including integer 0–6 such as `Reproductive_History`) is **continuous** by default. English labels and roman/ordinal tokens stay categorical. `CLIN_FORCE_CATEGORICAL` / `CLIN_FORCE_CONTINUOUS` override. `ORDINAL_MAX_LEVELS` no longer reclassifies raw integer columns as counts.
- User-facing endpoints are `OUTCOME_COLS` only (single endpoint = one-item list). `GROUP_SOURCE_COL` is a runtime slot written by `set_outcome`, not a console key. Output dirs are `{outcome}` or `{outcome}/{阳性展示名}_vs_{阴性展示名}` when pairwise; `SUBPROJECT_BY_OUTCOME` still remaps the parent. `OUT_DIR_BASE` is retired.
- 子结局分组来自该结局列：跑 `response_6m` 就用 `response_6m` 的水平（再按 `OUTCOME_BINARIZE` 收成 0/1）。表里即使已有 `Group`，也不许拿它或别的结局列当这个子结局的分组。仅当当前结局列不存在时才回退到 `Group` / `GROUP_COL_KEYWORD`。
- `SUBGROUP_COL`：与结局列不同时，**只评估、不重训**。全队列按结局训主模型（列线图 / RadScore / Clinical）；再把锁死公式套到该列各水平（ROC、校准、DCA）。`GROUP_KEEP` / 两两名单只决定评估哪些层，不筛训练行，也不再走 pairwise 重训。空或等于当前结局=不做分层评估。
- 公共页三个独立下拉（不互相跟随）：`VAL_MODE` 内部验证、`SUBGROUP_VAL_MODE` 亚组验证、`EXTERNAL_VAL_MODE` 外部验证。选项均为 `refit`（重新拟合）/ `apply_formula`（套公式）/ `lock_threshold`（锁定阈值）。均不重筛。
- 外验整队列评估（不按亚组再拆）。多条横拼，一条不拼。列表键 `EXTERNAL_TESTS`（起始页可多条）。
- `FORCE_INTER_FEATURES`：缺键继承公共/ini；某一结局的覆盖不写进其它结局。控制台多结局时只在各结局页改（公共页不画）。对子缺键继承该结局，再缺则公共。`SUBGROUP_COL` 仍缺省空（不做分层评估）。
- `FORCE_MODEL_FEATURES`：人为指定进入 Clinical 模型和 nomogram 的临床列，不受 Table 1 p / stepwise / 多因素 p 剔除。跳过列和强制剔除列不能选。缺键继承公共；各结局覆盖互不影响。与 `FORCE_INTER_FEATURES` 不同：交互名单仍可被 stepwise 拿掉，纳入模型名单会在筛选后强制加回并重拟合。

## Missingness and HTML

- Drop columns above the missingness cutoff **before** `data-impute` (default >50%).
- Results HTML: if a survival curve is drawn twice (sidebar + main), keep the **main** pane only.

## Run

From the project folder, after the console or `settings.ini` is set:

```text
python -m modules.pipeline
```

One `*-results.html` per endpoint. Numbers in the manuscript come only from that file.
