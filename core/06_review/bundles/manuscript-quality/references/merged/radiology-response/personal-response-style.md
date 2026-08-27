# 个人回复审稿人风格（基于历史信函归纳）

来源：对用户历史提交的近百份 response-to-reviewers / point-by-point 信件的比对归纳
（Qiang lab、Ying Li/Ju lab 等多个课题组稿件）。用于让 Claude 起草的回信读起来像
用户自己写的，而不是通用模板。**先套 `mode-3-response.md` 的骨架，再用本文件调声音、
调措辞、调收尾。**

---

## 1. 开头信件模板（三选一，按正式程度）

**A. 标准型（最常用，中等正式）**
```text
Dear Editors and Reviewers:

Thanks for the review of our manuscript and thanks for the suggestions. Those
comments are valuable and helpful for revising and improving our paper. We have
considered carefully these comments and have made relevant corrections
point-by-point.
```

**B. 加强型（大修 / 多轮修回，语气更郑重）**
```text
Dear Editor and Reviewers,

Thank you for the chance to revise our manuscript. We've carefully addressed the
reviewers' insightful comments and made relevant changes. Point-by-point responses
are provided in this letter and the annotated revised manuscript. We sincerely
appreciate the reviewers' excellent work and valuable feedback, which significantly
enhance our study and manuscript.
```

**C. 简短型（不写 Dear 抬头，直接进入正文，用于短信/单一审稿人少量意见）**
```text
Thank you for your detailed review and constructive feedback. We've carefully
addressed each comment with comprehensive revisions. Below is a point-by-point
response, with changes highlighted in bold or tracked in the attached document
for clarity.
```

默认用 A。审稿意见很尖锐/篇幅很长/是 R2 及以后时用 B。若用户明确说"简单回一下"用 C。

---

## 2. 每条意见的开场谢词——按意见类型分库

不要每条都写"Thank you for the suggestion"。根据审稿人这句话**实际在做什么**挑选：

| 审稿人在做什么 | 开场谢词 |
|---|---|
| 建议改一处表述/方法/呈现方式 | "Thank you for the suggestion." / "Thanks for the suggestion." |
| 提出疑问、要求澄清"为什么/如何" | "Thank you for the inquiry." / "Thanks for the inquiry." |
| 单纯提出观察/评论，未明确要求 | "Thank you for the comment." / "We thank the reviewer for this comment." |
| 给出正面评价 | "Thank you for your positive feedback on..." — 简短接受，不过度谦虚，不辩解 |
| 指出稿件中的**真实错误**（数字矛盾、图注错位、拼写） | "Thank you for pointing this out." / "We apologize for..." / "Upon review, we acknowledge that there were errors in..." |
| 要求做不了的事（外部验证、新实验、缺失数据） | 先认可价值："We agree/acknowledge that... is important for..."，再说明边界 |
| 重大方法学质疑（多重比较、循环分析、样本量） | "We thank the reviewer for this comment." 后接一段扎实的技术说明，不用寒暄带过 |

同一封信里这几种开场词要交替出现、按实际情况分配，不要通篇只用一种——这是历史信件里
真实呈现的分布，千篇一律的"Thank you for the suggestion"是能被一眼认出的 AI 味。

---

## 3. 正文句式骨架

```text
Response: [谢词]. We [revised/added/clarified/corrected] it in the [Section/Table/Figure].
"[逐字引用修改后或新增的句子]" We added/revised it in [具体位置，如 Discussion-paragraph 2 /
Methods-Statistical analysis / p. X, line Y]。
```

### 3.1 逐字引用是硬性习惯
凡是"改了一句话"或"加了一段话"，**必须在回复里用引号原样复述改后的文字**，
不能只说"we revised the sentence for clarity"就完事。审稿人和编辑要能在信里直接
看到新句子，不用去翻正文核对。

- 只改了一两个词：`"X" was revised to "Y" in the text.`
- 改写整句：`We revised it to "……"`
- 新增一段：`We added it in the text. "……"`

### 3.2 位置引用是硬性习惯
每一处改动后面都要跟位置标注，格式不追求统一，但必须具体、可定位：
`(Discussion-paragraph 2)` / `(Results section, Table 2)` / `(Methods-Statistical
analysis)` / `(Abstract-Methods, line 3)` / `(page 8, line 56)`。
绝不允许只写"revised accordingly"而不给出位置——这一条与
`response-audit-gate.md` 的可追溯性规则一致，是本用户信件里贯穿始终的硬指标。

### 3.3 给数字就给全套
被要求提供某个数值时，直接在回信正文里写出精确结果，而不是只承诺"已经加到正文"：
`The AUC of LC-MS in predicting PE from GH was 0.96 [95% CI: 0.91-1.00].`
`We have included ranges for all the values... The 3-year survival rates were
38.7% (19/49) for DC group and 20.5% (7/34) for PD group.`
技术细节（LASSO 阈值、ICC 界值、公式、精确 P 值）宁可写全，不写"see revised text"。

---

## 4. 认错的写法（审稿人抓到真实错误时）

固定四步，不多铺垫、不甩锅、不过度道歉：
1. 一句谢词认下来："Thank you for pointing this out." / "We apologize for this
   oversight."
2. 平实说明错在哪："There was a writing error in Table 1." / "We rechecked the
   data and confirmed..." / "A data filling error was found in Table 1."
3. 给出订正后的正确数值/表述。
4. 交代已改到哪。

示例（原信风格）：
> Thank you very much for the inquiry. We checked the original data and
> reperformed the statistical analysis. A data filling error was found in Table
> 1. We corrected it in the text.

不要写成"We sincerely apologize for this unfortunate mistake and any
inconvenience it may have caused..."这种过度道歉——用户历史信件里从不这样写。

---

## 5. 委婉拒绝 / 学术性不同意的写法

从不硬顶回去，也从不无条件妥协。三段式：
1. **先认可关切**："We agree that...", "We acknowledge this is an important
   limitation...", "We appreciate this important observation."
2. **说明边界原因**：研究设计（回顾性/单中心）、数据不可得、伦理限制、样本量、
   期刊字数限制等，讲清楚"为什么做不到"而不是"我们不想做"。
3. **落地成两选一**：
   - 提供能做的部分证据/文献支持（给出完整引用），或
   - 把限制原样写进 Limitation 段并在回信里引用原文。

示例（原信风格，数据不可得）：
> TMB score, MSI status were not obtained. Thus, we can't revise our models to
> include these factors and discuss their respective contributions to the
> predictive accuracy.

示例（原信风格，方法学争议但坚持己见）：
> We do agree that the varices veins is inappropriate to describe the 13
> selected veins. We change the "varices veins" to "collateral vessels" for the
> clarity for the readers.

**绝不编造未做的实验/分析/外部验证**——这条与 `response-audit-gate.md` 的
factuality lock 完全一致，本用户信件从未违反过。

---

## 6. 信件收尾——两种真实模板

**收尾模板 A（Qiang lab 风格，出现频率最高，多篇一字不差）：**
```text
We tried our best to improve the manuscript and made some changes which marked
in red in revised paper. We thank Editors and Reviewers' excellent works and
hope the modifications above meet your requests, and we trouble you to revise
any errors in this paper. If you have any queries about this modified paper,
please email to me (dr.jinweiqiang@163.com). Once again, thank you very much
for your comments, suggestions and considering the publication of our paper.

Your sincerely

Jinwei Qiang，MD.,PhD.
Chairman/Professor, Department of Radiology, Jinshan Hospital,
Fudan University, Shanghai, China
```
用于：Qiang 课题组内窥镜/影像组学系列稿件的回信，落款人是 Jinwei Qiang。

**收尾模板 B（无落款，直接结束）：**
最后一条回复写完即结束，不加致谢段、不加签名——多见于 MHE/schistosomiasis、
PCOS 等系列稿件。

默认用哪个取决于这次任务是否延续某个已知系列（同一批稿件、同一收件署名）。
不确定时问用户一句"要不要加标准结尾落款"，而不是自作主张套用 A。

---

## 7. 措辞微习惯（保留，不要"纠正"成教科书英语）

这些是用户信件里反复出现的非标准/半正式表达，**照用户原样保留**，不要替换成
更"标准"的说法，否则读起来就不像本人写的了：

- "Thanks for the suggestion"（不加 you）与"Thank you for the suggestion"混用。
- "Thank you for the reminding"（reminder 的非标准变体）——多篇稿件反复出现，
  遇到"感谢提醒/纠错"场景可用。
- "We clarified it in the text." / "We explicated it in the text." 两个近义收尾
  动词交替使用（explicate 是 MHE/PCOS 系列稿件偏好词）。
- "We admit that..."用于承认真实局限（而不是"We acknowledge that..."的通用说法，
  两者可混用但 admit 更口语化、更常出现在坦白采样偏倚/单中心/回顾性设计时）。
- Response 标签格式不强求统一：`Response:` / `**Response:**` / `Responses:`
  （复数，Qiang lab 少数信件）/ 中英文冒号混用 `Response：`。跟随该系列稿件已有
  的格式，不要在同一封信里来回切换。
- 意见与回复常以破折号列表呈现（`- ` 开头一条意见，`- **Response:**` 开头一条
  回复），也常以无编号纯段落呈现——两种都是本人真实用法，视稿件系列而定。

---

## 8. 使用方式

起草回信时：
1. 先用 `mode-3-response.md` 建立信件骨架、逐条 ID、change log。
2. 用本文件第 2 节挑选每条的开场谢词，避免重复单一模板。
3. 用第 3 节的引用+定位习惯写正文。
4. 遇到真错误按第 4 节四步走；遇到做不到的要求按第 5 节三段式走。
5. 收尾按第 6 节判断用哪个模板，不确定就问。
6. 全篇过一遍第 7 节，恢复几个用户本人的措辞习惯，去掉过于"客服式"的道歉腔调。
