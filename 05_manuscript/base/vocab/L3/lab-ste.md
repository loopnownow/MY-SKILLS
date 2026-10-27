## L3 specialty terms (merged)

# L3 specialty terms (pointer)

**Specialty nouns** (disease names, anatomy-specific labels, study-unique endpoints, named devices/software) live in:
1. Lab-STE default term-lock in this folder (`term-lock-default.tsv`) + per-project lock tables under the study folder
2. Per-project glossary under the study folder (when present)

Do **not** dump specialty nouns into L2 `approved-en.tsv`.

**L2 (not L3):** sequence names used as methods language; AUC / HR / OR and shared stats phrasing — see `../README.md`.


---

## Lab-STE — pointer + reusable rules

**Skill SSOT (method):** this file + `lab-ste-spec-digest.md` + `lexicons/` + `term-lock-default.tsv`.
**Approved EN lexicon:** `../L2/approved-en.tsv` (+ lemmas; hash-matched at absorb).
**Live method SSOT:** this folder (`lab-ste.md` + `lab-ste-spec-digest.md` + lexicons).
**Full SPEC / config / tools / HTML park** (`_library\lab-ste` retired 2026-10-23): `{doc_lab_ste}` (= durable skill-harvest-sources `library-methods-20261023\lab-ste`). Older park copy may also exist under `{DEL}\_by-project\0doc-library-methods-20261023\lab-ste\`.
**Spec version at absorb:** 0.2.1.
**Not a Gate:** Lab-STE does not enter `00_orchestrator/gates.md`. Open it only when polishing Methods English, writing Chinese manuscript comments (稿面批注), or tuning controllable-language checks.

### What lives where (after absorb)

| Asset | Location |
|---|---|
| Everyday rules + overrides | this `lab-ste.md` |
| Rule-ID index / profiles | `lab-ste-spec-digest.md` |
| `lexicons/*.tsv` | `L3/lexicons/` (vendored — small) |
| `term-lock-default.tsv` | `L3/term-lock-default.tsv` |
| `approved-en.tsv` | `L2/approved-en.tsv` (already mirrored) |
| Full SPEC + `config.yaml` + CHANGELOG | park / `_bank` durable only |
| `tools/` + `spec.html` | park / durable only — **do not** vendor into MY-SKILLS |

Project term-lock tables stay with each study folder. Per-project specialty nouns never enter L2.

### Standing overrides (05 / 06 win)

These already live in MY-SKILLS and **must not** be flipped by Lab-STE defaults:

- Methods voice stays **conventional passive** (Aitor / `route.md` / `05_manuscript/base/vocab/L1/sci-overrides.md`). Lab-STE's `EN-V01` default is active; when writing SCI Methods here, treat the on-disk profile as `methods_voice: conventional_passive`.
- Prose comparisons: **Compared** not Relative; metric names like `relCBF` / relative CBF stay (`05_manuscript/base/vocab/L1/ban-phrases.md`).
- **attenuated** banned; imaging noun **attenuation** stays.
- Split names use **set** (`training` / `test` / `validation set`), never rewrite set→group (`voice-portrait.md`).
- Short sentences, inside continuous paragraphs (`voice-portrait.md`).
- Track Changes: Aitee owns; Lee marks/comments only.
- Do not overwrite corresponding-author / funding / ethics defaults on an existing `.docx` (`06_review/advanced/word-edit.md`).
- Hard ban table and process/placeholder bans stay in `05_manuscript/base/vocab/L1/ban-phrases.md` (source of truth for English ban words).

### Reusable rules (new relative to prior advanced files)

#### Conflict order

When Lab-STE readability or de-AI checks collide with locked content:

1. Term lock, numerics, statistics, citations — do not change.
2. Factual accuracy — rewrite must not flip meaning or negation.
3. STE readability.
4. de-AI frequency rules.

Registered terms may repeat; unregistered nouns should not be swapped for unlisted near-synonyms just to "sound varied."

#### Vocabulary layers (pointer)

| Layer | On disk | What goes there |
|---|---|---|
| Approved general lexicon | `approved-en.tsv` | Function words, general operation/review verbs |
| Default lock template | `term-lock-default.tsv` | Domain-general nouns + general descriptive stats (mean/median) |
| Project term lock | each project's own table | Disease, sequence, named metrics (AUC/HR/OR), software, devices |

Specialty English never enters the approved lexicon. Admission test: would any field use this as an operation/review word? If no → lock table, not approved lexicon.

#### English Methods habits (profile `manuscript-methods-en`)

Use with the standing Methods-passive override above.

- One fact or one step per sentence; prefer short step sentences.
- Prefer verbs over `perform/conduct/carry out + noun` nominalizations (`Features were extracted.` not `We performed an extraction of features.`).
- Do not let bare `It` / `This` / `These` subject a sentence without a unique noun antecedent; repeat the noun.
- Keep noun stacks short; prefer `of` structures over long pre-modifier chains.
- Same subsection: do not mix past-tense procedure verbs with present-tense procedure verbs (Figure N shows may stay present when the house allows).
- Prefer one subordinate clause; avoid stacked non-restrictive `which`.

Numeric caps (words/sentence, passive ratio, etc.) live in parked `config.yaml` (see `lab-ste-spec-digest.md`) — do not hard-code a second copy here.

#### Chinese habits (批注 / LLM reply)

- One fact per sentence; avoid long comma chains.
- Prefer verbs: `提取特征` not `进行特征提取` (and similar `进行/开展/实施/做出 + verbal noun`).
- Quantify hedges: replace bare `较大/明显/一定程度/较好` with a number or named comparator (except stats terms such as relative risk).
- Cut empty four-character / stock phrases in comments (`至关重要`, `应运而生`, `综上所述` as empty openers, …). Full tables: `lexicons/hedge-zh.tsv`, `idiom-zh.tsv`, `nominalization-zh.tsv`, `de-ai-zh.tsv` (this folder).
- Bare `该/其/此/这` need a unique antecedent; otherwise repeat the noun.

#### Chinese manuscript-comment (稿面批注) five slots → 06

Face comments (Word author **A**) use the five-slot habit in `06_review/advanced/review.md` (CM-01). Journal English envelope stays `Lines n–m: + defect + Please…` in `06_review/advanced/review.md`. Lab-STE does not change the Word author field.

#### Profiles (when to open the full SPEC)

| Profile | Use |
|---|---|
| `manuscript-methods-en` | English Methods controllable language (with passive override) |
| `review-comment-zh` | Chinese manuscript-comment (稿面批注) five slots |
| `llm-reply-zh` | Chinese LLM replies — format / stock phrases first (on disk; optional) |
| `manuscript-id-en` | I/D readability + de-AI; no approved-lexicon coverage force |

### Related advanced files

- de-AI load order: `route.md` → `05_manuscript/base/vocab/L1/ban-phrases.md` / `05_manuscript/base/vocab/L1/patterns.md` / `05_manuscript/base/vocab/L1/sci-overrides.md`
- Voice / set / short sentence: `voice-portrait.md`
- Comment delivery / author A: `06_review/advanced/word-edit.md`, `06_review/advanced/review.md` §0
