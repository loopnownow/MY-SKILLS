# 环境配置检查清单

用于系统性配置与验证开发/科研环境。

## 1. Python 环境
- [ ] Python 版本（`python --version`）
- [ ] pip 可用（`pip --version`）
- [ ] conda 可用（`conda --version`，如使用）
- [ ] 虚拟环境已激活

## 2. GPU / CUDA
- [ ] GPU 检测（`nvidia-smi`）
- [ ] CUDA 版本匹配（`nvcc --version`）
- [ ] CUDA_PATH 环境变量已设置
- [ ] CuPy 可加载（`import cupy`）
- [ ] PyTorch GPU 可用（`torch.cuda.is_available()`）

## 3. 科研软件
- [ ] ANTs 已安装并加入 PATH
- [ ] SPM25 已加入 MATLAB 路径
- [ ] CAT12 已加入 MATLAB 路径
- [ ] DPABI 已加入 MATLAB 路径
- [ ] dcm2niix 可用（`dcm2niix --version`）

## 4. Python 库
- [ ] numpy / pandas
- [ ] nibabel / pydicom
- [ ] pyradiomics
- [ ] scikit-learn
- [ ] ants
- [ ] selenium（如需要）

## 5. R 环境
- [ ] R 版本（`R --version`）
- [ ] 所需包已安装（glmnet、rms、pROC、readxl 等）

## 6. IDE / 插件
- [ ] Obsidian 插件已配置
- [ ] MatrixSpy 已配置（pythonPath 正确）
- [ ] PowerShell 已设为默认终端

---

## 验证命令速查
```bash
# GPU
nvidia-smi
nvcc --version

# Python
python --version
pip list | findstr numpy

# 库导入测试
python -c "import nibabel, pydicom, radiomics"

# MATLAB 路径
# 在 MATLAB 中：addpath('SPM25'); addpath('CAT12'); addpath('DPABI')