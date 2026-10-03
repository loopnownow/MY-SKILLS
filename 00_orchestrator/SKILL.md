---
name: medical-research-orchestrator
description: >
  Intent-classify the task, run a skill chain, and close QC (file gates + local
  recovery). Use for end-to-end or multi-stage work. Do not use when a single
  domain skill is enough. Do not do literature, stats, writing, or review here.
---

# Medical Research Orchestrator

00 is the lab dispatcher. The live loop is **intent classify → skill chain → QC gate → local recovery**.
It does not duplicate research, statistical, imaging, writing, or discovery rules.

**唯一官方运行图：** [`runtime-flow.mmd`](runtime-flow.mmd)（读图说明 [`runtime-flow.md`](runtime-flow.md)）。入口 / QC / 局部回退以该图为准；更新流程时**只改这一张 mmd**。子流程是图上分支。Gate 条文仍以 [`gates.md`](gates.md) 为真源。

Specialists: 03 Victor (literature / design / 选刊 / ethics forms / Voice B grant / **citation-verify**); 02+04 Loopnow; 05 Aitee (manuscript + Evidence QC; owns all manuscript Track Changes; does not self-certify lit); 06 Lee (statement consistency, then data consistency; marks/comments and must not self-revise as default; lit accuracy is joint with Victor); 00 Aitor owns QC. 05 and 06 require 03 participation for citations. Mid-entry stays allowed. 投稿 is Bai after 06, not this loop. Per-paper channel seats all six (max).

**Word revise ownership:** All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.
Do not mount MedSci `orchestrate` as a third SOP.

**Comments / conflicts:** Word author field is always **A** (never yellow). Source-prefix rules (author ≠ prefix; mount-driven items must show **skill-level** prefixes (`[Nature:nature-reviewer]`, `[Scientific:scientific-critical-thinking]`, `[B:peer-review]`, …) — not source-only shells) live in `06_review/personal/personal-review-style.md` §0 — do not duplicate here. Mount advice that conflicts with lab rules stays in the comment with a concrete edit plan; **the user decides**. 00 does not silently prefer the mount.

**Citation verify (required):** before a 05 deliverable is done (Gate · 05) and inside every 06 review, 03 runs `03_research/personal/citation-verify.md` (claim→ref table + spot-check of strong claims). 05 and 06 call/require 03 citation-verify — do not self-certify lit. A 05 pass does not waive 06. Mid-entry does not waive it. Lee still does statement consistency, then data consistency. Literature accuracy is joint with Victor.

**Literature verify fail (G-LIT):** require a dual plan in comments — (1) revise/weaken/delete the sentence, (2) keep the sentence and ask whether to call `03_research` for substitute refs. Prefer the Evidence Request card in `05_manuscript/personal/evidence-request.md` when a mount (or 05/06) raised a structured gap. The verify pass itself is not optional. **00 decides at QC** only whether a further substitute-ref search runs; **05 (Aitee)** keeps Accept/Weaken/Delete on wording. If unsure, ask one question.

## HTML delivery (standing)

Whenever this lab **creates or edits** `.html`, follow `references/html-visual-design.md` (structure, a11y, no CDN, palette). Full-repo HTML architecture audits are **off** until the user asks. Do **not** vendor lab console / starter HTML pages into MY-SKILLS (rules only).

## Visualization compiler (standing)

Archify is a read-only visualization compiler. It is not a skill and not a top-level `07` layer. MY-SKILLS sources stay authoritative. Contract: [`visualization-architecture.md`](visualization-architecture.md), [`archify-version.yaml`](archify-version.yaml), [`visualization-source-contract.yaml`](visualization-source-contract.yaml). Rebuild derived files with `python3 scripts/gen_visualization.py`, which renders the two diagrams through the pinned `archify-v3.0.1.zip`. Generated HTML under `docs/` is disposable and is not a fact source. Mount diagrams use registry and preset metadata. Do not crawl `mounts-cap/` to draw them.

## 1. Intent classify

Pick the smallest skill set. One bounded task → that domain skill, not 00.

### Directory detection (before asking)

Look in the working / 0RAD project folder. Echo one lock line when the artifact is clear.

| Artifact found | Implies |
|---|---|
| `settings.ini` | 0RAD project; 02 or 04, not a new scaffold |
| `*-results.html` | numbers exist; may enter `sci-manuscript` |
| `Manuscript_*_house.docx` | writing underway; 05, then maybe 06 |
| reviewer letter / 审稿意见 | `06_review` as entry |
| imaging / ROI / features, no HTML | `radiomics-study` unless the user says otherwise |
| `ref/project-state.yaml` | read `pipeline.stage` and `qc`; do not re-init |

`*-results.html` and a reviewer letter in the same folder, and the user did not name the entry: ask which station. Do not pick the nearer artifact. One bounded task still goes to that skill, not the full SOP.

If detection is unclear, ask **one** question or render **one** decision node. Never two in the same turn. (Multi-node/new-capability entry points use the batched **clarify round** in Plan card instead — that's the one exception.)


### Flow chart approval (skills / mounts)

When the user asks to **use skills or mount packs for a specific task**, before session mount pick or specialist dispatch:

1. Show a **complete** flowchart taken from the official map [`runtime-flow.mmd`](runtime-flow.mmd) (read [`runtime-flow.md`](runtime-flow.md)).
2. The task is **one ring/branch** on that map, or the full chain — still show the **whole** official figure (or a faithful rendering of it), and **highlight** the path this run will take (entry → nodes → gates → QC loop).
3. Wait for **explicit approval**. Do not load mounts or start 02–06 until they agree.
4. After approval, proceed with 01 session mount pick / G0 as on the map.

This sits with Plan card / grilling for multi-node work; for mount/skill runs it is mandatory even when the plan looks obvious.

### Plan card (before dispatch)

Default is **interactive**, not silent automation. Before the first specialist runs a multi-node job, or before 01 evaluates a new external capability, run **grilling** (`grilling/SKILL.md`, `grill-me` mode): one batched clarify round, numbered questions with recommended defaults, find facts yourself first. This is the multi-node / new-capability exception to "ask one question, never two" (single-skill tasks keep that rule as-is).

Then show the plan: candidate mount ids · SOP · node order · risk gates. Wait for a nod. Do not invent `--e2e`.

Loop shape: `clarify round (grilling) → plan → execute node → file check → integrity gate → (repair broken node only) → execute`. Not a single straight line.

After that plan is approved, later crossings in the **same run** are one line: file present, gate passed, continue or pause. Still stop and wait at N2 (PHI), G-FACT on the results page, N4 (preview entry), and G-06.

### Decision nodes (one at a time)

After a pick, echo `Locking: …` then invoke the specialist. `back` / `pause` allowed. Do not skip N2.

| Node | When | Options |
|---|---|---|
| N1 SOP | 「全线」 / multi-stage with no lock | `radiomics-study` / `sci-manuscript` / `research-exploration-loop` / no SOP (single skill) |
| N2 PHI | before 02 tables or clinical extraction | PHI present → de-identify / stop; none → proceed |
| N3 WRITE | `*-results.html` exists after 04 | stop at HTML / enter `sci-manuscript` |
| N4 PREVIEW | house.docx exists | enter 06 / stop |

Never `--e2e`. Never skip session mount pick or N2.

### Fast routing (single-skill)

- 新技能 / 外接 / 挂载 → `01_skill-discovery-integration`
- grill-me / grill-with-docs / 盘问 / 烤透需求 / 需求不清楚就要写代码 → `00_orchestrator` (`grilling`)
- Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`
- 软编码 / dry-run / coding principles → `02_data-processing` (`code-refactoring`)
- 伦理申请表 → `03_research` (`ethics-application-forms`)
- 提取检验 / HIS → `02_data-processing` (`clinical-data-extraction`)
- 转化 / reader study / 前瞻部署 / 阈值到行动 → `03_research` (`clinical-translation`)
- MRI / DICOM / NIfTI / 预处理 / radiomics 准备 / 插补 → `02_data-processing`
- 选题 / 研究设计 / **文献** → `03_research`
- 选刊 → `03_research`
- 样本量 → `04_analysis` (`calc-sample-size`)
- 统计 / AUC / DeLong / DCA / **出图** → `04_analysis`
- 写作 / 润色 / 引言 / Discussion / de-AI → `05_manuscript`
- 预审 / 审稿 / **回复审稿人** → `06_review`
- 技能迭代 / 收益评估 → `skill-harvest`

## 2. Skill chain

### Routing

| Skill | Primary scope |
|---|---|
| `01_skill-discovery-integration` | Discover / evaluate / mount external Skills. Never literature, stats, writing, or review. |
| `02_data-processing` | Raw → analysis-ready data. Excel/CSV, 0RAD workspace, imaging QC, radiomics prep, imputation, **clinical extraction**, **coding principles**. No modeling. |
| `03_research` | Study design, **literature**, evidence, frontier, journal/topic (选刊), grants, **translational / reader-study design**, **ethics application forms**, **citation-verify** for 05 and 06. Literature enters 03 only. 选刊走 03 `find-journal`；`venue-templates` 只管体例. |
| `04_analysis` | Statistics, prediction, survival, **figures**. Data repair is not its role. |
| `05_manuscript` | Personal SCI writing / polish / de-AI. Not figures. Not reviewer response. Owns all manuscript Track Changes. Lee marks/comments; Aitee applies Track Changes. Requires 03 citation-verify before done. Does not self-certify lit. |
| `06_review` | Pre-submission, peer review, **reviewer response only here**. Does not write the paper. Lee must not self-revise as default. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed. |
| `skill-harvest` | Evolution / ROI / boundaries. Not a research domain. |

There are **no archive-as-standalone routes**. The four former archive packs live under 02/03.

### Session mount pick

Before routing or loading 02–06, run **01 session mount pick**: ask which packs to mount **this run**, then load only those. Registry `MOUNTED` is the menu, not an auto-attach. Unpicked packs stay unloaded. Personal layers are not a mount pick.

### Composite workflows

SOPs live in `workflows/` (ask which SOP on 「全线」, node N1, unless directory detection already locked it):

- Full project: `03_research` → `02_data-processing` (if data/imaging) → `04_analysis` → `05_manuscript` → `06_review`. 05 and 06 each require a 03 citation-verify pass.
- Imaging prediction paper: `03_research` → `02_data-processing` → `04_analysis` → `05_manuscript` → optional `06_review`. Writing still requires citation-verify before done.
- Manuscript revision: `05_manuscript` for prose; `06_review` for audit/response. Both require 03 citation-verify. Mid-entry does not waive it.
- Reviewer response: **`06_review` only as entry**; `05_manuscript` for changed sentences; `04_analysis` / `02_data-processing` only if new analysis or imaging verification is required. The 06 pass still includes 03 citation-verify.
- New capability: `01_skill-discovery-integration` runs its **GitHub discovery workflow** (search → license/domain/overlap/granularity checklist → recommendation table → `grill-me` confirmation before writing anything). Never auto-mount.

`radiomics-study` stops at HTML and **offers** `sci-manuscript` (N3). `sci-manuscript` requires HTML; do not start it from scratch stats.

### Data-flow contract

| Node | Writes (must exist before next) | Next reads |
|---|---|---|
| 02 | analysis-ready table / aligned IDs | 04 |
| 04 | one `*-results.html` per endpoint | 05 (numbers **only** from HTML) |
| 05 | `Manuscript_<结局>_house.docx` | 06 |
| 06 | pre-review or response; inventable items = questions | user, then 05 for sentences |
| 00 | `ref/project-state.yaml` + last `handoff.yaml` | every later node |

Copy `templates/handoff.yaml` at each skill crossing. Fill only known fields. Never invent n, AUC, PMID, or ethics IDs.

### Post-skill file check

After each node, verify the expected output **file exists and is non-empty**. Missing → do not start the next skill. Log the miss on `qc` / `defects` in `project-state.yaml`.

Project state template: `templates/project-state.yaml`.

## 3. QC closed loop

00 owns the last gate. Detail: `gates.md`. A task is complete only when the requested deliverable exists, major consistency checks pass, assumptions are visible, limitations are stated, and files are usable.

Integrity gates (not after every node):

| Gate | When | Fail if |
|---|---|---|
| G0 | every run | packs loaded without session mount pick; silent empty-mount fallback |
| G-PHI | before 02 tables / extraction | PHI status unknown; HIS credentials in files |
| G-04 | after `*-results.html` | invented n/AUC; `Development set`; VAL_MODE rewritten; DeLong sold as CI |
| G-FACT | after 04 HTML / after 05 docx | N/split/model/endpoint/AUC·CI·P drift vs upstream FILE |
| G-05 | after house.docx | numbers ≠ HTML; Methods citations; Table 1 not training vs test; 00 wrote prose; pre-submit-consistency checks left unresolved in the body; 03 citation-verify missing or self-certified by 05 |
| G-06 | after pre-review / response | fabricated reviewer facts; 选刊 routed to 05; Lee applied manuscript Track Changes (Lee must not self-revise as default; Lee marks/comments; Aitee applies Track Changes); decidable issues not annotated for Aitee to TC-fix; undecidable issues missing a Chinese 批注 body or the attached English suggested wording and/or suggested literature; resolution status when review-resolution protocol used; cross-manuscript conflicts rewritten instead of commented; 03 citation-verify skipped; if this run mounted a non-personal source, ≥1 comment prefix must name that source |
| G-LIT | citation-verify required before 05 done and inside 06; on fail | dual plan in comments (revise sentence **and** optional further 03 substitute refs); no invented PMID; verify pass itself is not optional |

Cross-cut Consistency is **G-FACT** (see `gates.md`). Learning/evolution QC lives in `skill-harvest/qc/` (record-only unless user asks for evolution HTML).

**Local recovery:** if QC finds a localized defect, identify the responsible skill and re-run **only the broken node**. Max **3** rounds on the same defect, then list it under `defects[]` as `unresolved` and stop. Do not advance `pipeline.stage`. Do not rerun already-correct stages. When the repair is prose, instruct **word/sentence units** only. Visual: FAIL → Locate → Impact → Local/Rollback → Budget → Resume in [`runtime-flow.mmd`](runtime-flow.mmd).

**Close.** Write `pipeline.stage` from the template values already listed there.

- 结束, or the file this run asked for is on disk and the last gate passed → `done`. Do not open the next SOP.
- 暂停 → leave `stage` at the current station. The next session reads it and does not re-init.
- Stop after the results page, or stop before pre-review → leave `stage` at `04` or `05`. That stay is not `done`.

`intent → chain node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

## Research exploration (sub-component)

Triggers such as 「这个研究还能做什么」「还缺哪些文献」「研究空白」「选题探索」 may enter [`workflows/research-exploration-loop.md`](workflows/research-exploration-loop.md): state resume, reuse completed work, dispatch **existing** 03/04 mounts (`lit-search`, `frontier-hypothesize`, …), L1 = gate recovery, L2 = cross-stage cap 3. Not a fine id. 00 stays structural-only.

## Boundaries

**00 owns runtime decisions only:** intent classify, skill chain / route, session mount pick coordination, QC gates, and local recovery. Domain knowledge (stats, writing, literature, review, figures, ethics forms, clinical extraction, coding principles) stays in `02`–`06` (and harvest for evolution proposals).

**Lab SSOT (not owned as file trees by 00):** runnable code → `D:\0Grok\0scripts`; human-facing archives / long static refs → `D:\0Grok\0doc`; skills keep procedures + pointers only (see `ARCHITECTURE.md` · Lab workspace SSOT). Do not vendor those trees into MY-SKILLS.

Before adding content to `00`, ask: **runtime decision vs domain knowledge?** If domain knowledge → put it in the owning specialist skill, not here.

Do not create a top-level skill for a disease, package, manuscript section, statistical test, metric, or imaging modality.
Do not load all nested material. Load the selected `SKILL.md`, then only the required files.
Mounted generic capability: ids in `MOUNTED_SKILLS.md` / `registry.yaml`. **This-run pick first** (01). Point at **picked ids**, not deleted `bundles/` paths.
00 does not write manuscript prose, invent numbers, or click 投稿.
00 does not absorb harvest evolution rules or 01 mount implementation — those stay in `skill-harvest` and `01_skill-discovery-integration`.
