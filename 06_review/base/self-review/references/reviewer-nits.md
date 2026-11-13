# Reviewer-language self-audit

Purpose: the comment classes real reviewers write, turned into a checklist the author runs on
their own draft before submission. Severity routing and blocking gates stay in
[pre-submission-hard-gates.md](pre-submission-hard-gates.md); number fidelity against primary
tables stays in [paper-claim-audit.md](paper-claim-audit.md).

Output vocabulary is the existing one: Blocking / Major / Minor / Nit. Every item carries a
location (section, page, line). An item without a location counts as not audited.

## What reviewers actually flag

1. One design name. Ethics paragraph, Methods, Discussion and the flow diagram must use the same
   design word (prospective / retrospective / ambispective). The usual offender is old ethics
   boilerplate that still says "prospective" while Methods says "retrospectively enrolled".
2. Executable inclusion and exclusion. Case definition, control definition and control source,
   matching variables (sex, age, stage), written to the reporting standard the journal asks for.
   The N staircase (screened, excluded with reasons, analysed) must add up across text, table
   and diagram.
3. Sample size on the record. The tool and its version are named, and the validation arm's N is
   stated where the claim is made, not only in a table.
4. Statistics as reported, not as run. Exact p (`P = 0.044`, not `P < 0.05`); confidence interval
   for subgroup differences; the multiplicity control named (FDR, Bonferroni, FWE); DeLong for an
   AUC comparison; calibration in deciles with error bars; the cut-off method (Youden) and the
   operating point; software and version.
5. Reproducibility detail. Missing-data handling; IBSI terms used as `selection` or
   `implementation` and not interchangeably; ComBat parameters (parametric or not, labels,
   covariate matrix); the Radscore formula and its coefficients; pixel spacing and slice
   thickness distribution when the pipeline depends on them.
6. Tables and figures. Every table is cited in the text; every caption is self-contained; lettering
   is legible at print size; abbreviations are defined at first use.
7. Reference style for the target journal. Output style, bracketed numbers not superscripts, all
   authors listed, `and` before the last author, no DOI/PMID/PMCID in the list, PubMed journal
   abbreviations.
8. Availability statements that survive a check. Every "available on request" has a mechanism;
   code and data claims match what exists, and the ethics statement does not promise more sharing
   than the consent allows.
9. Language as a page-line list. The actual errors with locations; "language needs polishing" is
   not a finding.
10. A conclusion that answers the question. Which metric or combination carries the information,
    in one sentence, without restating the Results.

## Run order

1. Walk the target journal's review form on the own draft; the eight form fields are listed in
   `06_review/base/peer-review/references/journal-review-form.md`.
2. Read the design name in the ethics paragraph, Methods, Discussion and the diagram.
3. Recompute what a reviewer recomputes: N staircase, train/test ratio, p, CI, AUC, calibration
   slope.
4. Cross-walk every table and figure number with the sentences that cite them.
5. Spot-check five references against the journal style.
6. Emit Blocking / Major / Minor / Nit with page and line; after the revision, re-run the same
   lists and record implemented / not implemented with the reason.

## Cautions

- Never report "no issues found". An audit that finds nothing did not look at locations.
- A self-audit list is not a review of another group's paper, and it is not sent out as one.
- Do not paste a real reviewer's text into the manuscript, a shared file, or a skill body.
- Zero-context claim audit: the auditor gets the blinded text and primary tables only, no prior
  verdicts and no author explanation.
