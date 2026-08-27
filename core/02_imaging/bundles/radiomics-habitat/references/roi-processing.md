# ROI Expansion & Image-ROI File Matching

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

Reference implementation pattern: `match_img_roi_updated.py` — pairs imaging files with their
corresponding segmentation/ROI files when filenames across a dataset don't follow one consistent
convention. This script was refined through three iterative cycles to handle real-world naming
messiness — treat naming-convention handling as inherently iterative and build for extensibility:

- Keep the matching rules (regex patterns, ID-extraction logic, suffix/prefix conventions) as a config
  list/table at the top of the script rather than inline conditional logic, so new naming patterns can
  be added without touching the matching algorithm itself.
- Log/report unmatched files explicitly (both orphan images and orphan ROIs) rather than silently
  dropping them — this is usually the fastest way to spot a new naming convention that needs a rule.
- Prefer a matching strategy based on extracting a stable patient/case identifier from each filename
  (via configurable regex) over pure string-similarity matching, which is fragile against real-world
  naming inconsistency.
- When multiple candidate matches are found for one image (e.g. multiple ROI files with similar names),
  flag for manual review rather than guessing.

## Batch medical record processing

Reference implementation pattern: `pfkm.py` — batch processing of medical records; follows the same
soft-coded-config-at-top convention. Recurring theme across this and the scripts above: code auditing
and bug fixing sessions tend to surface hard-coded values that should be config — when asked to
"review" or "fix" one of these scripts, proactively check for values that should be pulled out into the
config block even if not explicitly flagged by the user.
