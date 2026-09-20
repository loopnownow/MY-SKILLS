# 01 挂载指针（v4 · CHG-20260913-001）

[总览](README.md) · [迁移 v3→v4](MIGRATION_v3_to_v4.md) · [混合挂载指针（细ID配方）](hybrid-mount-pointers.md) · [配方 presets](presets.md) · [B · 底盘](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md) · [OpenClaw · 禁挂载](openclaw.md) · [AIPOCH · 备份](aipoch.md) · [Nature · 备份](nature.md)

**粗 ID 10 个（焊死 stage buckets）+ 细 ID 51 个（session-pick；其中 4 个 reference-only）。** Hybrid mount：不同细 ID 可用不同包；同一细 ID 内不混包。备份源仍 PROPOSED。OpenClaw **不得**作为任何细 ID 的 atomic source。

| 预设 | 摘要 |
|---|---|
| [迁移图](MIGRATION_v3_to_v4.md) | 旧 30 id → 新 fine ids / ARCHIVED |
| [配方 · 审稿混合默认](presets.md) | `review-hybrid-default`：B 底盘 + Nature/Scientific 细 ID 覆盖（仍 ask-each-run） |
| [B · 当前默认](b.md) | B 默认已含细 ID + 新增挂载；跨包 stub 在 `cross-pack/` |
| [ARS · 备份](ars.md) | 扫 `9443623`。备份候选；按细 ID 映射（非 30 粗） |
| [MedSci · 备份](medsci.md) | 扫 `912f7e8`。多数 B 细 ID 的原子技能源；`humanize` 仍 MedSci 接口 |
| [Scientific · 备份](scientific.md) | 扫 `1e5eeff`。跨包细 ID：paper-lookup / EDA / pydicom / … |
| [OpenClaw · 禁挂载](openclaw.md) | 扫 `b1f9b6e`。**license risk — never atomic mount** |
| [AIPOCH · 备份](aipoch.md) | 扫 `f5ef65b`。retraction-watcher / response-tone-polisher（clinic-research-design 已拒绝） |
| [Nature · 备份](nature.md) | 扫 `287ee37`。LICENSE Apache-2.0 已核实；`nature-figure`/`nature-reviewer`/`nature-response` MOUNTED；其余 PROPOSED |

**每次运行：** 先定粗 bucket → 多选细 ID；未选不加载。预审/审稿可预勾审稿混合配方（细 ID 级）。Registry 状态是菜单。

**空挂协议：** 先通知，再检索确认，不悄悄改挂。个人 de-AI 在 A `05_manuscript/personal/`。说 **默认挂载 B 包/本仓**，不说空挂。

**本地缓存：** 仓库根 `mounts-cap/`。B 整包；备份源只拉本轮选中的细 ID 路径。下载不等于改挂。

机器真源 `../registry.yaml` · 备份 `../_history/registry.v3.30.yaml` · 来源配置 `../sources/*.yaml`。

## Lifecycle reminders

- **下载 ≠ 挂载；更新缓存 ≠ 改变挂载配方；新增 skill ≠ 自动进 registry。**
- OpenClaw = reference-only（provenance/license mixed），never atomic.
- Recipes: `presets.md` (`review-hybrid-default`, `evidence-deep-L2`, `manuscript-final-W2`, `external-review-R1`).
