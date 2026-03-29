<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{页面标题} - 看板原型</title>
    <style>
        /* ========== 基础样式 ========== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }

        /* ========== 布局容器 ========== */
        .dashboard-container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 20px;
        }

        /* ========== 头部区域 ========== */
        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 24px;
            background: #fff;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .dashboard-title {
            font-size: 24px;
            font-weight: 600;
            color: #1a1a2e;
        }

        .dashboard-toolbar {
            display: flex;
            gap: 12px;
        }

        /* ========== KPI卡片区 ========== */
        .kpi-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 20px;
        }

        .kpi-card {
            background: #fff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .kpi-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.12);
        }

        .kpi-label {
            font-size: 14px;
            color: #666;
            margin-bottom: 8px;
        }

        .kpi-value {
            font-size: 28px;
            font-weight: 700;
            color: #1a1a2e;
            margin-bottom: 8px;
        }

        .kpi-trend {
            display: flex;
            align-items: center;
            font-size: 14px;
        }

        .kpi-trend.up {
            color: #10b981;
        }

        .kpi-trend.down {
            color: #ef4444;
        }

        /* ========== 图表区域 ========== */
        .chart-row {
            display: grid;
            grid-template-columns: 60% 40%;
            gap: 20px;
            margin-bottom: 20px;
        }

        .chart-card {
            background: #fff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .chart-title {
            font-size: 16px;
            font-weight: 600;
            color: #1a1a2e;
            margin-bottom: 16px;
        }

        .chart-placeholder {
            height: 250px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #999;
            font-size: 14px;
        }

        /* ========== 表格区域 ========== */
        .table-card {
            background: #fff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .table-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }

        .table-title {
            font-size: 16px;
            font-weight: 600;
            color: #1a1a2e;
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
        }

        .data-table th,
        .data-table td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }

        .data-table th {
            background: #f8f9fa;
            font-weight: 600;
            color: #666;
            font-size: 13px;
        }

        .data-table td {
            color: #333;
        }

        .data-table tr:hover {
            background: #f8f9fa;
        }

        /* ========== 按钮样式 ========== */
        .btn {
            padding: 8px 16px;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }

        .btn-primary {
            background: #4f46e5;
            color: #fff;
        }

        .btn-primary:hover {
            background: #4338ca;
        }

        .btn-secondary {
            background: #f1f5f9;
            color: #64748b;
        }

        .btn-secondary:hover {
            background: #e2e8f0;
        }

        /* ========== 筛选器样式 ========== */
        .filter-select {
            padding: 8px 12px;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            font-size: 14px;
            background: #fff;
            cursor: pointer;
        }

        /* ========== 响应式 ========== */
        @media (max-width: 1200px) {
            .kpi-row {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .kpi-row {
                grid-template-columns: 1fr;
            }
            .chart-row {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- 头部 -->
        <header class="dashboard-header">
            <h1 class="dashboard-title">📊 {页面标题}</h1>
            <div class="dashboard-toolbar">
                <select class="filter-select">
                    <option>本月</option>
                    <option>上月</option>
                    <option>近三月</option>
                </select>
                <button class="btn btn-secondary">🔄 刷新</button>
                <button class="btn btn-primary">📥 导出</button>
            </div>
        </header>

        <!-- KPI卡片区 -->
        <div class="kpi-row">
            <div class="kpi-card">
                <div class="kpi-label">📊 销售额</div>
                <div class="kpi-value">¥ 1,285,000</div>
                <div class="kpi-trend up">↑ 12.3% 环比</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">📦 订单数</div>
                <div class="kpi-value">3,256</div>
                <div class="kpi-trend up">↑ 5.2% 环比</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">👥 客户数</div>
                <div class="kpi-value">1,892</div>
                <div class="kpi-trend down">↓ 2.1% 环比</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">📈 转化率</div>
                <div class="kpi-value">23.5%</div>
                <div class="kpi-trend up">↑ 1.8% 环比</div>
            </div>
        </div>

        <!-- 图表区 -->
        <div class="chart-row">
            <div class="chart-card">
                <div class="chart-title">📈 销售趋势</div>
                <div class="chart-placeholder">
                    [折线图占位 - 实际项目中使用ECharts/Chart.js]
                </div>
            </div>
            <div class="chart-card">
                <div class="chart-title">🥧 销售占比</div>
                <div class="chart-placeholder">
                    [饼图占位 - 实际项目中使用ECharts/Chart.js]
                </div>
            </div>
        </div>

        <!-- 表格区 -->
        <div class="table-card">
            <div class="table-header">
                <h3 class="table-title">📋 区域销售明细</h3>
                <button class="btn btn-secondary">📥 导出数据</button>
            </div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>区域</th>
                        <th>销售额</th>
                        <th>订单数</th>
                        <th>客户数</th>
                        <th>同比</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>华东</td>
                        <td>¥ 450,000</td>
                        <td>1,200</td>
                        <td>680</td>
                        <td style="color: #10b981;">+15%</td>
                    </tr>
                    <tr>
                        <td>华南</td>
                        <td>¥ 380,000</td>
                        <td>980</td>
                        <td>520</td>
                        <td style="color: #10b981;">+8%</td>
                    </tr>
                    <tr>
                        <td>华北</td>
                        <td>¥ 320,000</td>
                        <td>850</td>
                        <td>460</td>
                        <td style="color: #ef4444;">-3%</td>
                    </tr>
                    <tr>
                        <td>西部</td>
                        <td>¥ 280,000</td>
                        <td>720</td>
                        <td>380</td>
                        <td style="color: #10b981;">+5%</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
