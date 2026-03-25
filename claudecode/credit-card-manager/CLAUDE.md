# credit-card-manager

信用卡还款与收支管理系统 — 前后端分离的个人财务管理应用。

## 快速启动（IDEA）

### 环境要求

| 依赖 | 版本 |
|------|------|
| JDK | 17+ |
| Maven | 3.8+ |
| Node.js | 18+ |
| MySQL | 8.0+ |

### 1. 数据库准备

```sql
-- 手动建库（或依赖 Spring Boot 自动初始化）
CREATE DATABASE IF NOT EXISTS finance_db DEFAULT CHARACTER SET utf8mb4;
```

MySQL 连接信息（见 `backend/src/main/resources/application.yml`）：
- 地址：`localhost:3306/finance_db`
- 用户：`root`
- 密码：`NewPass123!`

> 启动时 Spring Boot 会自动执行 `schema.sql`（建表）和 `data.sql`（默认支出分类数据）。

### 2. 后端启动（IDEA）

1. IDEA 中 **File → Open**，选择 `credit-card-manager/backend` 目录（或整个 `credit-card-manager`，然后将 `backend` 标记为 Maven 项目）
2. 等待 Maven 依赖下载完成
3. 运行 `com.finance.FinanceApplication` 的 `main` 方法
4. 后端启动在 **http://localhost:8081**

或命令行：
```bash
cd credit-card-manager/backend
mvn spring-boot:run
```

### 3. 前端启动

```bash
cd credit-card-manager/frontend
npm install   # 首次需要
npm run dev
```

前端启动在 **http://localhost:5173**，已配置代理将 `/api` 请求转发到后端 `8081` 端口。

### 4. 初始化账号

首次使用需要通过接口创建管理员：
```bash
curl -X POST http://localhost:8081/api/auth/init \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

## 技术架构

### 后端（Spring Boot 3.2.5）

| 技术 | 用途 |
|------|------|
| Spring Boot 3.2.5 | 基础框架 |
| Spring Security + JWT | 认证鉴权（JJWT 0.12.5） |
| MyBatis-Plus 3.5.6 | ORM 数据访问 |
| MySQL 8.0 | 主数据库 |
| Lombok | 简化实体类 |

**后端包结构** (`com.finance`)：
```
config/         — SecurityConfig, JwtUtil, JwtAuthenticationFilter
controller/     — REST API 控制器
dto/            — Result, LoginRequest, LoginResponse
entity/         — User, CreditCard, CreditCardBill, Income, Expense, ExpenseCategory
mapper/         — MyBatis-Plus Mapper 接口
service/        — 业务接口
service/impl/   — 业务实现
```

### 前端（Vue 3 + Vite）

| 技术 | 用途 |
|------|------|
| Vue 3 | UI 框架 |
| Vite 5 | 构建工具 |
| Vue Router 4 | 路由管理 |
| Pinia 2 | 状态管理 |
| Element Plus 2 | UI 组件库 |
| ECharts 5 | 图表可视化 |
| Axios | HTTP 请求 |

**前端目录结构**：
```
src/
  api/        — auth, cards, bills, incomes, expenses, categories, summary
  router/     — 路由配置，带登录守卫
  stores/     — Pinia 状态（user store）
  utils/      — request.js (axios 封装)
  views/      — Login, Layout, Dashboard, CreditCards, Bills, Incomes, Expenses, MonthlyReport
```

## 功能模块

| 模块 | 路由 | 说明 |
|------|------|------|
| 登录 | `/login` | JWT 认证 |
| 仪表盘 | `/dashboard` | 总览数据 |
| 信用卡管理 | `/cards` | 增删改查信用卡信息（银行、额度、账单日、还款日） |
| 账单管理 | `/bills` | 月度账单录入，还款状态跟踪（未还/已还/部分还款） |
| 收入管理 | `/incomes` | 工资/奖金/其他收入记录 |
| 支出管理 | `/expenses` | 按分类记录支出，可关联信用卡 |
| 月度报表 | `/report` | ECharts 图表展示月度收支分析 |

## 数据库表

- `user` — 用户（单用户系统）
- `credit_card` — 信用卡信息
- `credit_card_bill` — 信用卡月度账单
- `income` — 收入记录
- `expense_category` — 支出分类（预置 9 类）
- `expense` — 支出记录（关联分类，可选关联信用卡）

## API 端口约定

- 后端：`8081`
- 前端开发服务器：`5173`（Vite 代理 `/api` → `8081`）

## 开发约定

- 每次功能修改须更新 `CHANGELOG.md`
- 后端 REST API 统一返回 `Result<T>` 包装格式
- 前端请求统一通过 `src/utils/request.js` 封装的 axios 实例
- 路由均需登录认证（`meta.requiresAuth: true`），登录页除外
