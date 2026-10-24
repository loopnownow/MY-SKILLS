# Figures (palettes + claim planning)

## Standing defaults (2026-10-24)

- **In-figure text = Arial** (dual track with body Times New Roman). See `plot-figures-digest.md`.
- **Flowchart (Figure 1) = PDF preferred** — `draw-flowchart-digest.md` + `base/draw-flowchart/references/style.md`.

## Part A — Lab palettes

# Lab figure palettes (0RAD console)

**Owner:** `05_manuscript` (`{doc_root}\\templates\\lab-palettes.md`). Hex must match `{code_modules}\config\style.py` `FIG_PALETTES` and `modules\console\console_schema.js` `PALETTES`.

Generic journal palettes (ggsci NPG / Okabe–Ito / Morandi role maps) stay in mounted `plot-figures` (`color-systems.md`). This file is the **lab console five-set** used by the 0RAD pipeline.

One palette per manuscript. Main roles in order: **Combined, RadScore, Clinical, Reader, Age**. Auxiliary colors: remaining ROC curves, KM strata, unnamed models.

| id | Label | Use | Main (5) | Aux (5) |
|----|-------|-----|----------|---------|
| `npg` | NPG current | **Default.** Revisions / extra panels so Combined / RadScore / Clinical do not jump | `#D55E00` `#B2182B` `#2166AC` `#762A83` `#117733` | `#44AA99` `#DDCC77` `#EE8866` `#AA4499` `#332288` |
| `okabe` | Okabe–Ito | **New project first choice.** Color-blind safe | `#D55E00` `#0072B2` `#009E73` `#CC79A7` `#E69F00` | `#56B4E9` `#332288` `#882255` `#44AA99` `#999999` |
| `tol` | Paul Tol | Print / Radiology large figures | `#CC6677` `#332288` `#117733` `#88CCEE` `#DDCC77` | `#AA4499` `#44AA99` `#882255` `#6699CC` `#999933` |
| `radiology` | teal-orange | Lab console / series papers | `#0F4C5C` `#C44E52` `#3B6EA5` `#E07A3D` `#2F6F4E` | `#7EB6A4` `#88B4D8` `#D4A373` `#6B5B95` `#8A8A8A` |
| `ibm` | IBM | Projection / results HTML | `#DA1E28` `#0F62FE` `#198038` `#8A3FFC` `#B28600` | `#1192E8` `#009D9A` `#FA4D56` `#A56EFF` `#6F6F6F` |

`npg` keeps the **legacy named** map for clinical covariates (LNM, FIGO, …) so old figures do not recolor.

Config keys: `FIG_PALETTE`, `FIG_COLORS_MAIN`, `FIG_COLORS_AUX`. Hand-edited swatches become custom; write-back goes to `ref/settings.ini`.

## Publication extension palettes (10 sets; not console-bound)

Not wired into `style.py` / `console.html` and not managed by `FIG_PALETTE`. Cite manually for submission figures, not 0RAD pipeline plots. All from public scientific color specs (ColorBrewer / matplotlib built-ins / Paul Tol / Crameri / ggsci). Grouped by chart type; covers continuous, diverging, and grayscale-safe cases that the five `lab-palettes` sets plus mounted `plot-figures` (Okabe-Ito/NPG/Morandi) do not cover.

| id | Label | Type | Use | Values / source |
|----|-------|------|-----|-----------------|
| `brewer-set2` | ColorBrewer Set2 | categorical, soft | ≤6-group bar/scatter; color-blind friendly | `#66C2A5 #FC8D62 #8DA0CB #E78AC3 #A6D854 #FFD92F` |
| `brewer-dark2` | ColorBrewer Dark2 | categorical, saturated | multi-series line charts needing strong separation | `#1B9E77 #D95F02 #7570B3 #E7298A #66A61E #E6AB02` |
| `viridis` | Viridis | continuous, perceptually uniform | heatmaps / density / continuous risk scores; color-blind and grayscale safe | matplotlib built-in; `cmap="viridis"` |
| `magma` | Magma | continuous, warm | warm alternative to viridis; radiomics feature heatmaps avoid “green = normal” clinical cue | matplotlib built-in; `cmap="magma"` |
| `cividis` | Cividis | continuous, color-blind optimized | first choice for continuous values when reviewers may be color-weak | matplotlib built-in; `cmap="cividis"` |
| `rdbu` | RdBu Diverging | diverging | correlation / feature-selection heatmaps; signed symmetric values | ColorBrewer diverging; `cmap="RdBu_r"` |
| `prgn` | PRGn Diverging | diverging, purple-green | diverging alternative when red–green associations (political/clinical) must be avoided | ColorBrewer diverging; `cmap="PRGn"` |
| `batlow` | Batlow (Crameri) | continuous, scientific | perceptually safe maps journals (Nature/Science family) increasingly expect; replaces jet/rainbow | Fabio Crameri scientific colour maps; BSD |
| `grayscale-safe` | grayscale-safe ramp | mono gradient | some journals still require B&W print legibility; re-check with this ramp before submission | `#F7F7F7 #CCCCCC #969696 #636363 #252525` |
| `ggsci-lancet` | ggsci Lancet | categorical, journal style | closer to Lancet-family visual norms | R package `ggsci::pal_lancet()`; MIT |

Selection: categorical (≤6 groups) → `brewer-set2` / `brewer-dark2`; continuous (risk/probability/density) → `viridis` / `magma` / `cividis`; correlation / difference heatmaps → `rdbu` / `prgn`; grayscale pre-submission pass → `grayscale-safe`; journal-specific overlay → matching `ggsci-*`. Relation to the five `lab-palettes`: console plots (KM/ROC/risk strata) keep npg/okabe/tol/radiology/ibm; these 10 are for continuous/matrix figures or first-submission journal fit. Do not mix both on the same figure.


---

## Part B — Figure claim planning

# Figure claim planning (radiomics / clinical prediction)

**Owner:** `04_analysis`. Use in the planning stage before submission figures are built — not as after-the-fact rescue. Pair with `personal/figures.md` (palettes) and mounted `plot-figures` (chart templates). This section only covers “think first”.

## 1. Ask for the claim, then pick the chart — not “how this data is usually plotted”

Before choosing a chart, ask: **which Discussion sentence must this figure prove to the reader?** The claim picks the chart type, not the data type or aesthetics. Lab claim → chart map:

| Claim type | Use this | Do not use this |
|---|---|---|
| “Combined outperforms Clinical” | paired ROC overlay + DeLong p in the legend | two separate AUC bar charts (drops pairing) |
| “Predicted probabilities are well calibrated” | calibration curve (predicted vs observed) | a lone Brier score with no figure |
| “High vs low risk differ in survival” | KM + log-rank, risk table under the plot | Cox forest (lab does not run multivariate Cox; see `personal/pipeline.md`) |
| “Feature selection is stable” | LASSO path (TRAIN-only StratifiedKFold AUC path) | feature-importance bars (hides selection instability) |
| “Radiomics is reproducible” | ICC distribution / forest with ICC≥0.75 threshold line | prose-only “ICC was good” |

If the claim is unclear, write the Discussion sentence first, then back into the chart — if the sentence will not write, the figure should not start.

## 2. Figure–evidence checklist: build before drawing, not after reconciling

Before a submission, list planned figures (in `handoff.yaml` `outputs` or a `figure-manifest.md`). For each figure record three things:

| Figure | Claim (which Discussion sentence) | Data source (which `*-results.html`) |
|---|---|---|
| Fig 2 | Combined outperforms Clinical | `RadScore-results.html` |
| Fig 3 | High vs low risk differ in survival | `Survival-results.html` |

This is not a new invention — it moves existing **G-FACT / G-04** (numbers must come from upstream `*-results.html`, never invented) from “05 checks after writing” to “04 registers before plotting”. Once the list exists, plotting and writing both check the same table, so figure and prose cannot each “look right” while disagreeing.

## 3. Per-figure repair cap: three rounds; after round 3 mark “unresolved” honestly

Per figure: render → open the actual image (not “the code should be fine”) → fix → re-render → re-check. **At most three repair rounds**; the first render does not count. After round 3, keep the result and mark “unresolved” in `qc`/`defects` — do not stamp a broken figure “pass” just to deliver.

This reuses the `gates.md` rule “same defect ≤3 rounds, then unresolved and stop”. Reminder only: figure QC means “open the image”, not “script exited zero”.

## 4. Style and palette are two independent switches — do not fuse them into one two-option question

**Style** (console-internal vs journal submission; extra composite panels or not) and **palette** (five console `lab-palettes` vs the ten publication extensions) are unrelated and freely combinable. If both are unknown, one combined ask is fine; if either is already fixed for the project (e.g. submission style), ask only for the missing one — do not re-ask what is settled. Extra/reworked figures in the same task reuse both choices; do not re-ask per figure — same habit as the `00_orchestrator` Plan card “ask once, do not re-ask”.

---

## Part C — Imaging montage workflow (de-identify → grid → layered delivery)

**Owner:** `04_analysis` (personal). Generic rules (de-identify, WL/WW, annotations, legends) live in `04_analysis/base/plot-figures/references/imaging-panels.md`. This section only records the owner's montage defaults and delivery format; it does not override base.

### 1. Steps

1. **De-identify first:** crop burned-in patient identifiers — name (including Chinese names), MRN, and other PHI. Handle `Page x of y`, `IM/SE`, rulers/tick marks, edge bars, and extra black borders per this run's brief. **Standing (owner 2026-10-21):** before stripping **non-patient** burned-in labels/text (device params, sequence names, non-PHI notes, …), **ask the owner** whether to keep them; do not strip without explicit consent. **Open every cropped result and visually confirm** no residual patient ID — “coordinates were calculated” is not enough.
2. **Do not change WL/WW or contrast:** crop + resample (Lanczos) only; leave pixel values untouched.
3. **Grid:** rows×cols as the owner specifies; panel order follows the owner's original filenames a–f (after rename, map back by size etc.); do not reorder by sequence type.
4. **Cells:** equal squares; scale preserving aspect; **black fill** for empty margins.
5. **Gutter:** per this run; default 6 px white; when the owner says “no gutter”, use 0 px and a black background (no white showing anywhere).
6. **Labels:** A–F uppercase, **Arial Bold** (`arialbd.ttf`; PIL `ImageFont.truetype("arialbd.ttf", 48)` — not DejaVu defaults), white + thin black stroke (2 px), default **lower-left** of each cell; print size ~10–12 pt (~48 px tall at 300 dpi).
7. **Size:** dual-column ~174 mm @ 300 dpi ≈ 2055 px wide (e.g. 6 px gutter → 677 px cells, 2055×1372; 0 gutter → 685 px cells, 2055×1370).

### 2. Default delivery

- **Owner-facing deliverables (default):** **PNG preview** (300 dpi) + **layered PSD zip** (`.psd.zip`, `testzip()` before handoff). **Do not hand the owner a bare `.psd`** (usually huge); unzip when layers are needed. Bare `.psd` may stay in `ref/tmp` or `{DEL}\_by-project\<project>\` for QC — not on the “hand to owner” list (「交给本人」).
- **Layered PSD contents** (the file inside the zip): Background + one layer per panel (full-canvas size, transparent outside its cell) + Labels layer; size is **width first**; write 300 dpi (ResolutionInfo 1005); **must write a flattened composite** (image data) or most viewers show solid black.
- **TIFF only when the owner explicitly asks:** flat, LZW, 300 dpi. No multi-page TIFF unless asked.
- True layered TIFF is impractical without GIMP/Photoshop → deliver **PSD.zip**; owner unzips and “Save As TIFF (preserve layers)” in Photoshop.

### 3. QC (run all before every delivery)

- Re-open PSD with psd_tools: `size == (W, H)` and landscape.
- Pixel-compare `composite()` vs PNG preview; diff must be 0 (once for stored composite, once rebuilt with `force=True`).
- Each panel layer's opaque bbox stays inside its cell; Labels layer is letters only.
- With 0 gutter: white pixel count on cell borders/edges is 0; Background is pure black.
- zip `testzip()` returns None.
- Actually open the preview (same as Part B §3: look at the image, not “script exited zero”).

### 4. Known pitfalls

- **pytoshop `size` is (width, height)**; numpy channel arrays are (H, W); swap them and you get a portrait PSD.
- pytoshop does not write a composite by default → PSD opens black; set `psd.image_data`. Its RLE path errors on newer Python (`packbits` undefined) — use raw (large files → zip).

Label font: Arial Bold; on Linux without Arial (`ttf-mscorefonts-installer` unavailable), use metric-compatible Liberation Sans Bold and note the substitute in the delivery note.

Code fragment (pytoshop; `flat` / `labels` / each panel = full-canvas PIL RGBA):

```python
from pytoshop import enums, image_resources as ir
from pytoshop.user import nested_layers as nl
from pytoshop.image_data import ImageData
import numpy as np, struct
def lay(name, img):
    a = np.asarray(img.convert("RGBA"))
    return nl.Image(name=name, visible=True, opacity=255,
                    channels={0: a[..., 0], 1: a[..., 1], 2: a[..., 2], -1: a[..., 3]})
layers = [lay("Labels", labels)] + [lay(f"Panel {L}", p) for L, p in reversed(panels)] + [lay("Background", bg)]
psd = nl.nested_layers_to_psd(layers, color_mode=enums.ColorMode.rgb,
                              size=(W, H), compression=enums.Compression.raw)   # width first!
psd.image_resources.blocks.append(ir.GenericImageResourceBlock(
    resource_id=1005, data=struct.pack(">IHHIHH", 300 << 16, 1, 2, 300 << 16, 1, 2)))
psd.image_data = ImageData(channels=np.asarray(flat.convert("RGB")).transpose(2, 0, 1).copy(),
                           compression=enums.Compression.raw)                # flattened composite
```
