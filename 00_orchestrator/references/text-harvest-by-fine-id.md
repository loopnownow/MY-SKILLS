# text-harvest-by-fine-id

**Standing (2026-10-23, 城城):** when the owner gives free-form text to harvest, classify by **fine-ID** and extract only three buckets per lane.

**Standing (2026-10-24, 城城):** harvest **task flow** lives in the harvest pack (`00_orchestrator/harvest/SKILL.md`); this file is the thin lane card. Candidate/evidence fields → collection standard §8.


**Workspace (t1840u):** when/where harvest may run, and harvest ≠ closeout → `{RULES}/workspace-layout.md` 「工作区关系：阶段 · 分流 · harvest · 冷库」 (same-turn owner auth; pointer only).

**Decide first (t1952u):** classify H1–H4 before extracting; **H2 (data / PHI / third-party source / build output / profiles / one-off patches / logs) is never harvested — it goes straight to `harvested`**. Objects: `.Del`, `_library`, `_DataBase`; lanes = existing fine-ids only; no mirror snapshots. Authority: `{RULES}\del-and-harvest.md` §2（H1–H4）+ §6（对象与布局）.

**Evidence source priority by lane (t1953u, owner 2026-11-11):**

| Lane | Primary | Secondary | Last resort |
|---|---|---|---|
| `calc-sample-size` | **LLM-derived** (formula / assumption set / worked example) | — | own archives |
| `design-study` | **LLM-derived** | `_library\\references` method sections | our own published methods |
| `draw-flowchart`, `plot-figures` | **our published Figure 1** (`_library\\references` full text) | — | — |
| `track-changes` | **our `archived` manuscripts / replies** (revision marks) | project `ref\\review` | — |

**LLM-sourced drafts are not evidence of our practice.** Header must carry `evidence_type: AI假设` and
`归属: Cap`; keep only "what the rule is / when it breaks"; never invent numbers, cutoffs, citations or
DOIs. Promotion needs owner approval plus a real verification run. Figure-derived lanes record **layout
parameters and criteria only** — never copy the image (copyright) — and cite the source DOI in the draft.

Disk SSOT: `{doc_root}\\harvest\\HARVEST-STANDARD.md` §7 + §8.

| Bucket | Store |
|---|---|
| **语料库要素** (bank elements) | schemas, field lists, enums, short reusable patterns, hard constraints for that fine-ID |
| **过程** (process) | ordered steps, checklists, gates, path pointers (not whole script trees) |
| **注意事项** (cautions) | bans, gotchas, PHI/ethics walls, mix-up traps |

Optional add-on (does not replace the three buckets): `## candidates` — evidence type / ownership (R·S·Reg·Cap·Bank) / strength / disposition / summary. See standard §8.

## Rules

1. Resolve fine-ID via `00_orchestrator` / skill tree (`NN_slug/base/<fine-id>/`).
2. One text → possibly many fine-IDs; **split** — do not paste the whole text into every lane.
3. Draft under `harvest/` (prefer `<fine-id>-harvest.md` with the three bucket `##` headings). Absorb into skills only when the owner says 「进skills」 (promote into live skills) (**extract ≠ promote**).
4. Drop sentences that fit no bucket for any fine-ID (or park as owner triage notes).
5. Never harvest ethics/PHI, full grant/manuscript bodies, or `_code` `.py` trees into skills.
6. Success cases default into bank; AI hypotheses never auto-change runtime. Dispatch and regression four questions → `00_orchestrator/harvest/SKILL.md`.

## Related

- Cut methods: `HARVEST-STANDARD.md` §2
- Link verify: `HARVEST-STANDARD.md` §3
- Task flow and intake gates: `00_orchestrator/harvest/SKILL.md`
