# 06_review\base\track-changes\scripts

**Runnable code moved out of this repo (2026-11-01, t1521u P3).** No second copy lives here.

| 原位置 | 现位置 | 归属 |
|---|---|---|
| `scripts/office/**`（`pack` / `unpack` / `validate` + `helpers/` + `validators/`） | `{code_stats}\tools\office\` | Anthropic，见 `{code_stats}\tools\office\LICENSE.txt` |

跑法见 `06_review/base/track-changes/MODULE.md`（`## Tools` / `## The check that matters` / `## Workflow`）：
`validate.py --original <pre-edit.docx> --author A` 是硬门，静默覆盖必须 exit 1。
