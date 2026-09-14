# Mounted Skills Boundary (v4)

Canonical pointers live in 01 (`registry.yaml`). This file is the human table,
**generated** by `scripts/gen_mounted_skills.py` — do not hand-edit the tables below.
Default source: [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify → re-search → confirm. Never silently fall back.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`. Nature: `license_flag` until verified.
**OpenClaw is never an atomic mount source** (license risk).
**Every run:** ask which **fine ids** to attach under the relevant coarse buckets (`session_mount: ask-each-run`).
Local bytes: `mounts-cap/` (B full; other sources on-demand). Download ≠ mount.
Say 默认挂载 B 包/本仓 — not 空挂.

v4: **10 coarse + 52 fine** (48 session-pick mounts + 4 reference-only). Personal layers stay in A `00`–`06`.
Migration: [mounts/MIGRATION_v3_to_v4.md](mounts/MIGRATION_v3_to_v4.md). Backup: `_history/registry.v3.30.yaml`.

## Session-pick fine ids by coarse bucket


### 文献检索

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `paper-lookup` | 广度检索 | scientific-agent-skills | `skills/paper-lookup/` | PROPOSED |
| `verify-refs` | 引用真实性核验 | my-skills-capabilities | `03-research/lit-cite/` | MOUNTED |
| `manage-refs` | 引用格式化写入 | my-skills-capabilities | `03-research/lit-cite/` | MOUNTED |
| `lit-sync` | 个人文献库同步 | my-skills-capabilities | `03-research/lit-cite/` | MOUNTED |
| `retraction-watcher` | 撤稿检测 | aipoch-medical-research-skills | `skills/retraction-watcher/` | PROPOSED |
| `nature-academic-search` | 严格他引审计 | nature-skills | `skills/nature-academic-search/` | PROPOSED · 需核实 |


### 选题探索

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `find-cohort-gap` | 队列选题空白发现 | my-skills-capabilities | `03-research/frontier-ideate/` | MOUNTED |
| `ma-scout` | MA选题可行性 | my-skills-capabilities | `03-research/lit-review/` | MOUNTED |
| `hypothesis-generation` | 假设形成防HARKing | scientific-agent-skills | `skills/hypothesis-generation/` | PROPOSED |
| `intake-project` | 项目启动分类 | my-skills-capabilities | `03-research/intake-project/` | MOUNTED |


### 研究设计

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `design-study` | 研究设计审查 | my-skills-capabilities | `03-research/design-experiment/` | MOUNTED |
| `design-ai-benchmarking` | AI专家评估设计 | my-skills-capabilities | `03-research/design-ai-benchmarking/` | MOUNTED |
| `architecture-zoo` | 模型架构选型 | my-skills-capabilities | `03-research/architecture-zoo/` | MOUNTED |
| `write-protocol` | IRB方案撰写 | my-skills-capabilities | `03-research/design-protocol/` | MOUNTED |
| `fill-protocol` | IRB方案填表 | my-skills-capabilities | `03-research/fill-protocol/` | MOUNTED |
| `clinic-research-design` | 方案-按研究类型模板 | aipoch-medical-research-skills | `skills/clinic-research-design/` | PROPOSED |
| `calc-sample-size` | 样本量计算 | my-skills-capabilities | `04-analysis/stats-power/` | MOUNTED |
| `statistical-power` | 样本量-复杂设计模拟法 | scientific-agent-skills | `skills/statistical-power/` | PROPOSED |


### 正文写作

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `write-paper` | IMRAD正文起草 | my-skills-capabilities | `05-manuscript/write-manuscript/` | MOUNTED |
| `check-reporting` | 报告规范核验 | my-skills-capabilities | `05-manuscript/write-reporting/` | MOUNTED |
| `nature-data` | 数据可用性声明 | nature-skills | `skills/nature-data/` | PROPOSED · 需核实 |
| `nature-proposal-writer` | 基金标书-中文语境QA | nature-skills | `skills/nature-proposal-writer/` | PROPOSED · 需核实 |
| `grant-builder` | 基金标书-方法论 | my-skills-capabilities | `03-research/design-grant/` | MOUNTED |
| `find-journal` | 选刊推荐 | my-skills-capabilities | `05-manuscript/write-venue/` | MOUNTED |
| `venue-templates` | 期刊格式模板 | scientific-agent-skills | `skills/venue-templates/` | PROPOSED |


### 语言润色

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `polish-language` | 一致性硬规则lint | my-skills-capabilities | `05-manuscript/write-polish/` | MOUNTED |
| `humanize` | 去AI味 | med-sci-skills | `skills/humanize/` | MOUNTED |
| `nature-polishing` | LaTeX排版细节 | nature-skills | `skills/nature-polishing/` | PROPOSED · 需核实 |


### 数据处理

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `clean-data` | 三阶段确认式清洗 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED |
| `batch-cohort` | 批量队列分析生成 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED |
| `exploratory-data-analysis` | EDA | scientific-agent-skills | `skills/exploratory-data-analysis/` | PROPOSED |
| `preprocess-imaging` | 预处理设计与泄漏门禁 | my-skills-capabilities | `02-data-processing/imaging-qc/` | MOUNTED |
| `pydicom` | DICOM底层与匿名化审计 | scientific-agent-skills | `skills/pydicom/` | PROPOSED |
| `profile-imaging` | 训练前数据集画像 | my-skills-capabilities | `02-data-processing/imaging-qc/` | MOUNTED |
| `uncertainty-imaging` | 部署级不确定性量化 | my-skills-capabilities | `02-data-processing/imaging-qc/` | MOUNTED |


### 统计分析

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `analyze-stats` | 检验方法选择与加权调查数据 | my-skills-capabilities | `04-analysis/stats-guide/` | MOUNTED |
| `meta-analysis` | Meta分析抗数据操纵 | my-skills-capabilities | `04-analysis/stats-models/` | MOUNTED |
| `scikit-survival` | 生存分析leakage-safe管道 | scientific-agent-skills | `skills/scikit-survival/` | PROPOSED |
| `radiomics-ml` | 放射组学建模pipeline审计 | my-skills-capabilities | `02-data-processing/radiomics-habitat/` | MOUNTED |
| `model-evaluation` | 模型-任务正确指标选择 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED |
| `model-validation` | 模型-确定性泄漏门禁 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED |


### 图表呈现

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `make-figures` | 报告规范流程图与期刊配图 | my-skills-capabilities | `04-analysis/fig-flow/` | MOUNTED |


### 稿件评阅

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `peer-review-pdf-scan` | PDF注入攻击扫描 | my-skills-capabilities | `06-review/review-peer/` | MOUNTED |
| `peer-review` | 审稿意见生成 | my-skills-capabilities | `06-review/review-peer/` | MOUNTED |
| `self-review` | 数值级自审核算 | my-skills-capabilities | `06-review/review-critique/` | MOUNTED |
| `scientific-critical-thinking` | 证据质量评估 | scientific-agent-skills | `skills/scientific-critical-thinking/` | PROPOSED |


### 审稿回复

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `revise` | 修回分诊与数字血统追踪 | my-skills-capabilities | `06-review/review-response/` | MOUNTED |
| `response-tone-polisher` | 回复语气软化 | aipoch-medical-research-skills | `skills/response-tone-polisher/` | PROPOSED |


## Reference-only (not session mounts)

| Id | Label | Applied to |
|---|---|---|
| `scientific-visualization` | 诚实可视化准则 | `04-analysis/fig-plot/external-principles.md` |
| `nature-figure` | 审稿人风险预判 | `04-analysis/fig-plot/external-principles.md` |
| `nature-reviewer` | 多审稿人隔离原则 | `06-review/review-peer/external-principles.md` |
| `nature-response` | 隔离与正文精简原则 | `06-review/review-response/external-principles.md` |

## Archived (not in default menus)

- `02-fmri` — 假匹配已核实——AIPOCH neuropixels≠fMRI
- `02-pictures` — 场景错位——病理全切片非通用图片
- `03-design-experiment-wetlab` — 仅归档外部湿实验室DOE；MedSci design-study等已入研究设计
- `04-explainability` — 用户不使用；Grad-CAM vs SHAP不可互替
- `03-lit-fulltext` — 用户不使用批量全文
- `03-lit-review-full` — 不写综述全流程；ma-scout保留在选题探索
- `deidentify` — 导出已人工脱敏
- `05-write-venue-add-journal` — add-journal是维护工具非产出技能

## Backup candidates

- ARS / MedSci / Scientific / AIPOCH / Nature: `PROPOSED` (Nature license 需核实).
- OpenClaw: `PROPOSED` · **license-risk-reference-only** · never mount as atomic source.

Mapping is not a source-wide mount.
