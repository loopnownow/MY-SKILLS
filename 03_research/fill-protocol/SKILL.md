---
name: fill-protocol
description: >
  Bai seat route for IRB / ethics form fill. Canonical capability body is B
  MY-SKILLS-base/03-research/fill-protocol/ (MedSci Word-template filler).
  Jinshan hospital pack and PHI stay under 03_research/personal/fill-protocol/.
  Do not invent ethics Date/NO, PI 学历, GCP, or team members.
---

# 伦理申请表格填报（A top-layer / Bai seat）

**Seat:** Bai（投审伦理表专员）。Aitor 路由并盯梢。Victor 不填表。

**Canonical capability (B):** `MY-SKILLS-base/03-research/fill-protocol/`  
(`SKILL.md` + `MODULE.md` — MedSci institutional Word-template filler; pairs with `write-protocol`.)

Load **B** for fill mechanics: open the existing template in place, convert `.doc`→`.docx` when needed, label-match cells, validate unmatched labels. Do **not** duplicate the MedSci body here.

## Bai / Jinshan seat (A personal — not B)

| Task | Path |
|------|------|
| Jinshan checklist / five-hospital boilerplate | `03_research/personal/fill-protocol/` |
| Protocol-level ethics design notes | `03_research/personal/ethics.md` |
| On-disk blanks / 批件 / 人员信息 / PHI | `{doc_ethics}` / `{doc_fill_protocol}` — never copy into B or public base |

缺研究类型或缺 PI 关键字段先问用户，不要猜。旧课题痕迹必须全局清掉。

## Not this skill

- 选题 / 研究设计 → `03_research`
- 样本量 → `04_analysis` (`calc-sample-size`)
- 论著 Methods 伦理段 → `05_manuscript`
- 编造伦理批号、学历、GCP、未提供的团队成员
