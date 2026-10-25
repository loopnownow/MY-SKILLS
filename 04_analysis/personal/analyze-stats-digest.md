# analyze-stats — thin standing digest (2026-10-24)

Corpus proposal source: Downloads `Grok会话-技能草案-20261024.md` → archived under `{doc_root}\skill-harvest\by-fine-id\`. **Not** a new registry fine-id. Cap stays `base/analyze-stats`. Lab detail SSOT: `methods.md` + `pipeline.md`.

## elements
- **Table 1:** three-row header (group / variable / n); Significance column immediately after P; categorical → positive % only.
- **Multivariable tables:** show all entered features, not only significant rows.
- **DeLong:** paired model-comparison **p** columns live in `ROC summary — train & test`; drop meaningless `Thr source` (2026-08-28). AUC **CI** stays 1000-bootstrap — DeLong is not the CI.
- **Type inference (all lab sub-projects):** all-numeric column → continuous by default; English/roman/ordinal tokens stay categorical; override via `CLIN_FORCE_CATEGORICAL` / `CLIN_FORCE_CONTINUOUS` (2026-08-19).

## process
- Always report train | validation side-by-side; never merged-only results.
- Default pairwise group comparisons; external validation → split inside external; `VAL_MODE` default = refit.
- Nomogram vars: hand-picked first; else Multivariate P<0.05 features.
- Skip re-running QC when results already exist.

## cautions
- Nomogram axes must show original string labels (incl. merged multi-level), never 0/1/2/3 codes; FIGO stays Roman.
- Do not change outcome / inclusion / cutoff / covariates / missingness “to make it run”.
- After an exclusion list fires, re-check denominators (n must drop in lockstep).
- Algorithm library path is `{code_stats}` / `_code\04-analysis\stats-analysis` — **not** under `base/analyze-stats/`. Detail: `methods.md`, `pipeline.md`, `../qc/report-checks.md`.
