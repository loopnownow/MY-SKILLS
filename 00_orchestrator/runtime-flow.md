# 唯一官方运行图

**机器真源（只改这一张）：** [`runtime-flow.mmd`](runtime-flow.mmd)

子流程（写作链、审稿链、0RAD、修回分诊）都是该图上的**分支**，不另立主图。更新入口 / QC / 回退规则时只修订 `.mmd`。

00 = 控制层（入口、调度、Gate、回退）。业务在 02–07；外挂版本与缓存在 **01**；技能演进政策见 `references/skill-evolution.md`（skill-harvest 已归档），只观察与提案，不执行流程。



## Base / personal layering

**Main loop:** base fine-ID **first-pass** capability loops -> **00 QC gate** -> personal/top **re-loops**.

| Layer | Repo | Owns |
|---|---|---|
| **base** | MY-SKILLS `NN_slug/base/` | Capability bodies / fine-ID loops |
| **00** | MY-SKILLS `00_orchestrator` | QC gate between base first-pass and personal/top re-loop |
| **personal / top** | MY-SKILLS | Personal top-layer route/handoff/authority (A03-A07). Capability bodies for 02–07 live under `NN_slug/base/` |

Post-QC A re-loops (as needed):

- **A03** -- may trigger `verify-refs` + `retraction-watcher` (bodies under `NN_slug/base/`)
- **A05** -- `polish-language` -> `humanize` alongside Aitor-format/voice; vocab on first write
- **A06** -- post-QC **re-review only**
- **A07** -- **final authority for response** (`revise`/`tighten-response`/`response-tone-polisher` source my-skills (in-repo base))

Do not change fine IDs for stats-analysis / figures / data-processing / study-design.


## Seats on the map (2026-10-17 tidy)

| Coarse | Seat | On-map role |
|---|---|---|
| 02 + 04 | Loopnow | data / stats / figures |
| 03 | Victor | research / lit / 选刊 / citation-verify |
| 05 | Aitee | manuscript prose + Track Changes |
| **06** | **Lee** | **review / pre-review / re-review only** |
| **07** | **Aitee** | **response letter final authority** |
| 00 | Aitor | QC / gates / chain |
| (off-loop) | **Bai** | ethics forms (`03_research/base/fill-protocol`) + portal submit |

**Response → 07 / Aitee. Review → 06 / Lee.** Do not route 回复 to 06. Gate ids (`G0`, `G-PHI`, `G-FACT`, `G-LIT`, `G-CODE`, `Gate · 04/05/06/07`) stay stable.


## 读图要点

1. **Detect 定入口与终点**——已有 HTML 可停在 05，不必强进 06。已有统计可中途进 05，已有稿件可中途进 06，不必从 02 重跑。结果页和审稿信同时在、且没有点名入口时，先问从哪一站进。多节点 / 新能力 / 要用挂载时先 grilling + Plan card + 流程图审批。`结束` 或本次文件已在且最后一门 PASS → `pipeline.stage: done`。暂停，或停在结果页后 / 预审前，stage 留在当前站。**同一缺陷** `defects[].rounds` 第 3 轮仍失败：`unresolved`，stage 不往前（不是全局 `qc.rounds`）。同一次已批准运行里，后续过站报一行；患者信息、结果页数字、预审入口、审稿门仍停住。**凡写作或审稿（含中途进入）**，Gate · 05 的 done 之前、以及 06 审稿之内，必须经过 03 `citation-verify`（claim→ref 表 + 强断言抽查原文）。05 的核实不免除 06。Aitee 与 Lee 不得自证文献。Lee 仍先陈述一致、再数据一致；文献准确性与 Victor 共同负责。Ownership: see `00_orchestrator/references/ownership-contract.md`.
2. **PASS 才前进**——每节点出口 Gate；未到终点则进入下游。
3. **01/G0 = 执行前依赖**——每次独立运行需要一次挂载决定。`session_picked_fine_ids` 已覆盖本任务细 ID 时复用 session lock，不重问。否则进入 01。单节点个人层、且没有挂载依赖时不问（例：润色一句）。不是装饰性总闸门。
4. **QC 环**——FAIL → 定位 → 影响判断（局部 vs 回退到最早受影响节点）→ 预算内重入失败节点 → 再 Gate；禁止从 Start 整链重跑。局部恢复复用 session mount lock 并回到失败节点。只有依赖缺失、provenance 过期、或需要新能力时才重进 01。
5. **预算用尽**——Escalate → 等用户；授权后重置**该缺陷**的 `defects[].rounds`。
6. **命名**——图中 `Gate · NN` ↔ `gates.md` 的 `G-NN`（例：`Gate · 04` = `G-04`）。`G0` / `G-PHI` / `G-FACT` / `G-LIT` / `G-CODE` 同名。

## Gate 选用（真源 `gates.md`）

图中 `Gate · NN` = 按下表选取的集合（细节与失败列以 `gates.md` 为准）。

| 任务 / 节点 | 适用 Gate |
| --- | --- |
| 01 外部 Skill / Mount | G0。仅当本次需要新的挂载决定时进入 |
| 02 数据处理 | 出口是 G0 + G-PHI（适用时）+ 产物存在，然后进入 04。不单列 02 门禁编号，也没有 02 自己的 G-FACT。N2 = PHI 停点 |
| 02 personal/coding.md / 代码深审 | G-CODE |
| 03 文献研究 | 出口是 G0 + G-LIT + 证据/引文产物。不单列 03 门禁编号，也没有 03 自己的 G-FACT |
| 04 统计 / 图表 | G0 + G-FACT（04 HTML 之后的事实链）+ G-04。数与图来自 HTML / settings；报告规范清单不归 G-04。N3 WRITE = 停 HTML 或进写作 |
| 05 论文写作 | G0 + G-FACT（05 house.docx 之后再核）+ G-LIT + G-05（含 style-lint 子检）。Gate · 05 / done 之前必须有 03 citation-verify PASS（语义标签 **G-CIT-1**，草稿证据核实；`03_research/personal/citation-verify.md`）。N4 PREVIEW = 进 06 或停 |
| 07 回复审稿人 | G0 + response resolution + G-LIT when cites appear; A07 final authority; revise/tighten-response/response-tone-polisher stay source my-skills (in-repo base) |
| 06 审稿 / 修回 | G0 + G-LIT + G-05 + G-06；引用了数字时再跑 G-FACT（`gates.md` 已写 before 06 if numbers cited）。06 内 citation-verify 语义标签 **G-CIT-2**（修订后 / 06 内），不可跳过；G-CIT-1 不免除 G-CIT-2。Lee 管陈述一致然后数据一致，文献准确性与 Victor 共同负责。Ownership: see `00_orchestrator/references/ownership-contract.md` |
| 完整 02→04→05→06 | 各节点出口按上表；G-FACT 只在 04 HTML 之后、05 house.docx 之后，以及 06 引用数字时 |

个人层（写作风格 / 审稿框架）= `05_manuscript/personal`、`06_review/personal`。句权与裁决在个人层；能力正文在 `NN_slug/base/`。

## 调度冲突（摘要）

用户指定 → 主控 Skill → 必要上游 → 必要外挂 → 个人层 → 辅助 → QC。  
冲突：A 个人层优先于外挂包；同一 fine ID 单源。**QC 回退优先于正常调度顺序。**

- G-05 includes the `style-lint` sub-check (see gates.md). No new gate ID. Do not add a 02-only or 03-only gate id. Citation-verify is a branch on `runtime-flow.mmd` (Lit05 / semantic label G-CIT-1 before Gate · 05; Lit06 / semantic label G-CIT-2 inside 06). G-CIT-1 does not waive G-CIT-2. These labels are not new gate ids.

## Integrity · pre-06 / post-re-review (named nodes, not new gate ids)

**Inspired by ARS pipeline topology** (short original text only; no ARS copy).

| Node | Where | Reuses (existing gates/checks) | On FAIL |
|---|---|---|---|
| **Integrity · pre-06** (`I25`) | After Gate · 05 / N4→06, and mid-entry Need06 (Mount→Ready→…→Dispatch→I25→P06) | **G-FACT** (when numbers cited) + **G-CIT-1** evidence already required before Gate · 05 + short AI-failure / manuscript-local-qc spot checklist (`05_manuscript/qc/manuscript-local-qc.md`) | HARD-style block before Lee 06 (same recovery as G-FACT / G-CIT) |
| **Integrity · post-re-review lite** (`I45`) | After `P06r` 06 re-review | G-FACT spot + AI-fail lite (not full first-pass) | Locate / local rework |

Do **not** invent a new `G-*` id for these stations. They are compositions documented in `gates.md`.


## Review ↔ revise topology (R&R)

After 06 first-pass findings that need fix:

1. **Rev** decision → **05** (body Track Changes, Aitee) and/or **07** (response letter, Aitee).
2. Body fixes return to **`P06r` 06 re-review** (Lee): **verification only**; Round-1 findings frozen; fill R&R traceability (`00_orchestrator/templates/rr-traceability.md`).
3. **I45** integrity-lite → optional second revise (same Rev) → final out.
4. **Cap:** re-review loops ≤ **2**; then escalate / `unresolved` like `defects[].rounds`.

Seats unchanged: **Lee = 06 review/re-review**; **Aitee = 05 + 07**. Do **not** route response to 06.


## Checkpoint tiers (FULL / SLIM / MANDATORY)

| Tier | When | Behavior |
|---|---|---|
| **FULL** | Decision points (entry/plan, N2/N3/N4, gate FAIL needing user choice, budget escalate) | Show options; wait for explicit decision |
| **SLIM** | User already said continue / same approved run next station | One-line status; do not re-grill |
| **MANDATORY** | Integrity FAIL (I25/I45), review decision (Rev / re-review verdict), before `stage: done` | Must stop for user (or recorded PASS) |

**Rule:** after **≥4 consecutive SLIM continues**, force the next checkpoint to **FULL**.


## Domain QC standards (not capability bodies)

Pass/fail checklists live under domain `qc/` only: `05_manuscript/qc/` (Gate · 05 / Integrity · pre-06) and `06_review/qc/` (Gate · 06 / `P06r` re-review). 00 loads them at gate time; specialists do not self-certify via `qc/`. See `gates.md` Manuscript local QC + Integrity compositions.

## Before skills / mounts (standing)

When the user requests skills or external mounts for a concrete task: show this official map in full, highlight the run path, and **wait for approval** before 01 pick or specialist execution. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse that lock after approval instead of asking again. A single-node personal-layer task with no mounted dependency does not ask (example: polish one sentence). Do not invent a second master diagram — only highlight branches on `runtime-flow.mmd`.

Personal layers also include `07_response/personal` (response final authority). Flow: base fine-ID first-pass -> 00 QC -> personal/top re-loop.
