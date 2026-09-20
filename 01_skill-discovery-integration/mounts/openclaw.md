# OpenClaw · reference-only（provenance / license mixed）

[总览](README.md) · [OpenClaw · reference-only](openclaw.md)

来源 [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) · 配置 `../sources/openclaw-medical-skills.proposed.yaml` · 扫 `b1f9b6e`

| | |
|---|---|
| 状态 | PROPOSED · **reference-only**（禁止 atomic mount） |
| v4 政策 | **Never** use OpenClaw as `atomic_skill` source for any fine ID |
| 真正原因 | 聚合仓：README/badge 常写 MIT，但部分 skill 文件含 All Rights Reserved / proprietary；缺少可作为**整包**统一许可边界的根 LICENSE。不是“平台特殊”四个字，而是 **provenance/license surface 不可整包信任** |
| 正确用法 | 仅作发现线索 → 追溯真正上游 skill → 按上游 LICENSE 单独挂载 |

## 说明

v4 起 OpenClaw 仅保留审计轨迹与历史映射。**不得** on-demand mount 进会话。若某能力可证明来自独立 MIT/Apache 上游，应挂该上游，而不是经 OpenClaw 聚合包取字节。

机器真源 `../registry.yaml`（`openclaw_policy: never-mount-as-atomic-source`）。
