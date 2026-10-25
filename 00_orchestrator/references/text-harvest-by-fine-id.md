# text-harvest-by-fine-id

**Standing (2026-10-23, 城城):** when the owner gives free-form text to harvest, classify by **fine-ID** and extract only three buckets per lane.

**Standing (2026-10-24, 城城):** harvest **task flow** is owned by **00_orchestrator** and turned into a collection standard (not a new evolution tree). Flow body → `00_orchestrator/references/skill-evolution.md` "Harvest task flow". Candidate/evidence fields → collection standard §8.

Disk SSOT: `{doc_root}\skill-harvest\HARVEST-STANDARD.md` §7 + §8.

| Bucket | Store |
|---|---|
| **corpus elements** (corpus elements) | schemas, field lists, enums, short reusable patterns, hard constraints for that fine-ID |
| **process** (process) | ordered steps, checklists, gates, path pointers (not whole script trees) |
| **cautions** (cautions) | bans, gotchas, PHI/ethics walls, mix-up traps |

Optional add-on (does not replace the three buckets): `## candidates` — evidence type / ownership (R·S·Reg·Cap·Corpus) / strength / disposition / summary. See standard §8.

## Rules

1. Resolve fine-ID via `00_orchestrator` / skill tree (`NN_slug/base/<fine-id>/`).
2. One text → possibly many fine-IDs; **split** — do not paste the whole text into every lane.
3. Draft under `skill-harvest/` (prefer `<fine-id>-harvest.md` with the three bucket `##` headings). Absorb into skills only when the owner says 「进skills」 (promote into live skills) (**extract ≠ promote**).
4. Drop sentences that fit no bucket for any fine-ID (or park as owner triage notes).
5. Never harvest ethics/PHI, full grant/manuscript bodies, or `_code` `.py` trees into skills.
6. Success cases default into corpus; AI hypotheses never auto-change runtime. Dispatch and regression four questions → 00 `skill-evolution.md`.

## Related

- Cut methods (06 projects): `HARVEST-STANDARD.md` §2 + `harvest-projects-cut.md`
- Link verify: §3 + `harvest-verified-links.md`
- Task flow (00): `00_orchestrator/references/skill-evolution.md`
