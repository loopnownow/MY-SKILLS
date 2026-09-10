# HTML Visual Design (standing delivery rules)

**Owner:** `00_orchestrator`. Applies whenever any skill **generates or edits** a `.html` for this lab (选刊交付、QC、架构建议、报告页等).

**Source:** user Principles HTML 2026-09-10 (full sample in skill-library `extracts/00_orchestrator/`; do not require reading the full HTML at runtime).

**Not in scope now:** full-repo architecture audit / Decision Ledger theater. Keep those sections dormant until the user asks for an audit HTML.

## Hard rules (every `.html`)

1. **Information → Decision → Evidence → UI.** Structure before decoration.
2. **Native only:** HTML/CSS/JS in-file or local. No CDN frameworks, no remote fonts, no runtime SaaS deps (offline-openable).
3. **Theme in `:root`.** One primary accent. Status colors (ok/warn/danger) are semantic only — not a second brand palette.
4. **No decorative AI signatures:** no purple-blue gradients, multicolor text gradients, heavy glow, stacked glassmorphism, purposeless motion.
5. **Semantic HTML5:** `header` / `nav` / `main` / `section` / `footer` when they fit; `details`/`summary` for progressive disclosure.
6. **Interaction serves review:** hover / `focus-visible` / active; short transitions (~0.2s); honor `prefers-reduced-motion`.
7. **Print-aware when the page is a deliverable:** hide chrome; keep body content readable.
8. **Meta when it is a recommendation/audit artifact:** version, date, scope, status. Mark AI output as **Proposed** until the user approves — never look “already merged”.

## Type & spacing (defaults)

- Sans: system-ui stack; mono: ui-monospace stack. Weights **400 / 500 / 600** only.
- Rough scale: caption 12 · body-sm 14 · body 16 · H3 ~20 · H2 ~25 · H1 ~31.
- Radii: **4 / 8 / 16 / pill**. Prefer padding inside cards ≈ 1.5–2× child gaps.
- Layout: Grid/Flex with `repeat(auto-fit, minmax(…, 1fr))`; avoid fragile fixed widths.

## Palette defaults

Cool off-white / slate surfaces; **one** primary accent (Principles blue-ish defaults OK). Status colors are semantic only.

## Mini QC before handoff

- [ ] Readable without the stylesheet story (structure clear)
- [ ] One accent; no AI-gradient chrome
- [ ] Keyboard focus visible on controls
- [ ] Opens offline
- [ ] If recommendation page: Proposed ≠ Implemented
