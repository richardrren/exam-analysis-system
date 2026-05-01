# 初中科学试卷分析系统

一个基于AI的初中科学试卷自动分析工具，可以快速生成标准化的试卷细目表。

## 支持平台

- ✅ Windows 10/11
- ✅ 统信UOS / Linux

> **注意**：UOS/Linux版本请参考 [README_UOS.md](./README_UOS.md)

## 功能特性

- 📄 **PDF上传**：选择本地PDF试卷文件
- 🤖 **AI分析**：通过OpenAI兼容API自动分析试卷内容
- 📊 **细目表生成**：自动生成Excel格式的标准化试卷细目表
- ⚙️ **接口配置**：灵活配置API地址、密钥和模型
- 📥 **一键下载**：快速下载生成的细目表

## 环境要求

- Python 3.8+
- Windows 10/11 (本说明文档)

## 安装依赖

```bash
pip install -r requirements.txt
```

另外需要安装 `mineru-open-api`：

```bash
pip install mineru-open-api
```

## 运行程序

### 开发模式运行

```bash
python main.py
```

### 打包成EXE

双击运行 `build.bat`，或手动执行：

```bash
python build.py
```

打包完成后，EXE文件位于 `dist` 目录下。

## 使用说明

### 1. 配置API接口

1. 打开程序，切换到"接口配置"标签页
2. 填写API地址（例如：`https://api.openai.com/v1/chat/completions`）
3. 填写API密钥
4. 填写模型名称（例如：`gpt-4`、`gpt-3.5-turbo`）
5. 点击"保存配置"

### 2. 分析试卷

1. 切换到"试卷分析"标签页
2. 点击"选择PDF文件"，选择要分析的试卷
3. 点击"开始分析"
4. 等待分析完成（查看处理日志）

### 3. 下载细目表

1. 分析完成后，点击"下载细目表"
2. 选择保存位置
3. 完成！

## 项目结构

```
.
├── main.py              # 主程序入口（GUI界面）
├── config.py            # 配置管理
├── pdf_parser.py        # PDF解析模块
├── ai_client.py         # AI API调用模块
├── excel_generator.py   # Excel生成模块
├── requirements.txt     # Python依赖
├── build.py             # 打包脚本
├── build.bat            # Windows打包批处理
└── README.md            # 说明文档
```

## 细目表字段说明

- **题号**：题目序号
- **题型**：选择题/填空题/实验探究题/计算题
- **核心考点**：浙教版初中科学教材官方知识点
- **分值**：题目分值
- **难度等级**：基础/中档/难题
- **易错点**：题目的常见错误

## 注意事项

1. 确保已正确安装 `mineru-open-api`
2. API配置需要正确有效
3. 分析过程需要联网
4. 生成的细目表需要人工审核确认

## 技术栈

- GUI: tkinter
- PDF解析: mineru-open-api
- AI: OpenAI兼容API
- Excel: pandas + openpyxl
- 打包: PyInstaller
