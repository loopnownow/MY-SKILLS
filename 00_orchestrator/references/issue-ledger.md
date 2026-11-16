# Cross-stage issue ledger (00)

Standing problem register for one project (跨阶段问题台账). 00 owns the schema; seats `02` / `03` / `05` / `06` / `07` write and update rows. Do not open a second ledger in another skill. This is not a new gate id, and it does not replace `defects[]`, `CITATION_AUDIT`, `ref/manuscript-revision.md`, or `templates/rr-traceability.md`.

## Disk path

`ref/review/issue-ledger.yaml`, created on the first issue (copy [`templates/issue-ledger.yaml`](../templates/issue-ledger.yaml)). Do not pre-create an empty file or folder.

## One problem, one row

Search the file before adding a row. The same problem keeps one `id` across stages; later seats update `status`, `evidence`, and `resolution`. Do not open a duplicate because a later gate saw the same break.

## When to register

Register or update when:

- a gate FAIL is still open at the end of the run
- `defects[].status` becomes `unresolved` after 3 recoveries
- a specialist or the owner names a problem that will outlive this run

Do not register a fail that is recovered in the same run.

## Status

| status | meaning |
|---|---|
| `open` | not yet being worked |
| `in_progress` | the responsible seat is working it |
| `resolved` | actually fixed; `resolution` points to the fix |
| `accepted` | the limitation is kept and must be disclosed in the manuscript; not a silent close |
| `rejected` | the finding itself is declined (false finding, or the owner declined it); `resolution` holds the reason |

`accepted` is not `resolved`. Do not mark an unfixed problem `resolved`.

## Fields

See the template. Required: `id`, `first_detected`, `category`, `severity`, `summary`, `evidence`, `status`, `updated`. Optional: `first_gate`, `blocking`, `blocking_gate`, `resolution`.

- `id`: `ISS-001`, `ISS-002`, … in that project. Do not reuse a closed id for a different problem.
- `first_detected` / `blocking`: a coarse id (`02_data-processing` / `03_research` / `05_manuscript` / `06_review` / `07_response`) or a live fine id.
- `category`: `data` / `methods` / `statistics` / `writing` / `citation` / `review` / `response`.
- `severity`: `critical` / `major` / `minor`.
- `summary` / `evidence` / `resolution`: no PHI; no invented n, AUC, PMID, or ethics numbers. Evidence is a path, a table or figure id, a comment, a ledger key, or a `defects[]` id — not a pasted dataset.

`data` and `statistics` map to seat `02` (there is no seat `04`). `review` maps to `06` findings; `response` maps to `07` (response letters do not enter `06`).

## QC close

00 reports `open`, `in_progress`, and `accepted` issues at close. Do not write `pipeline.stage: done` while any `critical` issue is `open` or `in_progress`, unless the owner stops the run. `accepted` / `resolved` / `rejected` do not by themselves block `done`. Open `major` / `minor` issues are reported, not auto-blocking.

Specialized ledgers stay where they are; this file may point to them as `evidence`.
