# 06 handoff — working with other seats

| Need | Seat / skill |
|---|---|
| Manuscript Track Changes / prose | `05_manuscript` (Aitee) |
| Literature substitute / citation-verify | `03_research` (Victor) |
| Numbers / figures | `02_data-processing` |
| Tables / imaging prep | `02_data-processing` |
| Response letter / resolution | `07_response` |
| Exit QC / Gates | `00_orchestrator` |
| Local pre-submit + intro scorecard | `05_manuscript/qc/manuscript-local-qc.md` |
| Cross-manuscript / sister-paper QC | `06_review/qc/cross-manuscript-qc.md` |

Lee (06) annotates by default; does not own manuscript body TC (`word-edit.md`).

## R&R / re-review

- **Re-review = verification only** (frozen Round-1 items). Do not open a new full pre-review.
- Traceability table: `00_orchestrator/templates/rr-traceability.md` (item_id | reviewer_finding | author_claim | verified | residual).
- Topology: `00_orchestrator/runtime-flow.mmd` (`P06r` → `I45`). Response stays in `07_response` (Aitee); do not route 回复 to 06.

## Filename stems (standing)

Reviewer comments shell: `Comments_<project-slug>_V<n>.docx` (e.g. `Comments_lxf_PP_V1.docx`). `V<n>` matches the manuscript revision those comments belong to. Same family as `Manuscript_` / `Response_` / `Supplementary_`. Rules SSOT → `{RULES}/project-ref-layout.md`.

