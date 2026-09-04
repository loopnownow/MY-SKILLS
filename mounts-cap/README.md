# mounts-cap

Local **byte cache** for B and backup plugin packs. Not a domain skill. Pointers stay in `01_skill-discovery-integration`.

| On disk | Source | What is fetched |
|---|---|---|
| `b/` | `loopnownow/MY-SKILLS-capabilities` | **Always** the full B tree. Missing → download. Present → compare GitHub SHA, update if needed. |
| `ars/` `medsci/` `scientific/` | backup repos | **Only the skill path(s) for ids picked this run.** Never clone the whole backup. |
| `STATE.yaml` | local | Recorded SHAs. Gitignored. |

Download is **not** a mount. Backup fetches prefer zip/codeload; `STATE.yaml` merges under lock so parallel `ensure --id` does not clobber keys. Session pick and empty-mount protocol still apply. Never auto-mount a non-B source because a folder appeared here.

Canonical B path is `mounts-cap/b/`. If a leftover sibling `MY-SKILLS-capabilities/` exists, run `python mounts-cap/fetch.py migrate-b` (moves it into `b/`). New fetches always write here.

```text
python mounts-cap/fetch.py ensure-b
python mounts-cap/fetch.py ensure --id 04-explainability
python mounts-cap/fetch.py check
```

Do not vendor unpublished texts, PHI, HIS credentials, or 0RAD trees.
