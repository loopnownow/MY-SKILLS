---
name: "fill-protocol"
domain: "03_research"
description: "Fill institutional Word form templates (.doc/.docx) for IRB protocols, ethics applications and grant proposals, preserving original styles, table layouts, fonts and page geometry. Draft protocol content then fill the template. Absorbed former write-protocol draft step (2026-10-30)."
trigger: ["IRB", "伦理", "知情同意", "表单填充", "fill protocol", "fill template", "fill IRB form", "ethics template", "grant template"]
inputs: ["protocol_template"]
outputs: ["filled_protocol"]
tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"]
quality_control: "placeholders only; no patient data; never invent ethics numbers"
owner: "03_research/base/fill-protocol/MODULE.md"
---

# Fill-Protocol Skill

Contract only for fill-protocol (ethics form intake): scope, bans, phase names, and pointers. The recipe and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`rules/`, `data/`, `references/`) stays beside it as data.

## Draft first, then fill

One chain: draft the protocol body (generic study-protocol text; not experimental design blueprints -- those stay in design-study), then lay that content into the institutional Word template with the principles below. The former write-protocol pack was a stub and is absorbed here (directory removed 2026-10-30).



> **Provenance / on-disk status (Batch1 F9; Batch4 B2 trim):**
> In-repo body under `03_research/base/fill-protocol/` (extracted 2026-09-13).
> This MODULE keeps **principles + paths only**. The following assets are **not present**
> in `03_research/base/fill-protocol/` — do not pretend they exist; do not invent paths:
> - `setup.sh`
> - `scripts/doc_to_docx.py`, `scripts/inspect_template.py`, `scripts/fill_form.py`
> - `examples/`
> - `03_research/base/verify-refs/references/best_practices.md`
> Advanced/Jinshan: `03_research/advanced/fill-protocol/`. Registry path: `03_research/base/fill-protocol/`.

You are helping a researcher populate an institutional Word form (IRB protocol,
ethics application, grant proposal, etc.) without breaking the original document
formatting. This skill is the template-fill step after drafting: where
this pack drafts content then lays it into the
institutional template.

## Core Principles (Do Not Violate)

1. **Open the existing template — never create from scratch.** Use
   `Document(template_path)`, not `Document()`.
2. **Convert .doc → .docx via LibreOffice headless** before any editing.
   `pandoc -f doc` is not supported; `textutil` corrupts table structure.
3. **Match cells by left-label text**, not row/column coordinates. Templates
   evolve and coordinate matching breaks silently.
4. **Apply `cantSplit` to every filled row** so a row never breaks across pages.
5. **For CJK languages, set the `eastAsia` font attribute**, not just
   `run.font.name`. Hangul/Kanji/Hanzi will render in fallback fonts otherwise.
6. **Validate** every fill operation: report unmatched labels, count empty cells,
   and surface mismatches before saving.

## Paths

| Role | Path |
|---|---|
| Capability body (this file) | `03_research/base/fill-protocol/MODULE.md` |
| Thin skill pointer | `03_research/base/fill-protocol/SKILL.md` |
| Advanced / Jinshan / PHI packs | `03_research/advanced/fill-protocol/` |
| Registry fine id | `fill-protocol` (live under `03_research/base/fill-protocol/`) |

**Companion fine ids:** `check-reporting`,
`calc-sample-size`. Do not vendor missing scripts into this pack; if automation is
needed later, add real files under `scripts/` and update this MODULE in the same PR.

## Anti-Patterns (summary)

| Anti-pattern | Consequence |
|---|---|
| `Document()` then rebuild table | Loss of header logo, margins, footer, page numbering |
| `pandoc -f doc` / `textutil -convert docx` | Unsupported or corrupted tables |
| `cell.text = "value"` single assign | Erases run-level styles / eastAsia font |
| Coordinate-based `table.cell(r, c)` | Silent breakage when template rows reorder |

## Anti-Hallucination

- Never fabricate references, clinical definitions, or numerical results.
- Never invent paths to `setup.sh` / `scripts/*.py` / `examples/` until they exist on disk.
- If a reporting guideline or form field is uncertain, flag `[VERIFY]` rather than guessing.
