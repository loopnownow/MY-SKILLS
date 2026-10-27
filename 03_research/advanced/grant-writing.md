# Grants (writing your own — Voice B)

**This file is for writing your own proposal / proposal defense / protocol / abstract.**
Reviewing someone else's NSFC / general / cross-disciplinary → `grant-review.md` (Voice A). Do **not** mix voice habits: never put 「创新性有限」「可行性欠佳」「方案过于粗陋」 into your own draft.

Chapter skeleton (five-step justification, two innovation columns, three feasibility blocks, three goal tiers) → `grant-own-skeleton.md`.
Method upgrades into the proposal (MRS → hyperpolarized 13C / metabolic flux → multimodal+ML) → `method-upgrade-into-grant.md`.
Chinese/English abstracts, hypotheses, and inclusion/exclusion phrasing use **only** the sentence bank below (placeholders `[Title]` `[疾病]` `[n]` `[PI]`); do not copy Voice A critique habits.

Use this file when the user asks to write, polish, restructure, or strengthen a
grant/funding proposal for radiomics, medical imaging deep learning, or imaging AI
projects, including 国家自然科学基金 / 国自然, provincial NSFC, university/hospital schemes,
青年基金, 面上项目, 重点项目, and similar. For international schemes such as NIH R01,
ERC, or Wellcome, verify applicant and host-institution eligibility before drafting
(no separate radiology-grant bundle; when international eligibility is unclear, do not promise “ready to submit”).

## Core principles

Polishing a grant is not making the language prettier. It is making the chain
“clinical need → scientific question → hypothesis → aims → technical route → innovation → feasibility” clear.

Do not paste paper-style prose into a grant. Grant text must stress why funding is warranted, what the scientific question is, why the applicant can finish, and how risk is controlled.

Guidelines change by year, region, and scheme. For limits, format, word count, codes, budget, ethics, host institution, attachments, and annual priorities, remind the user to follow **this year's** official guide and verify online when needed.

International schemes cannot simply reuse NSFC logic. For NIH, ERC, Wellcome, or other cross-border funds, first check
PI nationality/region, host institution, collaborators, budget channel, subaward/host institution, data export, and ethics
requirements; if eligibility or channel is unclear, do not generate a full “ready to submit” commitment.

## Information to collect

```yaml
funding_scheme: 国自然青年/面上/地区/省自然/院校课题/其他
eligibility_context: applicant / host / collaborators / region / international?
proposal_section: title/abstract/justification/aims/key questions/route/innovation/feasibility/basis/timeline/outcomes
disease:
modality:
clinical_problem:
scientific_question:
hypothesis:
data_basis:
preliminary_results:
team_basis:
methods:
innovation_points:
risk_control:
word_limit:
target_year_or_guideline:
current_text:
```

If the user only has a rough idea, fill the research logic first; if they gave concrete paragraphs, diagnose then polish.

## Common proposal modules

| Module | What to write | Common failure |
|---|---|---|
| Title | Disease, modality, core method, scientific question or use case | Reads like a paper title; missing scientific question |
| Abstract | Pain point, question, hypothesis, ~3 aims, expected contribution | Tech-noun pile-up; no clear hypothesis |
| Justification | Clinical need, domestic/international status, key gap, this project's entry | Literature dump; weak problem condensation |
| Scientific question | Core mechanism / law / generalization / interpretability / translation question | Written as an engineering task or “build a model” |
| Aims | What question is answered when the project finishes | Aims too large or unverifiable |
| Content | 2–4 progressive work packages; each has input, method, output | Parallel pile-up; no progression |
| Technical route | Data, model, validation, explanation, statistics, risk control | Flowchart only; no critical nodes |
| Innovation | Problem / data / method / validation / mechanism novelty | “First / fills a gap” without evidence |
| Feasibility | Prior data, team, tech base, platform, ethics, collaboration | “We have conditions” without evidence |
| Expected outcomes | Scientific insight, model/tool, papers, data/code, translation base | Paper-count only |

## NSFC structure and review axes (general / youth shape; other types follow this year's outline)

Submission channel: NSFC information system (grants.nsfc.gov.cn). Open window, deadlines, lump-sum vs itemized budget, and application limits — always verify against **this year's** Project Guide; do not reuse last year's dates or budget rules. Host-institution account and seals are administrative prerequisites, not writing steps, but they take lead time.

Do not mix paragraph duties:

| Paragraph | Write | Do not write as |
|------|--------|----------|
| Justification | Argue the gap: problem → status → this entry. Highest review weight | Literature dump |
| Research content | Actual work packages | Synonym restatement of aims |
| Aims | What will be proven / delivered | Another task list |
| Key scientific questions | 1–3 falsifiable sentences | Title restated |
| Plan and technical route | Methods detailed enough to judge feasibility; usually with a route figure | Empty flowchart |
| Feasibility analysis | Forward: can this team, these pilots, these methods finish now | A copy of “research basis” |
| Features and innovation | What is new vs cited work | “First / fills a gap” without contrast |
| Research basis and conditions | Backward: pilots, related papers, equipment / cohort / collab | “Experienced” without names |
| Annual plan and outcomes | Year milestones mapped to aims | Vague paper counts |
| Budget | Itemized schemes only; youth is often lump-sum — follow this year's guide | Fake line items under lump-sum |

Review axes (check after drafting; prose polish cannot fix a weak axis): **innovation**, **scientific value/significance**, **research basis**, **feasibility**.

Imaging / radiomics plans must at least state: enrollment plan, scan protocol, ROI/segmentation, feature extraction and validation, statistical validation plan. Research basis should name prior papers and cohorts in this disease — not “long engaged in.”

Tone follows `05_manuscript` caution (no unsupported “first / fills a gap”; calibrate hedges), but **do not** force paper IMRAD / Aitor labeled-abstract style into a proposal.

## Radiomics / imaging-DL grant emphasis

### Radiomics

- Stress links between imaging phenotype and pathology, molecular, immune microenvironment, efficacy, or prognosis.
- State ROI/mask, feature stability, IBSI, batch effects, feature selection, and model validation.
- Do not write “extract features and model” as the scientific question; write whether a quantifiable imaging phenotype reflects a biological heterogeneity or clinical outcome.

### Imaging deep learning

- Stress weak labels, small samples, multi-center shift, generalization, interpretability, calibration, and clinical workflow.
- Explain why the model is necessary — not only “use Transformer/CNN/foundation model to raise accuracy.”
- Connect algorithm novelty to the clinical scientific question.

### Multimodal / radiogenomics

- Stress complementary mechanisms across imaging, clinical, pathology, molecular, and omics.
- State missingness, sample size, label reliability, and external validation.
- Avoid writing multimodal as simple concatenation.

## Polish strategy

Turn weak phrasing into grant-style phrasing:

| Weak | Better grant direction |
|---|---|
| We will build a prediction model | Parse association between imaging phenotype and [endpoint/biology], and build a verifiable risk framework |
| Raise diagnostic accuracy | Improve stability and interpretability across centers/devices |
| Use deep learning | Design interpretable, calibratable, externally validatable imaging-AI methods around [question] |
| Important clinical significance | May provide quantitative basis for [population]'s [screening/stratification/efficacy/follow-up] |
| No reports domestic or abroad | Prior work still weak on [data/labels/validation/mechanism/setting] |

## Output format

```text
Grant positioning
- Scheme type:
- Main line to emphasize:
- Weakest link now:

Diagnosis of the draft
- Scientific question:
- Logic structure:
- Language style:
- Method credibility:

Structure strengthen
- Justification:
- Aims:
- Content:
- Technical route:
- Innovation:
- Feasibility:

Polished text
[Rewrite only provided paragraphs; invent no new facts]

Author must confirm
- [sample size, prior results, team basis, ethics, budget type, word limits, …]
```


## Sentence bank (ZH/EN abstract / hypothesis / inclusion) — Voice B only

占位：`[Title]` `[疾病]` `[表型]` `[技术]` `[n]` `[PI]` `[假说]` `[动物模型]` `[平台]`。人名、电话、伦理号不要写进句中。

### Chinese abstract skeleton (keep ZH templates)

```
[疾病]（[英文缩写]）在[人群]中[发生率/危害]，[临床隐匿/缺乏客观指标]。
[主流学说]作为传统发病机制，不能解释[血指标与临床表现相关性差 / 常规治疗不佳 / 指标正常仍发病]等现象。
我们前期研究发现[关键临床或影像事实]。故推测[假说]。
我们拟使用[无创技术]，在[患者 / [动物模型]大鼠]中检测[读出]，并通过[对照模型或干预]加以验证，
期望完善[疾病]的发病机制，为[诊断/分级/治疗]提供新的思路。
```

区科委 / 影像组学变体（把「机制」换成「客观筛查」）：

```
目前[表型]的诊断缺乏客观评估手段，容易受主观因素影响。
如果能使用无创的影像学手段对[系统/脑区]进行全面评估，则有望客观地对[表型]进行早期筛查。
本研究拟使用[常规MRI/多模态]得到影像组学数据，通过[深度学习/机器学习]与临床信息相结合，
建立[表型]预测模型，期望为早期筛查提供新的思路与方法。
```

国自摘要栏很短，2022 起可各用一句钉死创新：

```
技术上拟创新性使用[技术]对[分子/表型]进行定量。
理论上创新性提出[分子]通过[通路]导致[细胞事件]，最终导致[表型]。
```

### English abstract skeleton

早期（青年）：

```
[Disease] is a common but covert complication of [population]. Conventional [theory] fails to explain [gap].
The literature and our previous work showed that [finding]. We hypothesize that [hypothesis].
In this study, [models] will be used. [Readouts] will be investigated by [technique].
The study aims at clarifying the role of [factor] in [phenotype], and to explore the feasibility of using [marker] to diagnose [phenotype].
```

技术 / 理论双创新（面上）：

```
Technically, [technique] combined with [enhancement] could be used to quantify [analyte].
Hypothetically, we propose that [analyte] may [mechanism] and eventually [phenotype].
We plan to establish [animal] and [cell] models; [analyte] would be quantified by [labeling]; [intervention] would be used.
Through systematic research, we hope to clarify the mechanism of [A] in regulating [B] in [phenotype].
```

关键词中英各 4–5 个，顺序：疾病、机制词、方法、表型。不要把医院名和基金类型写进关键词。

### Hypothesis (ZH templates)

- `故推测[因素]可能是导致[表型]的主要和起始因素。`
- `基于前期研究提出如下假说：[表型]是由[因素A]与[因素B]共同驱动的[下游事件]所致。`
- `我们假设：有[表型]时[底物]主要经[通路1]代谢，而无[表型]时主要经[通路2]代谢。`

立项开场（定义句，一句话把对象关死）：

- `[疾病]是由[原发]引起的、以代谢紊乱为基础的中枢神经系统功能失调综合征。`
- `[表型]指没有典型临床表现及体征，但在某些认知领域已经发生异常的一种[疾病]亚型。`
- `[表型]以[注意力/反应时间/工作记忆]缺陷为特征，严重影响患者生活质量。如不及早诊断和干预，将进展为更严重的[显性表型]，增加死亡率。`

### Inclusion / exclusion (bullet items for clinical protocols; not paragraphs)

```
纳入：（1）有[疾病]病史；（2）[影像]有[疾病]表现；（3）近期（[窗口]内）确诊[表型]。
排除：（1）临床诊断为[需排除的鉴别]；（2）[MRI禁忌/严重并发症]；（3）无法完成[量表/随访]。
```

例数写在设计句：`收集[疾病]患者[n]例。` 不要把入排写成长段落。

### Two innovation columns / three feasibility blocks (phrasing; chapter rhythm in design skeleton)

```
技术方法创新：本课题组拟通过更高灵敏度、分辨率和特异度的[技术]，对[分子]进行精准定量。
学术思想创新：在前期研究基础之上，提出[分子]通过[通路]介导[细胞事件]，最终导致[表型]，并拟通过系统性研究阐明上述机制。
```

```
使用[动物模型]模拟[表型]是成熟模型（[指南或文献]推荐），大鼠在术后[时间]形成[表型]。
[平台]拥有[仪器型号]，可进行[测量]，为[样本类型]研究提供技术支撑。
[PI]掌握[小动物MRI/MRS/组学数据处理]及数据后处理技术；相关方向已发表 SCI 论文[n]篇。
每年接诊[疾病]超过[n]例，积累了图像和临床诊断数据，为课题提供数据基础。
```

## Red lines

- Do not put Voice A critique habits (「创新性有限」「可行性欠佳」) into your own proposal.
- Do not put full proposal text, unpublished patient tables, ethics-scan PDFs, or phone numbers into GitHub or skill bodies.
- Do not invent prior results, papers, patents, prior grants, team members, collaborators, ethics approvals, or platforms.
- Do not use unsupported “first worldwide,” “fills a gap,” or “significantly improves.”
- Do not promise clinical use beyond the validation evidence.
- Do not ignore this year's official guide, format, and word limits.
- Do not treat model performance as the only innovation.
- Do not assume a China-based applicant/institution can be the primary NIH/ERC/Wellcome applicant without checking eligibility.

