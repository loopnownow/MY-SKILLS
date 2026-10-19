# Figure QA minima (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06.
**Distill of:** Yuan1z `nature-figure` → `qa-contract` pre-submission + image-integrity + stats-legend minima (Apache-2.0). Short pass/fail only; no gallery/scripts.

## Pre-submission (pass/fail)

| id | Check | Fail → |
|---|---|---|
| FQ-1 | Every panel maps to a one-sentence core claim (or marked supplementary) | 05 |
| FQ-2 | Final width/height within target venue limits; text readable at print size | 05 |
| FQ-3 | Panel labels present and consistent; color not red/green-only; grayscale still interpretable | 05 |
| FQ-4 | Quantitative panels meet `figure-stats-legend.md` minima | 05 / 04 |
| FQ-5 | Source data or script path traceable for quantitative panels | 04 / 05 |
| FQ-6 | Microscopy/blot: calibrated scale bar (not magnification alone) when applicable | 05 |

## Image-integrity minima

| id | Check | Fail → |
|---|---|---|
| II-1 | Crop / contrast / gamma / pseudo-color / stitching recorded when applied | 05 |
| II-2 | No unexplained panel reuse across figures; reuse disclosed if intentional | 05 / ethics |
| II-3 | Global adjustments preferred; selective local edits that hide background/bands → FAIL | 05 |
| II-4 | Raw ↔ processed link available or Word-commented as author input needed | 05 / user |

**PASS:** FQ-* + applicable II-* clean or commented.
**FAIL:** missing integrity disclosure on image panels, or claim panels without legend minima → rollback **05**.

*Attribution: distilled from Yuan1z0825/nature-skills `nature-figure` (Apache-2.0).*
