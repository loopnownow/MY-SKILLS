# Intake

Use this file first when the user gives an incomplete, mixed, or high-level radiology
AI request.

Writing / figures → `05_manuscript`. Pre-submission / **journal** peer review / reviewer response → `06_review`.
Reviewing someone else's NSFC → Voice A (this file § Grant Voice A) (this skill, not 06_review). Writing your own → Voice B (this file § Grant Voice B). Do not mix the two voice habits.
Clinical translation / reader studies → `clinical-translation/` (under `advanced/`). Ethics form packs → `fill-protocol`.

## Task modes

| Mode | Use when | Default next module |
|---|---|---|
| `project-start-lit` | New project or unsettled endpoint / grouping: run full pre-analysis literature pipeline before stats / writing / deep analysis | `design-study` → `lit-search` → `verify-refs` (see `route.md` 项目启动前置); NLM + abstracts → `ref/refer/` |
| `guideline-first` | Endpoint / grouping needs a named guideline definition; usually the first step inside `project-start-lit` / `design-study` | Prefer `project-start-lit` for full chain; else 项目启动前置 → `route.md` then study card |
| `frontier` | User wants new research directions, hotspots, or innovation points | Frontier |
| `literature` | User wants recent papers, evidence maps, or search terms | Literature |
| `evidence` | User wants 2023-2026 high-impact literature patterns, representative PMID/DOI seed papers, or journal publication patterns behind topic selection | Evidence |
| `public-datasets` | User asks about TCIA, TCGA, GEO, CPTAC, IDC, public imaging/omics datasets, or public validation cohorts | Public datasets |
| `radiomics` | User describes handcrafted features or Pyradiomics-style workflow | Radiomics |
| `deep-learning` | User describes CNN, transformer, segmentation, classification, foundation models, or multimodal AI | Deep learning |
| `mechanism` | User asks how radiomics/deep learning model scores relate to genomics, transcriptomics, single-cell, spatial transcriptomics, pathways, immune microenvironment, or biological mechanisms | Mechanism |
| `study-design` | User gives data and asks what project can be done | Design |
| `grant-writing` | User asks to **write/polish their own** NSFC/provincial/university proposals, opening, protocol, abstract (Voice B) | Grant (own) → this file sections Grant Voice B (+ skeleton + method upgrade) |
| `grant-review` | User asks to **review someone else's** NSFC/general/cross applications (Voice A) | Grant (others) → this file section Grant Voice A. Do not use 06_review English boilerplate |
| `annotation` | User asks about ROI, VOI, mask, lesion selection, segmentation annotation, reader agreement, or ICC/Dice | Annotation |
| `statistics` | User asks about statistical analysis, sample size, feature selection, LASSO, Cox, C-index, calibration, DCA, confidence intervals, or survival analysis | Statistics |
| `validation` | User asks whether the model or result is reliable | Validation |
| `multicenter` | User asks about multicenter data, external validation by center, scanner/vendor/protocol differences, center effects, harmonization, or domain shift | Multicenter |
| `checklist` | User asks about CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, METRICS | Checklists |
| `data` | User asks about DICOM, NIfTI, masks, labels, privacy, repository, or sharing | Data |
| `ethics` | User asks about ethics approval, IRB, consent waiver, privacy, de-identification, or data-use limits | Ethics |
| `reproducibility` | User asks about code, model weights, feature tables, random seeds, environment, supplementary files, or reproducibility | Reproducibility |
| `writing` | User asks for Methods, Results, Discussion, abstract, title, or translation | Writing |
| `figures` | User asks about figures, tables, graphical abstracts, figure legends, workflows, ROC/calibration/DCA/KM plots, or mechanism diagrams | Figures |
| `pre-submission` | User asks for pre-submission audit, simulated reviewer critique, manuscript risk review, or top-journal readiness | Pre-submission |
| `journal-selection` | User has a draft/manuscript and asks where to submit, whether a journal fits, or how to choose target journals | Journal selection (选刊) → `journal-selection.md` + `find-journal/` |
| `clinical-translation` | User asks about clinical utility, reader study, prospective validation, workflow integration, PACS/RIS, deployment, or real-world evaluation | Translation |
| `response` | User gives reviewer comments or revision notes | Response |

## Study card

Collect these fields when available:

```yaml
disease:
clinical_question:
modality:
data_format:
n_patients:
n_images_or_lesions:
centers:
time_span:
labels:
endpoint:
follow_up:
segmentation:
annotation_strategy:
readers:
reader_agreement:
clinical_variables:
omics_data:
paired_omics:
omics_sample_size:
omics_platform:
split_plan:
external_validation:
center_distribution:
scanner_protocols:
statistics_plan:
main_metrics:
calibration_dca:
figure_needs:
public_dataset_plan:
ethics_approval:
consent_status:
data_sharing_limits:
code_availability:
clinical_use_case:
reader_study_plan:
model_type:
target_journal_or_output:
candidate_journals:
publication_goal:
funding_scheme:
proposal_section:
grant_deadline_or_year:
main_constraint:
```

## Clarifying question rule

Proceed with explicit assumptions when the user wants brainstorming or a rough plan.
Ask before final wording when missing facts would otherwise fabricate:

- sample size or patient/lesion/image unit
- endpoint or label source
- segmentation source and reader agreement
- train/validation/test split unit
- external validation status
- reported performance values
- ethics, consent, code, or data availability

## Fast routing examples

- "我有 200 例 CT 想做预后模型" -> Design + radiomics or DL + validation
- "近三年影像 AI 前沿有哪些" -> Frontier + literature
- "根据近三年高水平期刊发表规律帮我选题" -> Evidence + frontier + literature + design
- "影像组学模型做完了，想结合转录组和单细胞解释机制" -> Mechanism + radiomics + literature + validation
- "帮我润色国自然立项依据" -> Voice B grant (own) + design skeleton + frontier method upgrade. No review tics
- "帮我评这份国自/面上" -> Voice A (this file section Grant Voice A) five columns. Do not write justification five steps or CN/EN abstract skeleton
- "ROI 是两位医生勾画的，Methods 怎么写" -> Annotation + radiomics + checklists
- "LASSO、Cox、DCA、C-index 这部分统计对不对" -> Statistics + validation
- "帮我看 Methods 是否符合 CLAIM" -> Checklists + DL + validation
- "帮我规划论文图表和 figure legend" -> Figures + writing + checklists
- "投稿前帮我模拟审稿人预审" -> Pre-submission + validation + checklists + figures
- "代码、特征表和模型参数怎么放补充材料" -> Reproducibility + data + ethics
- "4 家医院数据怎么做外部验证和中心差异分析" -> Multicenter + validation + statistics
- "想用 TCIA/TCGA/GEO 做验证或机制解释" -> Public datasets + literature + mechanism + data
- "伦理、知情同意豁免和数据共享怎么写" -> Ethics + data + reproducibility
- "这个模型怎么做读者研究和临床转化" -> Translation + validation + statistics
- "文章写好了，帮我选刊" -> Journal selection (选刊) + literature + checklists + validation
- "结合近三年类似文章发表情况判断能不能投 Nature Medicine" -> Evidence + journal selection + literature + pre-submission
- "新课题启动，先做文献和指南" -> `project-start-lit` (`design-study` → `lit-search` → `verify-refs`; NLM+abstracts → `ref/refer/`)
- "审稿人说没有外部验证怎么回复" -> Response + validation

---

## Absorbed grant packs (2026-10-30)

Standalone `grant-review.md` / `grant-writing.md` / `grant-own-skeleton.md` / `method-upgrade-into-grant.md` are pointer stubs. Full bodies live below. `radiology-design` / `radiology-frontier` / `multicenter` left unchanged this round (their links resolve via stubs).

### Grant Voice A (review others)

**This is for reviewing someone else's NSFC / general / youth / cross / original / goal-oriented proposal. Not for writing your own.**

- Writing your own justification / defense / protocol / abstract → § Grant Voice B (or stub `grant-writing.md`) + `radiology-design.md` + `radiology-frontier.md` (Voice B).
- English journal peer review / pre-submission / 回复审稿人 → `06_review`. Do not fill NSFC form fields with English imperatives like “Please clarify”.
- Do **not** mix the two voice habits: 「创新性有限」「可行性欠佳」 here must never enter your own proposal.

Placeholders only: `[Title]` `[疾病]` `[技术]` `[n]` `[PI]`. Do not put the applicant's hypothesis, pathways, unpublished patient tables, ethics scans, or phone numbers into the skill or output library.

First **restate in one sentence what the application does** (applicant's own terms; do not invent a new mechanism), then score innovation / feasibility / basis.

## System five fields (general / routine; fill the fields)

1. `请简述申请项目的主要研究内容和申请者提出的科学问题或假说`
2. `请评述申请项目的预期结果及其科学价值和意义`
3. `请评述科学问题或假说是否明确，是否具有创新性，并予以说明`
4. `请评述研究内容、研究方案及所采用的技术路线是否能验证所提出的科学问题或假说，方法的逻辑性、可行性如何`
5. `请评述申请人的研究能力（研究经历、水平等方面）；是否具备完成该项目的研究条件（材料、样本、设备等）`

Other: `其它意见或修改建议`

Bands:

- Overall: A 优（4）/ B 良（3）/ C 中（2）/ D 差（1）
- Funding: A 优先资助 / B 可资助 / C 不予资助
- Familiarity: 熟悉 / 较熟悉 / 不熟悉

Rules: overall A/B → funding only 优先 or 可资助; C → 可资助 or 不予; D → only 不予.

## Goal-oriented / cross / original variants (recent forms)

- `请评述该申请项目是否面向经济社会发展需要或国家需求背后的基础科学问题。请详细阐述判断理由。`
- `请评述申请项目所提出的科学问题的创新性与预期成果的科学价值。`
- `请评述该申请项目的研究基础与可行性；如有可能，请对完善研究方案提出建议。`
- `请针对创新点详细评述申请项目的创新性、科学价值以及对相关领域的潜在影响。`
- `请结合申请项目的研究方案与申请人的研究基础评述项目的可行性。`
- `请评述申请人的创新潜力与研究方案的可行性。` / `多学科背景和研究专长`
- `该申请项目的研究思想或方案是否具有新颖性和独特性？`
- `该申请项目的研究内容是否具有原创性并值得鼓励尝试？`

Still restate in one sentence first, then answer that field's question. Do not force the five general-field titles onto a cross form.

## Critique phrase bank (reusable; applicant science already stripped)

**Brief field (neutral restatement)**

```
申请者拟使用[技术]对[对象]进行[研究]，以[验证/探讨][科学问题]，为[临床/转化目标]提供[依据]。
```

**Innovation / scientific question**

- `该申请项目有具体的技术指标，预期结果有一定的创新及科学价值。`
- `该项目的科学问题比较明确，但创新性有限。`
- `该项目的科学问题比较明确，具有创新性。`
- `科学假说比较明确，但关键科学问题阐述尚有不足。`
- `假说的证据链不够完善，科学性欠佳。`
- `立项依据泛泛而谈，没有形成一个良好的研究假设。拟解决的科学问题范围过大。`

**Plan / feasibility**

- `该项目研究内容目标较为明确，研究方案和采用技术路线比较合理，有可行性。`
- `研究方案合理，研究内容明确，技术路线清晰，具备完成该项目的可行性。`
- `研究方案过于粗陋，可行性欠佳。`
- `现有的方案无法证明该研究的假设。`
- `关键性的研究基础不足，完成可行性差。`

**Applicant ability / conditions**

- `申请人具有较好的研究能力。但前期研究结果显示均为临床研究，未详细阐述是否具备完成[动物/分子]实验的研究条件。`
- `申请人具一定的研究能力，但未显示较好的前期研究基础。`
- `不足之处在于前期尚没有与该项目相关的论文发表。`
- `申请人研究基础较为薄弱。` / `代表性高质量论文成果较为欠缺。`
- `团队具备多学科背景。` / `研究团队配备有待进一步完善。`
- `不具备[AI/分子影像/动物]研究的基本条件，可行性不高。`

**Other comments (format and actionable advice)**

- `标书书写中有错别字。`
- `立项依据中未对引用文献进行标注。部分标点符号的格式不统一。`
- `建议进行样本量估算，增加科学依据，确保研究具有足够的统计效能。`
- `强化盲法设计与偏倚控制。`
- `建议申请者加强前期研究，加强训练科研设计的合理性与严谨性。`
- `预算说明中材料费及检测费的计算依据不够详细。`
- `建议把前期工作基础制成组图。`
- `可进一步完善前期实验，为向临床转化提供依据。`

## Fill order

1. Brief (applicant's own terms; one short paragraph)
2. Is the scientific question clear; does innovation hold
3. Can the plan/route test the hypothesis; logic and feasibility
4. Applicant ability and completion conditions (materials, samples, equipment)
5. Actionable revision advice (format, sample size, blinding, budget basis, panel figures)
6. Overall + funding opinion (obey band rules)

Tone may be more direct than English peer review, but still about the work not the person: no applicant name, unit, unpublished data, or pathway-figure detail.

## Do / Don't

- Do: answer by system field; phrases are reusable, but science must come from **this** application — do not invent pathways from memory.
- Don't: put pathway figures, unpublished patient tables, name/unit, phones, or ethics scans into the skill or a public repo.
- Don't: fill NSFC fields with `06_review` English peer-review boilerplate.
- Don't: write Voice B “确定 / 阐明 / 探讨” goal tiers or ZH/EN abstract skeletons as critique.
- Don't: invent scoring reasons to force A/B. If one axis is weak (innovation / value / basis / feasibility), write to that weakness.

### Grant Voice B (write your own)

**This file is for writing your own proposal / proposal defense / protocol / abstract.**
Reviewing someone else's NSFC / general / cross-disciplinary → § Grant Voice A (or stub `grant-review.md`) (Voice A). Do **not** mix voice habits: never put 「创新性有限」「可行性欠佳」「方案过于粗陋」 into your own draft.

Chapter skeleton (five-step justification, two innovation columns, three feasibility blocks, three goal tiers) → § Grant Voice B chapter skeleton.
Method upgrades into the proposal (MRS → hyperpolarized 13C / metabolic flux → multimodal+ML) → § Grant Voice B method upgrade into justification.
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
| Content | 2-4 progressive work packages; each has input, method, output | Parallel pile-up; no progression |
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
| Key scientific questions | 1-3 falsifiable sentences | Title restated |
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

关键词中英各 4-5 个，顺序：疾病、机制词、方法、表型。不要把医院名和基金类型写进关键词。

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

### Grant Voice B chapter skeleton

**This is for writing your own NSFC / municipal science / health commission / hospital / proposal-defense / clinical protocol.**
Reviewing someone else's NSFC → § Grant Voice A (or stub `grant-review.md`) (Voice A). Do not put 「创新性有限」「可行性欠佳」 into this draft.

Placeholders: `[Title]` `[疾病]` `[表型]` `[技术]` `[n]` `[PI]` `[假说]` `[动物模型]` `[平台]`.
Do not write unpublished patient-level result tables, ethics-scan PDFs, phone numbers, or full applicant pathway text.

Do not delete official subsection titles; below is the fill rhythm.

## Document types and outlines (fill under official titles)

| Doc type | Skeleton (do not delete official titles) |
|---|---|
| NSFC youth/general **报告正文** | （一）立项依据与研究内容 → 研究目标/关键科学问题 → 方案及可行性 → 特色与创新 → 年度计划及预期结果 → （二）研究基础与工作条件 |
| NSFC **摘要** (CN + EN each one para) | Burden/gap → prior finding → hypothesis → planned methods + validation → expected theory/clinical meaning → keywords. Phrasing in § Grant Voice B (or stub `grant-writing.md`) |
| Municipal science **可行性方案** | Trend judgment and needs analysis (domestic/abroad status + innovation points) → research content / tech key points / implementation → duration and schedule → existing basis and conditions. Move the two innovation columns into part 1 |
| City/district health commission **申请书正文** | Nearly isomorphic to NSFC body; annual plan in half-year blocks「完成 [n] 例 / 完成 XX 检测」; at district level write goals as measurable indicators |
| Hospital / youth-start **申请书、任务书** | Rationale → purpose and significance → study design (content/methods/route/key points) → research basis → completion metrics (paper tier + talent training) |
| **临床研究方案** inside the ethics pack | Purpose → protocol (inclusion/exclusion/termination/intervention/outcomes/stats) → research basis. ICF forms go through the ethics skill |

PPT, budget sheets, finance, contract scans, title/talent tables, filled ethics packs, images, Excel data: do not enter this skill body.

## Justification (立项依据): fixed five steps

1. **Disease burden + typology/grading.** Clarify the object first (including subtype controls). Give 1-2 epidemiology numbers — do not dump a review.
2. **Mainstream theory and its gap.** Typical phrasing: traditional hypothesis “cannot explain” poor correlation of [marker] with clinical phenotype, poor response to usual care, or disease despite normal markers. Gaps must be concrete — avoid empty「尚未完全阐明」.
3. **Prior work (literature + own).** 「文献和我们前期工作均显示」「我们前期研究发现」. Clinical phenomenon → imaging/omics evidence → animal or ex vivo validation — at least two of three chains.
4. **One-sentence hypothesis.** 「故推测…可能是…的主要和起始因素」; or「基于前期研究提出如下假说：…是由 A 与 B 共同驱动的 C」.
5. **What this study will do.** Noninvasive imaging / labeled metabolism / multimodal ML + animal (or cell) validation. Land on「完善发病机制 / 提供诊断分级方法 / 有助于治疗」.

Justification subsection titles use **mechanism nodes**, not method names. Method innovation and tech gaps (e.g. 1H-MRS cannot quantify) belong in the justification — not only in the innovation box. How to write method upgrades → `radiology-frontier` / § Grant Voice B method upgrade into justification.

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

Required blocks: purpose (testable clinical question) → design (prospective/retrospective, n) → inclusion/exclusion/termination/withdrawal → intervention and outcomes → data and stats. Inclusion/exclusion as bullets, not paragraphs. Put n in the design sentence: `收集[疾病]患者[n]例。` Phrasing in § Grant Voice B (or stub `grant-writing.md`).

## Do / Don't

- Do: justification uses mechanism subsection titles; innovation splits idea/method; feasibility names instruments and case sources; abstract five steps + one hypothesis sentence.
- Do: when animal and clinical lines cross-validate, state in the key question which contributes more / whether it can be reversed by intervention.
- Don't: put review boilerplate（「创新性有限」「方案过于粗陋」）into your own application.
- Don't: let the innovation box only repeat「我们用了 MRI/AI」.
- Don't: paste a 30-page NSFC mechanism review into a district health-commission application without changing assessment metrics.
- Don't: fill the ethics clinical protocol with proposal-style review; the protocol needs inclusion/exclusion and risk.

### Grant Voice B method upgrade into justification

**Put the method upgrade into the justification narrative — do not start a parallel essay, and do not dump it only in the innovation box.**
Reviewing someone else's NSFC → § Grant Voice A (or stub `grant-review.md`) (Voice A). Whether the topic is new enough / journal landscape → other files in this bundle; this chapter only answers how the upgraded method nests into the proposal justification.

Placeholders: `[Title]` `[疾病]` `[表型]` `[技术]` `[n]` `[PI]` `[假说]`. Do not write unpublished patient tables, ethics scans, phones, or full pathway text.

## Upgrade chain (method words — not pretending old work is new)

When writing justification, pick words by the **current** method generation. Do not write backwards: early drafts must not claim unfinished techniques as completed basis.

| Generation | Method words (tech gap in justification → this study) | How to use in justification |
|---|---|---|
| Baseline spectroscopy | 1H-MRS / in vivo + ex vivo MRS | As an existing readout; name the gap: low sensitivity/specificity, **cannot quantify [molecule]** |
| Upgrade 1 | Hyperpolarized 13C-MRS / metabolic-flux tracing (substrate → product) | Against the prior gap: quantify [molecule], trace [A]→[B] |
| Upgrade 2 | Multimodal imaging + interpretable ML | Against subjective scales / single-modality limits: integrate heterogeneous data and predict phenotype; gold standard still pathology or scales |

The chain belongs in the **justification body** (tech-gap paragraph under a mechanism-node heading). The innovation box only gets one sentence on “what method replaced that gap” — do not rewrite the review there.

## How to write it into justification (nest it; no new chapter)

1. **Subsection titles are mechanism nodes**, not method names. Methods are evidence, not chapter titles.
2. After “mainstream theory and its gap” or right after prior work, nail the tech gap in a short paragraph:
   - `[技术]敏感性、特异性低，且无法对[分子]进行定量。`
   - `目前通常采用[量表]协助诊断，缺乏客观评估手段，容易受到主观因素影响。`
3. “What this study will do” continues from the gap: noninvasive `[升级技术]` ± animal/cell validation — not a sudden unrelated new platform.
4. Align the two innovation columns with justification:
   - Method column = countermeasure to the named gap (1H-MRS cannot quantify → hyperpolarized 13C; subjective scales → radiomics / interpretable ML).
   - Idea column = mechanism one step forward — not “we used MRI.”

## Drop-in justification closers (placeholders)

```
如果能探寻[代谢节点]，示踪[A]到[B]的过程，有望早期发现[表型]，并进一步揭示发病机制。
我们拟使用无创的[升级技术]，检测[对象]的[读出]。通过比较[因素]与[表型]的相关性，并使用[对照模型]加以验证。
```

From 2022, abstracts can nail one sentence each (NSFC fields are short — these two earn their space; full bank in § Grant Voice B (or stub `grant-writing.md`)):

```
技术上拟创新性使用[技术]对[分子/表型]进行定量。
理论上创新性提出[分子]通过[通路]导致[细胞事件]，最终导致[表型]。
```

## Key scientific questions (after the method upgrade)

Question form fits general/cross schemes:

- `如何实现多模态异质数据的智能整合与精准预测？传统统计方法难以同时处理包含[临床/代谢/炎症/影像]的高维异质数据。本研究拟基于机器学习算法，构建具可解释性的跨模态预测模型。`
- `[疾病]相关[表型]的病理核心机制是什么？目前尚不清楚多系统异常如何协同作用。本研究拟通过整合[组学A]、[组学B]与[影像]数据，揭示[轴]的动态互作机制。`

Statement form fits early/youth: `使用在体和离体[技术]阐明[表型]干预前后的特征性代谢谱及其变化规律。`

## Division of labor vs other frontier files

- `03_research/advanced/radiology-frontier.md` + live `design-study` / `lit-search`: whether the direction is new, whether data can support it, what journals require for validation.
- **This file:** once the path is MRS → hyperpolarized 13C / flux → multimodal+ML, **which paragraph of the justification gets which sentence**.
- Do not put Voice A critique (「创新性有限」) or English journal “Please clarify” into the justification.

