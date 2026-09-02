---
name: ethics-application-forms
description: >
  Fill hospital IRB / ethics application form packs without changing template layout.
  Use for 伦理申请, 填伦理, IRB, 伦理表, 按填写好格式写伦理.
  Do not invent ethics Date/NO, PI 学历, GCP, or team members.
  Manuscript ethics prose stays in 05_manuscript; study design stays in 03_research.
---

# 伦理申请表格填报

**暂时挂在 02**（`02_data-processing/ethics-application-forms/`）。真正家园仍是 **03 伦理设计**（protocol-level `03_research/ethics.md`）；本技能只填院内表格，不发明研究设计。

## Purpose

按院内**空白表格模板**把一项研究填成可递交的伦理材料包。核心是填表，不是另写一套方案。
**铁律：只替换文字，不改版式。** 禁止另起空白 Word 重做表格。

## Capability map

| Task | Path |
|------|------|
| **填表（本技能）** | 下面工作流 + `docx_cell_replace.py` / `word_find_replace.py` |
| 金山医院空白包、递交清单、栏目 | `jinshan-form-pack.md` |
| 填完自检 | `checklist.md` |
| 研究类型 / 入排 / 终点 / 样本量口径 | `03_research` — 缺设计先问用户或走 03，不在本技能里发明 |
| 统计 / 样本量公式 | `04_analysis` |
| 知情同意通俗正文、论著里的伦理段落 | `05_manuscript` `radiology-ethics` — 本技能只把已定正文填进表 |
| Excel 登记表 | `02_data-processing`（mounted `02-xlsx`）若 COM/xlsx 脚本不够用 |

## Modes

- `fill` — 默认。复制默认包（官方 10 份空白 + 立项申请表）→ 按参数填 0–6 号表与立项申请表
- `plan` — 只出参数表和文件清单，等用户点头再填
- `qc` — 对已填包做一致性检索，不改版式

缺研究类型（干预 / 观察 / 免知情）或缺 PI 关键字段时**先问用户**，不要猜。

## 从其他技能取什么

填表前凑齐一套参数，能从已有技能/用户材料抄就抄，抄不到就标「待补充」：

```text
TITLE, PI, DEPT, PHONE, EMAIL, HOSP, TITLE_SHORT,
N, START, END, VER, VER_DATE,
DESIGN_TYPE (干预 / 观察 / 免知情),
VULNERABLE, PRIMARY_EP, SECONDARY_EP, AE_PLAN
```

- 题目、设计、入排、终点 ← `03_research` 或用户方案
- n、期限 ← 用户或 `04_analysis`，禁止编造
- ICF 通俗段落 ← 需要长文时请 `05_manuscript` 起草，再填入模板
- 旧课题痕迹（姓名、电话、病种、例数）必须全局清掉

## 填表工作流

1. 母版用金山 `0空白/临床研究-伦理初始审查申请.zip`，不用 `伦理/`、`填写好/`、`伦理/伦理/` 里的已填样例。
2. **默认包（不可漂移）** = zip 内官方 **10 份空白** **加上** 工作夹立项申请表。`01.金山医院研究生科研课题开题提纲模板` **不在本包**（开题不是伦理初审）。
3. 方案+知情共 5 份模板，**按研究类型选一对**（干预方案+干预知情 / 观察方案+观察知情 / 方案+免知情）。切勿五份全交，切勿交空白。
4. 先输出规划表（题目、PI、类型、n、期限、版本、文件清单、待补项）。用户同意后再写文件。
5. 复制 `0空白` zip 内 10 份文件，并加上工作夹的立项申请表，到 `填写好_<PI>_<短题>/`，**不覆盖**母版、**不拷开题提纲**。
6. 保格式填：`.docx` 用 python-docx（只改文字/勾选，保留签名表）；`.doc` 用 Word/WPS COM 查找替换，一次只开一个；`.xls` 只改数据行。
7. 按 `checklist.md` 自检后交付路径、参数摘要、待签字项。

登记表 `.xls` 只发伦理邮箱、不打印。初审申请表 PI 手签、日期写递交当天。干预性研究团队须有医生。科学性审查批件：院级立项、研究者发起自选（干预性）必须交；自选观察性可豁免。细节见 `jinshan-form-pack.md`。

立项申请表 `1-研究者发起的一般临床研究立项申请表.doc` **在默认包内**（官方空白 zip 未收，母版取工作夹空白/近空白件，填前清旧课题；不用 `伦理/伦理/` 已填件）。开题提纲仍不进默认包。

## Not this skill

- 选题 / 写研究设计 / 选刊 → `03_research`
- 写论著 Methods 伦理段、去 AI、配图 → `05_manuscript`
- 评阅 / 回审稿 → `06_review`
- 编造伦理批号、学历、GCP、未提供的团队成员

## Progressive disclosure

只发现本 `SKILL.md`。栏目和递交清单一律读同目录 `jinshan-form-pack.md` / `checklist.md`，不要把医院 Word 原件推进公开仓库。
