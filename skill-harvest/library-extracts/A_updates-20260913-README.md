# A_updates.zip reference (NOT applied as Chinese top-level rename)

CHG-20260913-001 deliberately **did not** replace `02_data-processing`…`06_review` with Chinese coarse folders.
Personal layers stay under existing A paths. Use this extract only as a skill-library reference.

# A包(个人层)更新包 — 合并说明

生成日期: 2026-09-13

## 这次改了什么

1. **10个新的粗ID中文文件夹**（文献检索/选题探索/研究设计/正文写作/
   语言润色/数据处理/统计分析/图表呈现/稿件评阅/审稿回复），把原本
   分散在`02_data-processing`~`06_review`里的个人层内容（Markdown规则、
   脚本），按最新讨论的10粗ID方案重新归位。每个文件夹里都有一份
   `SKILL.md`索引，列出"本粗ID下有哪些个人层文件"+"对应哪些B包/
   跨包挂载的细ID"。

2. **新增`顶层风格_我的风格/`文件夹**——把`Aitor-format.md`、
   `stop-slop-core.md`、`de-ai.md`、`corpus-phrase-bank.md`单独切出来，
   不再挂在"05_manuscript"下面。这是有意为之：这四份文件是凌驾于
   "正文写作"和"语言润色"两个粗ID之上的最终权威，不应该被当成
   "正文写作"的子集，物理上独立出来更符合它们的实际地位。

3. **`01_skill-discovery-integration/registry_v4.yaml`**——正式替换
   `registry.yaml`(已归档为`registry_v1_archived.yaml`)，10粗ID+52细ID
   完整结构，每个细ID标注状态(✅B默认/🟡新增挂载/🔵跨包补充/⚪规则参考)。

4. **`00_orchestrator/`原样保留，未做逻辑改动**——但新增了
   `迁移映射表_MIGRATION_MAP.md`，把旧路径引用（gates.md/workflows里
   绑定的具体文件路径、旧编号）跟新结构的对应关系列清楚，需要你自己
   过一遍手动重连（原因见该文件说明：gate逻辑和人格分工的语义边界
   我没有把握替你改，改错比不改风险更高）。

5. **`skill-harvest/`原样保留**——它的进化提案机制本来就该作用在
   细ID层面，registry_v4.yaml的结构变化不影响它的运作方式，只是它
   未来生成的提案需要参照新的细ID命名。

## 合并到你本地仓库的建议顺序

1. 先把10个新粗ID文件夹 + `顶层风格_我的风格/` 复制进你仓库根目录
2. 用`registry_v4.yaml`替换`01_skill-discovery-integration/registry.yaml`
   （建议保留旧版本作为`registry_v1_archived.yaml`，就像这次交付的一样）
3. 确认没问题后，**删除**旧的`02_data-processing`~`06_review`五个文件夹
   （内容已迁移，删除前建议先diff一遍确保没有遗漏）
4. 最后处理`00_orchestrator/gates.md`和`workflows/*.md`的手动重连
   （参照`迁移映射表_MIGRATION_MAP.md`）

## 尚未拍板的一个点

样本量计算（`calc-sample-size`/`statistical-power`）目前归在"研究设计"，
你之前提过也可能更习惯放"统计分析"——`registry_v4.yaml`的
`open_decision_points`字段记录了这个悬而未决项，确认后只需要搬动
两个细ID条目（以及对应的`04_analysis/personal/sample-size.md`文件
从"研究设计"挪到"统计分析"文件夹），不影响其他结构。
