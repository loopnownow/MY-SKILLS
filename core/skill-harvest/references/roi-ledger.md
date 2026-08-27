# Skill ROI ledger

The ledger is an evidence store, not a usage counter. Do not fabricate events. Record only observable task-level evidence.

## Event fields

| Field | Meaning | Allowed / example |
|---|---|---|
| `date` | Event date | `2026-08-25` |
| `skill` | Top-level owner | `05_manuscript` |
| `mode` | Bundle/mode | `manuscript-core` |
| `task_id` | Local task identifier | `paper-2026-08-25-01` |
| `outcome` | Final task outcome | `success`, `partial`, `failed` |
| `correction` | Substantive user correction | `0`, `1` |
| `rework` | Repeated execution attributable to Skill | `0`, `1` |
| `routing_ok` | Correct owner/mode | `0`, `1` |
| `turns` | Approximate interaction turns | integer |
| `context_cost` | Relative loaded-context burden | `0–3` |
| `benefit_note` | Short evidence note | concrete, task-specific |

## Interpretation

Do not promote a rule from E0 merely because it sounds useful.

- E0: expected benefit only.
- E1: one observed task.
- E2: ≥3 independent uses or repeated failure prevention.
- E3: comparable before/after improvement.
- E4: benchmark/test-backed improvement.

A high score with E0 evidence is a **candidate**, not a proven improvement.

## ROI decision

For each mode, inspect: success rate, correction rate, rework rate, routing accuracy, median turns, and context burden. Prefer a smaller Skill when two alternatives provide comparable outcomes.

Suggested action:

`KEEP` → repeated positive evidence; `OBSERVE` → insufficient evidence; `SIMPLIFY` → benefit exists but context/maintenance is excessive; `MERGE` → overlapping mode; `ARCHIVE` → no meaningful reuse; `ROLLBACK` → measurable regression.
