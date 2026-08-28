---
name: "radiomics-habitat"
domain: "02_imaging"
trigger: ["habitat", "pipeline coding"]
inputs: ["config", "images", "masks"]
outputs: ["scripts", "feature_table"]
tools: ["Python", "CONFIG", "Pictologics", "ANTsPy", "SimpleITK"]
quality_control: "soft-coded CONFIG; modular stages; no test-set reselection; never re-cluster post"
owner: "02_imaging/bundles/radiomics-habitat/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Radiomics & Medical Imaging Pipeline Toolkit

A skill for medical imaging / radiomics pipeline work: multi-parametric habitat radiomics, ROI
expansion and image-ROI file matching, R-to-Python ports of clinical+radiomics ML pipelines, and
foundation-model-based imaging pipelines (e.g. TimesFM for RECIST). Consolidates the coding
conventions and domain patterns already established across this user's prior pipeline projects so
every new script starts from the same baseline instead of being designed from scratch each time.

**Live trees (path pointers only — do not vendor `.py`, NIfTI, or CSV into this skill):**

- `D:\0Grok\0RAD\0scripts\habitat_pipeline` — multiparametric **single timepoint**
- `D:\0Grok\0RAD\0scripts\delta_habitat_pipeline` — longitudinal **delta**

The two trees are **mutually exclusive**. Feature extraction in both is **Pictologics**
`RadiomicsPipeline` (`standard_fbn_32` + `standard_fbs_16`). Do **not** describe the engine as
PyRadiomics. Read `references/habitat-radiomics.md` before writing habitat code.

## Non-negotiable coding conventions

These apply to every script produced under this skill, regardless of which domain below it belongs to.
They come directly from repeated, explicit instructions across this user's pipeline work — do not
deviate from them without being asked to.

1. **Fully soft-coded configuration, centralized at the top of the file.**
   No magic numbers or hard-coded paths buried in function bodies. Every tunable parameter (paths,
   thresholds, window sizes, model hyperparameters, column names, expansion margins in mm, etc.)
   lives in a single config block/section/dataclass at the very top of the script (or in a dedicated
   `config.py` / `0_config.py` for multi-file pipelines).
2. **Modular structure, each module independently runnable.**
   Split by responsibility (data loading, preprocessing, registration, feature extraction, modeling,
   reporting/visualization...). Each module should be runnable and testable on its own, not only as
   part of the full pipeline — mirrors the `config.py / data_loader.py / preprocessing.py /
   registration.py / habitat.py / radiomics.py / pipeline.py` split used in the habitat radiomics
   trees and the per-script split (`u_impute.py`, `u_outlier_detection.py`, `curves_roc.py`,
   `curves_dca.py`, `curves_calibration.py`, `nomogram.py`, `nri_cir.py`, `u_icc.py`, `results_html.py`,
   `pipeline.py`, ...) used in the R→Python clinical pipeline port (`python -m modules.pipeline`).
3. **Heavily commented — and comments are written fresh, not preserved from source material.**
   When porting/rewriting an existing script (e.g. R → Python), do not carry over the original
   comments. Write new, stronger comments in your own words: what each block does, why a parameter
   has the value it does, and any caveat a future user of the script needs to know.
4. **Deliver the final, complete output directly.** Don't hand back a partial draft or a "here's a
   skeleton, fill in the rest" version when the user has given enough information to complete the
   script — write the whole thing.
5. **Flag conversion/refactor caveats proactively.** When porting between languages or refactoring an
   existing pipeline (e.g. R→Python, delta/two-timepoint→single-timepoint), explicitly call out
   anything that changes behavior, precision, or statistical assumptions (e.g. R's `survival`/`rms`
   packages vs Python equivalents, 1-indexing vs 0-indexing, factor handling, RNG differences) — don't
   let those pass silently.

## Choosing the right domain reference

This skill covers four recurring domains. Read the matching reference file in `references/` before
writing code — each captures the specific architecture, known pitfalls, and validated conventions for
that domain:

| Domain | When to use | Reference |
|---|---|---|
| Multi-parametric habitat radiomics | Multi-sequence MRI/CT habitat analysis **or** pre/post delta habitats. Two exclusive CLIs; Pictologics only | `references/habitat-radiomics.md` |
| Clinical + radiomics ML pipeline | Table1, paper LASSO, ROC/DCA/calibration, nomogram, NRI/circos, ICC, imputation, HTML — R→Python ports via `python -m modules.pipeline` | `references/clinical-ml-pipeline.md` |
| ROI/image processing scripts | ROI expansion/dilation, image-ROI filename matching (`match_img_ior_updated.py`), batch medical records | `references/roi-processing.md` |
| Time-series / foundation-model imaging | TimesFM or other foundation-model-based tumor response prediction, RECIST-based longitudinal analysis | `references/timesfm-lung.md` |

If the user's request spans more than one domain (e.g. "extract habitat radiomics features, then feed
them into the LASSO+nomogram pipeline"), read both relevant references — the config conventions above
are shared, so the modules can be chained without redesigning either. In-pipeline habitat selection
is `radiomics.select_features` (**LassoCV** only). Paper-level LASSO / nomogram / `VAL_MODE` live in
`python -m modules.pipeline`, not `utility/LASSO.py`.

## Typical workflow

1. Identify which domain(s) apply and read the corresponding reference(s). For habitat work, pick
   **exactly one** of the two live trees — never blend single-timepoint fusion with delta clustering.
2. Clarify only what's genuinely ambiguous (e.g. imaging modality, expected file naming pattern,
   Python vs MATLAB vs R target) — don't over-ask if the request already specifies enough to proceed.
3. Design/adjust the module split and config schema first, consistent with the conventions above.
4. Write the complete, final code directly — not an outline followed by "I'll fill this in."
5. If this is a refactor or language port, include a short list of behavioral caveats introduced by
   the change (see convention 5 above).
