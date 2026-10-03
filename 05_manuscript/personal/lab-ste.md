# Lab-STE — pointer + reusable rules

**Disk SSOT (do not vendor):** `D:\0Grok\0doc\04_实验室参考\lab-ste\`  
**Spec version on disk:** see that folder's `config.yaml` / `Lab-STE-SPEC.md` / `CHANGELOG.md` (currently 0.2.1).  
**Not a Gate:** Lab-STE does not enter `00_orchestrator/gates.md`. Open it only when polishing Methods English, writing Chinese 稿面批注, or tuning controllable-language checks.

## What lives on disk (pointer only)

| Path under lab-ste | Role |
|---|---|
| `Lab-STE-SPEC.md` | Full rule IDs (EN-*/ZH-*/AI-*/CM-01), examples, conflict order |
| `config.yaml` | Thresholds, profiles, comment_schema numbers |
| `approved-en.tsv` + `approved-en.lemmas.txt` | English approved general lexicon (no specialty English) |
| `term-lock-default.tsv` | Domain-general lock template (patient, feature, slice, reader, …) |
| `lexicons/*.tsv` | de-AI / nominalization / hedge / idiom tables |
| `tools/` | Checker and HTML builder — run from disk; do not copy into MY-SKILLS |
| `规范.html` | Generated human view — regenerate on disk, do not vendor |

**Do not** copy the TSV dictionaries, Python tools, or HTML into this repo. Skills keep rules + pointers (`ARCHITECTURE.md` Lab workspace SSOT).

## Standing overrides (05 / 06 win)

These already live in MY-SKILLS and **must not** be flipped by Lab-STE defaults:

- Methods voice stays **conventional passive** (Ying Li / `de-ai.md` / `stop-slop-core.md`). Lab-STE's `EN-V01` default is active; when writing SCI Methods here, treat the on-disk profile as `methods_voice: conventional_passive`.
- Prose comparisons: **Compared** not Relative; metric names like `relCBF` / relative CBF stay (`forbidden-phrases.md`).
- **attenuated** banned; imaging noun **attenuation** stays.
- Split names use **set** (`training` / `test` / `validation set`), never rewrite set→group (`voice-portrait.md`).
- Short sentences, inside continuous paragraphs (`voice-portrait.md`).
- Track Changes: Aitee owns; Lee marks/comments only.
- Do not overwrite corresponding-author / funding / ethics defaults on an existing `.docx` (`word-edit-rules.md`).
- Hard ban table and process/placeholder bans stay in `forbidden-phrases.md` (source of truth for English ban words).

## Reusable rules (new relative to prior personal files)

### Conflict order

When Lab-STE readability or de-AI checks collide with locked content:

1. Term lock, numerics, statistics, citations — do not change.
2. Factual accuracy — rewrite must not flip meaning or negation.
3. STE readability.
4. de-AI frequency rules.

Registered terms may repeat; unregistered nouns should not be swapped for unlisted near-synonyms just to "sound varied."

### Vocabulary layers (pointer)

| Layer | On disk | What goes there |
|---|---|---|
| Approved general lexicon | `approved-en.tsv` | Function words, general operation/review verbs |
| Default lock template | `term-lock-default.tsv` | Domain-general nouns + general descriptive stats (mean/median) |
| Project term lock | each project's own table | Disease, sequence, named metrics (AUC/HR/OR), software, devices |

Specialty English never enters the approved lexicon. Admission test: would any field use this as an operation/review word? If no → lock table, not approved lexicon.

### English Methods habits (profile `manuscript-methods-en`)

Use with the standing Methods-passive override above.

- One fact or one step per sentence; prefer short step sentences.
- Prefer verbs over `perform/conduct/carry out + noun` nominalizations (`Features were extracted.` not `We performed an extraction of features.`).
- Do not let bare `It` / `This` / `These` subject a sentence without a unique noun antecedent; repeat the noun.
- Keep noun stacks short; prefer `of` structures over long pre-modifier chains.
- Same subsection: do not mix past-tense procedure verbs with present-tense procedure verbs (Figure N shows may stay present when the house allows).
- Prefer one subordinate clause; avoid stacked non-restrictive `which`.

Numeric caps (words/sentence, passive ratio, etc.) live only in on-disk `config.yaml` — do not hard-code a second copy here.

### Chinese habits (批注 / LLM reply)

- One fact per sentence; avoid long comma chains.
- Prefer verbs: `提取特征` not `进行特征提取` (and similar `进行/开展/实施/做出 + verbal noun`).
- Quantify hedges: replace bare `较大/明显/一定程度/较好` with a number or named comparator (统计术语如相对危险度除外).
- Cut empty 四字格 / 套话 in comments (`至关重要`, `应运而生`, `综上所述` as empty openers, …). Full tables: `lexicons/hedge-zh.tsv`, `idiom-zh.tsv`, `nominalization-zh.tsv`, `de-ai-zh.tsv`.
- Bare `该/其/此/这` need a unique antecedent; otherwise repeat the noun.

### Chinese 稿面批注 five slots → 06

Face comments (Word author **A**) use the five-slot habit in `06_review/personal/review-comment-habits.md` (CM-01). Journal English envelope stays `Lines n–m: + defect + Please…` in `personal-review-style.md`. Lab-STE does not change the Word author field.

### Profiles (when to open the full SPEC)

| Profile | Use |
|---|---|
| `manuscript-methods-en` | English Methods controllable language (with passive override) |
| `review-comment-zh` | Chinese 稿面批注 five slots |
| `llm-reply-zh` | Chinese LLM replies — format / 套话 first (on disk; optional) |
| `manuscript-id-en` | I/D readability + de-AI; no approved-lexicon coverage force |

## Related personal files

- de-AI load order: `de-ai.md` → `forbidden-phrases.md` / `ai-isms-checklist.md` / `stop-slop-core.md`
- Voice / set / short sentence: `voice-portrait.md`
- Comment delivery / author A: `06_review/personal/word-edit-rules.md`, `personal-review-style.md` §0
