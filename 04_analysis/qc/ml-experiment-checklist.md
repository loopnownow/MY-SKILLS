# ML experiment checklist (04 qc — standards only)

**Owner:** `00_orchestrator` at Gate → 04 / G-04 when the analysis is an ML / ablation / benchmark packet.
**Domain gate:** Use when the project trains or compares models (radiomics ML, deep learning, classical ML). **NOT_APPLICABLE** for pure biostat / nomogram-only RAD runs without model ablations.
**Distill of:** aiming-lab/AutoResearchClaw `experimental-design` + short `hypothesis-formulation` axes (MIT). Host-agnostic pass/fail only — **no** AutoResearchClaw pipeline / MCP / 23-stage runtime.

## Soft vs hard

| Mode | Behavior |
|---|---|
| Soft (default) | Word / HTML comment with edit plan; local rework at 04 |
| HARD compose | Open central claim fail → compose with **G-FACT** / **G-04** before next node |

## Must-check (ML-ED)

| Id | Check | Fail → |
|---|---|---|
| ML-ED-1 | Meaningful baselines present (not random-only): ≥1 classical **and** ≥1 recent/simple-strong baseline when claim is SOTA-style | 04 |
| ML-ED-2 | Multiple seeds (min 3 preferred); report mean ± SD (or justify single-seed) | 04 |
| ML-ED-3 | Ablations isolate **one** component at a time; each ablation differs meaningfully from baseline | 04 |
| ML-ED-4 | Train / val / test (or named analysis sets) stated; never evaluate on training data as test | 04 / G-FACT |
| ML-ED-5 | Primary metric + uncertainty (CI or seed spread); wall-clock / memory reported when resource claims appear | 04 |

## Hypothesis soft-check (when hypotheses are stated)

| Id | Check | Fail → |
|---|---|---|
| ML-H-1 | Hypothesis is specific and falsifiable (outcome that would refute it is named) | 04 / 03 |
| ML-H-2 | Confirmatory vs exploratory analyses distinguished | 04 / 05 |

## Six-state emit (when assurance ≥ polished)

`PASS | WARN | FAIL | BLOCKED | NOT_APPLICABLE | ERROR` — silent skip forbidden at `submission`.

**PASS:** ML-ED-1–5 clean or commented; ML-H when hypotheses present.
**FAIL:** training-as-test, missing primary split, or central ablation claim without control → rollback **04**.

*Attribution: AutoResearchClaw builtin experiment skills (MIT); lab G-04 / G-FACT remain authoritative.*
