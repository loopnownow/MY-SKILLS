# 04_analysis personal route -- top layer

## A/B flow (2026-10-17)

1. **base first-pass** stats/figures fine-IDs (`analyze-stats`, `calc-sample-size`, `model-evaluation`, `draw-flowchart`, `plot-figures`, ...)
2. **00 QC** (G-FACT / G-04)
3. **A04 re-loop** -- personal 0RAD pipeline / report-checks / figures; may re-trigger base mounts when 00 says needed

Fine IDs for stats-analysis / figures are **not** renamed.

Algorithm library entity = `{code_stats}` (not under `base\analyze-stats\`).


## Standing thin digests (2026-10-24)

Stats fine-IDs (norms / hard constraints / path pointers only; detail stays in methods/pipeline):

- nalyze-stats → nalyze-stats-digest.md (Table 1 / DeLong-as-p / type-inference)
- model-evaluation → model-evaluation-digest.md (panel order / VIF scope / leakage)
- calc-sample-size → calc-sample-size-digest.md (ban a-priori-not-performed / no derivation-as-results)

Figure digests (already wired from igures.md): draw-flowchart-digest.md, plot-figures-digest.md.


## Personal load order

1. Methods / which test -> `methods.md` (index: `module-notes.md`)
2. Already-reported numbers / polish checks -> `../qc/report-checks.md`
3. Pipeline implementation rules -> `pipeline.md`
4. Console UI / results HTML -> `console-ui.md`
5. Figures (palette + claim plan) -> `figures.md`
6. Cooperation -> `handoff.md`
