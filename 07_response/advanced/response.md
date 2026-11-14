# Response letter (style + resolution)

## Structure digest (_Docs absorb 2026-10-23)

Letter skeleton + unique bans: `references/response-structure-digest.md`. Type stubs: `references/response-letter-template-digest.md`. **Do not fork** opener nouns / thanks bank — this file remains SSOT.


## Hard rules (owner 2026-10-19)

- **Do not invent** response-letter format. Follow the existing comment shell / venue template / gold layout only.
- Keep each reviewer/editor comment **verbatim and complete**. Do not simplify, paraphrase, shorten, or drop clauses.
- **Do not** add invented subheadings (no extra `Editor comment N` / thematic mini-titles unless already in the shell).
- Editing an existing `.docx` response or comments shell: use **Track Changes**; word- or sentence-level inserts only—**no** large-block overwrite.
- Typography (manuscript = comments = response): Times New Roman, 12 pt, 1.5 line spacing, paragraph before/after 0, text before/after 0, justify, LTR, **no special paragraph format**. Do not change fonts/layout unless the owner asks this turn.
- **Color overlay — Response bodies are blue (owner 2026-11-01 t1588u).** In the response letter `.docx`, the **author reply content** — the answer text under each `Response:` / `**Response:**` / reply block — must be **blue font** (standard Word blue, e.g. RGB 0,0,255 or theme `Blue`). This is a color overlay on the TNR 12 / 1.5 layout above, **not** a new format family.
- Reviewer/editor **quoted comments stay black** (default body color). Do not recolor the verbatim comment text.
- Opening *Dear Editor* letter and closing thanks stay default **black** unless the gold template already sets blue there; when ambiguous, put blue only on the per-point Response bodies.


## Part A — Response letter voice

## Package and wording hard rules

- Deliver as `.docx` named `Response_<project-slug>_R<round>.<minor>.docx` (same token as that round’s manuscript; Rules SSOT → `{RULES}/project-ref-layout.md`). Requirements read `Please …`, never `Please fix:`.
- Quote the reviewer comment in full; use past tense for changes already made.
- Do not open a resolved item with `We agree that…`. Do not write `we will…` for a change already claimed.
- `ACCEPT-*.html` only when the user names it this run. Delivery goes to the folder the user already used for the project (e.g. `{lab_root}\reviewing\<project>`).
- Each point maps to one reply row and names its location; after revision re-check page, number, sample size, and citation.

## Advanced response-letter style (from historical letters)

Source: de-duplicated bank of 42 external-review responses (Qiang lab, Aitor/Ju lab, and other groups). Skeleton and thank-you distributions only — no full-letter dumps, no unpublished results. Goal: drafted replies should read like the user wrote them.
**This file is the letter skeleton and voice source of truth** (old `mode-3-response.md` was never split out). Opener defaults to A; B is almost never used. Triage and adjudication: `07_response/base/revise/references/resolution-protocol.md`.

Disk bank (external reviews and revise replies): `{doc_glossary}\banks\`（`flattened.jsonl` + `FLATTENED.tsv`）。

### 1. Opening letter templates (default A; B almost unused)

Use the noun that fits the reviewer's tone/content (comments = observations/critique; suggestions = concrete change requests; inquiries = why/how questions).

**A. Standard (most common; mid-formal)**

```
Dear Editor and Reviewers,

Thank you for your comments / suggestions / inquiry. We have carefully revised the manuscript accordingly. Our point-by-point responses follow.
```

**B. Strengthened (almost unused; do not treat as the historical default)**

```
Dear Editor and Reviewers,

Thank you for the chance to revise our manuscript and for the insightful comments. We have addressed each point below.
```

**C. Short (no Dear line; go straight to body — short emails / one reviewer, few points)**

```
Thank you for your comments. Our responses follow.
```

**Default to A.** Measured across 42 responses: A ≈ 21; B (chance to revise / insightful comments) ≈ 0-2, almost unused; C ≈ 1. Do **not** switch to B just because of Major Revision / multiple rounds / R2 — multi-round revise still stays on A unless the user asks.

### 2. Per-point thank-you openers — by comment type

Do not write "Thank you for the suggestion" on every point. Pick by what the reviewer is **actually doing**:

| What the reviewer is doing | Opener |
|---|---|
| Suggests changing wording / method / presentation | "Thank you for the suggestion." / "Thanks for the suggestion." |
| Asks why/how; wants clarification | "Thank you for the inquiry." / "Thanks for the inquiry." |
| Observation/comment without a clear ask | "Thank you for the comment." / "We thank the reviewer for this comment." |
| Positive feedback | "Thank you for your positive feedback on..." — brief accept; no over-humility, no defense |
| Points out a **real error** (number clash, legend mismatch, spelling) | "Thank you for pointing this out." / "We apologize for..." / "Upon review, we acknowledge that..." |
| Asks for something impossible (external validation, new experiment, missing data) | First acknowledge value: "We agree/acknowledge that... is important for...", then state the boundary |
| Major methods challenge (multiple comparisons, circular analysis, sample size) | "We thank the reviewer for this comment." then a solid technical paragraph — do not skate past with small talk |

Within one letter, alternate these openers by reality; do not use one template throughout — uniform "Thank you for the suggestion" reads as AI.

### 3. Body sentence skeleton

```
Response: [thank-you]. We [revised/added/clarified/corrected] it in the [Section/Table/Figure].
"[verbatim revised or new sentence]" We added/revised it in [concrete locus, e.g. Discussion-paragraph 2 /
Table 2 / Figure 3 legend].
```

#### 3.1 Verbatim quote is mandatory

Whenever a sentence was revised or a paragraph added, **quote the new wording in the letter**. Do not stop at "we revised the sentence for clarity." Reviewers and editors must see the new sentence in the letter without hunting the body.

- One or two words only: `"X" was revised to "Y" in the text.`
- Whole sentence rewrite: `We revised it to "……"`
- New paragraph: `We added it in the text. "……"`

#### 3.2 Location citation is mandatory

Every change is followed by a locus label. Format need not be uniform, but it must be concrete and findable.

Never write only "revised accordingly" without a locus — same traceability bar as §3.2; a hard metric across this user's letters (old `response-audit-gate.md` was never split out).

#### 3.3 When you give a number, give the full set

If asked for a value, put the exact result in the letter body — do not only promise "already added to the manuscript":

Technical detail (LASSO λ, ICC cutoffs, formulas, exact *P*) should be complete; avoid "see revised text."

### 4. How to admit a real error (when the reviewer caught one)

Fixed four steps — no padding, no blame-shift, no over-apology:

1. One thank-you / admit line: "Thank you for pointing this out." / "We apologize for this
   oversight."
2. Plain statement of what was wrong: "There was a writing error in Table 1." / "We rechecked the
   calculation."
3. Give the corrected number / wording.
4. State where it was fixed.

Example (historical style): keep short; correct; cite locus.

Do **not** write "We sincerely apologize for this unfortunate mistake and any inconvenience it may have caused..." — that over-apology never appears in the user's historical letters.

### 5. Soft refusal / scholarly disagreement

Never hard-push back; never unconditional surrender. Three beats:

1. **Acknowledge the concern:** "We agree that...", "We acknowledge this is an important
   point..."
2. **State the boundary:** study design (retrospective / single-center), data unavailable, ethics limits, sample size,
   journal word limits — explain **why it cannot be done**, not "we do not want to."
3. **Land as a binary:**
   - Provide the feasible partial evidence / literature (full citations), **or**
   - Put the limitation into the Limitation paragraph and quote that text in the letter.

Example (data unavailable) / Example (methods dispute but hold the line): keep measured; cite evidence.

**Never invent unrun experiments / analyses / external validation** — factuality lock; this user's letters never broke it.

### 6. Closings — two real templates

**Closing A (Qiang lab style; most frequent; often word-identical across papers):**

```
We hope that the revised manuscript is now acceptable for publication. If you have any questions,
please email to me (see mem:response_email). Once again, thank you very much
for your comments and suggestions.
```

Used for: Qiang-lab endoscopy / radiomics series replies; signed Jinwei Qiang.

**Closing B (no signature; stop after last point):**
After the last response, end — no thank-you block, no signature — common in MHE/schistosomiasis,
PCOS, and similar series.

Which default depends on whether this task continues a known series (same manuscript batch, same sign-off). When unsure, ask the user once whether to add the standard closing — do not silently apply A.

### 7. Micro-habits (keep; do not “correct” into textbook English)

These non-standard / semi-formal patterns recur in the user's letters. **Keep them as the user writes them** — replacing with “more standard” English makes the letter stop sounding like them:

- "Thanks for the suggestion" (no *you*) mixed with "Thank you for the suggestion".
- "Thank you for the reminding" (non-standard *reminder*) — appears across papers; usable when thanking for a reminder / correction.
- "We clarified it in the text." / "We explicated it in the text." — alternate near-synonym closers (*explicate* preferred in MHE/PCOS series).
- "We admit that..." for real limitations (vs generic "We acknowledge that..."; both OK, *admit* more spoken and common when confessing sampling bias / single-center / retrospective design).
- Response label format is not forced uniform: `Response:` / `**Response:**` / `Responses:`
  (plural, rare Qiang letters) / mixed Chinese/English colon `Response：`. Follow the series' existing
  format; do not flip within one letter.
- Comments and replies often use dash lists (`- ` for the comment, `- **Response:**` for the
  reply) or unnumbered plain paragraphs — both are authentic; follow the manuscript series.

### 8. How to use

When drafting a reply:

1. Build letter skeleton, per-point IDs, and change log from this file; triage against `07_response/base/revise/references/resolution-protocol.md`.
2. Pick each opener from §2; avoid one template everywhere.
3. Write body with §3 quote + locus habits.
4. Real errors → §4 four steps; impossible asks → §5 three beats.
5. Closing → §6; ask when unsure.
6. Pass §7 once — restore a few user micro-habits; drop over-servile apology tone.

### 9. Edit unit and comment source (aligned with 00/05)

- When landing a point, the edit unit is **词或句** (word or sentence); forbid whole-paragraph rewrite. Quoted text in the letter is that revised sentence. Ownership: see `00_orchestrator/references/ownership-contract.md`.
- Whether each point is truly resolved: use this file's status (Resolved / Partially resolved / Unresolved / New issue); do not only check “whether a sentence was added.”
- Manuscript comments (稿面批注) carry source: `[advanced]` / `[revise]` / `[…]`, etc.
- Fine-id suggestion vs lab doctrine conflict: comment states conflict + fix plan (before/after); **用户决定** (user decides). After agreement, Aitee still applies Track Changes. Lee does not edit the body by default.
- Decidable body edits: Lee comments for Aitee TC-fix. Past tense only for edits already landed.
- Still undecidable (missing source/analysis, ethics Date/NO unset): the **matching response point** must say pending and name the pending source. Do not write that point as already done. `Suggested …` stays in Word 批注 (see ownership-contract), not as invent/disclaimer in the letter body. Do not pretend experiments were done.
- **Process-negation / 未做-class (owner 2026-10-23):** Sentences that flag work not done («未做 / 未进行 / 我们未…» or similar CYA) **must not enter the body** (manuscript, revision, response letter). Word **批注** only (author **A**), and every comment **must** include **建议修改后内容**; bare flags forbidden. Empirical negative findings (*no significant difference*, *was not associated with*) are not banned by this rule. QC: `05_manuscript/qc/anti-leak-placeholders.md` AL-5; `07_response/qc/disclaimer-comment-only.md`.
- This-round new citations in the response letter: one `[cite-src]` comment on the letter's major heading (`05_manuscript/advanced/process/heading-source-comment.md`). New citations added into the manuscript are still placed by Aitee on the manuscript headings.

---

### Uncertainty and disagreement (回复审稿人画像)

Bank habit for **审稿回复** / response letters (not for inventing data):

- Keep replies short and concrete. Confirm, clarify, or refuse with evidence — no long defense essays.
- If the reviewer is wrong on a fact, politely correct **with the source** (HTML row, table, guideline). Do not rewrite the paper into an incorrect request.
- If you do not know (missing analysis, missing file, ethics Date/NO unset): the matching response point says the fact is still pending a source. Past tense only for edits already made. `Suggested …` and `cannot_invent` stay in the Word comment, not as invent disclaimers in the letter.
- Attitude lock: **uncertain → mark; never pretend certainty.**



---

### Part B — Resolution protocol

Moved 2026-11-14 to `07_response/base/revise/references/resolution-protocol.md` (bot map, issue card, roles, resolution checklist, three exits, out of scope, bank-skeleton pointers). This file keeps the letter voice. Standing letter opener remains authoritative here: **Thank you for your comments** | **suggestions** | **inquiry**.
