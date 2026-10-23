# Cache · Mount · Active · Registry = index

- **Bodies SSOT:** in-repo `NN_slug/base/` (`source: my-skills`).
- **Cache:** `{mounts_cap}/` (`D:/0del/_by-function/mounts-cap-retired-20261020`) is RETIRED as of 2026-10-20 and its bytes were moved to `D:/0del/_by-function/mounts-cap-retired-20261020`. It was the lab pack-cache root for non-base leftovers only. Live capability bodies are **not** resolved from `{mounts_cap}/`.
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`07` only. Never load from the retired `{mounts_cap}/`.
- **Registry:** routing index only. GitHub MY-SKILLS is the framework + body SSOT.

## Local cache (`{mounts_cap}/`, retired)

Bytes path: `D:/0del/_by-function/mounts-cap-retired-20261020` (alias `{mounts_cap}`; outside MY-SKILLS repo). Retired 2026-10-20; the bytes now sit at `D:/0del/_by-function/mounts-cap-retired-20261020`, and the alias stays here for path history only.

- Live resolve targets are `NN_slug/base/` in this repo (`{skills_runtime}` = `{skills_git}`).
- Non-base pack folders are no longer in the workspace (archived under `D:/0del`); they are **not** a runtime menu. Do not fetch ARS/OpenClaw (purged). Non-base = default deny.

## Mount lifecycle (in-repo)

01 owns path resolve + cache boundary. 00 gates that provenance is acceptable and owns base -> QC -> personal/top flow.

1. **Resolve** fine id -> in-repo path via `registry.yaml` (`source: my-skills`).
2. **Load** from `NN_slug/base/...` (git working tree = `{skills_runtime}`).
3. **Pick** -- user multi-selects fine ids (ask-each-run).
4. **Post-mount QC** -- loaded bytes match registry source + path.

**Stale policy:** pull/sync MY-SKILLS when bodies change. The retired `{mounts_cap}/` folders are never session candidates.

**G0 handoff:** if an in-repo body path is missing, fail back to 01.

## Post-merge deploy sync

- As of 2026-10-23, `{SKILLS}` / `{skills_runtime}` **is** the GitHub working copy `{skills_git}` (no separate `.grok\skills` tree). After merge: `git pull` on that clone; do **not** copy into a second runtime folder.
- Still: no whole-tree blind overwrite of unrelated paths, and no editing live skill bodies outside PR/merge.
- Acceptance: working tree on main matches the merged commit.
