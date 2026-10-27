# Own-proposal chapter skeleton — Voice B (writing yours)

**This is for writing your own NSFC / municipal science / health commission / hospital / proposal-defense / clinical protocol.**
Reviewing someone else's NSFC → `grant-review.md` (Voice A). Do not put 「创新性有限」「可行性欠佳」 into this draft.

Placeholders: `[Title]` `[疾病]` `[表型]` `[技术]` `[n]` `[PI]` `[假说]` `[动物模型]` `[平台]`.
Do not write unpublished patient-level result tables, ethics-scan PDFs, phone numbers, or full applicant pathway text.

Do not delete official subsection titles; below is the fill rhythm.

## Document types and outlines (fill under official titles)

| Doc type | Skeleton (do not delete official titles) |
|---|---|
| NSFC youth/general **报告正文** | （一）立项依据与研究内容 → 研究目标/关键科学问题 → 方案及可行性 → 特色与创新 → 年度计划及预期结果 → （二）研究基础与工作条件 |
| NSFC **摘要** (CN + EN each one para) | Burden/gap → prior finding → hypothesis → planned methods + validation → expected theory/clinical meaning → keywords. Phrasing in `grant-writing.md` |
| Municipal science **可行性方案** | Trend judgment and needs analysis (domestic/abroad status + innovation points) → research content / tech key points / implementation → duration and schedule → existing basis and conditions. Move the two innovation columns into part 1 |
| City/district health commission **申请书正文** | Nearly isomorphic to NSFC body; annual plan in half-year blocks「完成 [n] 例 / 完成 XX 检测」; at district level write goals as measurable indicators |
| Hospital / youth-start **申请书、任务书** | Rationale → purpose and significance → study design (content/methods/route/key points) → research basis → completion metrics (paper tier + talent training) |
| **临床研究方案** inside the ethics pack | Purpose → protocol (inclusion/exclusion/termination/intervention/outcomes/stats) → research basis. ICF forms go through the ethics skill |

PPT, budget sheets, finance, contract scans, title/talent tables, filled ethics packs, images, Excel data: do not enter this skill body.

## Justification (立项依据): fixed five steps

1. **Disease burden + typology/grading.** Clarify the object first (including subtype controls). Give 1–2 epidemiology numbers — do not dump a review.
2. **Mainstream theory and its gap.** Typical phrasing: traditional hypothesis “cannot explain” poor correlation of [marker] with clinical phenotype, poor response to usual care, or disease despite normal markers. Gaps must be concrete — avoid empty「尚未完全阐明」.
3. **Prior work (literature + own).** 「文献和我们前期工作均显示」「我们前期研究发现」. Clinical phenomenon → imaging/omics evidence → animal or ex vivo validation — at least two of three chains.
4. **One-sentence hypothesis.** 「故推测…可能是…的主要和起始因素」; or「基于前期研究提出如下假说：…是由 A 与 B 共同驱动的 C」.
5. **What this study will do.** Noninvasive imaging / labeled metabolism / multimodal ML + animal (or cell) validation. Land on「完善发病机制 / 提供诊断分级方法 / 有助于治疗」.

Justification subsection titles use **mechanism nodes**, not method names. Method innovation and tech gaps (e.g. 1H-MRS cannot quantify) belong in the justification — not only in the innovation box. How to write method upgrades → `radiology-frontier` / `method-upgrade-into-grant.md`.

For municipal science feasibility plans, move “domestic/abroad status” and “academic-idea / technical-method innovation” into part 1; write fewer goal sentences inside the justification.

## Research content / goals / key questions

**Research content** uses executable verbs + object + method, numbered (1)(2)(3) or 1.1/1.2.
- Animal block fixed order: modeling → behavior/cognition → imaging/spectroscopy → omics or enzyme/pathology → stats.
- Clinical block: enroll with scales to define phenotype → scan/sample → between-group compare and correlate.

**Research goals** use three verb tiers「确定 / 阐明 / 探讨」(do not make 探讨 the only goal):

| Tier | Use for | Example (placeholder) |
|---|---|---|
| 确定 | Whether a marker changes; whether an intervention works (animal-testable) | 确定[表型]大鼠脑内[指标]变化，确定[干预]对[表型]有无影响 |
| 阐明 | Mechanism, spectrum, pathway interaction | 阐明[表型]大鼠脑[技术]代谢谱的变化，及其与[因素]的关系 |
| 探讨 | Diagnostic grading, translation | 探讨[技术]对[表型]诊断及分级的作用 |

**Key scientific questions to solve:** recent general/cross schemes prefer question form; early NSFC may use statements. Under each question, 2 sentences: why traditional methods fail → what this study will do.

- Statement: `使用在体和离体[技术]阐明[表型]干预前后的特征性代谢谱及其变化规律。`
- Question: `如何实现多模态异质数据的智能整合与精准预测？` ` [疾病]相关[表型]的病理核心机制是什么？`

Do not copy-paste goals and content: content is a step list; goals are verifiable propositions. District/hospital schemes may hard-code accuracy numbers; NSFC rarely should.

## Innovation: split into two columns

Almost every self-written body uses **academic-idea innovation** + **technical-method innovation**. Do not treat「我们用了 MRI」as innovation.

- **Idea:** one step forward from a prior node. Use「在前期研究基础之上，提出…」.
- **Method:** against the tech gap named in justification ([old tech] cannot quantify [molecule] → [upgrade]; subjective scales → radiomics / interpretable ML).

Hospital AI drafts may add a third「可解释性 / fill a sequence-specific model gap」— still tie to a pathology gold standard; do not only hype network architecture.

Do not write: `本研究具有创新性。` `填补国内外空白。` Do not repeat the justification review in the innovation box.

## Feasibility: reviewers must see three blocks

1. **Mature model:** name guideline/literature-recommended or own published modeling. Give timepoints and enrollment rules (phenotype present → enroll; absent → control).
2. **Platform named to instruments:** `[平台]` has `[仪器]`, can perform `[测量]`. On the tech roadmap, write the executing unit next to each node.
3. **People:** `[PI]` visiting experience, SCI count (may say「其中本方向 [n] 篇」), ongoing related grant IDs. A bare「掌握各项实验技能，能确保课题顺利实施」is too empty — follow concrete platforms.

Clinical feasibility also needs: **case source**（「每年接诊 [疾病] 超过 [n] 例」）+ ethics and data security (no approval-letter scans, no phones). District/hospital schemes especially need the case-source line.

## Annual plan and expected outcomes

- NSFC / health commission: half-year blocks,「完成 [n] 例造模 + 某检测」. Do not write a whole year as only「撰写论文」.
- Expected results: write **scientific propositions** first (quantify a metabolite, clarify a pathway, inhibiting a protein alleviates a phenotype), then paper tier and talent training.
- District/hospital assessments may hard-code accuracy and case counts; NSFC prefers scientific propositions.

## Clinical research protocol (before ethics initiation)

Not the same document as the proposal body: the protocol must let ethics members judge risk — it does not need a full mechanism review.

Required blocks: purpose (testable clinical question) → design (prospective/retrospective, n) → inclusion/exclusion/termination/withdrawal → intervention and outcomes → data and stats. Inclusion/exclusion as bullets, not paragraphs. Put n in the design sentence: `收集[疾病]患者[n]例。` Phrasing in `grant-writing.md`.

## Do / Don't

- Do: justification uses mechanism subsection titles; innovation splits idea/method; feasibility names instruments and case sources; abstract five steps + one hypothesis sentence.
- Do: when animal and clinical lines cross-validate, state in the key question which contributes more / whether it can be reversed by intervention.
- Don't: put review boilerplate（「创新性有限」「方案过于粗陋」）into your own application.
- Don't: let the innovation box only repeat「我们用了 MRI/AI」.
- Don't: paste a 30-page NSFC mechanism review into a district health-commission application without changing assessment metrics.
- Don't: fill the ethics clinical protocol with proposal-style review; the protocol needs inclusion/exclusion and risk.
