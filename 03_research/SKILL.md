---
name: medical-research-design-and-evidence
description: >
  Research approach: study design, literature research, evidence, frontier,
  journal/topic selection, grants, translational/reader-study design.
  Literature enters here only — never via 01.
  Personal grant/ethics/intake/translation files are a SUPPLEMENT, not an upper writing layer.
  Manuscript prose → 05. Reviewer response → 06. Stats → 04.
---

# Research Design & Evidence

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.

**Mounted 03 ids** (`03-lit-*` / `03-design-*` / `03-frontier-*`) are the registry menu for generic retrieval and blueprints. Most of `design/` and `frontier/` were 1:1 duplicates of mounted `design-study`/`find-cohort-gap` and were retired 2026-09-13 (`EXTERNALIZATION_CANDIDATES.md`); what remains — `design/radiology-design.md`, `frontier/radiology-frontier.md`, `frontier/evidence-layer.md`, `frontier/idea-to-question.md` — has no live mount point covering it and is kept. `literature/` keeps `journal-selection.md` (选刊 SOP), `sources.md`, `public-datasets.md`, `literature.md`, `journal-patterns-2023-2026.md`, `intro-evidence-pack.md` — none duplicated in B; only `literature-evidence-2023-2026.md` was retired (duplicate of mounted `ma-scout`). Personal grant/ethics/intake/translation files stay here. 选刊 is 03 (`literature/journal-selection.md`; evidence via `03-lit-search` / literature layer), not `05-write-venue`.

## Literature rule

- Introduction evidence pack: on 05 cards (`guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`) → `literature/intro-evidence-pack.md`; the mounted `03-lit-review` supplies the row format. Candidates only; 05 decides.


**Literature research → 03 only.** Do not route literature through 01 (discovery) or 05 (writing). 05 consumes verified I/D evidence; it does not run a second literature-research route.

## Personal supplement (not an upper layer)

| Task | Path |
|---|---|
| Voice A — 评别人的国自/面上 | `personal/grant-review.md` |
| Voice B — 写自己的标书句库 | `personal/grant-writing.md` |
| Voice B 章节骨架 | `personal/grant-own-skeleton.md` |
| 方法升级写进立项 | `personal/method-upgrade-into-grant.md` |
| Intake | `personal/intake.md` |
| Ethics (protocol-level) | `personal/ethics.md` |
| Multicenter | `personal/multicenter.md` |
| JCR 分层荐刊（金山） | `medical-journal-submit/` |
| Clinical translation / reader-study **design** | `clinical-translation/` (`references/`) |
| Ethics application **forms** (fill pack) | `ethics-application-forms/` (`scripts/`, `references/`) |

Do not rewrite mounted literature/systematic-review capability inside these files.

`clinical-translation/` is **personal research-design supplement** (reader study, prospective deployment, regulatory, threshold-to-action). Not 02, not 04. Generic translational templates may later mount at `03-design-experiment` / `03-design-protocol`.

## Mounted capability ids (generic; registry MOUNTED = menu)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached. 03 ids are already MOUNTED in the registry (still ask-each-run).

- `03-lit-search` — retrieve papers
- `03-lit-fulltext` — fetch PDF/HTML
- `03-lit-review` — synthesize / systematic review
- `03-lit-cite` — citation library / Zotero
- `03-design-experiment` — pre-data experimental design
- `03-design-protocol` — write/fill protocol
- `03-design-grant` — grant text; A Voice A/B still wins
- `03-frontier-ideate` — topic brainstorm
- `03-frontier-hypothesize` — question/hypothesis

Retired coarse ids: `03-literature`, `03-design`, `03-frontier`.

Most of `design/` and `frontier/` were retired 2026-09-13 as duplicates of mounted `design-study` / `find-cohort-gap`; the remaining unique files (`radiology-design.md`, `radiology-frontier.md`, `evidence-layer.md`, `idea-to-question.md`) stay — see `EXTERNALIZATION_CANDIDATES.md` for why each was kept. `literature/` holds `journal-selection.md` as the 选刊 SOP (JCR pool + layer tables live in `medical-journal-submit/`) plus the non-duplicate reference files listed above. Mounted id for 选刊 evidence: `03-lit-search` / literature layer. Do not send 选刊 to `05-write-venue`.

## Modes

- Evidence: gaps, conflict, mechanism, journal fit. Never invent PMID/DOI.
- Design: question/hypothesis, eligibility, endpoints, sample size, bias, reporting guideline.
- Translational design: use scenario, reader study, threshold-to-action, prospective/regulatory — `clinical-translation/`.
- Grant-review (Voice A): load **only** `personal/grant-review.md`. English journal peer review stays in `06_review`.
- Grant-writing (Voice B): skeleton + method-upgrade + `personal/grant-writing.md`. Never paste Voice A tics into own text.

## Boundaries

- 选刊 / where to submit stays here (`literature/journal-selection.md` + `medical-journal-submit/`). `05-write-venue` is journal templates / house style while writing, not journal choice.
- Manuscript prose / I/D writing → `05_manuscript`
- Statistics / figures → `04_analysis`
- Data preprocessing / extraction → `02_data-processing`
- Ethics **forms** (fill pack) stay here (`ethics-application-forms/`); protocol-level ethics → `personal/ethics.md`
- Translational / reader-study **design** stays here (`clinical-translation/`)
- Reviewer response → `06_review`
