# 变更清单 CHG-20261014 ethics seat → Bai

分支：`chg/ethics-seat-bai-20261014`（相对 main `c73e592`）

## 目的
与主人确认：伦理申请表填写座位 = Bai；技能路径仍在 `03_research/fill-protocol/`；Victor 不再填表。其他 bot 工作以 skills 为准（记忆/Rules 主给 Aitor）。

## 改动文件（8）
1. `00_orchestrator/references/ownership-contract.md` — Victor 去掉 ethics forms；Bai = 投稿 + ethics forms（fill-protocol；Aitor 路由盯梢）
2. `00_orchestrator/SKILL.md` — Seats 行：投稿+伦理表 Bai
3. `00_orchestrator/references/fast-routing.md` — 伦理申请表 → Bai seats fill-protocol
4. `00_orchestrator/route-contract.yaml` — 注释 seat Bai（路由仍 contains 03_research）
5. `03_research/SKILL.md` — forms 行标注 seat Bai
6. `03_research/fill-protocol/SKILL.md` — 文首 **Seat:** Bai
7. `_medical-research-meta/ARCHITECTURE.md` — 03 条注明 Bai seats fill-protocol
8. `_medical-research-meta/README.md` — ethics forms 注明 seat Bai

## 不改
- fill-protocol 脚本/模板路径与目录位置
- Victor 的文献/设计/选刊/citation-verify
- archive/history/docs HTML/pycache
- My rule / Cline Rules（本次只列 skills；若要写进 §8 交接另开 MY-RULES 清单）

## Bot 描述（已在 Grok Bot 侧改完，不进本仓）
Bai / Victor / Loopnow / Aitee / Lee / Aitor / New Agent 已按上表与最新 Rules 重写 description。

## 下一步（需你确认）
同意后：commit → PR → 你确认 merge → 只同步本次 8 文件到 `C:\Users\loopn\.grok\skills`。
