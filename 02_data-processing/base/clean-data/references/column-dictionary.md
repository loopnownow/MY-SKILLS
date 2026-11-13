# Column dictionary v1 — clinical tables

Data companion to [MODULE.md](../MODULE.md): the 22 core columns, measured alias table, value enums, the six per-sheet questions, and the header/missingness pathologies that were measured. Gates stay in MODULE; this file is the reference data.

## 1 Core 22 columns (four groups)

| Group | Columns |
|---|---|
| Identity (12) | 全院号 / 影像号 / 医技号 / 门诊号 / 住院号 / 病理号 / 样本编号 / 体检编号 / 姓名 / 性别 / 年龄 / 出生日期 |
| Time (3) | 检查日期 / 图像时间 / 就诊时间 |
| Clinical (5) | 诊断 / 病理诊断 / 部位 / 检查项目 / 检查结论 |
| Measure (2) | 测量值 / 单位 — long-table form of `ALT (g/L)`-style columns |

Rules:

- Surface variants of the same column go into `item.alias_of`; semantically different columns do not (see §2).
- Number-like identifiers (`序号` / `ID` / `编号` / `样本编号` / `patient_id` / `受试者ID` …) are each an **independent id_type**, never merged into one another.
- `病理诊断` stays a separate column from `诊断` — do not fold it into the clinical diagnosis.

## 2 Alias table (measured)

| Canonical | Variants found |
|---|---|
| 姓名 | `name` (129 sheets) / `Name` (16) / `姓名` (69) / `患者姓名` (1) / `英文姓名` (4) |
| 性别 | `性别` (48) / `Gender` (40) / `gender` (17) / `sex` (21) / `Sex` (5) |
| 年龄 | `年龄` (63) / `Age` (74) / `age` (46) / `age_approx` (3) |
| 诊断 | `诊断` (15) / `临床诊断` (19) / `diagnosis` (4); `病理诊断` (12) kept separate |
| 部位 | `部位` (20) / `position` (10) / `lesion_id` (3) |
| 编号类 | `序号` / `ID` / `id` / `编号` / `样本编号` / `patient_id` / `Patient_ID` / `受试者ID` — independent types |

## 3 Header normalisation (three actions, in order)

1. Strip `\xa0`, leading/trailing spaces, full-width spaces; record the raw name alongside the normalised one.
2. Full-width → half-width.
3. Peel punctuation and units off the name: `ALB (g/L)` → `ALB`, with `g/L` moved to the unit field; keep the Chinese name when variants disagree on language.

Scope of this pass: **surface variants only**. 14,807 distinct column names were counted in one library, of which 2,020 groups are just case / space / dot / unit spellings of one column, and only 923 appear in ≥2 families — compress the spellings, do not attempt library-wide semantic merging.

Empty headers are a real class, not an exception: 234 sheets had empty header cells (17,940 cells in total, from merged cells and layout residue), and one 56-column sheet had its last 6 columns unnamed. Name them explicitly (`col_<i>`) before ingest; never rely on "skip empty columns at read time".

## 4 Value normalisation enum

| Target | Rule |
|---|---|
| 性别 | `男/女/1/2/M/F` → 男/女 |
| 年龄 | strip `岁`; clamp to 1–120 |
| Dates | `YYYY-MM-DD` |
| Numbers | strip unit and thousands separators: `13.5 g/L` → 13.5 + unit |
| Mixed per item | keep both `num` and `text`; unparseable → `num = NULL`, text preserved; never guess |
| Group codes | five incompatible schemes coexist; `CHM6W-P` and `CHM6W-p` were read as different groups, `CHM6W-X` / `CHM6W-J` carry no label — build a group → label mapping table before any cross-project merge |

## 5 Six questions per sheet (before it enters a database)

1. Does it carry an identity key (can a person be claimed)?
2. Is a row an individual or a result?
3. Is it an instrument export?
4. Is it a wide table (`ncol` large, numeric header)?
5. Can it be concatenated with a same / near-same-header table?
6. Does a normalised column name collide?

Answers are recorded as that sheet's source metadata; they are the ingest judgement, not a formality.

## 6 Key-column coverage (measured, by fact rows)

| Column | Rows |
|---|---|
| 姓名 | 52,746 |
| 门诊号 | 35,000 |
| 病理号 | 34,843 |
| 影像号 | 14,130 |
| 住院号 | 786 |
| 全院号 | 602 |

医技号 sits on `entity` (41,979 rows) rather than in facts. Read the spread as a warning: most sheets are result tables, so identity columns are sparse by design — a table without an identity column is normal, not a defect.

## 7 Missingness decisions (measured)

- 样本编号 missing >10%: 7 sheets, all `ly_THESIS` enzyme/activity tables; cause is stacked blocks where the sequence number appears only on the first row of each block. Fix the block structure, do not impute the identifier.
- Variables with 51% / 28% / 18% missing: complete-case analysis only; no imputation model is justified at those rates.
- Decide **after** the cause check: drop the column, keep complete cases, or repair the block layout — in that order of preference.
