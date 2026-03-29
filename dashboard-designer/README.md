# Dashboard Designer Plugin

BI驾驶舱设计全流程Plugin，支持从需求分析到高保真UI的完整设计流程。

## 目录

- [功能特性](#功能特性)
- [安装指南](#安装指南)
- [快速开始](#快速开始)
- [详细使用教程](#详细使用教程)
- [配置说明](#配置说明)
- [输出文件说明](#输出文件说明)
- [常见问题](#常见问题)
- [开发指南](#开发指南)

---

## 功能特性

### 核心功能

| 功能 | 说明 |
|------|------|
| 📄 **多格式输入** | 支持PDF/Word/Excel/TXT文档，以及图片输入 |
| 📊 **数据模型设计** | 自动生成汇总层数据模型（7个Sheet的Excel） |
| 🎨 **多风格UI** | 科技蓝、简约素雅、深色专业、企业商务 |
| 🔌 **外部工具对接** | 支持Figma、墨刀等设计工具 |
| 🔄 **模块化设计** | 各模块可独立使用，也可组合使用 |

### 工作流程

```
需求文档/图片
      │
      ▼
┌─────────────────┐
│  需求理解引擎    │ → 功能设计文档 + 数据模型Excel
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  原型生成器      │ → ASCII线框图 + HTML原型
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  UI设计引擎      │ → 高保真UI代码
└─────────────────┘
```

---

## 安装指南

### 前置要求

- Claude Code CLI
- Python 3.8+ (用于文档解析脚本)

### 安装步骤

#### 方式1: 从GitHub安装

```bash
# 克隆仓库
git clone https://github.com/YoumingWu07/dashboard-designer.git

# 复制到Claude插件目录
cp -r dashboard-designer ~/.claude/plugins/

# 安装Python依赖
cd dashboard-designer
pip install -r shared/scripts/requirements.txt
```

#### 方式2: 直接下载

```bash
# 下载压缩包
wget https://github.com/YoumingWu07/dashboard-designer/archive/refs/heads/master.zip
unzip master.zip

# 复制到Claude插件目录
cp -r dashboard-designer-master ~/.claude/plugins/dashboard-designer

# 安装依赖
cd ~/.claude/plugins/dashboard-designer
pip install -r shared/scripts/requirements.txt
```

### 验证安装

```bash
# 在Claude Code中执行
/reload-plugins

# 检查是否可用
/prototype-designer --help
```

---

## 快速开始

### 完整流程（推荐）

```
/prototype-designer
```

然后按提示操作：
1. 上传需求文档或图片
2. 确认需求分析结果
3. 确认原型设计
4. 选择UI风格
5. 获取最终交付物

### 单独使用各模块

```bash
# 只要功能设计文档
/requirement-analyzer

# 只要原型
/prototype-generator

# 只要UI代码
/ui-design-engine
```

---

## 详细使用教程

### 场景1: 从需求文档开始

**输入**: 上传需求文档 (支持 PDF/Word/Excel/TXT)

```
用户: /prototype-designer
      [上传 销售驾驶舱需求说明书.docx]

Claude: 正在分析需求文档...

        === 需求分析结果 ===
        项目名称: 销售驾驶舱
        目标用户: 销售经理、运营人员
        页面数量: 3个

        请选择下一步：
        ○ 继续生成原型
        ○ 调整需求分析
        ○ 只要功能设计文档
```

### 场景2: 从现有系统截图开始

**输入**: 上传系统截图

```
用户: /prototype-designer
      [上传 现有系统首页截图.png]

Claude: 正在解析图片...

        === 图片分析结果 ===
        识别到布局: 3行布局
        组件数量: 4个KPI卡片 + 2个图表 + 1个表格

        推断指标: 销售额、订单数、客户数、转化率
```

### 场景3: 从手绘草图开始

**输入**: 上传手绘草图

```
用户: /prototype-designer
      [上传 手绘草图.jpg]

Claude: 识别到草图内容...
        正在转换为结构化设计...
```

### 场景4: 从Figma设计稿生成UI

**前提**: 已配置Figma Token

```
用户: /ui-design-engine --figma "file_key"

Claude: 正在获取Figma设计稿...
        已识别 12 个组件

        请选择UI风格：
        ○ 科技蓝风格
        ○ 简约素雅风格
        ...
```

---

## 配置说明

### 1. 外部设计工具配置

编辑 `input/external/design-tools.yaml`:

```yaml
tools:
  # Figma配置
  - name: Figma
    vendor: Figma Inc.
    type: design
    enabled: true
    auth:
      type: token
      token: ${FIGMA_TOKEN}    # 从环境变量读取
    projects:
      - name: 销售驾驶舱设计稿
        file_key: "ABC123DEF456"
        link: "https://www.figma.com/file/ABC123DEF456/销售驾驶舱设计稿"

  # 墨刀配置
  - name: 墨刀
    vendor: Modao.cc
    type: prototype
    enabled: true
    auth:
      type: token
      token: ${MODAO_TOKEN}
    projects:
      - name: 销售驾驶舱原型
        project_id: "proj_abc123"
        link: "https://modao.cc/app/abc123"
```

### 2. 环境变量配置

创建 `.env` 文件：

```bash
# Figma
FIGMA_TOKEN=figd_your_figma_token

# 墨刀
MODAO_TOKEN=your_modao_token

# 蓝湖
LANHU_USERNAME=your_username
LANHU_PASSWORD=your_password
```

### 3. 自定义UI风格

在 `skills/ui-design-engine/styles/custom/` 创建自定义风格：

```yaml
# my-company-style.md
name: my-company-style
display_name: 公司品牌风格
extends: minimal-light          # 继承现有风格

# 覆盖配置
colors:
  primary: "#1890ff"           # 公司品牌色
  background:
    base: "#f0f2f5"
```

---

## 输出文件说明

### 目录结构

```
output/{项目名称}/
│
├── 01_需求分析/
│   ├── 功能设计文档.md         # Markdown格式
│   └── 数据模型设计.xlsx       # Excel格式 (7个Sheet)
│
├── 02_原型设计/
│   ├── ascii/
│   │   ├── 概览页.txt         # ASCII线框图
│   │   └── 分析页.txt
│   └── html/
│       ├── 概览页.html        # HTML原型
│       └── 分析页.html
│
└── 03_UI设计/
    ├── styles/
    │   └── tech-blue.md       # 使用的风格配置
    └── ui-code/
        ├── 概览页_tech-blue.html
        └── 分析页_tech-blue.html
```

### 功能设计文档内容

| 章节 | 内容 |
|------|------|
| 项目概述 | 名称、背景、目标、用户 |
| 设计说明 | 布局、功能、交互、筛选下钻 |
| 用户角色 | 角色定义、权限矩阵 |
| 数据说明 | 来源、更新频率、关键指标 |

### 数据模型Excel (7个Sheet)

| Sheet | 内容 |
|-------|------|
| 页面结构 | 页面ID、名称、描述、布局 |
| 组件清单 | 组件ID、类型、位置、交互 |
| 数据模型-表结构 | 表定义、主键、更新频率 |
| 数据模型-字段定义 | 字段ID、类型、示例值 |
| 组件与数据映射 | 组件使用哪些表的哪些字段 |
| 模型关联关系 | 表之间的关联 |
| 维度定义 | 筛选维度、下钻维度 |

---

## 常见问题

### Q: 支持哪些输入格式？

| 类型 | 格式 |
|------|------|
| 文档 | PDF, Word (.docx), Excel (.xlsx), TXT, MD |
| 图片 | JPG, PNG, GIF, BMP, WebP |
| 外部工具 | Figma, 墨刀, 蓝湖 |

### Q: 如何获取Figma Token？

1. 登录 Figma
2. 进入 Settings → Personal Access Tokens
3. 点击 "Create new token"
4. 复制生成的Token

### Q: 输出的数据模型是什么层级？

输出的是**汇总层数据模型**，直接服务于看板展示，数据已聚合计算完成，无需再次计算。

### Q: 如何添加自定义UI风格？

参考 `skills/ui-design-engine/styles/custom/custom-style-template.md` 模板创建。

### Q: 能否只使用部分功能？

可以。各Skill可独立调用：
- `/requirement-analyzer` - 只要功能设计
- `/prototype-generator` - 只要原型
- `/ui-design-engine` - 只要UI代码

---

## 开发指南

### 项目结构

```
dashboard-designer/
├── .claude-plugin/
│   └── plugin.json              # Plugin配置
├── skills/
│   ├── prototype-designer/      # 主Skill
│   ├── requirement-analyzer/    # 需求理解引擎
│   ├── prototype-generator/     # 原型生成器
│   └── ui-design-engine/        # UI设计引擎
├── shared/
│   ├── scripts/                 # 共享Python脚本
│   └── templates/               # 共享模板
└── input/
    └── external/                # 外部工具配置
```

### 添加新的UI风格预设

1. 在 `skills/ui-design-engine/styles/presets/` 创建新文件
2. 参考现有预设格式定义颜色、组件样式等
3. 在 SKILL.md 中添加到风格选择列表

### 添加新的外部工具支持

1. 在 `input/external/design-tools.yaml` 添加配置模板
2. 在 `skills/ui-design-engine/mcp/` 创建适配器文档
3. 如需MCP Server，参考墨刀适配器示例

---

## 许可证

MIT License

---

## 贡献

欢迎提交 Issue 和 Pull Request！

仓库地址: https://github.com/YoumingWu07/dashboard-designer
