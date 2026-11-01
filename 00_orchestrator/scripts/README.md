# 00_orchestrator\scripts

**Runnable scripts moved out of this repo (2026-11-01, t1521u P3).** No second copy lives here.

| 原脚本 | 现位置 | 跑法 |
|---|---|---|
| `style_lint.py`（G-05 子检查） | `{code_stats}\tools\orchestrator\style_lint.py` | `SKILLS_ROOT=<本仓> python {code_stats}\tools\orchestrator\style_lint.py <manuscript.md> --json` |

它**运行时读本仓** `05_manuscript/base/vocab/L1/ban-terms.yaml`，所以必须先设 `SKILLS_ROOT`（或 `MY_SKILLS`）
指向本仓；缺变量即 exit 非零，不猜路径、不回退缓存。规则正文仍在 `00_orchestrator/references/style-tells.md`
与 `00_orchestrator/gates.md` 的 G-05 段。
