# 个人审稿意见风格（英文 peer review）

来源：2014–2026 自审期刊意见全文库，去重 57 份。只收结构、口气与高频要害，不收录他人未刊题目、数据、伦理号或患者标识。

**先套** [`mode-2-prereview.md`](../../mode-2-prereview.md) §2.5 信封，再用本文件调声音。

本文件只服务 **英文期刊 peer review**（给别人写、可提交系统的审稿信）。下面两件事走别的模板，禁止混进本信封：

| 任务 | 文件 |
|---|---|
| 毕业论文 / 学位论文评阅 | [`thesis-review.md`](../../thesis-review.md) |
| 中文杂志 1–5 分项 + A–F / 学术审稿单 | [`chinese-journal-score-sheet.md`](../../chinese-journal-score-sheet.md) |

早期中文审稿单可以很冲（「并无新意」「选择偏倚」「未交代」）。**英文稿不要学那种冲法。** 英文用礼貌、直接、可执行的祈使。

---

## 1. 年代分层（决定信封，不决定把中文冲法搬进英文）

| 大约年份 | 形态 | 英文 peer review 怎么用 |
|---|---|---|
| 2014–2018 | 中文杂志审稿单（1–5 分项 + 前言/材料与方法/结果/讨论编号 + A–F） | **不要**当英文信模板。走 `chinese-journal-score-sheet.md` |
| 2019–2023 | `Dear Editor` + `Thank you for inviting me to evaluate…` + 页码行号出条 | 仅当邀请信/系统仍要抬头时用；口气已是礼貌 + 可重复性 |
| 2024–2026 | 无抬头或一行邀请致谢；**Opening 2–4 句** → `Major Comments` → 按章节出条 | **默认信封** |

约 17/57 仍以 Dear Editor 开头；约 12/57 明确 Major/Minor。`#n` 编号是少数近年稿，不是全库默认。多数条目是短祈使：`Please …` / `It is unclear whether …` / `The authors should …`。

正文一般不写 Accept / Reject / Major revision 分数；分数放内部备注或中文审稿单。

---

## 2. 默认信封（2024–2026）

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

需要时加一行 `Major Comments` / `Major concerns`。不要写成 25 问问卷（除非编辑部表格强制）。

**每条：** 先事实（n、划分、训练/测试 AUC 差、伦理句是不是占位符）→ 为何成问题 → 作者该改哪里（落到 Abstract / Methods / Table X）。不编造未做实验，不替作者补 AUC。

---

## 3. Opening（2–4 句）

点明设计 + 临床问题 → 总体有无价值 → 但方法学仍有要害。少空夸 *interesting*。

**默认（期刊系统英文）：**
```text
This [design] study [does X] to [clinical question]. The topic is clinically relevant, but methodological limitations—particularly [theme], [theme], and [theme]—currently weaken the strength of the conclusions.
```

变体（稿较好、只要修）：
```text
While the study is methodologically sound and clinically promising, a few key areas would benefit from further revision.
```

变体（方法不严、要可重复性）：
```text
This study had certain clinical usefulness. However, the method was not rigorous. Details should be provided for the repeatability. These are my comments.
```

**Dear Editor 信封（2019–2023；系统仍要抬头时）：**
```text
Dear Editor:
Thank you for inviting me to evaluate this article. The purpose of this study was to …. However, details for explanation of replicability of the methods should be provided.
```

不要在 Opening 里写 Accept/Reject。双语受邀时英文为主；中文段不扩写英文没有的新批评。

近年若保留脚注 `AI was used to refine the readability of the peer review comments, all of which came from the reviewer.` —— 只润色句法，不改判断、不加新批评。

---

## 4. 高频要害（去重 57 份命中；有则写，无则跳过）

按命中排序。写英文意见时用礼貌祈使，不要把早期中文单的冲词译进去。

| # | 主题 | 命中 | 英文怎么问 |
|---|---|---|---|
| 1 | 讨论 / 局限未写清 | 24 | Please mention missing data, inter-scanner variability, and the absence of independent external validation as key weaknesses. |
| 2 | ROI / 分割可重复性 | 23 | Please provide ROI size, number, whether measurements were averaged, who delineated, inter-/intra-observer agreement, and blinding. |
| 3 | 样本量 / 记录不全造成的偏倚 | 19 | Such limited enrollment may compromise generalizability. Please specify how incomplete records were handled, and whether cases were consecutive. |
| 4 | 伦理占位符 / waiver 未填 / 缺伦理号 | 18 | The ethics statement contains placeholder text. Please provide the IRB approval number and a rationale for waiving informed consent. |
| 5 | 未与常规影像或临床因素比（DeLong、NRI/IDI、校准、DCA） | 15 | Please use DeLong to compare the nomogram with the conventional / clinical model. Please perform calibration and DCA. |
| 6 | 语言 / 缩写全文首次展开 | 14 | Please provide the full name at first use of an abbreviation. Language editing by a native speaker is suggested. |
| 7 | 过拟合（训练 AUC 接近完美、测试掉点） | 13 | The training–test AUC drop should be discussed as a risk of overfitting. Including variables with only marginal significance increases that risk. |
| 8 | 特征筛选泄漏（全数据筛选；折内 nested；LASSO lambda） | 12 | Please clarify whether normalization and feature selection were performed on the full dataset or within each fold / on the training set only. Please report the LASSO lambda. |
| 9 | 扫描参数 / 多中心 / 多设备 ADC 一致性 | 12 | Please provide scan parameters of all sequences and mention inter-scanner variability. |
| 10 | 「external validation」实为同院时间划分 | 11 | Despite being labeled as "external," the validation cohort was drawn from the same hospital, which is more akin to internal / temporal validation. |
| 11 | 摘要报敏感度却藏低特异度 / 缺 95% CI | 10 | Report 95% CIs for all AUC values. Do not hide low specificity in the Abstract. |
| 12 | 因果措辞 vs 回顾性设计 | 8 | These are associations, not causal mechanisms. Please take caution in interpreting the biomarker as causal. |
| 13 | 引言末段要有一句清楚假设 | 5 | Please clearly state the research hypothesis in the last paragraph of the Introduction. |

数据泄漏 / nested CV 被点名的很少（约 2）；相关问题多数已算在「全数据特征筛选」（12）。不要把 nested CV 写成全库第一要害。

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

## 5. 口气

- 礼貌、直接、可执行。先事实，再为什么成问题，再作者该改哪里。
- 不编造未做实验、不替作者补 AUC、不在意见里复述可识别的未刊结果表。
- 只打分不写改法 = 禁止。
- 英文 peer review **禁止**导入：「并无新意」「选择偏倚」这类中文审稿单冲词的直译（*no novelty* / *selection bias* 作为骂句）。同一事实用英文写成可执行请求（*Please justify the incremental value relative to existing methods.* / *Please describe how consecutive enrollment was ensured.*）。

---

## 6. 禁止

- 把他人稿 PDF、补充材料、CSV、未刊题目写入技能或公开仓库
- 把毕业论文评阅套话或国自评议套话写进英文 peer review
- 把中文刊 A–F 审稿单的分项打分整段贴进英文信
- 空夸 interesting；emoji；灌水恭维
