---
name: "preprocess-imaging"
domain: "02_data-processing"
trigger: ["DICOM", "NIfTI", "nii", "读图", "格式转换", "ROI QC", "mask QC", "读片协议", "reader protocol", "ICC", "Dice", "mask geometry"]
inputs: ["images", "masks", "reader_logs"]
outputs: ["volume_or_series", "qc_report"]
tools: ["pydicom", "SimpleITK", "nibabel"]
quality_control: "geometry match before features; ICC/Dice on training subset only"
owner: "02_data-processing/base/preprocess-imaging/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Imaging I/O and ROI/reader QC

Contract only for preprocess-imaging: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/pipeline.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Covers volumetric **I/O** (DICOM/NIfTI read, convert, organise, geometry preserve) and **ROI / reader / mask QC** before radiomics or modelling. Absorbed former fine id `imaging-io` (alias in `00_orchestrator/legacy_aliases.yaml`). This pack does **not** translate papers and does **not** launch a bilingual reader. Full-text retrieve is `lit-search`.

## When to use

- Read, convert, or organise DICOM series / NIfTI volumes
- Who segmented, with what experience, blinded to what?
- Do image and mask share spacing / origin / direction / dimensions?
- Inter- and intra-observer ICC, Dice, Hausdorff on a pre-specified subset?
- Which lesion, 2D vs 3D, peritumoral ring, habitat sub-region?

## When to open extra files

| File | Open when |
|---|---|
| [references/data.md](references/data.md) | Imaging formats, labels, masks, privacy, repositories, availability wording |
| [references/reader-protocol.md](references/reader-protocol.md) | Number of readers, blinding, independent vs consensus, adjudication |
| [references/mask-geometry.md](references/mask-geometry.md) | Spacing/origin/direction mismatch; DICOM to NIfTI flips; mask resample |
| [references/reproducibility-qc.md](references/reproducibility-qc.md) | ICC / Dice / HD95; feature-stability filter before selection |
| [references/lesion-selection.md](references/lesion-selection.md) | 2D vs 3D, index lesion, multi-lesion rule, peritumoral ring |

## Workflow

### Phase A - I/O (former imaging-io)

1. **Identify** the input: DICOM series, NIfTI/NII, or mixed.
2. **Read** with a named library (pydicom, SimpleITK, nibabel). Record software + version.
3. **Preserve geometry** - spacing, origin, direction, slice order. Do not silently flip axes.
4. **Convert** only when asked. After DICOM to NIfTI, overlay or print geometry vs the source.
5. **Organise** one volume per series (or BIDS-like layout if the user wants it). Log unmatched files.

### Phase B - ROI / reader / mask QC

6. **Inventory** modality, software, mask format (NIfTI / DICOM-SEG / RTSTRUCT), intended ROI.
7. **Geometry QC** (`mask-geometry.md`) - assert image/mask invariants; overlay a sample; nearest-neighbour mask resample only.
8. **Reader protocol** (`reader-protocol.md`) - blinded readers on a reproducibility subset; define the analysis mask provenance.
9. **Reproducibility** (`reproducibility-qc.md`) - ICC/Dice/HD on that subset, **training only**; drop unstable features before selection.
10. **Lesion rule** (`lesion-selection.md`) - pre-specify index lesion / aggregation; do not change it after seeing AUC.
11. **Hand off** feature extraction / habitat clustering - `stats-analysis`. Do not fit models here.

## Output contract

- Volume or series path(s) with software/version and geometry note when I/O ran.
- Geometry pass/fail per case (or sampled subset) with the mismatch named.
- Reader protocol sentence (n readers, seniority, blinding, consensus rule, software).
- Reproducibility metrics and the pre-specified ICC threshold, with how many features survived.
- No invented n, ICC, or Dice. Paper translation is out of scope.

## Data availability

Imaging formats, labels, masks, privacy, repositories, and availability wording:
[data.md](references/data.md). That file is **not** the `clean-data` clinical-Excel front.

Clinical Excel/CSV (headers, missingness, ID, cohort) - `clean-data`.

Backup sources (not vendored): Scientific `pydicom` / `bids` / `imaging-data-commons`.

## Handoffs

- Clinical Excel/CSV - `clean-data`
- Radiomics / habitat / leakage - `stats-analysis`
- Modelling / calibration - `model-evaluation`
