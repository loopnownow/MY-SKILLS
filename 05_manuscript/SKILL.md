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

**Every SCI full paper uses `personal/Aitor-format.md` as the only Aitor-format.** If a rule is unclear, **ask the user**. Do not invent a second format.

## Layer model

**Mounted writing capability → 05 personal upper layer → 00 Final QC.**

## Personal assets

| Task | Path |
|---|---|
| Aitor-format (title page, IMRAD, DOCX, citation quotas) | `personal/Aitor-format.md` |
| Section polish templates | `personal/polisher-sections.md` |
| Sentence templates | `personal/sentence-templates.md` |
| Exemplars | `personal/exemplars.md` |
| Corpus phrase bank | `personal/corpus-phrase-bank.md` |
| Citation and language | `personal/citation-and-language.md` |
| I/D evidence consumption (not a literature-research route) | `personal/intro-discussion-evidence.md` |
| de-AI pack (forbidden phrases / AI-isms) | `personal/de-ai.md` + `personal/forbidden-phrases.md` |
| Diff harvest (evidence script) | `personal/diff_harvest.py` |

## Mounted capability ids (generic; not present until mounted)

- `05-writing-generic` — section templates, reporting/citation/ethics/polish generic, `doi_to_bibtex.py`, journal-family writing/house style (B `05-manuscript/writing-generic/`)
- `05-humanize` — generic de-AI / humanize (MedSci `skills/humanize/`). Not in B. Does **not** replace `personal/de-ai.md` + `personal/forbidden-phrases.md`.

`writing-generic` lives in B. `05-humanize` is a user-named MedSci interface. Personal de-AI stays in A (`personal/`).

## Figures

**Figures → `04_analysis`** (mounted `04-figure-engine` + `04_analysis/personal/lab-palettes.md`). 05 writes captions and body callouts; it does not own the figure pack.

## Literature

Literature search/evidence retrieval for Introduction/Discussion is executed through `03_research`. 05 consumes verified evidence (`personal/intro-discussion-evidence.md`) and applies Aitor quotas. 选题/选刊 stays in 03.

## Core rule

Write from evidence and supplied results. Missing info → Word comment (author **A**); never yellow fill; never invent.

## Lab voice (Ying Li) — summary

- Highly standardized · clinically oriented · quantitatively precise · objectively cautious
- Numbers attached to claims (`n`, AUC, 95% CI, *P*)
- Observational → avoid causal overclaim (*associated with*)
- Forbidden fluff: `personal/forbidden-phrases.md`
- Prediction-model full papers: patient-level split (training / test; validation set = external only); dual-set main metrics; LASSO+RadScore formula in prose; `95% CI: X–X`; no em-dash punctuation; Vancouver+DOI as required

Word counts, citation placement, typography, and Table 1 layout live only in **`personal/Aitor-format.md`**. If that file and any other note disagree, `personal/Aitor-format.md` wins.

## Not this skill

- Pre-submission / 模拟审稿 / 评阅 → `06_review`
- Response letter / 回复审稿人 → `06_review`
- Statistics / figures → `04_analysis`
- Literature landscape → `03_research`

## Writing QC (domain)

terminology · tense · numbers match sources · no unsupported causality · abbreviations at first use · figure/table cites · refs coherent · abstract matches main text · de-AI ban list clean · Aitor-format QC

Overall Final QC and local recovery are owned by `00_orchestrator`.
