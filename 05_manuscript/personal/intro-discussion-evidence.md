# Introduction / Discussion evidence

**Owner:** `05_manuscript` / `manuscript-core`. Purpose: consume verified evidence so this manuscript's Introduction and Discussion can be written. 05 does not run a literature-research route. Retrieval, guideline lookup, and full-text checks belong to `03_research`; 选题 / 选刊 also stay in `03_research` (选刊 is NOT `05-write-venue`; not 01).

Gap discovery from mounted packs → `evidence-request.md` (A 05 judges; 03 searches).

Quotas and IMRAD locks live only in `Aitor-format.md` (do not copy): Intro 800–1000 words, 10–15 refs, last paragraph no citations; Discussion 800–1000 words, 10–15 **new** refs (no overlap with Intro), first paragraph no citations and no result numbers; Methods no citations. Scoring: `introduction-scorecard.md`.

## When to load

写引言 · 写讨论 · 补文献 · 核对引用 · 这篇前言/讨论文献不够

## Introduction workflow (03 handoff)

1. **Endpoint frame (05).** Write the endpoint name once, exactly as Methods (Outcomes) will name it. Note whether it equals a guideline construct or is an operational surrogate of one.
2. **Raise cards (05 → 03)** per `evidence-request.md`: `guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`. One card set per endpoint.
3. **Evidence Pack (03 → 05).** 03 returns the table below plus a search log. 03 does not touch manuscript wording.
4. **Decide (A 05).** Accept / Weaken / Delete each row. Draft elements 2–5 only after every card has an exit.
5. **Budget references before drafting.** Select at most 15 rows. Rank: guideline > systematic review or meta-analysis > multicenter study > single-center study. Assign each row to Intro or Discussion, not both. If more than 15 remain, drop by rank and record why.
6. **Draft** with `Aitor-format.md` + `polisher-sections.md` §2.
7. **Verify (03).** Ledger at the level required below; retraction and correction check on every reference.
8. **Score.** `introduction-scorecard.md`, by a scorer independent of the drafter.

```text
Claim | Source (PMID/DOI) | Class | Design · n · effect | Strength | Weakness relevant to this study | Level (L1-L3) | Intro or Discussion | Keep?
```

Class: `guideline`, `mri_accuracy` (or the modality's accuracy class), `radiomics_endpoint`, `habitat_or_nearest`, `background`.

## Guideline rule

The Introduction uses the latest edition of the guideline that defines the endpoint or the decision. 03 confirms in the same session that no newer edition exists and records body, year, and where the definition sits (section, figure, or table). The gap is mined from what the guideline leaves open. If the study endpoint is an operational surrogate of the guideline construct, element 2 states the construct and element 6 names the study endpoint in one clause; algorithm details stay in Methods.

## Verification levels

- **L1** metadata resolves (title, authors, journal, DOI).
- **L2** numbers checked against the abstract or the full text.
- **L3** full text read. Required for guideline definitions, for any appraisal of strength or weakness, and for comparative claims.

Numbers in the Introduction need L2 or higher. Record the level in the Word comment whenever it is below L3. A reference that fails verification, or that has no retraction check, is a G-LIT case (`evidence-request.md`).

## Claim coverage (replaces a sentence-count gate)

Every literature claim is covered by a citation in its own sentence or by the same-source group it sits in. Reasoning sentences may stand uncited; word them as inference. The sentence-level uncited share is reported, not gated.

## QC (before the section is done)

- Elements 1–6 present; element 2 names guideline body, year, and the decision it supports
- One or two appraisal sentences, tied to this study's design
- Last paragraph: aim and hypothesis, **no** citations, endpoint name identical to Methods
- Reporting standards not named in the Introduction
- Intro vs Discussion reference lists do not overlap
- New writing: within 10–15 / 10–15 new. Checking an already-written manuscript: do **not** delete genuine refs to hit quota; note over-quota only
- Scarcity claims backed by a logged search
- Discussion first paragraph: **no** citations, **no** result numbers
- Methods still citation-free
- Page/year/author checked when the user asks to 核对

Scarcity checks use PubMed plus one other source; they are not a systematic sweep. Do not run Embase+Cochrane by default. Do not generate PRISMA or AI schematics.
