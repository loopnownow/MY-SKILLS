# 插补方法选择

## 速度与用途（经验量级，41×170 量级）

| method | 典型耗时 | 机制 | 适用 |
|--------|----------|------|------|
| `median` | ~0.2 s | 组内中位数填缺失 | 块状缺失（整模态缺失）、要极致快、可解释 |
| `mean` | ~0.2 s | 组内均值 | 近似对称连续变量 |
| `mice` | ~数秒 | IterativeImputer + BayesianRidge | **默认推荐**；连续特征联合建模 |
| `missForest` | 数十秒～数分钟 | IterativeImputer + RandomForest | 非线性/交互强；论文方法名要求时 |

## missForest 加速旋钮

| 参数 | 默认 | 说明 |
|------|------|------|
| `mf_n_trees` / `--mf-trees` | 30 | 原常见 100；30 通常够用 |
| `max_iter` / `--max-iter` | 10 | 原 20 |
| `n_nearest_features` / `--n-nearest` | 32 | 每列只用相关最强的 k 个预测变量；`0`/`None`=全部（更慢） |
| `mf_max_depth` | 8 | 限制树深 |
| `skip_complete` | True | 完整列不做迭代目标 |

Ultra 快（质量次之）：

```text
--method missForest --mf-trees 10 --max-iter 5 --n-nearest 16
```

## 分组原则

- **必须**按结局/队列分层（`Group` / SSD·HC / 病例·对照），避免用对侧组的分布填缺失。
- 某组内某列非缺失 < 2 或唯一值 < 2 → 该列该组跳过（或后续 median 回退）。
- 整列在某组全缺 → 无法组内学习，只能保持 NaN 或改用全局策略（本 skill 默认不跨组）。

## 块状缺失（如仅 DTI / 仅 IVIM）

优先 `median` 或 `mice`。missForest 对「整块模态缺失」收益有限且很慢。

## 分类变量

- 默认只插补数值列。
- 需要时：`--include-categorical` 或 `include_categorical=True`（编码 → 插补 → 就近取整还原）。
- ID 类列（几乎全唯一）自动跳过。

## 小数位对齐（默认开）

对新填入的格子：

```text
ndigits = round(mean(有效小数位数 of 该列非缺失观测))
imputed_cell = round(value, ndigits)
```

原非缺失格 **保持原值**。关：`--no-align-decimals`。
