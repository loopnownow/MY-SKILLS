# Response letter (style + resolution)

## Structure digest (0doc absorb 2026-10-23)

Letter skeleton + unique bans: `references/response-structure-digest.md`. Type stubs: `references/response-letter-template-digest.md`. **Do not fork** opener nouns / thanks bank — this file remains SSOT.


## Hard rules (owner 2026-10-19)

- **Do not invent** response-letter format. Follow the existing comment shell / venue template / gold layout only.
- Keep each reviewer/editor comment **verbatim and complete**. Do not simplify, paraphrase, shorten, or drop clauses.
- **Do not** add invented subheadings (no extra `Editor comment N` / thematic mini-titles unless already in the shell).
- Editing an existing `.docx` response or comments shell: use **Track Changes**; word- or sentence-level inserts only—**no** large-block overwrite.
- Typography (manuscript = comments = response): Times New Roman, 12 pt, 1.5 line spacing, paragraph before/after 0, text before/after 0, justify, LTR, **no special paragraph format**. Do not change fonts/layout unless the owner asks this turn.


## Part A — Response letter voice

## Package and wording hard rules

- Deliver as `.docx`. Requirements read `Please …`, never `Please fix:`.
- Quote the reviewer comment in full; use past tense for changes already made.
- Do not open a resolved item with `We agree that…`. Do not write `we will…` for a change already claimed.
- `ACCEPT-*.html` only when the user names it this run. Delivery goes to the folder the user already used for the project (e.g. `{WORK_B}\in-review\<project>`).
- Each point maps to one reply row and names its location; after revision re-check page, number, sample size, and citation.

# 个人回复审稿人风格（基于历史信函归纳）

来源：他审 response 全库去重 42 封（Qiang lab、Aitor/Ju lab 等多个课题组）。只收骨架与
谢词分布，不 dump 整信、不抄未刊结果。用于让起草的回信读起来像用户自己写的。
**本文件即回信骨架与声音真源**（旧 `mode-3-response.md` 未单独建档）。开场默认 A；B 几乎不用。分诊与裁决另见 `response.md`。

磁盘语料（外部评阅与 revise 回复、修改）：`{doc_review_replies}\`。索引入口：`{doc_review_replies}\_index\00-master-index.md`、`{doc_review_replies}\02-flattened\`。本文件不复制语料全文。

---

## 1. 开头信件模板（默认 A；B 几乎不用）

**Standing letter opener (owner 2026-10-21):** After the salutation, open with one of:
**Thank you for your comments** | **Thank you for your suggestions** | **Thank you for your inquiry** —
pick the noun that fits the reviewer's tone/content (comments = observations/critique; suggestions = concrete change requests; inquiry = questions/clarifications). Do not invent a fourth noun bank for the letter opener. Per-point谢词 still follow §2.

**A. 标准型（最常用，中等正式）**
```text
Dear Editors and Reviewers:

Thanks for the review of our manuscript and thanks for the suggestions. Those
comments are valuable and helpful for revising and improving our paper. We have
considered carefully these comments and have made relevant corrections
point-by-point.
```

**B. 加强型（几乎不用；不要当历史主体）**
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

**默认用 A。** 全库 42 封 response 实测：A 约 21；B（chance to revise / insightful comments）约 0–2，几乎不用；C 约 1。不要因为「大修 / 多轮 / R2」就切到 B——多轮修回仍在 A 上加一句 `Thank you for giving us an opportunity to resubmit`。仅当用户明确要求更郑重的英文才用 B。若用户明确说「简单回一下」用 C。

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
本文件 §3.2 的可追溯性规则一致，是本用户信件里贯穿始终的硬指标（旧 `response-audit-gate.md` 未单独建档）。

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

**绝不编造未做的实验/分析/外部验证**—— factuality lock；本用户信件从未违反过。

---

## 6. 信件收尾——两种真实模板

**收尾模板 A（Qiang lab 风格，出现频率最高，多篇一字不差）：**
```text
We tried our best to improve the manuscript and made some changes which marked
in red in revised paper. We thank Editors and Reviewers' excellent works and
hope the modifications above meet your requests, and we trouble you to revise
any errors in this paper. If you have any queries about this modified paper,
please email to me (见 mem:response_email). Once again, thank you very much
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
1. 用本文件建立信件骨架、逐条 ID、change log；需要分诊时对照 `response.md`。
2. 用本文件第 2 节挑选每条的开场谢词，避免重复单一模板。
3. 用第 3 节的引用+定位习惯写正文。
4. 遇到真错误按第 4 节四步走；遇到做不到的要求按第 5 节三段式走。
5. 收尾按第 6 节判断用哪个模板，不确定就问。
6. 全篇过一遍第 7 节，恢复几个用户本人的措辞习惯，去掉过于"客服式"的道歉腔调。

---

## 9. 改文单元与批注来源（与 00/05 对齐）

- 落实意见时，修改单元是 **词或句**，禁止整段重写。回信里引号复述的也是改后那一句。Ownership: see `00_orchestrator/references/ownership-contract.md`.
- 每条意见是否真正解决：用 `response.md` 的状态（Resolved / Partially resolved / Unresolved / New issue）；不要只看「有没有加一句」。
- 稿面批注标明来源：`[A:personal]` / `[B:revise]` / `[B:…]` 等。
- 挂载建议与实验室口径冲突：批注写清冲突点 + 修改方案（改前/改后），**用户决定**。点头后仍由 Aitee 用 Track Changes 改正文。Lee 默认不改正文。
- 可决定的正文修改：Lee 批注交给 Aitee TC-fix。过去时只用于已经落地的修改。
- 事实仍不可决（缺来源、缺分析、伦理号未定）：回复信**对应那一条**必须写明未决，并写待补来源（pending source）。不得把该条写成已经改完。`Suggested …` 建议句只放 Word 批注（见 ownership-contract），不作为 invent / disclaimer 写进回复正文。不假装已做实验。
- **否定句 / 未做类（owner 2026-10-23）：** 凡标「未做 / 未进行 / 我们未…」或同类 CYA 的过程性否定句，**不得写入正文**（稿件、修订稿、回复信）。只进 Word **批注**（作者 **A**），且每条批注必须含 **建议修改后内容**；禁止裸 flag。研究本身的阴性结果（如 *no significant difference*、*was not associated with*）不受本条禁止。质控：`05_manuscript/qc/anti-leak-placeholders.md` AL-5；`07_response/qc/disclaimer-comment-only.md`。

---

## Uncertainty and disagreement (回复审稿人画像)

Corpus habit for **审稿回复** (not for inventing data):

- Keep replies short and concrete. Confirm, clarify, or refuse with evidence — no long defense essays.
- If the reviewer is wrong on a fact, politely correct **with the source** (HTML row, table, guideline). Do not rewrite the paper into an incorrect request.
- If you do not know (missing analysis, missing file, ethics Date/NO unset): the matching response point says the fact is still pending a source. Past tense only for edits already made. `Suggested …` and `cannot_invent` stay in the Word comment, not as invent disclaimers in the letter.
- Attitude lock: **uncertain → mark; never pretend certainty.**



---

## Part B — Resolution protocol

# Review Resolution protocol (thin)

**Bot map:** response upper layer (07) → **Lee** (`07_response`); re-review Lee (`06_review`); literature substitute search if needed → **Victor** (`03`); manuscript Track Changes → **Aitee** (`05`). Ownership: see `00_orchestrator/references/ownership-contract.md`.

**Owner:** `07_response` personal. Final judgment on whether a review issue is truly fixed lives here (eight-section review / response voice). **Not** a B06 upgrade and **not** an A06 permanent three-engine dispatcher.

**Loop (lab):**

```text
Mounted review source (this-run pick: B / MedSci / Scientific / AIPOCH / Nature)
  → findings (optional status draft)
  → A 06 personal: post-QC re-review integrate / eight-section
  → A 07 personal: response letter / resolution status (final authority)
  → conflicts stay in comments; user decides
  → wording → 05; stats/figures → 04; evidence gap → Evidence Request → 03
  → 00 G-06 / G-LIT
```

Mount packs **propose** findings. They do **not** free-collaborate with each other, do not own Aitor review voice, and do not silently close an issue. A **07** **judges** Resolved / Partially resolved / Unresolved / New issue. 00 owns cross-skill QC and whether to re-invoke siblings.

Related: English peer-review envelope `06_review/personal/review.md`; response letter voice this file; claim gaps while writing `05_manuscript/personal/process/evidence.md`.

Disk corpus (external reviewer comments and revise replies; pointer only): `{doc_review_replies}\` (`{doc_review_replies}\_index\00-master-index.md`, `{doc_review_replies}\02-flattened\`).

## When to use

- `response` mode: after author revisions, verify each reviewer point was actually addressed  
- `pre-review` / re-audit: reopen prior Major/Minor items and set status  
- Mounted `peer-review` / `self-review` / `revise` (or backup source) returns findings that need consolidation under A 06  

Do **not** use this file to invent rescue experiments, missing AUCs, or unrun analyses. Ownership: see `00_orchestrator/references/ownership-contract.md`. Ask the user on undecidable items; do not edit the manuscript until the user picks, and then Aitee applies Track Changes.

## Issue card (required)

One card per atomic reviewer/pre-review point. Word comment author field stays **A**. Prefix the discoverer when a mount raised it; dual-tag with `[A:personal]` when A 06 also judges.

```text
Review Issue
────────────
issue_id: <R-001>
severity: <blocking | major | minor>
original_problem: <short>
domain: <stats | design | imaging | writing | refs | other>
source: <mount id or A:personal>
claimed_fix: <what the author/revision says was done>
checks:
  - methods_text: <yes|no|na>
  - results_numbers: <yes|no|na>
  - tables_figures: <yes|no|na>
  - conclusions_aligned: <yes|no|na>
status: <resolved | partially_resolved | unresolved | new_issue>
next: <close | weaken_claim | ask_user | call_04 | call_05 | evidence_request | reschedule_mount>
```

`status` is set only by **A 06 personal** after the checks. Mount drafts are suggestions.

## Roles

| Step | Who | May | Must not |
|---|---|---|---|
| Discover finding | Mounted pack (this-run) or A 06 | Raise/fill draft card | Cross-talk with other mounts; apply lab-rule conflicts silently |
| Route siblings | `00_orchestrator` | Call 02/03/04/05 when handoff says so | Treat 06 as manuscript writer |
| Judge resolution | **A 06 personal** | Set status; draft response / re-review text | Put “personal review intelligence” into B; auto-mount backup sources |
| Session mounts | 01 pick | Attach B / MedSci / Scientific / AIPOCH / Nature for this run | Permanent A06 three-pack sub-dispatcher; fixed Reviewer A/B/C pipeline |

A06 stays the review/response **entry** and personal upper layer. Capability labels / fine ids stay on `01_skill-integration/registry.yaml` + generated `MOUNTED_SKILLS.md` — do not fork a second A06-only registry of full skill texts.

## Resolution checklist (A 06)

For each issue, do not stop at “author added a sentence.” Prefer:

1. Was the **method** actually changed (or a justified refusal documented)?  
2. Do **Results / Tables / Figures** match the claimed fix (e.g. adjusted *P*, new CI)?  
3. Does the **conclusion / abstract** still depend on the pre-fix claim?  
4. Did the fix create a **new_issue**?  

Then set one status:

| Status | Meaning |
|---|---|
| `resolved` | Checks pass; safe to close in the response letter |
| `partially_resolved` | Something fixed, residual risk remains → keep open + `next` |
| `unresolved` | Claimed fix missing or cosmetic only |
| `new_issue` | Revision introduced a new defect |

## Three exits when not resolved

### A. Ask user / keep open
Need data, ethics, or unrun analysis → question the user; optional reference-only sentence; no silent edit.

### B. Call sibling
Wording → 05 (word/sentence). Even a decidable wording fix stays a comment for Aitee to TC-fix. Lee 默认不改正文. Numbers/figures → 04. Prep/imaging verify → 02. Literature fact → Evidence Request → 03 (not a second lit route inside 06). Victor supplies suggested literature for comments when needed.

### C. Reschedule mount (rare)
Only if this-run pick left a needed pack unloaded — go through **01 session-mount pick** again; never auto-mount a non-base source.

## Out of scope

- B06 as “Review Intelligence Core” or resolution home  
- A06 as always-on MedSci+Scientific dispatcher  
- Fixed Reviewer A→B→C personas  
- Mount packs writing free-form Word comments without status cards when this protocol is in use  
- Any backup becoming a standing fourth reviewer

## Corpus reply skeletons (2026-10-23)

Frequency evidence + per-point skeleton: `personal/references/corpus-reply-skeletons.md`.
Standing letter opener remains authoritative here: **Thank you for your comments** | **suggestions** | **inquiry**.
