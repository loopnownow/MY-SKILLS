---
name: medical-research-design-and-evidence
description: >
  Research approach: study design, literature research, evidence, frontier,
  journal/topic selection, grants, translational/reader-study design.
  Triggers: 文献, 选刊, 推荐杂志, 基金申请, 伦理, 研究设计, 转化, reader study,
  lit-search, find-journal, fill-protocol.
  Literature enters here only — never via 01.
  Personal grant/ethics/intake/translation files are a SUPPLEMENT, not an upper writing layer.
  Manuscript prose → 05. Reviewer response → 06. Stats → 04.
---

# Research Design & Evidence

## Purpose

Turn a clinical/biomedical idea into a defensible protocol and evidence base.

**Three pillars** (see `personal/route.md` for the full pointer table):

| Pillar | 中文 | Owns |
|---|---|---|
| Evidence & literature | 文献与证据 | citation-verify, intro-evidence-pack, 选题 SOP (`journal-selection.md`), lit-search (mounted) |
| Design & exploration | 研究设计与探索 | radiology-design/frontier, ethics, intake, multicenter, grants (Voice A/B), clinical-translation; ethics **forms** → `fill-protocol/` |
| Journal selection | 选刊 | `find-journal/` (list gates in-repo; **runtime pools in 0doc**); per-project 选刊/已投名单 → `<project>/ref/` — not in MY-SKILLS |

**Mounted 03 ids** are the registry menu for generic retrieval and blueprints (see Mounted capability ids). Personal grant/ethics/intake/translation files stay under `personal/`. 选题 is 03 (`personal/journal-selection.md`; evidence via `lit-search`). 选刊走 03 `find-journal`；`venue-templates` 只管体例.

## Literature rule

- Introduction evidence pack: on 05 cards (`guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`) → `personal/intro-evidence-pack.md`; the mounted `scout-meta-analysis` supplies the row format. Candidates only; 05 decides.

**Literature research → 03 only.** Do not route literature through 01 (discovery) or 05 (writing). 05 consumes verified I/D evidence; it does not run a second literature-research route.

**Citation verify (required on writing and review).** Semantic labels only: **G-CIT-1** is draft evidence verification before Gate → 05; **G-CIT-2** is post-revision / inside 06. G-CIT-1 does not waive G-CIT-2. Before Gate → 05 can mark a manuscript done, and inside every 06 review, run `personal/citation-verify.md`: claim↔ref table plus a spot-check of strong claims against the sources. Mid-entry does not waive it. A prior 05 pass does not waive the 06 pass. 05 and 06 call/require 03 citation-verify — do not self-certify lit. Ownership: see `00_orchestrator/references/ownership-contract.md`.

## Personal supplement (not an upper layer)

| Task | Path |
|---|---|
| Routing / handoff | `personal/route.md`, `personal/handoff.md` |
| Voice A — 别人的基金/标书 | `personal/grant-review.md` |
| Voice A 语料 — 别人标书批注 | `{doc_review_corpus}\source\grant-review\` |
| write-protocol / 申报书开写 | `{doc_grants}\` |
| Voice B — 写自己的标书 | `personal/grant-writing.md` |
| Voice B 章节骨架 | `personal/grant-own-skeleton.md` |
| 方法升级写入标书 | `personal/method-upgrade-into-grant.md` |
| Intake | `personal/intake.md` |
| Ethics (protocol-level) | `personal/ethics.md` |
| Multicenter | `personal/multicenter.md` |
| 选题 SOP（含 2023–2026 期刊规律） | `personal/journal-selection.md` |
| Intro evidence pack | `personal/intro-evidence-pack.md` |
| Radiology design / frontier | `personal/radiology-design.md`, `personal/radiology-frontier.md` |
| JCR 分层荐刊包（金山） | `find-journal/`（list gates in-repo；**full pools → `{doc_root}\04-lab-reference\find-journal\data\2026\`**） |
| Clinical translation / reader-study **design** | `personal/clinical-translation/` (`references/`) |
| Ethics application **forms** (fill pack; **seat Bai**, Aitor routes/monitors; path stays here) | `fill-protocol/` (`scripts/`, `references/`, `references/form-boilerplate.md`) |
| Citation verify | `personal/citation-verify.md` |
| Per-project 选刊/已投名单 | **`<project>/ref/`** (e.g. `journals-submitted.md`) — never store in MY-SKILLS |

Do not rewrite mounted literature/systematic-review capability inside these files.

`personal/clinical-translation/` is **personal research-design supplement** (reader study, prospective deployment, regulatory, threshold-to-action). Not 02, not 04. Generic translational templates may later mount at `design-study` / `write-protocol`.

## Mounted capability ids (generic; registry MOUNTED = menu)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

Live fine ids are in `01_skill-integration/registry.yaml` (for example `lit-search`, `frontier-hypothesize`, `design-study`, `find-cohort-gap`). Archived ids stay off the menu (registry `archived:`).

**Retirement pointer (single block):** Most of former `design/` and `frontier/` were retired 2026-09-13 as duplicates of mounted `design-study` / `find-cohort-gap` (`EXTERNALIZATION_CANDIDATES.md`); `radiology-design.md` and `radiology-frontier.md` stay under `personal/` (no B counterpart). `evidence-layer.md`, `idea-to-question.md`, `literature.md`, `sources.md`, `public-datasets.md`, and `literature-evidence-2023-2026.md` were retired 2026-09-22 — use `frontier-hypothesize`, `lit-search`, and `scout-meta-analysis`. 2026-10-16 reorg: `literature/`, `design/`, `frontier/` folders removed; files live under `personal/`; `journal-patterns-2023-2026.md` merged into `personal/journal-selection.md`. 选刊走 03 `find-journal`；`venue-templates` 只管体例.

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

## Routing labels

Labels only. Not new skills and not a new top layer. Detail: `personal/route.md`.

| Label | Use |
|---|---|
| Evidence | literature, citation-verify, intro-evidence pack |
| Design | study design, radiology-design, protocol ethics |
| Exploration | frontier and the question-to-reference loop |
| Research Administration | ethics forms, grants, journal selection / submit pack |

## Modes

- Evidence: gaps, conflict, mechanism, journal fit. Never invent PMID/DOI.
- Design: question/hypothesis, eligibility, endpoints, sample size, bias, reporting guideline.
- Exploration: frontier and reusable question-to-reference cards.
- Research Administration: ethics forms (**Bai** seats fill-protocol), grants, 选刊 submit pack.
- Translational design: use scenario, reader study, threshold-to-action, prospective/regulatory → `personal/clinical-translation/`.
- Grant-review (Voice A): load **only** `personal/grant-review.md`. English journal peer review stays in `06_review`.
- Grant-writing (Voice B): skeleton + method-upgrade + `personal/grant-writing.md`. Never paste Voice A tics into own text.

**Journal format (nested):** `find-journal/journal-format-compliance/` is invoked after 选刊 when formatting to author guidelines — not a fine id; see that pack's SKILL + parent → Journal format compliance.

## Boundaries

- 选题 / where to submit stays here (`personal/journal-selection.md` + `find-journal/`). 选刊走 03 `find-journal`；`venue-templates` 只管体例.
- Manuscript prose / I/D writing → `05_manuscript`
- Statistics / figures → `04_analysis`
- Data preprocessing / extraction → `02_data-processing`
- Ethics **forms** (fill pack) stay here (`fill-protocol/`); protocol-level ethics → `personal/ethics.md`
- Translational / reader-study **design** stays here (`personal/clinical-translation/`)
- Reviewer response → `06_review`
- Project 选刊结果 / 已投名单 → `<project>/ref/` only — not MY-SKILLS