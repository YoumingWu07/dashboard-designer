# 墨刀适配器

本文档说明如何对接墨刀原型平台。

## 概述

墨刀（modao.cc）是一个在线原型设计工具。目前暂无官方MCP Server，需要自建。

## 自建MCP Server

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
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const axios = require('axios');

class ModaoMCPServer {
    constructor() {
        this.server = new Server({
            name: 'modao-mcp-server',
            version: '1.0.0'
        }, {
            capabilities: { tools: {} }
        });

        this.apiBase = process.env.MODAO_API_BASE || 'https://api.modao.cc/v1';
        this.token = process.env.MODAO_API_TOKEN;

        this.setupToolHandlers();
    }

    setupToolHandlers() {
        // 工具列表
        this.server.setRequestHandler('tools/list', async () => ({
            tools: [
                {
                    name: 'get_project',
                    description: '获取墨刀项目信息',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            project_id: {
                                type: 'string',
                                description: '项目ID'
                            }
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
                            project_id: {
                                type: 'string',
                                description: '项目ID'
                            }
                        },
                        required: ['project_id']
                    }
                },
                {
                    name: 'get_screen_detail',
                    description: '获取屏幕详情',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            screen_id: {
                                type: 'string',
                                description: '屏幕ID'
                            }
                        },
                        required: ['screen_id']
                    }
                }
            ]
        }));

        // 工具调用处理
        this.server.setRequestHandler('tools/call', async (request) => {
            const { name, arguments: args } = request.params;
            try {
                const result = await this.callModaoAPI(name, args);
                return {
                    content: [{
                        type: 'text',
                        text: JSON.stringify(result, null, 2)
                    }]
                };
            } catch (error) {
                return {
                    content: [{
                        type: 'text',
                        text: `Error: ${error.message}`
                    }],
                    isError: true
                };
            }
        });
    }

    async callModaoAPI(toolName, args) {
        const headers = {
            'Authorization': `Bearer ${this.token}`,
            'Content-Type': 'application/json'
        };

        switch (toolName) {
            case 'get_project':
                const projectRes = await axios.get(
                    `${this.apiBase}/projects/${args.project_id}`,
                    { headers }
                );
                return projectRes.data;

            case 'get_screens':
                const screensRes = await axios.get(
                    `${this.apiBase}/projects/${args.project_id}/screens`,
                    { headers }
                );
                return screensRes.data;

            case 'get_screen_detail':
                const screenRes = await axios.get(
                    `${this.apiBase}/screens/${args.screen_id}`,
                    { headers }
                );
                return screenRes.data;

            default:
                throw new Error(`Unknown tool: ${toolName}`);
        }
    }

    async run() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
    }
}

const server = new ModaoMCPServer();
server.run().catch(console.error);
```

### 3. 配置MCP

在 Claude 的 MCP 配置中添加：

```json
{
  "mcpServers": {
    "modao": {
      "command": "node",
      "args": ["/path/to/modao-mcp-server/index.js"],
      "env": {
        "MODAO_API_TOKEN": "${MODAO_TOKEN}",
        "MODAO_API_BASE": "https://api.modao.cc/v1"
      }
    }
  }
}
```

## 墨刀API参考

### 获取项目信息

```
GET /projects/{project_id}
```

返回：
```json
{
  "id": "proj_abc123",
  "name": "销售驾驶舱原型",
  "description": "BI看板原型设计",
  "screen_count": 5,
  "created_at": "2024-01-15T10:00:00Z"
}
```

### 获取屏幕列表

```
GET /projects/{project_id}/screens
```

返回：
```json
{
  "screens": [
    {
      "id": "screen_001",
      "name": "概览页",
      "thumbnail_url": "https://...",
      "width": 1440,
      "height": 900
    }
  ]
}
```

### 获取屏幕详情

```
GET /screens/{screen_id}
```

返回屏幕的详细组件结构和属性。

## 数据转换

### 墨刀组件映射

| 墨刀组件 | HTML元素 |
|---------|---------|
| 矩形 | `<div>` |
| 文本 | `<span>` / `<p>` |
| 图片 | `<img>` |
| 按钮 | `<button>` |
| 输入框 | `<input>` |
| 列表 | `<ul>` / `<ol>` |
| 表格 | `<table>` |

### 交互转换

| 墨刀交互 | JavaScript实现 |
|---------|---------------|
| 页面跳转 | `location.href` |
| 显示/隐藏 | `style.display` |
| 弹窗 | Modal组件 |
| 滑动 | Swiper库 |

## 使用流程

1. 配置墨刀Token到环境变量
2. 在design-tools.yaml中配置项目
3. 启动MCP Server
4. 通过工具获取原型数据
5. 解析并转换为UI代码
