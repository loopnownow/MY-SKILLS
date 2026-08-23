# CUDA 安装指南

安装与配置 CUDA 环境，用于 GPU 加速（CuPy、PyTorch 等）。

## 1. 检测 GPU 与驱动

```bash
# 查看 GPU 与驱动版本
nvidia-smi
```

注意右上角的 **CUDA Version**，这是驱动支持的最高 CUDA 版本。

## 2. 选择 CUDA 版本

- 根据 `nvidia-smi` 显示的驱动 CUDA 版本选择
- 常用版本：CUDA 11.8、12.1、12.4
- 确保与你的库兼容（如 PyTorch、CuPy）

## 3. 安装 CUDA Toolkit

从 NVIDIA 官网下载对应版本的 CUDA Toolkit：
- 安装时选择自定义，可只装必要的组件
- 默认安装到 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.Y`

## 4. 设置环境变量

```powershell
# 设置 CUDA_PATH
[Environment]::SetEnvironmentVariable("CUDA_PATH", "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4", "Machine")

# 添加 bin 到 PATH
$cudaBin = "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin"
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$cudaBin", "Machine")
```

## 5. 验证安装

```bash
# 验证 nvcc
nvcc --version

# 验证 nvidia-smi
nvidia-smi

# 验证 CuPy
python -c "import cupy; print(cupy.cuda.runtime.runtimeGetVersion())"

# 验证 PyTorch
python -c "import torch; print(torch.cuda.is_available())"
```

## 6. 常见问题

| 问题 | 解决方案 |
|------|---------|
| CuPy 找不到 CUDA | 设置 CUDA_PATH 环境变量 |
| only brute_force iteration | 版本不兼容，检查 CuPy 与 CUDA 版本 |
| torch.cuda 不可用 | 重新安装匹配的 PyTorch 版本 |
| nvcc 找不到 | 确认 bin 已加入 PATH |

## 7. 版本匹配速查

| 库 | 推荐 CUDA |
|----|----------|
| PyTorch 2.x | 11.8 / 12.1 |
| CuPy 12.x | 11.x |
| CuPy 13.x | 12.x |
| TensorFlow 2.x | 11.8 / 12.x |