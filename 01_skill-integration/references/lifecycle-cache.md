# Cache · Mount · Active · Registry = index

- **Cache:** `{mounts_cap}/<pack>/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) is a verified local cache of bytes, not a source of truth. B bytes: the B repo is SSOT. Non-B bytes: that upstream is SSOT.
- **Registry `MOUNTED`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run. Cache is not mount is not active.
- **Advertised / auto-discovery:** `00`–`06` only. Do not load `{mounts_cap}/**/SKILL.md` unless the fine id is in `session_picked_fine_ids`.
- **Registry:** routing index only. GitHub MY-SKILLS is the A framework SSOT. `stub_in_b` (`cross-pack/…` or `external-principles.md`) is a **pointer**, not a second full tree.

## Local cache (`{mounts_cap}/`)

Bytes live at `D:/0Grok/0doc/04-lab-reference/mounts-cap` (alias `{mounts_cap}`; outside MY-SKILLS repo). Pointers stay in this skill.

- **B** (`{mounts_cap}/b/`): **canonical** full tree. Missing → `python D:/0Grok/0doc/04-lab-reference/mounts-cap/fetch.py ensure-b`.
- **MedSci / Scientific / AIPOCH / Nature**: download **only the path(s) of fine ids picked this run**. Never clone wholesale. Do not fetch ARS/OpenClaw (purged from catalog).
- `python D:/0Grok/0doc/04-lab-reference/mounts-cap/fetch.py ensure --id <fine-id>` after the session pick. Download is not a mount. Empty after fetch → empty-mount protocol.

## External Mount Lifecycle (Version & Cache Contract)

01 owns the external skill supply chain. 00 only gates that provenance/cache state is acceptable.

Before each session mount pick (when any non-B path may load, or when `cache_status` is stale/missing/unknown):

1. **Resolve** — upstream tag/release if any, else branch + commit SHA.
2. **Compare** — vs local `cache_commit` / last `resolved_commit`.
3. **Refresh** — update `{mounts_cap}/` cache only for paths that will be used (or that the user asked to refresh). Download ≠ mount.
4. **Inventory diff** — added / removed / renamed skills; update `inventory_hash` when scanned.
5. **License gate** — per-skill / per-path; repo-level MIT/Apache does not auto-cover every nested skill.
6. **Pick** — user multi-selects fine ids (ask-each-run). New skills stay **candidate/PROPOSED** until approved; never auto-MOUNTED.
7. **Post-mount QC** — loaded bytes match registry source + resolved commit.

**Stale policy:** do not hit GitHub on every trivial run. Resolve/refresh when `cache_status` is `stale` / `missing` / `blocked`, when `scanned_at` is older than **14 days** and a non-B fine id is in the candidate set, or when the user asks to update external packs.

**G0 handoff:** if external provenance is missing or not verified, fail back to 01 — 00 must not query GitHub itself.
