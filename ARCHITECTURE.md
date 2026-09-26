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
├── mounts-cap/       (local B + on-demand backups; pack bytes gitignored)
└── _medical-research-meta/
```

## Core layers

1. `00_orchestrator` — intent classify, skill chain, QC closed loop (file gates + local recovery; re-run only the broken node, max 3).
2. `01_skill-discovery-integration` — discover, evaluate, and mount; **pointers live only here**; default source B. Local bytes in `mounts-cap/` (full B; backup sources on-demand by picked id). Empty mount → notify, re-search, confirm. Never auto-mount a non-B source. Never literature/stats/writing/review.
3. `02_data-processing` — raw → analysis-ready; Excel/0RAD; imaging QC; radiomics prep; imputation; clinical extraction; coding principles. No modeling. Handoff → 04. Ethics forms are **not** here.
4. `03_research` — research design, **literature (03 only)**, evidence, frontier, grants, translational/reader-study **design**, **ethics application forms**, **选刊**. Personal grant/ethics/translation files are a supplement, not an upper writing layer. 选刊走 03 `find-journal`；`venue-templates` 只管体例.
5. `04_analysis` — statistics, prediction, survival, **figures**. Data repair is not its role. 样本量 is `calc-sample-size`.
6. `05_manuscript` — personal scientific writing upper layer over mounted writing capabilities. Personal de-AI lives at `05_manuscript/personal/`. 选刊走 03 `find-journal`；`venue-templates` 只管体例.
7. `06_review` — personal review/response upper layer. Reviewer response enters 06 only.

`skill-harvest` is governance. It does not replace domain layers. 01 mounts; harvest proposes evolution. Execution QC stays in `00` (incl. **G-FACT** consistency); learning QC is `skill-harvest/qc/` (passive events, on-demand HTML — never auto-modify).

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
- **v4 (CHG-20260913-001):** **10 coarse** stage buckets + **52 fine ids** (session-pick). `session_mount: ask-each-run` — multi-select fine ids under relevant coarse; do not auto-load all. Menu is not `mounts: []`.
- A folders stay `00`–`06` (not renamed to Chinese top-level).
- MedSci / Scientific / AIPOCH / Nature are **PROPOSED backups**. ARS/OpenClaw purged from catalog (`ars_openclaw_policy: removed-from-catalog`). Mapping is not a mount. Never auto-mount a non-B source.
- MedSci-only live interface: `humanize`. Explainability is **ARCHIVED** (not default menu).
- Figures fine ids: `make-figures` / `fig-plot`. No live figure engine.
- Live docs name v4 fine ids only. Sample-size fine ids sit under coarse 统计分析 (04 / Loopnow).
- Archived fine ids: see registry `archived:`.



## Fine-id expansion ceiling (v4)

**52 fine ids is the v4 expansion ceiling.** Do not create new fine ids for new capabilities by default.

Default path for a new capability:

1. **Merge** into an existing fine id (same coarse bucket / same atomic skill folder), or
2. Add a **sub-capability** / notes under that fine id’s source path, or
3. Reuse the **same source-path** already indexed by the registry.

Opening a 53rd fine id requires explicit architecture review (not Batch default).

## Cache ≠ Mount ≠ Active

| Concept | Meaning |
|---|---|
| **Cache** | Bytes on disk under `mounts-cap/<pack>/` (gitignored pack trees). Download/fetch only. |
| **Mount** | Registry fine-id pick for this session (`ask-each-run`). Pointers live in `01_skill-discovery-integration`. |
| **Active** | Actually loaded into the agent context this run. |
| **Registry** | Index only — not the skill body. External entity SSOT is the cache (`mounts-cap/<atomic_package>/…`). `stub_in_b` is pointer-only. |

## load_priority (YAML metadata only)

Optional `load_priority: P0|P1|P2` on each registry fine id. **No P0/P1/P2 directories.**

- **P0** — reserved for rare always-on mounts (chassis is `00`–`06`, not fine ids).
- **P1** — common mounts (e.g. verify-refs, write-paper, check-reporting, analyze-stats, make-figures/fig-plot, peer-review, lit-search, imaging-io, preprocess-imaging, revise, self-review).
- **P2** — niche / PROPOSED / specialty.

## Routing rules

- Literature research → `03_research` only.
- 选刊 / where to submit → `03_research` (`literature/journal-selection.md` + `medical-journal-submit/`; evidence `lit-search`). 选刊走 03 `find-journal`；`venue-templates` 只管体例.
- 样本量 → `04_analysis` (`calc-sample-size`).
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
- `03_research/clinical-translation` — translational / reader-study **design** (personal supplement; generic templates may later mount at `design-study` / `write-protocol`)

## A/B no-reflow contract

| Side | Role |
|---|---|
| **A** (this repo) | Framework + Personal Authority (orchestration, personal style, lab constraints, final say) |
| **B** (`MY-SKILLS-capabilities`) | Generic Capability (mountable workers; no personal voice) |

**B → A allowed:** finding / evidence / capability / recommendation.

**B → A forbidden:** personal preference, personal style, or personal decision rules.

**A → B only:** interface / task / context / constraints — **never** bake personal style or lab decision rules into B.

Mounting stays in `01`. Evolution proposals stay in `skill-harvest` (user approval). Execution QC stays in `00`.

## Design rules

**One fact → one authoritative home.**
**One task → one entry point.**
**Nested MODULE ≠ discoverable Skill.**
**Do not delete local generic capability until the user moves it to B (or an approved mount covers it).**
**User approval is mandatory for mounting or evolution.**
**Never auto-mount.**
