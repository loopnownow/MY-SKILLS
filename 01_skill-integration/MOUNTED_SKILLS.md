# Mounted Skills Boundary (v4)

Canonical pointers live in 01 skill-index (`registry.yaml`, the routing index). This file is the human table,
**generated** by `scripts/gen_mounted_skills.py` — do not hand-edit the tables below.
Default UNIQUE runtime source: in-repo `my-skills` (`NN_slug/base/`).
Non-base sources = default deny. OpenClaw/ARS not in catalog.

Empty mount → notify → re-search → confirm. Never silently fall back.
Never auto-mount a non-base source. `PROPOSED` is not pickable.
`ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick.
**Mount decision:** every independent run needs one. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01. A single-node personal-layer / A top-layer task with no mounted dependency does not ask.
**Pick menu:** status `MOUNTED` only, grouped by the 10 coarse buckets then by `load_priority`. `path_shared` siblings are consecutive rows. `PROPOSED` may be listed as optional candidates, separate from the pick menu.
Bodies live in-repo under `NN_slug/base/`. Former `{mounts_cap}/b/` B cache is obsolete for live mounts.
Say default mount = in-repo base/ -- not empty mount.

Generator stamp from `registry.yaml` (do not copy this sentence into hand-written docs): **10 coarse buckets, 28 fine ids** (28 MOUNTED session-pick + 0 PROPOSED candidates + 0 reference-only). Personal / A top layers stay in A `00`–`07` (not capability mounts).
Machine source: `registry.yaml`. Non-base deny: [references/hybrid-mount-pointers.md](references/hybrid-mount-pointers.md). Presets: [references/presets/](references/presets/).

## Session-pick fine ids (status MOUNTED only)


## P1 default (session menu) (25)


### lit-retrieval

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `verify-refs` | 引用真实性核验 | my-skills | `03_research/base/verify-refs/` | MOUNTED | P1 | — |
| `retraction-watcher` | 撤稿检测 | my-skills | `03_research/base/retraction-watcher/` | MOUNTED | P1 | — |
| `lit-search` | 文献检索与公开数据集 | my-skills | `03_research/base/lit-search/` | MOUNTED | P1 | — |


### study-design

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `design-study` | 研究设计审查 | my-skills | `03_research/base/design-experiment/` | MOUNTED | P1 | — |
| `write-protocol` | IRB方案撰写 | my-skills | `03_research/base/design-protocol/` | MOUNTED | P1 | — |


### manuscript-body

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `write-paper` | IMRAD正文起草 | my-skills | `05_manuscript/base/write-manuscript/` | MOUNTED | P1 | — |
| `check-reporting` | 报告规范核验 | my-skills | `05_manuscript/base/write-reporting/` | MOUNTED | P1 | — |
| `grant-builder` | 基金标书-方法论 | my-skills | `03_research/base/design-grant/` | MOUNTED | P1 | — |
| `find-journal` | 选刊推荐 | my-skills | `03_research/base/find-journal/` | MOUNTED | P1 | — |


### language-polish

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `polish-language` | 一致性硬规则lint | my-skills | `05_manuscript/base/write-polish/` | MOUNTED | P1 | — |
| `humanize` | 去AI味 | my-skills | `05_manuscript/base/humanize/` | MOUNTED | P1 | — |


### data-processing

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `clean-data` | 三阶段确认式清洗 | my-skills | `02_data-processing/base/tables/` | MOUNTED | P1 | — |
| `batch-cohort` | 批量队列分析生成 | my-skills | `02_data-processing/base/tables/` | MOUNTED | P1 | path_shared |
| `imaging-io` | CT/MRI DICOM与NIfTI读写 | my-skills | `02_data-processing/base/imaging-io/` | MOUNTED | P1 | — |
| `preprocess-imaging` | ROI与读者质控 | my-skills | `02_data-processing/base/imaging-qc/` | MOUNTED | P1 | — |


### stats-analysis

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `analyze-stats` | 检验方法选择与加权调查数据 | my-skills | `04_analysis/base/stats-guide/` | MOUNTED | P1 | — |
| `meta-analysis` | Meta分析抗数据操纵 | my-skills | `04_analysis/base/stats-models/` | MOUNTED | P1 | — |
| `model-evaluation` | 模型-任务正确指标选择 | my-skills | `04_analysis/base/model-eval/` | MOUNTED | P1 | — |
| `calc-sample-size` | 样本量计算 | my-skills | `04_analysis/base/stats-power/` | MOUNTED | P1 | — |


### figures

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `draw-flowchart` | 患者流程图 | my-skills | `04_analysis/base/fig-flow/` | MOUNTED | P1 | — |
| `plot-figures` | 统计图与影像面板 | my-skills | `04_analysis/base/fig-plot/` | MOUNTED | P1 | — |


### manuscript-review

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `peer-review` | 审稿意见生成 | my-skills | `06_review/base/review-peer/` | MOUNTED | P1 | path_shared |
| `self-review` | 数值级自审核算 | my-skills | `06_review/base/review-critique/` | MOUNTED | P1 | — |
| `simulate-reviewers` | 多审稿人隔离原则 | my-skills | `06_review/base/simulate-reviewers/` | MOUNTED | P1 | — |


### review-response

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `revise` | 修回分诊与数字血统追踪 | my-skills | `07_response/base/review-response/` | MOUNTED | P1 | — |


## P2 specialty (still pickable) (3)


### study-design

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `fill-protocol` | IRB方案填表 | my-skills | `03_research/base/fill-protocol/` | MOUNTED | P2 | — |


### review-response

| Fine id | Label | Source | Path | Status | Priority | Shared |
|---|---|---|---|---|---|---|
| `response-tone-polisher` | 回复语气软化 | my-skills | `07_response/base/response-tone-polisher/` | MOUNTED | P2 | — |
| `tighten-response` | 隔离与正文精简原则 | my-skills | `07_response/base/tighten-response/` | MOUNTED | P2 | — |


## Optional candidates (status PROPOSED — not pickable)

Not a pick menu. List only. Promoting one to MOUNTED is a registry change, not a session pick.


None.


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
- `check-grant-proposal` — PROPOSED never session-picked; overlaps grant-builder; cut 2026-10-17 round 3
- `model-validation` — deterministic leakage gates folded into model-evaluation; same B path 04-analysis/model-eval/; absorb 2026-10-17 round 3
- `scientific-critical-thinking` — PROPOSED never session-picked; overlaps self-review / peer-review; cut 2026-10-17 round 3

## Source notes

- Default unique runtime source = `my-skills` (in-repo). Non-base = default deny.
- OpenClaw/ARS: `ars_openclaw_policy: removed-from-catalog`.
- A top layers are not capability mounts (00 owns base→QC→A).

Mapping is not a source-wide mount. `fine_id` is the capability interface; `path` is the physical unit; `path_shared` means one path backs several fine ids — do not split that folder.
