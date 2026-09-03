---
name: medical-research-design-and-evidence
description: >
  Research framework: study design, literature research, evidence, frontier,
  journal/topic selection, grants, translational/reader-study design.
  Literature enters here only — never via 01.
  Personal grant/ethics/intake/translation files are a SUPPLEMENT, not an upper writing layer.
  Manuscript prose → 05. Reviewer response → 06. Stats → 04.
---

# Research Design & Evidence

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.

**Mounted 03 ids** (`03-lit-*` / `03-design-*` / `03-frontier-*`) are the registry menu for generic retrieval and blueprints. Local `literature/` `design/` `frontier/` are a **temporary dual-track supplement**, not those split ids (`EXTERNALIZATION_CANDIDATES.md`). Personal grant/ethics/intake/translation files stay here. 选刊 is 03 (`literature/journal-selection.md`; evidence via `03-lit-search` / literature layer), not `05-write-venue`.

## Literature rule

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

Local `literature/`, `design/`, `frontier/` are a **temporary dual-track supplement**, not the split ids (see `EXTERNALIZATION_CANDIDATES.md`). Dual-track `literature/` holds `journal-selection.md` as the 选刊 SOP. Mounted id for 选刊 evidence: `03-lit-search` / literature layer. Do not send 选刊 to `05-write-venue`.

## Modes

- Evidence: gaps, conflict, mechanism, journal fit. Never invent PMID/DOI.
- Design: question/hypothesis, eligibility, endpoints, sample size, bias, reporting guideline.
- Translational design: use scenario, reader study, threshold-to-action, prospective/regulatory — `clinical-translation/`.
- Grant-review (Voice A): load **only** `personal/grant-review.md`. English journal peer review stays in `06_review`.
- Grant-writing (Voice B): skeleton + method-upgrade + `personal/grant-writing.md`. Never paste Voice A tics into own text.

## Boundaries

- 选刊 / where to submit stays here (`literature/journal-selection.md`). `05-write-venue` is journal templates / house style while writing, not journal choice.
- Manuscript prose / I/D writing → `05_manuscript`
- Statistics / figures → `04_analysis`
- Data preprocessing / extraction → `02_data-processing`
- Ethics **forms** (fill pack) stay here (`ethics-application-forms/`); protocol-level ethics → `personal/ethics.md`
- Translational / reader-study **design** stays here (`clinical-translation/`)
- Reviewer response → `06_review`
