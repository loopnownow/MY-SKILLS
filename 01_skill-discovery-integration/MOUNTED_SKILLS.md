# Mounted Skills Boundary (v4)

Canonical pointers live in 01 (`registry.yaml`, the routing index). This file is the human table,
**generated** by `scripts/gen_mounted_skills.py` — do not hand-edit the tables below.
Default chassis: [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).
Non-B fine ids are mixed PROPOSED/MOUNTED per the registry rows below — not "all PROPOSED backups".
OpenClaw is not a default mount source.

Empty mount → notify → re-search → confirm. Never silently fall back.
Never auto-mount a non-B source. `PROPOSED` is not pickable. Nature LICENSE Apache-2.0 verified (ask when a new mount decision is required + bytes).
`ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick.
**Mount decision:** every independent run needs one. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01. A single-node personal-layer task with no mounted dependency does not ask.
**Pick menu:** status `MOUNTED` only. `PROPOSED` may be listed as optional candidates, separate from the pick menu.
Local bytes: `mounts-cap/` is a verified local cache, not a source of truth. Download ≠ mount ≠ active.
Say 默认挂载 B 包/本仓 — not 空挂.

Generator stamp from `registry.yaml` (do not copy this sentence into hand-written docs): **10 coarse buckets, 52 fine ids** (41 MOUNTED session-pick + 11 PROPOSED candidates + 0 reference-only). Personal layers stay in A `00`–`06`.
Machine source: `registry.yaml`. Human boards: [mounts/README.md](mounts/README.md).

## Session-pick fine ids (status MOUNTED only)


### 文献检索

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `verify-refs` | 引用真实性核验 | scientific-agent-skills | `skills/citation-management/` | MOUNTED |
| `manage-refs` | 引用格式化写入 | scientific-agent-skills | `skills/citation-management/` | MOUNTED |
| `lit-sync` | 个人文献库同步 | scientific-agent-skills | `skills/pyzotero/` | MOUNTED |
| `retraction-watcher` | 撤稿检测 | aipoch-medical-research-skills | `scientific-skills/Evidence Insight/retraction-watcher/` | MOUNTED |
| `lit-search` | 文献检索与公开数据集 | my-skills-capabilities | `03-research/lit-search/` | MOUNTED |


### 选题探索

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `find-cohort-gap` | 队列选题空白发现 | my-skills-capabilities | `03-research/frontier-ideate/` | MOUNTED |
| `ma-scout` | MA选题可行性 | my-skills-capabilities | `03-research/lit-review/` | MOUNTED |
| `frontier-hypothesize` | 假设形成 | my-skills-capabilities | `03-research/frontier-hypothesize/` | MOUNTED |
| `intake-project` | 项目启动分类 | my-skills-capabilities | `03-research/intake-project/` | MOUNTED |


### 研究设计

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `design-study` | 研究设计审查 | my-skills-capabilities | `03-research/design-experiment/` | MOUNTED |
| `design-ai-benchmarking` | AI专家评估设计 | my-skills-capabilities | `03-research/design-ai-benchmarking/` | MOUNTED |
| `architecture-zoo` | 模型架构选型 | my-skills-capabilities | `03-research/architecture-zoo/` | MOUNTED |
| `write-protocol` | IRB方案撰写 | my-skills-capabilities | `03-research/design-protocol/` | MOUNTED |
| `fill-protocol` | IRB方案填表 | my-skills-capabilities | `03-research/fill-protocol/` | MOUNTED |


### 正文写作

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `write-paper` | IMRAD正文起草 | my-skills-capabilities | `05-manuscript/write-manuscript/` | MOUNTED |
| `check-reporting` | 报告规范核验 | my-skills-capabilities | `05-manuscript/write-reporting/` | MOUNTED |
| `grant-builder` | 基金标书-方法论 | my-skills-capabilities | `03-research/design-grant/` | MOUNTED |
| `find-journal` | 选刊推荐 | my-skills-capabilities | `05-manuscript/write-venue/` | MOUNTED |


### 语言润色

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `polish-language` | 一致性硬规则lint | my-skills-capabilities | `05-manuscript/write-polish/` | MOUNTED |
| `humanize` | 去AI味 | med-sci-skills | `skills/humanize/` | MOUNTED |


### 数据处理

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `clean-data` | 三阶段确认式清洗 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED |
| `batch-cohort` | 批量队列分析生成 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED |
| `imaging-io` | CT/MRI DICOM与NIfTI读写 | my-skills-capabilities | `02-data-processing/imaging-io/` | MOUNTED |
| `preprocess-imaging` | ROI与读者质控 | my-skills-capabilities | `02-data-processing/imaging-qc/` | MOUNTED |


### 统计分析

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `analyze-stats` | 检验方法选择与加权调查数据 | my-skills-capabilities | `04-analysis/stats-guide/` | MOUNTED |
| `meta-analysis` | Meta分析抗数据操纵 | my-skills-capabilities | `04-analysis/stats-models/` | MOUNTED |
| `radiomics-ml` | 放射组学建模pipeline审计 | my-skills-capabilities | `02-data-processing/radiomics-habitat/` | MOUNTED |
| `model-evaluation` | 模型-任务正确指标选择 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED |
| `model-validation` | 模型-确定性泄漏门禁 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED |
| `calc-sample-size` | 样本量计算 | my-skills-capabilities | `04-analysis/stats-power/` | MOUNTED |


### 图表呈现

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `make-figures` | 患者流程图 | my-skills-capabilities | `04-analysis/fig-flow/` | MOUNTED |
| `fig-plot` | 统计图与影像面板 | my-skills-capabilities | `04-analysis/fig-plot/` | MOUNTED |
| `scientific-visualization` | 诚实可视化准则 | scientific-agent-skills | `skills/scientific-visualization/` | MOUNTED |
| `nature-figure` | 审稿人风险预判 | nature-skills | `skills/nature-figure/` | MOUNTED · Apache-2.0 verified 2026-09-14 |


### 稿件评阅

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `peer-review-pdf-scan` | PDF注入攻击扫描 | my-skills-capabilities | `06-review/review-peer/` | MOUNTED |
| `peer-review` | 审稿意见生成 | my-skills-capabilities | `06-review/review-peer/` | MOUNTED |
| `self-review` | 数值级自审核算 | my-skills-capabilities | `06-review/review-critique/` | MOUNTED |
| `nature-reviewer` | 多审稿人隔离原则 | nature-skills | `skills/nature-reviewer/` | MOUNTED · Apache-2.0 verified 2026-09-14 |


### 审稿回复

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `revise` | 修回分诊与数字血统追踪 | my-skills-capabilities | `06-review/review-response/` | MOUNTED |
| `response-tone-polisher` | 回复语气软化 | aipoch-medical-research-skills | `scientific-skills/Academic Writing/response-tone-polisher/` | MOUNTED |
| `nature-response` | 隔离与正文精简原则 | nature-skills | `skills/nature-response/` | MOUNTED · Apache-2.0 verified 2026-09-14 |


## Optional candidates (status PROPOSED — not pickable)

Not a pick menu. List only. Promoting one to MOUNTED is a registry change, not a session pick.


### 文献检索

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `paper-lookup` | 广度检索 | scientific-agent-skills | `skills/paper-lookup/` | PROPOSED |
| `nature-academic-search` | 严格他引审计 | nature-skills | `skills/nature-academic-search/` | PROPOSED · Apache-2.0 verified 2026-09-14 |


### 正文写作

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `nature-data` | 数据可用性声明 | nature-skills | `skills/nature-data/` | PROPOSED · Apache-2.0 verified 2026-09-14 |
| `nature-proposal-writer` | 基金标书-中文语境QA | nature-skills | `skills/nature-proposal-writer/` | PROPOSED · Apache-2.0 verified 2026-09-14 |
| `venue-templates` | 期刊格式模板 | scientific-agent-skills | `skills/venue-templates/` | PROPOSED |


### 语言润色

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `nature-polishing` | LaTeX排版细节 | nature-skills | `skills/nature-polishing/` | PROPOSED · Apache-2.0 verified 2026-09-14 |


### 数据处理

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `exploratory-data-analysis` | EDA | scientific-agent-skills | `skills/exploratory-data-analysis/` | PROPOSED |
| `pydicom` | DICOM底层与匿名化审计 | scientific-agent-skills | `skills/pydicom/` | PROPOSED |


### 统计分析

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `scikit-survival` | 生存分析leakage-safe管道 | scientific-agent-skills | `skills/scikit-survival/` | PROPOSED |
| `statistical-power` | 样本量-复杂设计模拟法 | scientific-agent-skills | `skills/statistical-power/` | PROPOSED |


### 稿件评阅

| Fine id | Label | Source | Path | Status |
|---|---|---|---|---|
| `scientific-critical-thinking` | 证据质量评估 | scientific-agent-skills | `skills/scientific-critical-thinking/` | PROPOSED |


## Reference-only (not session mounts)

| Id | Label | Applied to |
|---|---|---|
| — | — | — |

## Archived (not in default menus)

- `deidentify` — 导出已人工脱敏
- `profile-imaging` — 与 preprocess-imaging 共用 imaging-qc，没有单独正文
- `uncertainty-imaging` — 与 preprocess-imaging 共用 imaging-qc，没有单独正文
- `hypothesis-generation` — 未拉取字节；假设形成用已挂载的 frontier-hypothesize
- `database-lookup` — 2026-09-20 候选，路径未核实，本地无字节
- `model-scaffold` — 2026-09-20 候选，路径未核实；训练脚手架与 0RAD 重叠
- `model-card` — 2026-09-20 候选，路径未核实；不代替 A 正文层
- `paperclip` — 2026-09-20 候选，路径未核实；全文提取与已归档的批量全文同类

## Package notes

- Non-B fine ids follow the registry status on each row (mixed PROPOSED/MOUNTED). Do not describe a whole package as uniformly PROPOSED.
- OpenClaw is not a default mount source (`ars_openclaw_policy: removed-from-catalog`).
- Nature LICENSE Apache-2.0 verified where the registry row says so.

Mapping is not a source-wide mount. `fine_id` is the capability interface; `path` is the physical unit; `path_shared` means one path backs several fine ids — do not split that folder.
