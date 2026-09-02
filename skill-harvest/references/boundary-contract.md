# Skill Boundary Contract

## Purpose
Prevent skill sprawl, overlapping triggers, duplicated knowledge, and domain leakage.

## Boundary dimensions

For every Skill, define:

| Dimension | Required question |
|---|---|
| Trigger | What user intent activates it? |
| Non-trigger | What similar intent must not activate it? |
| Owner | Which Skill is authoritative for the task? |
| Inputs | What information must be present? |
| Outputs | What artifact/result does it own? |
| Dependencies | Which tools, references, or Skills may it call? |
| Exclusions | What is explicitly outside scope? |
| Promotion rule | When does a repeated mode deserve extraction? |

## Boundary tests

Reject a new Skill/module if any of the following is true:

1. It differs from an existing mode only by a keyword, disease, package, or statistical metric.
2. It duplicates an existing reference without a substantive new decision rule.
3. It exists only for one temporary project.
4. Its trigger overlaps an existing Skill and there is no routing rule.
5. Its value comes primarily from deterministic execution that should be a tool.
6. It is a multi-step cross-domain procedure that should be a workflow.

## Promotion thresholds

A recurring capability can be promoted from chat pattern → mode/module when at least one is true:

- repeated in ≥3 independent tasks;
- causes a reproducible failure that a persistent rule can prevent;
- has a stable trigger and stable output;
- materially reduces repeated user correction;
- is required by a defined workflow.

Top-level promotion is prohibited unless the architecture owner explicitly changes the 00–06 boundary.
