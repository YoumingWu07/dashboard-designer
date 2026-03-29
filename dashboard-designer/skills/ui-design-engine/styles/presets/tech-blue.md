# 科技蓝风格

深色背景 + 蓝色高光，适合数据监控大屏、指挥中心。

## 基本信息

```yaml
name: tech-blue
display_name: 科技蓝风格
description: 深色背景+蓝色高光，适合数据监控大屏、指挥中心
version: 1.0.0
```

## 颜色配置

```yaml
colors:
  # 主色调
  primary: "#00d4ff"           # 科技蓝
  secondary: "#0095ff"         # 次要蓝
  accent: "#ff6b35"            # 强调色-橙色
  success: "#00ff88"           # 成功-绿色
  warning: "#ffcc00"           # 警告-黄色
  danger: "#ff4757"            # 危险-红色

  # 背景色
  background:
    base: "#0a1628"            # 基础背景-深蓝黑
    card: "#0d1f3c"            # 卡片背景
    elevated: "#132743"        # 悬浮背景
    hover: "#1a3a5c"           # 悬停背景

  # 文字色
  text:
    primary: "#ffffff"         # 主文字-白色
    secondary: "#8b9cc2"       # 次要文字
    muted: "#5a6b8a"           # 弱化文字
    inverse: "#0a1628"         # 反色文字
```

## 图表配色

```yaml
charts:
  palette:
    - "#00d4ff"                # 主色
    - "#0095ff"                # 次色
    - "#6366f1"                # 靛蓝
    - "#8b5cf6"                # 紫色
    - "#ec4899"                # 粉色
  gradient: true               # 启用渐变
  glow: true                   # 启用发光效果
  transparent_bg: true         # 透明背景
```

## 组件样式

```yaml
components:
  card:
    border_radius: 8
    shadow: "0 4px 24px rgba(0, 212, 255, 0.1)"
    border: "1px solid rgba(0, 212, 255, 0.2)"
    background: "#0d1f3c"

  button:
    border_radius: 4
    primary_background: "#00d4ff"
    primary_text: "#0a1628"
    hover_glow: true

  input:
    border_radius: 4
    border: "1px solid rgba(0, 212, 255, 0.3)"
    focus_border: "#00d4ff"
    background: "transparent"

  table:
    header_background: "#132743"
    row_hover: "#1a3a5c"
    border: "1px solid rgba(0, 212, 255, 0.1)"

  kpi_card:
    value_color: "#00d4ff"
    trend_up: "#00ff88"
    trend_down: "#ff4757"
```

## 特效配置

```yaml
effects:
  particle: true               # 粒子效果
  scanline: false              # 扫描线效果
  glow: true                   # 发光效果
  gradient_border: true        # 渐变边框
  animated_background: true    # 动态背景
```

## CSS变量

```css
:root {
  --color-primary: #00d4ff;
  --color-secondary: #0095ff;
  --color-accent: #ff6b35;
  --color-success: #00ff88;
  --color-warning: #ffcc00;
  --color-danger: #ff4757;
  --bg-base: #0a1628;
  --bg-card: #0d1f3c;
  --bg-elevated: #132743;
  --text-primary: #ffffff;
  --text-secondary: #8b9cc2;
  --text-muted: #5a6b8a;
  --border-radius: 8px;
  --shadow: 0 4px 24px rgba(0, 212, 255, 0.1);
  --border-glow: 1px solid rgba(0, 212, 255, 0.2);
}
```

## 示例代码

```html
<!-- 科技蓝风格KPI卡片 -->
<div class="kpi-card" style="
    background: var(--bg-card);
    border: var(--border-glow);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
">
    <div class="kpi-label" style="color: var(--text-secondary);">销售额</div>
    <div class="kpi-value" style="color: var(--color-primary);">¥ 1,285,000</div>
    <div class="kpi-trend" style="color: var(--color-success);">↑ 12.3%</div>
</div>
```
