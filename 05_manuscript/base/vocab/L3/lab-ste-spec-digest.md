# lab-ste-spec-digest

**Absorbed:** 2026-10-23 thin index from `_library/lab-ste/` (SPEC + config + CHANGELOG).
**Full narrative/examples:** durable/park only — do not re-vendor `Lab-STE-SPEC.md` / `spec.html` / `tools/`.
**Version on absorb:** 0.2.1
**Everyday rules:** `lab-ste.md` (same folder). **Lexicons:** `lexicons/*.tsv` + `term-lock-default.tsv` (vendored — small). **Approved EN:** `../../L2/approved-en.tsv` (hash-matched to former disk SSOT).

## Live pointers (after move)

| Role | Path |
|---|---|
| Durable full tree | `{doc_root}\_corpus\skill-harvest\sources\library-methods-20261023\lab-ste\` |
| Park | `{DEL}\_by-project\0doc-library-methods-20261023\lab-ste\` |
| Tools / HTML (run from park or restore) | `…\lab-ste\tools\`, `spec.html` — **not in MY-SKILLS** |

## Rule ID index

| Family | IDs |
|---|---|
| EN | EN-S01 句长 · EN-V01 语态 · EN-L01 一词一词性/一义 · EN-VB01 动词 · EN-R01 指代 · EN-N01 名词串 · EN-T01 时态 · EN-C01 从句/which |
| ZH | ZH-S01 · ZH-SUB01 · ZH-R01 · ZH-NOM01 · ZH-DE01 · ZH-BEI01 · ZH-Q01 · ZH-ID01 · ZH-TERM01 · ZH-PUN01 |
| AI | AI-L01 词汇 · AI-S01 句式 · AI-D01 篇章 · AI-F01 格式 |
| Comment | CM-01 五槽 |

## Conflict order (SPEC §8)

1. Term lock / numerics / stats / citations  
2. Factual accuracy (no meaning/negation flip)  
3. STE readability  
4. de-AI frequency  

## Profiles (`config.yaml`)

| Profile | Use |
|---|---|
| `manuscript-methods-en` | Methods EN (with house **conventional_passive** override) |
| `review-comment-zh` | 稿面批注五槽 |
| `llm-reply-zh` | Chinese LLM reply hygiene |
| `manuscript-id-en` | I/D readability + de-AI (no approved-lexicon coverage force) |

Numeric thresholds stay in parked `config.yaml` — do not hard-code a second copy in skills (see `lab-ste.md`).

## Standing overrides (unchanged)

05/06 house rules win over Lab-STE defaults — listed in `lab-ste.md` (Methods passive, Compared/set/attenuation bans, Track Changes ownership, L1 ban table SSOT).

## Not absorbed into skills

- `tools/*.py`, `spec.html`, full SPEC example bodies
- Per-project term-lock tables (stay with studies)
