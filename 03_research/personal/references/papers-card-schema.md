# papers-card-schema

**Absorbed:** 2026-10-23 from `_library/papers/` (9 short cards). Schema + section union only.

## YAML frontmatter fields (all cards)

| field | present |
|---|---:|
| `slug` | 9/9 |
| `author` | 9/9 |
| `doc_type` | 9/9 |
| `doc_title` | 9/9 |
| `source_docx` | 9/9 |
| `source_sha256` | 9/9 |
| `source_format` | 9/9 |
| `fidelity` | 9/9 |
| `n_paras` | 9/9 |
| `n_sections` | 9/9 |
| `mode` | 9/9 |

### Field notes
- `slug`: stable id (`03-<pinyin>-<doctype>`)
- `fidelity`: `final-text` (docx) or `salvaged-text` (doc / docbin)
- `mode`: always `write` in this batch
- `source_docx` / `source_sha256`: point at Word under `{raw_root}\_lab\doc-word\03-research\grants\`
- Body = **verbatim excerpt** with trailing `¶N` paragraph markers — not rewrite

## `##` section union (frequency)

| section | cards |
|---|---:|
| 立题依据 | 9/9 |
| 研究内容 | 7/9 |
| 创新点 | 7/9 |
| 关键技术 | 6/9 |
| 进度安排 | 6/9 |
| 预期成果 | 6/9 |
| 工作基础 | 6/9 |
| 研究方案 | 5/9 |
| 纳排标准 | 4/9 |
| 可行性 | 3/9 |

### Recommended card spine (when drafting new brief)
立题依据 → 研究内容 → 研究方案 → 纳排标准 → 关键技术 → 创新点 → 进度安排 → 预期成果 → 可行性 → 工作条件

## Card inventory

| slug | doc_type | author |
|---|---|---|
| `03-dingyifan-kaitibaogao` | 开题报告 | 丁逸凡 |
| `03-jushuai-shenqingshu` | 申请书 | 鞠帅 |
| `03-lixin-shenqingshu-2017niandu` | 申请书(2017年度) | 李新 |
| `03-lulijuan-kaitibaogao-2018-11` | 开题报告(2018-11) | 陆丽娟 |
| `03-renyingying-linchuangyanjiufangan` | 临床研究方案 | 任盈盈 |
| `03-yanbicong-baogaozhengwen-03ban` | 报告正文(03版) | 颜碧从 |
| `03-yanbicong-boshishengkeyanjihuashu` | 博士生科研计划书 | 颜碧从 |
| `03-yanbicong-shenqingshu` | 申请书 | 颜碧从 |
| `03-yangting-kaitibaogaotigang` | 开题报告提纲 | 杨婷 |

## NOT absorbed
Quoted paragraph bodies inside cards (disease narratives, methods prose, person/hospital capability). Open park or `_corpus` copy when needed.
