---
name: medical-scientific-writing
description: >
  Personal SCI original-article prose layer (Ying Li / Aitor-format / de-AI).
  Mounted writing skills supply generic capability; this layer is the personal upper
  layer and final wording authority. Literature research → 03. Figures → 04.
  Reviewer response → 06. Do not use for 评阅 or 回复审稿人.
---

# Scientific Writing — personal upper layer

## Purpose

Convert **validated** research information into precise, publication-ready original-article prose.
**Never invent** sample sizes, P values, effects, CIs, procedures, ethics IDs, citations, or claims.

**Lab priority:** data truth > journal format > Ying Li voice > generic ornate English.

**Every SCI full paper uses `Aitor-format.md` as the only Aitor-format.** If a rule is unclear, **ask the user**. Do not invent a second format.

## Layer model

**Mounted writing capability → 05 personal upper layer → 00 Final QC.**

Generic writing files remaining locally are externalization candidates until a mount covers them.

## Personal assets

| Task | Path |
|---|---|
| Aitor-format (title page, IMRAD, DOCX, citation quotas) | `Aitor-format.md` |
| Section polish templates | `polisher-sections.md` |
| Sentence templates | `sentence-templates.md` |
| Exemplars | `exemplars.md` |
| Corpus phrase bank | `corpus-phrase-bank.md` |
| Citation and language | `citation-and-language.md` |
| I/D evidence consumption (not a literature-research route) | `intro-discussion-evidence.md` |
| de-AI pack | `de-ai/` |
| Diff harvest (evidence script) | `diff_harvest.py` |

## Mounted capability ids (generic; not present until mounted)

- `05-writing-generic` — section templates, reporting/citation/ethics/polish generic, `doi_to_bibtex.py`, journal-family writing/house style (C4 lives in B, not here)

Until mounted, local generic copies remain (see `EXTERNALIZATION_CANDIDATES.md`): `manuscript-core.md`, `mode-1-sci.md`, `section-templates.md`, reporting/citation files, etc. Journal-style files (`journal-family-writing-style`, `nature-family-shape`, `venue-voice-and-house-style`, `radiology-house-style`) are **not** kept in A; they live in B.

## Figures

**Figures → `04_analysis`** (mounted `04-figure-engine` + `lab-palettes.md`). 05 writes captions and body callouts; it does not own the figure pack.

## Literature

Literature search/evidence retrieval for Introduction/Discussion is executed through `03_research`. 05 consumes verified evidence (`intro-discussion-evidence.md`) and applies Aitor quotas. 选题/选刊 stays in 03.

## Core rule

Write from evidence and supplied results. Missing info → Word comment (author **A**); never yellow fill; never invent.

## Lab voice (Ying Li) — summary

- Highly standardized · clinically oriented · quantitatively precise · objectively cautious
- Numbers attached to claims (`n`, AUC, 95% CI, *P*)
- Observational → avoid causal overclaim (*associated with*)
- Forbidden fluff: `de-ai/forbidden-phrases.md`
- Prediction-model full papers: patient-level split (training / test; validation set = external only); dual-set main metrics; LASSO+RadScore formula in prose; `95% CI: X–X`; no em-dash punctuation; Vancouver+DOI as required

Word counts, citation placement, typography, and Table 1 layout live only in **`Aitor-format.md`**. If that file and any other note disagree, `Aitor-format.md` wins.

## Not this skill

- Pre-submission / 模拟审稿 / 评阅 → `06_review`
- Response letter / 回复审稿人 → `06_review`
- Statistics / figures → `04_analysis`
- Literature landscape → `03_research`

## Writing QC (domain)

terminology · tense · numbers match sources · no unsupported causality · abbreviations at first use · figure/table cites · refs coherent · abstract matches main text · de-AI ban list clean · Aitor-format QC

Overall Final QC and local recovery are owned by `00_orchestrator`.
