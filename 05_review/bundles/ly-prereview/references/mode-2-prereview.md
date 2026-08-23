# 模式 2 — 投稿前找问题 / 预审

含原：F 预审 · `ly-sci-writing` 的 I/清单再审计 · **B.1 给别人写英文 Peer review 审稿意见**。

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
   - 清单：`merged/radiology-reporting/*`  
   - 引用门：`merged/radiology-citation/claim-verification-gate.md`  
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

Recommended next: 改稿后回`ly-sci-writing`润色 / 或`ly-response`回审（若已有意见）
```

## 2.5 工作流 — 给别人写英文 Peer review（原 B.1）

与「预审自己的稿」共用方法学清单与 dealbreaker 意识，但**交付物是审稿意见信**，不是给作者的改稿清单信封（可同时给简短内部备注）。

```text
[Opening 2–4 sentences: relevance + contribution + judgment]

Abstract
#n ...
Introduction
#n ...
Methods
#n ...
Results
#n ...
Discussion
#n ...
Other Issues / Minor
#n language, refs, ethics, formatting
```

**Opening：** 点明临床问题与设计；写清 major revision / clarification 等判断。  
**每条：** 事实 → 为何成问题 → 作者应做什么（落到 Abstract / Methods / Table X）。  

**高频清单：** power / EPV / 过拟合 / 内外验证用语；嵌套 CV；STROBE·TRIPOD·CLEAR；伦理号；表内自洽；摘要-正文数字；因果措辞；效应量+CI。  

**禁止：** 空夸 interesting；只打分不写改法；emoji；灌水恭维。  

