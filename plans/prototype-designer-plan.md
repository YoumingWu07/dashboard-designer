# 需求原型设计Skill开发计划

## 技术组件清单

### 1. Plugin结构设计

**可以打包成一个Plugin**，结构如下：

```
dashboard-designer/                    # Plugin根目录
│
├── .claude-plugin/
│   └── plugin.json                    # Plugin元信息
│
├── README.md                          # Plugin说明文档
├── LICENSE                            # 许可证
│
├── skills/                            # 4个Skills
│   ├── prototype-designer/            # 主Skill（流程编排）
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── workflow.md
│   │
│   ├── requirement-analyzer/          # Module 1: 需求理解引擎
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── doc_parser.py
│   │   │   └── excel_generator.py
│   │   ├── templates/
│   │   │   ├── functional-design.md
│   │   │   └── data-model.xlsx
│   │   └── references/
│   │       ├── analysis-patterns.md
│   │       ├── bi-patterns.md
│   │       ├── summary-model-patterns.md
│   │       └── image-parsing-guide.md
│   │
│   ├── prototype-generator/           # Module 2: 原型生成器
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   │   └── wireframe-generator.md
│   │   ├── templates/
│   │   │   ├── ascii-wireframe.md
│   │   │   └── html-dashboard.md
│   │   └── references/
│   │       ├── chart-components.md
│   │       ├── layout-patterns.md
│   │       └── kpi-components.md
│   │
│   └── ui-design-engine/              # Module 3: UI设计引擎
│       ├── SKILL.md
│       ├── agents/
│       │   └── design-converter.md
│       ├── styles/
│       │   ├── presets/
│       │   │   ├── tech-blue.md
│       │   │   ├── minimal-light.md
│       │   │   ├── dark-pro.md
│       │   │   └── corporate.md
│       │   └── custom/
│       │       └── custom-style-template.md
│       ├── mcp/                       # MCP适配器文档
│       │   ├── figma-adapter.md
│       │   └── modao-adapter.md
│       └── references/
│           └── design-tokens.md
│
├── mcp/                               # MCP Server配置（可选）
│   ├── figma-mcp/                     # Figma MCP配置
│   │   └── mcp-config.json
│   └── modao-mcp/                     # 墨刀 MCP配置
│       └── mcp-config.json
│
├── shared/                            # 共享资源
│   ├── scripts/
│   │   ├── utils.py
│   │   └── requirements.txt
│   ├── templates/
│   │   └── design-tools.yaml         # 外部工具配置模板
│   └── references/
│       └── common-patterns.md
│
└── input/                             # 输入目录结构（示例）
    ├── documents/
    ├── images/
    └── external/
        └── design-tools.yaml
```

#### Plugin配置文件

**文件**: `.claude-plugin/plugin.json`

```json
{
  "name": "dashboard-designer",
  "description": "BI驾驶舱设计全流程Plugin。从需求分析到汇总层数据模型设计，再到原型和高保真UI。支持多风格输出、图片输入、外部设计工具对接(Figma/墨刀等)。",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  },
  "repository": "https://github.com/yourname/dashboard-designer",
  "keywords": ["BI", "dashboard", "prototype", "design", "Figma"],
  "license": "MIT"
}
```

#### 包含的Skills清单

| Skill名称 | 功能 | 可独立调用 |
|----------|------|-----------|
| `prototype-designer` | 主入口，编排完整流程 | ✅ `/prototype-designer` |
| `requirement-analyzer` | 需求分析+数据模型设计 | ✅ `/requirement-analyzer` |
| `prototype-generator` | ASCII/HTML原型生成 | ✅ `/prototype-generator` |
| `ui-design-engine` | 多风格UI代码生成 | ✅ `/ui-design-engine` |

#### MCP配置集成

MCP配置可以放在Plugin内，用户安装时自动配置：

```json
// mcp/figma-mcp/mcp-config.json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/figma-mcp"],
      "env": {
        "FIGMA_TOKEN": "${FIGMA_TOKEN}"
      }
    }
  }
}
```

#### 安装后的调用方式

```bash
# 完整流程
/prototype-designer + 上传需求文档

# 单独使用各模块
/requirement-analyzer + 上传需求文档      # 只出功能设计+数据模型
/prototype-generator + 需求描述           # 只出原型
/ui-design-engine + 选择风格              # 只出UI代码
```

### 2. 需要复用的现有Skill

| Skill名称 | 来源 | 用途 | 调用场景 |
|----------|------|------|---------|
| `frontend-design` | 官方插件 | 高保真UI代码生成 | Module 2/3 生成HTML和UI代码 |
| `playground` | 官方插件 | 交互式原型预览 | Module 2 可选生成playground |
| `skill-creator` | 官方插件 | Skill创建和验证 | 开发阶段用于创建新skill |

### 3. MCP Server清单

| MCP名称 | 厂商 | 状态 | 用途 | 认证方式 |
|---------|------|------|------|---------|
| **Figma MCP** | Figma Inc. | 官方/社区已有 | 获取Figma设计稿 | Token / OAuth2 |
| **墨刀 MCP** | Modao.cc | **需自建** | 获取墨刀原型数据 | Token / Password |
| **蓝湖 MCP** | Lanhuapp.com | **需自建** | 获取蓝湖设计稿 | Password |
| **MasterGo MCP** | MasterGo.com | **需自建** | 获取MasterGo设计稿 | Token |
| **PixSo MCP** | Pixso.cn | **需自建** | 获取PixSo设计稿 | Token |

### 4. 内置工具使用

| 工具名称 | 用途 | 使用模块 |
|---------|------|---------|
| `Read` | 文档/图片解析（多模态） | Module 1 |
| `Write` | 输出文件生成 | 所有模块 |
| `AskUserQuestion` | 用户交互（风格选择、确认） | 所有模块 |
| `Bash` | 执行Python脚本 | Module 1 |
| `Glob/Grep` | 文件搜索 | 辅助功能 |

### 5. Python依赖

| 包名 | 版本 | 用途 |
|------|------|------|
| `python-docx` | >=0.8.11 | Word文档解析 |
| `openpyxl` | >=3.1.2 | Excel读写 |
| `PyPDF2` | >=3.0.0 | PDF解析（备用） |
| `pyyaml` | >=6.0 | YAML配置解析 |
| `python-dotenv` | >=1.0.0 | 环境变量管理 |

### 6. 技术依赖关系图

```
┌─────────────────────────────────────────────────────────────────────┐
│                         prototype-designer                           │
│                           (主Skill入口)                              │
└─────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│ requirement-  │          │ prototype-    │          │ ui-design-    │
│ analyzer      │          │ generator     │          │ engine        │
└───────────────┘          └───────────────┘          └───────────────┘
        │                           │                           │
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│ • Read工具    │          │ • frontend-   │          │ • frontend-   │
│ • Python脚本  │          │   design skill│          │   design skill│
│ • openpyxl    │          │ • playground  │          │ • Figma MCP   │
│ • python-docx │          │   skill(可选) │          │ • 墨刀 MCP    │
└───────────────┘          └───────────────┘          └───────────────┘
```

### 7. 开发优先级

| 优先级 | 组件 | 说明 |
|-------|------|------|
| P0 | `requirement-analyzer` | 核心模块，基础能力 |
| P0 | Python文档解析脚本 | 基础设施 |
| P0 | Excel生成脚本 | 数据模型输出 |
| P1 | `prototype-generator` | 核心模块 |
| P1 | `ui-design-engine` | 核心模块 |
| P1 | 风格预设系统 | UI风格配置 |
| P2 | `prototype-designer` | 主入口编排 |
| P2 | Figma MCP集成 | 已有可用方案 |
| P3 | 墨刀 MCP | 需自建 |
| P3 | 其他设计工具MCP | 需自建，按需开发 |

---

## Context

用户希望创建一个**模块化**的skill系统，专注于：
- **BI报表/驾驶舱看板**的需求到设计全流程
- 功能设计文档包含**汇总层数据模型设计**
- UI输出支持**多种风格**选择
- 开发者可**预设风格参数**
- 支持**图片输入**（手绘草图、系统截图、参考图等）

---

## 模块化架构设计

### 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                    prototype-designer                        │
│                   (BI/驾驶舱设计入口)                        │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Module 1    │    │   Module 2    │    │   Module 3    │
│ 需求理解引擎  │───▶│  原型生成器   │───▶│  UI设计引擎   │
│(汇总层数据模型)│   │  (看板原型)   │    │ (多风格支持)  │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
  功能设计文档           ASCII/HTML看板        高保真UI代码
  + 汇总层数据模型设计   原型                  (可选风格)
```

### 输入源支持

```
┌─────────────────────────────────────────────────────────────┐
│                        输入源                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📄 文档输入                    🖼️ 图片输入                  │
│  ├── TXT/MD                    ├── 手绘草图/线框图          │
│  ├── PDF                       ├── 现有系统截图             │
│  ├── Word (.docx)              ├── 参考设计图               │
│  ├── Excel (.xlsx)             ├── 竞品截图                 │
│  └── 直接文本描述              └── 白板/会议记录照片        │
│                                                             │
│  🎨 外部设计工具                                            │
│  ├── Figma 设计稿链接                                       │
│  └── 墨刀原型链接                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Module 1: 需求理解引擎 (requirement-analyzer)

### 功能定位
- 解析BI/驾驶舱需求文档和**图片**
- 提取功能模块、指标维度、用户角色
- **从图片中识别UI结构和设计意图**
- **输出汇总层数据模型设计**

### 输入源处理

#### 文档输入处理
| 格式 | 解析方式 | 说明 |
|------|---------|------|
| TXT/MD | Read工具 | 直接读取文本内容 |
| PDF | Read工具 | 内置PDF解析能力 |
| Word | Python python-docx | 通过脚本解析 |
| Excel | Python openpyxl | 通过脚本解析 |

#### 图片输入处理
| 图片类型 | 提取信息 | 处理方式 |
|---------|---------|---------|
| 手绘草图 | 布局结构、组件位置 | Read工具(多模态) |
| 系统截图 | 组件类型、布局、交互 | Read工具(多模态) |
| 参考设计 | 配色方案、组件样式 | Read工具(多模态) |
| 白板照片 | 文字内容、结构关系 | Read工具(多模态) |

### 图片信息提取流程

```
用户上传图片
      │
      ▼
┌─────────────────────────────────────┐
│ 1. 图片识别 (Read工具多模态能力)    │
│    - 识别图片类型                   │
│    - 识别整体布局结构               │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│ 2. 结构化信息提取                   │
│    - 页面布局：头部/侧边/内容区     │
│    - 组件识别：KPI卡片/图表/表格    │
│    - 文字提取：标题/标签/数值       │
│    - 交互元素：按钮/筛选器/链接     │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│ 3. 设计意图推断                     │
│    - 业务场景推断                   │
│    - 数据指标推断                   │
│    - 交互流程推断                   │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│ 4. 输出功能设计文档                 │
│    + 汇总层数据模型设计             │
└─────────────────────────────────────┘
```

### 图片解析输出示例

**输入**：一张销售看板截图

**提取输出**：
```markdown
## 图片分析结果

### 布局结构
- 顶部：标题栏 + 时间筛选器 + 刷新按钮
- 第一行：4个KPI指标卡
- 第二行：左侧趋势图 + 右侧饼图
- 第三行：数据明细表格

### 组件识别
| 位置 | 组件类型 | 识别内容 |
|------|---------|---------|
| 顶部 | 导航栏 | "销售驾驶舱" 标题 |
| 第一行左1 | KPI卡片 | "销售额 ¥128.5万 ↑12.3%" |
| 第一行左2 | KPI卡片 | "订单数 3,256 ↑5.2%" |
| 第二行左 | 折线图 | 6个月趋势数据 |
| 第二行右 | 饼图 | 区域占比分布 |
| 第三行 | 表格 | 区域销售明细 |

### 推断指标
- 销售额 (SUM)
- 订单数 (COUNT)
- 客户数 (COUNT DISTINCT)
- 转化率 (计算指标)

### 推断维度
- 时间维度 (月度)
- 区域维度 (华东/华南/...)
```

### 文件结构
```
requirement-analyzer/
├── SKILL.md
├── scripts/
│   ├── doc_parser.py           # 文档解析脚本
│   └── excel_generator.py      # Excel生成脚本
├── templates/
│   ├── functional-design.md    # Word文档模板
│   └── data-model.xlsx         # Excel模板（多Sheet）
└── references/
    ├── analysis-patterns.md    # 需求分析模式
    ├── bi-patterns.md          # BI看板设计模式
    ├── summary-model-patterns.md  # 汇总层数据模型模式
    └── image-parsing-guide.md  # 图片解析指南
```

### 输出：功能设计文档（多文件）

#### 输出文件清单

| 文件名 | 格式 | 内容说明 |
|-------|------|---------|
| `功能设计文档.md` | Markdown/Word | 文字描述、业务说明、交互设计 |
| `数据模型设计.xlsx` | Excel | 结构化数据：页面结构、组件清单、数据模型等 |

---

### Word文档结构 (`功能设计文档.md`)

```markdown
# BI驾驶舱功能设计文档

## 1. 项目概述
### 1.1 项目名称
### 1.2 业务背景
### 1.3 业务目标
### 1.4 目标用户

## 2. 设计说明
### 2.1 页面布局说明
### 2.2 核心功能说明
### 2.3 交互设计说明
### 2.4 筛选与下钻逻辑

## 3. 用户角色与权限
### 3.1 角色定义
### 3.2 权限矩阵

## 4. 数据说明
### 4.1 数据来源概述
### 4.2 数据更新频率
### 4.3 关键指标定义

## 5. 附录
### 5.1 术语说明
### 5.2 相关文档链接
```

---

### Excel文件结构 (`数据模型设计.xlsx`)

#### Sheet 1: 页面结构
| 页面ID | 页面名称 | 页面描述 | 布局方式 | 核心功能 | 父页面 |
|--------|---------|---------|---------|---------|--------|
| P001 | 销售概览页 | 展示销售核心指标 | 3行布局 | KPI展示、趋势分析 | - |
| P002 | 区域分析页 | 区域销售分布 | 左右分栏 | 地图展示、区域对比 | P001 |
| P003 | 产品明细页 | 产品销售明细 | 上下布局 | 明细查询、导出 | P001 |

#### Sheet 2: 组件清单
| 组件ID | 所属页面 | 组件名称 | 组件类型 | 位置说明 | 交互说明 |
|--------|---------|---------|---------|---------|---------|
| C001 | P001 | 销售额KPI | 指标卡 | 第一行左1 | 点击跳转区域分析 |
| C002 | P001 | 销售趋势图 | 折线图 | 第二行左侧 | 支持缩放、拖动 |
| C003 | P001 | 区域占比图 | 饼图 | 第二行右侧 | 点击下钻 |

#### Sheet 3: 数据模型-表结构
| 表ID | 表名称 | 表英文名 | 说明 | 主键字段 | 更新频率 |
|------|-------|---------|------|---------|---------|
| T001 | 月度销售汇总表 | monthly_sales_summary | 各事业部月度销售汇总 | month + business_unit | T+1 |
| T002 | 区域销售汇总表 | regional_sales_summary | 各区域销售汇总 | region_code + province | T+1 |
| T003 | 产品销售汇总表 | product_sales_summary | 产品销售汇总 | category_name + product_name | T+1 |

#### Sheet 4: 数据模型-字段定义
| 字段ID | 所属表ID | 字段名称 | 字段英文名 | 字段类型 | 说明 | 示例值 |
|--------|---------|---------|-----------|---------|------|-------|
| F001 | T001 | 月份 | month | VARCHAR(7) | 数据月份 | 2024-01 |
| F002 | T001 | 事业部 | business_unit | VARCHAR(50) | 业务单元 | 华东事业部 |
| F003 | T001 | 销售额 | sales_amount | DECIMAL(12,2) | 销售金额 | 1285000.00 |
| F004 | T001 | 同比增长率 | yoy_growth | DECIMAL(5,2) | 同比增长 | 12.35 |
| F005 | T002 | 区域名称 | region_name | VARCHAR(50) | 销售区域 | 华东 |
| F006 | T002 | 销售额 | sales_amount | DECIMAL(12,2) | 销售金额 | 568000.00 |

#### Sheet 5: 组件与数据模型映射
| 映射ID | 组件ID | 组件名称 | 数据表ID | 数据表名称 | 使用字段 | 筛选条件 | 聚合方式 |
|--------|--------|---------|---------|-----------|---------|---------|---------|
| M001 | C001 | 销售额KPI | T001 | monthly_sales_summary | sales_amount, yoy_growth | 当月 | SUM |
| M002 | C002 | 销售趋势图 | T001 | monthly_sales_summary | month, sales_amount | 近6月 | 按月GROUP BY |
| M003 | C003 | 区域占比图 | T002 | regional_sales_summary | region_name, sales_amount | 当月 | 按区域GROUP BY |

#### Sheet 6: 模型关联关系
| 关联ID | 主表ID | 主表名称 | 从表ID | 从表名称 | 关联字段(主表) | 关联字段(从表) | 关联说明 |
|--------|--------|---------|--------|---------|--------------|--------------|---------|
| R001 | T001 | monthly_sales_summary | T002 | regional_sales_summary | business_unit | region_name | 事业部与区域映射 |
| R002 | T001 | monthly_sales_summary | T003 | product_sales_summary | month | month | 时间维度关联 |

#### Sheet 7: 维度定义
| 维度ID | 维度名称 | 维度英文名 | 数据类型 | 层级结构 | 支持筛选 | 支持下钻 | 说明 |
|--------|---------|-----------|---------|---------|---------|---------|------|
| D001 | 时间 | month | VARCHAR(7) | 年-季-月-日 | 是 | 是 | 主维度 |
| D002 | 事业部 | business_unit | VARCHAR(50) | 单层 | 是 | 否 | 组织维度 |
| D003 | 区域 | region_name | VARCHAR(50) | 区域-省-市 | 是 | 是 | 地理维度 |

---

### 输入输出目录规划

#### 输入目录结构

```
input/
├── documents/                      # 需求文档
│   ├── 需求说明书.docx
│   ├── 业务需求.pdf
│   └── 需求明细.xlsx
│
├── images/                         # 图片资料
│   ├── sketches/                   # 手绘草图
│   │   └── 草图_销售看板.jpg
│   ├── screenshots/                # 系统截图
│   │   └── 现有系统_首页.png
│   └── references/                 # 参考设计
│       └── 参考设计_科技风.png
│
└── external/                       # 外部设计工具配置
    ├── design-tools.yaml           # 设计工具配置文件
    └── README.md                   # 配置说明
```

#### 外部设计工具配置文件格式

**文件**: `input/external/design-tools.yaml`

```yaml
# 外部设计工具配置
# 用于对接Figma、墨刀、蓝湖等设计工具

tools:
  # ==================== Figma 配置 ====================
  - name: Figma
    vendor: Figma Inc.
    type: design                    # design(设计) / prototype(原型)
    enabled: true
    description: 团队主要设计工具
    auth:
      type: token                   # token / oauth2 / password
      # 方式1: 使用 Personal Access Token
      token: ${FIGMA_TOKEN}         # 建议使用环境变量
      # 方式2: OAuth2 (企业版)
      # client_id: ${FIGMA_CLIENT_ID}
      # client_secret: ${FIGMA_CLIENT_SECRET}
    projects:
      - name: 销售驾驶舱设计稿
        project_id: "123456789"
        file_key: "ABC123DEF456"
        link: "https://www.figma.com/file/ABC123DEF456/销售驾驶舱设计稿"
        pages:
          - name: 概览页
            page_id: "0:1"
          - name: 分析页
            page_id: "0:2"
      - name: 另一个设计项目
        project_id: "987654321"
        file_key: "XYZ789ABC123"
        link: "https://www.figma.com/file/XYZ789ABC123/另一个设计项目"

  # ==================== 墨刀 配置 ====================
  - name: 墨刀
    vendor: Modao.cc
    type: prototype
    enabled: true
    description: 原型设计工具
    auth:
      type: token
      token: ${MODAO_TOKEN}
      # 或使用用户名密码
      # username: ${MODAO_USERNAME}
      # password: ${MODAO_PASSWORD}
    api_base: "https://api.modao.cc/v1"
    projects:
      - name: 销售驾驶舱原型
        project_id: "proj_abc123"
        link: "https://modao.cc/app/abc123-sales-dashboard"
        screens:
          - name: 概览页
            screen_id: "screen_001"
          - name: 区域分析页
            screen_id: "screen_002"

  # ==================== 蓝湖 配置 ====================
  - name: 蓝湖
    vendor: Lanhuapp.com
    type: design
    enabled: false                  # 暂未启用
    description: 设计协作平台
    auth:
      type: password
      username: ${LANHU_USERNAME}
      password: ${LANHU_PASSWORD}
    api_base: "https://lanhuapp.com/api/v1"
    projects:
      - name: 设计规范库
        project_id: "lh_123456"
        link: "https://lanhuapp.com/web/#/item/project/lh_123456"

  # ==================== MasterGo 配置 ====================
  - name: MasterGo
    vendor: MasterGo.com
    type: design
    enabled: false
    auth:
      type: token
      token: ${MASTERGO_TOKEN}
    projects:
      - name: 项目名称
        project_id: ""
        link: ""

  # ==================== PixSo 配置 ====================
  - name: PixSo
    vendor: Pixso.cn
    type: design
    enabled: false
    auth:
      type: token
      token: ${PIXSO_TOKEN}
    projects:
      - name: 项目名称
        project_id: ""
        link: ""
```

#### 配置字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 工具名称，用于识别 |
| `vendor` | string | 是 | 厂商名称 |
| `type` | enum | 是 | 工具类型: `design` / `prototype` |
| `enabled` | boolean | 是 | 是否启用 |
| `description` | string | 否 | 工具描述 |
| `auth.type` | enum | 是 | 认证方式: `token` / `oauth2` / `password` |
| `auth.token` | string | 条件 | API Token (建议使用环境变量) |
| `auth.username` | string | 条件 | 用户名 (password方式) |
| `auth.password` | string | 条件 | 密码 (password方式) |
| `auth.client_id` | string | 条件 | OAuth2客户端ID |
| `auth.client_secret` | string | 条件 | OAuth2客户端密钥 |
| `api_base` | string | 否 | API基础地址 |
| `projects` | array | 否 | 项目列表 |
| `projects[].name` | string | 是 | 项目名称 |
| `projects[].project_id` | string | 是 | 项目ID |
| `projects[].link` | string | 是 | 项目链接 |
| `projects[].file_key` | string | 条件 | 文件Key (Figma专用) |
| `projects[].pages` | array | 否 | 页面列表 (Figma) |
| `projects[].screens` | array | 否 | 屏幕列表 (墨刀) |

#### 环境变量配置

**文件**: `.env` (不提交到版本控制)

```bash
# Figma
FIGMA_TOKEN=figd_xxxxxxxxxxxxx

# 墨刀
MODAO_TOKEN=modao_xxxxxxxxxxxxx
# 或
MODAO_USERNAME=your_username
MODAO_PASSWORD=your_password

# 蓝湖
LANHU_USERNAME=your_username
LANHU_PASSWORD=your_password

# MasterGo
MASTERGO_TOKEN=mg_xxxxxxxxxxxxx

# PixSo
PIXSO_TOKEN=pixso_xxxxxxxxxxxxx
```

#### 支持的设计工具

| 工具 | 厂商 | 类型 | 认证方式 | MCP支持 |
|------|------|------|---------|---------|
| Figma | Figma Inc. | 设计 | Token / OAuth2 | 官方/社区 |
| 墨刀 | Modao.cc | 原型 | Token / Password | 需自建 |
| 蓝湖 | Lanhuapp.com | 设计协作 | Password | 需自建 |
| MasterGo | MasterGo.com | 设计 | Token | 需自建 |
| PixSo | Pixso.cn | 设计 | Token | 需自建 |
| 即时设计 | JS.design | 设计 | Token | 需自建 |

#### 输出目录结构

```
output/
├── {项目名称}/                     # 按项目组织
│   │
│   ├── 01_需求分析/                # Module 1 输出
│   │   ├── 功能设计文档.md         # Word文档
│   │   └── 数据模型设计.xlsx       # Excel文件
│   │       ├── Sheet1: 页面结构
│   │       ├── Sheet2: 组件清单
│   │       ├── Sheet3: 数据模型-表结构
│   │       ├── Sheet4: 数据模型-字段定义
│   │       ├── Sheet5: 组件与数据模型映射
│   │       ├── Sheet6: 模型关联关系
│   │       └── Sheet7: 维度定义
│   │
│   ├── 02_原型设计/                # Module 2 输出
│   │   ├── ascii/                  # ASCII原型
│   │   │   ├── 概览页.txt
│   │   │   └── 分析页.txt
│   │   └── html/                   # HTML原型
│   │       ├── 概览页.html
│   │       └── 分析页.html
│   │
│   ├── 03_UI设计/                  # Module 3 输出
│   │   ├── styles/                 # 使用的风格配置
│   │   │   └── tech-blue.md
│   │   └── ui-code/                # 高保真UI代码
│   │       ├── 概览页_tech-blue.html
│   │       └── 分析页_tech-blue.html
│   │
│   └── assets/                     # 资源文件
│       ├── images/                 # 图片资源
│       └── fonts/                  # 字体资源
│
└── .history/                       # 历史版本（可选）
    └── {项目名称}_20240115/
```

#### 目录说明

| 目录 | 说明 | 生成时机 |
|------|------|---------|
| `input/documents/` | 用户上传的需求文档 | 用户输入 |
| `input/images/` | 用户上传的图片资料 | 用户输入 |
| `input/external/` | 外部设计工具链接 | 用户输入 |
| `output/{项目}/01_需求分析/` | 功能设计文档和数据模型 | Module 1 执行后 |
| `output/{项目}/02_原型设计/` | ASCII和HTML原型 | Module 2 执行后 |
| `output/{项目}/03_UI设计/` | 高保真UI代码 | Module 3 执行后 |
| `output/{项目}/assets/` | 相关资源文件 | 按需生成 |

#### 文件命名规范

```
功能设计文档: {项目名称}_功能设计文档.md
数据模型设计: {项目名称}_数据模型设计.xlsx
ASCII原型:    {页面名称}.txt
HTML原型:     {页面名称}.html
UI代码:       {页面名称}_{风格名称}.html
```

---

## Module 2: 原型生成器 (prototype-generator)

### 功能定位
- 基于功能设计生成看板原型
- 针对BI场景优化的组件库
- ASCII快速预览 + HTML原型

### 文件结构
```
prototype-generator/
├── SKILL.md
├── agents/
│   └── wireframe-generator.md
├── templates/
│   ├── ascii-wireframe.md
│   └── html-dashboard.md       # 看板专用HTML模板
└── references/
    ├── chart-components.md     # 图表组件库
    ├── layout-patterns.md      # 看板布局模式
    └── kpi-components.md       # KPI组件库
```

### ASCII看板原型示例
```
┌─────────────────────────────────────────────────────────────┐
│  📊 销售驾驶舱                          [时间筛选▼] [刷新]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 销售额    │  │ 订单数    │  │ 客户数    │  │ 转化率    │   │
│  │ ¥128.5万 │  │ 3,256    │  │ 1,892    │  │ 23.5%    │   │
│  │ ↑12.3%   │  │ ↑5.2%    │  │ ↓2.1%    │  │ ↑1.8%    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌─────────────────────────────┐ ┌───────────────────────┐ │
│  │     📈 销售趋势图            │ │   🥧 销售占比          │ │
│  │     ~~~~~                   │ │       ┌───┐           │ │
│  │    /     \    /\            │ │      /███\  45%      │ │
│  │   /       \__/  \           │ │     /─────\          │ │
│  │  /              \           │ │    /███████\ 55%     │ │
│  │ ─────────────────────       │ │   └───────┘          │ │
│  │ 1月 2月 3月 4月 5月 6月     │ │                      │ │
│  └─────────────────────────────┘ └───────────────────────┘ │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  📋 区域销售明细表                    [导出] [筛选]  │   │
│  │  ┌──────┬──────┬──────┬──────┬──────┐              │   │
│  │  │ 区域 │ 销售额│ 订单数│ 客户数│ 同比 │              │   │
│  │  ├──────┼──────┼──────┼──────┼──────┤              │   │
│  │  │ 华东 │ 45万  │ 1,200│  680  │ +15% │              │   │
│  │  │ 华南 │ 38万  │  980 │  520  │ +8%  │              │   │
│  │  │ ...  │ ...  │ ...  │ ...   │ ...  │              │   │
│  │  └──────┴──────┴──────┴──────┴──────┘              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Module 3: UI设计引擎 (ui-design-engine)

### 功能定位
- 生成高保真UI代码
- **支持多种预设风格**
- **支持开发者自定义风格参数**
- **支持从参考图片提取风格**

### 输入源支持
| 输入源 | 处理方式 | 输出 |
|-------|---------|------|
| 本地原型 | 直接处理 | 高保真UI |
| Figma设计稿 | 通过MCP获取 | 高保真UI |
| 墨刀原型 | 通过MCP获取 | 高保真UI |
| **参考设计图** | **提取配色/样式** | **风格迁移UI** |

### 参考图风格提取

```
用户上传参考设计图
        │
        ▼
┌─────────────────────────────────────┐
│ 1. 图片分析                         │
│    - 提取主色调/配色方案            │
│    - 识别组件样式(圆角/阴影/边框)   │
│    - 识别字体风格                   │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│ 2. 生成临时风格配置                 │
│    - colors: 提取的配色             │
│    - components: 提取的组件样式     │
│    - effects: 识别的特效            │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│ 3. 应用到原型生成UI                 │
└─────────────────────────────────────┘
```

### 文件结构
```
ui-design-engine/
├── SKILL.md
├── agents/
│   └── design-converter.md
├── styles/                          # 风格配置
│   ├── presets/                     # 预设风格
│   │   ├── tech-blue.md             # 科技蓝风格
│   │   ├── minimal-light.md         # 简约素雅风格
│   │   ├── dark-pro.md              # 深色专业风格
│   │   └── corporate.md             # 企业商务风格
│   └── custom/                      # 自定义风格
│       └── custom-style-template.md
├── mcp/
│   ├── figma-adapter.md
│   └── modao-adapter.md
└── references/
    └── design-tokens.md
```

### 风格预设系统

#### 预设风格列表

| 风格名称 | 描述 | 适用场景 |
|---------|------|---------|
| **tech-blue** | 科技蓝风格，深色背景+蓝色高光 | 数据监控大屏、指挥中心 |
| **minimal-light** | 简约素雅，浅色背景+柔和配色 | 企业报表、运营后台 |
| **dark-pro** | 深色专业，深灰背景+多色图表 | 数据分析平台、BI工具 |
| **corporate** | 企业商务，蓝色主色调+白色背景 | 管理驾驶舱、汇报展示 |

#### 风格参数结构

```yaml
# styles/presets/tech-blue.md
name: tech-blue
display_name: 科技蓝风格
description: 深色背景+蓝色高光，适合数据监控大屏

# 颜色配置
colors:
  primary: "#00d4ff"           # 主色调-科技蓝
  secondary: "#0095ff"         # 次要色
  accent: "#ff6b35"            # 强调色-橙色
  success: "#00ff88"           # 成功-绿色
  warning: "#ffcc00"           # 警告-黄色
  danger: "#ff4757"            # 危险-红色

  background:
    base: "#0a1628"            # 基础背景-深蓝黑
    card: "#0d1f3c"            # 卡片背景
    elevated: "#132743"        # 悬浮背景

  text:
    primary: "#ffffff"         # 主文字-白色
    secondary: "#8b9cc2"       # 次要文字
    muted: "#5a6b8a"           # 弱化文字

# 图表配色
charts:
  palette: ["#00d4ff", "#0095ff", "#6366f1", "#8b5cf6", "#ec4899"]
  gradient: true               # 启用渐变
  glow: true                   # 启用发光效果

# 组件样式
components:
  card:
    border_radius: 8
    shadow: "0 4px 24px rgba(0, 212, 255, 0.1)"
    border: "1px solid rgba(0, 212, 255, 0.2)"

  button:
    border_radius: 4
    hover_glow: true

  chart:
    animation: true
    background_transparent: true

# 特效
effects:
  particle: true               # 粒子效果(可选)
  scanline: false              # 扫描线效果
  glow: true                   # 发光效果
  gradient_border: true        # 渐变边框
```

```yaml
# styles/presets/minimal-light.md
name: minimal-light
display_name: 简约素雅风格
description: 浅色背景+柔和配色，适合企业报表和运营后台

colors:
  primary: "#4f46e5"           # 主色调-靛蓝
  secondary: "#6366f1"         # 次要色
  accent: "#f59e0b"            # 强调色-琥珀
  success: "#10b981"           # 成功-翠绿
  warning: "#f59e0b"           # 警告-琥珀
  danger: "#ef4444"            # 危险-红色

  background:
    base: "#f8fafc"            # 基础背景-浅灰白
    card: "#ffffff"            # 卡片背景-白色
    elevated: "#ffffff"        # 悬浮背景

  text:
    primary: "#1e293b"         # 主文字-深灰
    secondary: "#64748b"       # 次要文字
    muted: "#94a3b8"           # 弱化文字

charts:
  palette: ["#4f46e5", "#06b6d4", "#10b981", "#f59e0b", "#ef4444"]
  gradient: false
  glow: false

components:
  card:
    border_radius: 12
    shadow: "0 1px 3px rgba(0, 0, 0, 0.1)"
    border: "1px solid #e2e8f0"

  button:
    border_radius: 8
    hover_glow: false

  chart:
    animation: true
    background_transparent: false

effects:
  particle: false
  scanline: false
  glow: false
  gradient_border: false
```

### 自定义风格配置

开发者可在 `styles/custom/` 目录下创建自定义风格：

```yaml
# styles/custom/my-company-style.md
name: my-company-style
display_name: 公司品牌风格
extends: minimal-light          # 继承现有风格

# 覆盖配置
colors:
  primary: "#1890ff"           # 公司品牌色
  background:
    base: "#f0f2f5"

# 新增自定义组件
components:
  header:
    height: 64
    logo_position: left
```

### 风格选择交互

```
生成UI时，使用AskUserQuestion展示风格选项：

┌─────────────────────────────────────────┐
│ 请选择UI风格：                           │
├─────────────────────────────────────────┤
│ ○ 科技蓝风格 (推荐大屏监控场景)          │
│ ○ 简约素雅风格 (推荐企业报表场景)        │
│ ○ 深色专业风格 (推荐BI分析平台)          │
│ ○ 企业商务风格 (推荐管理驾驶舱)          │
│ ○ 自定义风格 (使用开发者预设)            │
└─────────────────────────────────────────┘
```

---

## 完整文件结构

```
prototype-designer-system/
│
├── prototype-designer/              # 主Skill
│   ├── SKILL.md
│   └── references/
│       └── workflow.md
│
├── requirement-analyzer/            # Module 1
│   ├── SKILL.md
│   ├── scripts/
│   │   └── doc_parser.py
│   ├── templates/
│   │   └── functional-design.md
│   └── references/
│       ├── analysis-patterns.md
│       ├── bi-patterns.md
│       ├── data-model-patterns.md
│       └── image-parsing-guide.md   # 图片解析指南
│
├── prototype-generator/             # Module 2
│   ├── SKILL.md
│   ├── agents/
│   │   └── wireframe-generator.md
│   ├── templates/
│   │   ├── ascii-wireframe.md
│   │   └── html-dashboard.md
│   └── references/
│       ├── chart-components.md
│       ├── layout-patterns.md
│       └── kpi-components.md
│
├── ui-design-engine/                # Module 3
│   ├── SKILL.md
│   ├── agents/
│   │   └── design-converter.md
│   ├── styles/
│   │   ├── presets/
│   │   │   ├── tech-blue.md
│   │   │   ├── minimal-light.md
│   │   │   ├── dark-pro.md
│   │   │   └── corporate.md
│   │   └── custom/
│   │       └── custom-style-template.md
│   ├── mcp/
│   │   ├── figma-adapter.md
│   │   └── modao-adapter.md
│   └── references/
│       └── design-tokens.md
│
└── shared/                          # 共享资源
    ├── scripts/
    │   └── utils.py
    └── references/
        └── common-patterns.md
```

---

## 各模块SKILL.md设计

### requirement-analyzer
```yaml
---
name: requirement-analyzer
description: 分析BI/驾驶舱需求文档或图片，输出功能设计文档和汇总层数据模型设计。支持PDF/Word/Excel/TXT格式，以及图片输入(手绘草图/系统截图/参考设计)。专注于报表和看板场景。
user-invocable: true
---
```

### prototype-generator
```yaml
---
name: prototype-generator
description: 基于功能设计生成BI看板原型。输出ASCII线框图和HTML原型。包含KPI卡片、图表、表格等看板组件。
user-invocable: true
---
```

### ui-design-engine
```yaml
---
name: ui-design-engine
description: 基于原型生成高保真UI代码。支持多种预设风格(科技蓝/简约素雅/深色专业/企业商务)和开发者自定义风格。可对接Figma/墨刀等外部设计工具。
user-invocable: true
---
```

### prototype-designer
```yaml
---
name: prototype-designer
description: BI驾驶舱设计全流程。从需求分析(支持文档/图片输入)到汇总层数据模型设计，再到原型和高保真UI。支持多风格输出和外部设计工具对接。
user-invocable: true
---
```

---

## 详细SKILL.md内容设计

### Skill 1: prototype-designer (主入口)

**文件**: `skills/prototype-designer/SKILL.md`

```markdown
---
name: prototype-designer
description: BI驾驶舱设计全流程。从需求分析到数据模型设计，再到原型和高保真UI。支持文档/图片输入、多风格输出、外部设计工具对接。
version: 1.0.0
user-invocable: true
---

# BI驾驶舱设计全流程

你是BI驾驶舱设计专家，负责将用户需求转化为完整的设计产出。

## 工作流程

### 步骤1: 需求理解
调用 `requirement-analyzer` skill，分析用户输入的需求文档或图片，输出：
- 功能设计文档 (Markdown)
- 数据模型设计 (Excel，7个Sheet)

### 步骤2: 用户确认
使用 AskUserQuestion 确认需求分析结果：
- 选项1: 继续生成原型
- 选项2: 调整需求分析
- 选项3: 只需要功能设计文档，结束流程

### 步骤3: 原型生成
调用 `prototype-generator` skill，基于功能设计生成：
- ASCII线框图 (命令行快速预览)
- HTML原型 (浏览器预览)

### 步骤4: 用户确认原型
使用 AskUserQuestion 确认原型：
- 选项1: 继续生成高保真UI
- 选项2: 调整原型
- 选项3: 只需要原型，结束流程

### 步骤5: UI设计
调用 `ui-design-engine` skill：
1. 展示风格选项供用户选择
2. 基于选定风格生成高保真UI代码

### 步骤6: 输出交付物
整理输出目录结构：
```
output/{项目名称}/
├── 01_需求分析/
│   ├── 功能设计文档.md
│   └── 数据模型设计.xlsx
├── 02_原型设计/
│   ├── ascii/
│   └── html/
└── 03_UI设计/
    └── ui-code/
```

## 输入类型处理

### 文档输入
- TXT/MD/PDF: 直接使用Read工具读取
- Word (.docx): 调用 doc_parser.py 解析
- Excel (.xlsx): 调用 doc_parser.py 解析

### 图片输入
- 手绘草图/线框图: 识别布局结构
- 系统截图: 识别组件和交互
- 参考设计图: 提取配色和样式

### 外部设计工具
读取 `input/external/design-tools.yaml` 获取配置的Figma/墨刀等工具链接

## 注意事项

1. 每个步骤都需要用户确认后再继续
2. 用户可随时终止流程，获取当前阶段的产出物
3. 输出文件统一存放在 output/{项目名称}/ 目录下
```

---

### Skill 2: requirement-analyzer (需求理解引擎)

**文件**: `skills/requirement-analyzer/SKILL.md`

```markdown
---
name: requirement-analyzer
description: 分析BI/驾驶舱需求文档或图片，输出功能设计文档和汇总层数据模型设计。支持PDF/Word/Excel/TXT格式及图片输入。
version: 1.0.0
user-invocable: true
---

# 需求理解引擎

你是BI驾驶舱需求分析专家，负责解析需求并输出结构化设计文档。

## 输入处理

### 文档解析
| 格式 | 处理方式 |
|------|---------|
| TXT/MD/PDF | 使用Read工具直接读取 |
| Word (.docx) | 执行 `python scripts/doc_parser.py {file_path}` |
| Excel (.xlsx) | 执行 `python scripts/doc_parser.py {file_path}` |

### 图片解析
使用Read工具的多模态能力，识别：
1. 布局结构 (头部/侧边/内容区)
2. 组件类型 (KPI卡片/图表/表格/筛选器)
3. 文字内容 (标题/标签/数值)
4. 交互元素 (按钮/链接/下拉框)

## 分析流程

### 1. 提取项目信息
- 项目名称
- 业务背景
- 业务目标
- 目标用户

### 2. 识别页面模块
- 页面清单
- 页面层级关系
- 页面核心功能

### 3. 识别组件
- 组件名称和类型
- 数据字段需求
- 交互说明

### 4. 设计数据模型
基于组件需求设计汇总层数据模型：
- 数据表设计
- 字段定义
- 表关联关系
- 维度定义

### 5. 组件与数据映射
确定每个组件使用哪个数据表的哪些字段

## 输出文件

### 功能设计文档 (Markdown)
输出到: `output/{项目名称}/01_需求分析/功能设计文档.md`

内容结构：
```markdown
# {项目名称} 功能设计文档

## 1. 项目概述
### 1.1 项目名称
### 1.2 业务背景
### 1.3 业务目标
### 1.4 目标用户

## 2. 设计说明
### 2.1 页面布局说明
### 2.2 核心功能说明
### 2.3 交互设计说明
### 2.4 筛选与下钻逻辑

## 3. 用户角色与权限
### 3.1 角色定义
### 3.2 权限矩阵

## 4. 数据说明
### 4.1 数据来源概述
### 4.2 数据更新频率
### 4.3 关键指标定义

## 5. 附录
### 5.1 术语说明
### 5.2 相关文档链接
```

### 数据模型设计 (Excel)
输出到: `output/{项目名称}/01_需求分析/数据模型设计.xlsx`

执行命令生成：
```bash
python scripts/excel_generator.py --project "{项目名称}" --output "output/{项目名称}/01_需求分析/"
```

Excel包含7个Sheet：
1. 页面结构
2. 组件清单
3. 数据模型-表结构
4. 数据模型-字段定义
5. 组件与数据模型映射
6. 模型关联关系
7. 维度定义

## 参考文档

加载以下参考文档辅助分析：
- `references/analysis-patterns.md` - 需求分析模式
- `references/bi-patterns.md` - BI看板设计模式
- `references/summary-model-patterns.md` - 汇总层数据模型模式
- `references/image-parsing-guide.md` - 图片解析指南
```

---

### Skill 3: prototype-generator (原型生成器)

**文件**: `skills/prototype-generator/SKILL.md`

```markdown
---
name: prototype-generator
description: 基于功能设计生成BI看板原型。输出ASCII线框图和HTML原型。包含KPI卡片、图表、表格等看板组件。
version: 1.0.0
user-invocable: true
---

# 原型生成器

你是BI看板原型设计专家，负责将功能设计转化为可视化原型。

## 输入来源

1. 功能设计文档路径: `output/{项目名称}/01_需求分析/功能设计文档.md`
2. 数据模型设计路径: `output/{项目名称}/01_需求分析/数据模型设计.xlsx`
3. 或用户直接描述的需求

## 生成流程

### 步骤1: 解析功能设计
读取功能设计文档，提取：
- 页面结构
- 组件清单
- 交互说明

### 步骤2: 生成ASCII原型
参考 `templates/ascii-wireframe.md` 模板，生成ASCII线框图。

输出到: `output/{项目名称}/02_原型设计/ascii/{页面名称}.txt`

### 步骤3: 用户确认
展示ASCII原型，使用 AskUserQuestion 确认：
- 确认 → 继续生成HTML
- 调整 → 修改ASCII原型

### 步骤4: 生成HTML原型
参考 `templates/html-dashboard.md` 模板，生成HTML原型。

输出到: `output/{项目名称}/02_原型设计/html/{页面名称}.html`

### 步骤5: 打开预览
执行 `open output/{项目名称}/02_原型设计/html/{页面名称}.html` 在浏览器预览

## 组件库参考

加载 `references/` 目录下的组件库文档：
- `chart-components.md` - 图表组件
- `layout-patterns.md` - 布局模式
- `kpi-components.md` - KPI组件

## ASCII原型示例

```
┌─────────────────────────────────────────────────────────────┐
│  📊 销售驾驶舱                          [时间筛选▼] [刷新]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 销售额    │  │ 订单数    │  │ 客户数    │  │ 转化率    │   │
│  │ ¥128.5万 │  │ 3,256    │  │ 1,892    │  │ 23.5%    │   │
│  │ ↑12.3%   │  │ ↑5.2%    │  │ ↓2.1%    │  │ ↑1.8%    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│  ┌─────────────────────────────┐ ┌───────────────────────┐ │
│  │     📈 销售趋势图            │ │   🥧 销售占比          │ │
│  └─────────────────────────────┘ └───────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## HTML原型要求

1. 单文件HTML，内联CSS和JS
2. 使用CSS Grid或Flexbox布局
3. 响应式设计
4. 包含示例数据展示
```

---

### Skill 4: ui-design-engine (UI设计引擎)

**文件**: `skills/ui-design-engine/SKILL.md`

```markdown
---
name: ui-design-engine
description: 基于原型生成高保真UI代码。支持多种预设风格和开发者自定义风格。可对接Figma/墨刀等外部设计工具。
version: 1.0.0
user-invocable: true
---

# UI设计引擎

你是高保真UI设计专家，负责将原型转化为精美的UI代码。

## 输入来源

1. 本地原型: `output/{项目名称}/02_原型设计/`
2. 外部设计工具: `input/external/design-tools.yaml` 配置的Figma/墨刀等
3. 用户直接提供的原型描述

## 风格选择

### 预设风格

| 风格 | 适用场景 | 配置文件 |
|------|---------|---------|
| 科技蓝 | 大屏监控、指挥中心 | `styles/presets/tech-blue.md` |
| 简约素雅 | 企业报表、运营后台 | `styles/presets/minimal-light.md` |
| 深色专业 | BI分析平台 | `styles/presets/dark-pro.md` |
| 企业商务 | 管理驾驶舱 | `styles/presets/corporate.md` |

### 风格选择流程

使用 AskUserQuestion 展示风格选项：

```
请选择UI风格：
○ 科技蓝风格 (推荐大屏监控场景)
○ 简约素雅风格 (推荐企业报表场景)
○ 深色专业风格 (推荐BI分析平台)
○ 企业商务风格 (推荐管理驾驶舱)
○ 自定义风格 (使用开发者预设)
```

### 自定义风格

开发者可在 `styles/custom/` 目录创建自定义风格配置。

## 生成流程

### 步骤1: 加载风格配置
读取选定风格的配置文件，获取：
- 颜色配置 (primary, secondary, background, text)
- 图表配色 (palette, gradient, glow)
- 组件样式 (card, button, chart)
- 特效配置 (particle, glow, gradient_border)

### 步骤2: 解析原型结构
读取HTML原型，提取：
- 页面布局
- 组件结构
- 数据字段

### 步骤3: 调用frontend-design skill
使用风格配置和原型结构，调用 frontend-design skill 生成高保真UI。

### 步骤4: 输出UI代码
输出到: `output/{项目名称}/03_UI设计/ui-code/{页面名称}_{风格名称}.html`

### 步骤5: 打开预览
执行 `open output/{项目名称}/03_UI设计/ui-code/{页面名称}_{风格名称}.html`

## 外部设计工具对接

### Figma
1. 读取 `input/external/design-tools.yaml` 获取Figma配置
2. 通过Figma MCP获取设计稿
3. 解析设计稿结构
4. 生成对应UI代码

### 墨刀
1. 读取配置获取墨刀项目链接
2. 通过墨刀API获取原型数据
3. 解析原型结构
4. 生成对应UI代码

## 参考文档

- `references/design-tokens.md` - 设计Token规范
- `mcp/figma-adapter.md` - Figma适配器说明
- `mcp/modao-adapter.md` - 墨刀适配器说明
```

---

## MCP配置详细设计

### Figma MCP配置

**文件**: `mcp/figma-mcp/mcp-config.json`

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/figma-mcp-server"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "${FIGMA_TOKEN}"
      }
    }
  }
}
```

**文件**: `skills/ui-design-engine/mcp/figma-adapter.md`

```markdown
# Figma适配器

## 功能说明
从Figma设计稿获取组件结构和样式信息。

## 使用方式

### 1. 配置Figma Token
在 `.env` 文件中配置：
```
FIGMA_TOKEN=figd_your_token_here
```

### 2. 获取设计稿
通过Figma MCP获取设计稿数据：
- File信息
- Node结构
- 组件定义
- 样式信息

### 3. 数据转换
将Figma数据转换为UI代码结构：
| Figma元素 | 转换规则 |
|----------|---------|
| Frame | → 容器组件 (div) |
| Component | → 可复用组件 |
| Text | → 文本元素 (span/p) |
| Rectangle | → 块元素 (div) |
| Vector | → SVG图标 |

### 4. 样式提取
- 颜色 → CSS color/background
- 字体 → CSS font-family/font-size
- 圆角 → CSS border-radius
- 阴影 → CSS box-shadow

## 常用操作

### 获取File信息
```
获取Figma文件 {file_key} 的结构
```

### 获取节点详情
```
获取Figma节点 {node_id} 的详细信息
```

### 导出图片
```
导出Figma节点 {node_id} 为图片
```
```

---

### 墨刀MCP配置

**文件**: `mcp/modao-mcp/mcp-config.json`

```json
{
  "mcpServers": {
    "modao": {
      "command": "python",
      "args": ["-m", "modao_mcp_server"],
      "env": {
        "MODAO_API_TOKEN": "${MODAO_TOKEN}",
        "MODAO_API_BASE": "https://api.modao.cc/v1"
      }
    }
  }
}
```

> 注：墨刀MCP Server需要自建，参考 `skills/ui-design-engine/mcp/modao-adapter.md`

**文件**: `skills/ui-design-engine/mcp/modao-adapter.md`

```markdown
# 墨刀适配器

## 概述
墨刀暂无官方MCP Server，需要自建。

## 自建MCP Server步骤

### 1. 创建项目
```bash
mkdir modao-mcp-server
cd modao-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk axios
```

### 2. 实现MCP Server
```javascript
// index.js
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const axios = require('axios');

const server = new Server({
  name: 'modao-mcp-server',
  version: '1.0.0'
}, {
  capabilities: { tools: {} }
});

// 定义工具
server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'get_project',
      description: '获取墨刀项目信息',
      inputSchema: {
        type: 'object',
        properties: {
          project_id: { type: 'string', description: '项目ID' }
        },
        required: ['project_id']
      }
    },
    {
      name: 'get_screens',
      description: '获取项目所有屏幕',
      inputSchema: {
        type: 'object',
        properties: {
          project_id: { type: 'string', description: '项目ID' }
        },
        required: ['project_id']
      }
    }
  ]
}));

// 处理工具调用
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  const response = await callModaoAPI(name, args);
  return { content: [{ type: 'text', text: JSON.stringify(response) }] };
});
```

### 3. 墨刀API接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/projects/{project_id}` | GET | 获取项目信息 |
| `/projects/{project_id}/screens` | GET | 获取屏幕列表 |
| `/screens/{screen_id}` | GET | 获取屏幕详情 |

### 4. 启动服务
```bash
node index.js
```
```

---

## 安装和使用说明

### 安装方式

#### 方式1: 本地安装
```bash
# 复制到Claude插件目录
cp -r dashboard-designer ~/.claude/plugins/

# 重新加载插件
/reload-plugins
```

#### 方式2: 从Git安装
```bash
# 克隆仓库
git clone https://github.com/yourname/dashboard-designer.git

# 链接到插件目录
ln -s $(pwd)/dashboard-designer ~/.claude/plugins/dashboard-designer

# 重新加载插件
/reload-plugins
```

### 配置环境变量

创建 `.env` 文件：
```bash
# Figma配置
FIGMA_TOKEN=figd_your_token

# 墨刀配置
MODAO_TOKEN=your_modao_token

# 其他设计工具...
```

### 使用方式

#### 完整流程
```
/prototype-designer
```
上传需求文档或图片，按提示完成全流程。

#### 单独使用各模块
```
# 只需要功能设计文档
/requirement-analyzer + 上传需求文档

# 基于已有功能设计生成原型
/prototype-generator

# 基于已有原型生成UI
/ui-design-engine
```

#### 指定输入源
```
# 使用Figma设计稿
/ui-design-engine --source figma --project "销售驾驶舱设计稿"

# 使用墨刀原型
/ui-design-engine --source modao --project "销售驾驶舱原型"
```

## 实现步骤

### Phase 1: Plugin基础结构

#### 1.1 创建Plugin骨架
- [ ] 创建 `dashboard-designer/` 根目录
- [ ] 创建 `.claude-plugin/plugin.json`
- [ ] 创建 `README.md`
- [ ] 创建 `LICENSE`

#### 1.2 创建目录结构
```
- [ ] skills/
- [ ] mcp/
- [ ] shared/scripts/
- [ ] shared/templates/
- [ ] shared/references/
- [ ] input/documents/
- [ ] input/images/
- [ ] input/external/
```

#### 1.3 创建基础配置文件
- [ ] `shared/scripts/requirements.txt`
- [ ] `shared/templates/design-tools.yaml`
- [ ] `input/external/design-tools.yaml` (示例)

---

### Phase 2: requirement-analyzer Skill

#### 2.1 SKILL.md主文件
- [ ] 创建 `skills/requirement-analyzer/SKILL.md`
- [ ] 定义frontmatter (name, description, user-invocable)
- [ ] 编写输入处理逻辑
- [ ] 编写分析流程
- [ ] 编写输出规范

#### 2.2 Python脚本
- [ ] `scripts/doc_parser.py` - 文档解析脚本
  ```python
  # 功能：
  # - parse_word(file_path) -> str
  # - parse_excel(file_path) -> dict
  # - parse_pdf(file_path) -> str
  ```
- [ ] `scripts/excel_generator.py` - Excel生成脚本
  ```python
  # 功能：
  # - generate_data_model_excel(project_name, data) -> xlsx
  # - 包含7个Sheet生成逻辑
  ```

#### 2.3 模板文件
- [ ] `templates/functional-design.md` - 功能设计文档模板
- [ ] `templates/data-model.xlsx` - Excel模板

#### 2.4 参考文档
- [ ] `references/analysis-patterns.md` - 需求分析模式
- [ ] `references/bi-patterns.md` - BI看板设计模式
- [ ] `references/summary-model-patterns.md` - 汇总层数据模型模式
- [ ] `references/image-parsing-guide.md` - 图片解析指南

---

### Phase 3: prototype-generator Skill

#### 3.1 SKILL.md主文件
- [ ] 创建 `skills/prototype-generator/SKILL.md`
- [ ] 编写ASCII生成逻辑
- [ ] 编写HTML生成逻辑
- [ ] 编写用户确认交互

#### 3.2 Agent定义
- [ ] `agents/wireframe-generator.md` - 线框图生成代理

#### 3.3 模板文件
- [ ] `templates/ascii-wireframe.md` - ASCII线框图模板
- [ ] `templates/html-dashboard.md` - HTML看板模板

#### 3.4 参考文档
- [ ] `references/chart-components.md` - 图表组件库
- [ ] `references/layout-patterns.md` - 布局模式
- [ ] `references/kpi-components.md` - KPI组件库

---

### Phase 4: ui-design-engine Skill

#### 4.1 SKILL.md主文件
- [ ] 创建 `skills/ui-design-engine/SKILL.md`
- [ ] 编写风格选择逻辑
- [ ] 编写frontend-design调用逻辑
- [ ] 编写外部工具对接逻辑

#### 4.2 Agent定义
- [ ] `agents/design-converter.md` - 设计转换代理

#### 4.3 风格预设
- [ ] `styles/presets/tech-blue.md` - 科技蓝风格
- [ ] `styles/presets/minimal-light.md` - 简约素雅风格
- [ ] `styles/presets/dark-pro.md` - 深色专业风格
- [ ] `styles/presets/corporate.md` - 企业商务风格
- [ ] `styles/custom/custom-style-template.md` - 自定义风格模板

#### 4.4 MCP适配器文档
- [ ] `mcp/figma-adapter.md` - Figma适配器说明
- [ ] `mcp/modao-adapter.md` - 墨刀适配器说明

#### 4.5 参考文档
- [ ] `references/design-tokens.md` - 设计Token规范

---

### Phase 5: prototype-designer主Skill

#### 5.1 SKILL.md主文件
- [ ] 创建 `skills/prototype-designer/SKILL.md`
- [ ] 编写工作流编排逻辑
- [ ] 编写模块调用顺序
- [ ] 编写用户交互点

#### 5.2 参考文档
- [ ] `references/workflow.md` - 工作流配置

---

### Phase 6: MCP Server配置

#### 6.1 Figma MCP
- [ ] `mcp/figma-mcp/mcp-config.json`
- [ ] 测试Figma MCP连接

#### 6.2 墨刀 MCP (可选，需自建)
- [ ] 创建墨刀MCP Server项目
- [ ] `mcp/modao-mcp/mcp-config.json`
- [ ] 测试墨刀API连接

---

### Phase 7: 测试验证

#### 7.1 单元测试
- [ ] 测试文档解析脚本
- [ ] 测试Excel生成脚本
- [ ] 测试各Skill独立调用

#### 7.2 集成测试
- [ ] 测试完整流程 (Phase 1-5)
- [ ] 测试图片输入场景
- [ ] 测试外部设计工具对接

#### 7.3 风格测试
- [ ] 测试科技蓝风格输出
- [ ] 测试简约素雅风格输出
- [ ] 测试自定义风格

---

### 开发时间估算

| Phase | 预估工作量 | 优先级 |
|-------|-----------|--------|
| Phase 1 | 0.5天 | P0 |
| Phase 2 | 2天 | P0 |
| Phase 3 | 1.5天 | P1 |
| Phase 4 | 2天 | P1 |
| Phase 5 | 1天 | P2 |
| Phase 6 | 1天 | P2 |
| Phase 7 | 1天 | P3 |
| **总计** | **9天** | - |

---

## 验证场景

### 场景1: 完整流程（文档输入）
```
/prototype-designer + 上传销售报表需求文档
→ 功能设计文档(含汇总层数据模型)
→ ASCII看板原型
→ 选择"科技蓝风格"
→ 高保真UI代码
```

### 场景2: 图片输入流程
```
/prototype-designer + 上传现有系统截图
→ 图片分析：识别布局、组件、指标
→ 功能设计文档(含汇总层数据模型)
→ ASCII看板原型
→ 选择风格
→ 高保真UI代码
```

### 场景3: 只要功能设计
```
/requirement-analyzer + 上传需求Word
→ 功能设计文档 + 汇总层数据模型设计 → 结束
```

### 场景4: 图片转功能设计
```
/requirement-analyzer + 上传手绘草图/白板照片
→ 图片解析：识别结构、提取文字
→ 功能设计文档 + 汇总层数据模型设计 → 结束
```

### 场景5: 风格选择
```
/ui-design-engine + 指定原型
→ 选择风格：
  - 科技蓝(适合大屏)
  - 简约素雅(适合报表)
  - 自定义风格
→ 生成对应风格UI
```

### 场景6: 自定义风格
```
开发者预设 styles/custom/my-style.md
/ui-design-engine → 选择"自定义风格" → 应用my-style配置
```

### 场景7: 参考图风格迁移
```
/ui-design-engine + 上传参考设计图
→ 提取配色方案、组件样式
→ 应用到当前原型
→ 生成符合参考风格的UI
```
