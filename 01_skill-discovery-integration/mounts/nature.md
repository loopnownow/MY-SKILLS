# 预设 Nature · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md) · [OpenClaw · 备份](openclaw.md) · [AIPOCH · 备份](aipoch.md) · [Nature · 备份](nature.md)

仅用 Nature Skills（2026-09-07 HEAD）。**第三方包，非 Springer Nature 官方。** 仓库 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) · 配置 `../sources/nature-skills.proposed.yaml`

粗 ID 细拆（CHG-20260903-011）。共 30 个 A id。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 13 / 30（若干部分） |
| 空挂 | 17 |
| 扫描 | 2026-09-07 · `287ee37` |
| 许可 | Apache-2.0（根目录 LICENSE；部分子 skill 另有自己的 LICENSE） |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-tables` | — | `02_data-processing` | 临床表 Excel / CSV（含缺失/异常值） | 空挂 | 无对应包 |
| `02-imaging-io` | — | `02_data-processing` | CT/MRI 读写 · DICOM / NIfTI / NII | 空挂 | 无影像 IO |
| `02-imaging-qc` | — | `02_data-processing` | CT/MRI QC · ROI / 阅片 | 空挂 | 无对应包 |
| `02-pictures` | — | `02_data-processing` | 图片 TIFF / PNG / JPG / PDF(图) | 空挂 | 无对应包 |
| `02-fmri` | — | `02_data-processing` | fMRI · DICOM / NIfTI | 空挂 | 无对应包 |
| `02-radiomics-habitat` | — | `02_data-processing` | radiomics / 生境准备（建模交 04） | 空挂 | 无对应包 |
| `03-lit-search` | `skills/nature-academic-search/; skills/nature-literature-pipeline/` | `03_research` | 文献检索 | 已映射 | pipeline 是定时抓取+打分投递，不是综述 |
| `03-lit-fulltext` | `skills/nature-downloader/` | `03_research` | 全文获取 | 已映射 | 填补 Scientific/OpenClaw 空挂；机构/CNKI 路线需登录态 Chrome |
| `03-lit-review` | — | `03_research` | 综述 / 综合 | 空挂 | 单篇精读不进此 id |
| `03-lit-cite` | `skills/nature-citation/; skills/nature-ref-verifier/` | `03_research` | DOI→BibTeX / 引文校验 | 已映射 | citation 插入正文；ref-verifier 核已有列表 |
| `03-design-experiment` | — | `03_research` | 采集前实验设计 | 空挂 | 无对应包 |
| `03-design-protocol` | — | `03_research` | 写方案 / 填方案 | 空挂 | 无对应包 |
| `03-design-grant` | `skills/nature-proposal-writer/` | `03_research` | 标书（通用槽）；个人 Voice A/B 优先 | 已映射 | 触发名 researchwrite |
| `03-frontier-ideate` | — | `03_research` | 选题 / 头脑风暴 | 空挂 | 无对应包 |
| `03-frontier-hypothesize` | — | `03_research` | 问题化 / 假说 | 空挂 | 无对应包 |
| `04-stats-guide` | `skills/nature-statistics/` | `04_analysis` | 选检验 / 效应量（审查为主） | 部分 | 不做原始计算；A 04 personal / 0RAD 仍优先 |
| `04-stats-power` | — | `04_analysis` | 样本量 / 功效 | 空挂 | 无对应包 |
| `04-stats-models` | — | `04_analysis` | 统计/ML 拟合 | 空挂 | 无对应包 |
| `04-model-eval` | — | `04_analysis` | 校准 / DCA / 外验证 | 空挂 | 无对应包 |
| `04-fig-flow` | `skills/nature-figure/` | `04_analysis` | 图形摘要 / 机制示意图 | 部分 | AI 出图路线，非 STROBE gold |
| `04-fig-plot` | `skills/nature-figure/` | `04_analysis` | 统计图 / 影像拼图 | 已映射 | Python + R 双后端；POLE gold 仍 B/A |
| `04-explainability` | — | `04_analysis` | 影像模型可解释性 | 空挂 | 无对应包 |
| `05-write-manuscript` | `skills/nature-writing/` | `05_manuscript` | 论著/报告草稿 | 已映射 |  |
| `05-write-reporting` | `skills/nature-data/` | `05_manuscript` | 数据可用性 / FAIR | 部分 | 填补空挂，但不含 TRIPOD/CLAIM |
| `05-write-venue` | — | `05_manuscript` | 期刊体例 / house style（not 选刊） | 空挂 | 无对应包 |
| `05-write-polish` | `skills/nature-polishing/` | `05_manuscript` | 通用学术英语润色 | 已映射 | 含 LaTeX 版式修补；个人去 AI 层仍优先 |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 个人 de-AI 仍在 A |
| `06-review-peer` | `skills/nature-reviewer/` | `06_review` | 他审草稿 | 已映射 |  |
| `06-review-critique` | `skills/nature-reviewer/` | `06_review` | 自审 / 投稿前找洞 | 部分 | 与 review-peer 同一包 |
| `06-review-response` | `skills/nature-response/` | `06_review` | 回复审稿人 | 已映射 | 填补空挂；审稿人互盲。默认挂载仍是 B，本行只是备份路径 |

## 仅用当前挂载 · 空挂

**17 个空挂：** `02-tables` · `02-imaging-io` · `02-imaging-qc` · `02-pictures` · `02-fmri` · `02-radiomics-habitat` · `03-lit-review` · `03-design-experiment` · `03-design-protocol` · `03-frontier-ideate` · `03-frontier-hypothesize` · `04-stats-power` · `04-stats-models` · `04-model-eval` · `04-explainability` · `05-write-venue` · `05-humanize`。

若只用本套（不叠加 B），这些先通知再检索确认，不悄悄换源。个人 de-AI 仍在 A `05_manuscript/personal/`。批注前缀用 `[Nature:…]`。

## A 没有对应接口

仓库 20 个 skill，未进 30 个挂载 id 的按领域归组，不逐条抄进 A。

| 领域 | 例子（路径均在 `skills/`） | 备注 |
|---|---|---|
| PPT / 演示 | `nature-image2ppt/` · `nature-paper2ppt/` | 不是论文管线 id |
| 专利 | `nature-paper-to-patent/` | 中文技术交底书，超出论文管线 |
| 单篇精读 | `nature-paper-card/` · `nature-reader/` | 单篇分析/中英对照，非多篇综述 |
| 实验室系统 | `nature-experiment-log/` | 飞书/Obsidian 日志集成 |
| 内部依赖 | `nature-shared/` | 只服务其他 nature-* skill，不能单独挂 |

机器真源 `../registry.yaml` · 来源配置 `../sources/nature-skills.proposed.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
