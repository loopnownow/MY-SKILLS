---
name: "manuscript-core"
domain: "05_manuscript"
trigger: ["润色", "SCI写作", "Aitor-format", "去AI", "写引言", "写讨论"]
inputs: ["results_html", "draft_docx"]
outputs: ["Manuscript_house_docx"]
tools: ["Aitor-format", "polisher-sections"]
quality_control: "numbers only from *-results.html; Methods no citations; no invented n/AUC"
owner: "05_manuscript/bundles/manuscript-core/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# manuscript-core — SCI 写作 / 润色 / 去 AI / 李瀛语言风格（单一真源）

**职责：** 写与改科研正文（含全文流程）。不是预审。

> 高度规范 · 临床导向 · 定量精确 · 客观谨慎

**铁律：** 数据真实 > 期刊格式 > 李瀛语气 > 通用华丽英语

详规：[`references/mode-1-sci.md`](references/mode-1-sci.md)  
**全文版式（title page / IMRAD / DOCX / 引用配额）：** [`references/Aitor-format.md`](references/Aitor-format.md)  
分节润色：[`references/polisher-sections.md`](references/polisher-sections.md)  
引言/讨论文献：[`references/intro-discussion-evidence.md`](references/intro-discussion-evidence.md)  
去 AI：[`references/de-ai/ai-isms-checklist.md`](references/de-ai/ai-isms-checklist.md)

---

## 何时用

- 起草或重写 Title / Abstract / Intro / Methods / Results / Discussion
- 润色；去 AI 腔；按李瀛风格改
- 影像组学 / habitat / 列线图 / TRIPOD 双集**全文**
- Radiology Summary/Key Results 或 Nature 体例
- 实验/机制英文纲要；通用学术大纲
- Methods 伦理句；写作时的引用/清单自检
- 为引言/讨论检索并核对文献（`intro-discussion-evidence.md`）

**不要用本模块：** 投稿前找洞 / 评阅 / 回复审稿人 → `06_review`；选题选刊 → `03_research`

---

## 作者锚点（勿虚构）

李瀛 / Ying Li · 复旦大学附属金山医院 放射科  
领域：影像、MHE/PSE、MRS、定量 MRI、组学、妇产影像、代谢组学、介入等  

默认作者栏、通讯、基金、回顾性 waiver：见 `references/Aitor-format.md`（勿在此复制）。

---

## 硬规则

1. 数字贴断言（n、AUC、CI、P）；禁空话
2. 问题—缺口—方案
3. 观察性反过度因果（*associated with*）
4. 术语一致；缩写首次全称
5. 短句（英文尽量 ≤55 词）
6. 禁 AI 腔 → 见 `references/de-ai/forbidden-phrases.md`
7. Results 不空套 hedge；Discussion 按证据强度 hedge
8. **预测模型全文额外：** 禁 em-dash 作标点；`95% CI: X–X`；**training** 拟合 / **test** 只评估 / **validation set** = 外部队列；禁用 hold-out 与 development set；患者级划分；**nomogram**（即 Combined / combined logistic，正文不写流水线名）双集 AUC/NRI/IDI/DCA（未导出则 **Word 批注**，正文不写 not generated）；LASSO+RadScore 公式在正文、不设特征表；无免责声明、不重复同一句 hedge；**禁止黄底留空**（缺方法/产物进批注）；正文不写 *coded*/*displayed* 前缀；第二遍润色只去管线词并对 `*-results.html` 数字、不并句、不改 IMRAD；Vancouver+DOI  
9. **不编造** 结果、文献、伦理号、未做实验  
10. **英文 SCI 全文必须遵守** `references/Aitor-format.md`（金标准：`0del/lxf_LG/Response/Manuscript_Response_house.docx`：除表芯 11 磅外全稿 12 磅；题目/节标题 12 磅加粗；单位左齐不加粗）。不清楚就问用户。
11. **缺项只批注：** 缺方法/产物事实、未测/未完成/`was not tested`、无外部验证集（*A validation set is required* / *No validation set was available*）一律 Word 批注，永不正文、永不黄底。不编造。新写与修订同规。批注/修订作者 **A**（禁 Grok）。
12. **I/D 配额：** 新写仍 10–15 / 10–15-new。核已成稿不删真引用凑配额，只注明超额。
13. **修订 Vancouver：** 按正文出现顺序重排角标。参考文献表重复项用已核 substitute 替换（作者 A）。
14. **禁 COMMENTARY 读法指引**（they should not be summarized as / is not reported as / should not be read as / given this extent / should not be described as；修辞性 rather than、but not by）。观察性对比仍用 *associated with*；事实对比（e.g. but not by sex）不禁。
15. **禁 elucidat*。** 目的/aim → exploring；机制未知 → remain unclear（不用 explain/clarify 顶替）。
16. **少用副词**（新写与润色）。统计 *significantly*（已有 P 值规则）不禁。

| 项 | 约定 |
|----|------|
| n | *(n = N)* |
| P | 斜体 *P* |
| CI | 95% CI: X–X（见 `Aitor-format.md`） |
| 伦理 | 见 `Aitor-format.md`（回顾性默认 waiver；Date/NO 空则 Word 批注，不黄底） |

---

## 模式与加载

| Mode | 打开 |
|------|------|
| `polish` | 本文件硬规则 → 全文则 `Aitor-format.md` → `polisher-sections.md`（按节）→ `sentence-templates.md` / `stats-checklist.md` → 可选 `de-ai/` |
| `draft-section` | `mode-1-sci.md` + `section-templates.md` / `polisher-sections.md` |
| `full-prediction` | `pipeline-stages.md` · `section-templates.md` · `radiomics-reporting.md` · mode-1 |
| `venue-shape` | `merged/radiology-writing/*` · polishing house style |
| `de-ai` | `references/de-ai/README.md`（先 forbidden，再 `ai-isms-checklist.md`，再 stop-slop；检测报告才开 detector） |
| `intro-discussion` | `intro-discussion-evidence.md` → Aitor 配额 → `polisher-sections.md` §2/§5 |
| `experiment-outline` / `academic-outline` | `mode-academic-pipeline.md` |

### 英文 SCI 全文（默认路径）

先套 `Aitor-format.md`（版式 + Methods 固定顺序 + 引言/讨论字数与文献配额），预测模型再叠加 `pipeline-stages.md` 的双集/LASSO/RadScore 约束。

### 润色输出

```text
[Polished — paste-ready]

---
Key changes:
- ...
```

### 统一信封

```text
Skill: 05_manuscript / manuscript-core
Subtask: polish | draft-section | full-prediction | de-ai | ...
Venue: ...

[Draft / Polished]

Missing inputs:
- ...

Next: 06_review 预审（可选）
```

---

## references 地图

| 路径 | 用途 |
|------|------|
| `Aitor-format.md` | 全文版式 / 分集用词 / 删表与诚实边界 / Methods 顺序 / 字数与引用配额 / DOCX / 第二遍去管线 |
| `intro-discussion-evidence.md` | 为写引言/讨论检索、核 DOI、分节配额（不复制 Aitor） |
| `../figure-engine/MODULE.md` | Figure 1 入组/分析流程图（不画纳入标准；training/test 下连分析行；有外部队列才画 validation set） |
| `mode-1-sci.md` | 主工作流 |
| `polisher-sections.md` | 分节润色 §1–§9（原 ying-li-polisher） |
| `sentence-templates.md` / `stats-checklist.md` / `exemplars.md` | 句式与统计表述 |
| `de-ai/*` | 去 AI / 检测 / slop 结构 |
| `pipeline-stages.md` 等 | 预测模型全文 |
| `mode-academic-pipeline.md` | 通用大纲 |
| `methods_template_export.md` | skills_export 方法模板 |
| `merged/radiology-writing/*` | 期刊体例 |
| `merged/radiology-polishing/*` | house style |
| `merged/radiology-citation/*` · `reporting/*` · `ethics/*` | 写作自检/伦理段 |

---

## 已合并（P1，勿再当独立 skill）

- ~~ying-li-polisher~~ → `polisher-sections.md`
- ~~stop-slop~~ → `references/de-ai/stop-slop-core.md` + phrases/structures/examples
- ~~ai-writing-detector~~ → `references/de-ai/ai-writing-detector.md`

---

# End of module
