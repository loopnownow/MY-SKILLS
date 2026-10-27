# Canonical ID Rule

Hard rule. Do not rename fine ids to match a folder.

1. `id` is the only runtime and session-pick identifier.
2. `path` is a physical location and must not be used as a fine id.
3. `label` is descriptive and must not be used for routing.
4. The coarse id **is** the execution seat and the session-pick bucket; a fine id declares no `coarse` field, its bucket is its `a_domain`.
5. `a_domain` is the execution owner.
6. One path may back several fine ids (`path_shared`). Currently no live fine id does: `batch-cohort` was absorbed into `clean-data` and survives only as an alias.
7. Renaming a physical path does not rename the fine id. Alignment runs the other way: the directory takes the fine id name (`base/<fine_id>/`, or `qc/<fine_id>/` for a seat QC body). `check-reporting` lives at `05_manuscript/qc/check-reporting/`. `tests/test_registry_contract.py` enforces directory name = fine id.
8. Renaming a fine id requires an explicit registry migration.
9. The live identity is `fine_id` / seat (`a_domain`, which is the coarse id) / `path`, plus A pack when the note names one (`find-journal` → `03_research/base/find-journal/`; `fill-protocol` → `03_research/base/fill-protocol/`). There is no separate coarse field, so a fine id cannot sit in a bucket its owner does not serve.

A path must never be used to infer an id. QC tools use `registry.yaml` `id` as the only canonical identifier. Legacy call-site aliases in `legacy_aliases.yaml` resolve old name → current `id` (for example `02-tables` → `clean-data`). Do not reverse that direction.
