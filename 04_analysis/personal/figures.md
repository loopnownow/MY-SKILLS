# Figures (palettes + claim planning)

## Part A — Lab palettes

# Lab figure palettes (0RAD console)

**Owner:** `05_manuscript` (`{doc_root}\\templates\\lab-palettes.md`). Hex must match `{script_modules}\config\style.py` `FIG_PALETTES` and `modules\console\console_schema.js` `PALETTES`.

Generic journal palettes (ggsci NPG / Okabe–Ito / Morandi role maps) stay in mounted `plot-figures` (`color-systems.md`). This file is the **lab console five-set** used by the 0RAD pipeline.

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

不进 `style.py` / `console.html`，不受 `FIG_PALETTE` 管理；手动引用，用于投稿图表而非 0RAD 流水线出图。全部来自公开科研配色规范（ColorBrewer / matplotlib 内建 / Paul Tol / Crameri / ggsci 开源包），按图表类型分类，覆盖 `lab-palettes` 五套 + 挂载 `plot-figures`（Okabe-Ito/NPG/Morandi）没有覆盖到的连续量、发散量、灰阶安全场景。

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


---

## Part B — Figure claim planning

# Figure claim planning (放射组学/临床预测图表规划)

**Owner:** `04_analysis`. 适用于生成投稿图表前的规划阶段，不是画完图再补救。与 `personal/figures.md`（配色）、mounted `plot-figures`（具体图型模板）配合使用，本文件只管"先想清楚"这一步。

## 1. 先问论断，再选图型——不按"这类数据通常怎么画"选图

选图前问自己：**这张图要向读者证明哪一句 Discussion 里的话？** 论断决定图型，不是数据类型或美观偏好决定图型。本实验室常见论断 → 图型映射：

| 论断类型 | 用这个 | 不要用这个 |
|---|---|---|
| "Combined 模型优于 Clinical" | 配对 ROC 叠加图 + 图注标 DeLong p | 把两个 AUC 分别画柱状图对比（丢了配对信息） |
| "模型概率预测校准良好" | 校准曲线（预测概率 vs 观察频率） | 只报一个 Brier score 数字，没有图 |
| "高低风险组生存有差异" | KM + log-rank，风险表放在图下 | Cox 森林图（本实验室不做多变量 Cox，见 `personal/pipeline.md`） |
| "特征选择稳定" | LASSO 路径图（TRAIN-only StratifiedKFold AUC path） | 特征重要性柱状图（掩盖了选择过程的不稳定性） |
| "影像组学可重复" | ICC 分布图/森林图，标注 ICC≥0.75 阈值线 | 只报文字"ICC 良好" |

不确定论断是什么时，先把 Discussion 里对应那句话写出来，再倒推图型——句子写不出来，说明这张图还不该动手画。

## 2. 图表-证据清单：动笔前先建，不是画完再对账

投一篇稿子前，先列一张清单（可以直接写在 `handoff.yaml` 的 `outputs` 里，或单独存一份 `figure-manifest.md`），每张计划图记三件事：

| 图 | 论断（对应 Discussion 哪句） | 数据来源（哪个 `*-results.html`） |
|---|---|---|
| Fig 2 | Combined 优于 Clinical | `RadScore-results.html` |
| Fig 3 | 高低风险组生存有差异 | `Survival-results.html` |

这张清单不是新发明——它是把已有的 **G-FACT / G-04**（数字必须来自上游 `*-results.html`，不能编造）从"05 写作时事后核对"前移到"04 画图前先登记"。清单建好之后，画图和写作两边都对着同一份表核对，避免图和正文数字对不上却各自都"看起来对"的情况。

## 3. 单图修复上限：三轮，第三轮后仍有问题就如实标"未解决"

每张图：渲染 → 打开实际生成的图片检查（不是看代码觉得应该对）→ 有问题就修 → 重新渲染 → 再检查。**最多三轮**，首次渲染不计入修复轮次。第三轮之后还有问题，保留结果、在 `qc`/`defects` 里如实标注"未解决"，不要为了交付硬把有问题的图标成"通过"。

这条复用的是 `gates.md` 里"同一缺陷最多3轮，之后标 unresolved 并停"的通用规则，不是给图表单独定的新上限——只是提醒：图表检查必须是"打开图片看"，不能是"跑完脚本没报错就算过"。

## 4. 风格与配色是两个独立开关，不要合并成一次询问的两个选项

**风格**（这张图集是给 0RAD console 内部看，还是给期刊投稿；是否需要额外的组合子图）和**配色**（用 `lab-palettes.md` 的 console 五套，还是发表用扩展的10套）是两件不相关的事，能任意组合。两者都不确定时可以合并成一次询问，但只要有一个已经在项目里确定过（比如这次任务已经定了投稿风格），后续只问缺的那一个，不要连已经定过的一起重新问一遍。同一任务里的补图、改图沿用已确定的两个选择，不逐图重复询问——和已经写进 `00_orchestrator` Plan card 的"问清楚一次不重复问"是同一个习惯。
