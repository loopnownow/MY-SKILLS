# 混合挂载指针说明（细 ID 配方表）

[总览](README.md) · [迁移 v3→v4](MIGRATION_v3_to_v4.md) · [registry.yaml](../registry.yaml)

**用途：** 会话点选时的「细 ID → 来源包 → 原子技能」对照。粗 ID 是阶段桶（焊死 10 个）；细 ID 才是挂载点。同一细 ID 内不混包；不同细 ID 可来自不同包（混合挂载）。

**图例**

| 标记 | 含义 |
|---|---|
| ✅ B默认已含 | 原子技能已在 `MY-SKILLS-capabilities`（本仓 B） |
| 🟡 新增挂载 | 审计补进 B 的 MedSci 本体（见 capabilities PR） |
| 🔵 跨包补充 | Scientific / AIPOCH / Nature 等；多为 PROPOSED，启用前确认 |
| 🟢 跨包已挂载 | 跨包来源，已从 PROPOSED confirm 为 MOUNTED（非 B 默认，仍需按细 ID 单独按需拉取） |
| ⚪ 规则参考 | 不挂载字节；原则写入对应 B 技能的 `external-principles.md`（2026-09-14：原四条已升 🟢，本表无残留 ⚪） |

**硬规则：** Nature LICENSE 已核实为 Apache-2.0（2026-09-14）；正式 `MOUNTED` 仍须 ask-each-run 细 ID 多选 + `mounts-cap/` 字节到位，不因许可证已核实而自动挂载。选刊决策权威仍在 A `03_research/medical-journal-submit`（Victor），不因「选刊推荐」细 ID 在正文写作桶而改归属。Catalog backups = MedSci / Scientific / AIPOCH / Nature only（ARS/OpenClaw purged）。

**专员对照（A 域不变）**

| 粗 ID | A 域 | 专员 |
|---|---|---|
| 文献检索 · 选题探索 · 研究设计 | `03_research` | Victor |
| 数据处理 · 统计分析 · 图表呈现 | `02_data-processing` · `04_analysis` | Loopnow |
| 正文写作 · 语言润色 | `05_manuscript` | Aitee（选刊交 Victor） |
| 稿件评阅 · 审稿回复 | `06_review` | Lee |

---

## 1. 文献检索（7）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 广度检索 | Scientific | `paper-lookup` | 🔵 |
| 引用真实性核验 | Scientific | `verify-refs` | 🟢（2026-09-13 换自B lit-cite） |
| 引用格式化写入 | Scientific | `manage-refs` | 🟢（同上，同目录） |
| 个人文献库同步 | Scientific | `lit-sync` | 🟢（同上，pyzotero） |
| 撤稿检测 | AIPOCH | `retraction-watcher` | 🟢（2026-09-13 promoted） |
| 严格他引审计 | Nature | `nature-academic-search` | 🔵（Apache-2.0 verified；仍需 ask-each-run / bytes） |
| 文献检索与公开数据集 | MedSci | `lit-search` | ✅ |

## 2. 选题探索（4）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 队列选题空白发现 | MedSci | `find-cohort-gap` | ✅ |
| MA选题可行性 | MedSci | `ma-scout` | ✅ |
| 假设形成 | MedSci | `frontier-hypothesize` | ✅ |
| 项目启动分类 | MedSci | `intake-project` | 🟡 |

## 3. 研究设计（6）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 研究设计审查 | MedSci | `design-study` | ✅ |
| AI专家评估设计 | MedSci | `design-ai-benchmarking` | 🟡 |
| 模型架构选型 | MedSci | `architecture-zoo` | 🟡 |
| IRB方案撰写 | MedSci | `write-protocol` | ✅ |
| IRB方案填表 | MedSci | `fill-protocol` | 🟡 |

## 4. 数据处理（6）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 三阶段确认式清洗 | MedSci | `clean-data` | ✅ |
| 批量队列分析生成 | MedSci | `batch-cohort` | ✅ |
| EDA | Scientific | `exploratory-data-analysis` | 🔵 |
| CT/MRI DICOM与NIfTI读写 | MedSci | `imaging-io` | ✅ |
| ROI与读者质控 | MedSci | `preprocess-imaging` | ✅ |
| DICOM底层与匿名化审计 | Scientific | `pydicom` | 🔵 |

## 5. 统计分析（8）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 检验方法选择与加权调查数据 | MedSci | `analyze-stats` | ✅ |
| Meta分析抗数据操纵 | MedSci | `meta-analysis` | ✅ |
| 生存分析leakage-safe管道 | Scientific | `scikit-survival` | 🔵 |
| 放射组学建模pipeline审计 | MedSci | `radiomics-ml` | ✅ |
| 模型-任务正确指标选择 | MedSci | `model-evaluation` | ✅ |
| 模型-确定性泄漏门禁 | MedSci | `model-validation` | ✅ |
| 样本量计算 | MedSci | `calc-sample-size` | ✅ |
| 样本量-复杂设计模拟法 | Scientific | `statistical-power` | 🔵 |

> 样本量归粗 ID「统计分析」（04 / Loopnow；CHG-20260926-004）。

## 6. 图表呈现（4）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 患者流程图 | MedSci | `make-figures` | ✅ |
| 统计图与影像面板 | MedSci | `fig-plot` | ✅ |
| 诚实可视化准则 | Scientific | `scientific-visualization` | 🟢（2026-09-14 REFERENCE→MOUNTED） |
| 审稿人风险预判 | Nature | `nature-figure` | 🟢（2026-09-14 REFERENCE→MOUNTED；Apache-2.0） |

## 7. 正文写作（7）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| IMRAD正文起草 | MedSci | `write-paper` | ✅ |
| 报告规范核验 | MedSci | `check-reporting` | ✅ |
| 数据可用性声明 | Nature | `nature-data` | 🔵 |
| 基金标书-中文语境QA | Nature | `nature-proposal-writer` | 🔵 |
| 基金标书-方法论 | MedSci | `grant-builder` | ✅ |
| 选刊推荐 | MedSci | `find-journal` | ✅（A 权威仍 `medical-journal-submit`） |
| 期刊格式模板 | Scientific | `venue-templates` | 🔵 |

## 8. 语言润色（3）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 一致性硬规则lint | MedSci | `polish-language` | ✅ |
| 去AI味 | MedSci | `humanize` | ✅（可仍走 MedSci 接口） |
| LaTeX排版细节 | Nature | `nature-polishing` | 🔵 |

## 9. 稿件评阅（5）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| PDF注入攻击扫描 | MedSci | `peer-review`（Phase1.5） | ✅ |
| 审稿意见生成 | MedSci | `peer-review` | ✅ |
| 数值级自审核算 | MedSci | `self-review` | ✅ |
| 证据质量评估 | Scientific | `scientific-critical-thinking` | 🔵 |
| 多审稿人隔离原则 | Nature | `nature-reviewer` | 🟢（2026-09-14 REFERENCE→MOUNTED；Apache-2.0） |

## 10. 审稿回复（3）

| 细ID | 来源包 | 原子技能 | 状态 |
|---|---|---|---|
| 修回分诊与数字血统追踪 | MedSci | `revise` | ✅ |
| 隔离与正文精简原则 | Nature | `nature-response` | 🟢（2026-09-14 REFERENCE→MOUNTED；Apache-2.0） |
| 回复语气软化 | AIPOCH | `response-tone-polisher` | 🟢（2026-09-13 promoted） |

---

**合计：** 注册表 **52** 细 ID。机器真源 [`../registry.yaml`](../registry.yaml)。旧 30 粗 ID 对照见 [MIGRATION_v3_to_v4.md](MIGRATION_v3_to_v4.md)。
