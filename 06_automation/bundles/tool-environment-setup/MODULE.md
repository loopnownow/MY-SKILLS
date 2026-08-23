# 工具与环境配置

## 适用场景
- IDE 插件配置（Obsidian、MatrixSpy）
- 环境变量、终端设置（PowerShell）
- CUDA / GPU 环境安装
- 科研软件配置（ANTs、SPM、CAT12、DPABI）
- GitHub 项目安装（rtk、agentmemory、skills、spec-kit、medgemma）
- Python 包安装（pip / conda）

## 核心工作流

### 1. 插件 / 软件配置
```
[Step 1] 找到安装目录/配置文件
[Step 2] 阅读 README 或文档了解配置方法
[Step 3] 修改配置（路径、环境变量）
[Step 4] 验证配置生效
```

### 2. CUDA / GPU 环境
```
[Step 1] 检测 GPU 与驱动
[Step 2] 安装匹配的 CUDA 版本
[Step 3] 设置 CUDA_PATH 环境变量
[Step 4] 验证（nvidia-smi、cupy 加载）
```

### 3. GitHub 项目安装
```
[Step 1] 下载/克隆项目
[Step 2] 阅读 README
[Step 3] 安装依赖（pip install -r requirements.txt）
[Step 4] 配置运行
```

## 关键规则
1. **先读文档**：安装前先阅读 README / 文档，确认 API 与版本兼容性
2. **验证生效**：配置后必须验证（如 nvidia-smi、import 测试）
3. **版本匹配**：确认 CUDA、Python、库版本兼容
4. **软编码**：路径、环境变量作为配置
5. **记录步骤**：记录安装配置过程，便于复现

## 附带的模板
- `scripts/env_checklist.md` — 环境配置检查清单
- `scripts/cuda_install.md` — CUDA 安装指南
