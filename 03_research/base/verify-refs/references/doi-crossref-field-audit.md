# DOI-first Crossref field audit (capability · short)

**Owner:** Victor / `03_research/base/verify-refs`. Extends Vancouver + DOI spotcheck; does **not** replace `03_research/personal/citation-verify.md` (claim→ref).
**Distill of:** Yuan1z `nature-ref-verifier` workflow (Apache-2.0). Short original steps; no Zotero sync scripts.

## When

Pre-submit bibliography field audit, or when Gate · 05 / Integrity · pre-06 needs `refs-verified` cleared. Pair with `05_manuscript/qc/refs-verified.md` (pass/fail) and `05_manuscript/qc/style-spotcheck.md` (Vancouver+DOI).

## Steps (DOI-first)

1. **Parse** reference list / BibTeX / pasted items. Extract DOI when present.
2. **DOI resolve first** — for each DOI, query Crossref `works/<DOI>` (or equivalent).
   - HTTP 404 / not found → Critical: bad or mistyped DOI.
   - 200 → compare title, first author, year/volume/pages against the manuscript entry.
3. **Field audit matrix** (severity when DOI present; else title+author fallback search):

| Severity | Fail modes (examples) |
|---|---|
| Critical | Author name/order wrong; missing co-author on short lists; pages off ≥5; article-id letter/digit swap; title core words differ; DOI resolves to a **different** paper |
| Warning | Volume-year ≠ DOI year; Early-Access metadata drift; missing issue; pages off ≤4; middle-initial drift |
| Info | Title case; journal abbrev vs full; `&` vs `and` |

4. **Confidence** per item: `Verified` | `Check suggested` | `Needs fix` | `Unverifiable`.
5. **Report** counts + unresolved list (Needs fix + Unverifiable). Hand unresolved to Aitee wording / Victor substitute; do **not** invent DOI/PMID.

## Fail → gate

Any Critical or unresolved `Needs fix` without Word comment → FAIL `05_manuscript/qc/refs-verified.md` → rollback before Gate · 05 done / Integrity · pre-06.

## Cross-links

- G-CIT / claim→ref: `03_research/personal/citation-verify.md`
- Style: `05_manuscript/qc/style-spotcheck.md`
- Broader metadata tools: this pack's `MODULE.md` / scripts (optional)

*Attribution: distilled from Yuan1z0825/nature-skills `nature-ref-verifier` (Apache-2.0).*
