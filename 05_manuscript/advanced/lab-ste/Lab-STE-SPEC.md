# Lab-STE 可控语言规范

**版本：** 0.2.1
**日期：** 2026-10-03
**状态：** 实验室内部规范（给人读；阈值与词表在配置文件）
**不是：** ASD-STE100 译本或摘录。规则按本实验室设计重写。例句自撰，不抄官方。

| 文件 | 作用 |
|---|---|
| 本文件 | 规则、格式、冲突、场景、验证 |
| `config.yaml` | 全部阈值、场景开关、冲突顺序 |
| `approved-en.tsv` | 英文批准词典（949 词元，通用词） |
| `term-lock-default.tsv` | 领域通用词默认锁定模板（patient、feature、slice、reader 等） |
| `lexicons/` | 去 AI、名词化、模糊词、四字格 |
| 课题 `term_lock` | 专业术语对照（不进批准词典） |

---

## 0. 范围与非目标

Lab-STE 管**怎么写得可检测、可改、不改事实**。它不管统计是否做对、文献是否存在、伦理号是否真实。那些仍走 03/04/05/06 与 Gate。

本版先落地两个场景档案：

1. `manuscript-methods-en` — 英文 Methods
2. `review-comment-zh` — 中文审稿/写作批注

`llm-reply-zh` 与 `manuscript-id-en` 已在配置里占位，默认后开。

**批准词典不收录专业英语。** 成像、疾病、解剖、统计量、设备名、软件名、指南名一律进课题术语锁定表，不进 `approved-en.tsv`。

**领域通用词走默认锁定模板。** `patient`、`feature`、`slice`、`reader`、`image`、`scan`、`cohort`、`dataset` 这类每个课题都要用、又不属于通用操作词的名词，登记在 `term-lock-default.tsv`。检查时按已锁定词计，不要求每个课题重新登记。

---

## 1. 核心设计原则

1. **一词一义。** 同一概念全文只用一个词。未登记的近义替换视为不一致。已登记术语必须重复，不得为了“避免重复”而换词。
2. **一句一事。** 一个句子只承载一个动作或一个判断。
3. **动作用动词。** 禁止“进行/开展 + 动词性名词”和 `perform an analysis of` 一类名词化。
4. **指代明确。** `it / this / these / 其 / 该 / 这 / 此` 必须能唯一回指；不能则重复名词。
5. **可检测。** 每条规则必须能写成程序条件（阈值、正则、词表或结构计数）。不能检测的条目不进规范。
6. **有例外。** 术语、引文、数字与单位、代码块默认不检查。见 §3 豁免。

---

## 2. 规则条目统一格式

每条规则使用同一字段，便于配置化与统计。

| 字段 | 含义 |
|---|---|
| ID | 稳定编号，如 `EN-S01`、`ZH-NOM01`、`CM-01` |
| 语言 | `en` / `zh` / `both` |
| 场景 | 配置里的 profile 名；空=所有已启用档案 |
| 检测 | 句长 / 词表 / 正则 / 结构 |
| 严重度 | `must_fix` / `should_fix` / `hint`（档位名在配置，本文件不写死数字） |
| 正例 | 自撰，一条 |
| 反例 | 自撰，一条 |
| 豁免 | 默认豁免之外的本条例外 |

严重度如何映射到必须改/建议改/提示：见 `config.yaml` → `severity`。

---

## 3. 默认豁免（所有规则）

不检查：

- 围栏代码与行内代码
- 引号内引文
- 文献条目与文内编号引用跨度
- 公式
- 纯数字单元格
- 术语锁定表中的规范形与已列别名
- 数字 + 单位（单位格式仍受 `ZH-PUN01` / 数字体例约束，但批准词典覆盖率不计入这些词）

---

## 4. 英文规则（EN）

适用稿件 Methods（高）、Introduction/Discussion 仅可读性子集（低）。邮件可复用 Methods 的句长与指代，不强制词表。

**例句的词汇来源。** 英文例句只用批准词典中的词，加上 `term-lock-default.tsv` 中的领域通用词。另假定课题锁定表含 `logistic regression`、`nomogram`、`AUC`、`calibrate`、`covariate`、`radiomics`。`tools/check_spec_examples.py` 逐条核对正例，失败即改例句，不改词典凑数。

### EN-S01 句长

- **语言 / 场景：** en；Methods 步骤句用 `sentence_words_step_max`，描述句用 `sentence_words_desc_max`。
- **检测：** 按空白切词，计词数。步骤句启发式：句首动词，或含 `then` / 序号。
- **严重度：** 超过步骤上限 `must_fix`；超过描述上限 `should_fix`。
- **正例：** `We drew a region on the largest slice.`
- **反例：** `We then carefully and subsequently performed the drawing of a region of interest on the slice that was considered to be the largest after a visual comparison of adjacent slices.`
- **豁免：** 纳入/排除标准的分号列表可按配置改用描述上限。

### EN-V01 语态

- **语言 / 场景：** en。默认主动；施动者不重要或不可知时保留被动。
- **检测：** 结构：`be` + 过去分词。Methods 被动比上限按档案的 `methods_voice` 取键：`ste_active` 用 `passive_ratio_methods_max_ste_active`，`conventional_passive` 用 `passive_ratio_methods_max_conventional_passive`（映射在 `passive_ratio_key_by_voice`）。其他档案用 `passive_ratio_other_max`。
- **严重度：** 有明确施动者仍用被动 → `should_fix`。
- **正例：** `Two readers drew the region.` / `Patients were randomized.`
- **反例：** `The region was drawn by two readers.`（施动者已知且重要）
- **豁免：** 配置 `methods_voice: conventional_passive` 时，Methods 被动不因本条必改。该开关用于对齐 05 现行体例，与本条默认不同，冲突见 §8。

### EN-L01 一词一词性、一词一义

- **语言 / 场景：** en；`manuscript-methods-en` 对批准词典做覆盖检查。`manuscript-id-en` 默认关闭覆盖，只做概念别名检查。
- **检测：** 词表；一词多 POS 以词典行的 `pos` 为准，同形不同类须分行。未登录词且不在术语锁定、数字、专名中 → 命中。
- **严重度：** 未登录词 `should_fix`；同一概念两个未锁定写法 `must_fix`。
- **正例：** 全文只用 `use`，不用 `utilize`。
- **反例：** 上一段 `use the tool`，下一段 `utilize the tool`。
- **豁免：** 术语锁定；软件界面字符串。

### EN-VB01 动词：少短语动词、少多义、少名词化

- **语言 / 场景：** en。
- **检测：** 短语动词表计数 / 千词；名词化表正则；`perform/conduct/make/take + a/an + 名词`。改写目标动词（如 `analyze`、`evaluate`、`extract`）已在批准词典。名词 `analysis` 可用，但不得接 `perform`、`conduct`、`carry out`。
- **严重度：** 名词化 `must_fix`；短语动词超阈 `should_fix`。
- **正例：** `We extracted features.`
- **反例：** `We performed an extraction of features.` / `We carried out the analysis.`
- **豁免：** 固定方法名（若已锁定）。

### EN-R01 指代

- **语言 / 场景：** en。
- **检测：** `It/This/These` 独立作主语。需要前一句有唯一名词先行语。
- **严重度：** `must_fix`。
- **正例：** `The nomogram had a higher AUC. The nomogram did not calibrate in the test set.`
- **反例：** `The nomogram had a higher AUC. This was not adequate.`
- **豁免：** `This study` 在摘要首句若档案允许；默认 Methods 不允许。

### EN-N01 名词串

- **语言 / 场景：** en。
- **检测：** 连续名词（不含 of 结构）个数 > `noun_stack_max`。
- **严重度：** `should_fix`。
- **正例：** `score of radiomics features`
- **反例：** `radiomics feature selection model performance score`
- **豁免：** 已锁定多词术语按一个词计。

### EN-T01 时态

- **语言 / 场景：** en。
- **检测：** Methods/Results 以过去时为主；普遍事实现在时。`tense_mix_same_subsection` 为真时，同一小节同时出现过去时限定动词与现在时限定动词即 `should_fix`。
- **严重度：** `should_fix`。
- **正例：** `We fitted the model. A byte has eight bits.`
- **反例：** `We fit the model and report that patients are being scanned tomorrow.`（步骤与未发生的事混在一句）
- **豁免：** `figure_present_tense_ok` 为真时，`Figure N shows` 允许现在时。

### EN-C01 从句与 which

- **语言 / 场景：** en。
- **检测：** 从句数 > `subordinate_clauses_max`；非限制性 `which` 计数。
- **严重度：** 多从句 `must_fix`；补充性 which `should_fix`。
- **正例：** `We used logistic regression. Age was a covariate.`
- **反例：** `We used logistic regression, which was selected after a comparison that included age, which was coded as a continuous variable.`
- **豁免：** 限制性 that 从句一条以内。

---

## 5. 中文规则（ZH）

中文无词形变化，风险在歧义与冗长。

### ZH-S01 句长与逗号子句

- **检测：** 句号/问号/叹号切句；汉字数 > `sentence_chars_max`（`review-comment-zh` 用 `sentence_chars_comment_max`，由档案的 `sentence_chars_key` 指定）；逗号切分的子句数 > `comma_clauses_max`。
- **严重度：** `must_fix`。
- **正例：** `在 Methods 第二段写明连续入组。`
- **反例：** `在仔细阅读全文并对照结果页之后，建议作者在方法、结果与讨论三处同时补充连续入组、排除标准与流程图，从而使读者能够理解队列是如何形成的。`
- **豁免：** 引用整句；批注修改建议行中引号内的补写文本（按引文跳过）。

### ZH-SUB01 主语完整

- **检测：** 连续无主语句段（逗号或句号后无名词/代词主语）长度 > `dropped_subject_run_max`。
- **严重度：** `must_fix`。
- **正例：** `作者未报告扫描参数。作者也未报告重建核。`
- **反例：** `未报告扫描参数，未写重建核，未给 b 值，未说明方向数。`
- **豁免：** 祈使句批注的修改建议行（见 CM-01）允许无主语句。

### ZH-R01 指代

- **检测：** `该/其/此/这` + 名词或单独 `其`。前一句必须能唯一对齐对象。
- **严重度：** `must_fix`。
- **正例：** `列线图的 AUC 为 0.84。列线图在测试集未校准。`
- **反例：** `列线图和临床模型都报告了 AUC。其并未校准。`
- **豁免：** `该研究` 作为标题后首句，若对象唯一。

### ZH-NOM01 名词化

- **检测：** 词表 `进行/开展/实施/做出 + 动词性名词`。
- **严重度：** `must_fix`。
- **正例：** `提取特征。`
- **反例：** `进行特征提取。`
- **豁免：** 法规或指南固定搭配（须写入术语锁定）。

### ZH-DE01 长定语

- **检测：** 同一名词短语内 `的` 连续嵌套层数 > `de_nest_max`。
- **严重度：** `should_fix`。
- **正例：** `测试集上的 AUC。该 AUC 来自联合模型。`
- **反例：** `来自联合模型的测试集上的未经校准的预测概率的均值的差异。`
- **豁免：** 机构正式名称。

### ZH-BEI01 被动

- **检测：** `被` 字句。有明确施动者且施动者重要 → 改主动。
- **严重度：** `should_fix`。
- **正例：** `两名医师勾画病灶。` / `患者被随机分组。`
- **反例：** `病灶被两名医师进行了勾画。`
- **豁免：** 施动者未知。

### ZH-Q01 量化

- **检测：** 模糊词表（较大、明显、一定程度 等）。
- **严重度：** `must_fix`。
- **正例：** `测试集 AUC 比临床模型高 0.07。`
- **反例：** `测试集表现有较大提升。`
- **豁免：** 词表 `exempt_if` 列。

### ZH-ID01 书面套话与四字格

- **检测：** 成语/套话表密度 / 千字。
- **严重度：** 超阈 `should_fix`。
- **正例：** `这项研究是单中心回顾。`
- **反例：** `本研究应运而生，具有至关重要的临床意义。`
- **豁免：** 患者原文引语。

### ZH-TERM01 术语对照

- **检测：** 课题术语表。首次：全称 + 缩写；此后只用缩写。中英混用别名计数 > 1 → 不一致。
- **严重度：** `must_fix`。
- **正例：** `intravoxel incoherent motion (IVIM)` 首次，其后 `IVIM`。
- **反例：** 同段交替 `IVIM` / `体素内不相干运动` / `IVIM 成像`。
- **豁免：** 题名可保留全称。

### ZH-PUN01 标点与数字单位

- **检测：** 中文语境出现 ASCII `,` `.` `:` 作句读；数字与单位之间空格策略与全文不一致。
- **严重度：** `should_fix`。
- **正例：** `间隔 2 mm。`
- **反例：** `间隔2mm,然后重建.`
- **豁免：** 英文专名、DOI、代码。

---

## 6. 去 AI 规则（四层）

不要只做绝对黑名单。多数条目用**频率阈值**。字段固定：替换建议、可豁免场景、触发阈值（次/千词或千字）。词表在 `lexicons/de-ai-*.tsv`。

### AI-L01 词汇层

- **检测：** 词表命中 / 千词（英）或 / 千字（中）。
- **严重度：** 阈值为 0 的条目 `must_fix`；其余超阈 `should_fix`。
- **正例：** `We used logistic regression.`
- **反例：** `We leveraged a pivotal framework to delve into the tapestry of the data.`
- **豁免：** 行内 `exempt_if`。

### AI-S01 句式层

- **检测：** 三段并列；`不是……而是……` / `not X, but Y`；段首空总述；空泛升华结尾。
- **严重度：** `should_fix`。
- **正例：** `测试集未做外部验证。`
- **反例：** `这不仅是方法问题，而是关乎未来诊疗格局的深刻命题。`
- **豁免：** 真纳入/排除三条（计数器不记这类规定列表）。

### AI-D01 篇章层

- **检测：** 连续段首句式相同超过 `para_openers_same_pattern_run_max`；段落长度变异系数低于 `para_length_cv_min`；以总结句收尾的段落比例过高。
- **严重度：** `hint`（误报高，先提示）。
- **正例：** 长短段混排，段首动词变化。
- **反例：** 每段都以“综上所述，本研究表明……”收尾。
- **豁免：** Methods 逐步操作可以同构（档案可关此条）。

### AI-F01 格式层

- **检测：** 破折号密度、加粗密度、额外小标题、列表占比。
- **严重度：** 破折号在 `emdash_must_fix_profiles` 所列档案（默认两个稿件档案）`must_fix`；其余档案和其余子项 `should_fix`。
- **正例：** 中文批注连续成段，一条一个问题。
- **反例：** 一条批注拆成五个加粗小标题加项目符号。
- **豁免：** IMRAD 规定标题；真枚举。

---

## 7. 批注体例（专章）

场景 `review-comment-zh`。一条批注只写一个问题。Word 作者字段仍为 **A**（实验室硬规则，本规范不改）。

固定五槽，顺序不可换：

1. **位置** — 行号或 `节, 段, 句` / 图 / 表。
2. **问题** — 错什么，一句。
3. **依据** — 规则 ID 或数据源（结果页、术语表）。
4. **修改建议** — 以动作动词开头，可直接粘贴或执行。
5. **严重度** — `must_fix` / `should_fix` / `hint`。

### CM-01 批注五槽

- **语言 / 场景：** zh；`review-comment-zh`。
- **检测：** 先按 `source_tag_strip` 剥文首来源标签，再按 `comment_schema.slots` 用句号切槽。槽 1 匹配 `location_patterns`；只命中 `location_coarse_patterns` 为过粗。槽 3 以 `basis_prefix` 开头，且须命中 `basis_source_patterns`（规则 ID 或数据源）。槽 4 首词在 `action_verbs` 内，且不含 `vague_phrases`。槽 5 为三档严重度之一。槽 2：句号数大于 `multi_problem.max_sentences`，或命中 `conjunction_re`，判一条多问。
- **严重度：** 缺槽、顺序错、位置两表都不中、建议不可执行、一条多问 `must_fix`；位置过粗 `should_fix`。
- **正例 / 反例：** 见下。
- **豁免：** 引号内的补写文本不计句长。Word 作者字段由 `word_author_field` 固定，不属本条检测。来源标签剥掉后不参与切槽。

**正例：**

> Methods 第 2 段第 1 句。未写连续入组。依据 ZH-TERM01 与结果页队列句。补写：连续纳入 2019 年 1 月至 2022 年 12 月的病例。must_fix。

**反例：**

> 方法部分整体不够清晰，建议完善并提升规范性，同时注意语言润色。

禁止：一条批注堆多个互不相关问题；建议不可执行（“酌情修改”“适当补充”）；用去 AI 套话写批注。

与 06 审稿信封的关系：信封条目用英文 `Lines n–m: + defect + Please…`。中文五槽用于稿面批注。二者都遵守一句一事。

---

## 8. 冲突优先级

程序按此顺序裁决（配置键 `conflict_order`）：

1. **术语锁定、数值、统计量、引文** — 不动。
2. **事实准确性** — 改写不得改变含义，不得增删否定。
3. **STE 可读性规则**
4. **去 AI 规则**

典型冲突：STE 要求重复固定名词，去 AI 要求避免重复。
**裁决：** 名词重复豁免只对**已登记术语**生效。未登记名词仍鼓励变化，但不得换成未登录的多义词充数。

与 05 去 AI 规范的已知分歧：05 要求 Methods 保持被动。本规范默认 `EN-V01` 主动优先。稿件若走 Ying Li 体例，把该档案 `methods_voice` 设为 `conventional_passive`，被动比例阈值会自动换键。不要改数字去“打平”两条规则。

---

## 9. 场景档案（Profile）

同一规则集，强度按档案变。阈值只在 `config.yaml`。

| 档案 | 语言 | STE | 去 AI | 备注 |
|---|---|---|---|---|
| `llm-reply-zh` | 中文 | 中 | 高 | 格式层和套话 |
| `review-comment-zh` | 中文 | 高 | 中 | 五槽批注 |
| `manuscript-methods-en` | 英文 | 高 | 低 | 步骤句最严 |
| `manuscript-id-en` | 英文 | 低（可读性子集） | 高 | 不强制批准词表 |

本版实施顺序：先 Methods 与中文批注，再扩展另外两个。

---

## 10. 批准词典（英文，949 词元）

- 路径：`approved-en.tsv`（`lemma / pos / sense / note`）。
- 词元列表：`approved-en.lemmas.txt`。
- **收：** 功能词、普通操作动词、普通形容词/副词、文书与度量名词、数词、通用单位。
- **不收：** 专业英语（病名、解剖、序列名、具名指标、设备、软件、指南）。
- **文件规范：** UTF-8、LF 换行；每行 4 列；同一 `lemma + pos` 只许一行；`sense` 只写一个意思，用法提醒写进 `note`。
- **词元数与条目数分开记：** 949 词元，1091 条目（多词性分行）。
- **一词一行 POS。** 需要两种词性则两行，各锁一个意思。
- **覆盖率：** 仅 `manuscript-methods-en` 默认计算。其他档案可关。
- 未登录词的处理：改为登录词，或登记进术语锁定，禁止用专业近义堆砌充覆盖率。

### 词汇三层

| 层 | 文件 | 收什么 | 谁维护 |
|---|---|---|---|
| 批准词典 | `approved-en.tsv` | 功能词、通用操作词、评审词 | 实验室，变更记 CHANGELOG |
| 默认锁定模板 | `term-lock-default.tsv` | 领域通用名词；通用描述统计（mean、median） | 实验室 |
| 课题锁定表 | 课题 `term_lock` | 病名、序列、具名指标（AUC、HR、OR）、软件、设备 | 各课题 |

**增词准入。** 只问一件事：这个词是否是任何领域都会用的操作词或评审词。是，进批准词典；否，进某一层锁定表。批准词典增词必须在 CHANGELOG 里写一句来源场景。

词典不是 ASD-STE100 词表副本，也不从 0doc 稿件频率表直接倒专业词。0doc 只用来确认实验室行文需要哪些**通用**操作（如 `report`、`compare`、`add`）。

---

## 11. 验证指标

没有指标就不能改阈值。每次抽检至少报告：

| 指标 | 算法要点 |
|---|---|
| 平均句长 | 词或字，按语言 |
| 超长句比例 | 相对对应上限 |
| 术语一致率 | 1 −（同概念写法数−1）/ 出现次数 |
| 被动句比例 | be+V-ed 或“被”字句 / 句数 |
| 名词化命中数 | 词表 |
| 去 AI 命中 / 千词或千字 | 分层：词汇/句式/篇章/格式 |
| 语义保持 | 改写前后数字、锁定术语、否定词集合不变 |
| 词典覆盖率 | （批准词典 + 默认锁定 + 课题锁定命中词）/ 总词数，只在 `manuscript-methods-en` 计算 |
| 例句自检 | 规范正例全部通过词典与锁定表（`tools/check_spec_examples.py`） |
| 误报率 | 人工抽样；反向改配置，不改事实 |

语义保持失败视为冲突层 1–2 失败，不得用 STE 或去 AI 分数开脱。

---

## 12. 与现有技能包的对齐

| 包 | 关系 |
|---|---|
| 旧 personal 去 AI 档案（已退役，不在本仓） | 去 AI 词与禁 em-dash 的入口。本规范把阈值外置，便于对版本。 |
| 旧 stop-slop 档案（已退役） | 通用 hygiene；医学覆盖条款仍优先于其博客规则。 |
| 旧 ai-writing-detector 档案（已退役） | 只在用户要检测报告时用。本规范的 AI-* 规则是可配置检查，不是检测器分数。 |
| 旧 forbidden-phrases 档案（已退役） | 实验室硬禁词。阈值为 0 的去 AI 条目应与之同向，冲突时硬禁词优先。 |
| 旧 06 批注作者档案（已退役，不在本仓） | 批注作者 A、来源前缀、一行一条。CM-01 补中文五槽，不取代信封。 |

版本号与 `config.yaml` 的 `version` 同步。变更记 `CHANGELOG.md`。

---

## 13. 实施建议（规范附属，非规则）

1. 先接两个档案的检查器：英文 Methods、中文批注。
2. 阈值和词表只改配置与 TSV，不改规则 ID。
3. 例句继续用本实验室场景自撰，避免版权与领域脱节。
4. 专业词增长只加术语锁定，不加批准词典。
5. 误报先降严重度或加豁免，再删规则。
6. 改 TSV 后先跑 `tools/check_spec_examples.py`，再改版本号。
