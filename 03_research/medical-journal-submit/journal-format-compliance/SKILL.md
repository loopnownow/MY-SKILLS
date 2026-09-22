---
name: journal-format-compliance
description: >
  Use this skill whenever the user asks to format, revise, or check a manuscript against a specific journal's author guidelines (e.g. "根据xx期刊作者须知修改稿件格式", "format this for submission to [journal]", "make this ready to submit to [journal]"). Also trigger when the user gives a journal name or author-guidelines URL alongside a manuscript file and asks for a submission-ready version, or asks whether a manuscript complies with a journal's requirements. Covers identifying the journal from a name, ISSN, or URL; retrieving its author guidelines; producing a structured compliance plan (title page elements, abstract structure and word limit, keyword count, reference style, figure and table order, required statements like COI, ethics, data availability, funding); flagging content-level inconsistencies that must NOT be silently resolved; and, once confirmed, applying the changes to a .docx as Word tracked changes. Always plan before editing; never guess on author identity, funding attribution, or other factual matters.
---

# Journal Format Compliance

Bring an existing manuscript (usually a .docx) into compliance with a specific journal's author guidelines, deliver a plan before touching the file, and produce a submission-ready .docx with the changes visible as Word tracked changes.

This skill assumes the `docx` skill is available for the actual file editing (unzip → edit `word/document.xml` → rezip → validate). Use the lab Word Track Changes workflow (`06_review/personal/word-edit-rules.md` + existing docx tooling). This skill covers journal-rule finding, planning, and knowing when to stop and ask.

## Workflow

### 1. Identify the journal and find its guidelines

- If given a URL, `web_fetch` it. Author-guidelines pages are frequently bot-blocked (this is common for Wiley's `onlinelibrary.wiley.com` pages) — if `web_fetch` is refused, fall back to `web_search` with the URL or journal name as the query; snippets from the guidelines page usually surface even when direct fetch fails. Issue several targeted searches (title page elements, abstract structure/word limit, keyword count, reference style, article-type word limits) rather than one broad query — guideline pages are long and a single search rarely surfaces everything.
- If only a journal name is given, search for `"<journal name>" author guidelines` and confirm the publisher/journal identity (ISSN, submission-system code, e.g. Wiley's CAM4 for *Cancer Medicine*) before proceeding — don't assume from the name alone if it's ambiguous.
- **Never infer the journal's identity from an uploaded manuscript's filename, a prior formatted version, or an offhand name mentioned earlier in the conversation — confirm it from the URL/journal number/ISSN itself.** A Springer `link.springer.com/journal/<number>` link does not tell you which journal *family* it belongs to by the number alone, and files are routinely misnamed after the wrong target (e.g. a file called `..._BMC_Cancer_....docx` submitted alongside a link to journal `12672`, which is actually *Discover Oncology*, not *BMC Cancer* — two journals with materially different formatting rules, see `../rules/journal-format-publisher-notes.md`). Fetch/search the actual guidelines page and check the journal's real name and publisher "brand" (Springer / BMC / Palgrave / Apress / Discover — shown in the page footer) before planning any edits. If the confirmed journal differs from what the file name or earlier conversation implied, say so plainly before proceeding.
- See `../rules/journal-format-publisher-notes.md` for known quirks of specific publishers' guideline pages, including the BMC-series vs. Springer "Discover"-series template differences.

### 2. Read the manuscript

- Convert to markdown for easy inspection: `pandoc -t markdown file.docx`.
- Extract: title page block, abstract (and its structure/word count), keywords, section headings, reference style actually used, figure/table order and placement, and check explicitly for the presence/absence of each required statement (Conflict of Interest / Competing Interests, Ethics approval, Data availability, Funding, Author contributions). Missing statements are a very common finding — always check for COI specifically, since it's easy to overlook and manuscripts frequently lack it.

### 3. Build the compliance table and plan — before editing anything

Produce a short table: requirement → what the journal wants → what the manuscript currently has. Then a bullet list of the concrete edits you intend to make.

**Critical rule:** if anything you find is a *factual/content* inconsistency rather than a pure formatting gap — mismatched corresponding-author names, a funding recipient not on the author list, contradictory dates, author-order disputes, etc. — do NOT resolve it yourself, and do NOT silently pick the version that looks more plausible. List it separately as an open question and ask the user directly. Proceed to editing only for the items that are unambiguous formatting fixes; hold everything touching facts about people, money, or attribution until the user answers. Getting one of these wrong in a real submission is a much worse failure than asking one extra question.

Also respect lab rule: if corresponding author, funding, ethics, or affiliations already exist in the manuscript, do not overwrite them with defaults/templates (`Aitor-format.md` / `word-edit-rules.md`).

Present the plan and, if there are open questions, stop and wait for the user's answers before editing the file.

### 4. Apply changes as tracked changes

Once confirmed:
- Use the `docx` skill's tracked-changes approach: unzip, locate the exact paragraph/run in `word/document.xml`, wrap changed text in `<w:ins>`/`<w:del>` (with `<w:delText>` inside deletions), rezip.
- Deleting a whole paragraph requires marking its paragraph mark as deleted too (see the docx skill's notes on this) so it doesn't leave a stray empty line.
- Inserting a new paragraph requires marking the *preceding* paragraph's mark as inserted, since that's the break being introduced.
- Pick a consistent tracked-changes author name (ask the user if they have a preference; otherwise something like "A" plus today's date is fine) and reuse it for every edit in the pass.
- After editing, run `scripts/office/validate.py out.docx --original original.docx --author "<name>"` from the docx skill to confirm every changed run is actually wrapped in a revision tag.
- Render to PDF/JPEG and visually check the tracked-changes markup looks right before delivering — especially for paragraph insertions/deletions, which are the easiest place to get the XML subtly wrong. Also render an "all changes accepted" preview (the docx skill's `accept_changes.py`) and check it too — the tracked-changes view can look fine while the accepted result still has a defect (see the nested-revision caution below, which specifically breaks silently in the tracked view and only shows up once accepted).

**Converting a structured abstract to unstructured (or vice versa).** A common cross-publisher edit (e.g. BMC's headed Background/Methods/Results/Conclusions abstract vs. Springer "Discover"-series' single unstructured paragraph) is a paragraph-merge, not a text swap: pick one surviving paragraph, replace its content with the new combined text, then for every other paragraph being folded in, delete all of its runs *and* mark its paragraph mark as deleted (this merges the now-empty paragraph into the next one on accept, so it collapses away rather than leaving a stray blank line). Do this for each paragraph in sequence so they all fold forward into the final surviving one.

**Editing content from an earlier, still-unaccepted tracked-changes round.** If a prior pass in the same session already wrapped some text in `<w:ins>` and this pass needs to remove or replace that same text, do **not** nest a new `<w:del>` inside the existing `<w:ins>` — `w:ins`/`w:del` run-track-change containers don't validly nest inside each other, and even where a tool accepts the XML, downstream processing (e.g. LibreOffice's accept-all-changes conversion) does not reliably resolve it, silently leaving the "deleted" text present in the final accepted document. Since that earlier insertion hasn't been accepted by anyone yet, the correct fix is simpler: remove the whole `<w:ins>` element outright to retract it. The original `<w:del>` from the earlier round (wrapping the true original text) is untouched and still shows the correct diff against the real original.

**Reformatting a numbered reference list's date placement.** A frequent gap regardless of target journal: manuscripts that write `Journal Abbrev. Vol(Issue):Pages (Year).` when the actual house style (BMC and Springer "Discover" series both use this) is `Journal Abbrev. Year;Vol(Issue):Pages.`. To convert reliably even when the journal abbreviation itself contains parentheses (e.g. `Cancers (Basel).`), don't parse left-to-right — match the trailing `(YYYY).` first, take everything before it as the prefix, then find the *last* `". "` in that prefix (volume/page segments don't contain periods) to split the journal name from the volume/pages segment. Reassemble as `<journal name>. <year>;<volume/pages>.`.

### 5. Deliver

Present the final .docx via `present_files`. Summarize what was changed and, separately, what was left untouched because it already complied — don't just list the diffs.

## Things not to touch without being asked

- Scientific content, results, or interpretation — this skill is about compliance formatting, not scientific editing.
- Abstract/text length purely to hit a word limit, if trimming would require cutting substantive content — flag the overage and ask, rather than cutting text on your own judgment.
- Reference list content (only formatting/style, not which references are cited).
