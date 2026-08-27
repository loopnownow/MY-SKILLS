# 插补任务检查清单

## 执行前

- [ ] 确认输入路径与 sheet 名（`cln` / `rad` / 单表）
- [ ] 确认分组列名（默认 `Group`）及水平（如 HC / SSD）
- [ ] 预览缺失：列数、总缺失格、是否块状缺失
- [ ] 选定 method（默认 `mice`；块状缺失可 `median`）
- [ ] 计划备份路径（默认 `<stem>_pre_impute.xlsx`）

## 执行

- [ ] 运行 CLI 或项目内 `z_impute` / `scripts/impute_*.py`
- [ ] 日志显示各组 n、填补格数、method 参数

## 执行后

- [ ] 数值缺失格数下降（理想为 0，低方差列可残留）
- [ ] **原观测值未变**（非缺失位置与备份一致）
- [ ] 新值小数位 ≈ 该列观测小数位均值
- [ ] `impute_qc`（或等价表）含：列、miss_before/after、ndigits
- [ ] 不把 ID / 标签 / 分组列当预测变量写进模型泄漏叙述

## 写入 Methods 时可写（示例句）

> Missing values were imputed within outcome groups using [group-wise median / MICE with Bayesian ridge / missForest]. Observed values were left unchanged. Imputed continuous values were rounded to the mean number of decimal places of non-missing observations in the same variable.

## 禁止

- 跨 Group 用全体均值填结局相关缺失（除非用户明确要求）
- 在测试集上用训练集之外的信息做插补（若已划分 train/test，应 **仅在 train 拟合插补器** 再 transform test——当前 CLI 为「整表按组」，划分后场景需额外脚本）
- 无备份直接覆盖唯一原始文件
