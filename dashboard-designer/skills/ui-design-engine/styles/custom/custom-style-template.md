# 自定义风格模板

复制此文件到 `styles/custom/` 目录，重命名并修改配置。

## 基本信息

```yaml
name: my-custom-style                    # 风格标识（英文，无空格）
display_name: 自定义风格                  # 风格显示名称
description: 描述这个风格的特点和适用场景  # 风格描述
version: 1.0.0
extends: minimal-light                   # 可选：继承现有风格
```

## 颜色配置

```yaml
colors:
  # 主色调
  primary: "#4f46e5"           # 主色
  secondary: "#6366f1"         # 次要色
  accent: "#f59e0b"            # 强调色
  success: "#10b981"           # 成功色
  warning: "#f59e0b"           # 警告色
  danger: "#ef4444"            # 危险色

  # 背景色
  background:
    base: "#f8fafc"            # 页面背景
    card: "#ffffff"            # 卡片背景
    elevated: "#ffffff"        # 悬浮元素背景
    hover: "#f1f5f9"           # 悬停背景

  # 文字色
  text:
    primary: "#1e293b"         # 主文字
    secondary: "#64748b"       # 次要文字
    muted: "#94a3b8"           # 弱化文字
    inverse: "#ffffff"         # 反色文字
```

## 图表配色

```yaml
charts:
  palette:                      # 图表配色序列
    - "#4f46e5"
    - "#06b6d4"
    - "#10b981"
    - "#f59e0b"
    - "#ef4444"
  gradient: false               # 是否使用渐变
  glow: false                   # 是否使用发光效果
  transparent_bg: false         # 是否透明背景
```

## 组件样式

```yaml
components:
  card:
    border_radius: 12           # 圆角大小
    shadow: "0 1px 3px rgba(0, 0, 0, 0.1)"
    border: "1px solid #e2e8f0"
    background: "#ffffff"

  button:
    border_radius: 8
    primary_background: "#4f46e5"
    primary_text: "#ffffff"
    hover_glow: false

  input:
    border_radius: 8
    border: "1px solid #e2e8f0"
    focus_border: "#4f46e5"
    background: "#ffffff"

  table:
    header_background: "#f8fafc"
    row_hover: "#f1f5f9"
    border: "1px solid #e2e8f0"

  kpi_card:
    value_color: "#1e293b"
    trend_up: "#10b981"
    trend_down: "#ef4444"
```

## 特效配置

```yaml
effects:
  particle: false              # 粒子效果
  scanline: false              # 扫描线效果
  glow: false                  # 发光效果
  gradient_border: false       # 渐变边框
  animated_background: false   # 动态背景
```

## 自定义组件（可选）

可以添加自定义组件样式：

```yaml
custom_components:
  header:
    height: 64
    background: "#ffffff"
    border_bottom: "1px solid #e2e8f0"

  sidebar:
    width: 240
    background: "#ffffff"
    border_right: "1px solid #e2e8f0"

  footer:
    height: 48
    background: "#f8fafc"
```

## CSS变量输出

风格配置将自动转换为CSS变量：

```css
:root {
  --color-primary: #4f46e5;
  --color-secondary: #6366f1;
  /* ... 其他变量 */
}
```

## 继承现有风格

如果想基于现有风格进行微调，使用 `extends` 字段：

```yaml
name: my-company-style
display_name: 公司品牌风格
extends: minimal-light          # 继承简约素雅风格

# 只覆盖需要修改的配置
colors:
  primary: "#1890ff"           # 公司品牌色
```
