# ROI Expansion & Image-ROI File Matching

## Delta habitats: 1 pre + 1 post, both with ROI

`delta_habitat_pipeline.data_loader.load_patient_pairs` is a **pair** loader: each patient has
exactly **one pre and one post**, and **both** timepoints must have an ROI (`roi_path`). There is
no "post without mask, invent one" path.

- Cluster **baseline only** (`build_habitats` on pre image + pre ROI).
- Post habitat masks come from `registration.propagate_masks` (ANTs forward transform of the
  baseline habitat list onto registered post space).
- **Never re-cluster post.**

`HABITAT["min_voxels"]` is the minimum voxels inside a habitat mask before Pictologics extraction
(`extract_features_single_habitat` / `_sequence` raise `ValueError` below the threshold). Live
default is `0` (still a config key — do not hard-code a different floor in function bodies).

## propagate_masks is the source of truth

`delta_habitat_pipeline/registration.py::propagate_masks` is how post habitats stay anatomically
corresponding to baseline IDs.

HTML / pipeline comments that say **"remove mask propagation"** / **"方案 A，删除传播"** (reuse
`habitat_masks_t1` as `habitat_masks_t2` without a transform) are **wrong**. Do not document or
re-implement that shortcut. Validation: `utility/validate_delta_habitat.py::propagate_masks_val`.

`compute_delta_features` assumes pre/post habitat indices match because of `propagate_masks`.

## ROI expansion (dilation)

Reference implementation pattern: `expand_roi_5mm.py` — expands a segmentation mask (ROI/VOI) by a
configurable margin (e.g. 5mm) in physical space, not voxel space, so the same config value produces
the correct expansion regardless of a case's voxel spacing.

Config to expose at the top of the script (not hard-coded):
- Expansion margin in mm (the "5mm" should be a config value, not baked into the filename/logic).
- Whether expansion should be clipped to image bounds and/or to an anatomical mask (e.g. don't expand
  outside the liver into surrounding organs).
- Interpolation/structuring-element shape for the morphological dilation (spacing-aware, e.g. using the
  image's actual voxel spacing to build the structuring element rather than assuming isotropic voxels).
- Output naming convention for the expanded mask (should not silently overwrite the original ROI).

Common bug pattern to check for: dilation implemented in voxel space with a fixed number of voxels,
which produces inconsistent physical expansion across cases with different voxel spacing — always
convert the mm margin to voxel units per-case using that case's actual spacing.

## Image-ROI file matching across heterogeneous datasets

Reference implementation: `habitat_pipeline/utility/match_img_ior_updated.py`.

This is **filename matching** (regex / ID extraction / suffix-prefix rules for pairing image files
with IOR/ROI files). It is **not** HIS / EMR / hospital-information-system lookup. Do not describe
it as pulling identifiers from HIS.

Keep matching rules as a config list/table at the top of the script rather than inline conditionals.
Log unmatched files (orphan images and orphan ROIs). Prefer extracting a stable patient/case id
from each filename over pure string-similarity. Multiple candidates → flag for manual review, do
not guess.

(Older notes named this `match_img_roi_updated.py`; the live filename is `match_img_ior_updated.py`.)

## Batch medical record processing

Reference implementation pattern: `pfkm.py` — batch processing of medical records; follows the same
soft-coded-config-at-top convention. Recurring theme: code auditing sessions tend to surface
hard-coded values that should be config — when asked to "review" or "fix" one of these scripts,
proactively check for values that should be pulled out into the config block even if not explicitly
flagged by the user.
