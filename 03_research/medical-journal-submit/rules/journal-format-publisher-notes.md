> Moved from `rules/journal-format-publisher-notes.md` (depth ≤4).

# Publisher-specific notes

Quirks observed when researching author guidelines by publisher. Add to this file as new publishers/journals come up.

## Wiley (onlinelibrary.wiley.com)

- Author-guidelines pages (`.../homepage/forauthors.html` or `.../author-guidelines`) commonly return a bot-detection error on direct `web_fetch`. Don't stop there — `web_search` for the journal name + "author guidelines" surfaces indexed snippets of the same page, usually enough to piece together title-page order, abstract/keyword rules, and reference style across 2-4 searches.
- Journals are identified internally by a short submission-system code (e.g. CAM4 = *Cancer Medicine*, BRX2 = *Brain-X*). Useful to confirm you've got the right journal when the name is generic.
- Common Wiley medical-journal pattern for references: "use any consistent generic style for review; final typeset output converts to Vancouver." So a manuscript already using Vancouver-style numbered citations is normally fine as-is — don't force reformatting of a compliant reference list.
- Title-page element lists and required statements (COI, ethics, data availability, funding, CRediT-based author contributions) vary per journal but follow a recognizable shared template across Wiley's medical/oncology titles — cross-checking a couple of sibling journals (e.g. other Wiley cancer journals) when the target journal's own page is thin on detail is a reasonable way to fill gaps, but flag anything inferred this way as unconfirmed rather than stating it as the target journal's own rule.

## Springer Nature — BMC series vs. "Discover" series

Both live under `link.springer.com/journal/<number>`, both use numbered Vancouver-style references, and it is easy to assume one is the other — confirm the actual journal name and the publisher "brand" shown on the page (Springer / BMC / Palgrave / Apress / Discover) rather than guessing from the journal number or a filename. Example: journal number `12672` is *Discover Oncology* (Discover series), not *BMC Cancer* — despite a manuscript file having previously been named as if for BMC Cancer.

**BMC / SpringerOpen family** (journals hosted at `*.biomedcentral.com`, e.g. BMC Cancer, BMC Public Health):
- Structured abstract with bolded headers: Background, Methods, Results, Conclusions.
- First main-text section heading is "Background" (not "Introduction").
- Declarations section is headed exactly "Declarations", with subheadings: Ethics approval and consent to participate; Consent for publication; Availability of data and materials; Competing interests; Funding; Authors' contributions; Acknowledgements.
- Keywords: typically 3–10.
- References: numbered Vancouver, e.g. `J Med Genet. 2022;59(7):632-643.` — year immediately after the journal abbreviation, not parenthesized at the end.

**Springer "Discover" series** (e.g. Discover Oncology, Discover Applied Sciences, Discover Education, Discover Mental Health, Discover Sustainability, Green Technology Resilience and Sustainability):
- Unstructured abstract, 150–250 words, no headed subsections — write it as one flowing paragraph.
- Keywords: 4–6 (tighter range than BMC).
- First main-text section heading is conventionally "Introduction".
- Declarations section is headed "Statements and Declarations" (not "Declarations"), listing the same kinds of statements (Funding, Competing Interests, Ethics approval, Consent to participate, Consent for publication, Data availability, Author contributions, Code availability where relevant).
- References: same numbered Vancouver style as BMC — `Journal Abbrev. Year;Vol(Issue):Pages.` — confirmed from the guidelines' own example (`Smith JJ. The world of science. Am J Sci. 1999;36:234–5.`).
- Author-Contribution and Competing-Interest information is usually also collected via the submission portal interface separately from the manuscript text — the in-text statement is still required, but don't be surprised if the portal has its own version of the same fields.

Because both families otherwise look similar (same publisher, similar reference style, similar declarations concept), the abstract structure and the "Declarations" vs. "Statements and Declarations" heading are the fastest tells for which one you're actually dealing with — check both early.

## General

- When a journal's own guidelines are silent on something (e.g. exact abstract word cap), don't assert a number — say what you found and what's unconfirmed, and let the user decide or check the submission portal directly.
