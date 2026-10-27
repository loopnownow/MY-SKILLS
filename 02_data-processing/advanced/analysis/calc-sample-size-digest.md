# calc-sample-size — thin standing digest (2026-10-24)

Bank proposal source: Downloads `Grok会话-技能草案-20261024.md` → `{doc_root}\skill-harvest\by-fine-id\`. Cap stays `base/calc-sample-size`. Lab detail SSOT: `methods.md` § Sample size & power; generic formulas in `base/calc-sample-size/references/effect_sizes_and_power.md`.

## elements
- **Inputs for prediction models:** development n, event rate / outcome proportion, candidate variable count.
- **Caliber:** events-per-variable (EPV, aim ≥10–15) and/or Riley / `pmsampsize` when the journal expects a minimum n; classical two-group formulas do **not** cover multivariable / radiomics models.
- Fixed retrospective N → use pre-study power, EPV/Riley, MDES at 80%, or precision (CI half-width) — **not** observed / post-hoc power from the obtained p.

## process
- Compute first, then write: Methods states which of the four approaches and the inputs; do not invent n / effect / power in prose.
- Cross-check reported n against Results denominators.
- Imaging: do not equate slice/image count with independent sample size.

## cautions
- **Ban:** `A formal a priori sample-size calculation was not performed.`
- Do not present the derivation trail as Results (2026-08-15 · 01a002c1).
- Do not answer a reviewer post-hoc-power ask with observed power; offer CI width or MDES vs a clinical difference (Hoenig & Heisey 2001). Detail: `methods.md` § Sample size & power.
