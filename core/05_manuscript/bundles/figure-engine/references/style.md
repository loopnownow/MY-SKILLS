# STROBE / patient-analysis flowchart — visual spec

Single home for **how the boxes look**. When to insert the figure: `Aitor-format.md`.

## Layout (top → bottom)

1. Screened / identified cohort (only if *n* or the screening sentence exists).
2. Right-hand **Exclusion criteria** box; horizontal arrow **out of** the spine.
3. Analyzed / included *n*.
4. Optional split: development | validation (or training | test), using written sizes.
5. From the two split boxes: vertical stems down to a **plain bar** (no arrowheads on the bar), then **one vertical arrow** from the bar midpoint onto the top of the first analysis box.
6. Analysis row: imaging → processing / feature extraction → model and statistics, boxes linked left to right.

Do **not** draw an Inclusion criteria box. Do **not** leave Development / Validation hanging.

## Geometry

- Main spine left-of-center; exclusion sits in the right column, vertically centered on the stem between screened and analyzed (do not push analyzed below the whole exclusion stack).
- All boxes use the same 1 pt black rule and regular (not bold) type. Box width and height follow the text.
- Development / Validation stay on one line when possible; equal height.
- Analysis boxes in one row under the split, equal height, linked left to right.
- Arial (or Calibri / DejaVu Sans). No fill, no grey, no rounded corners.

## Text

- English for English SCI papers.
- Exclusion lines copied from Methods; trim only length, not meaning. No inclusion list.
- Split labels include `n =`.
- No *P*, AUC, or ethics identifiers inside boxes.

## Export

- PNG, 300 dpi; optional PDF/SVG if the caller asks.
- Width on the page: 16 cm.
- Do not center the Word legend.
