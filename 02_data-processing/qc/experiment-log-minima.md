# Experiment log minima (02 qc — standards only)

**Owner:** `00_orchestrator` when raw experiment / acquisition / processing logs are part of the packet.
**Domain gate:** Wet-lab, imaging-acquisition, or multi-session processing logs. **NOT_APPLICABLE** for pure secondary-data RAD tables with no experiment log artifact.
**Distill of:** Yuan1z `nature-experiment-log` hygiene axes (MIT frontmatter). **Do not** install Feishu / Obsidian / vision runtime — standards only.

## Must-check (EL)

| Id | Check | Fail → |
|---|---|---|
| EL-1 | Missing or fuzzy fields (condition, ID, unit, timestamp) are marked unknown / questioned — **never guessed** into the log | 02 |
| EL-2 | Stable experiment / batch ID scheme documented (or project convention cited) | 02 |
| EL-3 | Raw inputs archived or path-referenced; log points to raw locus | 02 |
| EL-4 | Asia/Shanghai (or project zone) stamps consistent on log faces | 02 |
| EL-5 | No PHI / identifiable LIS dumps in log filenames or bodies (compose **G-PHI**) | stop; user |

**PASS:** EL-1-5 clean or commented.
**FAIL:** invented conditions/results in the log, or PHI path → block until 02 / user clears.

*Attribution: nature-experiment-log (MIT); lab 02 coding-qc / G-PHI remain authoritative. No MCP absorb.*
