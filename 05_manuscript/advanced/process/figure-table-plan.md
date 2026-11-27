# Figure and table plan (display needs, not production)

**Owner:** `05_manuscript` advanced, on the existing writing route (`05_manuscript/advanced/route.md`).
**Not a QC gate**, and not a new form, scorecard, second router, or fine id.

## Purpose

After the Claim Map exists, decide which main-text figures and tables are actually needed, and **why** (which claim or question each display carries). This is a light planning note, not a production specification and not a completeness audit.

## Seat split

- **05** decides why a display is needed and which claim it serves, then writes the caption and the body callout.
- **02** generates the display from the locked data and statistical plan (`plot-figures`, `draw-flowchart`, and `02_data-processing/advanced/analysis/figures.md`). 05 does not copy those production rules here, and it does not redraw the figure pack.

## When to load

Load this file after `05_manuscript/advanced/process/study-type.md` and `05_manuscript/advanced/process/claim-map.md`, before asking 02 to generate or regenerate a main-text display. Revisit a row only if a load-bearing claim or a supplied result file changes.

## Fields (keep light)

One short row per planned main-text figure or table. Leave a cell blank when it does not apply. Do not turn this into a heavy template.

```text
ID | Serves claim | Data source | Analysis set / n | Statistical method | Display type | Manuscript role | Status
```

| Field | What to record |
|---|---|
| ID | Working label (Fig 1, Table 1, …) |
| Serves claim | The Claim Map label (C1, C2, …) or the research question this display carries |
| Data source | Named table, `*-results.html`, or 02 handoff; never an invented file |
| Analysis set / n | The locked analysis population and its n, if already supplied |
| Statistical method | The method already in the locked plan (not a new analysis) |
| Display type | Table, scatter, ROC, calibration, forest, flow, or another type that fits the data and the statistical aim |
| Manuscript role | Main text, supplement, or dropped |
| Status | planned / awaiting data / generated / checked against source |

Status `awaiting data` means the display is needed but the real output is not in hand. It is a comment (author **A**), not a licence to invent numbers.

## Hard constraints

1. Every main-text figure or table must state the claim or research question it carries. If none can be named, drop the display or move it out of the main text.
2. Do not repeat the same information without purpose across prose, a table, and a figure.
3. If the real data are not available, mark the row `awaiting data`. Do not simulate results to fill the formal manuscript.
4. Numbers, grouping, and methods on the planned display must match the analysis output. Do not tidy a value to make the claim look cleaner.
5. At the planning stage, do not change primary or secondary endpoints, and do not add an analysis that was not in the locked plan, just to fill a slot.
6. Choose the display type from the data type and the statistical aim, not from how elaborate the figure would look.
7. Do not invent results, sample sizes, or graphics. Do not override a user-locked design or statistical plan.

## Call graph

| Direction | File | Role |
|---|---|---|
| Upstream | `05_manuscript/advanced/process/claim-map.md` | Which claims need a visible display; do not copy that map here |
| Entry | `05_manuscript/base/write-paper/MODULE.md` | Load this plan after the Claim Map, before a 02 display request |
| Production | `02_data-processing` (`plot-figures` / `draw-flowchart`) | How to generate the display correctly from the data |
| Later QC | `05_manuscript/qc/figure-qa-minima.md`, `figure-stats-legend.md`, `claim-number-align.md` | Legend, number, and callout checks after the display exists; this file does not emit those verdicts |

Study-type wording constraints stay in `05_manuscript/advanced/process/study-type.md`. This plan does not restack those rules.

## Out of scope

- Style metrics, method-experiment alignment, or an intake brief
- New fine ids, new gates, or a parallel 05 router
- Changing 00 gate composition or editing 02 production rules
- A required catalogue of “must-have” figures for each study type

*Thin lab rewrite, 2026-11-27, on display planning (why a figure or table is needed, not how to draw it). Method reference: [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill). See `NOTICE`.*
