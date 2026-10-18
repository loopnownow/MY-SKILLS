# Cache · Mount · Active · Registry = index

- **Bodies SSOT:** in-repo `NN_slug/base/` (`source: my-skills`).
- **Cache:** `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) remains the lab pack-cache root for non-base leftovers only. Live capability bodies are **not** resolved from `{mounts_cap}/`.
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`07` only. Do not load `{mounts_cap}/**/SKILL.md` unless the fine id is in `session_picked_fine_ids`.
- **Registry:** routing index only. GitHub MY-SKILLS is the framework + body SSOT.

## Local cache (`{mounts_cap}/`)

Bytes path: `D:/0Grok/0doc/04-lab-reference/mounts-cap` (alias `{mounts_cap}`; outside MY-SKILLS repo). Pointers stay in this skill.

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
