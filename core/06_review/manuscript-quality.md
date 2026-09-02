---
name: "manuscript-quality"
domain: "06_review"
trigger: ["投稿前预审", "评阅", "审稿", "找洞", "落实审稿意见", "回复审稿人", "毕业论文评阅", "审稿单"]
inputs: ["manuscript_docx", "results_html"]
outputs: ["blocking_major_minor_report"]
tools: ["dealbreakers"]
quality_control: "flag leakage first; do not invent rescue experiments"
owner: "06_review/manuscript-quality.md"
---

# trigger is documentation only; not independently discoverable.

# manuscript-quality — 投稿前找问题 / 审他人稿 / 回复审稿人

**职责：** 找问题、写审稿意见、起草 point-by-point 回信；不重写全文（改句交给 `05_manuscript` `manuscript-core`）。

详规：预审/英文 peer review [`references/mode-2-prereview.md`](references/mode-2-prereview.md)；回信 [`references/mode-3-response.md`](references/mode-3-response.md)；毕业论文 [`references/thesis-review.md`](references/thesis-review.md)；中文刊 A–F [`references/chinese-journal-score-sheet.md`](references/chinese-journal-score-sheet.md)

**铁律：** 数据真实 > 期刊格式 > 李瀛语气；**不编造**补救实验或指标。

---

## 路径

### A. 预审自己的稿

- 触发：投稿前预审、找洞、dealbreaker、落实审稿意见、按审稿意见改已有稿  
- 输出：Summary + Blocking/Major/Minor + 清单缺口 + 引用旗标（格式见 `references/merged/radiology-prereview/review-report-format.md`）  
- 默认**不再**写 25–30 条问句。用户明确要「25-30条」时才用该格式。无法代决（脏数据、终点范围、姓名）仍做成**选择题**问用户  
- 打开：`merged/radiology-prereview/*`；清单/引用门只读 `05_manuscript` `manuscript-core/references/merged/radiology-reporting/` 与 `radiology-citation/`  
- 版式/字数不在此改 → `05_manuscript` `Aitor-format.md`  

**标题页整页跳过（落实审稿意见 / 改已有稿；不填、不黄标、不改写）：**

| 项 | 动作 |
|----|------|
| 伦理号（Date/NO） | 跳过 |
| 作者栏 | 跳过 |
| 目标刊 | 跳过 |
| 是否声明 “not generated” | 跳过 |

从零写 title page 仍归 `05_manuscript` `Aitor-format.md`（此处不复制 Aitor）。

**已成稿引用：** 核 Intro 10–15 / Discussion 10–15-new 时不删真引用凑配额，只注明超额。新写 I/D 配额与证据检索在 `05_manuscript` `Aitor-format.md` / `intro-discussion-evidence.md`，此处不重复检索步骤。

优先查：泄漏 · 非患者级划分却声称 patient-level · 无验证 · 无法追溯 AUC · 过度临床宣称 · 预测模型未双集报告主模型  

### B. 给别人写英文 Peer review

- 触发：你作为审稿人批**他人**稿、写审稿意见、peer review  
- 交付：可提交系统的英文审稿结构（Opening 2–4 句 → Major Comments → 按章节出条）  
- 声音：`references/merged/radiology-prereview/personal-review-style.md`  
- 每条：事实 → 为何问题 → 作者应做什么；`#n` 不是默认  
- 高频（自审 57）：讨论/局限、ROI 可重复性、样本偏倚、伦理占位符、未与常规方法比、过拟合、特征筛选泄漏、同院称作 external  
- 禁止空夸 interesting；禁止只打分不写改法；禁止把毕业论文套话或中文 A–F 审稿单冲词写进英文信  

```text
[Opening 2–4 sentences]

Major Comments

Abstract / Introduction / Methods / Results / Discussion / Limitations
…

Other / Minor
```

### C. 回复审稿人

- 触发：已有 Reviewer 意见、修回、point-by-point、response letter  
- 交付：可提交系统的英文回复信 + change log（`references/mode-3-response.md`）  
- 打开：`merged/radiology-response/*`  
- 开场**默认 A**（thanks + point-by-point）。风格 B 几乎不用；多轮修回仍留在 A 上加一句 resubmit。  
- 禁止编造未做实验；改句交给 `05_manuscript`

### D. 毕业论文评阅（与 B 分开）

- 触发：评阅毕业论文 / 学位论文 / 是否同意答辩  
- 交付：中文评阅表骨架（选题意义 → 不足 2–4 条 → 是否同意答辩）  
- 打开：`references/thesis-review.md`  
- **禁止**写成英文 Opening / Major Comments / Methods 长清单  

中文期刊若发来 1–5 分项或 A–F 处理意见单：只用 `references/chinese-journal-score-sheet.md`，不要与 B 或 D 混用。

---

## 输出信封（预审自己的稿）

```text
Skill: 06_review / manuscript-quality
Path: own-manuscript | peer-review-others | response | thesis-review | chinese-score-sheet

Blocking
- [loc] problem → action

Major
- ...

Minor
- ...

Reporting / citation gaps
- ...

Next: 05_manuscript 改稿
```

---

## 触发语

`/medical-manuscript-review` · 投稿前预审 · 找问题 · 落实审稿意见 · peer review · 回复审稿人 · 毕业论文评阅 · 中文刊审稿单  

---

# End of skill
