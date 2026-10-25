# 02_data-processing/base

Capability bodies for 02 (data processing + analysis). No domain-level SKILL.md.

| Pack | Path | Role |
|---|---|---|
| `clean-data` | `clean-data/` | Clinical Excel/CSV cleaning / cohort tables |
| `imaging-io` | `imaging-io/` | CT/MRI I/O DICOM/NIfTI |
| `preprocess-imaging` | `preprocess-imaging/` | ROI / reader QC |
| `stats-analysis` | `stats-analysis/` | Test selection / assumptions / reporting |
| `calc-sample-size` | `calc-sample-size/` | Sample size / power |
| `meta-analysis` | `meta-analysis/` | Bayesian notes / assumption script (not lab) |
| `model-evaluation` | `model-evaluation/` | Calibration / DCA / external validation + leakage gates |
| `draw-flowchart` | `draw-flowchart/` | STROBE / patient-flow |
| `plot-figures` | `plot-figures/` | Statistical plots / imaging panels |

Lab pipeline policy stays in `personal/analysis/`.

Do not create archive dirs here (historical labels only — do not add new directories in this repo): pictures, fmri, radiomics-habitat.
