# 01 挂载指针

[总览](README.md) · [配方 presets](presets.md) · [B · 底盘](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md) · [OpenClaw · 备份](openclaw.md) · [AIPOCH · 备份](aipoch.md) · [Nature · 备份](nature.md)

粗 ID 共 30 个（CHG-20260903-011：P0+P1 细拆）。**审稿默认会话配方**见 [presets.md](presets.md)（B 底盘 + Nature 主外挂 + Scientific 批判叠加）。映射不等于改挂；备份源仍是 PROPOSED。

| 预设 | 摘要 |
|---|---|
| [配方 · 审稿混合默认](presets.md) | `review-hybrid-default`：预勾换源表；芯在 `presets/review-hybrid.yaml`，可换 path。 |
| [B · 当前默认](b.md) | 28 个 id 各一个 B 文件夹。另 2 个 MedSci 接口。空挂无。 |
| [ARS · 备份](ars.md) | 扫 `9443623`。已映射 7 / 30。空挂 23 个。ARS 仍只有 4 包。 |
| [MedSci · 备份](medsci.md) | 扫 `912f7e8`。已映射 27 / 30。空挂 3：`02-pictures`、`02-fmri`、`04-fig-flow`。 |
| [Scientific · 备份](scientific.md) | 扫 `1e5eeff`。已映射 21 / 30。空挂 9 个。 |
| [OpenClaw · 备份](openclaw.md) | 扫 `b1f9b6e`。已映射 23 / 30。空挂 7：`02-imaging-qc`、`02-fmri`、`03-lit-fulltext`、`05-write-reporting`、`05-write-venue`、`05-humanize`、`06-review-response`。 |
| [AIPOCH · 备份](aipoch.md) | 扫 `f5ef65b`。已映射 25 / 30。空挂 5：`02-imaging-qc` · `02-radiomics-habitat` · `05-write-reporting` · `05-humanize` · `06-review-critique`。 |
| [Nature · 备份](nature.md) | 扫 `287ee37`。已映射 13 / 30。空挂 17 个，但填上其他源都空挂的 `03-lit-fulltext`、`06-review-response`。 |

**每次运行：** 先问本轮挂哪些 id（可多选），未选不加载。预审/审稿任务预勾审稿混合配方。Registry `MOUNTED` 是菜单。

**空挂协议：** 先通知，再检索确认，不悄悄改挂。个人 de-AI 在 A `05_manuscript/personal/`。
**本地缓存：** 仓库根 `mounts-cap/`。B 整包；备份源只拉本轮选中的 id 路径。下载不等于改挂。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
