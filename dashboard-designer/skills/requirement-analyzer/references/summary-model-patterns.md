# 汇总层数据模型模式参考

本文档定义了BI驾驶舱汇总层数据模型的设计模式。

## 设计原则

1. **直接可用**: 数据已聚合，无需再次计算
2. **面向展示**: 字段设计直接对应图表组件
3. **适度冗余**: 为了查询性能，允许适当冗余
4. **维度一致**: 确保各表维度定义一致

## 数据表命名规范

```
{业务域}_{时间粒度}_{指标}_summary

示例：
- sales_monthly_summary    # 月度销售汇总
- region_daily_summary     # 日区域汇总
- product_category_summary # 产品分类汇总
```

## 常用数据表模式

### 1. 时间序列汇总表

适用于：趋势图、KPI卡片

```sql
CREATE TABLE monthly_summary (
    month VARCHAR(7),           -- 月份 2024-01
    business_unit VARCHAR(50),  -- 业务维度
    metric_1 DECIMAL(12,2),     -- 指标1
    metric_2 DECIMAL(12,2),     -- 指标2
    yoy_growth DECIMAL(5,2),    -- 同比增长
    mom_growth DECIMAL(5,2),    -- 环比增长
    PRIMARY KEY (month, business_unit)
);
```

### 2. 区域分布汇总表

适用于：地图、条形图

```sql
CREATE TABLE regional_summary (
    region_code VARCHAR(10),    -- 区域编码
    region_name VARCHAR(50),    -- 区域名称
    province VARCHAR(50),       -- 省份
    city VARCHAR(50),           -- 城市
    metric_1 DECIMAL(12,2),     -- 指标1
    target DECIMAL(12,2),       -- 目标值
    completion_rate DECIMAL(5,2), -- 完成率
    PRIMARY KEY (region_code, province, city)
);
```

### 3. 分类占比汇总表

适用于：饼图、环形图

```sql
CREATE TABLE category_summary (
    category_name VARCHAR(100), -- 分类名称
    sub_category VARCHAR(100),  -- 子分类
    metric_1 DECIMAL(12,2),     -- 指标1
    ratio DECIMAL(5,2),         -- 占比
    rank INT,                   -- 排名
    PRIMARY KEY (category_name, sub_category)
);
```

### 4. 明细汇总表

适用于：表格展示

```sql
CREATE TABLE detail_summary (
    id VARCHAR(20),             -- 唯一标识
    dimension_1 VARCHAR(50),    -- 维度1
    dimension_2 VARCHAR(50),    -- 维度2
    metric_1 DECIMAL(12,2),     -- 指标1
    metric_2 DECIMAL(12,2),     -- 指标2
    metric_3 DECIMAL(12,2),     -- 指标3
    status VARCHAR(20),         -- 状态
    update_time DATETIME        -- 更新时间
);
```

## 字段类型规范

| 字段类型 | 数据库类型 | 说明 |
|---------|-----------|------|
| 时间(月) | VARCHAR(7) | 格式: YYYY-MM |
| 时间(日) | DATE | 标准日期格式 |
| 时间(时) | DATETIME | 精确到小时 |
| 金额 | DECIMAL(12,2) | 12位整数，2位小数 |
| 比率 | DECIMAL(5,2) | 百分比，如12.35表示12.35% |
| 数量 | INT | 整数 |
| 名称 | VARCHAR(50-200) | 根据实际长度 |
| 编码 | VARCHAR(10-20) | 业务编码 |

## 常用指标计算

| 指标名称 | 计算方式 | 说明 |
|---------|---------|------|
| 同比增长 | (本期-去年同期)/去年同期*100 | 与去年同期对比 |
| 环比增长 | (本期-上期)/上期*100 | 与上一周期对比 |
| 完成率 | 实际值/目标值*100 | 目标达成情况 |
| 占比 | 部分值/总计值*100 | 占整体比例 |
| 平均值 | SUM/COUNT | 平均水平 |
| 累计值 | SUM(本期及之前所有值) | 累计总量 |

## 维度层级设计

### 时间维度

```
年 → 季 → 月 → 周 → 日 → 时
```

### 区域维度

```
大区 → 省 → 市 → 区县
```

### 组织维度

```
集团 → 事业部 → 部门 → 团队
```

### 产品维度

```
产品线 → 产品分类 → 产品系列 → 产品
```

## 数据更新策略

| 场景 | 更新频率 | 更新方式 |
|------|---------|---------|
| 日常报表 | T+1 | 每日定时任务 |
| 实时监控 | 实时/准实时 | 流式计算 |
| 月度分析 | 月初 | 月度任务 |
| 大屏展示 | 分钟级 | 定时刷新 |
