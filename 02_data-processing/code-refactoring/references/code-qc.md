# 0RAD modules 深度代码 QC — 可复用规则

副标题：亦覆盖科研数据处理脚本（R / Python / MATLAB / shell；raw → analysis-ready）的轻量 **Code QC Core**（吸收自 awesome-copilot 类稳定原则，已医学科研适配）。

来源：2026-09-07 Deep Code QC Report（`modules.zip` / `D:\0Grok\0RAD\modules`）+ 2026-09-22 Code QC Core 吸收方案  
目标并入：`MY-SKILLS/02_data-processing/code-refactoring/`（本文件为唯一细则家园）  
**不**进：`skill-harvest/qc`（仓治理）、`02-imaging-qc`（影像质控）、新建顶层技能、B 挂载菜单、平行的 `02_data-processing/code-qc.md` / `coding-principles.md`、mount Copilot `playbooks/quality/` / Council / CI。

## 何时触发
- 审 / 深审 / Deep QC / 代码质控 `modules` / 0RAD 统计库
- 发布前、大改 pipeline/console/radiomics/clinical/impute 后复测
- 与软编码 / dry-run / 重构同一入口（code-refactoring），先 QC 再改或改后复测
- 科研数据处理脚本（raw→analysis-ready）release-ready / 深审

00 仅路由：见 `00_orchestrator/gates.md` **G-CODE**；细则只在本文件。

## 五轴 + 医学轴（Deep QC 保留）
| 轴 | 审什么 |
|----|--------|
| Correctness | 启动、默认参数、公式/检验选择、注释与实现一致性；错位筛选/计算、错误输出、数据泄漏 |
| Architecture | 超大函数、职责耦合、可测边界（**完整保留**；不以「仅 02 边界」窄化） |
| Data Safety（原 Security 扩展） | PHI/PII；secrets/tokens 进代码/日志/输出；勿在未显式要求且无版本化前提下覆盖 raw；输出污染；**保留**本地 console CORS、路径是否 project-scoped |
| Performance | 高维相关矩阵、重复全表扫描、不必要全量预计算；无明确 perf 问题不优化 |
| Testability / Verification | 有无单测 / smoke / 合成数据回归；科研脚本以 sanity（n、dims、NA、ranges、output counts）与边角为主，**不强制**生产级 test coverage |
| Medical / Statistical Integrity | **只对照 `04_analysis` 金标准**，不在本技能重写方法 |
| Reproducibility（Core 新增） | 输入、参数、环境、随机种子、路径、输出是否足以复现；能定则定；拆分时确认 train/test 分离 |
| Boundary（P2 附加） | 02 不得拥有统计建模 / 稿件写作 / 审稿 QC（→ 04 / 05 / 06） |

医学轴必对照（指针，正文在 04）：
- AUC 95% CI = 1000 bootstrap；成对 DeLong 是 **p** 不是 CI
- LASSO / 预筛 / impute / scale / NZV / corr filter：**折内**拟合，禁止全训练集预筛后再 CV
- VAL_MODE ∈ {refit, apply_formula, lock_threshold}；不重筛特征
- 内部拆分 training/test；外部验证 = 外院；禁用 Development set
- Cox 可选默认关；声称 MICE 须真多重插补 + Rubin，否则改名
- 插补分层禁止用 outcome 派生 Group；transformer 在 train 拟合再应用到 test

## 分级（主标签 + 报告别名）
| 主标签（报告优先） | 别名（P0–P3） | 含义 |
|---|---|---|
| **Critical** | P0 BLOCK | 启动级故障、CV leakage、本机 console 可跨项目读写、错误结果/腐蚀/泄漏、不安全数据处置、关键步不可复现 → 未修不作为可发布/正式建模版；**遇 Critical/P0 即停** |
| **Required** | P1 FIX | 统计实现边界、选择偏倚、静默 except、无测试、缺 lock、实质性可靠性/验证缺口 → 修完再复测 |
| **Optional** | P2 WARN / P3 NOTE | 风格/命名/小优化；可维护性、明显 perf、Boundary；P3 = 可选备注 |

输出：HTML 或表格式报告（ID / 级别[+P别名] / 轴 / 问题 / 证据路径 / 影响 / 建议）。结论句先写能不能当正式建模版。  
Verdict：`PASS` / `PASS_WITH_WARNINGS` / `FAIL`。

## 最小流程（Preflight → Verdict）
```
Code / Script
    ↓
0. Preflight — I/O / env / deps + Existing Pattern First
    ↓
1. P0 Critical QC — Correctness / Data Safety / Reproducibility
                 + Medical axis when relevant
    ↓  (stop on Critical/P0)
2. P1 Verification — sanity: n, dims, NA, ranges, output counts; edge cases
    ↓
3. P1 Maintainability — 命名、重复、错误处理、函数职责、关键注释
    ↓
4. P2 Performance / Boundary
    ↓
Verdict — PASS / PASS_WITH_WARNINGS / FAIL
```

不要求每次跑满；大型影像处理、批量变换、train/test 构建优先 P0/P1；小型格式转换可走轻量路径。

### Existing Pattern First
结构改动前先检查项目既有约定（布局、命名、CONFIG 风格、日志与路径习惯）；禁止 AI 强行套用外来编码风格。

### Findings 规则
- 尽量引用 **file / function / line**
- 说明机制 + 下游影响，不只复述规则名
- 证据不足 → **QUESTION**，不是 BUG
- 不发明缺失需求
- 无可靠性/可复现/可维护影响时，不做纯风格 nit
- 无明确 perf 问题不优化

## 已验证通过也要记
语法 compileall、无明显 os.system/exec/pickle、subprocess 列表调用、patient-level split 检查、VAL_MODE 设计意图 —— 报告里单独「已通过」块，避免只报问题。

## 与 code-refactoring 原原则的关系
保留：CONFIG 置顶、dry-run、checkpoint、模块化、精简、注释。  
新增：深审流程与分级；Code QC Core（Data Safety、Reproducibility、Preflight→Verdict、P0–P3 别名）；重构建议仍遵循「重构与功能修改分开」。

## 明确不要
- 不把整树 `.py` / 患者表 / 课题 Excel vendor 进 GitHub
- 不把 Medical 轴写成第二套 04 金标准
- 不把 skill-harvest `repo_qc.py` 与本流程混为一谈
- ≠ skill-harvest/qc；≠ imaging-qc；≠ 04 model/figure QC；≠ mount Copilot playbooks/`quality/` / Council / CI
- 不另建 `02_data-processing/code-qc.md`、`coding-principles.md`，不建 `code-qc/` / `quality/` / `testing/` 目录

## 写后复杂度检查（吸收自稳定阶梯共识）

见同目录 `complexity-ladder.md`。在 Deep QC 报告中可作为 Architecture / Optional（或重复实现时 Required）条目；**不得**压过 Critical。

## Critical 检查项（来自 2026-09-07 modules 深审；改 modules 须用户点名）

- **C-01**：无 `settings.ini` 时 config fallback 键不全 → stats 导入失败（启动级）
- **C-02**：LASSO CV 前全训练集 impute/scale/NZV/corr + AUC top-k → 折间泄漏
- **C-03**：console `CORS=*` + `under_root` 仅限 `GROK_ROOT` → 跨项目路径风险

路径指针（不 vendor）：`D:\0Grok\0RAD\modules`
