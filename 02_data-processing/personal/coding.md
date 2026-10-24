# 代码优化与重构

个人层：`02_data-processing/personal/coding.md`（由 `code-refactoring/SKILL.md` 迁入；复杂度阶梯并入下文）。  
深度代码 QC 细则见`../qc/coding-qc.md`。不另建顶层、不登记 01 coarse id。

## 适用场景
- 代码软编码（配置置顶）
- 大幅精简、去除无用部分
- 断点续传 / 并行 / CUDA
- dry-run
- **深审 / Deep QC / modules 代码质控**（五轴 + 医学完整性**引用** 04）
- 写时代码阶梯 / 写后复杂度检查（稳定方法论吸收，非外挂）
- 科研数据处理脚本（R/Python/MATLAB/shell；raw→analysis-ready）release-ready QC

## Capability map

| 任务 | 路径 |
|---|---|
| 软编码 + dry-run 模板 | `{code_root}\_infra\_templates\soft_code_template.py` |
| 深度代码 QC（五轴/分级/Critical + Code QC Core） | `../qc/coding-qc.md` |
| 写时代码阶梯 + 强度/护栏 | 下文「Complexity ladder」节 |

Medical / Statistical Integrity：**只引用** `04_analysis/qc/report-checks.md` 与 `04_analysis/personal/pipeline.md`，不在本技能复制金标准。

## 核心原则

权威总则（含配置置顶 / 仅注释配置与运行说明 / 不写回退 / 多模块可配置可选 / dry-run / 断点续传）→ MY-RULES `My rule.md` §3。下文为技能侧展开与模板指针。

### 1. 软编码（配置置顶）
- 路径、关键词、参数集中在文件顶部配置区（配置块在逻辑之前）
- 避免硬编码；配置字段加注释
- 允许多模块；模块可用配置开关可选启用

### 2. 精简 + 阶梯
- 最少必要代码；不为单次使用建抽象
- 写前按下文「Complexity ladder」节停在第一个「是」
- 医学入口禁用 **ultra** 强度

### 3. 断点续传
- 已处理结果跳过；检查中间文件或完成标记

### 4. 并行 / CUDA
- 独立任务可并行；注意内存

### 5. 注释规范
- **2026-10-24 裁决维持**：注释 = 配置字段含义 + 如何运行；**不写业务「为什么」**。权威 → `{RULES}` `My rule.md` §3。
- **仅**注释：(a) 配置字段含义；(b) 脚本如何运行。不对业务逻辑写长文注释。

### 5b. 不写回退
- 禁止 fallback / 静默降级；勿用 try-except 吞失败后走默认路径；失败要响

### 6. Dry Run
- 先试运行；打印将执行操作供确认

### 7. 深度 QC
- 触发、分级、Preflight→Verdict、Data Safety / Reproducibility 见 `../qc/coding-qc.md`
- 废料进 `0del`、子模块 dry-run、禁止静默成功：见 `../qc/coding-qc.md`
- Critical/Required/Optional 为主标签；P0–P3 为报告别名
- 边界：≠ archived `skill-harvest/qc` / MY-RULES skills.md (skill-evolution)；≠ `preprocess-imaging`；≠ 04 model/figure QC；≠ Copilot playbooks/`quality/`
- 不 vendor `{code_modules}` 整树
- 00 路由：`gates.md` **G-CODE**

## 附带的模板
- `{code_root}\_infra\_templates\soft_code_template.py` — 软编码 + 断点续传 + dry run 模板

---

## Complexity ladder（吸收自 complexity-ladder.md）

Absorbed stable consensus (Ponytail-style lazy ladder). **Not** a 01 mount / coarse id.

## When writing (stop at first yes)

1. **YAGNI** — Is this needed? If no, skip.
2. **Reuse in-repo** — Same capability already in the project?
3. **Stdlib** — Language standard library enough?
4. **Platform native** — OS / runtime already provides it?
5. **Existing dependency** — Already in env/`requirements`? Do not add deps lightly.
6. **One-liner** — Clear few-line expression enough?
7. **Minimal new code** — Only then write the smallest working code.

Aligns with: soft-coding, dry-run, CONFIG-on-top, no one-off abstractions.

## After writing (complexity check)

Remove/merge when medically unnecessary:

- Extra new dependencies
- Duplicate logic already in-repo
- Speculative wrappers / factories used once
- Dead "maybe later" features
- Needless indirection / over-config

Severity: usually **Optional**; clear duplicate of an existing module may be **Required**. Never outrank **Critical** (leakage, dry-run broken, startup failure, QC bypass).

## Intensity

| Mode | When | Behavior |
|---|---|---|
| **full** (default) | Refactors / figure scripts | Strict ladder, few new deps |
| **lite** | User confirmed new feature | Suggest lazier options; do not block confirmed need |
| **ultra** | — | **Disabled** for medical/stats entrypoints |

## Medical guardrails (hard)

Do **not** delete or weaken for shortness:

- train/test (/ external) isolation; seeds; artifacts / reproducibility dumps
- dry-run / `--execute`; CONFIG-on-top; checkpoint
- Stats & data QC (point to `04_analysis/personal/pipeline.md` / `report-checks.md`; do not rewrite gold standards here)
- Registration / habitat hard QC; Pictologics constraints

**Minimal necessary complexity ≠ fewest lines.** Correctness, reproducibility, auditability first.
