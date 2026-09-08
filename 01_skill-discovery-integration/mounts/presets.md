# 挂载配方（presets）

[总览](README.md) · [配方表](presets.md) · [B](b.md) · [Nature](nature.md) · [Scientific](scientific.md)

**现行默认会话配方：** `review-hybrid-default`（机器芯 [`presets/review-hybrid.yaml`](presets/review-hybrid.yaml)）。

映射 ≠ 改挂。六个备份源在 registry 仍是 `PROPOSED`。配方只决定**本轮点选的预勾与换源**；用户仍可改选。细节 path 可换，粗 ID 壳尽量不动。

## 默认：`review-hybrid-default` @ 2026-09-08

| 层 | 源 | 粗 ID / 路径要点 | 角色 | 必选 |
|---|---|---|---|---|
| 底盘 | **B** | 本轮其余已选 id | 主干能力 | 是 |
| 个人 | A `06_review/personal` | `review-resolution` · 前缀规则 | 裁决 / Issue status | 是 |
| 主外挂 | **Nature** | `03-lit-cite` → `nature-citation` + `nature-ref-verifier` | 文献核对 | 是 |
| 主外挂 | **Nature** | `04-stats-guide` → `nature-statistics` | 报告侧数字/统计表述审计 | 是 |
| 主外挂 | **Nature** | `03-lit-fulltext` → `nature-downloader`（可选） | 全文 | 否 |
| 叠加 | **Scientific** | `06-review-critique` → `scientific-critical-thinking` 等 | 逻辑/机制 | 是 |
| 强制 B | B | `06-review-peer` · `06-review-response` | 同侪审 / 回复骨架 | 若本轮需要这些 id |

**禁用（默认配方）：** ARS；带外未注册编辑工具（不得静默改数字）。

**暂不预勾（可换芯候选）：** MedSci、OpenClaw、AIPOCH（试跑 response drafter 时另开临时配方）。

## 换芯规则

1. 只改 yaml 里 `overrides[].paths` / `source`（目标源须已有该粗 ID 映射）。
2. `version` 递增；在本页记一行变更。
3. 改「谁当主外挂」属大改：先按 `skill-harvest/qc/mount-score-rubric.md` 复盘，用户确认后再改默认配方。
4. 禁止把评分结果自动写回 registry / 自动 MOUNTED。

## 会话点选怎么用

1. 任务若是预审 / 审稿 / 回复审稿 → **预勾本配方**（仍展示多选，可改）。
2. 其它任务 → 仍按 id 默认源（多为 B），不强制本配方。
3. `fetch.py ensure` 只拉本轮选中 id 的路径。

## 人读评分表

实测打分表给人看（归档在 skill-library 或本地报告）。**评分标准**在 `skill-harvest/qc/mount-score-rubric.md`，不进 gates。
