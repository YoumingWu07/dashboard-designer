# 深色专业风格

深灰背景 + 多色图表，适合数据分析平台、BI工具。

## 基本信息

```yaml
name: dark-pro
display_name: 深色专业风格
description: 深灰背景+多色图表，适合数据分析平台、BI工具
version: 1.0.0
```

## 颜色配置

```yaml
colors:
  # 主色调
  primary: "#6366f1"           # 靛蓝
  secondary: "#8b5cf6"         # 紫色
  accent: "#22d3ee"            # 强调色-青色
  success: "#22c55e"           # 成功-绿色
  warning: "#eab308"           # 警告-黄色
  danger: "#ef4444"            # 危险-红色

  # 背景色
  background:
    base: "#18181b"            # 基础背景-深灰
    card: "#27272a"            # 卡片背景
    elevated: "#3f3f46"        # 悬浮背景
    hover: "#52525b"           # 悬停背景

  # 文字色
  text:
    primary: "#fafafa"         # 主文字-白色
    secondary: "#a1a1aa"       # 次要文字
    muted: "#71717a"           # 弱化文字
    inverse: "#18181b"         # 反色文字
```

## 图表配色

```yaml
charts:
  palette:
    - "#6366f1"                # 靛蓝
    - "#8b5cf6"                # 紫色
    - "#ec4899"                # 粉色
    - "#22d3ee"                # 青色
    - "#22c55e"                # 绿色
    - "#eab308"                # 黄色
  gradient: true               # 启用渐变
  glow: false                  # 不使用发光
  transparent_bg: true         # 透明背景
```

## 组件样式

```yaml
components:
  card:
    border_radius: 10
    shadow: "0 4px 6px rgba(0, 0, 0, 0.3)"
    border: "1px solid #3f3f46"
    background: "#27272a"

  button:
    border_radius: 6
    primary_background: "#6366f1"
    primary_text: "#ffffff"
    hover_glow: false

  input:
    border_radius: 6
    border: "1px solid #3f3f46"
    focus_border: "#6366f1"
    background: "#18181b"

  table:
    header_background: "#27272a"
    row_hover: "#3f3f46"
    border: "1px solid #3f3f46"

  kpi_card:
    value_color: "#fafafa"
    trend_up: "#22c55e"
    trend_down: "#ef4444"
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
  --color-primary: #6366f1;
  --color-secondary: #8b5cf6;
  --color-accent: #22d3ee;
  --color-success: #22c55e;
  --color-warning: #eab308;
  --color-danger: #ef4444;
  --bg-base: #18181b;
  --bg-card: #27272a;
  --bg-elevated: #3f3f46;
  --text-primary: #fafafa;
  --text-secondary: #a1a1aa;
  --text-muted: #71717a;
  --border-radius: 10px;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  --border: 1px solid #3f3f46;
}
```
