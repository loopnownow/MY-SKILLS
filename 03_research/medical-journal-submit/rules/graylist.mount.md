# Graylist (mounted)

Journals the lab does **not recommend** for new submissions when better options exist, but that are not hard-banned.

- Files (SSOT): `data/2026/graylist.csv` / `data/2026/graylist-names.csv`
- Tier order: **blacklist** (never) → **graylist** (prefer alternatives) → normal pool → **whitelist-submitted** boost → **BMC/Medicine** pattern boost

## Pattern: Frontiers 系列 (always gray)

Treat as graylist when any of:
- Publisher / publisher group is Frontiers Media (SA) / Frontiers
- Title starts with `Frontiers ` / `Frontiers in`
- ISO abbreviation starts with `FRONT ` or `FRONTIERS`

Seed CSV lists full-pool Frontiers hits; the **pattern** still applies to new Frontiers titles not yet in the CSV.

## Recommendation rule (user 2026-09-19)

**If the layer already has better non-gray matches, do not use graylist journals.**

Practical:
1. Fill each layer (default 10) from non-blacklist, **non-gray** candidates first (match → submitted whitelist → BMC pattern → JESI).
2. Only pull from graylist when the layer would otherwise be short **and** the gray title still has reasonable scope fit — or the user explicitly asks to include Frontiers / graylist.
3. When a gray title is shown: mark 「灰名单/不推荐」; never boost; never auto-fill like whitelist.
4. Never promote graylist → whitelist-submitted without explicit user approval.
5. Blacklist always wins over graylist.

User may add non-Frontiers gray titles to the CSV with a `reason`.
