---
name: "track-changes"
domain: "06_review"
trigger: ["Word 修订", "Track Changes", "w:ins", "w:del", "修订痕迹", "docx 校验"]
inputs: ["docx", "pre_edit_original"]
outputs: ["validated_docx", "revision_audit"]
tools: ["Python", "defusedxml", "lxml"]
quality_control: "every text change wrapped in w:ins / w:del; author A; no silent overwrite"
owner: "06_review/base/track-changes/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Word Track Changes: unpack, edit, verify, pack

Mechanical tooling for the rule in MY-RULES `My rule.md` §5.1 and
`06_review/advanced/word-edit.md`: **every `.docx` edit lands under Track Changes with author
`A`; word/sentence grain; never a silent overwrite.** This pack proves that rule was followed.
Contract only: the invariant plus the unpack / validate / pack commands; every text decision belongs to `05_manuscript/advanced/`, `06_review/advanced/`, or `07_response/advanced/`.

Not a Word editor. Text decisions belong to `05_manuscript` (`Aitor-format.md`, `humanize`), to
`06_review/advanced/review.md` for findings, and to `07_response/base/revise/` for letters. This
pack only inspects and repacks the file.

**Scripts live here on purpose.** They are the exception to the "code goes to stats-analysis" rule:
they are Word-format mechanics with no patient data and no analysis, and they need to travel with
the redlining contract. Attribution: `LICENSE.txt` (Anthropic).

## Tools

```text
scripts/office/
  unpack.py     # .docx -> directory of XML (optionally merge runs / simplify redlines)
  validate.py   # structural checks + "was every change tracked by --author?"
  pack.py       # directory -> .docx (condense XML, validate, write)
  helpers/merge_runs.py        # collapse adjacent identical runs
  helpers/simplify_redlines.py # merge adjacent w:ins / w:del by same author
  validators/{base,docx,redlining}.py
```

## The check that matters

`validate.py --original <pre-edit.docx>` compares the text of the two files **after** removing the
requested author's revisions. If anything still differs, the edit was not tracked:

```bash
python scripts/office/validate.py edited.docx --original comments-org.docx --author A
```

Exit `0` = every change is under Track Changes by `A`. Exit `1` = something was overwritten silently
and the caller must go back and redo it as a revision. This is a hard gate, not advice.

Without `--original` only structural checks run (well-formed XML, namespace prefixes, unique IDs,
relationship targets, whitespace preservation, `w:del`/`w:ins` nesting, comment markers).

## Workflow

1. **Keep the original.** The pre-edit file is `*-org.docx` and stays in the project
   (`ref/review/`); `{RULES}\project-ref-layout.md`.
2. **Unpack** when an edit needs XML-level surgery:
   ```bash
   python scripts/office/unpack.py comments-org.docx unpacked/
   ```
3. Edit the XML. Every changed run goes inside `<w:ins w:author="A" …>`; every removed run inside
   `<w:del w:author="A" …>`. To reject someone else's insertion, nest `<w:del>` inside their
   `<w:ins>` rather than deleting their tag.
4. **Pack** back:
   ```bash
   python scripts/office/pack.py unpacked/ revised.docx --original comments-org.docx
   ```
   `pack.py` re-validates before writing and refuses on failure.
5. **Re-validate** the delivered file against the original (step above). Record the outcome in the
   project's `ref/manuscript-revision.md`.

## Rules

1. Author field is always **`A`**; source tags are a separate axis (`06_review/advanced/review.md`
   §0). `--author` defaults to `A` for this reason.
2. Word or sentence grain. Never rewrap a whole paragraph in one `w:ins`.
3. If the owner already edited that span, ask before touching it again — do not revert their text
   (`My rule.md` §5.1 "城城已改先问").
4. Do not restyle. Fonts, spacing, margins and table geometry change only when the owner names them
   this turn.
5. No new files to hold an intermediate — unpack into a `{DEL}` scratch directory and remove it.

## Handoffs

- What to change and how to phrase it → `06_review/advanced/word-edit.md`,
  `06_review/advanced/review.md`
- Response letters → `07_response/base/revise/`
- Formatting contract → `05_manuscript/advanced/Aitor-format.md`
