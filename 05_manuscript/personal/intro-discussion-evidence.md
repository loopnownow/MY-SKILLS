# Introduction / Discussion evidence (thin)

**Owner:** `05_manuscript` / `manuscript-core`. Purpose: find and verify papers **so this manuscript’s Introduction and Discussion can be written**. Not a systematic-review skill. 选题 / 选刊 → `03_research` (选刊 is NOT `05-write-venue`; not 01).

Quotas and IMRAD locks live only in `Aitor-format.md` (do not copy): Intro 800–1000 words, 10–15 refs, last paragraph no citations; Discussion 800–1000 words, 10–15 **new** refs (no overlap with Intro); first paragraph no citations and no result numbers; Methods no citations. Prose templates: `polisher-sections.md` §2 / §5.

## When to load

写引言 · 写讨论 · 补文献 · 核对引用 · 这篇前言/讨论文献不够 · 查文献（工程里已有稿或正在写 SCI 全文）

选题 / 选刊 / 研究设计 / 国自然 → `03_research`（选刊 is NOT `05-write-venue`），不用本文件。

## Workflow

1. List **claims** that need a source (disease burden, gap, prior imaging/radiomics work, mechanism, conflicting results). Do not search “the topic” in the abstract.
2. For each claim: PubMed (or publisher page) → record PMID/DOI, design, *n*, effect + CI, year. **Never invent** a paper, PMID, DOI, or page.
3. Assign each keepable paper to **Intro** or **Discussion**, not both.
4. Fill the table, then draft/polish I/D with `polisher-sections.md` + `Aitor-format.md`.
5. Optional DOI→BibTeX: `scripts/doi_to_bibtex.py` (Vancouver+DOI still follows Aitor).

```text
Claim | PMID/DOI | Design · n · effect | Intro or Discussion | Keep?
```

## QC (before the section is done)

- Every factual sentence in Intro/Discussion (except the two locked paragraphs) has a real citation
- Intro last paragraph: aim/hypothesis, **no** citations
- Discussion first paragraph: **no** citations, **no** result numbers
- Intro vs Discussion reference lists do not overlap
- New writing: count within Aitor 10–15 / 10–15 new
- Checking an already-written manuscript: do **not** delete genuine refs to hit quota; note over-quota only
- Methods still citation-free
- Page/year/author checked when the user asks to 核对

Do not run Embase+Cochrane by default. Do not generate PRISMA or AI schematics.
