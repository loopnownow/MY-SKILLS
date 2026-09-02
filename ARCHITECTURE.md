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
2. `01_skill-discovery-integration` — discover, evaluate, and mount external Skills; infrastructure only. Never literature/stats/writing/review. Never auto-mount.
3. `02_data-processing` — raw → analysis-ready; Excel/0RAD; imaging QC; radiomics prep; imputation; clinical extraction; coding principles; ethics form packs (temporary parking). No modeling. Handoff → 04.
4. `03_research` — research design, **literature (03 only)**, evidence, frontier, journals, grants, translational/reader-study **design**. Personal grant/ethics/translation files are a supplement, not an upper writing layer.
5. `04_analysis` — statistics, prediction, survival, **figures**. Data repair is not its role.
6. `05_manuscript` — personal scientific writing upper layer over mounted writing capabilities.
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

## Routing rules

- Literature research → `03_research` only.
- Reviewer response → `06_review` only.
- Data preprocessing / Excel / 0RAD / extraction / coding principles / ethics forms (temp) → `02_data-processing`.
- Translational / reader-study design → `03_research` (`clinical-translation`).
- Statistics and figures → `04_analysis`.
- Scientific writing/polishing → `05_manuscript`.
- New external capability → `01_skill-discovery-integration` (network first, then ask for a local path).
- Evolution proposals → `skill-harvest` and explicit user approval.

## Rehomed packs (no longer standalone)

- `02_data-processing/code-refactoring` — soft-coding / dry-run / CONFIG on top
- `02_data-processing/ethics-application-forms` — ethics application forms (**temporary**; true home is 03 ethics design)
- `02_data-processing/clinical-data-extraction` — clinical/HIS extraction
- `03_research/clinical-translation` — translational / reader-study **design** (personal supplement; generic templates may later mount at B `03-research/design`)

## Design rules

**One fact → one authoritative home.**
**One task → one entry point.**
**Nested MODULE ≠ discoverable Skill.**
**Do not delete local generic capability until an approved mounted replacement covers it.**
**User approval is mandatory for mounting or evolution.**
**Never auto-mount.**
