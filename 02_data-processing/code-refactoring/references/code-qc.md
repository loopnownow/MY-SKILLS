# 0RAD modules 深度代码 QC — 可复用规则

来源：2026-09-07 Deep Code QC Report（`modules.zip` / `D:\0Grok\0RAD\modules`）  
目标并入：`MY-SKILLS/02_data-processing/code-refactoring/`  
**不**进：`skill-harvest/qc`（仓治理）、`02-imaging-qc`（影像质控）、新建顶层技能、B 挂载菜单。

## 何时触发
- 审 / 深审 / Deep QC / 代码质控 `modules` / 0RAD 统计库
- 发布前、大改 pipeline/console/radiomics/clinical/impute 后复测
- 与软编码 / dry-run / 重构同一入口（code-refactoring），先 QC 再改或改后复测

## 五轴 + 医学轴
| 轴 | 审什么 |
|----|--------|
| Correctness | 启动、默认参数、公式/检验选择、注释与实现一致性 |
| Architecture | 超大函数、职责耦合、可测边界 |
| Security | 本地 console CORS、路径是否 project-scoped |
| Performance | 高维相关矩阵、重复全表扫描、不必要全量预计算 |
| Testability | 有无单测 / smoke / 合成数据回归 |
| Medical / Statistical Integrity | **只对照 `04_analysis` 金标准**，不在本技能重写方法 |

医学轴必对照（指针，正文在 04）：
- AUC 95% CI = 1000 bootstrap；成对 DeLong 是 **p** 不是 CI
- LASSO / 预筛 / impute / scale / NZV / corr filter：**折内**拟合，禁止全训练集预筛后再 CV
- VAL_MODE ∈ {refit, apply_formula, lock_threshold}；不重筛特征
- 内部拆分 training/test；外部验证 = 外院；禁用 Development set
- Cox 可选默认关；声称 MICE 须真多重插补 + Rubin，否则改名
- 插补分层禁止用 outcome 派生 Group；transformer 在 train 拟合再应用到 test

## 分级
- **Critical**：启动级故障、CV leakage、本机 console 可跨项目读写 → 未修不作为可发布/正式建模版
- **Required**：统计实现边界、选择偏倚、静默 except、无测试、缺 lock 文件等 → 修完再复测
- **Optional**：风格 / 命名 / 小优化

输出：HTML 或表格式报告（ID / 级别 / 轴 / 问题 / 证据路径 / 影响 / 建议）。结论句先写能不能当正式建模版。

## 已验证通过也要记
语法 compileall、无明显 os.system/exec/pickle、subprocess 列表调用、patient-level split 检查、VAL_MODE 设计意图 —— 报告里单独「已通过」块，避免只报问题。

## 与 code-refactoring 原原则的关系
保留：CONFIG 置顶、dry-run、checkpoint、模块化、精简、注释。  
新增：深审流程与分级；重构建议仍遵循「重构与功能修改分开」。

## 明确不要
- 不把整树 `.py` / 患者表 / 课题 Excel vendor 进 GitHub
- 不把 Medical 轴写成第二套 04 金标准
- 不把 skill-harvest `repo_qc.py` 与本流程混为一谈


## 写后复杂度检查（吸收自稳定阶梯共识）

见同目录 `complexity-ladder.md`。在 Deep QC 报告中可作为 Architecture / Optional（或重复实现时 Required）条目；**不得**压过 Critical。

## Critical 检查项（来自 2026-09-07 modules 深审；改 modules 须用户点名）

- **C-01**：无 `settings.ini` 时 config fallback 键不全 → stats 导入失败（启动级）
- **C-02**：LASSO CV 前全训练集 impute/scale/NZV/corr + AUC top-k → 折间泄漏
- **C-03**：console `CORS=*` + `under_root` 仅限 `GROK_ROOT` → 跨项目路径风险

路径指针（不 vendor）：`D:\0Grok\0RAD\modules`
