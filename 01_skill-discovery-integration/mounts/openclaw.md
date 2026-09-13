# OpenClaw · 禁挂载（license risk）

[总览](README.md) · [OpenClaw · 禁挂载](openclaw.md)

来源 [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) · 配置 `../sources/openclaw-medical-skills.proposed.yaml` · 扫 `b1f9b6e`

| | |
|---|---|
| 状态 | PROPOSED · **license-risk-reference-only** |
| v4 政策 | **Never** use OpenClaw as `atomic_skill` source for any fine ID |
| 原因 | 仓库内多处 “MD BABU MIA, PhD” proprietary 声明，与 README MIT 矛盾（见 registry governance） |
| 历史映射 | v3 曾映射 23 / 30；空挂 7：`02-imaging-qc`、`02-fmri`、`03-lit-fulltext`、`05-write-reporting`、`05-write-venue`、`05-humanize`、`06-review-response` |

## 说明

v4 起 OpenClaw 仅保留审计轨迹与历史映射（含 `pubmed-search`、`clinical-trial-protocol-skill`、`radiomics-pathomics-fusion-agent` 等）。**不得** on-demand mount 进会话。clinical-reports not included as a writing mount.

机器真源 `../registry.yaml`（`openclaw_policy: never-mount-as-atomic-source`）。
