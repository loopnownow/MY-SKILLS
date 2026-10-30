# 02_data-processing/base

Thin contracts for 02 (data processing + analysis). No domain-level SKILL.md. The recipe and the revision authority live in `02_data-processing/advanced/` (per-pack digest or the analysis pipeline files); each pack keeps its prose data (`references/`, `scripts/`) beside it.

**Prose SSOT.** Heavy / reusable analysis for this seat lives in `stats-analysis` (`{code_stats}`): `modules/` is the library, `model-validation/` is the CLI half. In-pack `scripts/` may hold **thin helpers** that are meaningful only beside the skill (flowchart drawer, assumption check). Do not vendor patient-table or modeling engines here.

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

Lab pipeline policy stays in `advanced/analysis/` and is the authority; a base pack that grows a long procedure points there instead of restating it.

Retired directory names — never recreate: `pictures`, `fmri`, `radiomics-habitat`. They resolve through `00_orchestrator/legacy_aliases.yaml`.
