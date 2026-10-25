# Session pick · Empty path · Resolution

## In-repo bodies

Capability bodies live under `NN_slug/base/` (`source: my-skills`), except `check-reporting` at `05_manuscript/qc/check-reporting/`.

Agents propose `MOUNTED` fine ids from `registry.yaml`. Still ask each run; the user may change picks. Attribution is per skill path.

**A listed id is not loaded until this run selects it.** Status `PROPOSED` is not pickable.

## Session mount pick

Registry status `MOUNTED` = catalog-approved and session-selectable. It is not attached until this run selects it.
`PROPOSED` is not pickable.
`session_picked_fine_ids` = selected this run. Active = actually loaded.

Every independent run needs a selection. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock and do not ask. Otherwise enter this section. A single-node personal-layer task with no in-repo dependency does not ask (example: polish one sentence). **A top layers are not capability mounts.**

1. Classify the task. Propose the **relevant seat(s)** (`a_domain`) then **MOUNTED candidate fine ids**.
2. Show each candidate as one line: **fine ID · seat (a_domain) · registry path · role**. Paths are `NN_slug/base/...` except `check-reporting` at `05_manuscript/qc/check-reporting/`.
3. **Ask the user to multi-select fine ids**. Also offer: select all candidates / personal layer only. Empty picked path -> tell the user; do not silent-fallback.
4. Load **only** the picked fine ids from their registry paths (`NN_slug/base/...`, or `05_manuscript/qc/check-reporting/` for `check-reporting`). Unpicked stay unloaded.
5. If a picked path is empty -> empty-path protocol. Do not silently substitute another path.
6. Do not change `registry.yaml` just because this run wanted a path that is not in the index.

Silence is not approval. Personal layers and A top layers are not session picks.
Say **bodies are in-repo under NN_slug/base/**.

## Empty-path protocol

If a listed path is empty (path missing, zero files, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search in-repo `NN_slug/base/` first, then ask for a local path.
3. **Confirm with the user** before changing `registry.yaml`.

Never invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (the five seat rows + fine `mounts:`).
2. Resolve each fine id against `source: my-skills` (registry path; `NN_slug/base/` except `05_manuscript/qc/check-reporting/`). Retired ids (`legacy_aliases.yaml` only) are not on the menu.
3. If that path is empty or missing -> empty-path protocol.
4. Evaluate capability, boundaries, dependencies, and overlap.
5. After approval the registry status becomes `MOUNTED`. Update `registry.yaml` only (no generated mirror).
