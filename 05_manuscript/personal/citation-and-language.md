# Citation and language rules

## Citation

1. **Style:** Vancouver / NLM.  
2. **DOI mandatory** for every reference entry. Format: `doi:10.xxxx/xxxxx.`  
3. Vancouver order of first appearance. Do not cite every sentence. Neighbouring sentences that share one source: cite once. Do not reuse an earlier number after a later number has entered (no `[1]` after `[3]`). Intro last paragraph and Discussion first paragraph: **no citations**. Methods: **no citations**. Quotas and placement: **`Aitor-format.md`**. Avoid `[1–3]` clusters. When **revising an existing** manuscript, reorder in-text numbers to appearance order against the reference list. Duplicate entries in the list: replace the duplicate with an already-verified substitute (author A). Checking already-written I/D: do not delete genuine refs to hit 10–15 / 10–15-new; note over-quota only.  
5. **Methods does not cite.** TRIPOD, Riley, IBSI, and Monti belong in the Introduction or Discussion if cited.  
6. Keep ledger CSV: `id, section, citation_text, doi, verified (Y/N)`.  
7. No DOI → replace source or drop claim.  
8. Functional self-citation only: *as previously shown for whole-nodule radiomics [n].*

## Citation hygiene (pre-submit)

Check ids live in `pre-submit-consistency.md`. Apply them on every reference pass. call/require 03 citation-verify — do not self-certify lit (`03_research/personal/citation-verify.md`). Aitee does not sign the claim→ref table.

9. **Consecutive same paper** (`consecutive_same_cite`). Do not cite the same work in consecutive sentences unless the second sentence adds a distinct claim that work supports. Shared neighbouring sentences cite once.
10. **Claim matches the source** (`claim_matches_source`). Population, modality, and direction of effect in the sentence are claims the cited work makes. A mismatch is weaken or replace (`evidence-request.md`), not a decorative number.
11. **No cross-manuscript copy** (`no_unverified_cross_copy`). A DOI, author list, year, or volume taken from another manuscript is not verification. Check the cited work (`03_research` / verify-refs) before the entry stays.
12. **Year and volume from the source** (`year_volume_from_source`). A year or volume correction is applied only after the source confirms it. An unverified correction stays a Word comment (author **A**).
13. **Introduction opening.** When a verified source exists, the opening paragraph cites it. Element 6 (aim / hypothesis) and the Discussion first paragraph stay uncited (`Aitor-format.md`).

## Language (李瀛 + this workflow)

| Rule | Do | Don't |
|------|----|-------|
| Sentence length | Prefer ≤55 English words | Long nested slogans |
| Dashes | Use periods or clauses; math minus `−` in formulas only | Em dash `—`, Chinese `——`, prose en dash stacks |
| Ranges | Size/time: `4 to 12 mm`. CI: `Aitor-format.md` (`95% CI: X–X`) | Em dash; CI written with `to` |
| Numbers | Next to claim | Orphan AUC without set name |
| Novelty | *few studies* / *remains limited* | *novel* / *first* / *groundbreaking* |
| Performance | *higher AUC* / *outperformed* | *superior* / *robust* |
| Comparison | *Compared with* / *Compared to* | *Relative* / *relative to* as a comparison word |
| Results | Past tense, no empty hedge | *may suggest* in Results |
| Discussion | demonstrated / suggested / may | Over-causal *proved that* |

Prose comparisons use *Compared*. Do not rewrite technical metric names (*relative CBF*, *relCBF*, and other "relative …" measures) unless the surrounding prose uses *relative* as a comparison word.

## Banned filler (English)

delve, landscape, pivotal, robust, comprehensive, leverage, seamless, game-changer, groundbreaking, state-of-the-art, interestingly, surprisingly, remarkably, paradigm, tapestry, attenuated.

## Chinese side notes (if bilingual abstract)

少用“值得注意的是 / 综上所述 / 全面系统”。数字贴断言。
