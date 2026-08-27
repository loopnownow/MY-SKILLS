---
name: "data-impute"
domain: "04_analysis"
trigger: ["插补", "补缺失", "MICE", "按组填"]
inputs: ["excel_or_csv", "group_column"]
outputs: ["imputed_table", "impute_qc", "backup"]
tools: ["Python", "u_impute"]
quality_control: "group-stratified; observed cells unchanged; align_decimals"
owner: "04_analysis/bundles/data-impute/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# data-impute — 分组缺失值插补

把 **按 Group 分层插补 + 小数位对齐 + 备份/QC** 固化为可复用 Skill。  
实现核心与 `0RAD/*/modules/u_impute.py`、`jfl/modules/u_impute.py` 同源。

## 何时用本 skill

| 触发 | 动作 |
|------|------|
| 用户给 Excel/CSV 说「插补」「补缺失」「按组填」 | 跑 CLI 或 `z_impute` |
| 影像/多模态表有整块 NA（仅 DTI / 仅 IVIM） | 优先 `median` 或 `mice` |
| 嫌 missForest 太慢 | 换 `mice`/`median` 或加速参数 |
| 要求插补值小数位像原始数据 | 保持 `align_decimals=True`（默认） |

## 必读 references

| 文件 | 内容 |
|------|------|
| [references/methods.md](references/methods.md) | 方法选择、速度、missForest 旋钮 |
| [references/checklist.md](references/checklist.md) | 执行前后检查、Methods 表述 |

## 工具位置

```text
<grok-home>/skills/data-impute/
  SKILL.md
  scripts/u_impute.py      # z_impute 核心库
  scripts/impute_excel.py  # Excel CLI
  references/
```

若项目内已有 `modules/u_impute.py`（如 `D:\0Grok\jfl`、`0RAD/*`），**优先用项目模块** 保持与 pipeline 一致；仅无模块时用本 skill 的 `scripts/`。

---

## STEP 0 — 探查（先做再插补）

1. 读表：`shape`、sheet 列表、`Group`（或用户指定列）水平与 n  
2. 缺失：`n_miss_cols`、总缺失格、是否 **块状**（整人缺一整段特征）  
3. 确认：分组列名、method、输出是覆盖还是新文件、是否备份  

缺分组列则 **先问** 或创建伪分组（不推荐）；不要默认用全体均值跨组成填。

---

## STEP 1 — 选 method（默认 mice）

| 场景 | method |
|------|--------|
| 默认 / 连续特征多 | **`mice`** |
| 极速 / 块状缺失 / 可解释 | **`median`** |
| 论文指定 missForest | `missForest`（用加速默认） |
| 对称近似正态单变量 | `mean` |

详见 [methods.md](references/methods.md)。

---

## STEP 2 — 执行

### A. CLI（推荐）

```bash
python "<grok-home>/skills/data-impute/scripts/impute_excel.py" \
  --input "PATH/data.xlsx" \
  --sheet cln \
  --group Group \
  --method mice
```

常用参数：

| 参数 | 默认 | 含义 |
|------|------|------|
| `--output` | 覆盖 input | 输出路径 |
| `--all-sheets` | off | 所有含 group 列的 sheet |
| `--backup` | `<stem>_pre_impute.xlsx` | 备份；`--no-backup` 关闭 |
| `--no-align-decimals` | off | 关闭小数位对齐 |
| `--n-nearest` | 32 | `0` = 全特征（更慢） |
| `--mf-trees` | 30 | 仅 missForest |
| `--include-categorical` | off | 分类列编码插补 |

### B. Python

```python
import sys
from pathlib import Path
sys.path.insert(0, r"<grok-home>/skills/data-impute/scripts")
# 或: sys.path.insert(0, r"D:\0Grok\jfl")  # 用项目 modules

from u_impute import z_impute  # skill scripts
# from modules.u_impute import z_impute  # 项目内

out = z_impute(
    df,
    group_col="Group",
    method="mice",          # median | mean | mice | missForest
    align_decimals=True,
    verbose=True,
)
```

### C. 项目脚本

若存在 `scripts/impute_ssd_dti_ivim.py` 一类专用脚本，按其路径跑；逻辑应调用同一 `z_impute`。

---

## STEP 3 — 铁律（不可违反）

1. **按组插补**：各组独立；禁止无声明的跨组污染  
2. **观测不动**：原非缺失格与备份逐格一致  
3. **小数位**：新值 `round` 到该列非缺失观测小数位数的 **均值**（`align_decimals=True`）  
4. **先备份**：默认写 `*_pre_impute.xlsx`（或 `0del/`）  
5. **写 QC**：`impute_qc` 含 column / n_miss_before / n_miss_after / n_filled / ndigits_mean_obs  
6. **不把 Name/ID 当特征插补目标**；分组列不参与数值建模  
7. **删列阈值**（默认缺 >50%）由建表/pipeline 决定，见 `04_analysis/references/0rad-pipeline-rules.md`；本 skill 只插补留下来的列  

---

## STEP 4 — 验收

```text
numeric missing cells: N → 0 (or residual low-info cols only)
observed cells changed: 0
backup exists
impute_qc present
```

不通过则：换 `median` 回退、检查组内方差、打印 skip low-info 列。

---

## STEP 5 — 交付物说明（回复用户）

1. 输入/输出路径、method、分组列  
2. 缺失格 before → after  
3. 备份路径  
4. QC 摘要（缺失最多的几列 + ndigits 样例）  
5. 若用了 missForest：写明加速参数，避免用户误以为跑了「全特征 100 树」  

---

## 与影像 pipeline 的关系

| 阶段 | 建议 |
|------|------|
| 合并临床+特征后、LASSO 前 | 本 skill 插补 |
| 已 train/test 划分 | 理想：仅 train 拟合插补器再 transform test（当前 CLI 为整表按组；划分后需定制） |
| 后续建模 | `pipeline.py` / radiomics 模块 |

---

## 触发语

- `/data-impute`  
- 按 Group 插补 / 缺失值填充 / MICE / missForest  
- 插补值小数位对齐原始数据  
- u_impute 太慢，换快方法  

---

# End of skill
