# 01 挂载指针

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

粗 ID 共 30 个（CHG-20260903-011：P0+P1 细拆）。默认仍是 B。映射不等于改挂。

| 预设 | 摘要 |
|---|---|
| [B · 当前默认](b.md) | 28 个 id 各一个 B 文件夹。另 2 个 MedSci 接口。空挂无。 |
| [ARS · 备份](ars.md) | 扫 `9443623`。已映射 7 / 30。空挂 23 个。ARS 仍只有 4 包。 |
| [MedSci · 备份](medsci.md) | 扫 `912f7e8`。已映射 27 / 30。空挂 3：`02-pictures`、`02-fmri`、`04-fig-flow`。 |
| [Scientific · 备份](scientific.md) | 扫 `1e5eeff`。已映射 21 / 30。空挂 9 个。 |

**每次运行：** 先问本轮挂哪些 id（可多选），未选不加载。Registry `MOUNTED` 是菜单。

**空挂协议：** 先通知，再检索确认，不悄悄改挂。个人 de-AI 在 A `05_manuscript/personal/`。
**本地缓存：** 仓库根 `mounts-cap/`。B 整包；备份源只拉本轮选中的 id 路径。下载不等于改挂。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
