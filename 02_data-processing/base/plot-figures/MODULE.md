---
name: "plot-figures"
domain: "02_data-processing"
trigger: ["作图", "ROC图", "校准", "DCA图", "Kaplan-Meier"]
inputs: ["results_tables", "png_from_pipeline"]
outputs: ["publication_figure", "legend"]
tools: ["matplotlib", "palette"]
quality_control: "CI and n match supplied results; colorblind-safe"
owner: "02_data-processing/base/plot-figures/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Statistical and imaging-panel figures

Contract only for plot-figures: scope, bans, phase names, and pointers. The recipe and the revision authority live in `02_data-processing/advanced/analysis/plot-figures-digest.md`; pack data (`references/`, `scripts/`) stays beside it as data.

Build plots that pass a technical bar: vector-first export, legible type, color-blind-safe
palettes, honest axes, and the chart types imaging-AI reviewers expect (ROC, calibration,
decision-curve, forest/SROC, Kaplan-Meier, Bland-Altman), plus **de-identified** annotated
imaging panels.

**STROBE / patient-selection Figure 1 belongs in `draw-flowchart`**, not here.

## Core stance

- **Vector first.** Primary `.svg` (or `.pdf`); secondary ≥ 300 dpi raster. Keep text as text.
- **One figure, one message.** Panels labelled A, B, C or a, b, c — venue-dependent, never mixed.
- **Honest graphics.** Don't truncate axes to exaggerate; show uncertainty; state n.
- **De-identify every image.** No PHI; report windowing; scale bar where size matters.
- **Never fabricate data.** Plot only supplied/loaded values; mark example data.

## When to use

- Statistical figures: ROC, calibration, DCA, forest, SROC, KM, Bland-Altman, box/violin, heatmaps.
- Imaging panels: montages, arrows/insets, windowing labels.
- **Not** enrolment flowcharts — those are `draw-flowchart`.

## When to open extra files

| File | Open when |
|---|---|
| [references/radiology-figure-guidelines.md](references/radiology-figure-guidelines.md) | Format, resolution, size, fonts, colour, de-identification |
| [references/chart-types.md](references/chart-types.md) | Choosing ROC / calibration / DCA / forest / KM / Bland-Altman |
| [references/imaging-panels.md](references/imaging-panels.md) | Montages, windowing, arrows, scale bars |
| [references/api.md](references/api.md) | matplotlib preamble, palette helpers |
| [references/design-theory.md](references/design-theory.md) | Typography, grid, colour-blind palettes |
| [references/color-systems.md](references/color-systems.md) | One palette (Okabe-Ito / NPG / Morandi) mapped to meaning |
| [references/lab-palettes.md](references/lab-palettes.md) | Lab console sets: 20 `FIG_PALETTE` palettes, hex SSOT in `style.py` |
| [references/survival-figures.md](references/survival-figures.md) | KM integrity, numbers-at-risk, time-dependent ROC |
| [references/figure-set-consistency.md](references/figure-set-consistency.md) | Unify palette/fonts across the set |
| [references/nature-figure-spec.md](references/nature-figure-spec.md) | Nature-portfolio column widths, lowercase panels |
| [references/figure-intent-and-render-qa.md](references/figure-intent-and-render-qa.md) | Full-set planning and render QA |
| [references/journal-family-visual-style.md](references/journal-family-visual-style.md) | Family visual taste |
| [references/plot_types.md](references/plot_types.md) | Generic plot catalogue |
| [references/common_issues.md](references/common_issues.md) | Frequent render bugs |
| [references/figure-asset-package.md](references/figure-asset-package.md) | Shipping a figure set: final vs raw library, inventory sheet, gaps and suspect files |

Patient-flow / STROBE / study-workflow / methods-pipeline cartoons → `../draw-flowchart/`.

## Workflow

0. Confirm the target venue before sizing (column widths and panel-letter case differ).
1. For full sets, open `figure-intent-and-render-qa.md` and build the intent table.
2. Pick the chart for the message (`chart-types.md`). Patient selection → `draw-flowchart`.
3. Start the script with the rcParams preamble (`api.md`).
4. Build panels; add CI, n, units; label via helpers — never hardcode `chr(65+i)` per script.
5. Imaging panels: de-identify, windowing, scale bar.
6. Export `.svg` (text-as-text) **and** a 300-600 dpi raster.
7. QA at final print width.
8. Package the set (`references/figure-asset-package.md`): final vs raw two layers, inventory sheet,
   explicit gaps and suspect files.

## Output contract

1. Figure plan — what each panel shows.
2. Script — runnable `.py` with real vs example data marked.
3. Files — `figure.svg` + ≥ 300 dpi raster.
4. QA notes — fonts as text, colour-blind check, n shown, de-identification.
5. Asset package — final files in `01_终版/`, one junction per figure into `02_原始库/`, inventory
   sheet (figure | dir | files | size | confidence | text match), gaps `⚠ 缺` and `[可疑]` rows
   visible.

## Panel stitching (train + external validation)

- Assemble panels with the helpers, never ad hoc: `{code_stats}\modules\stats\figure_panels.py`
  (`stitch_row` / `stitch_grid` / `stitch_plain` / `stitch_train_ext`). Gap, panel-letter position and
  DPI come from `FIGURE_PANEL_*` settings, not from literals in the calling script.
- **Derivation + external validation is one standard figure**: `stitch_train_ext()` runs at the end of
  `build_outcome_panels()` and writes `panel_<kind>_train_ext.png` (A = derivation, B = external; more
  external cohorts extend the letters). Do not hand-stitch that pair.
- **No in-figure titles by default** (`FIGURE_PANEL_TITLES=False`): ROC, calibration, DCA and the
  nomogram carry no title, so cohort tokens (`train`, `ext_Validation`) never reach the artwork. Cohort
  name, n and events belong in the caption; `true` restores the old behaviour.
- Every panel must state **n and events** in the caption, and DeLong P values must be attributed to the
  panel's own cohort (derivation and external P values are not interchangeable).
- Verify before shipping: aspect ratio of the placed image must equal the file's (≤1% drift), and the
  figure lock (`hashes.tsv` equivalent) must be recomputed. A one-command gate lives in the project
  (`ref/code-gates/check_figure_swap.py` for zyj_OV); replicate rather than eyeball.

## Handoffs

- Statistic behind the plot → `stats-analysis` / `model-evaluation`
- Checklist item (STROBE flow) → `draw-flowchart` and `05_manuscript/qc/check-reporting/`
- Captions / display-item plan → `write-paper` (`05_manuscript/base/write-paper/radiology-writing/nature-family-shape.md`)
- Harsh read before submission → `self-review`

Principles extracted from cross-package research (not a fine id; rule reference only): [external-principles.md](references/external-principles.md)

## On-demand references

| File | Open when |
|---|---|
| `references/radiology-figures.md` | Radiology-family figure conventions (panel labels, size, legends); pair with `references/nature-figure-spec.md` when the target is a Nature-portfolio venue |
