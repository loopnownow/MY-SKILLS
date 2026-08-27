# Lab figure palettes (0RAD console)

**Owner:** `05_manuscript` (`references/lab-palettes.md`). Hex must match `D:\0Grok\0RAD\modules\config\style.py` `FIG_PALETTES` and `console.html` `PALETTES`.

Generic journal palettes (ggsci NPG / Okabe–Ito / Morandi role maps) stay in `bundles/figure-engine/references/color-systems.md`. This file is the **lab console five-set** used by the 0RAD pipeline.

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
