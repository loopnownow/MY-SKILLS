# Restore subject-level data from summary tables (synthetic reconstruction)

Advanced layer page for `02_data-processing` (proposed 2026-11-11; no new fine id — an advanced reference page, routed from `clean-data`).
Code: `{code_root}\tools\restore-from-summary\` (`restore_raw.py`, `smoke_test.py`).
First use: `re.xlsx` (mT2 / mT1 / mFA / mADC / GA / SINBAD / Age / BMI; n = 56: Pos 23 / Neg 13 / Ctrl 20; Sheet1 = 51-person subset).

## When it applies

- A source table reports only aggregate statistics — n, mean (SD), AUC, sensitivity, specificity, P, r — and downstream work needs **subject-level rows** (pooled re-analysis, re-plotting, sensitivity checks, power simulation).
- The reconstruction is **SYNTHETIC by construction**: it reproduces the reported summary statistics, not the measurements. Every output row must carry `SYNTHETIC=1`, and the workbook must say in plain words that it is not real measurement.

## When it does not apply

- Real table cleaning / cohort assembly → `02_data-processing/base/clean-data/`.
- Test selection, assumptions, DeLong intervals → `02_data-processing/base/stats-analysis/`.
- Predicting what a *new* study would show (that is sample-size / simulation) → `calc-sample-size`.
- Reported-number consistency in a manuscript → `02_data-processing/qc/report-checks.md`; prose claims → 05.

## Three-tier match contract (owner ruling 2026-11-11)

| Tier | Target | Rule |
|---|---|---|
| **A** | n / mean / SD | reproduce the **display precision** of the source table (1 dp → `round(mean, 1)` equals the printed value); do not chase hidden precision |
| **B** | AUC / sens / spec | hit the nearest **mathematically attainable** value: AUC ∈ k/(nA·nB), sens/spec ∈ k/n; report the residue, never dress it as a hit |
| **C** | P | fixed by the locked moments; compute parametric **and** non-parametric (Welch / pooled / Mann-Whitney; ANOVA / Kruskal-Wallis), report all; a threshold target (`<0.001`) is judged HIT/MISS, an exact target is only REPORTed |

## Pipeline

1. **Moment construction.** Subset ⊂ full cohort is solved with the sum-of-squares identity `SS_F = SS_S + SS_C`; a ±half-display-unit window grid (step 0.01) searches a feasible decomposition. Ordinal scores (SINBAD-type) are enumerated as integer count vectors with pruning, then shuffled.
2. **ROC shape tuning.** Moment-preserving shape transform `z + a(z²−1) + b(z³−3z)/3`, re-standardized each step; `scipy.optimize.minimize` (Powell) under logistic annealing (τ 0.5 → 0.2 → 0.08) plus random restarts.
3. **Moment-preserving repair.** Three-point move (δ, ε, ζ) with `Σx` and `Σx²` both conserved (ε from a quadratic), annealing then hill-climb, best snapshot restored.
4. **Correlation pairing.** Within-group swaps only — marginals unchanged, so moments / AUC / counts cannot move; annealing + greedy polish; convergence judged by **per-item max |Δr|**, not the summed loss.
5. **Land at simulation precision → micro-repair → correlation → land at table precision → verify twice.** Individuals are rounded to SIM_DP, critical values nudged so no count flips, within-group swaps then set the correlations, and RawData is written at LAND_DP while Verify keeps both the simulation-precision rows and the `*-landed` recomputation.

## Hard rules and known traps

- **Two precisions, both read off the table.** *Simulation precision* — 4 decimals for variables that carry AUC/CI targets (the reported AUC is 3 dp, but the attainable grid is k/(nA·nB), so the search needs finer values); every other variable uses the **SD's** decimals (age 71.2(8.4) → 1 dp). *Landing precision* — the **mean's** decimals: mT2 90.4 → 1 dp, mFA 0.418 → 3 dp, ordinal scores integer. RawData is written at landing precision; never a blanket 4 dp (owner ruling 2026-11-11: 模拟精度…落盘…与表格一致).
- **Verify both levels.** Rows at simulation precision say what the paper's table is matched against; `*-landed` rows recompute the same statistics on the written values. Any difference is `DRIFT` (e.g. one sensitivity count stepping over the cut at 1 dp) — report it, never hide it behind a formatting trick.
- **Rounding must be repaired, not hoped away.** If the search runs on continuous values and rounds afterwards, a pre-round hit flips. Observed once: mADC Neg vs Ctrl sensitivity 9/13 → 10/13 because one critical value crossed the cut. Fix by nudging only the critical values (&#124;value − cut&#124; ≤ a few units in the last simulated place) with a moment-preserving three-point move, accepting only moves that keep the displayed moments and lower the discrete loss (2026-11-11).
- **ROC granularity ceiling.** With nA·nB pairs and n per group, most printed AUC/sens/spec are unreachable (e.g. AUC 0.948 in 19×12 → 216/228 = 0.9474; sens 0.889 in 19 → 17/19 = 0.895). Take the nearest attainable value and label it `UNREACHABLE-*` in the README sheet.
- **Cross-table incompatibility is a finding, not a bug.** If a subset row and its full-cohort row cannot both hold inside the display-rounding window (observed: age|Negative 63.1(12.9) n=12 ⊂ 63.6(11.5) n=13 needs SD ≈ 12.48), keep the subset exact, take the identity-implied full-cohort SD, and mark `INCOMPATIBLE` with the arithmetic shown.
- **P cannot be tuned once moments are locked.** Report the computed values (a `MISS` on an exact P target is expected, e.g. target `<0.0001` vs computed 0.0001).
- **No fallbacks, no silent degradation.** Infeasible targets raise or land in the Verify sheet with a status; never substitute a default path.
- **Determinism.** Fixed `SEED`; record it in the workbook. CPU only — n ≤ 56, ~3k flops per loss evaluation, GPU adds dependency with zero gain. Full run ≈ 12 min on one core.
- **Anchors before execution.** Assert that transcribed source strings/numbers actually occur in the source file (guards manual transcription error).

## Output contract

- `RawData`: one row per subject; `subject_id` synthetic, `group`, `in_subset_S`, canonical units, `SYNTHETIC=1`; values are written at **landing precision** (mean's decimals) and the cell number formats follow the same rule.
- `Verify`: one row per checked quantity with `block / item / target / achieved / delta / status / note`; statuses `EXACT` `HIT` `NEAREST` `REPORT` `MISS` `DRIFT` `INCOMPATIBLE` (`DRIFT` = landed-value recomputation differs from the simulation-precision row).
- `README`: purpose, source path, seed, cohort definition, precision, assumptions, method, P policy, `UNREACHABLE-*` and `INCOMPATIBLE:*` lines.

## Related

- Rounding of individual values and display-precision reporting → `02_data-processing/qc/report-checks.md`.
- Method-validation gate for any downstream statistic computed on reconstructed rows → `02_data-processing/qc/method-validation-gate.md`.
- Figure panels built on reconstructed data keep the `SYNTHETIC` statement → `02_data-processing/base/plot-figures/references/figure-set-consistency.md`.
