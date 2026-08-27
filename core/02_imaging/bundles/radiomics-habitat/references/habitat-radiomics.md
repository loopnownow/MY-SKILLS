# Multi-Parametric Habitat Radiomics

## Architecture (validated pattern — reuse this module split)

A seven-module split has been validated end-to-end against a real 309-patient MRI dataset. Use it as
the default skeleton unless the user's data/goals require a different split:

- `config.py` — all soft-coded parameters: input/output paths, sequence list, habitat cluster count(s),
  clustering algorithm choice, radiomics feature classes to extract, registration method, random seed.
- `data_loader.py` — reads multi-sequence imaging + ROI/segmentation files, handles missing sequences,
  builds the per-patient case list.
- `preprocessing.py` — resampling, intensity normalization/standardization per sequence, N4 bias field
  correction if MRI, skull-stripping/masking as applicable.
- `registration.py` — inter-sequence (and inter-timepoint, if used) registration; keep the registration
  method and interpolation swappable via config, not hard-coded.
- `habitat.py` — voxel-level clustering across the fused multi-sequence feature space to define tumor
  sub-regions ("habitats"); cluster count and algorithm read from config.
- `radiomics.py` — per-habitat and whole-tumor radiomics feature extraction (e.g. via PyRadiomics),
  feature naming should make habitat origin traceable.
- `pipeline.py` — orchestrates the above modules in order; should be the only place that calls all
  modules together, so each module remains independently runnable/testable.

A companion `visualize_pipeline.py` (habitat maps, per-sequence overlays, QC visualizations) is a
useful addition once the core pipeline is stable — keep it decoupled so it can run on already-computed
outputs without re-running the full pipeline.

## Single-timepoint multi-sequence fusion vs. delta/two-timepoint paradigm

Two distinct designs exist for habitat definition — confirm which one the user wants before building:

- **Delta/two-timepoint**: habitats defined from *change* between two timepoints (e.g. pre/post
  treatment). Requires robust inter-timepoint registration; sensitive to registration error.
- **Single-timepoint multi-sequence fusion**: habitats defined by clustering across multiple
  sequences/parameters at one timepoint (e.g. T1/T2/ADC/DCE at baseline). Avoids inter-timepoint
  registration error but loses temporal-change information.

If migrating between these two paradigms, this is a major architectural change — expect it to touch
`data_loader.py`, `registration.py`, and `habitat.py` at minimum, and flag to the user that habitat
definitions (and therefore downstream radiomics features) are not directly comparable across the two
paradigms.

## Known pitfalls (from prior debugging)

Six categories of bugs have recurred in this type of pipeline and are worth checking proactively:

1. Sequence misalignment silently proceeding without a hard registration-quality check.
2. Habitat cluster count not actually read from config (hard-coded fallback left in from earlier dev).
3. Feature extraction running on the wrong mask (whole-tumor mask instead of per-habitat mask, or vice
   versa) after a refactor.
4. Off-by-one/indexing errors when a case has fewer sequences than expected (missing-sequence handling).
5. Normalization applied before vs. after registration inconsistently across modules.
6. Visualization script assuming a fixed number of habitats when the pipeline now supports a
   configurable count.

## Documentation deliverables

If the user asks for supporting documentation (not just code), prior work in this domain has included:
a technical operations manual, a validation script + report, a bug-fix log, and a merged HTML user
manual. Offer these as optional add-ons rather than assuming they're wanted for every request.
