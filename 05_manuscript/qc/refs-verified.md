# Refs verified (05 qc · standards only)

**Owner:** `00_orchestrator` at Gate · 05 / Integrity · pre-06.
**Capability:** `03_research/base/verify-refs/references/doi-crossref-field-audit.md` (Victor).
**Distill of:** Yuan1z `nature-ref-verifier` gate shape (Apache-2.0). Pass/fail only.
**Compose:** `citation-audit-gate.md` (Layer 4 existence+metadata+context) — this file owns **field-verify** severity; citation-audit owns claim-context KEEP/FIX/REPLACE/REMOVE.

## Standard

| id | Check | Fail → |
|---|---|---|
| RV-1 | DOI-first field audit run (or Word-commented skip with reason) | 03 Victor |
| RV-2 | No open Critical field mismatches (author/title/DOI mismatch/pages…) | 03 / 05 |
| RV-3 | Unresolved list present: every `Needs fix` / `Unverifiable` row listed or justified | 03 |
| RV-4 | Cross-link: Vancouver+DOI spot (`style-spotcheck.md`) and G-CIT claim→ref (`citation-verify.md`) not skipped | 03 / 05 |

## Crossref / field axes (DOI-first)

Run capability steps in `doi-crossref-field-audit.md`. Gate uses these severity classes:

| Severity | Examples (field axis) | Gate effect |
|---|---|---|
| **Critical** | Author name/order wrong; missing co-author on short lists; pages off ≥5; article-id letter/digit swap; title core words differ; DOI 404; DOI resolves to a **different** paper | Open Critical → **FAIL** RV-2 |
| **Warning** | Volume-year ≠ DOI year; Early-Access metadata drift; missing issue; pages off ≤4; middle-initial drift | May PASS with Word comment / `Check suggested` |
| **Info** | Title case; journal abbrev vs full; `&` vs `and` | Advisory only |

Per-item confidence: `Verified` | `Check suggested` | `Needs fix` | `Unverifiable`.
DOI-first: resolve Crossref `works/<DOI>` before title+author fallback. Non-Crossref (CNKI, old IEEE 404, theses) → fallback sources; do not invent DOI/PMID.

**PASS:** RV-1–4 clean or commented.
**FAIL:** Critical unresolved refs → rollback **before Gate · 05 done / Integrity · pre-06** (03 re-audit; 05 does not self-certify lit).

*Attribution: distilled from Yuan1z0825/nature-skills `nature-ref-verifier` (Apache-2.0).*
