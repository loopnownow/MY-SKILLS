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

Specialists: 02+04 Loopnow; 03+05 Aitee; 06 Lee; 00 Aitor owns QC. 投稿 is Bai after 06, not this loop.
Do not mount ARS `academic-pipeline` or MedSci `orchestrate` as a third SOP.

**Comments / conflicts:** Word comments are author **A** (never yellow). Tag source (`[A:personal]`, `[06-…]`, `[B:…]`, …). Mount advice that conflicts with lab rules stays in the comment with a concrete edit plan (before/after sentence); **the user decides**. 00 does not silently prefer the mount.

**Literature verify fail (G-LIT):** require a dual plan in comments — (1) revise the sentence, (2) keep the sentence and ask whether to call `03_research` for substitute refs. **00 decides at QC** whether to invoke 03; if unsure, ask one question.

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

If detection is unclear, ask **one** question or render **one** decision node. Never two in the same turn.

### Plan card (before dispatch)

Default is **interactive**, not silent automation. Before the first specialist runs a multi-node job, show a short plan: candidate mount ids · SOP · node order · risk gates · what you will ask the user. Wait for a nod. Do not invent `--e2e`.

Loop shape: `plan → execute node → file check → integrity gate → (repair broken node only) → execute`. Not a single straight line.

### Decision nodes (one at a time)

After a pick, echo `Locking: …` then invoke the specialist. `back` / `pause` allowed. Do not skip N2.

| Node | When | Options |
|---|---|---|
| N1 SOP | 「全线」 / multi-stage with no lock | `radiomics-study` / `sci-manuscript` / no SOP (single skill) |
| N2 PHI | before 02 tables or clinical extraction | PHI present → de-identify / stop; none → proceed |
| N3 WRITE | `*-results.html` exists after 04 | stop at HTML / enter `sci-manuscript` |
| N4 PREVIEW | house.docx exists | enter 06 / stop |

Never `--e2e`. Never skip session mount pick or N2.

### Fast routing (single-skill)

- 新技能 / 外接 / 挂载 → `01_skill-discovery-integration`
- Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`
- 软编码 / dry-run / coding principles → `02_data-processing` (`code-refactoring`)
- 伦理申请表 → `03_research` (`ethics-application-forms`)
- 提取检验 / HIS → `02_data-processing` (`clinical-data-extraction`)
- 转化 / reader study / 前瞻部署 / 阈值到行动 → `03_research` (`clinical-translation`)
- MRI / DICOM / NIfTI / 预处理 / radiomics 准备 / 插补 → `02_data-processing`
- 选题 / 研究设计 / **文献** → `03_research`
- 选刊 → `03_research`
- 样本量 → `04_analysis` (`04-stats-power`)
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
| `03_research` | Study design, **literature**, evidence, frontier, journal/topic (选刊), grants, **translational / reader-study design**, **ethics application forms**. Literature enters 03 only. 选刊 is 03, not `05-write-venue`. |
| `04_analysis` | Statistics, prediction, survival, **figures**. Data repair is not its role. |
| `05_manuscript` | Personal SCI writing / polish / de-AI. Not figures. Not reviewer response. |
| `06_review` | Pre-submission, peer review, **reviewer response only here**. Does not write the paper. |
| `skill-harvest` | Evolution / ROI / boundaries. Not a research domain. |

There are **no archive-as-standalone routes**. The four former archive packs live under 02/03.

### Session mount pick

Before routing or loading 02–06, run **01 session mount pick**: ask which packs to mount **this run**, then load only those. Registry `MOUNTED` is the menu, not an auto-attach. Unpicked packs stay unloaded. Personal layers are not a mount pick.

### Composite workflows

SOPs live in `workflows/` (ask which SOP on 「全线」, node N1, unless directory detection already locked it):

- Full project: `03_research` → `02_data-processing` (if data/imaging) → `04_analysis` → `05_manuscript` → `06_review`
- Imaging prediction paper: `03_research` → `02_data-processing` → `04_analysis` → `05_manuscript` → optional `06_review`
- Manuscript revision: `05_manuscript` for prose; `06_review` for audit/response
- Reviewer response: **`06_review` only as entry**; `05_manuscript` for changed sentences; `04_analysis` / `02_data-processing` only if new analysis or imaging verification is required
- New capability: `01_skill-discovery-integration` (network first, then ask for a local path). Never auto-mount.

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
| G-05 | after house.docx | numbers ≠ HTML; Methods citations; Table 1 not training vs test; 00 wrote prose |
| G-06 | after pre-review / response | fabricated reviewer facts; 选刊 routed to 05 |
| G-LIT | after lit verify fail in 05/06 | dual plan in comments (revise sentence **and** optional 03 substitute refs); no invented PMID |

**Local recovery:** if QC finds a localized defect, identify the responsible skill and re-run **only the broken node**. Max **3** rounds on the same defect, then list it under `defects[]` as `unresolved` and stop. Do not rerun already-correct stages. When the repair is prose, instruct **word/sentence units** only.

`intent → chain node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

## Boundaries

Do not create a top-level skill for a disease, package, manuscript section, statistical test, metric, or imaging modality.
Do not load all nested material. Load the selected `SKILL.md`, then only the required files.
Mounted generic capability: ids in `MOUNTED_SKILLS.md` / `registry.yaml`. **This-run pick first** (01). Point at **picked ids**, not deleted `bundles/` paths.
00 does not write manuscript prose, invent numbers, or click 投稿.
