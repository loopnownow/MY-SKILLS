---
name: code-refactoring
description: >
  Lab code refactoring and deep code QC for 0RAD/modules-style repos: CONFIG on top,
  dry-run, checkpoint, modular scripts, YAGNI/reuse ladder, Critical/Required/Optional
  code review. Use for 软编码, dry-run, 配置置顶, 模块化, 深审, Deep QC, 代码质控,
  modules QC, YAGNI, 最小实现, 反过度工程. Do not use for 统计方法正文 (04_analysis),
  影像 ROI QC (02-imaging-qc), Excel 批处理 (02-tables), 伦理填表, skill-harvest/qc
  repo scans, or registering a new 01/B mount.
---

# 代码优化与重构

家园在 `02_data-processing/code-refactoring/`（模板在 `scripts/`）。  
深度代码 QC 与复杂度阶梯**吸收**进本技能，不另建顶层、不登记 01/B 粗 ID。

## 适用场景
- 代码软编码（配置置顶）
- 大幅精简、去除无用部分
- 断点续传 / 并行 / CUDA
- dry-run
- **深审 / Deep QC / modules 代码质控**（五轴 + 医学完整性**引用** 04）
- 写时代码阶梯 / 写后复杂度检查（稳定方法论吸收，非外挂）

## Capability map

| 任务 | 路径 |
|---|---|
| 软编码 + dry-run 模板 | `scripts/soft_code_template.py` |
| 深度代码 QC（五轴/分级/Critical） | `references/code-qc.md` |
| 写时代码阶梯 + 强度/护栏 | `references/complexity-ladder.md` |

Medical / Statistical Integrity：**只引用** `04_analysis`（`personal/0rad-pipeline-rules.md` 等），不在本技能复制金标准。

## 核心原则

### 1. 软编码（配置置顶）
- 路径、关键词、参数集中在文件顶部配置区
- 避免硬编码；关键参数加注释

### 2. 精简 + 阶梯
- 最少必要代码；不为单次使用建抽象
- 写前按 `references/complexity-ladder.md` 停在第一个「是」
- 医学入口禁用 **ultra** 强度

### 3. 断点续传
- 已处理结果跳过；检查中间文件或完成标记

### 4. 并行 / CUDA
- 独立任务可并行；注意内存

### 5. 注释规范
- 文件顶功能/用法；关键逻辑与配置区注释

### 6. Dry Run
- 先试运行；打印将执行操作供确认

### 7. 深度 QC
- 触发与分级见 `references/code-qc.md`
- 边界：≠ `skill-harvest/qc`；≠ `02-imaging-qc`
- 不 vendor `D:\0Grok\0RAD\modules` 整树

## 附带的模板
- `scripts/soft_code_template.py` — 软编码 + 断点续传 + dry run 模板
