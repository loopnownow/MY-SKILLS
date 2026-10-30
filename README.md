# MY-SKILLS

Live medical and imaging research skill library for Grok Bot seats `00`-`07`.

## 三仓分工（2026-10-27 站立）

| 仓 | 放什么 | 不放什么 |
|---|---|---|
| **MY-RULES** | 站立运营政策：本机布局、交付落点、新建禁区、网络红线、技能库契约 | 专业技能正文、可运行代码 |
| **MY-SKILLS**（本仓） | 专业技能：`NN_slug/base/` 能力正文 + `advanced/` 个人层 + `qc/` 门控标准（**prose SSOT**）；席位/`00_orchestrator` 下允许**轻量 helper**（`**/scripts/` 薄脚本） | 重分析/清洗代码；患者数据 |
| **stats-analysis** | 可运行代码：`modules/` 算法库 + CLI 目录，即 02 席位的脚本半 | skill 正文；课题配置；患者数据 |

判据：**经常用的运营规则进 RULES，专业技能进 SKILLS，重分析/可复用算法进 stats-analysis / `{code_root}`。**
本仓以 prose 为 SSOT；允许席位与 `00_orchestrator/scripts/` 下的**轻量 helper**（lint、flowchart drawer、citation check、viz generator 等）。重分析、清洗、建模 CLI 仍只写路径别名（`{code_stats}` / `{code_modules}` / `{code_model_validation}` / `{code_root}`），不把重脚本 vendor 进本仓。
`{RULES}\skills.md` 规定改本仓的流程（propose-only + PR）；`{RULES}\My rule.md` 规定全局优先级。

## Seats

| Seat | Folder | Role |
|------|--------|------|
| 00 orchestrator | `00_orchestrator` | Intent, skill chain, QC closed loop; registry / index / session-pick |
| 02 data-processing | `02_data-processing` | Raw → analysis-ready; Excel and batch workspace; imaging prep; extraction; coding principles; statistics, prediction, figures (`draw-flowchart` / `plot-figures`) |
| 03 research | `03_research` | Study design, literature, journal selection, grants, ethics forms |
| 05 manuscript | `05_manuscript` | Scientific writing and de-AI |
| 06 review | `06_review` | Peer review (Lee) |
| 07 response | `07_response` | Reviewer response (Aitee) |

Capability bodies for seats 02-07 live in-repo under `NN_slug/base/`. The routing index is `00_orchestrator/registry.yaml`. Lab path aliases (`{code_root}`, `{doc_root}`, `STATS_ROOT`, and the rest) are in `00_orchestrator/references/lab-paths.yaml`. Heavy / reusable analysis stays on `{code_root}` (02 operations) and `{code_stats}` (stats engine + modeling CLIs); human docs stay on `{doc_root}`. This repo may keep **thin helper scripts** under seat `**/scripts/` and `00_orchestrator/scripts/`; it is not a vendor of full `0doc\_code` trees or the stats-analysis library.

Paths under `00`-`07` are at most five parts from the repo root, except `NN_slug/base/**`.

License: MIT (`LICENSE`). Third-party notices: `NOTICE`. Release notes: `VERSION.txt`.

Tests: `python -B -m pytest tests/` (or `unittest discover -s tests`; `-B` keeps `__pycache__` out; needs `pyyaml`).

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
