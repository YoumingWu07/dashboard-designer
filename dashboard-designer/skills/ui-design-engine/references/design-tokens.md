# 设计Token规范

本文档定义了设计系统的Token规范，用于确保UI风格的一致性。

## Token分类

### 1. 颜色Token (Color Tokens)

#### 语义颜色

| Token名称 | 用途 | 示例值 |
|----------|------|--------|
| `--color-primary` | 主色调 | #4f46e5 |
| `--color-secondary` | 次要色 | #6366f1 |
| `--color-accent` | 强调色 | #f59e0b |
| `--color-success` | 成功状态 | #10b981 |
| `--color-warning` | 警告状态 | #f59e0b |
| `--color-danger` | 危险状态 | #ef4444 |

#### 背景颜色

| Token名称 | 用途 | 示例值 |
|----------|------|--------|
| `--bg-base` | 页面基础背景 | #f8fafc |
| `--bg-card` | 卡片背景 | #ffffff |
| `--bg-elevated` | 悬浮元素背景 | #ffffff |
| `--bg-hover` | 悬停状态背景 | #f1f5f9 |

#### 文字颜色

| Token名称 | 用途 | 示例值 |
|----------|------|--------|
| `--text-primary` | 主要文字 | #1e293b |
| `--text-secondary` | 次要文字 | #64748b |
| `--text-muted` | 弱化文字 | #94a3b8 |
| `--text-inverse` | 反色文字 | #ffffff |

### 2. 间距Token (Spacing Tokens)

使用8px基础单位的间距系统：

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--space-1` | 4px | 极小间距 |
| `--space-2` | 8px | 小间距 |
| `--space-3` | 12px | 中小间距 |
| `--space-4` | 16px | 标准间距 |
| `--space-5` | 20px | 中等间距 |
| `--space-6` | 24px | 大间距 |
| `--space-8` | 32px | 较大间距 |
| `--space-10` | 40px | 大间距 |
| `--space-12` | 48px | 超大间距 |

### 3. 圆角Token (Border Radius Tokens)

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--radius-sm` | 4px | 小圆角（按钮、标签） |
| `--radius-md` | 8px | 中圆角（输入框） |
| `--radius-lg` | 12px | 大圆角（卡片） |
| `--radius-xl` | 16px | 超大圆角 |
| `--radius-full` | 9999px | 圆形 |

### 4. 阴影Token (Shadow Tokens)

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--shadow-sm` | 0 1px 2px rgba(0,0,0,0.05) | 轻微阴影 |
| `--shadow-md` | 0 4px 6px rgba(0,0,0,0.1) | 标准阴影 |
| `--shadow-lg` | 0 10px 15px rgba(0,0,0,0.1) | 大阴影 |
| `--shadow-xl` | 0 20px 25px rgba(0,0,0,0.1) | 超大阴影 |

### 5. 字体Token (Typography Tokens)

#### 字体大小

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--text-xs` | 12px | 辅助文字 |
| `--text-sm` | 14px | 小号文字 |
| `--text-base` | 16px | 标准文字 |
| `--text-lg` | 18px | 大号文字 |
| `--text-xl` | 20px | 标题文字 |
| `--text-2xl` | 24px | 大标题 |
| `--text-3xl` | 30px | 超大标题 |

#### 字重

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--font-normal` | 400 | 正常字重 |
| `--font-medium` | 500 | 中等字重 |
| `--font-semibold` | 600 | 半粗体 |
| `--font-bold` | 700 | 粗体 |

#### 行高

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--leading-tight` | 1.25 | 紧凑行高 |
| `--leading-normal` | 1.5 | 正常行高 |
| `--leading-relaxed` | 1.75 | 宽松行高 |

### 6. 动画Token (Animation Tokens)

| Token名称 | 值 | 用途 |
|----------|-----|------|
| `--duration-fast` | 150ms | 快速动画 |
| `--duration-normal` | 300ms | 标准动画 |
| `--duration-slow` | 500ms | 慢速动画 |
| `--ease-in` | cubic-bezier(0.4, 0, 1, 1) | 缓入 |
| `--ease-out` | cubic-bezier(0, 0, 0.2, 1) | 缓出 |
| `--ease-in-out` | cubic-bezier(0.4, 0, 0.2, 1) | 缓入缓出 |

## Token使用示例

### CSS变量定义

```css
:root {
  /* 颜色 */
  --color-primary: #4f46e5;
  --bg-base: #f8fafc;
  --text-primary: #1e293b;

  /* 间距 */
  --space-4: 16px;

  /* 圆角 */
  --radius-lg: 12px;

  /* 阴影 */
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
}
```

### 组件使用

```css
.card {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--space-4);
}

.card-title {
  color: var(--text-primary);
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
}
```

## Token与风格配置的对应

| Token | 风格配置路径 |
|-------|-------------|
| `--color-primary` | colors.primary |
| `--bg-base` | colors.background.base |
| `--text-primary` | colors.text.primary |
| `--radius-lg` | components.card.border_radius |
| `--shadow-md` | components.card.shadow |
