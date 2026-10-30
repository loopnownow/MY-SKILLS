# 07_response/base - thin contracts for 07

Response-letter fine IDs live here (moved from `06_review/base/` on 2026-10-17 for symmetry with 06). The packs carry scope, bans, mode names, and load order; the letter voice, opener templates, and resolution protocol are `07_response/advanced/response.md`.

| Fine id | Path | Role |
|---|---|---|
| `revise` | `revise/` | Point-by-point structure |
| `tighten-response` | `tighten-response/` | Tightening / anti-accretion; on-demand tone-polish |

Former fine id `response-tone-polisher` was absorbed into `tighten-response` on 2026-10-25 (legacy alias). Do not recreate a `response-tone-polisher/` directory here. Structure stays `revise`.

Routing table (decision-type × task-mode): [`routing.md`](routing.md). Does not move ownership off Aitee.

**Flow:** base thin first pass -> 00 QC -> **07 advanced** revise loop and final authority.

Review / re-review bodies stay under `06_review/base/`.
