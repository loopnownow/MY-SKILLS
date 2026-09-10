# AIM, author instructions, and further checks

Use this file only in phase 2, after the user has confirmed 备选杂志.

Phase 1 forbids live lookups of AIM, author instructions, and APC.

Blacklist remains mounted in both phases: PLoS One, Scientific Reports, MEDICINE (LWW Baltimore).

## Live lookups (confirmed titles only)

Search

- `"{journal}" aims and scope`
- `"{journal}" instructions for authors`
- `"{journal}" article processing charge` or `APC`
- `"{journal}" article types`

Record article types, exclusions, word limits, abstract structure, reference style, reporting guideline, ethics, data policy, APC or subscription path, reviewer suggestions, preprint policy.

If the official page cannot be opened, write 未核实. Never invent a word limit or fee.

## Manuscript cleanup after one target is chosen

Title length; structured abstract headings; keywords; IMRAD extras; reference style; figure/table files; EQUATOR checklist; ethics ID; consent; registration; funding and COI; CRediT; ORCID; cover letter; AI statement if required.

## Further checks before delivery

Quote AIM against the paper aim. Confirm article type. Restate IF and layer. Mark APC as official or 未核实. Strip identifiers. Ask about MDPI/Frontiers unit bans only if those titles were confirmed in phase 1.

## Phase-2 short HTML (user delivery)

After confirmed 备选, deliver **one short HTML table per paper** (not a long “分刊详情” dump).

| Column | Rule |
|---|---|
| 期刊全称 | Confirmed title |
| JCR分区 | Display only — do not persist |
| 影响因子 | Display only — do not persist |
| 年发文量 | Display only — do not persist |
| 投稿网址/作者须知 | **Same cell/column**; show **full URLs** for portal and for author instructions (labels OK as long as the URL text is visible) |

**Omit from the short table:** ISO/ISO缩写, OA, 置信度, 「分刊详情（可勾选阅读）」, **APC**.

APC / deep AIM notes may still be researched for agent use (`Live lookups` above) or a separate note if the user asks — they are **not** columns in the short user HTML.

Persist portal submission URLs to `submission-urls.csv` only. Prefer dependency-free HTML craft (`00_orchestrator/references/html-visual-design.md` when present).
