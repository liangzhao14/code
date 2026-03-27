# 测试用例生成开放服务详细设计

## 1. 设计范围

本次详细设计覆盖 V1.0 的最小可运行闭环：

- 应用接入创建与查询
- HMAC 签名鉴权
- 同步/异步测试用例生成
- 任务状态查询与失败重试
- 限流与审计日志

## 2. 目录结构

```text
src/test_case_generation_api/
├── __init__.py
├── __main__.py
├── generator.py
├── models.py
├── server.py
└── services.py
```

## 3. 核心数据模型

| 模型 | 核心字段 | 说明 |
| --- | --- | --- |
| `Application` | `app_id`, `name`, `api_key_id`, `api_secret`, `callback_url` | 第三方接入应用 |
| `Task` | `task_id`, `app_id`, `request_id`, `status`, `result`, `error_code` | 生成任务 |
| `GeneratedCase` | `case_id`, `title`, `scenario`, `steps`, `expected_results` | 结构化测试用例 |
| `AuditEvent` | `event_type`, `app_id`, `detail`, `created_at` | 审计事件 |

## 4. 接口设计

### 4.1 创建接入应用

- `POST /api/v1/apps`
- 入参：`name`、`description`、`callback_url`、`contact`
- 出参：应用基础信息、`api_key_id`、`api_secret`

### 4.2 查询接入应用

- `GET /api/v1/apps/{app_id}`
- 出参：应用基础信息，不返回密钥明文

### 4.3 发起生成任务

- `POST /api/v1/tasks/generate`
- 鉴权头：
  - `X-App-Id`
  - `X-Timestamp`
  - `X-Nonce`
  - `X-Signature`
- 业务字段：
  - `request_id`
  - `title`
  - `description`
  - `generation_mode`
  - `template_id`
  - `coverage_dimensions`
  - `structured_rules`
  - `attachments`

### 4.4 查询任务

- `GET /api/v1/tasks/{task_id}`
- 头部：`X-App-Id`
- 返回任务状态、错误信息、结果列表

### 4.5 重试任务

- `POST /api/v1/tasks/{task_id}/retry`
- 使用与生成接口相同的鉴权方式
- 仅允许失败任务重试

## 5. 关键业务规则

| 规则编号 | 规则内容 |
| --- | --- |
| BR-01 | 接入应用名称必须唯一 |
| BR-02 | 回调地址如提供，必须为合法 `http/https` URL |
| BR-03 | 所有生成请求必须带 `request_id` |
| BR-04 | 请求签名按 `timestamp.nonce.canonical_json(body)` 计算 |
| BR-05 | 请求时间戳超过 5 分钟视为失效 |
| BR-06 | 默认每应用每分钟最多 60 次生成请求 |
| BR-07 | 仅失败任务可重试 |

## 6. 类与职责

| 类 | 职责 |
| --- | --- |
| `AppService` | 应用生命周期管理 |
| `AuthService` | 验签与请求时效校验 |
| `TaskService` | 任务受理、执行、状态管理 |
| `InMemoryRateLimiter` | 基于时间窗口的限流 |
| `AuditLog` | 审计事件收集 |
| `CaseFlowRequestHandler` | HTTP 请求处理与错误转换 |

## 7. 异常设计

| 错误码 | 场景 |
| --- | --- |
| `INVALID_APP_NAME` | 应用名缺失 |
| `APP_NAME_EXISTS` | 应用名重复 |
| `INVALID_CALLBACK_URL` | 回调地址格式错误 |
| `AUTH_HEADERS_MISSING` | 鉴权头缺失 |
| `SIGNATURE_INVALID` | 签名校验失败 |
| `TIMESTAMP_INVALID` | 时间戳格式错误 |
| `TIMESTAMP_EXPIRED` | 时间戳过期 |
| `REQUEST_ID_REQUIRED` | 请求流水号缺失 |
| `INPUT_REQUIRED` | 标题或描述缺失 |
| `RATE_LIMITED` | 命中限流 |
| `TASK_NOT_FOUND` | 任务不存在 |
| `TASK_FORBIDDEN` | 越权访问任务 |
| `TASK_NOT_RETRYABLE` | 非失败任务发起重试 |

## 8. 测试设计

| 被测对象 | 正常路径 | 边界/异常 |
| --- | --- | --- |
| `build_test_cases` | 按覆盖维度生成结构化用例 | 标题或描述缺失时报错 |
| `AppService` | 成功创建应用 | 重名应用拒绝 |
| `AuthService` | 合法签名通过认证 | 错误签名或过期时间戳拒绝 |
| `TaskService.submit` | 同步/异步任务成功 | 限流触发时报错 |

## 9. 后续扩展点

- 引入真实 LLM/规则引擎作为生成器实现
- 抽离仓储接口并接入数据库
- 增加回调下发、模板 CRUD、结果导出下载
