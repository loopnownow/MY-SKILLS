# English peer review (style + habits)

> **Post-QC re-review (2026-10-17):** A06 runs after base isolation + 00 QC. See `review-isolation.md`. Response letters -> `07_response`.


## Part A — English peer-review envelope

# 个人审稿意见风格（英文 peer review）

来源：2014–2026 自审期刊意见全文库，去重 57 份。只收结构、口气与高频要害，不收录他人未刊题目、数据、伦理号或患者标识。

磁盘语料（内部评阅，用户本人的意见风格来源）：`{doc_review_corpus}\`。本文件不复制语料全文。

本文件只服务 **英文期刊 peer review**（给别人写、可提交系统的审稿信；本室预审也可套同一章节骨架）。下面两件事走别的模板，禁止混进本信封：

| 任务 | 文件 |
|---|---|
| 毕业论文 / 学位论文评阅 | `thesis-review.md` |
| 中文杂志 1–5 分项 + A–F / 学术审稿单 | `chinese-journal-score-sheet.md` |

早期中文审稿单可以很冲（「并无新意」「选择偏倚」「未交代」）。**英文稿不要学那种冲法。** 英文用礼貌、直接、可执行的祈使。

**模式入口：** `06_review/SKILL.md`（`pre-review` / `peer-review` / `response`）。不要引用已删除的 `mode-2-*.md`。

---

## 0. 批注与冲突（实验室硬规则）

Ownership: see `00_orchestrator/references/ownership-contract.md`.

- Word / 稿面批注**作者字段**永远是 **A**。禁止黄底。作者栏 ≠ 来源标签。
- 来源只写在批注**正文前缀**（文首）：这条判断从哪一层来，不是标信封。
  - **格式（挂载项）：** `[源:包内skill-id]`。禁止只写源名（如光秃 `[Nature:]` / `[Scientific:]`）。B 用 v4 细 ID：`[B:peer-review]`。
  - 例：`[A:personal]` · `[B:peer-review]` · `[Nature:simulate-reviewers]` · `[Scientific:scientific-critical-thinking]` · `[MedSci:self-review]` · `[AIPOCH:peer-review]` · `[lit-search]`（个人/细 ID 任务）
  - 挂载 + 个人都成立 → **双标**，例：`[Nature:simulate-reviewers] [A:personal]` / `[Scientific:scientific-critical-thinking] [A:personal]`
- **强制：** 本轮挂了 MedSci / Scientific / AIPOCH / Nature（或非个人 B 包）时，凡发现/门控/清单条目来自该挂载，前缀**必须**含 **skill 级**标签（`[Nature:simulate-reviewers]` 这类），不能只写源。禁止因为走了个人八章信封就把全部写成 `[A:personal]`。**禁止默认回落 `[A:personal]`**（Rules：`manuscript-docx.md` §1）。
- 无挂载时不得出现空壳源前缀。纯实验室改句（语法、Aitor 标点）只标 `[A:personal]`。无从判定来源时才用 `[A:personal]`。
- **挂载建议与实验室口径冲突时：** 不静默采用挂载改法。全部写进批注：冲突点 + **修改方案**（改前句 / 改后句，或「保持原句 + 换文献」）。**最终由用户决定**。用户点头后仍由 Aitee 落 Track Changes，Lee 只批注。
- **可决定的问题：** Lee 写清批注（定位、缺陷、要改的词或句），交给 Aitee TC-fix。Lee 默认不改正文。
- 定不了的事实（缺 n、伦理、未做分析）：标 `cannot_invent`，问用户。中文批注加英文建议措辞和/或建议文献（见 ownership-contract）。建议文献由 Victor 供给。Lee 不落稿件修订；用户选定后由 Aitee 用 Track Changes 改正文。
- 改文单元：**词或句**，禁止整段重写。

---


## 0.1 意见条目定位（硬规则）

- 每条 Major / Minor **正文**：`Lines n–m:`（或图/表/章节定位）+ 哪里不好 + Please 怎么改。
- **优先：** Proof/原稿行号，如 `Lines 76–79:` / `Line 216:`。
- **无可靠行号时：** `Introduction, paragraph 2, line 3:`；或 `Table 1 legend:` / `Figure 5A:` / `Section 2.3, paragraph 1:`。
- **已给行号则不复述、不引用原稿句子。**
- **来源标签**（如 `[B:self-review][A:personal]`）只写在 Word **批注**文首；作者字段 **A**。不好的原因用**中文**写在同一条批注里，放在来源标签后面。`cannot_invent` / G-LIT 双轨也只进批注（不进信封正文）。
- **禁止**把行号埋在句中或句末；禁止无定位的空泛指摘（Opening 总述除外，Opening 可不写行号）。
- **定位不确定时：** 不硬编精确行号。在 Word **批注**中说明不确定原因 + 建议 locator + 建议修改内容；批注**作者字段 = A**。用户确认后，只可改审稿**信封**里对应的那一条。稿件正文不在这里用修订模式改（见 ownership-contract）。
- 用户若粘贴原文句子：先在 Proof/plain 对齐行号，再写入对应章节；不要另起新的审稿 docx。

## 1. 年代分层（决定信封，不决定把中文冲法搬进英文）

| 大约年份 | 形态 | 英文 peer review 怎么用 |
|---|---|---|
| 2014–2018 | 中文杂志审稿单 | **不要**当英文信模板。走 `chinese-journal-score-sheet.md` |
| 2019–2023 | `Dear Editor` + 行号优先（Lines n–m / Section, paragraph, line）出条 | 仅当邀请信/系统仍要抬头时用 |
| 2024–2026 | 无抬头或一行邀请致谢；Opening → 按章节 Major/Minor | **默认信封** |

正文一般不写 Accept / Reject / Major revision 分数；分数放内部备注或中文审稿单。

---

## 2. 默认信封（2024–2026）

按用户模版分八章出条。每章内先 **Major Issues**，再 **Minor Issues**。Major = 可改变结论/可重复性/伦理/数据一致性；Minor = 字词、格式、图注补全。

```text
[Opening 2–4 sentences: design + clinical question + overall value + the methodological catch]

1. Title
Major Issues: [Lines n–m: / Section, paragraph, line: + defect + Please fix]  （来源标签进批注，见 §0.1）
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

**每条：** `Lines n–m:`（或 section）→ 缺陷 → **Please** 明确修改建议。来源标签与中文原因进批注（§0.1）。不编造未做实验，不替作者补 AUC。

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
- Minor：开头段有可引用的证据却 0 条文献；连续两句引用同一篇却没有新论点。见 §4.9。Aim 段仍不引用。

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
- Major：同一队列上既筛选又取阈值又做组间检验，却把 *P* 写成确认性结果。请改为描述性，或提供真实做过的 nested CV / bootstrap。不要替作者写成做过 nested CV。
- Major：入组阈值与纳入组的中位数、Q1 或最小值矛盾；IQR 超出量表范围。只批注，不改数字。
- Major：检索式为空，或扫描参数仍是占位。见 §4.9。

### 4.5 Results
**重点：** 统计与分布匹配；正文与图表一致；无选择性汇报；无对非显著结果过度解读。
- Major：过拟合（训练近完美、测试掉点，约 13）；未与常规/临床模型比（DeLong、校准、DCA，约 15）；p 与表不符。
- Major：*t*/*F*/*z* 达不到所述体素或团块阈值；相关的 *r* 与 *P* 隐含的 *n* 与文中分析 *n* 不符；大量 ROI 相关未交代多重比较；relative 指标未定义分母。只标矛盾，不补数字。见 §4.9。
- Minor：表注 Mean±SD / Median(IQR) 未标明。

### 4.6 Discussion
**重点：** 结论是否由数据支撑；有无把相关当因果；与既往研究比较；局限性是否客观。
- Major：局限未写清（约 24）；因果措辞 vs 回顾性（约 8）。
- Minor：结构松散、重复 Results。

### 4.7 References
**重点：** 是否客观代表性；近 2–3 年关键文献；格式；有无重复条目。
- Major：同一 DOI / 同一题名出现两次 → Major：先并号或换文献；换文献时**不得**把旧篇独有数字（病例数、AUC 等）抄到新篇。
- Major：文献核对有误 → 批注给 **双轨方案**（见下），由 00 QC 决定是否调 `03_research`；不编造 PMID。
- Minor：格式、DOI 缺漏。
- Major：作者名单、DOI、年份或卷号从另一篇稿抄来，或年份/卷号未对照原文就改。请对照原文核对。不要凭记忆填“正确”年份。见 §4.9。
- 文献准确性与 Victor 共同负责。call/require 03 citation-verify — do not self-certify lit。Lee 不签 claim→ref 表。

**文献核对失败（双轨，写入批注，用户拍板）：**
1. **改原文方案**（词/句级）：改前句 / 改后句。
2. **不改原文方案**：交接 03 检索可支撑现句的替代文献（真实 PMID/DOI）。  
是否真调 03 → **00 在 QC 决定**；吃不准问用户一句。换上的新篇只带该篇真实信息；旧篇数字不迁移。

### 4.8 Figures & Tables
**重点：** 自明性；与正文一致；分辨率、比例尺、图例、统计符号。
- Major：图数与正文矛盾；Figure 1 无 inclusion 框却自称 STROBE 流。
- Minor：缺 scale bar；Table 1 未标 Mean±SD / Median(IQR)。
- Major：表与另一篇稿完全相同，却未说明样本是否重叠。
- Minor：图注残留 `TRAIN_RATIO` 或其他流程词。见 §4.9。

可复用短句（占位符，不贴未刊数字）：
- `Please specify if this is a retrospective or a prospective study.`
- `Please acknowledge and describe how cases were consecutively or randomly selected.`
- `Please provide the exclusion criteria.`
- `It is unclear how the authors performed the ROI drawing.`
- `Please report 95% confidence intervals for all AUC values and include them in the Results and Discussion.`
- `Please comply with the STROBE / TRIPOD reporting guidelines.`
- `Please discuss how the model would be used in practice.`
- `The authors should more clearly justify the clinical utility given the modest discriminative performance.`

### 4.9 Pre-submit consistency requests

Chapter scans above point here. Full check ids: `05_manuscript/qc/manuscript-local-qc.md`. Run order and sister-paper rules: `06_review/qc/cross-manuscript-qc.md`. Statement consistency first, then data. On a conflict, annotate. Do not invent the number.

Reusable requests (no unpublished results in the sentence):

- `Please show that the reported statistic meets the voxel-wise or cluster-forming threshold named in Methods, or correct the threshold statement.`
- `Please state the n for each correlation and confirm that it matches the reported r and P. Please name the multiple-comparison procedure, or label the correlations uncorrected and exploratory.`
- `Please define the denominator and the units of any relative measure before interpreting its spread.`
- `Feature selection, threshold selection, and the group comparison appear to use the same participants. Please relabel these P values as descriptive, or provide the nested cross-validation or bootstrap correction that was actually run.`
- `Please state whether this score is a transform of a single metric, and whether nested regions were entered as independent tests.`
- `Please remove pipeline tokens, source-attribution hedges, and placeholder text from the manuscript and the figure legends.`
- `Please reconcile the inclusion cutoff with the reported median, quartile, and IQR.`
- `These manuscripts appear to share a site, a scanner, or an ethics approval. Please state the participant overlap and cite the related paper.`
- `This table matches another manuscript. Please state whether the samples overlap.`
- `The same biomarker is reported with a different P in a related manuscript. Please reconcile the difference.`
- `Please cite the opening background claim, or weaken it. Please do not cite the same paper in consecutive sentences unless the second sentence adds a distinct claim.`
- `Please verify this reference against the source. Do not copy the author list, DOI, year, or volume from another manuscript.`

---

## 5. 口气与质量自检

- 礼貌、直接、可执行。先事实，再为什么成问题，再作者该改哪里。
- 不编造未做实验、不替作者补 AUC、不在意见里复述可识别的未刊结果表。
- 只打分不写改法 = 禁止。
- 英文 **禁止**导入中文审稿单冲词直译（*no novelty* / *selection bias* 作为骂句）。同一事实写成可执行请求。

提交前自检四维：
1. **精准可操作** — 有 Lines n–m / Section, paragraph, line（或 section）+ 明确改法。
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


---

## Part B — Comment habits

# Review comment habits (Aitor / Jinshan)

Personal upper layer for **审稿** / 投稿前预审（找缺陷、出批注与可执行请求）.  
Journal-facing English envelope stays in `review.md`.  
This file is the **consistency-first** habit layer.

**Locks (2026-09-24):** do **not** teach minimal `?` / bare “核实” as the house style. Lead with **statement consistency**, then **data consistency**, then integrity stops.

**Locks (2026-10-02):** on a data conflict, annotate every locus. Do not invent a replacement number. Pre-submit classes and sister-paper checks: `06_review/qc/cross-manuscript-qc.md`. Check ids: `05_manuscript/qc/manuscript-local-qc.md`. call/require 03 citation-verify — do not self-certify lit.

**Locks (Word revise ownership):** Ownership: see `00_orchestrator/references/ownership-contract.md`.

---

## 1. Overall portrait (reviewer side)

Review like a careful editor + statistician: numbers, abbreviations, reference hygiene, legend placement, and causal vs association wording.

- Prefer **actionable** comments: what is wrong, where, and what to do.
- Prefer finite choices at decision points; still stop for real ambiguity.
- Uncertain facts: mark `cannot_invent` / ask — never pick a number silently.
- Mount vs lab conflict: write both options in the comment; **user decides** (`review.md` §0).

---

## 2. Statement consistency (first pass)

Before arguing about a new analysis, check whether the manuscript **agrees with itself**:

| Check | Fail examples | Comment action |
|---|---|---|
| Same claim, same wording | Abstract vs Results vs Discussion disagree on what was compared | Point to both loci; ask which wording is intended |
| Comparison object explicit | “higher risk” without naming who vs whom | Require “A vs B” (or named groups) in Methods/Results |
| Endpoint / label boundaries | Pseudoprogression vs multi-horizon ORR conflated | Ask for one clarifying sentence; do not invent the endpoint |
| Time / follow-up arithmetic | Follow-up window conflicts with enrollment dates | Ask to reconcile from source calendar; do not invent dates |
| Co-author comment vs body | Reviewer/co-author note does not match current text | Say the mismatch plainly; force version sync |
| Section misplacement | Discussion sentence that belongs in Introduction (or reverse) | Relocate request; do not rewrite content here (prose → 05) |

Comments stay concrete (locator + ask). Avoid empty style lectures.

---

## 3. Data consistency (second pass)

| Check | Fail examples | Comment action |
|---|---|---|
| Cross-surface numbers | AUC / *n* / *P* differ across Abstract, body, tables, figures | Flag all loci; **do not choose** which number is “right” |
| CI pairing | AUC without 95% CI; training reported without test (when both exist) | Request paired reporting from `*-results.html` |
| Table ↔ prose | Prose invents a cell the table does not have (or contradicts it) | Prefer table as file truth unless HTML says otherwise |
| Extreme / perfect patterns | Identical counts across splits; AUC = 1.000 with no caveat | Stop and raise integrity concern before more polish |
| Stats method label | `multivariate` used for multi-predictor regression | Request `multivariable` unless multiple outcomes are meant |
| Display rules | *P* decimals / mean±SD format drift mid-paper | One house rule end-to-end (`Aitor-format` / 04) |
| Statistic vs threshold | Printed *t*/*F*/*z* cannot meet the voxel or cluster *P* named in Methods | Flag both loci; do not replace either number |
| Correlation *n* | *n* implied by *r* and *P* disagrees with the stated analysis *n* | Flag; do not invent *n* |
| Table → *p* spot-check | Primary between-group rows report mean±SD (or counts) and *n*, but the printed *P* cannot be roughly recovered | Back-calculate an approximate *p* (two-sample *t* from mean/SD/*n*, or χ²/Fisher from counts). In the Word comment: cite the cells used, name the approximation, label the value an **estimate**. Green = same direction + same order of magnitude; yellow = within ~1 order of magnitude or rounding ambiguity; red = opposite direction or report *p*<0.05 while estimate ≫0.2 (or the reverse). **Comment only** — do not rewrite table cells or *P*. Missing SD/*n* → `cannot_invent`. Welch / continuity correction / survival / multivariable: annotate method mismatch; escalate formal recompute to **04**. Scope: primary result tables (spot-check Table 1); do not hand-calc every multiplicity *p*. |
| Multiplicity | Many ROI or voxel correlations with no correction and no exploratory label | Ask for the family and the method, or an uncorrected label |
| Relative unit | A relative measure whose denominator is undefined | Ask for the denominator; do not interpret the variance |
| Inclusion vs scale | Cutoff excludes values that the included group's median, Q1, or minimum still shows; IQR wider than the scale | Flag; do not rewrite the cutoff or the quartile |
| Circular *P* | Selection, threshold, and group test on one cohort, *P* written as confirmatory | Ask to relabel as descriptive, or to show nested CV / bootstrap if it was run. Do not invent a corrected *P* |
| Score identity | A named score is only a transform of one metric, or nested ROIs are treated as independent | Ask to name the transform and the dependence |
| Process language | `TRAIN_RATIO`, "as stated by the source", 待补, internal labels, empty queries, placeholder scan parameters, repeated disclaimers | Ask to delete them from the body and legends. Missing facts stay comments |
| Sister papers | Shared site, scanner, or ethics; an identical table; the same biomarker with a different *P* | `06_review/qc/cross-manuscript-qc.md`. Comment the conflict; do not average *P* or invent overlap counts |

**Hard rule:** when Abstract / body / table / sister paper disagree, **comment only**. Never silently pick a value for the author. A back-calculated *n*, critical value, or table→*p* estimate in the comment is labeled an **estimate** (see §3.1).

### 3.1 Table → *p* recipes

Spot-check primary between-group rows (e.g. Table 1). Comment only; never rewrite cells or *P*.

| Band | Meaning |
|---|---|
| Green | Same direction + same order of magnitude as printed *P* |
| Yellow | Within ~1 order of magnitude, or rounding / method ambiguity |
| Red | Opposite direction, or printed *p*<0.05 while estimate ≫0.2 (or the reverse) |

Formula map (schematic):

- mean±SD + *n* (two groups) → approximate two-sample *t* → *p*
- contingency counts → χ² or Fisher → *p*
- rates / proportions → binomial CI magnitude check
- 3+ groups / Welch / continuity / survival / multivariable → magnitude-only note; escalate formal recompute to **04**

Missing SD/*n* → `cannot_invent`. Do not hand-calc every multiplicity *p*.

---


## 4. Data-integrity protocol (stop conditions)

1. Number conflict across surfaces → annotate every locus; wait for author/HTML truth.
2. Missing IRB / author / CI slots → comment (author **A**); do not fill; do not yellow-fill body.
3. Suspicious perfect patterns or possible leakage → raise before continuing polish.
4. Material defects stay in the open (comments / Major issues). Do not “quiet-fix” them away.

---

## 5. Where the long form lives

`06_review/qc/cross-manuscript-qc.md` is the run order (statement, then data, then sister papers). `05_manuscript/qc/manuscript-local-qc.md` is the check-id list. `04_analysis/qc/report-checks.md` is the statistic definition. This file stays the habit: statement first, then data, annotate only.

## 5.1 Who revises the manuscript

Ownership: see `00_orchestrator/references/ownership-contract.md`.

Decidable issues: Lee annotates for Aitee to TC-fix. The note is concrete (locator, what is wrong, the word or sentence to change) so Aitee can apply Track Changes without guessing.

Undecidable issues: Chinese 批注 plus English suggested wording and/or suggested literature (see ownership-contract). Do not invent the missing fact. call/require 03 citation-verify — do not self-certify lit. After the user picks, Aitee applies Track Changes.

---

## 5.2 Chinese 稿面批注五槽 (Lab-STE CM-01)

Journal English envelope stays in `review.md` (`Lines n–m:` + defect + Please…).  
**Chinese Word face comments** (author field still **A**; source tag at text start) use five fixed slots, one problem per comment:

1. **位置** — line range, or `节 第n段第m句`, or Figure/Table id. Prefer precise patterns; coarse location-only wording (e.g. methods section alone) is should_fix.
2. **问题** — what is wrong, one sentence. One problem only (no stacking multiple unrelated defects in one comment).
3. **依据** — start with 依据; name a rule id and/or data source (结果页 / 术语表 / 课题锁定 / HTML / settings.ini).
4. **修改建议** — lead with an action verb (补写 / 删除 / 改为 / 替换 / 拆分 / 合并 / 核对 / 补充数值 / 写明 / 统一 / 移至 / 重算 / 增加 / 标注 / 改用). Ban vague 酌情 / 适当 / 进一步完善 / 提升规范性 / 注意语言润色.
5. **严重度** — `must_fix` / `should_fix` / `hint`.

**Severity crosswalk (mode and G-06 ↔ CM-01).** `pre-review` and G-06 grade Blocking / Major / Minor. The fifth slot grades `must_fix` / `should_fix` / `hint`. Judge G-06 with this map:

| Mode and G-06 | CM-01 严重度 |
|---|---|
| Blocking | `must_fix` |
| Major | `should_fix` |
| Minor | `hint` |

Strip leading source tags like `[A:personal]` before counting slots; tags stay at the comment start for delivery. Quoted paste-in rewrite text is exempt from sentence-length checks.

**Example:**

> [A:personal] Methods 第 2 段第 1 句。未写连续入组。依据 ZH-TERM01 与结果页队列句。补写：连续纳入 2019 年 1 月至 2022 年 12 月的病例。must_fix。

**Bad:** 方法部分整体不够清晰，建议完善并提升规范性，同时注意语言润色。

Full thresholds and regexes: `{doc_lab_ste}\` (`config.yaml` comment_schema; `Lab-STE-SPEC.md` CM-01). Summary pointer: `05_manuscript/personal/lab-ste.md`. Do not vendor the lab-ste tree.

Internal-review corpus (the user's own comments; style source only): `{doc_review_corpus}\`. Do not vendor.

## 6. What this file is not

- Not a license for one-character `?` comments as the default voice.
- Not the English peer-review envelope (use `review.md`).
- Not manuscript prose rewrite (changed sentences → `05_manuscript`).
- Not reviewer-response letters (use `response.md`).
