# 02_data-processing/base

Capability bodies for 02 (data processing + analysis). No domain-level SKILL.md.

**Prose only.** Runnable code for this seat lives in `stats-analysis` (`{code_stats}`):
`modules/` is the library, `model-validation/` is the CLI half. Never vendor `.py` here.

| Pack | Path | Role | Runs from |
|---|---|---|---|
| `clean-data` | `clean-data/` | Clinical Excel/CSV cleaning / cohort tables | `impute` CLI → `{code_model_validation}\impute_excel.py` |
| `imaging-io` | `imaging-io/` | CT/MRI I/O DICOM/NIfTI | `{code_data_processing}` |
| `preprocess-imaging` | `preprocess-imaging/` | ROI / reader QC | `{code_data_processing}` |
| `stats-analysis` | `stats-analysis/` | Test selection / assumptions / reporting | `{code_modules}` |
| `calc-sample-size` | `calc-sample-size/` | Sample size / power | prose + `{code_modules}` |
| `meta-analysis` | `meta-analysis/` | Bayesian notes / assumption script (not lab) | in-pack `scripts/` |
| `model-evaluation` | `model-evaluation/` | Calibration / DCA / external validation + leakage gates | `{code_model_validation}` |
| `draw-flowchart` | `draw-flowchart/` | STROBE / patient-flow | in-pack `scripts/` |
| `plot-figures` | `plot-figures/` | Statistical plots / imaging panels | `{code_modules}` |

In-pack `scripts/` is reserved for code that is meaningful only as skill prose (a flowchart
drawer, a citation validator). Anything that touches patient tables belongs in `stats-analysis`.

Lab pipeline policy stays in `personal/analysis/`.

Retired directory names — never recreate: `pictures`, `fmri`, `radiomics-habitat`. They resolve through `00_orchestrator/legacy_aliases.yaml`.
