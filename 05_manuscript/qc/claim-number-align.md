# Claim ↔ number / table / figure align (05 qc · standards only)

**Owner:** `00_orchestrator` (composes **G-FACT**). Capability bodies stay in personal/base.
Inspired by ARS topology/checklists (short original text; no ARS copy).

## Standard

Abstract claims, Results text, tables, figures, and Conclusions must use the **same fact chain** as the upstream artifact (usually `*-results.html` / 02 handoff). Source = FILE / UPSTREAM / USER — never LLM guess.

## Must-check

| id | Check | Fail → |
|---|---|---|
| CN-1 | n / split / AUC·CI·P in prose match HTML (or named upstream) | 04 (stats) or 05 (prose drift) |
| CN-2 | Table numbers match the same endpoint HTML | 05 / 04 |
| CN-3 | Figure values / captions do not contradict tables or Results | 05 / 04 |
| CN-4 | Conclusions do not over-claim beyond Results | 05 Aitee |

Points to **G-FACT** composition in `00_orchestrator/gates.md`. Integrity · pre-06 reuses this when numbers are cited.

**PASS:** CN-1…4 clean or commented with edit plan.
**FAIL:** silent mismatch → HARD block (G-FACT) before next node / before 06.
