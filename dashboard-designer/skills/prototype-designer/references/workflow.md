# 工作流配置

本文档定义了BI驾驶舱设计的完整工作流程配置。

## 工作流定义

```yaml
name: bi-dashboard-design
version: 1.0.0
description: BI驾驶舱设计全流程

steps:
  - id: input
    name: 接收输入
    type: input
    supported_types:
      - document
      - image
      - external_tool
    output:
      - raw_content

  - id: analysis
    name: 需求分析
    type: skill
    skill: requirement-analyzer
    input:
      - raw_content
    output:
      - functional_design_doc
      - data_model_excel
    next:
      - confirm_analysis

  - id: confirm_analysis
    name: 确认需求分析
    type: interaction
    method: AskUserQuestion
    options:
      - label: 继续生成原型
        next: prototype
      - label: 调整需求分析
        next: analysis
      - label: 只需要功能设计文档
        next: end

  - id: prototype
    name: 原型生成
    type: skill
    skill: prototype-generator
    input:
      - functional_design_doc
    output:
      - ascii_wireframe
      - html_prototype
    next:
      - confirm_prototype

  - id: confirm_prototype
    name: 确认原型
    type: interaction
    method: AskUserQuestion
    options:
      - label: 继续生成高保真UI
        next: style_selection
      - label: 调整原型设计
        next: prototype
      - label: 只需要原型
        next: end

  - id: style_selection
    name: 选择UI风格
    type: interaction
    method: AskUserQuestion
    options:
      - label: 科技蓝风格
        value: tech-blue
        next: ui_generation
      - label: 简约素雅风格
        value: minimal-light
        next: ui_generation
      - label: 深色专业风格
        value: dark-pro
        next: ui_generation
      - label: 企业商务风格
        value: corporate
        next: ui_generation
      - label: 自定义风格
        value: custom
        next: ui_generation

  - id: ui_generation
    name: UI生成
    type: skill
    skill: ui-design-engine
    input:
      - html_prototype
      - selected_style
    output:
      - high_fidelity_ui
    next: end

  - id: end
    name: 完成
    type: terminal
```

## 状态管理

### 工作流状态

```json
{
  "session_id": "uuid",
  "project_name": "销售驾驶舱",
  "current_step": "prototype",
  "completed_steps": ["input", "analysis", "confirm_analysis"],
  "output_files": {
    "functional_design_doc": "output/销售驾驶舱/01_需求分析/功能设计文档.md",
    "data_model_excel": "output/销售驾驶舱/01_需求分析/数据模型设计.xlsx"
  },
  "user_choices": {
    "confirm_analysis": "继续生成原型"
  }
}
```

### 回滚支持

支持返回任意已完成步骤重新执行：

```yaml
rollback:
  supported: true
  preserve_output: false  # 回滚时是否保留后续步骤的输出
```

## 模块调用规范

### Skill调用

```
调用 {skill_name} skill
输入: {input_data}
期望输出: {expected_outputs}
```

### 用户交互

```
使用 AskUserQuestion
问题: {question}
选项:
  - {option_1} → {next_step_1}
  - {option_2} → {next_step_2}
```

### 文件操作

```
读取: {file_path}
写入: {file_path}
内容: {content}
```

## 错误处理

### 步骤失败

```yaml
on_error:
  action: retry  # retry | skip | abort
  max_retries: 3
  fallback_step: null
```

### 用户取消

```yaml
on_cancel:
  save_state: true
  output_partial: true
```

## 超时配置

```yaml
timeouts:
  step_timeout: 300      # 单步骤超时（秒）
  total_timeout: 3600    # 总流程超时（秒）
  interaction_timeout: 600  # 用户交互超时（秒）
```

## 日志记录

```yaml
logging:
  level: info
  format: "{timestamp} [{step}] {message}"
  file: "logs/workflow_{session_id}.log"
```
