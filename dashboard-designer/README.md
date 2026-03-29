# Dashboard Designer Plugin

BI驾驶舱设计全流程Plugin，支持从需求分析到高保真UI的完整设计流程。

## 功能特性

- 📄 **多格式输入支持**: PDF/Word/Excel/TXT文档，以及图片输入
- 📊 **汇总层数据模型设计**: 直接服务于看板展示的数据模型
- 🎨 **多种UI风格**: 科技蓝、简约素雅、深色专业、企业商务
- 🔌 **外部设计工具对接**: 支持Figma、墨刀等设计工具
- 🔄 **模块化设计**: 各模块可独立使用，也可组合使用

## 包含Skills

| Skill | 功能 | 调用命令 |
|-------|------|---------|
| `prototype-designer` | 主入口，编排完整流程 | `/prototype-designer` |
| `requirement-analyzer` | 需求分析+数据模型设计 | `/requirement-analyzer` |
| `prototype-generator` | ASCII/HTML原型生成 | `/prototype-generator` |
| `ui-design-engine` | 多风格UI代码生成 | `/ui-design-engine` |

## 安装

```bash
# 复制到Claude插件目录
cp -r dashboard-designer ~/.claude/plugins/

# 重新加载插件
/reload-plugins
```

## 快速开始

### 完整流程

```
/prototype-designer
```
上传需求文档或图片，按提示完成全流程。

### 单独使用

```bash
# 只需要功能设计文档
/requirement-analyzer + 上传需求文档

# 基于已有功能设计生成原型
/prototype-generator

# 基于已有原型生成UI
/ui-design-engine
```

## 输出结构

```
output/{项目名称}/
├── 01_需求分析/
│   ├── 功能设计文档.md
│   └── 数据模型设计.xlsx    # 7个Sheet
├── 02_原型设计/
│   ├── ascii/
│   └── html/
└── 03_UI设计/
    └── ui-code/
```

## 配置外部设计工具

编辑 `input/external/design-tools.yaml`:

```yaml
tools:
  - name: Figma
    vendor: Figma Inc.
    enabled: true
    auth:
      type: token
      token: ${FIGMA_TOKEN}
    projects:
      - name: 我的设计项目
        link: "https://www.figma.com/file/xxx"
```

## 环境变量

创建 `.env` 文件：

```bash
FIGMA_TOKEN=figd_your_token
MODAO_TOKEN=your_modao_token
```

## 许可证

MIT License
