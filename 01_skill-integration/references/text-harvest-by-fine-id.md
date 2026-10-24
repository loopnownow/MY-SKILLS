# text-harvest-by-fine-id

**Standing (2026-10-23, 城城):** when the owner gives free-form text to harvest, classify by **fine-ID (细ID)** and extract only three buckets per lane.

**Standing (2026-10-24, 城城):** harvest **任务流程**由 **00_orchestrator** 管理，并做成收集标准（非新 evolution 树）。流程正文 → `00_orchestrator/references/skill-evolution.md`「Harvest 任务流程」。候选/证据字段 → 收集标准 §8。

Disk SSOT: `{doc_root}\_corpus\skill-harvest\HARVEST-STANDARD.md` §7 + §8.

| Bucket | Store |
|---|---|
| **语料库要素** (corpus elements) | schemas, field lists, enums, short reusable patterns, hard constraints for that fine-ID |
| **过程** (process) | ordered steps, checklists, gates, path pointers (not whole script trees) |
| **注意事项** (cautions) | bans, gotchas, PHI/ethics walls, mix-up traps |

可选附加（不替换三桶）：`## candidates` — 证据类型 / 归属(R·S·Reg·Cap·Corpus) / 强度 / 处置 / 摘要。见标准 §8。

## Rules

1. Resolve fine-ID via `01_skill-integration` / skill tree (`NN_slug/base/<fine-id>/`).
2. One text → possibly many fine-IDs; **split** — do not paste the whole text into every lane.
3. Draft under `_corpus/skill-harvest/` (prefer `<fine-id>-harvest.md` with the three Chinese `##` headings). Absorb into skills only when owner says「进skills」(**extract ≠ promote**).
4. Drop sentences that fit no bucket for any fine-ID (or park as owner triage notes).
5. Never harvest ethics/PHI, full grant/manuscript bodies, or `_code` `.py` trees into skills.
6. 成功案例默认进 corpus；AI假设永不自动改 runtime。调度与回归四问 → 00 `skill-evolution.md`。

## Related

- Cut methods (06 projects): `HARVEST-STANDARD.md` §2 + `harvest-projects-cut.md`
- Link verify: §3 + `harvest-verified-links.md`
- Task flow (00): `00_orchestrator/references/skill-evolution.md`
