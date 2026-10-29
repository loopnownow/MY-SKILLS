# Forbidden combinations · Hard rules · Fine-id expansion

## Forbidden combinations

These are **session-pick** bans, not skill deletions:

1. Do **not** offer a second runtime package menu. Bodies are in-repo `my-skills` (`NN_slug/base/`).
2. Do **not** let multiple authoring engines **directly edit** the same manuscript sentences in one pass — one primary authoring authority (05 advanced); others are verifier / QC / venue only.
3. Reviewer engines output **findings only**; they must not edit the manuscript bypassing 06.
4. Venue polishing must not overwrite base write-paper / advanced author voice.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review (00 is index only).
- Never rewrite MY-SKILLS because an external text exists.
- Never replace an advanced / top layer because an external text is more general.
- `PROPOSED` is not `LIVE`.
- Advanced de-AI (`05_manuscript/advanced/`) is not a base row. Generic de-AI is `humanize` (`05_manuscript/base/humanize/`). The advanced forbidden list still wins.
- Top layers are not capability rows (00 owns base→QC→advanced).

## Fine-id expansion

Prefer merge into an existing fine id / sub-capability / same source-path. Do not open a new fine id unless architecture review approves. Live count is `fine_id_count_canonical` in `registry.yaml` (must equal `len(fine ids)`). Do not restate the number in prose.


## load_priority

Optional historical metadata. Live rows no longer carry `load_priority`. Session pick order follows coarse grouping + agent judgment, not P0/P1/P2 folders.
