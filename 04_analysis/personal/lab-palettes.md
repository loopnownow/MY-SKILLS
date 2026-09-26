# Lab figure palettes (0RAD console)

**Owner:** `05_manuscript` (`references/lab-palettes.md`). Hex must match `D:\0Grok\0RAD\modules\config\style.py` `FIG_PALETTES` and `console.html` `PALETTES`.

Generic journal palettes (ggsci NPG / Okabe–Ito / Morandi role maps) stay in mounted `fig-plot` (`color-systems.md`). This file is the **lab console five-set** used by the 0RAD pipeline.

One palette per manuscript. Main roles in order: **Combined, RadScore, Clinical, Reader, Age**. Auxiliary colors: remaining ROC curves, KM strata, unnamed models.

| id | Label | Use | Main (5) | Aux (5) |
|----|-------|-----|----------|---------|
| `npg` | NPG 现行 | **Default.** Revisions / extra panels so Combined / RadScore / Clinical do not jump | `#D55E00` `#B2182B` `#2166AC` `#762A83` `#117733` | `#44AA99` `#DDCC77` `#EE8866` `#AA4499` `#332288` |
| `okabe` | Okabe–Ito | **New project first choice.** Color-blind safe | `#D55E00` `#0072B2` `#009E73` `#CC79A7` `#E69F00` | `#56B4E9` `#332288` `#882255` `#44AA99` `#999999` |
| `tol` | Paul Tol | Print / Radiology large figures | `#CC6677` `#332288` `#117733` `#88CCEE` `#DDCC77` | `#AA4499` `#44AA99` `#882255` `#6699CC` `#999933` |
| `radiology` | 青橙 | Lab console / series papers | `#0F4C5C` `#C44E52` `#3B6EA5` `#E07A3D` `#2F6F4E` | `#7EB6A4` `#88B4D8` `#D4A373` `#6B5B95` `#8A8A8A` |
| `ibm` | IBM | Projection / results HTML | `#DA1E28` `#0F62FE` `#198038` `#8A3FFC` `#B28600` | `#1192E8` `#009D9A` `#FA4D56` `#A56EFF` `#6F6F6F` |

`npg` keeps the **legacy named** map for clinical covariates (LNM, FIGO, …) so old figures do not recolor.

Config keys: `FIG_PALETTE`, `FIG_COLORS_MAIN`, `FIG_COLORS_AUX`. Hand-edited swatches become custom; write-back goes to `ref/settings.ini`.

## 发表用扩展色板（10套，非 console 绑定）

不进 `style.py` / `console.html`，不受 `FIG_PALETTE` 管理；手动引用，用于投稿图表而非 0RAD 流水线出图。全部来自公开科研配色规范（ColorBrewer / matplotlib 内建 / Paul Tol / Crameri / ggsci 开源包），按图表类型分类，覆盖 `lab-palettes` 五套 + 挂载 `fig-plot`（Okabe-Ito/NPG/Morandi）没有覆盖到的连续量、发散量、灰阶安全场景。

| id | Label | 类型 | 用途 | 取值/来源 |
|----|-------|-----|------|-----------|
| `brewer-set2` | ColorBrewer Set2 | 分类，柔和 | 分组少（≤6）的柱状/散点图，色盲友好 | `#66C2A5 #FC8D62 #8DA0CB #E78AC3 #A6D854 #FFD92F` |
| `brewer-dark2` | ColorBrewer Dark2 | 分类，饱和 | 多组折线图，需要强区分度时 | `#1B9E77 #D95F02 #7570B3 #E7298A #66A61E #E6AB02` |
| `viridis` | Viridis | 连续，感知均匀 | 热图/密度图/连续风险评分，色盲与灰阶均安全 | matplotlib 内建 colormap，直接 `cmap="viridis"` |
| `magma` | Magma | 连续，暖色 | viridis 的暖色替代，radiomics 特征热图避免"绿=正常"的临床联想 | matplotlib 内建，`cmap="magma"` |
| `cividis` | Cividis | 连续，色盲优化 | 审稿人可能色弱时的连续量首选，专为色盲设计 | matplotlib 内建，`cmap="cividis"` |
| `rdbu` | RdBu Diverging | 发散 | 相关矩阵/特征选择热图，正负值对称场景 | ColorBrewer diverging，`cmap="RdBu_r"` |
| `prgn` | PRGn Diverging | 发散，紫绿 | 需要避开红-绿关联（政治/临床）时的发散量替代 | ColorBrewer diverging，`cmap="PRGn"` |
| `batlow` | Batlow (Crameri) | 连续，科学色图 | 期刊（Nature/Science系）近年要求的抗感知畸变色图，替代传统 jet/rainbow | Fabio Crameri scientific colour maps，开源 BSD |
| `grayscale-safe` | 灰阶安全斜坡 | 单色渐变 | 部分期刊仍要求黑白打印可辨；投稿前用此渐变复核 | `#F7F7F7 #CCCCCC #969696 #636363 #252525` |
| `ggsci-lancet` | ggsci Lancet | 分类，期刊风格 | 投柳叶刀系期刊时接近其视觉规范 | R 包 `ggsci::pal_lancet()`，开源 MIT |

选择规则：分类变量（≤6组）用 `brewer-set2`/`brewer-dark2`；连续量（风险评分/概率/密度）用 `viridis`/`magma`/`cividis`；相关矩阵/差值热图用 `rdbu`/`prgn`；投稿前灰阶复核统一过一遍 `grayscale-safe`；投特定期刊时叠加对应 `ggsci-*` 风格。与 `lab-palettes` 五套的关系：console 出图（KM/ROC/风险分层）继续用 npg/okabe/tol/radiology/ibm；这10套用于连续量/矩阵类图或首次投稿的期刊适配，两者不混用同一张图。
