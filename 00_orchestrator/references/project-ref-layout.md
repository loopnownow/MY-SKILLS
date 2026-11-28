<!-- rules-mirror-of: project-ref-layout.md src-sha256-8: 36f7810d -->
# Project `ref/` layout — runtime index

**Owner:** `00_orchestrator`.
**SSOT:** `{RULES}\project-ref-layout.md`（中文，权威副本）. This page is an index only: it says which section to open. It does not restate rule text. On any conflict the SSOT wins.

Read the SSOT before writing into a project `ref/`.

| Need | Section in the SSOT |
|---|---|
| What must stay at `ref/` root | `{RULES}\project-ref-layout.md` 「根目录不变量（勿挪位）」 |
| Which subfolder each artifact goes in | `{RULES}\project-ref-layout.md` 「子文件夹地图」 |
| Results / scratch area | `{RULES}\project-ref-layout.md` 「三区 / 临时结果区」 |
| Submission packs (accepted vs not) | `{RULES}\manuscript-docx.md` 「投稿包」 |
| Manuscript names (`Manuscript_` / `Comments_` / `Response_` / `Supplementary_`, `V*` / `R*` / `P*`) | `{RULES}\manuscript-docx.md` 「SCI 稿件文件名」 |
| Journal-specific format copy (generic 通稿 only at project root; format copy in `ref/submission-*`) | `{RULES}\manuscript-docx.md` 「目标刊格式版（母本不动，按刊另存）」 |
| Non-contract edit suffixes | `{RULES}\manuscript-docx.md` 「非契约编辑后缀稿」 |
| `-org` pre-edit originals | `{RULES}\project-ref-layout.md` 「编辑前原件」 |
| Detecting 城城 hand edits before overwrite | `{RULES}\manuscript-docx.md` 「城城手改识别」 |
| Data ledger table (D-1) | `{RULES}\project-ref-layout.md` 「数据底表（D-1）」 |
| What must survive an accepted project | `{RULES}\project-ref-layout.md` 「accepted 收工硬留」 |
| Cleanup tiers | `{RULES}\project-ref-layout.md` 「Cleanup」 |
| Skip / idempotent rules (read the ledger before re-running) | `{RULES}\project-ref-layout.md` 「跳过 / 幂等规则」 |
| What this contract deliberately does not cover | `{RULES}\project-ref-layout.md` 「本契约不做的事」 |

## Boundary

- This page exists so a skill can find the right section fast. It is not a rule source and must not grow a second copy of the map.
- New layout detail belongs in `{RULES}\project-ref-layout.md`; manuscript names, submission packs, and journal-format copies belong in `{RULES}\manuscript-docx.md`. Cite by **section title**, not by number.
- The rules layer was renumbered in 2026-11 (old §5.1 → §3 交付与清理, old §5.3 → 当时 `{RULES}\del-and-harvest.md`，现行 `{RULES}\zone-docs.md` §1 / §3，`{DEL}` 落点见 `{RULES}\zone-del.md`）。
