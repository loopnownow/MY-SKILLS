---
name: ethics-application-forms
description: >
  Fill hospital IRB / ethics application form packs without changing template layout.
  Use for 伦理申请, 填伦理, IRB, 伦理表, 按填写好格式写伦理.
  Do not invent ethics Date/NO, PI 学历, GCP, or team members.
  Manuscript ethics prose stays in 05_manuscript; study design stays in 03_research.
---

# 伦理申请表格填报

## Purpose

按院内**空白表格模板**把一项研究填成可递交的伦理材料包。核心是填表，不是另写一套方案。
**铁律：只替换文字，不改版式。** 禁止另起空白 Word 重做表格。

## Capability map

| Task | Path |
|------|------|
| **填表（本技能）** | 下面工作流 + `scripts/docx_cell_replace.py` / `word_find_replace.py` |
| 金山医院空白包、递交清单、栏目 | `references/jinshan-form-pack.md` |
| 填完自检 | `references/checklist.md` |
| 研究类型 / 入排 / 终点 / 样本量口径 | `03_research` — 缺设计先问用户或走 03，不在本技能里发明 |
| 统计 / 样本量公式 | `04_analysis` |
| 知情同意通俗正文、论著里的伦理段落 | `05_manuscript` `radiology-ethics` — 本技能只把已定正文填进表 |
| Excel 登记表 | `01_automation` 若 COM/xlsx 脚本不够用 |

## Modes

- `fill` — 默认。复制空白包 → 按参数填 0–6 号表
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

1. 母版用金山 `0空白/临床研究-伦理初始审查申请.zip`，不用 `伦理/`、`填写好/` 里的已填样例。
2. 方案+知情共 5 份模板，**五选一**（干预方案 / 观察方案 / 干预知情 / 观察知情 / 免知情）。切勿全交，切勿交空白。
3. 先输出规划表（题目、PI、类型、n、期限、版本、文件清单、待补项）。用户同意后再写文件。
4. 复制 `0空白` zip 内文件，并加上工作夹的立项申请表，到 `填写好_<PI>_<短题>/`，**不覆盖**母版。
5. 保格式填：`.docx` 用 python-docx（只改文字/勾选，保留签名表）；`.doc` 用 Word/WPS COM 查找替换，一次只开一个；`.xls` 只改数据行。
6. 按 `references/checklist.md` 自检后交付路径、参数摘要、待签字项。

登记表只发伦理邮箱、不打印。初审申请表 PI 手签、日期写递交当天。干预性研究团队须有医生。观察性自选课题可豁免科学性审查批件。细节见 `references/jinshan-form-pack.md`。

一并填写工作夹里的 `1-研究者发起的一般临床研究立项申请表.doc`（官方空白 zip 没有这份，母版用 `伦理/` 工作夹里的空白/近空白件，填前清掉旧课题）。开题提纲仍不是伦理初审材料。

## Not this skill

- 选题 / 写研究设计 / 选刊 → `03_research`
- 写论著 Methods 伦理段、去 AI、配图 → `05_manuscript`
- 评阅 / 回审稿 → `06_review`
- 编造伦理批号、学历、GCP、未提供的团队成员

## Progressive disclosure

只发现本 `SKILL.md`。栏目和递交清单一律读 `references/`，不要把医院 Word 原件推进公开仓库。
