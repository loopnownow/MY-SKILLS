# L2 personal writing phrases (owner's recurring usage)

Personal L2 layer. The lab-wide phrase bank stays in `05_manuscript/base/vocab/L2/preferred.md`;
this file records only expressions **this owner** reuses, with the count that
justifies each entry. Base wins on anything the two disagree about; nothing here
may contradict `05_manuscript/personal/Aitor-format.md` or `05_manuscript/personal/voice-portrait.md`.

## What may enter this file

| Bucket | Goes here? | Where it actually lives |
|---|---|---|
| Structural wording (sentence families, limitations skeleton, closers, connectors) | yes | this file, with counts |
| Domain nouns (disease, sequence, device, named metric) | no | `05_manuscript/base/vocab/L3/term-lock-default.tsv` |
| Banned words | no | `05_manuscript/base/vocab/L1/ban-terms.yaml` (the linter reads that file only) |

## Tiers

| Tier | Rule | Handling |
|---|---|---|
| A | ≥3 papers **and** ≥5 occurrences, and still usable in the next manuscript | recommend and reuse |
| B | below the A line, or semantically identical to a base L2 row | record, do not push |
| C | single-paper noun, one-off number, someone else's sentence | discard |
| **Locked** | listed in `05_manuscript/base/vocab/L1/ban-terms.yaml`, or fixed by `05_manuscript/personal/Aitor-format.md` | keep, tag `格式锁` / `禁词替代`; **frequency never decides** |

A row without a filled `Count` / `Docs` is an unverified habit claim. Keep it out of
Tier A until the harvest fills the columns.

**Frequency never overrides a lock.** Two cases where a low or zero count must not
be read as evidence against the row:

- `could assist [task]` is the mandated replacement for the banned
  `suggesting its potential` (`05_manuscript/base/vocab/L1/ban-phrases.md`). Zero
  hits means the corpus predates the ban, not that the row is wrong.
- `95% CI: X–X`, `n = N`, `training set` / `test set` and the Table 1 shape are
  `Aitor-format.md` hard format, not habits. Statistics cannot retire them.

Conversely, a high count never unlocks a banned word: `novel` may be frequent in
old drafts, and `ban-terms.yaml` still governs.

## How the numbers get filled

Counts come from the **paragraph layer** (`paras.jsonl`), not from the review or
reply lanes: those hold other people's manuscripts and the owner's letters, and
their wording does not belong in this table.

```text
python3 {skills_git}\05_manuscript\personal\vocab\scripts\harvest_write_phrases.py --bank "{doc_review_bank}\bank\paras.jsonl" --limit 80
python3 ... --bank "{doc_review_bank}\bank\paras.jsonl" --execute --out <temp>.md
python3 ... --bank "{doc_review_bank}\bank\paras.jsonl" --execute --out <temp>.md
```

The script is read-only on the bank, offline, and prints a table in this file's
column order. It never edits this file. Paste the rows, then apply the tiers.

What it counts:

- **Paragraphs only.** `in_table` and `in_textbox` rows are skipped, and a
  paragraph must clear 60 characters (20 for Chinese) to count.
- **Section-aware.** `section_idx` maps to Abstract / Introduction / Methods /
  Results / Discussion, and the `主要章节` column reports where a phrase lives. A
  phrase that only appears in Discussion is not an Abstract template.
- **Sentence-edge windows** (2–6 words English, 2–10 characters Chinese), because
  a sentence's sliding windows all carry the same count and would bury the table
  in fragments. Overlapping head/tail windows in a short sentence are emitted
  once; a shorter span is dropped when a longer one with an identical count
  contains it.
- **次数 and 篇数 are separate series.** 次数 counts occurrences, 篇数 counts
  distinct manuscripts. Never compare them as one number.
- `--bans` flags rows that `05_manuscript/base/vocab/L1/ban-terms.yaml` already
  forbids; it flags, it does not delete.

Known limits (recorded, not hidden): Chinese is cut by character, so a window can
start mid-compound (`比较这些指标`). A leading-function-character filter removes
the worst of it, but the Chinese rows still need a human pass. Use
`--lang en` when only the English habits are wanted.

## Abstract

### Purpose sentence

Three families are all in use. Do not collapse to one.

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| This study aimed to … | 9 | 9 | Abstract Objective / Intro closing | family 1 (base L2 §1) |
| The aim of this study was to … | 11 | 7 | Abstract Objective | family 2 |
| To investigate / explore / evaluate … | 267 | 70 | Abstract Objective | family 3, bare infinitive |

### Methods and results

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| The AUC was X (95% CI: X–X) in the training set and X (95% CI: X–X) in the test set | 0 | 0 | Abstract Results | report both sides; lock: 格式锁; frequency does not decide |

### Conclusion

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| could assist [task] | 0 | 0 | Abstract Conclusion | replaces the 0-hit `suggesting its potential`; lock: 禁词替代; frequency does not decide |
| may provide / may optimize [workflow] | 2 | 2 | Abstract Conclusion | **B** — calibrated, no absolute claim |

## Introduction

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| This study aimed to … using [method] in [population] | 2 | 2 | ¶ aim, no citations | **B** — |

## Methods

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| Patients were randomly divided into a training set (n = N) and a test set (n = N) | 0 | 0 | Study population | body split is training / test; lock: 格式锁; frequency does not decide |

## Results

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| The nomogram exhibited good discrimination in the training set (AUC X [95% CI, X–X]) | 0 | 0 | Model performance | lock: 格式锁; frequency does not decide |

## Discussion

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| In this study, we … | 22 | 17 | ¶1 opener | workhorse (base L2 §2) |
| This finding is consistent with a previous study by [Author] et al. | 1 | 1 | ¶2 literature | **B** — |
| may reflect / might be related to [mechanism] | 15 | 12 | ¶3 mechanism | one hedge, never stacked |

## Limitations and closer

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| This study has several limitations. First, … Second, … | 2 | 2 | own paragraph | **B** — First… Second…, no CYA essay |
| Future research should … | 13 | 8 | last sentence of Limitations | dominant closer (base L2 §5) |
| Future studies should … | 3 | 3 | same slot | **B** — interchangeable variant |

## Conclusion

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| In conclusion, … | 26 | 25 | Conclusion section | standard opener |
| In summary, … | 2 | 2 | Conclusion section | **B** — minority alternate |

## Connectors and hedge ladder

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| Therefore / Thus | 180 | 54 | after a concrete observation | one per paragraph, only where logic turns |
| This finding is consistent with … | 1 | 1 | Discussion ¶2 | **B** — agreement |
| in contrast | 17 | 8 | Discussion ¶2 | disagreement; more common than `in line with` |
| may / might / could + suggest | 1 | 1 | Discussion only | **B** — Results stay unhedged |

## Review replies (07 lane)

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|
| Thank you for the suggestion / comments / inquiry | 612 | 30 | per-point opener | noun follows the reviewer's tone; **07 layer, not for 05 tables** |
| We clarify that … | 1 | 1 | action sentence | **B** — for questions, not changes; **07 layer, not for 05 tables** |

## Chinese manuscript comments (marginal notes)

| Phrase | Count | Docs | Where | Note |
|---|---:|---:|---|---|

(every row scored 0; see "Unverified / to rewrite")


## Unverified / to rewrite (0 hits)

These rows scored 0 and carry no lock. `Count / Docs` stay blank: rewrite the wording or delete the row; do not treat it as habit evidence. Locked rows (format or ban replacement) never appear here.

- `A total of N patients … were retrospectively enrolled` — 0 hits; longest literal span "were retrospectively enrolled" occurs 2 times
- `However, to our knowledge, few studies have …` — 0 hits; longest literal span "however, to our knowledge, few studies have" occurs 0 times
- `The accurate preoperative prediction of X remains challenging` — 0 hits; longest literal span "accurate preoperative prediction" occurs 0 times
- `Regions of interest were manually delineated … blinded to clinical information` — 0 hits; longest literal span "regions of interest were manually delineated" occurs 0 times
- `Features were extracted using pyradiomics (version X.X)` — 0 hits; longest literal span "features were extracted using pyradiomics (version" occurs 0 times
- `No significant difference was observed in X between A and B (P = X)` — 0 hits; longest literal span "no significant difference was observed" occurs 2 times
- `In contrast, [Author] et al. reported X, which may be attributed to …` — 0 hits; longest literal span "may be attributed" occurs 1 times
- `We have revised the manuscript accordingly` — 0 hits; longest literal span "we have revised the manuscript accordingly" occurs 0 times
- `建议补充……` (lit. "suggest adding …") — 0 hits; longest literal span "建议补充" occurs 0 times
- `请在讨论里说明……` (lit. "please explain in the Discussion …") — 0 hits; longest literal span "请在讨论里说明" occurs 0 times
- `样本量偏小，建议……` (lit. "sample size is small; suggest …") — 0 hits; longest literal span "样本量偏小，建议" occurs 0 times

## Not used (pointers only)

Banned words are not restated here; the single authority is
`05_manuscript/base/vocab/L1/ban-terms.yaml` with the human table in
`05_manuscript/base/vocab/L1/ban-phrases.md`. The four 2026-08-29 reversals
(`novel`, `notably`, `interestingly`, `importantly`) are banned regardless of how
often the bank counts them.

## Provenance

- Owner habits already on file: `05_manuscript/personal/voice-portrait.md`,
  `05_manuscript/personal/process/polisher-sections.md`,
  `05_manuscript/personal/references/bank-voice.md`.
- Bank bulk bodies stay on disk and are never vendored here.
