# IMRAD section contract

Companion to [MODULE.md](../MODULE.md). Generic scientific IMRAD — not a personal house format.

Language polish → `humanize`. Venue / house style → this pack (`05_manuscript/base/write-paper/radiology-writing/journal-family-writing-style.md`, `radiology-polishing/`).
Reporting checklists → `check-reporting`. Self-audit → `self-review`.

## Section jobs

| Section | Job |
|---------|-----|
| Title | Study design + population + endpoint; no result dump |
| Abstract | Structured if the venue wants it; every number must exist in Results |
| Introduction | Stakes → prior tools → gap → purpose. No current-study AUC |
| Methods | Reproducible order (see `methods_template_export.md`); citations only where the field expects them |
| Results | Cohort flow, then primary endpoint with CI, then secondary; no methods rerun |
| Discussion | What the result means, comparators, limitations, bounded clinical implication |
| Conclusion | One claim the data support |

## Honesty

- Do not invent n, AUC, ethics IDs, or unrun experiments.
- Dual-set metrics: training fit / test evaluate. A validation set is an **external** cohort.
- Figures: STROBE flow → `draw-flowchart`; statistical plots → `plot-figures`.
