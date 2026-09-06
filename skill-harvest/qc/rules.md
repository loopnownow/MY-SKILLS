# Harvest-QC rules

## Event schema (`data/qc-events/YYYY-MM-DD-<short>.yaml`)

```yaml
id: QC-20260906-001
when: "2026-09-06T13:00:00+08:00"
gate: G-FACT   # or G0 / G-04 / G-05 / G-06 / G-LIT / BOUNDARY / other
status: FAIL   # PASS | FAIL | UNKNOWN
error_type: fact-drift-auc
responsible_node: "05"   # 00–06 or 01
source_artifact: "OS-results.html"
expected: "0.842"
found: "0.824"
user_correction: null
notes: "manuscript Results row drifted from HTML"
```

## Core vs learning

- **Fixed core** stays in `00_orchestrator/gates.md` (including G-FACT).
- This file only governs **recording** and **on-demand proposals**.
- Rejected proposals: log reason under `evolution/feedback-log.md`; do not re-spam the same candidate without new evidence.

## Stale-reference

Broken meta paths (`bundles/`, `skills/core/`, …) are harvest/meta hygiene tasks — schedule or on-demand scan — **not** a per-manuscript execution gate.
