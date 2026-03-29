# Figma适配器

本文档说明如何通过Figma MCP获取设计稿数据。

## 配置Figma MCP

### 1. 获取Figma Token

1. 登录 Figma
2. 进入 Settings → Personal Access Tokens
3. 点击 "Create new token"
4. 复制生成的Token

### 2. 配置环境变量

在 `.env` 文件中添加：

```bash
FIGMA_TOKEN=figd_your_token_here
```

### 3. 配置design-tools.yaml

```yaml
tools:
  - name: Figma
    vendor: Figma Inc.
    type: design
    enabled: true
    auth:
      type: token
      token: ${FIGMA_TOKEN}
    projects:
      - name: 销售驾驶舱设计稿
        file_key: "ABC123DEF456"
        link: "https://www.figma.com/file/ABC123DEF456/销售驾驶舱设计稿"
```

## 使用Figma MCP

### 获取文件信息

```
获取Figma文件 {file_key} 的结构
```

返回文件的基本信息，包括：
- 文件名称
- 页面列表
- 组件库

### 获取页面节点

```
获取Figma文件 {file_key} 中页面 {page_id} 的节点树
```

返回页面的节点结构：
- Frame节点
- Component节点
- 文本节点
- 图片节点

### 获取节点详情

```
获取Figma节点 {node_id} 的详细信息
```

返回节点的完整信息：
- 样式属性
- 文字内容
- 布局信息
- 效果（阴影、模糊等）

### 导出图片

```
导出Figma节点 {node_id} 为PNG图片
```

## Figma数据转换

### 节点类型映射

| Figma节点 | 转换结果 |
|----------|---------|
| FRAME | `<div>` 容器 |
| COMPONENT | 可复用组件 |
| INSTANCE | 组件实例 |
| TEXT | `<span>` / `<p>` |
| RECTANGLE | `<div>` 块元素 |
| ELLIPSE | `<div>` + border-radius: 50% |
| VECTOR | SVG |
| LINE | `<hr>` 或 border |
| POLYGON | SVG |
| STAR | SVG |
| IMAGE | `<img>` |

### 样式属性映射

| Figma属性 | CSS属性 |
|----------|---------|
| fills | background-color, background-image |
| strokes | border-color, border-width |
| effects | box-shadow, filter: blur() |
| opacity | opacity |
| rectangleCornerRadii | border-radius |
| size | width, height |
| layoutAlign | align-self |
| layoutGrow | flex-grow |
| primaryAxisAlignItems | justify-content |
| counterAxisAlignItems | align-items |
| itemSpacing | gap |
| paddingLeft/Right/Top/Bottom | padding |
| fontName | font-family |
| fontSize | font-size |
| fontWeight | font-weight |
| lineHeight | line-height |
| letterSpacing | letter-spacing |
| textAlignHorizontal | text-align |
| textColor | color |

### Auto Layout转换

Figma的Auto Layout直接转换为Flexbox：

```
Auto Layout:
- Direction: Horizontal → flex-direction: row
- Direction: Vertical → flex-direction: column
- Spacing → gap
- Padding → padding
- Primary Axis Alignment → justify-content
- Counter Axis Alignment → align-items
```

## 示例：从Figma生成代码

1. 获取文件结构
2. 遍历页面节点
3. 提取样式信息
4. 转换为HTML/CSS
5. 应用选定风格

```
输入: Figma File Key + 页面ID
输出: 高保真HTML/CSS代码
```
