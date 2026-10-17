# Cache · Mount · Active · Registry = index

- **Cache:** `{mounts_cap}/b/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap/b`) is the **base byte cache** (alias `DIRS['my-skills-base']='b'` OK). Not a source of truth — live B repo is SSOT for bodies.
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`07` only (A domains). Do not load `{mounts_cap}/**/SKILL.md` unless the fine id is in `session_picked_fine_ids`.
- **Registry:** routing index only. GitHub MY-SKILLS is the A framework SSOT.

## Local cache (`{mounts_cap}/`)

Bytes live at `D:/0Grok/0doc/04-lab-reference/mounts-cap` (alias `{mounts_cap}`; outside MY-SKILLS repo). Pointers stay in this skill.

- **Base** (`{mounts_cap}/b/`): **canonical** full tree for `my-skills-base`. Missing → `python D:/0Grok/0doc/04-lab-reference/mounts-cap/fetch.py ensure-b`.
- **Non-base pack folders** may still exist as historical cache leftovers; they are **not** a runtime menu. Do not fetch ARS/OpenClaw (purged). Non-base = default deny.
- `python D:/0Grok/0doc/04-lab-reference/mounts-cap/fetch.py ensure --id <fine-id>` after the session pick (base paths). Download is not a mount.

## External mount lifecycle (base)

01 owns path resolve + cache boundary. 00 gates that provenance/cache state is acceptable and owns B→QC→A flow.

1. **Resolve** fine id → B path via `registry.yaml`.
2. **Ensure** `{mounts_cap}/b/` (or live sibling clone) has bytes.
3. **Pick** — user multi-selects fine ids (ask-each-run).
4. **Post-mount QC** — loaded bytes match registry source + path.

**Stale policy:** refresh base cache when `cache_status` is stale/missing or the user asks. Do not treat non-base folders as session candidates.

**G0 handoff:** if base provenance is missing, fail back to 01 — 00 must not query GitHub itself.
