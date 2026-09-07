---
name: table-qc
description: >
  Raw measurement table QC signals: leading-digit distribution, terminal-digit
  preference, between-group SD smoothness heuristic, optional near-duplicate rows.
  Use when auditing assay/clinical numeric tables before analysis. Not for code
  structure QC (code-refactoring), imaging ROI QC, skill-harvest evolution, or
  reported NHST/Table1 math (04 personal stats-consistency).
---

# Table QC (raw numeric tables)

## Purpose

Lightweight **signals** on raw numeric tables. Human review decides; nothing here proves misconduct.

## References

| Topic | Path |
|---|---|
| Leading digits (Benford) | `references/benford-first-digit.md` |
| Terminal-digit preference | `references/terminal-digit-bias.md` |
| SD smoothness heuristic | `references/variance-too-smooth.md` |
| Near-duplicate rows (optional) | `references/row-clone-lsh.md` |

## Boundaries

- Not `code-refactoring/` (deep code QC)
- Not `skill-harvest/qc/`
- Not `02-imaging-qc`
- Reported stats consistency → `04_analysis/personal/stats-consistency.md`
- No vendored checker scripts in this pack; Loopnow/Build may implement runners later

## Upstream (links only)

- https://github.com/milcent/benford_py
- https://github.com/lorenz-walthert/scrutiny
- https://github.com/ekzhu/datasketch
