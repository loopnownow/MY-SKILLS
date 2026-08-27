---
name: "manuscript-quality"
domain: "06_review"
trigger: ["投稿前预审", "评阅", "审稿", "找洞", "回复审稿人"]
inputs: ["manuscript_docx", "results_html"]
outputs: ["blocking_major_minor_report"]
tools: ["dealbreakers"]
quality_control: "flag leakage first; do not invent rescue experiments"
owner: "06_review/bundles/manuscript-quality/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# manuscript-quality — 投稿前找问题 / 审他人稿 / 回复审稿人

**职责：** 找问题、写审稿意见、起草 point-by-point 回信；不重写全文（改句交给 `05_manuscript` `manuscript-core`）。

详规：预审/评阅 [`references/mode-2-prereview.md`](references/mode-2-prereview.md)；回信 [`references/mode-3-response.md`](references/mode-3-response.md)

**铁律：** 数据真实 > 期刊格式 > 李瀛语气；**不编造**补救实验或指标。

---

## 三条路径

### A. 预审自己的稿

- 触发：投稿前预审、找洞、dealbreaker  
- 输出：Summary + Blocking/Major/Minor + 清单缺口 + 引用旗标（格式见 `references/merged/radiology-prereview/review-report-format.md`）  
- 默认**不再**写 25–30 条问句。用户明确要「25-30条」时才用该格式。无法代决（伦理号、脏数据、终点范围、姓名）仍做成**选择题**问用户  
- 打开：`merged/radiology-prereview/*`；清单/引用门只读 `05_manuscript` `manuscript-core/references/merged/radiology-reporting/` 与 `radiology-citation/`  
- 版式/字数/title page 不在此改 → `05_manuscript` `Aitor-format.md`  

优先查：泄漏 · 非患者级划分却声称 patient-level · 无验证 · 无法追溯 AUC · 过度临床宣称 · 预测模型未双集报告主模型  

### B. 给别人写英文 Peer review

- 触发：你作为审稿人批**他人**稿、写审稿意见、peer review  
- 交付：可提交系统的英文审稿结构（Opening + 分节 #n）  
- 每条：事实 → 为何问题 → 作者应做什么  
- 禁止空夸 interesting；禁止只打分不写改法  

```text
[Opening 2–4 sentences]

Abstract / Introduction / Methods / Results / Discussion
#n ...

Other Issues / Minor
```

### C. 回复审稿人

- 触发：已有 Reviewer 意见、修回、point-by-point、response letter  
- 交付：可提交系统的英文回复信 + change log（`references/mode-3-response.md`）  
- 打开：`merged/radiology-response/*`  
- 禁止编造未做实验；改句交给 `05_manuscript`

---

## 输出信封（预审自己的稿）

```text
Skill: 06_review / manuscript-quality
Path: own-manuscript | peer-review-others | response

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

`/medical-manuscript-review` · 投稿前预审 · 找问题 · peer review · 回复审稿人  

---

# End of skill
