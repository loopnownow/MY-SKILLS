# MY-SKILLS

Live medical and imaging research skill library for Grok Bot seats `00`–`07`.

## 三仓分工（2026-10-27 站立）

| 仓 | 放什么 | 不放什么 |
|---|---|---|
| **MY-RULES** | 站立运营政策：本机布局、交付落点、新建禁区、网络红线、技能库契约 | 专业技能正文、可运行代码 |
| **MY-SKILLS**（本仓） | 专业技能：`NN_slug/base/` 能力正文 + `personal/` 个人层 + `qc/` 门控标准，**全部 prose** | 分析/清洗代码；患者数据 |
| **stats-analysis** | 可运行代码：`modules/` 算法库 + CLI 目录，即 02 席位的脚本半 | skill 正文；课题配置；患者数据 |

判据：**经常用的运营规则进 RULES，专业技能进 SKILLS，能跑的脚本进 stats-analysis。**
本仓提到脚本时只写路径别名（`{code_stats}` / `{code_modules}` / `{code_model_validation}`），不 vendor `.py`。
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

Capability bodies for seats 02–07 live in-repo under `NN_slug/base/`. The routing index is `00_orchestrator/registry.yaml`. Lab path aliases (`{code_root}`, `{doc_root}`, `STATS_ROOT`, and the rest) are in `00_orchestrator/references/lab-paths.yaml`. Runnable code stays on `{code_root}` (02 operations) and `{code_stats}` (stats engine + the modeling CLIs); human docs stay on `{doc_root}`. This repo is not a vendor of `0doc\_code` or `stats-analysis`.

Paths under `00`–`07` are at most five parts from the repo root, except `NN_slug/base/**`.

License: MIT (`LICENSE`). Third-party notices: `NOTICE`. Release notes: `VERSION.txt`.

Tests: `python -B -m unittest discover -s tests` (`-B` keeps `__pycache__` out of the tree; needs `pyyaml`).

Maintained by Aitor for [loopnownow](https://github.com/loopnownow).
