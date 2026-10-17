# 01 skill-index · mounts board

[总览](README.md) · [非 base 例外 = 默认拒绝](hybrid-mount-pointers.md) · [配方 presets](presets.md) · [B · 唯一默认](b.md)

**粗 ID 10 个（焊死 stage buckets）。细 ID 以 `registry.yaml` `fine_id_count_canonical` 为准（session-pick；reference_only 已空）。**

**默认唯一运行时来源 = `my-skills-base`（MY-SKILLS-base）。** 非 base 来源默认拒绝（见 hybrid-mount-pointers）。ARS / OpenClaw **已从 catalog 清除**（`ars_openclaw_policy: removed-from-catalog`）— 永不 remount，不进 session pick。

**细 ID 全表：** [`../registry.yaml`](../registry.yaml)（机器）· [`../MOUNTED_SKILLS.md`](../MOUNTED_SKILLS.md)（生成会话菜单）。本板不是多包挂载叙事。

| 页 | 角色 |
|---|---|
| [配方 presets](presets.md) | **First-pass fine-ID lists**（不是“选哪个包”） |
| [B · 唯一默认](b.md) | Base 细 ID 与路径 |
| [MedSci / Scientific / AIPOCH / Nature stubs](medsci.md) | 死包板 stub → 归档；默认拒绝 |

**每次运行：** 先定粗 bucket → 多选细 ID；未选不加载。Registry 状态是菜单门。A 顶层不是 capability mount（00 管 B→QC→A）。

**空挂协议：** 先通知，再检索确认，不悄悄改挂。个人 de-AI 在 A `05_manuscript/personal/`。说 **默认挂载 B = 本仓**，不说空挂。

**本地缓存：** `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`)。**Base 字节 = `{mounts_cap}/b/`**（`DIRS['my-skills-base']='b'` 别名 OK）。下载不等于改挂。

机器真源 `../registry.yaml` · 唯一活源配置 `../sources/b-my-skills-base.yaml`。

## Lifecycle reminders

- **下载 ≠ 挂载；更新缓存 ≠ 改变挂载配方；新 skill ≠ 自动进 registry。**
- Non-base = default deny. ARS/OpenClaw purged.
- Recipes: `presets.md` (`review-hybrid-default`, `evidence-deep-L2`, `manuscript-final-W2`, `external-review-R1`) — fine-ID lists only.

## Cache · Mount · Active

| | |
|---|---|
| Cache | `{mounts_cap}/b/` base bytes (alias OK) |
| Mount | registry fine-id session pick |
| Active | loaded this run |
| Registry | **index only** — B repo / cache holds bodies |

**Fine-id ceiling** is `fine_id_count_canonical` in `registry.yaml`. Do not restate the number here.

**load_priority:** optional `P0|P1|P2` on registry fine ids (YAML only).
