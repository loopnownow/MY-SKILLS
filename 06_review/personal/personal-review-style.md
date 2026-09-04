# 个人审稿意见风格（英文 peer review）

来源：2014–2026 自审期刊意见全文库，去重 57 份。只收结构、口气与高频要害，不收录他人未刊题目、数据、伦理号或患者标识。

本文件只服务 **英文期刊 peer review**（给别人写、可提交系统的审稿信；本室预审也可套同一章节骨架）。下面两件事走别的模板，禁止混进本信封：

| 任务 | 文件 |
|---|---|
| 毕业论文 / 学位论文评阅 | `thesis-review.md` |
| 中文杂志 1–5 分项 + A–F / 学术审稿单 | `chinese-journal-score-sheet.md` |

早期中文审稿单可以很冲（「并无新意」「选择偏倚」「未交代」）。**英文稿不要学那种冲法。** 英文用礼貌、直接、可执行的祈使。

**模式入口：** `06_review/SKILL.md`（`pre-review` / `peer-review` / `response`）。不要引用已删除的 `mode-2-*.md`。

---

## 0. 批注与冲突（实验室硬规则）

- Word / 稿面批注作者 **A**。禁止黄底。
- 每条批注标明来源前缀：`[A:personal]` · `[06-review-peer]` · `[06-review-critique]` · `[06-review-response]` · `[B:…]` · `[MedSci:…]` 等。
- **挂载建议与实验室口径冲突时：** 不静默采用挂载改法。全部写进批注：冲突点 + **修改方案**（改前句 / 改后句，或「保持原句 + 换文献」）。**最终由用户决定**；未点头不改稿。
- 定不了的事实（缺 n、伦理、未做分析）：标 `cannot_invent`，问用户；可附 1–2 句 **reference only** 改写，不直接落稿。
- 改文单元：**词或句**，禁止整段重写。

---

## 1. 年代分层（决定信封，不决定把中文冲法搬进英文）

| 大约年份 | 形态 | 英文 peer review 怎么用 |
|---|---|---|
| 2014–2018 | 中文杂志审稿单 | **不要**当英文信模板。走 `chinese-journal-score-sheet.md` |
| 2019–2023 | `Dear Editor` + 页码行号出条 | 仅当邀请信/系统仍要抬头时用 |
| 2024–2026 | 无抬头或一行邀请致谢；Opening → 按章节 Major/Minor | **默认信封** |

正文一般不写 Accept / Reject / Major revision 分数；分数放内部备注或中文审稿单。

---

## 2. 默认信封（2024–2026）

按用户模版分八章出条。每章内先 **Major Issues**，再 **Minor Issues**。Major = 可改变结论/可重复性/伦理/数据一致性；Minor = 字词、格式、图注补全。

```text
[Opening 2–4 sentences: design + clinical question + overall value + the methodological catch]

1. Title
Major Issues: [Page/Line + defect + actionable fix]
Minor Issues: …

2. Abstract
Major Issues:
Minor Issues:

3. Introduction
Major Issues:
Minor Issues:

4. Methods
Major Issues:
Minor Issues:

5. Results
Major Issues:
Minor Issues:

6. Discussion
Major Issues:
Minor Issues:

7. References
Major Issues:
Minor Issues:

8. Figures & Tables
Major Issues:
Minor Issues:
```

需要时加一行 `Major Comments`。不要写成 25 问问卷（除非编辑部表格强制）。空章写 `None` 或省略，不要注水。

**每条：** `Page X, Line Y`（或 section）→ 缺陷 → **明确修改建议**。不编造未做实验，不替作者补 AUC。

---

## 3. Opening（2–4 句）

点明设计 + 临床问题 → 总体有无价值 → 但方法学仍有要害。少空夸 *interesting*。

**默认：**
```text
This [design] study [does X] to [clinical question]. The topic is clinically relevant, but methodological limitations—particularly [theme], [theme], and [theme]—currently weaken the strength of the conclusions.
```

变体（稿较好）：`While the study is methodologically sound and clinically promising, a few key areas would benefit from further revision.`

变体（要可重复性）：`This study had certain clinical usefulness. However, the method was not rigorous. Details should be provided for the repeatability. These are my comments.`

**Dear Editor（系统仍要抬头时）：**
```text
Dear Editor:
Thank you for inviting me to evaluate this article. The purpose of this study was to …. However, details for explanation of replicability of the methods should be provided.
```

不要在 Opening 里写 Accept/Reject。近年若保留脚注 `AI was used to refine the readability of the peer review comments, all of which came from the reviewer.` —— 只润色句法，不改判断。

---

## 4. 分章审查重点（模版）与高频要害

写意见时按章扫；有则写，无则跳过。英文用礼貌祈使。

### 4.1 Title
**重点：** 是否准确反映核心内容与研究类型（RCT / 队列 / 诊断性试验 / 预测模型）。
- Major：题不对文；把 temporal split 写成 external validation。
- Minor：冗余词、缩写未展开。

### 4.2 Abstract
**重点：** 结构完整；目的/方法/主要数据（OR/HR、95% CI、*P*）及结论与正文一致。
- Major：藏低特异度；缺 95% CI；与正文数字不符。（命中约 10）
- Minor：字数、缩写首次展开。

### 4.3 Introduction
**重点：** 背景是否引出空白；假说与目的是否清晰。
- Major：末段无清楚假设。（命中约 5）`Please clearly state the research hypothesis in the last paragraph of the Introduction.`
- Minor：背景过长、引用堆砌（预审：不删真文献，只注 over-quota）。

### 4.4 Methods
**重点：** 设计是否匹配问题；对照是否合理；样本量依据；入排是否严密；技术/序列/软件版本可重复；IRB/知情同意/注册。
- Major（高频）：
  - ROI / 分割可重复性（约 23）
  - 样本量 / 连续入组 / 缺记录处理（约 19）
  - 伦理占位符 / 缺伦理号（约 18）
  - 特征筛选泄漏 / LASSO λ / 折内 nested（约 12）
  - 扫描参数 / 多设备一致性（约 12）
  - 「external」实为同院时间划分（约 11）
- Minor：试剂厂家、软件版本、参数补全。

### 4.5 Results
**重点：** 统计与分布匹配；正文与图表一致；无选择性汇报；无对非显著结果过度解读。
- Major：过拟合（训练近完美、测试掉点，约 13）；未与常规/临床模型比（DeLong、校准、DCA，约 15）；p 与表不符。
- Minor：表注 Mean±SD / Median(IQR) 未标明。

### 4.6 Discussion
**重点：** 结论是否由数据支撑；有无把相关当因果；与既往研究比较；局限性是否客观。
- Major：局限未写清（约 24）；因果措辞 vs 回顾性（约 8）。
- Minor：结构松散、重复 Results。

### 4.7 References
**重点：** 是否客观代表性；近 2–3 年关键文献；格式。
- Major：文献核对有误 → 批注给 **双轨方案**（见下），由 00 QC 决定是否调 `03_research`；不编造 PMID。
- Minor：格式、DOI。

**文献核对失败（双轨，写入批注，用户拍板）：**
1. **改原文方案**（词/句级）：改前句 / 改后句。
2. **不改原文方案**：交接 03 检索可支撑现句的替代文献（真实 PMID/DOI）。  
是否真调 03 → **00 在 QC 决定**；吃不准问用户一句。

### 4.8 Figures & Tables
**重点：** 自明性；与正文一致；分辨率、比例尺、图例、统计符号。
- Major：图数与正文矛盾；Figure 1 无 inclusion 框却自称 STROBE 流。
- Minor：缺 scale bar；Table 1 未标 Mean±SD / Median(IQR)。

可复用短句（占位符，不贴未刊数字）：
- `Please specify if this is a retrospective or a prospective study.`
- `Please acknowledge and describe how cases were consecutively or randomly selected.`
- `Please provide the exclusion criteria.`
- `It is unclear how the authors performed the ROI drawing.`
- `Please report 95% confidence intervals for all AUC values and include them in the Results and Discussion.`
- `Please comply with the STROBE / TRIPOD reporting guidelines.`
- `Please discuss how the model would be used in practice.`
- `The authors should more clearly justify the clinical utility given the modest discriminative performance.`

---

## 5. 口气与质量自检

- 礼貌、直接、可执行。先事实，再为什么成问题，再作者该改哪里。
- 不编造未做实验、不替作者补 AUC、不在意见里复述可识别的未刊结果表。
- 只打分不写改法 = 禁止。
- 英文 **禁止**导入中文审稿单冲词直译（*no novelty* / *selection bias* 作为骂句）。同一事实写成可执行请求。

提交前自检四维：
1. **精准可操作** — 有 Page/Line（或 section）+ 明确改法。
2. **结构清晰** — Major / Minor 分清。
3. **建设性** — 学术尊重；即使得拒稿建议也指出可改进方向。
4. **辅助编辑** — Opening 已概括核心优势与关键短板。

---

## 6. 禁止

- 把他人稿 PDF、补充材料、CSV、未刊题目写入技能或公开仓库
- 把毕业论文评阅或国自评议套话写进英文 peer review
- 把中文刊 A–F 分项整段贴进英文信
- 空夸 interesting；emoji；灌水恭维
- 静默采用与实验室冲突的挂载改法（必须进批注，用户决定）
