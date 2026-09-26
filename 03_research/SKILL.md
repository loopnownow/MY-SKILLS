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

**Mounted 03 ids** are the registry menu for generic retrieval and blueprints (see Mounted capability ids below for the short retirement pointer). Personal grant/ethics/intake/translation files stay here. 选刊 is 03 (`literature/journal-selection.md`; evidence via `lit-search`). 选刊走 03 `find-journal`；`venue-templates` 只管体例.

## Literature rule

- Introduction evidence pack: on 05 cards (`guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`) → `literature/intro-evidence-pack.md`; the mounted `ma-scout` supplies the row format. Candidates only; 05 decides.


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

`clinical-translation/` is **personal research-design supplement** (reader study, prospective deployment, regulatory, threshold-to-action). Not 02, not 04. Generic translational templates may later mount at `design-study` / `write-protocol`.

## Mounted capability ids (generic; registry MOUNTED = menu)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

Live fine ids are in `01_skill-discovery-integration/registry.yaml` (for example `lit-search`, `frontier-hypothesize`, `design-study`, `find-cohort-gap`). Archived ids stay off the menu (registry `archived:`).

**Retirement pointer (single block):** Most of `design/` and `frontier/` were retired 2026-09-13 as duplicates of mounted `design-study` / `find-cohort-gap` (`EXTERNALIZATION_CANDIDATES.md`); `radiology-design.md` and `radiology-frontier.md` stay (no B counterpart). `evidence-layer.md`, `idea-to-question.md`, `literature.md`, `sources.md`, `public-datasets.md`, and `literature-evidence-2023-2026.md` were retired 2026-09-22 — use `frontier-hypothesize`, `lit-search`, and `ma-scout`. `literature/` keeps `journal-selection.md` (选刊 SOP), `journal-patterns-2023-2026.md`, and `intro-evidence-pack.md`. 选刊走 03 `find-journal`；`venue-templates` 只管体例.

## Default research spine (workflow)

**Not a literature-search mega-flow.** Default exploration chain:

`R1 Question → R2 Evidence & Mechanism → R3 Design → R4 Data need → R5 Research Brief`

Full rules and card schemas: [`workflows/question-to-reference.md`](workflows/question-to-reference.md).

- **03** owns the content chain and stage cards.
- **00** chooses mid-chain entry, reuse of completed cards, rollback, and STOP (`00_orchestrator/workflows/research-exploration-loop.md`).
- `lit-search` is invoked **inside R2** only; R2 also screens, verifies claims, maps mechanisms (`direct|indirect|hypothesis|unknown`), and records conflicts/gaps.
- R4 lists data needs and hands feasibility to **02** (obtain/process) and **04** (stats support). R5 is a **Research Brief**, not a paper Conclusion.

| Task | Path |
|---|---|
| Question → Evidence → Design → Data → Brief | `workflows/question-to-reference.md` |

## Modes

- Evidence: gaps, conflict, mechanism, journal fit. Never invent PMID/DOI.
- Design: question/hypothesis, eligibility, endpoints, sample size, bias, reporting guideline.
- Translational design: use scenario, reader study, threshold-to-action, prospective/regulatory — `clinical-translation/`.
- Grant-review (Voice A): load **only** `personal/grant-review.md`. English journal peer review stays in `06_review`.
- Grant-writing (Voice B): skeleton + method-upgrade + `personal/grant-writing.md`. Never paste Voice A tics into own text.



**Journal format (nested):** `medical-journal-submit/journal-format-compliance/` is invoked after 选刊 when formatting to author guidelines — not a fine id; see that pack's SKILL + parent § Journal format compliance.

## Boundaries

- 选刊 / where to submit stays here (`literature/journal-selection.md` + `medical-journal-submit/`). 选刊走 03 `find-journal`；`venue-templates` 只管体例.
- Manuscript prose / I/D writing → `05_manuscript`
- Statistics / figures → `04_analysis`
- Data preprocessing / extraction → `02_data-processing`
- Ethics **forms** (fill pack) stay here (`ethics-application-forms/`); protocol-level ethics → `personal/ethics.md`
- Translational / reader-study **design** stays here (`clinical-translation/`)
- Reviewer response → `06_review`
