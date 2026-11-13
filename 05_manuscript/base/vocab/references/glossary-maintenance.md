# Glossary evidence layer — maintenance contract

Open when maintaining `GLOSSARY_ROOT` (four layers + `index.csv`), adding entries,
regenerating section pointer pages, or migrating legacy section text. This is the
**evidence seat**: rule bodies stay in `05_manuscript/base/vocab/` (and named advanced
files); a glossary row may only point back with `rule_ptr`.

## Index schema (13 columns)

`layer, sub, sub2, entry, lang, example, evidence_ref, freq, verdict, rule_ptr, note,
sections, updated_at`

| Column | Rule |
|---|---|
| `layer` | only `words` / `sentences` / `paragraphs`; a `sections` layer is retired — section text lives in pointer pages |
| `sub` | `words`: terms / collocations / avoid · `sentences`: writing / review / reply · `paragraphs`: moves / connectives / length |
| `sub2` | filled **only** for `sentences` + `review` (bucket: grant-review / journal-review / thesis-review / projects); leave empty elsewhere |
| `sections` | multi-value `;`; values from abstract, intro, methods, results, discussion, limitation, conclusion, other |
| `verdict` | `use` / `avoid` / `context-only` |
| `rule_ptr` | pointer into `05_manuscript/base/vocab/` (or a named advanced file); never a copied rule |
| `evidence_ref` | `doc#pidx` → `banks\paras.jsonl` · `rv-doc#pidx` → `banks\revisions.jsonl` · `rt-###` → `banks\review-text.jsonl` · `flat-###` → `banks\flattened.jsonl` |

**Single source of truth:** entry bodies live in the four layer markdown files;
`index.csv` is generated and verified, never hand-edited in parallel with them.
`sections/*.md` are generated pointer pages (no body text).

## Entry body template

Each entry carries five fields: `用法` / `证据` / `频次` / `判断` / `规则`. An entry
without a resolvable `evidence_ref` is not admitted. The quote in `证据` must be a
verbatim substring of the cited record — locate case-insensitively, then store the
original casing.

## Rebuild order (serial only)

1. regenerate `index.csv` from the layer markdown (apply mode)
2. regenerate section pointer pages (they read `index.csv`)
3. verify every entry against its evidence record
4. count rows per layer
5. structure check (columns, enums, pointer parity)
6. path audit of `rule_ptr`
7. cleanup scan of stale rows

Never run an `--apply` step in parallel with anything that reads `index.csv`: a
concurrent read can write an older snapshot back over the regenerated index. One
apply step, then the readers, one at a time.

## Two gates (both must pass before hand-off)

| Gate | Test |
|---|---|
| column / enum gate | 13 columns present; `layer` enum respected; no `sections`-layer rows; `verdict`, `rule_ptr`, `evidence_ref` populated |
| pointer parity gate | each pointer page's row set equals the `sections` column of the index in **both** directions; pointer pages contain no body prose |

Negative tests: add an empty heading to a pointer page → parity gate fails; add a row
with `layer=sections` → column gate fails. Revert and re-run.

## Expected shape (assert shape, not literals)

A healthy live glossary at the last rebuild: ~200 entries, 0 entry mismatches,
structure check 18 pass / 0 fail / 2 skip, 8 section pages and ~41 pointer rows,
0 stale `rule_ptr`. These numbers drift with every batch — recompute them, use them
only to notice a large drop or duplication spike.

## Migration discipline

Legacy section text and one-off fragments are absorbed, not deleted:
`659 → 203` entries (net −456), sections `340 → 0`, auto fragments `469 → 13`
overview rows. On merge keep at least one `evidence_ref`; move additional refs into
`note`; never drop an entry without owner approval.

## Failure modes

- Parallel regeneration → stale index snapshot (see rebuild order).
- `note` stays empty for secondary refs: the generator reads only the primary
  evidence line, so merged refs remain in the markdown SSOT; do not re-add them by hand.
- Duplicate paragraphs across drafts (>40 characters; >1.2k known instances) inflate
  `freq`; dedupe or weight before quoting counts as evidence.
- Case-different quotes (`Thank you` vs `thank you`) fail verbatim checks.
- Markdown markers (`**作者回复：**`, `### 意见 N`) get parsed as entry keys; reject keys
  that do not start alphanumeric and prune historic noise.
- A fragment overview row is a retrieval entry point, **not** a recommended sentence;
  writing criteria still come from `base/vocab/`.
