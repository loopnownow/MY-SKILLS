# 挂载配方（presets）

[总览](README.md) · [配方表](presets.md) · [B](b.md) · [Nature](nature.md) · [Scientific](scientific.md)

**现行默认会话配方：** `review-hybrid-default` @ `2026-09-08.2`（芯 [`presets/review-hybrid.yaml`](presets/review-hybrid.yaml)）。

**挂载 / 评分 / 批注单位 = 源 + 包内 skill**，不是整包。粗 ID 只做会话壳。映射 ≠ 改挂；备份源仍 `PROPOSED`。

## 默认：`review-hybrid-default`

| 粗 ID | 源 | 包内 skill（可换芯） | 路径 | 批注前缀例 | 必选 |
|---|---|---|---|---|---|
| （底盘） | B | （本轮其余已选 id） | mounts-cap/b | `[B:<粗ID>]` | 是 |
| — | A 06 personal | review-resolution 等 | personal/ | `[A:personal]` | 是 |
| `03-lit-cite` | Nature | **`nature-ref-verifier`** | `skills/nature-ref-verifier/` | `[Nature:nature-ref-verifier]` | 是 |
| `04-stats-guide` | Nature | **`nature-statistics`** | `skills/nature-statistics/` | `[Nature:nature-statistics]` | 是 |
| `03-lit-fulltext` | Nature | `nature-downloader` | `skills/nature-downloader/` | `[Nature:nature-downloader]` | 否 |
| `06-review-critique` | Scientific | **`scientific-critical-thinking`** | `skills/scientific-critical-thinking/` | `[Scientific:scientific-critical-thinking]` | 是 |
| `06-review-peer` / `response` | **强制 B** | 粗 ID | B 包 | `[B:06-review-peer]` 等 | 若选用 |

**禁用默认：** ARS；带外未注册编辑工具。  
**不预勾：** MedSci / OpenClaw / AIPOCH 整包或其它 Nature skills（要加就改 yaml `skills`/`paths`）。

## 换芯

1. 改 yaml 的 `skills` + 对齐 `paths`（目标源须已映射该粗 ID）。
2. bump `version`；本页记一行。
3. 大改默认主 skill 前，按 `skill-harvest/qc/mount-score-rubric.md` 按 **skill** 复盘。
4. 禁止只凭「Nature 总分」改挂；禁止自动 MOUNTED。

## 会话点选

预审/审稿：预勾本配方；展示列为 **粗 ID · 源 · skill**。`fetch` 只拉列出的 skill 路径。

## 人读评分表

结果表给人看（skill-library / 本地）。主键必须是 `源/skill`。尺子在 `skill-harvest/qc/mount-score-rubric.md`。
