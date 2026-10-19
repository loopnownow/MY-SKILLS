# Project `ref/` map

Layout contract: `00_orchestrator/references/project-ref-layout.md` (in MY-SKILLS).

## Root (keep)

- `settings.ini` — RAD/pipeline config only
- `manuscript-revision.md` — append-only main change ledger
- this `README.md`

## Subfolders

| Dir | Contents |
|---|---|
| `review/` | Per-round changelog / handoff |
| `citation/` | `CITATION_AUDIT.json` + skip notes |
| `gates/` | GATE reports, number-lock, hashes |
| `code/` | Script/path notes, patch pointers |
| `results/` | Table/figure lock notes |
| `exec/` | Optional EXECUTION wrap-ups |

## Skip (short)

- Lit: same DOI|citekey + layer + fine_id → do not re-run
- Word: do not re-polish sections logged in `manuscript-revision.md`
- Review: do not reopen a completed round without owner ask
- Never silent-skip a mandatory gate without a ledger reason
