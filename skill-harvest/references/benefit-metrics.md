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
