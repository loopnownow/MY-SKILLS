# 02_data-processing personal route -- top layer

## Top-layer flow (2026-10-17)

1. **base first-pass** stats/figures fine-IDs (`analyze-stats`, `calc-sample-size`, `model-evaluation`, `draw-flowchart`, `plot-figures`, ...)
2. **00 QC** (G-FACT / G-STATS)
3. **02 re-loop** -- personal lab pipeline / report-checks / figures; may re-trigger base mounts when 00 says needed

Fine IDs for stats-analysis / figures are **not** renamed.

Algorithm library entity = `{code_stats}` (`0doc\_code\04-analysis\stats-analysis`). Do **not** split the `modules` package out of that tree (`{code_modules}` stays inside `{code_stats}`). Not under `base\analyze-stats\`.

**Number conflict:** `Results*.html` wins over a companion `.xlsx`. Flag both loci; the workbook does not override the HTML. Detail: `console-ui.md` §6.


## Standing thin digests (2026-10-24)

Stats fine-IDs (norms / hard constraints / path pointers only; detail stays in methods/pipeline):

- `analyze-stats` → `analyze-stats-digest.md` (Table 1 / DeLong-as-p / type-inference)
- `model-evaluation` → `model-evaluation-digest.md` (panel order / VIF scope / leakage)
- `calc-sample-size` → `calc-sample-size-digest.md` (ban a-priori-not-performed / no derivation-as-results)

Figure digests (already wired from `figures.md`): `draw-flowchart-digest.md`, `plot-figures-digest.md`.


## Personal load order

1. Methods / which test -> `methods.md` (index: `module-notes.md`)
2. Already-reported numbers / polish checks -> `../../qc/report-checks.md`
3. Pipeline implementation rules -> `pipeline.md`
4. Console UI / results HTML -> `console-ui.md`
5. Figures (palette + claim plan) -> `figures.md`
6. Cooperation -> `handoff.md`
