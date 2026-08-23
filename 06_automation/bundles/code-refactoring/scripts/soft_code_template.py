#!/usr/bin/env python3
"""soft_code_template.py - 软编码 + 断点续传 + dry run 模板
功能：展示软编码、断点续传、dry run 的最佳实践
用法：修改配置后运行
"""

import os
import sys
import time
from pathlib import Path

# ==================== 配置区（软编码，置顶） ====================
SRC_DIR = r"F:\data\input"          # 源目录
DST_DIR = r"F:\data\output"         # 目标目录
KEYWORD = "bold"                    # 文件匹配关键词
DRY_RUN = True                      # dry run 模式（True=只打印不执行）
SKIP_EXIST = True                   # 跳过已处理文件（断点续传）
NUM_WORKERS = 4                     # 并行进程数
# ================================================================


def process_file(src_file: Path, dst_file: Path):
    """处理单个文件（示例：复制）"""
    # 实际处理逻辑
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    dst_file.write_bytes(src_file.read_bytes())


def main():
    src = Path(SRC_DIR)
    dst = Path(DST_DIR)

    # 收集待处理文件
    files = [f for f in src.rglob(f"*{KEYWORD}*") if f.is_file()]
    print(f"发现 {len(files)} 个待处理文件")

    # 断点续传：过滤已处理文件
    if SKIP_EXIST:
        todo = []
        for f in files:
            rel = f.relative_to(src)
            dst_file = dst / rel
            if not dst_file.exists():
                todo.append((f, dst_file))
        print(f"跳过 {len(files) - len(todo)} 个已处理文件，剩余 {len(todo)} 个")
    else:
        todo = [(f, dst / f.relative_to(src)) for f in files]

    # Dry run：只打印不执行
    if DRY_RUN:
        print("\n=== DRY RUN 模式（不实际执行）===")
        for src_file, dst_file in todo:
            print(f"  将处理: {src_file} -> {dst_file}")
        print(f"共 {len(todo)} 个文件将被处理")
        return

    # 实际执行
    for i, (src_file, dst_file) in enumerate(todo, 1):
        try:
            process_file(src_file, dst_file)
            print(f"✅ [{i}/{len(todo)}] {src_file.name}")
        except Exception as e:
            print(f"❌ {src_file.name}: {e}")

    print(f"\n✅ 完成，共处理 {len(todo)} 个文件")


if __name__ == "__main__":
    main()