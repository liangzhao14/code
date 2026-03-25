# Changelog

所有对本项目的修改都会记录在此文件中。

格式：`## [版本号] - YYYY-MM-DD`，每条记录标注类型：`新增` / `修改` / `修复` / `删除` / `优化`。

---

## [1.3.0] - 2026-03-18

### 新增
- 后端：user 表新增 `avatar` 字段（默认 `preset:1`），支持预设标识或上传文件名
- 后端：新增 `UserController`
  - `PUT /api/user/avatar` — 切换预设头像（preset:1~6）
  - `POST /api/user/avatar/upload` — 上传自定义头像（支持 JPG/PNG/GIF/WebP，限 2MB）
  - `GET /api/user/profile` — 获取当前用户信息含头像
- 后端：新增 `WebConfig` 配置上传头像静态资源映射（`/api/avatars/uploads/**`）
- 后端：`LoginResponse` 新增 avatar 字段，登录接口返回头像信息
- 后端：SecurityConfig 放行 `/api/avatars/**` 路径
- 前端：新增 6 个预设头像 SVG（`public/avatars/preset-1~6.svg`），风格各异
- 前端：新增 `api/user.js`（getProfile、updateAvatar、uploadAvatar）
- 前端：user store 新增 `avatar` 计算属性和 `updateAvatar` 方法
- 前端：Layout 顶部栏头像从首字母文本改为实际图片显示
- 前端：用户下拉菜单新增"更换头像"选项
- 前端：头像选择弹窗 — 当前预览 + 6 个预设头像网格 + 自定义上传按钮
- 前端：Login.vue 登录成功后保存 avatar 到 store

---

## [1.2.1] - 2026-03-18

### 修复
- 前端：修复侧边栏折叠态图标与顶部 Logo 图标不对齐的问题
  - 根因：`:deep(.el-menu--collapse .el-menu-item)` 选择器无法匹配（`el-menu--collapse` 在自身而非子元素）
  - 改为在 `<el-aside>` 添加 `.collapsed` class，用 `.sidebar.collapsed :deep(...)` 控制折叠态样式
  - 统一 Logo 和菜单项图标尺寸为 `20px`，折叠态水平 margin/padding 均为 `10px`
  - 图标中心统一在 sidebar 宽度 64px 的正中 32px 处

---

## [1.2.0] - 2026-03-18

### 优化
- 前端：侧边栏全面重构样式
  - 引入 CSS 自定义属性（`--sidebar-bg`, `--primary`, `--sidebar-text` 等）统一全局色彩体系
  - 移除 `el-menu` 上硬编码的颜色属性，改为纯 CSS 控制
  - 侧边栏背景改用渐变色（`#0f1423` → `#161b2e`）
  - 菜单选中态：渐变蓝底 + 发光阴影 + 左侧白色指示条
  - 菜单悬浮态：蓝色半透背景 + 图标微缩放
  - 折叠态图标完全居中（flex 居中 + 清除 padding/margin）
  - Logo 图标加发光滤镜，用户头像改为渐变背景
  - 菜单滚动条美化为 3px 半透明样式
  - 所有过渡动画统一为 cubic-bezier(0.4, 0, 0.2, 1)

---

## [1.1.0] - 2026-03-18

### 新增
- 后端：新增 `NotificationController`（`/api/notifications`），提供通知数据接口
  - 还款提醒：查询 7 天内到期且未还清的信用卡账单，按紧急程度分级（danger/warning/info）
  - 逾期提醒：检测上月逾期未还账单
  - 系统消息：返回当月收支概况汇总
  - 通知按优先级排序（danger > warning > info），返回 unreadCount 用于角标显示
- 前端：新增 `api/notifications.js` 接口封装
- 前端：Layout 顶部栏铃铛按钮改为可交互的通知中心
  - 点击弹出 Popover 面板，展示还款提醒 + 逾期提醒 + 收支概况
  - 未读角标显示待处理通知数量
  - 页面加载时自动获取通知，每 60 秒轮询刷新
  - 不同级别通知用不同颜色区分

---

## [1.0.0] - 2026-03-18

项目初始化，搭建完整的前后端框架。

### 新增
- 后端：Spring Boot 3.2.5 + Spring Security + JWT 认证体系
- 后端：MyBatis-Plus 集成，6 张核心数据表（user, credit_card, credit_card_bill, income, expense_category, expense）
- 后端：完整 REST API — Auth、CreditCard、CreditCardBill、Income、Expense、ExpenseCategory、Summary、Dashboard 控制器
- 前端：Vue 3 + Vite 5 + Element Plus + ECharts 搭建
- 前端：7 个页面 — Login、Dashboard、CreditCards、Bills、Incomes、Expenses、MonthlyReport
- 前端：Pinia 用户状态管理 + axios 请求封装 + 路由守卫
- 数据库：自动初始化建表脚本 + 9 个默认支出分类
