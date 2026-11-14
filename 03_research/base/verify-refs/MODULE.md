---
name: "verify-refs"
domain: "03_research"
trigger: ["verify-refs", "引用核验", "citation validation", "bibtex", "retraction", "撤稿"]
outputs: ["skill_output"]
owner: "03_research/base/verify-refs/MODULE.md"
---

# verify-refs (citation integrity)

Citation authenticity check + BibTeX format/write.

Thin contract for verify-refs (DOI-first integrity): scope, bans, phase names, and pointers. The house working method and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`references/`, `scripts/`) stays beside it as data. Absorbed from Scientific `skills/citation-management/` (MIT, 2026-10-17); source line: `references/api_contracts.md`.

## Mission

Every reference that reaches a manuscript, grant or response must resolve to a real record whose metadata matches the record. verify-refs finds, validates, formats and audits citations; it does not write prose around them.

Out of scope: literature selection and synthesis (`lit-search`), OA full-text retrieval (`lit-fulltext`), and reference-list house style (05 base `write-paper`).

## Input

Minimum: a DOI / PMID / arXiv ID, a `.bib` file, or a reference list to audit. If a claimed citation has no identifier, ask for the source record; never guess a DOI, year, volume or author list. A "not found" answer is a valid output; an invented record is a fail.

## Workflow (decision nodes)

1. **Identify the record.** DOI first, then PMID/PMCID/arXiv; a title-only match needs a source page. Detail: `references/core_workflow.md`.
2. **Extract metadata** from the record (not from memory), then cross-check fields: `references/metadata_extraction.md`, `references/doi-crossref-field-audit.md`.
3. **Integrity pass** (same pass as metadata validation): retraction / correction / expression-of-concern scan, plus the library pointer layer (entity, `references/index.csv` row and `DOI_<doi>.md` pointer must agree): `references/retraction-audit.md`, `references/library-pointer-sync.md`. Gate: `05_manuscript/qc/refs-verified.md`.
4. **Format BibTeX** deterministically: `references/bibtex_formatting.md`; script arguments in `references/script_reference.md`.
5. **Validate** every entry (resolve, completeness, duplicates): `references/citation_validation.md`.
6. **Hand off**: claim→ref table and a strong-claim spot-check go to `03_research/advanced/citation-verify.md`; a missed citation is a 05 prose repair, not a verify-refs rewrite.

## Constraints (never)

- Never invent or "fill in" a DOI, year, volume, page range or author list. A missing field stays missing and is reported.
- Never cite a retracted or expression-of-concern record without flagging it.
- Never bypass a paywall or use Sci-Hub (OA-only retrieval belongs to `lit-fulltext`).
- Never rename or correct a DOI in only one layer: entity filename, index row and project pointer move together in one operation (`references/library-pointer-sync.md`).
- Network gate (2026-11-01): every script that reaches PubMed / OpenAlex / Crossref / Unpaywall / Retraction Watch refuses to run by default and exits 1 with `network disabled`; opt in per call with `--allow-network`, or per shell with `SKILLS_ALLOW_NETWORK=1`. Offline scripts (`format_bibtex.py`, `search_google_scholar.py`) need no flag; `validate_citations.py` takes the flag even for a local-only run. Command examples omit the flag for readability only.
- Scripts live under `{code_stats}\tools\verify-refs\`; this pack keeps pointers, not a copy.

## Output and handoff

- BibTeX file (or a diff to the existing `.bib`) plus a one-line PASS/FAIL per entry.
- Integrity verdict: metadata match / mismatch (with field), retraction status, pointer agreement.
- Handoff: to 05 `write-paper` for insertion; to 00 at G-LIT / G-CIT; to `lit-search` when the missing item is a search problem rather than a metadata problem.

## References

| File | Open when |
|---|---|
| `references/core_workflow.md` | the five phases in full, with canonical commands |
| `references/search_strategies.md`, `references/google_scholar_search.md`, `references/pubmed_search.md` | query construction per source |
| `references/metadata_extraction.md`, `references/bibtex_formatting.md`, `references/citation_validation.md` | per-topic detail |
| `references/doi-crossref-field-audit.md` | DOI-first field audit (P1) |
| `references/retraction-audit.md`, `references/library-pointer-sync.md` | integrity pass and pointer layer |
| `references/best_practices.md`, `references/example_workflows.md` | quality rules / end-to-end examples |
| `references/api_contracts.md` | upstream API contracts and the MIT source note |
