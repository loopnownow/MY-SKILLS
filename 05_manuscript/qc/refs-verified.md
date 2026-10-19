# Refs verified (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06.
**Capability:** `03_research/base/verify-refs/references/doi-crossref-field-audit.md` (Victor).
**Distill of:** Yuan1z `nature-ref-verifier` gate shape (Apache-2.0). Pass/fail only.

## Standard

| id | Check | Fail → |
|---|---|---|
| RV-1 | DOI-first field audit run (or Word-commented skip with reason) | 03 Victor |
| RV-2 | No open Critical field mismatches (author/title/DOI mismatch/pages≥5) | 03 / 05 |
| RV-3 | Unresolved list present: every `Needs fix` / `Unverifiable` row listed or justified | 03 |
| RV-4 | Cross-link: Vancouver+DOI spot (`style-spotcheck.md`) and G-CIT claim→ref (`citation-verify.md`) not skipped | 03 / 05 |

**PASS:** RV-1–4 clean or commented.
**FAIL:** Critical unresolved refs → rollback **before Gate · 05 done / Integrity · pre-06** (03 re-audit; 05 does not self-certify lit).

*Attribution: distilled from Yuan1z0825/nature-skills `nature-ref-verifier` (Apache-2.0).*
