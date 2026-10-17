# 混合挂载指针说明（配方叙事 · 例外）

[总览](README.md) · [registry.yaml](../registry.yaml) · [MOUNTED_SKILLS.md](../MOUNTED_SKILLS.md)

**用途：** 会话点选时的「细 ID → 来源包 → 原子技能」配方叙事与例外说明。粗 ID 是阶段桶（焊死 10 个）；细 ID 才是挂载点。同一细 ID 内不混包；不同细 ID 可来自不同包（混合挂载）。

**细 ID 状态与包路径以 [`../registry.yaml`](../registry.yaml) 为准；会话菜单见 [`../MOUNTED_SKILLS.md`](../MOUNTED_SKILLS.md)（生成）。本文件只保留配方叙事与例外。**

**图例**

| 标记 | 含义 |
|---|---|
| ✅ B默认已含 | 原子技能已在 `MY-SKILLS-capabilities`（本仓 B） |
| 🟡 新增挂载 | 审计补进 B 的 MedSci 本体（见 capabilities PR） |
| 🔵 跨包补充 | Scientific / AIPOCH / Nature 等；多为 PROPOSED，启用前确认 |
| 🟢 跨包已挂载 | 跨包来源，已从 PROPOSED confirm 为 MOUNTED（非 B 默认，仍需按细 ID 单独按需拉取） |
| ⚪ 规则参考 | 不挂载字节；原则写入对应 B 技能的 `external-principles.md`（2026-09-14：原四条已升 🟢，本表无残留 ⚪） |

**硬规则：** Nature LICENSE 已核实为 Apache-2.0（2026-09-14）；正式 `MOUNTED` 仍须 ask-each-run 细 ID 多选 + `{mounts_cap}/` 字节到位，不因许可证已核实而自动挂载。选刊决策权威仍在 A `03_research/find-journal`（Victor），不因「选刊推荐」细 ID 在正文写作桶而改归属。Catalog backups = MedSci / Scientific / AIPOCH / Nature only（ARS/OpenClaw purged）。

**专员对照（A 域不变）**

| 粗 ID | A 域 | 专员 |
|---|---|---|
| lit-retrieval · topic-explore · study-design | `03_research` | Victor |
| data-processing · stats-analysis · figures | `02_data-processing` · `04_analysis` | Loopnow |
| manuscript-body · language-polish | `05_manuscript` | Aitee（选刊交 Victor） |
| manuscript-review · review-response | `06_review` | Lee |

## 配方叙事与例外（非全表）

机器真源与全量细 ID 表不在此重复。保留下列独有笔记：

- **lit-cite 换源（CHG-20260913）→ round 2：** `verify-refs` 仍 Scientific citation-management；`manage-refs`/`lit-sync` 已 ARCHIVED（2026-10-17 round 2；manage-refs 并入 verify-refs）。
- **AIPOCH promote（2026-09-13）：** `retraction-watcher`、`response-tone-polisher` 曾升 🟢；`clinic-research-design` 已拒绝。
- **AIPOCH absorb into B（2026-10-17）：** 上述两细 ID 改挂 `my-skills-capabilities` domain paths；`cross-pack/aipoch/` stubs 删除。
- **Nature / Scientific（2026-10-17 round 2）：** `simulate-reviewers`、`tighten-response` 仍 MOUNTED；`scientific-visualization`/`audit-figure-risk` 已 ARCHIVED→`plot-figures`（原则在 B fig-plot/external-principles.md）。
- **样本量归属（CHG-20260926-004）：** 样本量归粗 ID「统计分析」（04 / Loopnow），不在正文写作桶。
- **选刊权威：** `find-journal` 细 ID 可在 manuscript-body 桶展示，A 权威仍 `03_research/find-journal`。
- **`humanize`：** 2026-10-17 吸收进 B `05-manuscript/humanize/`（✅ B默认）；个人 de-AI 仍在 A `05_manuscript/personal/`。
- **图例 ⚪：** 2026-09-14 后本文件无残留规则参考行；原则已写入对应 B `external-principles.md`。
- **PROPOSED cut round 1（2026-10-17）：** 归档 `paper-lookup` · `analyze-survival` · `audit-citations` · `audit-dicom` · `exploratory-data-analysis` · `polish-latex` · `statistical-power` · `venue-templates` · `write-data-statement`（registry `archived:`）；`check-grant-proposal` / `scientific-critical-thinking` 已在 round 3 ARCHIVED。

- **Round 3 2026-10-17：** `verify-refs` / `simulate-reviewers` / `tighten-response` 吸收进 B domain paths（bodies-to-b-keep-ids，细 ID 仍 MOUNTED）；`check-grant-proposal` ARCHIVED→`grant-builder`；`scientific-critical-thinking` ARCHIVED→`self-review`；`model-validation` ARCHIVED→`model-evaluation`（同 path `04-analysis/model-eval/`）。

**合计口径：** 注册表细 ID 数以 `registry.yaml` `fine_id_count_canonical` 为准（见生成表 `MOUNTED_SKILLS.md`）。
