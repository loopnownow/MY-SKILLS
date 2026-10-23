# text-harvest-by-fine-id

**Standing (2026-10-23, 城城):** when the owner gives free-form text to harvest, classify by **fine-ID (细ID)** and extract only three buckets per lane.

Disk SSOT: `{doc_root}\_corpus\skill-harvest\HARVEST-STANDARD.md` §7.

| Bucket | Store |
|---|---|
| **语料库要素** (corpus elements) | schemas, field lists, enums, short reusable patterns, hard constraints for that fine-ID |
| **过程** (process) | ordered steps, checklists, gates, path pointers (not whole script trees) |
| **注意事项** (cautions) | bans, gotchas, PHI/ethics walls, mix-up traps |

## Rules

1. Resolve fine-ID via `01_skill-integration` / skill tree (`NN_slug/base/<fine-id>/`).
2. One text → possibly many fine-IDs; **split** — do not paste the whole text into every lane.
3. Draft under `_corpus/skill-harvest/` (prefer `<fine-id>-harvest.md` with the three Chinese `##` headings). Absorb into skills only when owner says「进skills」.
4. Drop sentences that fit no bucket for any fine-ID (or park as owner triage notes).
5. Never harvest ethics/PHI, full grant/manuscript bodies, or `_code` `.py` trees into skills.

## Related

- Cut methods (06 projects): `HARVEST-STANDARD.md` §2 + `harvest-projects-cut.md`
- Link verify: §3 + `harvest-verified-links.md`
