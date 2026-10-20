<!-- Engine: 03_research/base/find-journal/; A personal is Victor pointer only. -->
# 选刊

Use this file when a manuscript, abstract, or near-complete study is available and
the user asks where to submit, which journal fits, how to rank target journals, or
how to position the paper for submission.

## 核心原则

选刊不是只看影响因子。先判断“文章证据强度”和“期刊发表偏好”是否匹配，再决定冲刺、稳妥和保底梯队。

不要承诺“必中”“容易中”或用过期影响因子做决定。期刊范围、版面费、审稿政策、开放获取政策、影响因子和文章类型要求可能变化；给最终建议前要联网核验目标期刊官网、近期发表文章和投稿须知，并写明检索日期。

当用户要求“结合近三年高水平期刊发表规律”“这篇文章适合投 Radiology/Lancet Digital
Health/Nature Medicine/npj Precision Oncology 吗”时，先读取：

- mounted `meta-analysis` (B `04_analysis/base/meta-analysis/`) — former `literature-evidence-2023-2026.md` retired 2026-09-22
- this file §「2023-2026 期刊规律」(merged below; former journal-patterns-2023-2026.md archived 2026-10-16)

这些文件提供的是 PubMed 验证的种子证据和期刊规律，不是完整系统综述。最终投稿建议仍需当天核验目标期刊官网和近期同类文章。

## 输入信息

尽量收集：

```yaml
title:
abstract:
study_type:
disease:
modality:
sample_size:
centers:
external_validation:
prospective_or_retrospective:
reader_study:
clinical_endpoint:
main_results:
calibration_or_dca:
code_data_availability:
novelty_claim:
target_region_or_specialty:
article_type:
candidate_journals:
must_avoid:
publication_goal: 冲高分 / 稳妥发表 / 快速发表 / 专科影响力 / 开放获取
```

## 评价维度

| 维度 | 高匹配信号 | 降级信号 |
|---|---|---|
| 临床问题 | 明确临床痛点、目标人群和使用场景 | 只是“建一个模型” |
| 数据强度 | 多中心、外部验证、前瞻/读者研究、清楚标签 | 单中心、小样本、标签弱、无外部验证 |
| 方法可靠性 | 患者级划分、避免泄漏、校准、DCA、亚组和失败案例 | 只报告 AUC 或 Dice |
| 创新性 | 临床工作流、泛化、机制解释、多模态生物学联系 | 仅更换模型结构 |
| 期刊契合 | 近期发表同类主题、栏目匹配、读者群一致 | 主题偏离期刊 scope |
| 可复现性 | 代码、模型、数据或特征表有可用路径 | 数据/代码完全不说明 |

## 期刊梯队逻辑

按稿件证据强度给 3 个梯队：

1. **冲刺期刊**：需要临床问题强、验证强、创新点清楚。通常适合多中心、外部验证、前瞻/读者研究、真实工作流或机制解释充分的文章。
2. **主投期刊**：与疾病、模态、方法和读者群高度匹配，是最现实的投稿目标。
3. **备选期刊**：当创新性、样本量或验证强度不足时，选择专业方向更匹配、方法学要求相对适中的期刊。

影像 AI 常见候选池可以从这些类别开始，再按具体稿件核验：

- 综合医学和数字医学：Nature Medicine、The Lancet Digital Health、npj Digital Medicine、JAMA Network Open、eClinicalMedicine、EBioMedicine。
- 肿瘤和精准医学：The Lancet Oncology、Cell Reports Medicine、npj Precision Oncology、Clinical Cancer Research、European Journal of Cancer。
- 影像和放射学：Radiology、Radiology: Artificial Intelligence、European Radiology、Investigative Radiology、American Journal of Roentgenology、Academic Radiology。
- 专病专科：按疾病选择肝胆、肺癌、乳腺、神经肿瘤、泌尿、消化、核医学或超声方向期刊。
- 方法和工程：Medical Image Analysis、IEEE Transactions on Medical Imaging、IEEE Journal of Biomedical and Health Informatics、Computerized Medical Imaging and Graphics。

不要把这些期刊当成固定推荐清单。必须结合文章主题、近期发表情况、栏目类型、文章长度、开放获取、版面费和投稿政策重新筛选。

## 近期发表情况整合

当用户要求“结合现有文章和发表情况选刊”时：

1. 用文章关键词生成检索式：疾病 + 模态 + 任务 + 方法 + endpoint。
2. 检索近 3-5 年目标期刊同类文章，优先看同疾病/同模态/同任务文章。
3. 提取每篇文章的：期刊、年份、疾病、模态、样本量、验证方式、主要方法、主要结论。
4. 判断用户文章与这些文章相比的强项和短板。
5. 将期刊分为 `高度匹配`、`可尝试`、`不建议优先`。

## 输出格式

```text
投稿定位
- 文章类型：
- 核心卖点：
- 最大短板：
- 适合的读者群：

期刊梯队
| 梯队 | 期刊 | 匹配理由 | 需要补强 | 风险 |

近期发表对照
| 期刊 | 近年同类文章特点 | 与本文相比 |

文献规律差距
- 与 2023-2026 高水平期刊规律相比：
- 代表性 PMID 种子：

投稿前修改建议
- 标题/摘要：
- Methods：
- Results：
- Discussion：
- 数据和代码：

不建议投稿的期刊或方向
- [期刊/方向]：原因

需要作者确认
- [缺失事实]
```

## 红线

- 不要只按影响因子排序。
- 不要推荐掠夺性期刊或无法核验的期刊。
- 不要说“这个一定能中”。
- 不要忽略目标期刊是否近期发表过同类研究。
- 不要把无外部验证、小样本、弱标签研究包装成适合顶刊，除非它有其他非常强的设计优势。


## JCR 分层荐刊包（金山）

当用户要「推荐杂志 / 按 JCR·JCI 分层选刊 / 易投指数」时，加载个人包：

- `03_research/base/find-journal/SKILL.md`（权威流程；Victor；version ≥ **1.14**；Gemini+ChatGPT 2026-09）
- `03_research/base/find-journal/references/AGENTS.md`（须与 SKILL/policy 一致）
- 策展表：`{jcr2026_xlsx}`
- 指数与模块：`03_research/base/find-journal/rules/jesi-model.md`（JESI/JEI / JDI / JCI-C / **MJF=MFI** / PAI）、`modules.md`、`query-sources.md`
- 持久化：`03_research/base/find-journal/rules/persistence.md` — **absorb / query / delete** 表；投稿 URL 与个人先验可存；年度 IF/分区/年发文量/APC 等 **QUERY ONLY**（勿写入 `{find_journal_pools}/2026/submission-urls.csv`）；**Unknown ≠ Low Risk**；无固定权重政策（动态加权）

本文件仍负责证据强度 vs 期刊偏好、冲刺/稳妥/保底叙事，以及 §「2023-2026 期刊规律」 below / mounted `meta-analysis` 对照。分层表输出以个人包为准（默认**层2→层3→层4，每层10本**；层2≈主攻/Target、层3≈稳妥/Safety偏上、层4≈Q3；**层2补**冲刺默认不出、每次用前询问；黑名单三刊永不荐；投过/选刊白名单（`whitelist-submitted.csv`）层内优先；灰名单（含 Frontiers 系列）有更好匹配则不荐（`graylist.csv`））。层内排序：稿件匹配度 → 投稿易投指数 → 年发文量（弱）。Medicine 刊名层内降权、表中不标可疑；仅 JESI≥80 黄底。外部 journal-recommender 仅作查询/候选池，不作顶层决策。 Phase-2 用户短表（按 paper）：期刊全称｜JCR分区｜影响因子｜年发文量｜投稿网址/作者须知（完整 URL）；无 ISO/OA/置信/APC/分刊详情；细则见 `03_research/base/find-journal/`。

选刊走 03 `find-journal`；体例走 `05_manuscript/base/write-venue/`。

---

## 2023-2026 期刊规律（merged from journal-patterns-2023-2026.md, 2026-10-16）

> Former standalone file archived to `D:\0del\03_research_reorg_20261016\`. Keep this section with the 选刊 SOP.

Use this section when the user asks where to submit a radiomics,
medical imaging AI, radiogenomics, or imaging deep learning manuscript and wants advice
grounded in recent high-impact publication patterns.

## Evidence boundary

本文件只负责「证据强度 vs 期刊偏好」的取舍。期刊家族规律表及其免责声明以 `05_manuscript/base/write-venue/references/journal-patterns-2023-2026.md` 为准，不在本文件重复。

## Journal pattern table

| 期刊家族信号表（2023–2026 种子） | 见 `05_manuscript/base/write-venue/references/journal-patterns-2023-2026.md`（SSOT，本文件不再复制） |

Representative PMID seeds used for this pattern map include 37690911, 38876123,
39775040, 41876649, 37268451, 38519154, 39070173, 37557177, 39244594, 39112796,
41339572, and 38809149. Use mounted `meta-analysis` (B `04_analysis/base/meta-analysis/`) for the full seed; `literature-evidence-2023-2026.md` was retired 2026-09-22
table and DOI-level metadata.

## Submission-tier logic

### Tier A: top clinical AI journals

Examples: Nature Medicine, The Lancet Digital Health, The Lancet Oncology for appropriate
oncology questions.

Usually needs at least one of:

- prospective, randomized, real-world, or reader-study evidence;
- strong multicenter external validation;
- clear effect on clinical pathway or decision-making;
- broad disease burden or screening/program-level relevance;
- transparent reporting, calibration, and utility analysis.

### Tier B: strong clinical/translational medical journals

Examples: eClinicalMedicine, EBioMedicine, Cell Reports Medicine, Radiology, npj Digital
Medicine, npj Precision Oncology depending on topic.

Usually needs:

- clinically meaningful endpoint;
- robust retrospective or multicenter validation;
- clear baseline comparison;
- calibration/decision utility if prediction is claimed;
- mechanism or precision oncology link when relevant.

### Tier C: focused radiology AI or specialty journals

Usually suitable when:

- study is retrospective and clinically useful but not broad enough for top-tier;
- external validation is limited or absent but methods are transparent;
- the paper contributes a disease-specific model, workflow, or reproducibility resource.

## Manuscript-positioning rules

- If no external validation: do not recommend top-tier clinical AI journals as realistic
  unless the study has another major strength such as prospective reader evidence.
- If single-center and no reader study: frame as exploratory or model-development work.
- If multicenter but pooled random split: downgrade because this is not external validation.
- If radiogenomics/multi-omics: match to npj Precision Oncology, Cell Reports Medicine,
  or disease-specific translational journals only when pairing and biology are credible.
- If foundation model: Nature Medicine/Nature Communications-level framing requires scale,
  generality, external validation, and reusable contribution.
- If clinical utility is claimed: require calibration, DCA/net benefit, threshold-action logic,
  and ideally reader/workflow evidence.

## Output rule

```text
文献规律驱动的选刊判断
- 证据来源边界：
- 文章当前证据等级：
- 与近三年高水平期刊规律的差距：

期刊梯队
| 梯队 | 期刊 | 近三年规律匹配 | 当前短板 | 投稿前升级动作 |

不建议直接投的期刊
| 期刊 | 原因 |

需要当天核验
- scope, author instructions, data/code policy, article type, similar recent papers
```

## Red lines

- Do not promise acceptance.
- Do not rank only by impact factor.
- Do not use a seed paper as proof that the user's weaker design fits the same journal.
- Do not invent journal policies, APCs, turnaround times, or recent publications.
- Do not hide single-center, no-external-validation, or AUC-only limitations.
