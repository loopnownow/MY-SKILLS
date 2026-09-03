# MedicalResearch Skills

```text
skills/
├── 00_orchestrator
├── 01_skill-discovery-integration
├── 02_data-processing
├── 03_research
├── 04_analysis
├── 05_manuscript
├── 06_review
├── skill-harvest
├── archive/          (empty of skills; packs rehomed)
└── _medical-research-meta/
```

## Core layers

1. `00_orchestrator` — classification, routing, composite workflow, Final QC, local recovery (re-run only the broken node).
2. `01_skill-discovery-integration` — discover, evaluate, and mount; **pointers live only here**; default source B. Empty mount → notify, re-search, confirm. Never auto-mount a non-B source. Never literature/stats/writing/review.
3. `02_data-processing` — raw → analysis-ready; Excel/0RAD; imaging QC; radiomics prep; imputation; clinical extraction; coding principles. No modeling. Handoff → 04. Ethics forms are **not** here.
4. `03_research` — research design, **literature (03 only)**, evidence, frontier, grants, translational/reader-study **design**, **ethics application forms**. Personal grant/ethics/translation files are a supplement, not an upper writing layer. 选刊 is `05-write-venue`.
5. `04_analysis` — statistics, prediction, survival, **figures**. Data repair is not its role. 样本量 is `04-stats-power`.
6. `05_manuscript` — personal scientific writing upper layer over mounted writing capabilities. Personal de-AI lives at `05_manuscript/personal/`.
7. `06_review` — personal review/response upper layer. Reviewer response enters 06 only.

`skill-harvest` is governance. It does not replace domain layers. 01 mounts; harvest proposes evolution.

## Layer principle

```text
L0  Orchestration: 00
L1  Domain frameworks: 02–06
L2  Mounted capabilities: external Skills / MY-SKILLS-capabilities ids
L3  Personal control: 02/03/04 supplements; 05/06 personal upper layers
```

**Mounted Skill owns generic capability. MY-SKILLS owns orchestration, personalization, constraints, and final authority.**

An A skill path is at most four parts from repo root: `<skill>/<category-or-pack>/<scripts|references|personal>/file`. After lifting `core/`, one extra folder is allowed for classification. No fifth folder, no `core/`, no `bundles/`, no `merged/`.

## Mounts (SSOT with `_medical-research-meta/ARCHITECTURE.md`)

- Default source **B** (`loopnownow/MY-SKILLS-capabilities`).
- **30 coarse ids** are registry `MOUNTED` as a **menu**, not `mounts: []`. `session_mount: ask-each-run` — pick before loading packs; do not auto-load all.
- ARS / MedSci / Scientific are **PROPOSED backups**. Mapping is not a mount. Never auto-mount a non-B source.
- MedSci-only: `04-explainability`, `05-humanize`.
- No live `04-figure-engine`. Figures: `04-fig-flow` (STROBE / patient-flow) and `04-fig-plot` (plots).
- Retired ids are not live routes: `02-xlsx`, `02-imaging` (umbrella), `02-impute`, `02-generic-docs`, `03-literature`, `03-design`, `03-frontier`, `04-stats-generic`, `04-figure-engine`, `05-writing-generic`, `06-review-generic`.

## Routing rules

- Literature research → `03_research` only.
- 选刊 → `05_manuscript` (`05-write-venue`).
- 样本量 → `04_analysis` (`04-stats-power`).
- Reviewer response → `06_review` only.
- Data preprocessing / Excel / 0RAD / extraction / coding principles → `02_data-processing`.
- Ethics application forms + translational / reader-study design → `03_research`.
- Statistics and figures → `04_analysis`.
- Scientific writing/polishing / de-AI → `05_manuscript` (`05_manuscript/personal/`).
- New external capability → `01_skill-discovery-integration` (B first; empty → notify then re-search).
- Evolution proposals → `skill-harvest` and explicit user approval.

## Rehomed packs (no longer standalone)

- `02_data-processing/code-refactoring` — soft-coding / dry-run / CONFIG on top
- `03_research/ethics-application-forms` — ethics application forms (fill pack; protocol-level `personal/ethics.md`)
- `02_data-processing/clinical-data-extraction` — clinical extraction of exported txt/docx; HIS clients stay on the hospital machine, never in git
- `03_research/clinical-translation` — translational / reader-study **design** (personal supplement; generic templates may later mount at `03-design-experiment` / `03-design-protocol`)

## Design rules

**One fact → one authoritative home.**
**One task → one entry point.**
**Nested MODULE ≠ discoverable Skill.**
**Do not delete local generic capability until the user moves it to B (or an approved mount covers it).**
**User approval is mandatory for mounting or evolution.**
**Never auto-mount.**
