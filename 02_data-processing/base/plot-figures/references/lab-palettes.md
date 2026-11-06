# Lab palettes — 20 console sets (`FIG_PALETTE`)

**Numeric SSOT:** `{code_modules}\config\style.py` → `FIG_PALETTES`. Console twin:
`modules\console\console_schema.js` → `PALETTES`. If a hex here and `style.py`
disagree, `style.py` wins — regenerate this table, do not hand-edit hexes.

`tests/test_lab_paths.py` (`LabPalettesDrift`) fails when this table stops matching
`style.py`; it skips only when the MY-CODES checkout is absent.

Every set is 5 main + 5 aux colours. One palette per manuscript; main roles in
order **Combined, RadScore, Clinical, Reader, Age**; aux covers the remaining ROC
curves, KM strata and unnamed models. Config keys: `FIG_PALETTE`,
`FIG_COLORS_MAIN`, `FIG_COLORS_AUX` — hand-edited swatches become custom, write-back
goes to `ref/settings.ini`. Semantic colour choice and the colour-blind rules live in
`color-systems.md`; the 10 non-console publication sets live in
`02_data-processing/advanced/analysis/figures.md`.

Palettes: **20**

| key | label | tag | main (5) | aux (5) |
|---|---|---|---|---|
| `npg` | NPG 现行 | 与现图一致（默认） | `#D55E00` `#B2182B` `#2166AC` `#762A83` `#117733` | `#44AA99` `#DDCC77` `#EE8866` `#AA4499` `#332288` |
| `okabe` | Okabe–Ito | 新稿推荐 / 色盲安全 | `#D55E00` `#0072B2` `#009E73` `#CC79A7` `#E69F00` | `#56B4E9` `#332288` `#882255` `#44AA99` `#999999` |
| `tol` | Paul Tol | 印刷 / Radiology | `#CC6677` `#332288` `#117733` `#88CCEE` `#DDCC77` | `#AA4499` `#44AA99` `#882255` `#6699CC` `#999933` |
| `radiology` | 青橙 | 本组控制台同色 | `#0F4C5C` `#C44E52` `#3B6EA5` `#E07A3D` `#2F6F4E` | `#7EB6A4` `#88B4D8` `#D4A373` `#6B5B95` `#8A8A8A` |
| `ibm` | IBM | 投影 / 幻灯 | `#DA1E28` `#0F62FE` `#198038` `#8A3FFC` `#B28600` | `#1192E8` `#009D9A` `#FA4D56` `#A56EFF` `#6F6F6F` |
| `aaas` | AAAS / Science | Science 风 | `#3B4992` `#EE0000` `#008B45` `#631879` `#008280` | `#BB0021` `#5F559B` `#A20056` `#808180` `#1B1919` |
| `nejm` | NEJM | 新英格兰 | `#BC3C29` `#0072B5` `#E18727` `#20854E` `#7876B1` | `#6F99AD` `#FFDC91` `#EE4C97` `#7E6148` `#3C5488` |
| `lancet` | Lancet | 柳叶刀 | `#00468B` `#ED0000` `#42B540` `#0099B4` `#925E9F` | `#ADA638` `#ADB6B6` `#1B1919` `#FDAF91` `#6A6599` |
| `jama` | JAMA | JAMA 风 | `#374E55` `#DF8F44` `#00A1D5` `#B24745` `#79AF97` | `#6A6599` `#80796B` `#024B7A` `#EFC000` `#868686` |
| `jco` | JCO | 临床肿瘤 | `#0073C2` `#EFC000` `#868686` `#CD534C` `#7AA6DC` | `#003C67` `#8F7700` `#3B3B3B` `#A73030` `#4A6990` |
| `d3` | D3 Category10 | 通用 / 多模型 | `#1F77B4` `#FF7F0E` `#2CA02C` `#D62728` `#9467BD` | `#8C564B` `#E377C2` `#7F7F7F` `#BCBD22` `#17BECF` |
| `tableau` | Tableau 10 | 柔和 / 幻灯 | `#4E79A7` `#F28E2B` `#E15759` `#76B7B2` `#59A14F` | `#EDC948` `#B07AA1` `#FF9DA7` `#9C755F` `#BAB0AC` |
| `set1` | Brewer Set1 | 高对比 | `#E41A1C` `#377EB8` `#4DAF4A` `#984EA3` `#FF7F00` | `#A65628` `#F781BF` `#999999` `#1B9E77` `#E6AB02` |
| `dark2` | Brewer Dark2 | 深色 / 印刷 | `#1B9E77` `#D95F02` `#7570B3` `#E7298A` `#66A61E` | `#E6AB02` `#A6761D` `#666666` `#1F78B4` `#B15928` |
| `paired` | Brewer Paired | 主辅成对 | `#1F78B4` `#E31A1C` `#33A02C` `#FF7F00` `#6A3D9A` | `#A6CEE3` `#FB9A99` `#B2DF8A` `#FDBF6F` `#CAB2D6` |
| `tolbright` | Tol Bright | 色盲安全 / 明亮 | `#4477AA` `#EE6677` `#228833` `#CCBB44` `#66CCEE` | `#AA3377` `#BBBBBB` `#222255` `#225555` `#663333` |
| `frontiers` | Frontiers | Frontiers 风 | `#D51317` `#F39200` `#95C11F` `#0094CD` `#6F286A` | `#007B3D` `#31B7BC` `#164194` `#EFD500` `#706F6F` |
| `bmj` | BMJ | BMJ 风 | `#2A6EBB` `#F0AB00` `#C50084` `#7D5CC6` `#E37222` | `#69BE28` `#00B2A9` `#CD202C` `#747678` `#1B1919` |
| `uchicago` | UChicago | 沉稳 / 学术 | `#800000` `#155F83` `#FFA319` `#8A9045` `#767676` | `#C16622` `#8F3931` `#58593F` `#350E20` `#D6D6CE` |
| `gray` | 灰度 | 黑白印刷 | `#000000` `#4D4D4D` `#7F7F7F` `#262626` `#A6A6A6` | `#595959` `#8C8C8C` `#333333` `#BFBFBF` `#1A1A1A` |

## Notes (from `style.py`)

- **npg** (NPG 现行): 保留当前 Combined / RadScore / Clinical。改稿、返修、补图用这个，颜色不会跳。
- **okabe** (Okabe–Ito): Nature Methods 常用。红绿色盲可分，屏幕和印刷都稳。新开课题优先。
- **tol** (Paul Tol): Paul Tol muted。饱和度低，CMYK 印刷不容易糊。适合 Radiology / Eur Radiol 大图。
- **radiology** (青橙): 深青 + 砖红 + 陶土橙，和 console 同一套。组会幻灯、系列论文统一视觉用。
- **ibm** (IBM): IBM color-blind safe。对比强，投大屏清楚。网页结果 HTML 也好认。
- **aaas** (AAAS / Science): Science / AAAS 常用离散色。主色偏蓝红绿，适合多曲线对照。
- **nejm** (NEJM): NEJM 系列色。对比清晰，适合临床结局曲线。
- **lancet** (Lancet): Lancet 风格。红橙青绿，印刷与屏幕都清楚。
- **jama** (JAMA): JAMA 网络期刊常用色。偏深蓝与暖橙。
- **jco** (JCO): Journal of Clinical Oncology 系列色。蓝紫绿对比稳。
- **d3** (D3 Category10): D3 / matplotlib 默认 10 色。辨识度高，模型多时不撞色。
- **tableau** (Tableau 10): Tableau 10 新版。饱和度适中，屏幕和投影都耐看。
- **set1** (Brewer Set1): ColorBrewer Set1。红蓝绿紫橙对比强，适合 3–5 条主曲线。
- **dark2** (Brewer Dark2): ColorBrewer Dark2。偏深，白底印刷不发虚，细线也清楚。
- **paired** (Brewer Paired): ColorBrewer Paired。主色深、辅色为同色系浅色，适合训练/验证成对曲线。
- **tolbright** (Tol Bright): Paul Tol bright + dark。色盲可分，比 muted 更亮，适合屏幕阅读。
- **frontiers** (Frontiers): Frontiers 系列期刊常用色。红橙绿蓝紫跨度大。
- **bmj** (BMJ): BMJ 系列色。蓝金品红对比清楚，适合临床对照曲线。
- **uchicago** (UChicago): UChicago 学术配色。栗红、灰、金为主，低饱和，正式场合用。
- **gray** (灰度): 纯灰阶。黑白印刷或复印不丢信息，配合线型区分曲线。
