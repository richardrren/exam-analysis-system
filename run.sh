#!/bin/bash

echo "========================================"
echo "初中科学试卷分析系统 - 统信UOS版"
echo "========================================"
echo ""

# 检查Python是否存在
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python 3.8+"
    exit 1
fi

# 检查Node.js目录
if [ ! -d "node/node-v20.10.0-linux-x64" ]; then
    echo "警告: 未找到Linux版Node.js"
    echo "请按照 README_UOS.md 中的说明下载和配置"
    echo ""
    echo "PDF解析功能可能无法正常工作！"
    echo ""
fi

# 运行主程序
python3 main.py
