# mounts-cap

Local **byte cache** for B and backup plugin packs. Not a domain skill. Pointers stay in `01_skill-discovery-integration`.

| On disk | Source | What is fetched |
|---|---|---|
| `b/` | `loopnownow/MY-SKILLS-capabilities` | **Always** the full B tree. Missing → download. Present → compare GitHub SHA, update if needed. |
| `ars/` `medsci/` `scientific/` | backup repos | **Only the skill path(s) for ids picked this run.** Never clone the whole backup. |
| `STATE.yaml` | local | Recorded SHAs. Gitignored. |

Download is **not** a mount. Session pick and empty-mount protocol still apply. Never auto-mount a non-B source because a folder appeared here.

Legacy: if `MY-SKILLS-capabilities/` still sits next to A, 01 may read it as B until `b/` exists. New fetches go here.

```text
python mounts-cap/fetch.py ensure-b
python mounts-cap/fetch.py ensure --id 04-explainability
python mounts-cap/fetch.py check
```

Do not vendor unpublished texts, PHI, HIS credentials, or 0RAD trees.
