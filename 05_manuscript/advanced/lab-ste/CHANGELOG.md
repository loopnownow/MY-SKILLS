# Changelog — Lab-STE

## 0.2.1 — 2026-10-03

- 脚本移入 `tools/`（`parent.parent` 指向 Lab-STE 根）。例句检查改为整词短语匹配锁定项。
- 批准词典删除 `mean` 的 adj/n 统计量义，保留动词义；T-MEA/T-MED 留在默认锁定。§10：通用描述统计在默认层，具名指标进课题表。现 949 词元、1091 条目。
- CM-01：切槽前剥来源标签；补 `location_coarse_patterns`、`basis_source_patterns`、`multi_problem`。
- EN-T01：`tense_mix_same_subsection`（同一小节过去时与现在时并存即标记）。

## 0.2.0 — 2026-10-03

- 词典：新增 49 个通用词元（analyze、assess、acquire、evaluate、validate、verify、extract、sample、predict、train、analysis、outcome、evidence、limitation、reviewer、consistent 等，来源场景：Methods 操作句与审稿批注）。现为 949 词元、1093 条目。
- 词典修正：删除 `figure`、`table` 两条旧的双义行（已有单义替代行）；约 70 行 “A; or B” 双义改为单义，用法提醒移入 `note`；补齐两条只有 3 列的行；全表改为 LF 换行并按词元排序。
- 新增 `term-lock-default.tsv`：领域通用词默认锁定模板（patient、feature、slice、reader、image、scan 等 21 条）。
- 例句：EN-T01 正例改用词典内的词；EN-* 正例统一由 `tools/check_spec_examples.py` 核对。
- 配置：`passive_ratio_methods_max` 拆成 `_ste_active` 与 `_conventional_passive` 两键，随 `methods_voice` 自动取键；新增 `sentence_chars_comment_max`（批注句长）、`emdash_must_fix_profiles`（破折号 must_fix 的档案）、`comment_schema`（CM-01 的槽、位置正则、动作动词、模糊词）、`dictionary`（覆盖率口径）。
- 规范：CM-01 补成标准规则条目；§10 增加词汇三层与增词准入；§11 增加词典覆盖率与例句自检；ZH-S01 对批注补写文本豁免。
- 文件名统一为 `approved-en.lemmas.txt`。`lexicons/` 本次未改动。

## 0.1.0 — 2026-10-03

- 首版规范：核心原则、统一规则格式、EN/ZH/去 AI 四层、冲突优先级、四个场景档案（先实施 Methods 与中文批注）。
- 英文批准词典 900 词元：功能词与通用操作词；不收录专业英语。
- 阈值与词表外置到 `config.yaml` 与 `lexicons/`。
- 批注五槽：位置 → 问题 → 依据 → 修改建议 → 严重度。
- 对齐说明：旧 personal 去 AI / stop-slop / ai-writing-detector / forbidden-phrases 档案与 06 批注作者字段（这些旧档案已退役，不经技能仓分发）。
