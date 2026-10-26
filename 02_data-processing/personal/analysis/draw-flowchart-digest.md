# draw-flowchart — thin standing digest (2026-10-24)

Corpus proposal source: Downloads `Grok会话-技能草案-20261024.md` → archived under `{doc_root}\skill-harvest\`. **Not** a new registry fine-id. Cap stays in-repo `base/draw-flowchart`.

## elements
- Figure 1 = enrollment / selection flow only (screen → include/exclude → enrolled → Training | Validation).
- Generate via `modules/` py (or skill scripts); do not hand-drag final art.
- Look: white fill, black 1 pt rules, square corners; box size follows text.

## process
- Structure first (boxes, levels, edges), then type size / whitespace.
- Exclusion reasons + counts per step; branch sums must equal upstream n.
- Export **PDF preferred**; font **Arial** 12 (figure dual-track).

## cautions
- Do not bold the enrolled-n box; do not restack inclusion criteria as a second figure.
- Development/Validation (or Training/Test) must connect with edges to children.
- Re-run script after data change; do not hand-edit the PDF/PNG as SSOT.
- Detail SSOT: `02_data-processing/base/draw-flowchart/references/style.md` + `05_manuscript/personal/Aitor-format.md` Figures.
