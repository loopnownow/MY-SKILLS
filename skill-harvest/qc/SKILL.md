---
name: harvest-qc
description: >
  Passive execution-learning QC under skill-harvest: record QC events during runs;
  when the user asks for 进化/更新/总结, emit an HTML proposal with options.
  Never auto-modify domain skills. Use with skill-harvest governance.
---

# Harvest-QC (passive + on-demand)

## Split from 00

| Layer | Owner | Job |
|---|---|---|
| Execution QC | `00_orchestrator` (`gates.md`) | Route / Mount(G0) / Boundary / Evidence(G-LIT) / **Consistency(G-FACT)** / Artifact — diagnose and local re-run |
| Learning QC | **this folder** | Append QC events; on explicit user ask, propose evolution HTML |

Do **not** create `07_QC`. Do **not** put evolution back into `00`.

## Normal runs (passive)

When 00 (or a specialist) hits FAIL / UNKNOWN / user correction:

1. Append one event under `../data/qc-events/` (see schema in `rules.md`).
2. Stop. Do **not** open an evolution proposal.
3. Do **not** edit `00`–`06` Skill files.

## On-demand evolution (user must ask)

Trigger phrases: 进化 / 更新技能建议 / 总结 QC / harvest QC 提案.

Then:

1. Read recent `../data/qc-events/`.
2. Cluster by `error_type` + `responsible_node` (no hard-coded ≥2/≥3/≥5 thresholds in Skill text — judge from severity × frequency × downstream impact when drafting).
3. Write one HTML under `../evolution/` (or project scratch) from `../templates/qc-evolution.html`.
4. Include preset options **and** a free-text box for user views outside the presets.
5. Wait for explicit approval before any GitHub / Skill edit.

Forbidden: `OBSERVED → AUTO MODIFY`.

## Allowed statuses (execution side, echoed in events)

```text
PASS
FAIL -> <responsible skill>
UNKNOWN -> <user decision required>
```
