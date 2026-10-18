---
name: "imaging-qc"
domain: "02_data-processing"
trigger: ["ROI QC", "mask QC", "读片协议", "reader protocol", "ICC", "Dice", "mask geometry"]
inputs: ["images", "masks", "reader_logs"]
outputs: ["qc_report"]
tools: ["SimpleITK"]
quality_control: "geometry match before features; ICC/Dice on training subset only"
owner: "02-data-processing/imaging-qc/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Imaging ROI / reader / mask QC

Quality-control the **region of interest**, **reader protocol**, and **mask geometry** before
radiomics or modelling. This pack does **not** translate papers and does **not** launch a
bilingual reader. Full-text retrieve is `03-lit-fulltext`. I/O is `02-imaging-io`.

## When to use

- Who segmented, with what experience, blinded to what?
- Do image and mask share spacing / origin / direction / dimensions?
- Inter- and intra-observer ICC, Dice, Hausdorff on a pre-specified subset?
- Which lesion, 2D vs 3D, peritumoral ring, habitat sub-region?

## When to open extra files

| File | Open when |
|---|---|
| [references/reader-protocol.md](references/reader-protocol.md) | Number of readers, blinding, independent vs consensus, adjudication |
| [references/mask-geometry.md](references/mask-geometry.md) | Spacing/origin/direction mismatch; DICOM→NIfTI flips; mask resample |
| [references/reproducibility-qc.md](references/reproducibility-qc.md) | ICC / Dice / HD95; feature-stability filter before selection |
| [references/lesion-selection.md](references/lesion-selection.md) | 2D vs 3D, index lesion, multi-lesion rule, peritumoral ring |

## Workflow

1. **Inventory** modality, software, mask format (NIfTI / DICOM-SEG / RTSTRUCT), intended ROI.
2. **Geometry QC** (`mask-geometry.md`) — assert image/mask invariants; overlay a sample; nearest-neighbour mask resample only.
3. **Reader protocol** (`reader-protocol.md`) — ≥2 blinded readers on a reproducibility subset; define the analysis mask provenance.
4. **Reproducibility** (`reproducibility-qc.md`) — ICC/Dice/HD on that subset, **training only**; drop unstable features before selection.
5. **Lesion rule** (`lesion-selection.md`) — pre-specify index lesion / aggregation; do not change it after seeing AUC.
6. **Hand off** feature extraction / habitat clustering → `02-radiomics-habitat`. Do not fit models here.

## Output contract

- Geometry pass/fail per case (or sampled subset) with the mismatch named.
- Reader protocol sentence (n readers, seniority, blinding, consensus rule, software).
- Reproducibility metrics and the pre-specified ICC threshold, with how many features survived.
- No invented n, ICC, or Dice. Paper translation is out of scope.

## Handoffs

- Volumetric I/O → `02-imaging-io`
- Radiomics / habitat / leakage → `02-radiomics-habitat`
- Modelling / calibration → `04-stats-models` / `04-model-eval`
