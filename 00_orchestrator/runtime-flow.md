# 唯一官方运行图

**机器真源（只改这一张）：** [`runtime-flow.mmd`](runtime-flow.mmd)

子流程（写作链、审稿链、0RAD、修回分诊）都是该图上的**分支**，不另立主图。更新入口 / QC / 回退规则时只修订 `.mmd`。

00 = 控制层（入口、调度、Gate、回退）。业务在 02–06；外挂版本与缓存在 **01**；skill-harvest 只观察与提案（经 CHG），不执行流程。

## 读图要点

1. **Detect 定入口与终点**——已有 HTML 可停在 05，不必强进 06。已有统计可中途进 05，已有稿件可中途进 06，不必从 02 重跑。结果页和审稿信同时在、且没有点名入口时，先问从哪一站进。`结束` 或本次文件已在且最后一门 PASS → `pipeline.stage: done`。暂停，或停在结果页后 / 预审前，stage 留在当前站。同一缺陷第 3 轮仍失败：`unresolved`，stage 不往前。同一次已批准运行里，后续过站报一行；患者信息、结果页数字、预审入口、审稿门仍停住。**凡写作或审稿（含中途进入）**，Gate · 05 的 done 之前、以及 06 审稿之内，必须经过 03 `citation-verify`（claim→ref 表 + 强断言抽查原文）。05 的核实不免除 06。Aitee 与 Lee 不得自证文献。Lee 仍先陈述一致、再数据一致；文献准确性与 Victor 共同负责。All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.
2. **PASS 才前进**——每节点出口 Gate；未到终点则进入下游。
3. **01/G0 = 执行前依赖**——每次独立运行需要一次挂载决定。`session_picked_fine_ids` 已覆盖本任务细 ID 时复用 session lock，不重问。否则进入 01。单节点个人层、且没有挂载依赖时不问（例：润色一句）。不是装饰性总闸门。
4. **QC 环**——FAIL → 定位 → 影响判断（局部 vs 回退到最早受影响节点）→ 预算内重入失败节点 → 再 Gate；禁止从 Start 整链重跑。局部恢复复用 session mount lock 并回到失败节点。只有依赖缺失、provenance 过期、或需要新能力时才重进 01。
5. **预算用尽**——Escalate → 等用户；授权后可重置预算。

## Gate 选用（真源 `gates.md`）

图中 `Gate · NN` = 按下表选取的集合（细节与失败列以 `gates.md` 为准）。

| 任务 / 节点 | 适用 Gate |
| --- | --- |
| 01 外部 Skill / Mount | G0。仅当本次需要新的挂载决定时进入 |
| 02 数据处理 | 出口是 G0 + G-PHI（适用时）+ 产物存在，然后进入 04。不单列 02 门禁编号，也没有 02 自己的 G-FACT |
| 03 文献研究 | 出口是 G0 + G-LIT + 证据/引文产物。不单列 03 门禁编号，也没有 03 自己的 G-FACT |
| 04 统计 / 图表 | G0 + G-FACT（04 HTML 之后的事实链）+ G-04。数与图来自 HTML / settings；报告规范清单不归 G-04 |
| 05 论文写作 | G0 + G-FACT（05 house.docx 之后再核）+ G-LIT + G-05。Gate · 05 / done 之前必须有 03 citation-verify PASS（语义标签 **G-CIT-1**，草稿证据核实；`03_research/personal/citation-verify.md`） |
| 06 审稿 / 修回 | G0 + G-LIT + G-05 + G-06；引用了数字时再跑 G-FACT（`gates.md` 已写 before 06 if numbers cited）。06 内 citation-verify 语义标签 **G-CIT-2**（修订后 / 06 内），不可跳过；G-CIT-1 不免除 G-CIT-2。Lee 管陈述一致然后数据一致，文献准确性与 Victor 共同负责。Lee marks/comments; Aitee applies Track Changes. Lee must not self-revise as default |
| 完整 02→04→05→06 | 各节点出口按上表；G-FACT 只在 04 HTML 之后、05 house.docx 之后，以及 06 引用数字时 |

个人层（写作风格 / 审稿框架）= `05_manuscript/personal`、`06_review/personal`（勿称 B05/B06，以免与 capabilities 的 B 包混淆）。句权与裁决在个人层；外挂只提供能力 / findings。

## 调度冲突（摘要）

用户指定 → 主控 Skill → 必要上游 → 必要外挂 → 个人层 → 辅助 → QC。  
冲突：A 个人层优先于外挂包；同一 fine ID 单源。**QC 回退优先于正常调度顺序。**

- G-05 includes the `style-lint` sub-check (see gates.md). No new gate ID. Do not add a 02-only or 03-only gate id. Citation-verify is a branch on `runtime-flow.mmd` (Lit05 / semantic label G-CIT-1 before Gate · 05; Lit06 / semantic label G-CIT-2 inside 06). G-CIT-1 does not waive G-CIT-2. These labels are not new gate ids.

## Before skills / mounts (standing)

When the user requests skills or external mounts for a concrete task: show this official map in full, highlight the run path, and **wait for approval** before 01 pick or specialist execution. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse that lock after approval instead of asking again. A single-node personal-layer task with no mounted dependency does not ask (example: polish one sentence). Do not invent a second master diagram — only highlight branches on `runtime-flow.mmd`.
