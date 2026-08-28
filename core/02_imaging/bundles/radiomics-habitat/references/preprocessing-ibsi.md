# Preprocessing to IBSI standard

Every preprocessing choice changes the features. Fix them a priori, apply uniformly, and report
to IBSI so the features are reproducible.

Live trees (do not vendor): `habitat_pipeline` and `delta_habitat_pipeline` `PREPROC` /
`preprocessing.py`.

## Resampling (voxel size)

- **Target spacing:** `PREPROC["target_spacing"] = (1.0, 1.0, 1.0)` mm, both trees.
- **Image interpolator:** SimpleITK `sitkBSpline` (**B-Spline order 5**).
- **Mask interpolator:** `sitkNearestNeighbor`.
- **Default pixel fill:** `SetDefaultPixelValue(0)`.

**Delta-tree bug to not reintroduce:** `resample_image` must fill **0**, not
`image.GetPixelIDValue()` (that passes the pixel-type enum, e.g. Float32=8, as the pad value).
The delta tree documents this as BUG-2.

## Intensity normalisation / handling

| Modality | Live handling |
|---|---|
| **CT** | **No N4** (`apply_n4` False). `normalization` = **minmax** after `ct_window` clip (live window `(-1000, 400)` HU unless overridden). |
| **MRI** | **N4 + zscore** (`apply_n4` True; `normalization` = `zscore`). |
| **ADC** | Habitat tree `PREPROC["SEQUENCE_OVERRIDES"]`: `{"ADC": {"normalization": "none"}}` — ADC is already quantitative; do not z-score it. Delta tree has no per-sequence override dict (single-image pre/post). |
| **PET** | Not configured in these trees; if added, use SUV and state the normalisation. |

Habitat tree: `resolve_preproc_settings(sequence_name, modality)` applies modality defaults then
`SEQUENCE_OVERRIDES`. Delta tree: `preprocess(...)` uses flat `PREPROC` (live defaults are CT-like:
N4 off, minmax). Do not silently copy habitat MRI/ADC overrides onto delta without a config change.

State whether normalisation is fit per-image (these trees: per-image / per-mask) — never use test
cohort statistics for intensity scaling.

## Gray-level discretisation (IBSI; complementary, not "pick one")

These trees run **both** Pictologics standard configs (`feature-extraction.md`):

- **FBN32** — `standard_fbn_32` (fixed bin **number**, 32).
- **FBS16** — `standard_fbs_16` (fixed bin **size**, width = range / 16).

They are **complementary** (IBSI: different families are sensitive to different discretisations).
Do not collapse this to "choose one of binWidth or binCount." Report both config names.

## Filters / image transforms

Voxel-clustering channels (habitat tree `VOXEL_FEATURES`: local texture, gradient, optional LoG /
wavelet) are **inputs to K-means**, not a substitute for Pictologics standard configs. Declare
each switch and account for multiplicity downstream (→ radiology-stats).

## Mandatory IBSI reporting (cross-ref radiology-reporting/ibsi-features.md)

- Image interpolation + resampled spacing `(1,1,1)`; B-Spline 5 / mask NN; fill 0.
- Intensity normalisation / re-segmentation range (`ct_window`) / ADC `normalization=none`.
- Discretisation: FBN32 **and** FBS16.
- Filters + parameters (voxel-feature switches vs Pictologics configs — keep them distinct).
- Feature aggregation (3D, habitat masks).
- Software + version + IBSI compliance statement (**Pictologics**, not PyRadiomics).

## Reporting sentence

*"Images were resampled to 1×1×1 mm (B-spline order 5; masks nearest-neighbour; default fill 0,
not pixel-id). CT: no N4, minmax after ct_window. MRI: N4 + z-score. ADC in the habitat tree uses
SEQUENCE_OVERRIDES normalization=none. Features used Pictologics standard_fbn_32 and
standard_fbs_16 as complementary IBSI discretisations."*
