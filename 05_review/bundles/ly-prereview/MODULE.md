# ly-prereview — 投稿前找问题 / 审他人稿

**职责：** 找问题、写审稿意见；不重写全文（改句交给 `ly-sci-writing`）。

详规：[`references/mode-2-prereview.md`](references/mode-2-prereview.md)

**铁律：** 数据真实 > 期刊格式 > 李瀛语气；**不编造**补救实验或指标。

---

## 两条路径

### A. 预审自己的稿

- 触发：投稿前预审、找洞、dealbreaker  
- 输出：Blocking / Major / Minor + 清单缺口 + 引用旗标  
- 实验室英文 SCI 全文：再写 **25–30 条批判性问题**；改稿前把无法代决的项做成**选择题**问用户  
- 打开：`merged/radiology-prereview/*` · `merged/radiology-reporting/*` · `merged/radiology-citation/*`  
- 版式/字数/title page 不在此改 → `04_writing` `Aitor-format.md`  

优先查：泄漏 · 非患者级划分却声称 patient-level · 无验证 · 无法追溯 AUC · 过度临床宣称 · 预测模型未双集报告主模型  

### B. 给别人写英文 Peer review

- 触发：审这篇（他人）、peer review 意见  
- 交付：可提交系统的英文审稿结构（Opening + 分节 #n）  
- 每条：事实 → 为何问题 → 作者应做什么  
- 禁止空夸 interesting；禁止只打分不写改法  

```text
[Opening 2–4 sentences]

Abstract / Introduction / Methods / Results / Discussion
#n ...

Other Issues / Minor
```

---

## 输出信封（预审自己的稿）

```text
Skill: ly-prereview
Path: own-manuscript | peer-review-others

Blocking
- [loc] problem → action

Major
- ...

Minor
- ...

Reporting / citation gaps
- ...

Next: ly-sci-writing 改稿 / ly-response（若已是正式意见需回信）
```

---

## 触发语

`/ly-prereview` · 投稿前预审 · 找问题 · 模拟审稿 · 帮我审这篇 · peer review  

---

# End of skill
