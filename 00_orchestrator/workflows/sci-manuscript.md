# SOP: sci-manuscript

**Owner:** `00_orchestrator`. Prediction-model SCI from existing HTML, not from scratch stats.

Use when the user picks this SOP, or 写稿 / 按我的风格写 / 全线写论著（且选了本 SOP）。

Numbers **only** from that endpoint’s `*-results.html`. Format: `Aitor-format.md`.

If `ref/project-state.yaml` exists, read `manuscript:` (journal, docx paths, reviewer_items). Do not overwrite `settings.ini`.

## Sequence

0. **Session mount pick (`01`)** — before loading packs, ask which of the registry `MOUNTED` ids to attach **this run**. Load only the picked ids. Do not auto-load all mounted ids. Personal layers are not a mount pick.
1. **Confirm inputs** — results HTML, PNG, Figure 1 n from text. Missing n → ask, do not invent.
2. **Methods / Results (`05_manuscript`)** — personal upper layer + Aitor. Table 1 = training vs test. Nomogram not “Combined”.
3. **Figure 1 (`04_analysis`)** — STROBE / patient-flow: mounted `04-fig-flow`. Statistical plots / imaging panels: mounted `04-fig-plot`. Palette: `lab-palettes.md` / `FIG_PALETTE` in ini. Captions still 05. Do not draw Figure 1 with `04-fig-plot` and “no inclusion box”.
4. **Introduction / Discussion** — literature via `03_research`; 05 consumes `intro-discussion-evidence.md` then polisher §2/§5. Quotas only in Aitor.
5. **De-AI (`05_manuscript`)** — `05_manuscript/personal/forbidden-phrases.md` then ai-isms. Methods stay passive.
6. **Pre-review (`06_review`)** — Summary / Major / Minor. Inventable items → questions for the user.
7. **Revise (`05_manuscript`)** after the user answers. If reviewer comments exist → **`06_review` only as entry**, then `05_manuscript` for changed sentences.

## Do not

- Run pipeline unless `04_analysis` is also requested.
- Cite in Methods; cite in Intro last paragraph or Discussion first paragraph.
- Dual-write VAL_MODE into YAML.
- Draw figures inside 05.

## Output

Overwrite `Manuscript_<结局>_house.docx` in place (or `_polished.docx` after an archive pass).
