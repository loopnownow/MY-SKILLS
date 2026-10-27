# Index · selected this run · loaded this run

- **Bodies:** in-repo `NN_slug/base/` (`source: my-skills`).
- **Registry `LIVE`:** catalog-approved and session-selectable. Not the same as selected.
- **`session_picked_fine_ids`:** selected this run.
- **Active:** actually loaded this run.
- **Advertised:** `00`–`07` only.
- **Registry:** routing index only. GitHub MY-SKILLS is the framework + body source of truth.

## Resolve (in-repo)

00 owns path resolve (registry), gates provenance, and owns base -> QC -> advanced/top flow.

1. **Resolve** fine id -> in-repo path via `registry.yaml` (`source: my-skills`).
2. **Load** from the registry path (`NN_slug/base/...`, or `05_manuscript/qc/check-reporting/` for `check-reporting`; git working tree = `{skills_runtime}`).
3. **Pick** -- user multi-selects fine ids (ask-each-run).
4. **Post-pick QC** -- loaded bytes match registry source + path.

**Stale policy:** pull/sync MY-SKILLS when bodies change.

**G0 handoff:** if an in-repo body path is missing, fail back to 00 (empty-path protocol).

## Post-merge deploy sync

- As of 2026-10-23, `{SKILLS}` / `{skills_runtime}` **is** the GitHub working copy `{skills_git}` (no separate `.grok\skills` tree). After merge: `git pull` on that clone; do **not** copy into a second runtime folder.
- Still: no whole-tree blind overwrite of unrelated paths, and no editing live skill bodies outside PR/merge.
- Acceptance: working tree on main matches the merged commit.
