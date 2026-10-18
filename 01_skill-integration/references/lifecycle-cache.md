# Cache · Mount · Active · Registry = index

- **Bodies SSOT:** in-repo A `NN_slug/base/` (`source: my-skills`). Not a separate remote package.
- **Cache:** `{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) remains the lab pack-cache root for historical / non-base leftovers. Former `{mounts_cap}/b/` B byte cache is **obsolete for live mounts** (retired with MY-SKILLS-base 2026-10-17).
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`07` only (A domains). Do not load `{mounts_cap}/**/SKILL.md` unless the fine id is in `session_picked_fine_ids`.
- **Registry:** routing index only. GitHub MY-SKILLS is the A framework + body SSOT.

## Local cache (`{mounts_cap}/`)

Bytes path: `D:/0Grok/0doc/04-lab-reference/mounts-cap` (alias `{mounts_cap}`; outside MY-SKILLS repo). Pointers stay in this skill.

- **Former Base** (`{mounts_cap}/b/`): historical B tree only -- **not** live resolve target. Live paths are A `NN_slug/base/`.
- **Non-base pack folders** may still exist as historical cache leftovers; they are **not** a runtime menu. Do not fetch ARS/OpenClaw (purged). Non-base = default deny.
- Do not run `fetch.py ensure-b` for live mounts.

## Mount lifecycle (in-repo)

01 owns path resolve + cache boundary. 00 gates that provenance is acceptable and owns base->QC->A flow.

1. **Resolve** fine id -> in-repo path via `registry.yaml` (`source: my-skills`).
2. **Load** from A `NN_slug/base/...` (git working tree / `{skills_runtime}` after sync).
3. **Pick** -- user multi-selects fine ids (ask-each-run).
4. **Post-mount QC** -- loaded bytes match registry source + path.

**Stale policy:** pull/sync MY-SKILLS when bodies change. Do not treat `{mounts_cap}/b/` or non-base folders as session candidates.

**G0 handoff:** if an in-repo body path is missing, fail back to 01 -- 00 must not query a retired remote B repo.
