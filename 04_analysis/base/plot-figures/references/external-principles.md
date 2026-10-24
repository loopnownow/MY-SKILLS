# External principles for figure production

File role: rule reference (not a mount).
Purpose: record design principles found in cross-package research that are worth borrowing
without mounting the whole package. Stack these as gate rules on top of the fig-plot
(make-figures) flow; do not call any external package.
Source: Scientific (K-Dense) scientific-visualization SKILL.md
Extracted: 2026-09-13

# External principle reference for figure production

This file is not a standalone skill. It holds two gate rules extracted from external-package
research and stacked onto this skill's (fig-plot) figure flow. When producing figures, after
the charts are done and before delivery, self-check against both rules below.

## Principle 1: Honest encoding is non-negotiable (from Scientific scientific-visualization)

Self-check before and after plotting. Any fail means the figure is unfit and must be redone:

- Do not truncate axes to exaggerate differences (especially bar-chart y-axis origins)
- Do not use misleading dual-y scales to invent a false correlation
- Prefer bar charts (or other easy-to-read forms) over area/angle encodings (pie, bubble)
- Color maps must be color-blind friendly; color alone must not carry the only categorical cue
- Define error bars / CIs in the legend (SD vs SEM vs CI)

## Principle 2: Pre-submission reviewer-risk preview (from Nature nature-figure)

After figures are done and before formal delivery, walk each figure from a reviewer viewpoint:

1. What is this figure most likely to be challenged on? (e.g. sample size shown, survivor-bias
   case picking, whether the statistical test matches the chart type)
2. If a sensitivity analysis or subgroup split is requested, can current data/code respond fast?
3. Can the legend stand alone so a reviewer need not flip back to Methods?

If a figure is clearly weak on these three points, fix it during figure generation — do not wait
for reviewer comments.
