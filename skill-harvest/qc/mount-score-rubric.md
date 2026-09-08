# Mount / reviewer score rubric（评分标准 · skills 质控）

人读的**评分表**（谁几分、哪篇稿）不放这里——给人看的结果表进 skill-library 归档或本地报告。  
本文件只定义**尺子**：维度、锚点、意见 vs 兑现、何时据此提议改 `mounts/presets`。

**评分主键 = `源/包内skill-id`**（可附粗 ID）。默认禁止只打「Nature / Scientific 整包总分」作为换芯依据；整包汇总仅可作附录（由 skill 分聚合）。旧四稿整包分标为历史、不可比。

被动记录；改默认配方或换 Nature/Scientific 路径须用户明确同意。禁止 `OBSERVED → AUTO MODIFY`。

## 适用

- 比较挂载源 / 审稿角色在真实稿件批注上的表现
- 复盘后决定是否 bump `review-hybrid-default` 的换芯行
- 与执行门控分工：G-06 / G-FACT 仍在 `00`；本尺不替代 Issue Card

## A. 意见质量（0–10）

| 维度 | 10 锚点 | 0 锚点 |
|---|---|---|
| 研究方法细节 | 可操作的方法学缺口，能指向改 Methods | 空泛或与方法无关 |
| 数据准确性 | 可复核的表/数冲突，最好带正确来源线索 | 无核验、或引入错误数 |
| 写作逻辑一致性 | 叙述方向与数值/机制交叉核对 | 只改措辞级挑剔 |
| 文献引用正确性 | 相关性和标识（DOI/PMID/主题）都查 | 不做文献，或只查格式 |
| 报告规范完整性（可选单列） | STROBE/TRIPOD 等可勾项 | 忽略报告骨架 |
| 不臆造原则（可选单列） | 缺证据就标未知/问用户 | 脑补结果或静默改数 |

**你关心的 4 项均值**（默认）：方法细节、数据准确性、写作逻辑、文献引用。  
后两项报告规范 / 不臆造可单列，**默认不进均值**（避免专项角色被综合分淹没；如 `03-lit-search` 应看文献专项分）。

## B. 回复兑现（对照 `review-resolution`）

对「该角色自己提出的」Major/Blocking：

| 状态 | 含义 |
|---|---|
| Resolved | 方法/结果/表图/结论均已对齐，无依赖修复前说法 |
| Partially resolved | 有改动但实质问题仍在，或缺二次回读 |
| Unresolved | 未改或仅换说法 |
| New issue | 本轮介入引入新错误（极严重） |

**回复综合分建议：** 以 Blocking 清零为主；Partial 上限约 5；出现 New issue ≤ 2。

## C. 记录与进化

1. 可选：把一次复盘摘要追加到 `skill-harvest/data/qc-events/`（`error_type: mount-score-review` 或笔记型事件）。
2. 用户说 进化 / 更新技能建议 / 总结 QC 时，可在 evolution HTML 中提议：**只改 preset yaml 的 path/source**，不改粗 ID，不批量 MOUNTED。
3. 评分表正文给人看；不要把分数写进 `gates.md`。

## D. 与现行默认配方的关系

现行默认见 `01_skill-discovery-integration/mounts/presets.md`（Nature 主外挂 + Scientific 批判叠加 + B 底盘）。  
本尺用于验证该默认是否仍划算；ARS / 带外编辑工具不纳入默认候选集。
