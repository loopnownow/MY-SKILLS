# Skill Benefit Metrics

## Principle
Measure whether a Skill change improves real work. Usage alone is not benefit.

## Core metrics

| Metric | Meaning | Preferred direction |
|---|---|---|
| Reuse | Number of independent tasks using the rule | ↑ |
| Success | Tasks completed without substantive correction | ↑ |
| Correction rate | User edits/overrides attributable to the Skill | ↓ |
| Rework | Repeated execution caused by Skill failure | ↓ |
| Time/turns | Interaction cost for equivalent work | ↓ |
| Routing accuracy | Correct Skill selected for the intent | ↑ |
| Context cost | Added tokens/files loaded per task | ↓ unless justified |
| Downstream utility | Whether output remains useful in later workflow stages | ↑ |

## Evidence levels

### E0 — Hypothesis
Expected benefit only. No observed use yet.

### E1 — Single-use signal
One real task suggests improvement. Keep under observation.

### E2 — Repeated-use evidence
At least 3 independent uses or repeated failure prevention. Suitable for keeping as a stable rule.

### E3 — Measured improvement
Comparable before/after evidence shows lower correction/rework/time or higher success/routing accuracy.

### E4 — Benchmark-backed
Automated benchmark or test suite demonstrates the improvement and guards against regression.

## Practical score

For prioritization, assign 0–3 to each:

- impact: 0 none, 1 minor, 2 meaningful, 3 major
- frequency: 0 rare, 1 occasional, 2 repeated, 3 frequent
- reliability gain: 0 none, 1 plausible, 2 observed, 3 demonstrated
- reuse potential: 0 project-only, 1 narrow, 2 cross-project, 3 broad
- maintenance cost: 0 trivial, 1 low, 2 moderate, 3 high
- context cost: 0 none, 1 low, 2 moderate, 3 high

Priority score = impact + frequency + reliability gain + reuse potential - maintenance cost - context cost.

Interpretation:

- ≥6: prioritize / retain
- 3–5: retain if evidence continues
- 0–2: observe, simplify, or archive
- <0: revise or rollback

This score is a prioritization aid, not a scientific effect estimate.

## ROI ledger and anti-bloat

Use `data/roi-ledger.csv` as the only local evidence ledger. Do not backfill invented usage. One row = one observable task outcome.

Before promoting a new mode, require either ≥3 independent positive uses, a reproducible failure prevented by the rule, or a defined workflow requirement. If context cost rises while success/correction metrics do not improve, prefer `SIMPLIFY`, `MERGE`, or `ARCHIVE` (`keep-merge-delete.md`).

The repository should optimize for **benefit per context cost**, not file count or text volume.

## Scripts

| Script | When |
|---|---|
| `scripts/harvest_score.py` | `keep-update` / `keep-new-mode` only; skip for typos / pointer-only |
| `scripts/harvest_record.py` | append observable task evidence |
| `scripts/harvest_report.py` | summarize recorded evidence |

Default decision after observation:

```text
benefit demonstrated + no material boundary regression → keep
benefit uncertain → observe / revise only if the problem recurs
benefit negative or scope leakage → revise or rollback
```

Do not optimize for usage count alone.
