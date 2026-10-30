# jinshan-form-pack-digest

**Absorbed:** 2026-10-23 from `_library/study-design/fill-protocol/jinshan-form-pack.md`.
**Dedupe:** default-pack self-check → `checklist.md`; registration fixed columns + 10 blanks + pair table → `form-boilerplate.md`. This digest keeps **per-form field tips**, **official submit extras (0-14)**, and **common-error traps** only.

## Live pointers (after move)

| Role | Path |
|---|---|
| Durable original | `{DEL}\_by-project\skill-harvest-sources-20261024\sources\library-methods-20261023\study-design\fill-protocol\` |
| Park | `{DEL}\_by-project\0doc-library-methods-20261023\study-design\fill-protocol\` |
| Blank templates | `{doc_root}\templates\ethics-blank\` |
| Filled/PHI | ethics tree / `{raw_root}\_lab\ethics\raw-20261023\` — **never GitHub** |
| Seat | `03_research/advanced/fill-protocol/` (`README`, `checklist`, `form-boilerplate`) |

## Default pack (align with 填写说明 — do not drift)

**Default pack = official zip 10 blanks + project-initiation application. Opening outline is not in this pack.**

Work-folder 「填写说明」8-file delivery map (observational path; swap intervention pair if needed):

1. 登记表 `.xls`  2. 初审申请表  3. **立项申请表** (not in zip; required in default pack; master from work-folder blank; clear old project before fill)
4-5. Protocol + ICF **matching pair**  6. CV  7. Declaration  8. Roster

Hard rule: change text only — do not alter table structure/layout; dedupe `(1)` same-name files by basename — never treat as a second master.

**Not in this pack:** opening-outline template; work-folder “email” xlsx (default to `.xls` inside the zip).

## Official submit extras (beyond the 8)

| # | Item | Note |
|---|---|---|
| 0 | 登记表 | email only — value in the local ethics contact library (outside the repo); never print |
| 1 | 初审申请表 | PI hand-sign; date = submit day |
| 2-3 | Protocol / ICF or 免知情 | version+date; multi-site = lead-site protocol + local sign page |
| 4-6 | CV / declaration / roster | interventional must include a physician; multicenter attach site + PI |
| 7 | 科学性审查批件 | required for hospital-level initiation / investigator-initiated optional **intervention**; optional observational may waive |
| 8 | 新技术可行性与安全性 | if applicable |
| 9 | 组长单位批件 | if this hospital is a participating site |
| 10-14 | Sponsor quals, CRF/EDC export, insurance, drug/device registration | if applicable |

Email subject: `申请类型＋申请人姓名`. Paper: two copies, double-sided separately bound → Science Building 313 (after form check passes).

## Per-form field tips (thin)

**0 登记表:** self-selected project ID →「无」; period to the day; this-site headcount; single-center=1; protocol/ICF initial V1.0 + draft date; checklist = files actually submitted.

**1 初审申请表:** vulnerable populations, confidentiality/outbound, consent process (who/when/where/ads), illiterate / incapacity / human genetics, **rewrite emergency measures for this project's risks**, PI signature block.

**1b 立项申请表:** class/funding/single-vs-multi/total vs this-site n; exploratory/confirmatory; **intervention vs observation**; extra exams, EDC, insurance, human genetics; start/end; brief/purpose/content; PI statement + department opinion.

**2 Protocol spine (keep hospital section order):** cover → signature page → background+refs → purpose → overview (design/n/flow) → inclusion/exclusion → endpoints → process → AE → data → recruitment/consent → stats/sample size → confidentiality → schedule. Intervention adds randomization/controls/blinding limits/intervention detail/safety review. Digital health/AI: version lock, de-id, logs, human review.

**3 ICF:** protocol name/version/investigator; background purpose process; risks benefits costs compensation; alternatives and rights; contacts = investigator + ethics office; **do not delete signature page**. Sample phone/email follow template (ethics office phone / email: take from the local ethics contact record, outside the repo; never commit it).

**4 CV:** unknown →「待补充」, never invent. **5 Declaration:** usually only swap department + title. **6 Roster:** if only PI known, one row + note pending fill.

## Common error traps (sample residue)

- Old PI / department / phone still in contact lines
- Still checked「观察性」while the protocol is an RCT
- Vulnerable「无」checked but subjects are pregnant
- Emergency measures still unrelated boilerplate (e.g.「停止影像学检查/给氧」)
- Consent still says「不涉及干预/仅病历回顾」

## See also

- `checklist.md` — default-pack self-check + consistency + privacy + delivery
- `form-boilerplate.md` — registration fixed columns + five-hospital swaps + 10 blanks table
