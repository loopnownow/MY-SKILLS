# Forbidden combinations · Hard rules · Ceiling · load_priority

## Forbidden combinations (mount red lines)

These are **mount-time** bans, not skill deletions:

1. Do **not** default-load three literature search engines together (Scientific literature-review + MedSci literature-search + AIPOCH literature-search).
2. Do **not** let Scientific scientific-writing + MedSci write-paper + A/B05 personal all **directly edit** the same manuscript sentences in one pass — one primary authoring engine; others are verifier / QC / venue only. **Sentence authority stays A/B05 personal** (Intro v3 / de-AI).
3. Reviewer engines (Scientific / MedSci / Nature peer-review) output **findings only**; they must not edit the manuscript bypassing A06.
4. Nature (or any venue) polishing must not overwrite B05 / A personal author voice.
5. Never keep AIPOCH as a whole-pack resident context — fine ids only.
6. Do not remount packs purged from catalog (`ars_openclaw_policy: removed-from-catalog`).

Intro / Discussion default discovery: Scientific `paper-lookup` (or Research Lookup) + MedSci/Scientific **verify-refs**. Open MedSci literature-search only when a structured clinical search is needed.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a **non-B** Skill.
- Never bulk-download MedSci / Scientific / AIPOCH / Nature. On-demand paths only, after a pick.
- Never remount ARS/OpenClaw (removed from catalog).
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `humanize` (B `05-manuscript/humanize/`). The personal forbidden list still wins.

## Fine-id expansion ceiling

`fine_id_count_canonical` in `registry.yaml` is the **v4 expansion ceiling**. Prefer merge into an existing fine id / sub-capability / same source-path. Do not open a new fine id unless architecture review approves. Do not restate the number in prose.

## load_priority (optional YAML)

Registry fine ids may carry `load_priority: P0|P1|P2` (metadata only — **no** P0/P1/P2 folders).

| Level | Meaning |
|---|---|
| P0 | Rare always-on mounts (chassis is 00–06; usually unused on fine ids) |
| P1 | Common mounts (verify-refs, write-paper, check-reporting, analyze-stats, draw-flowchart/plot-figures, peer-review, lit-search, imaging-io, preprocess-imaging, revise, self-review, …) |
| P2 | Niche / PROPOSED / specialty |
