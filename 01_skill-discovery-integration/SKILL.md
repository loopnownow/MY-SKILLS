---
name: skill-discovery-integration
description: >
  Discover, evaluate, and mount external Skills. Use for finding a new Skill,
  checking mounted capability coverage, integrating an approved external Skill,
  or resolving missing capability. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Mount pointers live only here.
  Default mount is B (MY-SKILLS-capabilities). Every run: ask which fine ids to
  mount this session under relevant coarse buckets. Never auto-mount a non-B source.
  OpenClaw is never an atomic mount source.
---

# Skill Discovery & Integration

## Purpose

Infrastructure for Skill discovery and mounting. Professional work stays in 02–06.
This layer only resolves **where a capability comes from**.
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`.
Human board: `mounts/` (`README.md`, `MIGRATION_v3_to_v4.md`, `hybrid-mount-pointers.md`, `presets.md` + `presets/*.yaml`, `b.md` / `ars.md` / `medsci.md` / `scientific.md` / `openclaw.md` / `aipoch.md` / `nature.md`).
Domain skills call fine ids; they do not keep a second pointer table.

## Architecture (v4 · CHG-20260913-001)

- **10 coarse ids** = welded stage buckets（文献检索 … 审稿回复）. Not A folder renames.
- **51 fine ids** = session-pick mount points (51 mounts; reference_only emptied).
- **Hybrid mount:** different fine ids may use different packages; never mix packages inside one fine id.
- A domains stay `00_orchestrator` … `06_review` (+ skill-harvest). Personal layers stay in A.
- 选刊 stays Victor / `03_research/medical-journal-submit` — do not move into 05.
- Backup of 30-id registry: `_history/registry.v3.30.yaml`.

## Default mount

**Default session recipe (review / pre-review):** `review-hybrid-default` in `mounts/presets.md` (machine core `mounts/presets/review-hybrid.yaml`) — B chassis, Nature fine-id overlays (license 需核实), Scientific critique fine id. Still ask each run; user may change picks. Attribution and fetch are **per pack skill** (see preset `skills:`), not whole source. ARS and OpenClaw are not in the default recipe.

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
ARS, MedSci, Scientific, AIPOCH, Nature are **backup candidates** (PROPOSED). OpenClaw is **license-risk-reference-only** — never atomic source.
Nature fine ids stay PROPOSED until license verified; do not claim MOUNTED if bytes absent.

**Mapping is not a mount.** Status stays `PROPOSED` until the user confirms.

## Local cache (`mounts-cap/`)

Bytes live at repo-root `mounts-cap/` (gitignored pack trees). Pointers stay in this skill.

- **B** (`mounts-cap/b/`): **canonical** full tree. Missing → `python mounts-cap/fetch.py ensure-b`.
- **ARS / MedSci / Scientific / AIPOCH / Nature**: download **only the path(s) of fine ids picked this run**. Never clone wholesale. OpenClaw: do not fetch for mount.
- `python mounts-cap/fetch.py ensure --id <fine-id>` after the session pick. Download is not a mount. Empty after fetch → empty-mount protocol.

## Session mount pick（每次运行必问 · 细 ID 多选）

Registry `MOUNTED` / `PROPOSED` = **available to pick**, not attached for this run.
**Every MY-SKILLS run** (00 composite or a single 02–06 skill) must ask before loading any mounted pack.

1. Classify the task. Propose **relevant coarse bucket(s)** then **candidate fine ids** (not all 51 unless 全线).
2. Show each candidate as one line: **粗 ID · 细 ID · 源 · 包内 skill** · 做什么。默认源多为 B。审稿混合配方行必须写出 skill 名（如 `nature-ref-verifier`）。
3. **Ask the user to multi-select fine ids**. For 预审/审稿/回复审稿, **pre-check `review-hybrid-default`** then allow edits. Also offer: 用审稿混合默认配方 / 候选全用 B / 只要个人层不外挂 / 换源（MedSci / Scientific / AIPOCH / Nature，仅当该细 ID 有路径；**OpenClaw 不提供**；ARS 默认不提供）.
4. Load **only** the picked fine ids (and for non-B overrides, **only the preset/skill paths** listed). Ensure bytes in `mounts-cap/` first. Unpicked stay unloaded — do not prefetch a whole Nature/Scientific tree. Never bulk-download.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run picked a backup source.

Silence is not approval. Never auto-mount a non-B source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) are not mount picks.
Say **默认挂载 B 包/本仓**, not 空挂.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to ARS/MedSci/Scientific/OpenClaw/AIPOCH/Nature or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (coarse buckets + fine `mounts:`).
2. Resolve each fine id against its `source`. Default source is B. `humanize` mounts from MedSci. Archived ids are not in the default menu (includes former `04-explainability`).
3. If that path is empty or missing → empty-mount protocol.
4. Only after confirmation may a *different* backup candidate be proposed.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. New non-B sources stay `PROPOSED` until explicit approval. Nature needs license confirmation.
7. After approval: `APPROVED` → `MOUNTED`. Update `registry.yaml` and `MOUNTED_SKILLS.md`.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a **non-B** Skill.
- Never bulk-download ARS / MedSci / Scientific / OpenClaw / AIPOCH / Nature. On-demand paths only, after a pick.
- **Never mount OpenClaw** as an atomic skill source.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `humanize` (MedSci). The personal forbidden list still wins.

## GitHub discovery workflow（自动搜索 → 比较 → 出建议 → grilling 确认）

Triggered by 00's "new capability" routing, or a direct ask to find/evaluate an external Skill.
**01 searches and recommends; it never writes `registry.yaml` / `sources/*.yaml` / `personal/`
without a confirmed grilling round.** This is not 00's QC decision either — 00 only routes here.

1. **搜索**：`web_search`（关键词取自任务领域 + "claude skill" / "agent skill" / "skill.md"）+
   GitHub 搜索，取 3–6 个候选，不止评估一个仓库就下结论。
2. **拉取**：对每个候选 `git clone --depth 1`，读 `SKILL.md` / `README` / `LICENSE`。不做超出候选数量的批量克隆。
3. **决策清单**（按顺序过，任一步不通过就在该步停止，不继续评估后续维度）：
   - **a. License 硬门槛** — 必须是允许衍生作品和再分发的宽松协议（MIT/Apache-2.0/BSD/CC-BY 等）。
     缺失协议，或含"仅限个人非商业 / 禁止二次开发 / 禁止再分发"字样 → 标记**不可挂载、不可吸收**。
     "只取一部分内容/只改几处"不改变这个判定——衍生作品的性质不因取用比例变化（先例：
     vivid-figures-skill，见 `_medical-research-meta/INTEGRATION_MAP.md` CHG-20260913-003）。
   - **b. 领域对口** — 内容是否落在现有10个粗ID/6个A域实际需求范围内；域外内容（如通用软件
     工程技能）默认不纳入，除非用户明确提出具体需求（先例：mattpocock/skills 的多数技能未纳入，
     只有 grilling 一项经用户确认后吸收，见 CHG-20260913-003）。
   - **c. 重叠检查** — 和已挂载细ID、`personal/` 现有文件比对内容重合度。已被覆盖 ≥ 约80% 的
     候选标记**低边际价值**，不建议整体挂载或吸收，只挑真正缺的部分（先例：no-ai-slop 21/23
     禁用词已在 `ai-isms-checklist.md`，且其"强制主动语态"规则与既有 Methods 段落被动语态例外
     冲突，整体跳过）。
   - **d. 颗粒度** — 候选能否干净对应一个细ID（一细ID=一来源包，不跨包混装）；体量过大过杂
     （整个软件产品、需要额外运行时）优先原生轻量方案，不为单一需求引入重依赖（先例：archify
     的 Node.js 工具链，改用手写 SVG 加进 `00_orchestrator/scripts/gen_repo_map.py`）。
4. **输出建议表**（不直接执行）：每个候选一行——`仓库 | License状态 | 建议动作(挂载/吸收/跳过) |
   目标(粗ID·细ID 或 personal/文件) | 理由`。
5. **移交 grilling 确认**：把建议表包成一轮 `grill-me`（`00_orchestrator/grilling/SKILL.md`），
   每条建议是一道题、附带推荐动作，等用户逐条确认或改。**这一步之前不写任何文件。**
6. 用户确认后才执行：
   - **挂载** → 按现有 `sources/<name>.proposed.yaml` schema 建档（参考 `sources/ars.proposed.yaml`
     的字段结构），状态 `PROPOSED`，走既定 lifecycle（见「Registry」一节）升到 `APPROVED`/`MOUNTED`。
   - **吸收** → 由对应 `0X_domain` 用自己的语言重写关键内容到 `personal/`，不整体挂载来源，
     不建 `sources/*.yaml`。
   - **跳过** → 不留痕迹；如果候选未来可能复用，可选择记一行到 `mounts/README.md`。

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle index (canonical). `sources/<source>.yaml` = one config per external source. `mounts/*.md` = human interface board. `interface.yaml` = capability-contract template.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` / `ARCHIVED` / `REJECTED`.
**Layout rule:** one external source → one yaml. Fine ids are the mount points; coarse ids are stage buckets only.
