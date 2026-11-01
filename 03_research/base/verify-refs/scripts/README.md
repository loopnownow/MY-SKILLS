# 03_research\base\verify-refs\scripts

**Runnable code moved out of this repo (2026-11-01, t1521u P3-B).** No second copy lives here.

| 原位置 | 现位置 | 归属 |
|---|---|---|
| `scripts/*.py`（`_common.py` + 8 个 CLI） | `{code_stats}\tools\verify-refs\` | MIT，上游与版权见 `{code_stats}\tools\verify-refs\LICENSE_NOTE.txt` |

网络闸：联网脚本默认拒绝运行（`network disabled`，exit 1）；每次加 `--allow-network`，或整壳设
`SKILLS_ALLOW_NETWORK=1`。离线脚本（`format_bibtex.py`、`search_google_scholar.py`）无需开关。

跑法见 `03_research/base/verify-refs/MODULE.md`（Phase 1–4 命令）与
`03_research/base/verify-refs/references/script_reference.md`（逐脚本参数）。
