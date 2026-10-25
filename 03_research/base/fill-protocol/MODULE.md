---
name: "fill-protocol"
domain: "03_research"
trigger: ["IRB", "伦理", "知情同意", "表单填充", "fill protocol"]
inputs: ["protocol_template"]
outputs: ["filled_protocol"]
quality_control: "placeholders only; no patient data; never invent ethics numbers"
owner: "03_research/base/fill-protocol/MODULE.md"
---

<!--
Format-layer stub (pairs with write-protocol)
fine_id: IRB form fill (format layer; write-protocol owns content)
extracted: 2026-09-13
maintain: blank-source / as-absorbed stub only; not rewritten to Aitor-format.
-->

---
name: fill-protocol
description: >
  Fill institutional Word form templates (.doc/.docx) for IRB protocols, ethics
  applications, grant proposals, and other structured research documents while
  preserving the original styles, table layouts, fonts, and page geometry. Pairs
  with write-protocol — write-protocol drafts the scientific content, fill-protocol
  renders it into the institutional template.
triggers: fill protocol, fill template, fill IRB form, IRB template, ethics template, grant template
tools: Read, Write, Edit, Bash, Grep, Glob
model: inherit
---

# Fill-Protocol Skill

> **Provenance / on-disk status (Batch1 F9; Batch4 B2 trim):**
> In-repo body under `03_research/base/fill-protocol/` (extracted 2026-09-13).
> This MODULE keeps **principles + paths only**. The following assets are **not present**
> in `03_research/base/fill-protocol/` — do not pretend they exist; do not invent paths:
> - `setup.sh`
> - `scripts/doc_to_docx.py`, `scripts/inspect_template.py`, `scripts/fill_form.py`
> - `examples/`
> - `references/best_practices.md`
> Personal/Jinshan: `03_research/personal/fill-protocol/`. Registry path: `03_research/base/fill-protocol/`.

You are helping a researcher populate an institutional Word form (IRB protocol,
ethics application, grant proposal, etc.) without breaking the original document
formatting. This skill is the formatting counterpart to `write-protocol`: where
`write-protocol` drafts content, `fill-protocol` lays that content into the
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
| Personal / Jinshan / PHI packs | `03_research/personal/fill-protocol/` |
| Registry fine id | `fill-protocol` (live under `03_research/base/fill-protocol/`) |

**Companion fine ids (content / upstream):** `write-protocol`, `check-reporting`,
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
