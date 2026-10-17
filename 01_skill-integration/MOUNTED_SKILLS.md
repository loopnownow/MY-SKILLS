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
**Pick menu:** status `MOUNTED` only, grouped by the 10 coarse buckets then by `load_priority`. `path_shared` siblings are consecutive rows. `PROPOSED` may be listed as optional candidates, separate from the pick menu.
Local bytes: `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) is a verified local cache, not a source of truth. Download ≠ mount ≠ active.
Say 默认挂载 B 包/本仓 — not 空挂.

Generator stamp from `registry.yaml` (do not copy this sentence into hand-written docs): **10 coarse buckets, 31 fine ids** (29 MOUNTED session-pick + 2 PROPOSED candidates + 0 reference-only). Personal layers stay in A `00`–`06`.
Machine source: `registry.yaml`. Human boards: [mounts/README.md](mounts/README.md).

## Session-pick fine ids (status MOUNTED only)


## P1 default (session menu) (26)


### lit-retrieval

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `verify-refs` | 引用真实性核验 | scientific-agent-skills | `skills/citation-management/` | MOUNTED | P1 | path_shared |
| `retraction-watcher` | 撤稿检测 | my-skills-capabilities | `03-research/retraction-watcher/` | MOUNTED | P1 | — |
| `lit-search` | 文献检索与公开数据集 | my-skills-capabilities | `03-research/lit-search/` | MOUNTED | P1 | — |


### study-design

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `design-study` | 研究设计审查 | my-skills-capabilities | `03-research/design-experiment/` | MOUNTED | P1 | — |
| `write-protocol` | IRB方案撰写 | my-skills-capabilities | `03-research/design-protocol/` | MOUNTED | P1 | — |


### manuscript-body

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `write-paper` | IMRAD正文起草 | my-skills-capabilities | `05-manuscript/write-manuscript/` | MOUNTED | P1 | — |
| `check-reporting` | 报告规范核验 | my-skills-capabilities | `05-manuscript/write-reporting/` | MOUNTED | P1 | — |
| `grant-builder` | 基金标书-方法论 | my-skills-capabilities | `03-research/design-grant/` | MOUNTED | P1 | — |
| `find-journal` | 选刊推荐 | my-skills-capabilities | `05-manuscript/write-venue/` | MOUNTED | P1 | — |


### language-polish

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `polish-language` | 一致性硬规则lint | my-skills-capabilities | `05-manuscript/write-polish/` | MOUNTED | P1 | — |
| `humanize` | 去AI味 | my-skills-capabilities | `05-manuscript/humanize/` | MOUNTED | P1 | — |


### data-processing

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `clean-data` | 三阶段确认式清洗 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED | P1 | — |
| `batch-cohort` | 批量队列分析生成 | my-skills-capabilities | `02-data-processing/tables/` | MOUNTED | P1 | path_shared |
| `imaging-io` | CT/MRI DICOM与NIfTI读写 | my-skills-capabilities | `02-data-processing/imaging-io/` | MOUNTED | P1 | — |
| `preprocess-imaging` | ROI与读者质控 | my-skills-capabilities | `02-data-processing/imaging-qc/` | MOUNTED | P1 | — |


### stats-analysis

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `analyze-stats` | 检验方法选择与加权调查数据 | my-skills-capabilities | `04-analysis/stats-guide/` | MOUNTED | P1 | — |
| `meta-analysis` | Meta分析抗数据操纵 | my-skills-capabilities | `04-analysis/stats-models/` | MOUNTED | P1 | — |
| `model-evaluation` | 模型-任务正确指标选择 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED | P1 | — |
| `model-validation` | 模型-确定性泄漏门禁 | my-skills-capabilities | `04-analysis/model-eval/` | MOUNTED | P1 | path_shared |
| `calc-sample-size` | 样本量计算 | my-skills-capabilities | `04-analysis/stats-power/` | MOUNTED | P1 | — |


### figures

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `draw-flowchart` | 患者流程图 | my-skills-capabilities | `04-analysis/fig-flow/` | MOUNTED | P1 | — |
| `plot-figures` | 统计图与影像面板 | my-skills-capabilities | `04-analysis/fig-plot/` | MOUNTED | P1 | — |


### manuscript-review

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `peer-review` | 审稿意见生成 | my-skills-capabilities | `06-review/review-peer/` | MOUNTED | P1 | path_shared |
| `self-review` | 数值级自审核算 | my-skills-capabilities | `06-review/review-critique/` | MOUNTED | P1 | — |
| `simulate-reviewers` | 多审稿人隔离原则 | nature-skills | `skills/nature-reviewer/` | MOUNTED · Apache-2.0 verified 2026-09-14 | P1 | — |


### review-response

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `revise` | 修回分诊与数字血统追踪 | my-skills-capabilities | `06-review/review-response/` | MOUNTED | P1 | — |


## P2 specialty (still pickable) (3)


### study-design

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `fill-protocol` | IRB方案填表 | my-skills-capabilities | `03-research/fill-protocol/` | MOUNTED | P2 | — |


### review-response

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `response-tone-polisher` | 回复语气软化 | my-skills-capabilities | `06-review/response-tone-polisher/` | MOUNTED | P2 | — |
| `tighten-response` | 隔离与正文精简原则 | nature-skills | `skills/nature-response/` | MOUNTED · Apache-2.0 verified 2026-09-14 | P2 | — |


## Optional candidates (status PROPOSED — not pickable)

Not a pick menu. List only. Promoting one to MOUNTED is a registry change, not a session pick.


### manuscript-body

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `check-grant-proposal` | 基金标书-中文语境QA | nature-skills | `skills/nature-proposal-writer/` | PROPOSED · Apache-2.0 verified 2026-09-14 | P2 | — |


### manuscript-review

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `scientific-critical-thinking` | 证据质量评估 | scientific-agent-skills | `skills/scientific-critical-thinking/` | PROPOSED | P2 | — |


## Reference-only (not session mounts)

| Id | Label | Applied to |
|---|---|---|
| — | — | — |

## Archived (not in default menus)

- `deidentify` — 导出已人工脱敏
- `profile-imaging` — 与 preprocess-imaging 共用 imaging-qc，没有单独正文
- `uncertainty-imaging` — 与 preprocess-imaging 共用 imaging-qc，没有单独正文
- `hypothesis-generation` — 未拉取字节；假设形成经 frontier-hypothesize 已并入 design-study（2026-10-17 round 2）
- `database-lookup` — 2026-09-20 候选，路径未核实，本地无字节
- `model-scaffold` — 2026-09-20 候选，路径未核实；训练脚手架与 0RAD 重叠
- `model-card` — 2026-09-20 候选，路径未核实；不代替 A 正文层
- `paperclip` — 2026-09-20 候选，路径未核实；全文提取与已归档的批量全文同类
- `paper-lookup` — PROPOSED never session-picked; overlaps lit-search; cut 2026-10-17 round 1
- `analyze-survival` — PROPOSED never session-picked; overlaps meta-analysis / analyze-stats; cut 2026-10-17 round 1
- `audit-citations` — PROPOSED never session-picked; overlaps verify-refs; cut 2026-10-17 round 1
- `audit-dicom` — PROPOSED never session-picked; overlaps imaging-io / preprocess-imaging; cut 2026-10-17 round 1
- `exploratory-data-analysis` — PROPOSED never session-picked; overlaps clean-data; cut 2026-10-17 round 1
- `polish-latex` — PROPOSED never session-picked; overlaps polish-language; cut 2026-10-17 round 1
- `statistical-power` — PROPOSED never session-picked; overlaps calc-sample-size; cut 2026-10-17 round 1
- `venue-templates` — PROPOSED never session-picked; overlaps find-journal; cut 2026-10-17 round 1
- `write-data-statement` — PROPOSED never session-picked; overlaps check-reporting / write-reporting; cut 2026-10-17 round 1
- `manage-refs` — path_shared with verify-refs; fold cite format/write into verify-refs; cut 2026-10-17 round 2
- `lit-sync` — Scientific P2; rarely used; Zotero sync optional; cut 2026-10-17 round 2
- `find-cohort-gap` — cohort topic-gap discovery folded into design-study; B folder 03-research/frontier-ideate/ kept; absorb 2026-10-17 round 2
- `scout-meta-analysis` — MA topic feasibility before MA folded into meta-analysis; B folder 03-research/lit-review/ kept; absorb 2026-10-17 round 2
- `frontier-hypothesize` — hypothesis formation folded into design-study; B folder 03-research/frontier-hypothesize/ kept; absorb 2026-10-17 round 2
- `intake-project` — project intake classification folded into design-study; B folder 03-research/intake-project/ kept; absorb 2026-10-17 round 2
- `design-ai-benchmarking` — AI expert-eval design folded into design-study; B folder 03-research/design-ai-benchmarking/ kept; absorb 2026-10-17 round 2
- `architecture-zoo` — model architecture selection folded into design-study; B folder 03-research/architecture-zoo/ kept as reference; absorb 2026-10-17 round 2
- `radiomics-ml` — radiomics pipeline audit invoked via analyze-stats / preprocess-imaging; B folder 02-data-processing/radiomics-habitat/ kept; absorb 2026-10-17 round 2
- `peer-review-pdf-scan` — same B path already path_shared with peer-review; PDF inject scan covered by peer-review; absorb 2026-10-17 round 2
- `scientific-visualization` — principles distilled into B plot-figures/external-principles.md; use plot-figures; cut 2026-10-17 round 2
- `audit-figure-risk` — Nature P2; principles already in B 04-analysis/fig-plot/external-principles.md; use plot-figures; cut 2026-10-17 round 2

## Package notes

- Non-B fine ids follow the registry status on each row (mixed PROPOSED/MOUNTED). Do not describe a whole package as uniformly PROPOSED.
- OpenClaw is not a default mount source (`ars_openclaw_policy: removed-from-catalog`).
- Nature LICENSE Apache-2.0 verified where the registry row says so.

Mapping is not a source-wide mount. `fine_id` is the capability interface; `path` is the physical unit; `path_shared` means one path backs several fine ids — do not split that folder.
