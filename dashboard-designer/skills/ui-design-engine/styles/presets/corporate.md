# 企业商务风格

蓝色主色调 + 白色背景，适合管理驾驶舱、汇报展示。

## 基本信息

```yaml
name: corporate
display_name: 企业商务风格
description: 蓝色主色调+白色背景，适合管理驾驶舱、汇报展示
version: 1.0.0
```

## 颜色配置

```yaml
colors:
  # 主色调
  primary: "#1890ff"           # 蓝色
  secondary: "#40a9ff"         # 浅蓝
  accent: "#fa8c16"            # 强调色-橙色
  success: "#52c41a"           # 成功-绿色
  warning: "#faad14"           # 警告-黄色
  danger: "#ff4d4f"            # 危险-红色

  # 背景色
  background:
    base: "#f0f2f5"            # 基础背景-浅灰
    card: "#ffffff"            # 卡片背景-白色
    elevated: "#ffffff"        # 悬浮背景
    hover: "#e6f7ff"           # 悬停背景-浅蓝

  # 文字色
  text:
    primary: "#262626"         # 主文字-深灰
    secondary: "#595959"       # 次要文字
    muted: "#8c8c8c"           # 弱化文字
    inverse: "#ffffff"         # 反色文字
```

## 图表配色

```yaml
charts:
  palette:
    - "#1890ff"                # 主色-蓝
    - "#52c41a"                # 绿色
    - "#fa8c16"                # 橙色
    - "#722ed1"                # 紫色
    - "#eb2f96"                # 粉色
  gradient: false              # 不使用渐变
  glow: false                  # 不使用发光
  transparent_bg: false        # 不透明背景
```

## 组件样式

```yaml
components:
  card:
    border_radius: 4
    shadow: "0 1px 2px rgba(0, 0, 0, 0.03), 0 2px 4px rgba(0, 0, 0, 0.03)"
    border: "none"
    background: "#ffffff"

  button:
    border_radius: 4
    primary_background: "#1890ff"
    primary_text: "#ffffff"
    hover_glow: false

  input:
    border_radius: 4
    border: "1px solid #d9d9d9"
    focus_border: "#1890ff"
    background: "#ffffff"

  table:
    header_background: "#fafafa"
    row_hover: "#e6f7ff"
    border: "1px solid #e8e8e8"

  kpi_card:
    value_color: "#262626"
    trend_up: "#52c41a"
    trend_down: "#ff4d4f"
```

## 特效配置

```yaml
effects:
  particle: false              # 无粒子效果
  scanline: false              # 无扫描线
  glow: false                  # 无发光效果
  gradient_border: false       # 无渐变边框
  animated_background: false   # 无动态背景
```

## CSS变量

```css
:root {
  --color-primary: #1890ff;
  --color-secondary: #40a9ff;
  --color-accent: #fa8c16;
  --color-success: #52c41a;
  --color-warning: #faad14;
  --color-danger: #ff4d4f;
  --bg-base: #f0f2f5;
  --bg-card: #ffffff;
  --bg-elevated: #ffffff;
  --text-primary: #262626;
  --text-secondary: #595959;
  --text-muted: #8c8c8c;
  --border-radius: 4px;
  --shadow: 0 1px 2px rgba(0, 0, 0, 0.03), 0 2px 4px rgba(0, 0, 0, 0.03);
  --border: 1px solid #d9d9d9;
}
```

## 示例代码

```html
<!-- 企业商务风格KPI卡片 -->
<div class="kpi-card" style="
    background: var(--bg-card);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
">
    <div class="kpi-label" style="color: var(--text-secondary);">销售额</div>
    <div class="kpi-value" style="color: var(--text-primary);">¥ 1,285,000</div>
    <div class="kpi-trend" style="color: var(--color-success);">↑ 12.3%</div>
</div>
```
