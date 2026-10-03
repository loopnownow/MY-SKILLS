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
├── mounts-cap/       (verified local cache, not the source of truth; pack bytes gitignored)
└── _medical-research-meta/
```

## Core layers

1. `00_orchestrator` — intent classify, skill chain, QC closed loop (file gates + local recovery; re-run only the broken node, max 3).
2. `01_skill-discovery-integration` — discover, evaluate, and mount; **pointers live only here**; default source B. Local bytes in `mounts-cap/` are a verified local cache, not the source of truth. Non-B packages are mixed PROPOSED/MOUNTED per registry.yaml; upstream (the B repo, or the non-B upstream) is the source of truth for those bytes. Empty mount → notify, re-search, confirm. Never auto-mount a non-B source. Never literature/stats/writing/review.
3. `02_data-processing` — raw → analysis-ready; Excel/0RAD; imaging QC; radiomics prep; imputation; clinical extraction; coding principles. No modeling. Handoff → 04. Ethics forms are **not** here.
4. `03_research` — research design, **literature (03 only)**, evidence, frontier, grants, translational/reader-study **design**, **ethics application forms**, **选刊**. Personal grant/ethics/translation files are a supplement, not an upper writing layer. 选刊走 03 `find-journal`；`venue-templates` 只管体例.
5. `04_analysis` — statistics, prediction, survival, **figures**. Data repair is not its role. 样本量 is `calc-sample-size`.
6. `05_manuscript` — personal scientific writing upper layer over mounted writing capabilities. Personal de-AI lives at `05_manuscript/personal/`. 选刊走 03 `find-journal`；`venue-templates` 只管体例. All manuscript Track Changes are owned by Aitee (05). Lee marks/comments; Aitee applies Track Changes. Requires 03 citation-verify before done; does not self-certify lit.
7. `06_review` — personal review/response upper layer. Reviewer response enters 06 only. Lee must not self-revise as default. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.

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

## Mounts (agrees with `_medical-research-meta/ARCHITECTURE.md`)

- **B is the default source and the default chassis** (`loopnownow/MY-SKILLS-capabilities`). Hybrid mount stays: different fine ids may use different packages; never mix packages inside one fine id.
- Menu shape is `01_skill-discovery-integration/registry.yaml` (`coarse_id_count`, `fine_id_count_canonical`) and the generated `MOUNTED_SKILLS.md`. Do not restate those totals here. `session_mount: ask-each-run` — multi-select fine ids under relevant coarse when a new mount decision is required; reuse `session_picked_fine_ids` when they already cover the task. Menu is not `mounts: []`. The pick menu is status MOUNTED only.
- A folders stay `00`–`06` (not renamed to Chinese top-level).
- Non-B packages are mixed PROPOSED/MOUNTED per registry.yaml, never "all PROPOSED backups". OpenClaw is not a default mount source (`ars_openclaw_policy: removed-from-catalog`). Mapping is not a mount. Never auto-mount a non-B source.
- MedSci-only live interface: `humanize`. Explainability is **ARCHIVED** (not default menu).
- Figures fine ids: `make-figures` / `fig-plot`. No live figure engine.
- Live docs name v4 fine ids only. Sample-size fine ids sit under coarse 统计分析 (04 / Loopnow).
- Archived fine ids: see registry `archived:`.



## Fine-id expansion ceiling (v4)

`fine_id_count_canonical` is the v4 expansion ceiling. Do not create new fine ids for new capabilities by default. Do not restate the number here.

Default path for a new capability:

1. **Merge** into an existing fine id (same coarse bucket / same atomic skill folder), or
2. Add a **sub-capability** / notes under that fine id’s source path, or
3. Reuse the **same source-path** already indexed by the registry.

Opening another fine id past that ceiling requires explicit architecture review (not Batch default).

## Cache ≠ Mount ≠ Active

| Concept | Meaning |
|---|---|
| **Cache** | Bytes on disk under `mounts-cap/<pack>/` (gitignored pack trees). Verified local cache, not a source of truth. Download/fetch only. |
| **Registry MOUNTED** | Catalog-approved and session-selectable. |
| **session_picked_fine_ids** | Selected this run. |
| **Active** | Actually loaded into the agent context this run. Cache is not mount is not active. |
| **Registry** | Routing index — not the skill body. B repo is SSOT for B bytes; non-B upstream is SSOT for those bytes. `stub_in_b` is pointer-only. |

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
- Scientific writing/polishing / de-AI → `05_manuscript` (`05_manuscript/personal/`). Writing or peer review, including mid-entry, still requires `03_research` citation-verify.
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

## Lab workspace homes (with skills)

Skills are **not** the home for production scripts or manuscript archives. These disks are homes for run and read, not a second source of truth for skill bytes.

| Home | Path | Owns |
|---|---|---|
| Skill (judge / route) | this repo / `~\.grok\skills` | Gates, short procedure `references/`, orchestration templates, harvest maintenance scripts |
| Run | `D:\0Grok\0scripts` | `modules` / `tidy` / `stat` / `sync` — executable lab code |
| Read | `D:\0Grok\0doc` | Human-facing docs (theses, submissions, reviews, grants); optional long static refs under `04_实验室参考/` (e.g. Lab-STE at `04_实验室参考/lab-ste/`; skills point via `05_manuscript/personal/lab-ste.md`, do not vendor) |

**Pointer, do not mirror.** Skill text may cite `0scripts` / `0doc` paths; do not vendor those trees into MY-SKILLS. Do not symlink skill `references/` ↔ `0doc`. Migration candidates (list only until user approves a move): `D:\0Grok\0doc\MIGRATE_FROM_SKILLS.md`.

GitHub MY-SKILLS is the A framework source of truth.

## Design rules

**One fact → one authoritative home.**
**One task → one entry point.**
**Nested MODULE ≠ discoverable Skill.**
**Do not delete local generic capability until the user moves it to B (or an approved mount covers it).**
**User approval is mandatory for mounting or evolution.**
**Never auto-mount.**
**Lab run/read SSOT stays on `0scripts` / `0doc` — skills keep rules + pointers only.**
