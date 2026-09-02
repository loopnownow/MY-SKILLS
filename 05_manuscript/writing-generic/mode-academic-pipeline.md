# 模式 E — 通用学术论文流水线（浓缩自 academic-paper）

**说明：** 原 `academic-paper` 整包已从 agents 删除；日常只用本浓缩版（模式 E）。深细节以本文件 + `ly-writing-style` 主 SKILL 为准。  
本文件是并入 `ly-writing-style` 后的**可执行浓缩版**。

## 优先级

数据真实 > 期刊格式 > 李瀛语气 > 通用华丽英语。  
若同时是影像预测模型全文 → **优先模式 C**，本模式作通用补充。

## 10 种操作模式

| Mode | 触发 | 产出 |
|------|------|------|
| `full` | 从零写全文 | 完整稿 |
| `plan` | 引导规划 / 不确定结构 | Chapter plan |
| `outline-only` | 只要大纲 | Outline + evidence map |
| `revision` | 按审稿意见改稿 | 修订稿（SCI 论著评阅/回信本身 → `06_review`） |
| `revision-coach` | 解析杂乱审稿意见 | 把回复骨架交给 `06_review` mode-3；本模式只改正文 |
| `abstract-only` | 只要摘要 | 中英摘要 + keywords |
| `lit-review` | 文献综述文 | 注释书目 + 综合 |
| `format-convert` | 转 LaTeX/DOCX/引用格式 | 格式化文件 |
| `citation-check` | 查引用 | 引用审计 |
| `disclosure` | AI 使用声明 | 期刊向 disclosure 段落 |

不确定时默认 **`plan`**。

## 8 阶段（full）

```
0 CONFIG   论文类型/学科/期刊/引用格式/字数/已有材料 → 用户确认
1 RESEARCH 检索策略 + 文献池（可跳过若用户自带文献）
2 ARCH     结构 + 大纲 + 证据映射 → 用户确认大纲
3 ARGUMENT claim–evidence 链
4 DRAFT    分节起草（不编造数据/文献）
5a CITE    引用格式 + DOI 核验
5b ABS     中英摘要独立撰写（非机翻）
6 REVIEW   五维自评（原创/方法/证据/逻辑/写作）最多 2 轮修订
7 FORMAT   Markdown/LaTeX/DOCX 说明
```

## IRON RULES

1. **禁止虚构引用**；每条尽量 DOI 可核  
2. 修订最多 2 轮环；未解项 → Acknowledged Limitations  
3. 全文须含（适用时）：Data Availability、Ethics、CRediT、COI、Funding、AI disclosure、Limitations  
4. 禁止 AI 腔：delve / pivotal / robust / comprehensive / 滥用 em dash / throat-clearing openers  
5. 不编造结果、p、AUC、伦理号  

## 引用格式

默认影像 SCI → **Vancouver + DOI**（与模式 C 对齐）。  
通用：APA7 / Chicago / MLA / IEEE / Vancouver 按用户指定。

## 输出包

1. 正文或当前模式产物  
2. 配置记录 / 大纲 / 主张-证据表（按模式）  
3. 缺失输入列表  
4. 下一步（选刊 → `03_research`；回审 → `06_review`）  

