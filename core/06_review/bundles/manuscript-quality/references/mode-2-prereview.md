# 模式 2 — 投稿前找问题 / 预审

含原：F 预审 · `manuscript-core` 的 I/清单再审计 · **B.1 给别人写英文 Peer review 审稿意见**。

## 2.1 何时用

### A. 预审自己的稿
- 「投稿前找洞」「模拟审稿」「dealbreaker」  
- 全文或 Methods/Results 已齐，要 Blocking / Major / Minor  

### B. 给别人写审稿意见
- 你作为审稿人批**他人**稿  
- 输出可投期刊系统的英文 peer review 文本  

## 2.2 工作流 — 预审自己的稿

1. 确认稿件类型（诊断准确度 / 预测模型 / 组学 / 其他）与目标刊  
2. 打开：  
   - `merged/radiology-prereview/dealbreakers.md`  
   - `merged/radiology-prereview/pre-submission-hard-gates.md`  
   - `merged/radiology-prereview/review-report-format.md`  
   - 清单：`05_manuscript/bundles/manuscript-core/references/merged/radiology-reporting/*`  
   - 引用门：`05_manuscript/bundles/manuscript-core/references/merged/radiology-citation/claim-verification-gate.md`  
3. 分块：Methods · Stats · Reporting · Claims · Figures/Tables（若有）  
4. 每条：位置 → 问题 → 作者应改什么（不编造未做实验）  
5. 输出报告（见 §2.4）  

## 2.3 Dealbreaker 优先查

- 数据泄漏 / 非患者级划分却声称 patient-level  
- 无验证或内外验证用语混乱  
- 编造或无法追溯的 AUC/NRI/IDI  
- 观察性设计却强因果 / 临床效用过度宣称  
- 主模型未在双集报告（若声称 TRIPOD 预测模型）  

## 2.4 输出格式

```text
Mode: 2 投稿前预审
Venue / study type:

Blocking
- [loc] problem → action

Major
- ...

Minor
- ...

Reporting checklist gaps
- CLAIM/TRIPOD/... item: missing | ok

Citation flags
- ...

Recommended next: 改稿后回 `05_manuscript` `manuscript-core` 润色
```

Default is this envelope, **not** a 25–30-question list (only if the user asks).

## 2.5 工作流 — 给别人写英文 Peer review（原 B.1）

与「预审自己的稿」共用方法学清单与 dealbreaker 意识，但**交付物是审稿意见信**，不是给作者的改稿清单信封（可同时给简短内部备注）。

声音与句模：`merged/radiology-prereview/personal-review-style.md`（2014–2026 自审 57）。  
**不要混：** 毕业论文评阅 → `thesis-review.md`；中文刊 A–F 审稿单 → `chinese-journal-score-sheet.md`。英文信不要导入中文审稿单的冲词。

默认信封（2024–2026；Opening 2–4 句 → Major → 按章节出条）：

```text
[Opening 2–4 sentences: design + clinical question + overall value + the methodological catch]

Major Comments

Abstract / Title
…

Introduction
…

Methods
…

Results
…

Discussion / Limitations
…

Other / Minor
… language, abbreviations, figure legends, ethics placeholders, punctuation
```

`#n` 编号是少数近年稿，不是默认。多数条目用 `Please …` / `It is unclear whether …` / `The authors should …`。约 17/57 仍用 Dear Editor 抬头——仅当系统要抬头时加。

**Opening：** 点明设计与临床问题；总体有无价值；方法学要害。Accept / Reject / Major revision **不要写进提交正文**（放内部备注或中文审稿单）。  
**每条：** 事实 → 为何成问题 → 作者应做什么（落到 Abstract / Methods / Table X）。不编造未做实验，不替作者补 AUC。

**高频要害（去重 57 份命中，有则写、无则跳过）：**

1. 讨论 / 局限未写清（24）
2. ROI / 分割可重复性：谁勾、肿瘤还是淋巴结、inter-/intra-observer、盲法（23）
3. 样本量 / 记录不全造成的偏倚（19）
4. 伦理占位符、waiver 未填、缺伦理号（18）
5. 未与常规影像或临床因素比（DeLong、NRI/IDI、校准、DCA）（15）
6. 语言、缩写全文首次展开（14）
7. 训练 AUC 接近完美而测试掉点 → 过拟合（13）
8. 特征筛选是否在全数据集上做（泄漏）；折内 nested；LASSO lambda（12）
9. 扫描参数、多中心/多设备一致性（12）
10. 「external validation」实际是同院时间划分（11）

其次才是摘要藏低特异度 / 缺 95% CI、因果措辞 vs 回顾性、引言末段假设。nested CV 被点名很少，不要写成第一要害。

**禁止：** 空夸 interesting；只打分不写改法；emoji；灌水恭维；把毕业论文套话或中文 A–F 分项打分贴进英文信。

**输出信封（内部备注，随审稿信一并给出，不提交期刊系统）：**

```text
Mode: 2 peer-review-others
Venue / study type:
Recommendation: Accept | Minor revision | Major revision | Reject

[Opening 2–4 sentences]

Major Comments
Abstract / Introduction / Methods / Results / Discussion / Limitations
…

Other / Minor
…

Internal note: dealbreakers found — [list, or none]
```

有前面的判断（Recommendation）+ dealbreaker 清单，方便你自己归档决策依据；正式提交的仍是不含此信封的审稿意见正文。

## 2.6 预审自己的稿时：他审实际会问什么（inbound，n=48）

写英文意见用 §2.5；修自己的稿用本节预判。命中与自审侧不完全相同：他审更常抓讨论/局限/overclaim（30）、统计（29）、验证/过拟合（29）、方法写不清（21）；伦理占位符命中低于自审侧。

预审时优先补上：伦理委员会名称+批号、样本量计算、局限段写全、缩写首次展开、图注、例数与流程图一致、多机扫描参数、测量次数/ICC。不要把推荐审稿人名单或期刊行政须知写进技能或仓库。

