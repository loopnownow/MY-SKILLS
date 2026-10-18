# External executor monitoring (Cline / Cursor)

Only during that task. Stop when the task ends or no external agent is active (not standing).

1. Check progress every 10 minutes; estimate and report ETA, adjust with progress.
2. Watch process / log / artifacts / blockers; report only at milestone, stuck, or done.
3. At the end, collect the executor feedback (summary, paths, acceptance, leftovers) and report to Aitor.
4. Usage pages: query only the executor, only when that run lasted ≥30 minutes. Cline `https://app.cline.bot/dashboard/usage`; Cursor `https://cursor.com/dashboard/spending`. Grok usage page only when the user names it.
5. All report times: Asia/Shanghai (UTC+08:00).
