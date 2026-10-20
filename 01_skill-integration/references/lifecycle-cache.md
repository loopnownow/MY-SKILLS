# Cache · Mount · Active · Registry = index

- **Bodies SSOT:** in-repo `NN_slug/base/` (`source: my-skills`).
- **Cache:** `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) is retired (deleted 2026-10-20). Live capability bodies are **not** resolved from `{mounts_cap}/`.
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`07` only. Do not load anything from `{mounts_cap}/` (retired).
- **Registry:** routing index only. GitHub MY-SKILLS is the framework + body SSOT.

## Local cache (`{mounts_cap}/`)

RETIRED: `D:/0Grok/0doc/04-lab-reference/mounts-cap` (alias `{mounts_cap}`) was deleted 2026-10-20; the bullets below are historical.

- Live resolve targets are `NN_slug/base/` in this repo (or `{skills_runtime}` after sync).
- Non-base pack folders may still exist as historical cache leftovers; they are **not** a runtime menu. Do not fetch ARS/OpenClaw (purged). Non-base = default deny.

## Mount lifecycle (in-repo)

01 owns path resolve + cache boundary. 00 gates that provenance is acceptable and owns base -> QC -> personal/top flow.

1. **Resolve** fine id -> in-repo path via `registry.yaml` (`source: my-skills`).
2. **Load** from `NN_slug/base/...` (git working tree / `{skills_runtime}` after sync).
3. **Pick** -- user multi-selects fine ids (ask-each-run).
4. **Post-mount QC** -- loaded bytes match registry source + path.

**Stale policy:** pull/sync MY-SKILLS when bodies change. Do not treat `{mounts_cap}/` pack folders as session candidates.

**G0 handoff:** if an in-repo body path is missing, fail back to 01.

## Post-merge deploy sync

- After an MY-SKILLS merge, copy only the files changed in that merge from the GitHub working copy `D:\0Grok\0doc\GitHub\MY-SKILLS` into `{SKILLS}`. The whitelist is exactly that merge's changed paths.
- No whole-tree overwrite, and no editing an unchanged skill under the name of a sync.
- Acceptance: target path exists and the sampled file hash (or equivalent) matches the working copy.
