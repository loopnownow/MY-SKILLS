# Style spot-check (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 (with `style-lint` sub-check). Capability bodies: `Aitor-format.md`, vocab — not this file.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Standard

- References: **Vancouver + DOI** (or journal house style after venue lock) — **do not** adopt **APA** as primary.
- Prose/layout spot-check against `05_manuscript/personal/Aitor-format.md` only.

## Must-check

| id | Check | Fail → |
|---|---|---|
| ST-1 | Citation style is Vancouver-like / venue-locked — not APA-primary | 05 Aitee |
| ST-2 | DOI present when required by venue or house rule | 03 / 05 |
| ST-3 | Aitor-format spot: Table 1 = training vs test; nomogram not "Combined"; Methods have no citations | 05 |
| ST-4 | `style-lint` sub-check run when English prose polished (see gates.md) | 05 local rework |

**PASS:** ST-1…4 clean or commented.
**FAIL:** APA-as-primary or format drift → rollback **05**.
