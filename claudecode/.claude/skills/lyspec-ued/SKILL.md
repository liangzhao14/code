---
name: lyspec-ued
description: 'UI/UE设计与HTML Demo生成。当用户说"设计界面"、"画页面"、"UED设计"、"交互设计"、"原型设计"时使用。基于羚羊设计系统，生成可交互HTML Demo和页面清单。'
---

# UI/UE 设计规范与页面生成模板（AI友好版）

> 基于羚羊设计系统（Lingyang Design System），面向AI辅助生成场景。
> 本文档处于软件生命周期的"PRD→**UI/UE设计**→详细设计"阶段。
> 组件和页面参考文档通过 references/ 按需加载，避免一次性消耗过多 context。

**设计系统**: 羚羊设计系统 | **组件库**: lingyang | **产物**: HTML Demo

---

## 全局规则

| 内容类型 | 格式要求 |
|----------|----------|
| 页面布局描述 | Mermaid 图 或 组件树文本 |
| 样式值 | 必须使用 `references/design-tokens.md` 定义的 Token，禁止硬编码 |
| 页面模板 | 参考 `references/page-patterns.md` 选择模板并遵循必须结构清单 |

### 信息提取策略

| 级别 | 处理方式 |
|------|----------|
| ① 直接提取 | PRD中有明确描述 → 直接使用，标注"PRD" |
| ② AI推导 | 可从业务场景推导 → 标注"AI推导"，*斜体标识* |
| ③ 待补充 | 完全无依据 → 标注"待补充"，询问用户 |

### 术语一致性

- 页面名称、功能名称必须与PRD一致
- 组件名称使用 lingyang 设计系统官方命名

---

## 前置条件

### 上游文档

| 文档 | 必需/可选 | 提取内容 |
|------|-----------|----------|
| PRD | **必需** | 页面清单、功能点、交互规则、角色权限 |
| 架构设计文档 | 可选 | 前端技术栈、模块划分 |
| UI设计稿 | 可选 | 视觉还原基准 |

### AI执行流程

1. **判断是否需要UED** — 新系统→执行；小迭代→询问用户
2. **从PRD提取**（必须逐项检查）：
   - 3.1 功能结构图 → 侧边栏菜单
   - 3.2 功能清单 → 页面/弹窗映射
   - 3.4 页面导航关系图 → 跳转链接
   - 4.x 关键交互动作表 → Modal/Drawer/确认弹窗
   - 4.x 状态-操作矩阵 → 按钮显隐逻辑
   - 4.x 配置项清单表（变体A）→ Settings 页 Tab 表单字段
   - 4.x 展示要素清单表（变体B）→ 看板/分析页布局
   - 2.2 目标用户 → 角色权限差异
   > 若 PRD 缺失交互表，从 CRUD 语义推导；缺失配置项表，从业务语义推导（≥3项/分组）
3. **确认技术栈**（Vue 3 / React）
4. **确认屏幕适配**（默认 1440px 桌面端）
5. **加载参考文档**：`read references/page-patterns.md` + `read references/design-tokens.md`
6. **进入设计流程**

---

## 设计流程（三阶段）

### 阶段一：页面规划

> **产出**：页面清单 + 导航结构 + 页面模板选择
> **参考**：`read references/page-patterns.md`（页面模板选择指引）

**页面清单表格式**：

| 页面名称 | 路由 | 所属模块 | 页面模板类型 | 核心功能 | 包含的覆盖层（Modal/Drawer） | 角色权限 |
|---------|------|---------|-------------|---------|--------------------------|---------|

**AI生成规则**：
- 页面名称与PRD一致，路由 kebab-case
- 覆盖层从PRD交互动作表提取；无交互表时从 CRUD 推导（新增→Modal、编辑→Drawer、删除→Confirm）
- **非 CRUD 页面**：按 `references/page-patterns.md` 中的「非 CRUD 交互推导规则」处理

**阶段一完成后暂停**，等待用户确认。

### 阶段二：布局与组件设计

> **产出**：每个页面的组件树 + 布局方案
> **参考**：`read references/page-patterns.md`（组件选择决策树 + 必须结构清单）

**组件树须含覆盖层子树**（使用 `【Modal】`/`【Drawer】`/`【Confirm】` 前缀）。每个覆盖层包含：内部字段、校验规则、按钮行为。

**阶段二完成后暂停**，等待用户确认。

### 阶段三：HTML Demo 生成

> **产出**：`doc/{projectName}_{projectVersion}_UED/` 文件夹
> **必读**：`read references/design-tokens.md`（CSS 变量模板）+ `read references/pages/shared-tokens.md`（布局规格）

**步骤**：
1. 生成 `assets/styles.css`（CSS 变量必须与 `references/design-tokens.md` 中的模板**完全一致**）
2. 按页面逐一生成 `pages/{页面名}.html`
3. 生成 `index.html`（总入口）
4. 生成 `README.md`（8章结构设计说明文档）

**AI生成规则**：
- 不依赖 npm 安装或构建流程，HTML 文件打开即可预览
- **允许通过 CDN `<script>` 标签引入外部库**（如图表库 ECharts、工具库等），按需引入，不滥用
- **CSS 变量名禁止修改**（参见 `references/design-tokens.md` 的命名规范）
- **每种页面模板必须满足 `references/page-patterns.md` 中的「必须结构清单」**
- 委托给子 agent 时，prompt 中必须嵌入 CSS 变量模板全文

**页面视觉必备元素**（每个标准页面必须包含，登录页除外）：

| 必备元素 | CSS 类名 | 说明 |
|---------|---------|------|
| 侧边栏 Logo | `.logo-icon` + `.logo-text` | 品牌色方块图标+名称 |
| 菜单图标 | `.nav-icon` | Unicode emoji 或 SVG |
| 子菜单折叠 | `.nav-group-title` + `.nav-submenu` | 点击展开/收起 |
| Topbar | `.topbar` > `.breadcrumb` + `.topbar-search` + `.topbar-icon-btn`(通知) + `.topbar-avatar`(头像) | 面包屑+搜索+通知下拉面板+头像下拉菜单 |
| 页面标题栏 | `.page-header` > `.page-title` | 20px, font-weight 600 |
| 指标卡 | `.stat-bar` > `.stat-card` > `.stat-icon` + `.stat-info` | 含圆形图标背景 |

**styles.css 必须定义的页面级组件类**：
`.logo-icon` `.logo-text` `.nav-icon` `.nav-submenu` `.topbar` `.topbar-left` `.topbar-right` `.breadcrumb` `.topbar-search` `.topbar-avatar` `.topbar-icon-btn` `.badge-dot` `.topbar-dropdown` `.topbar-notify-panel` `.topbar-notify-header` `.topbar-notify-item` `.topbar-notify-dot` `.topbar-notify-content` `.topbar-notify-text` `.topbar-notify-time` `.topbar-notify-footer` `.topbar-avatar-menu` `.topbar-avatar-menu-item` `.topbar-avatar-menu-divider` `.page-header` `.page-title` `.stat-bar` `.stat-card` `.stat-icon` `.stat-info` `.stat-value` `.stat-label` `.icon-red` `.icon-green` `.icon-orange` `.icon-blue` `.toolbar` `.toolbar-left` `.toolbar-right` `.rank-list` `.rank-num` `.chart-box` `.multi-select` `.multi-select-trigger` `.ms-tag` `.ms-tag-close` `.ms-placeholder` `.multi-select-dropdown` `.multi-select-option`

**覆盖层生成规则**：
- 嵌入页面 HTML 末尾，默认 `display:none`
- **必须提供 JS** 实现开关（openModal/closeModal/openDrawer/closeDrawer/showToast）
- 表单含完整字段、placeholder、必填标识
- 确认弹窗含警告图标和操作后果描述

**交互状态覆盖**（列表页至少2种）：空状态、表单校验错误、确认删除弹窗、操作成功 Toast

---

## 组件 Schema

### 全局共识规则

1. 命名统一 — `import { ... } from 'lingyang'`
2. 尺寸四档 — lingyang 独有 `mini`
3. 受控显隐 — `popupVisible` / `onVisibleChange`（非 Ant Design 的 `open`）
4. Form 字段名 — `field`（非 `name`）
5. Form 方法名 — `form.validate()` / `form.getFields()`
6. onChange 参数 — 第一参数为 value（非 event）
7. getPopupContainer — 无参数

### 组件目录

> 使用某组件前，先 `read references/components/<组件名>.md`。

| 分类 | 组件 |
|------|------|
| 布局 | Layout, Grid, Space, Divider |
| 表单 | Form, Input, Select, AutoComplete, Cascader, Radio, Checkbox, Upload |
| 导航 | Tabs |
| 展示 | Table, Badge, Tag |
| 操作 | Button, Popover, Message |

### 参考文档加载路径

| 任务 | 必读 | 按需读取 |
|------|------|---------|
| 生成 styles.css | `references/design-tokens.md` | — |
| 选择页面模板 | `references/page-patterns.md` | — |
| 生成 HTML 页面 | `references/design-tokens.md` + `references/pages/shared-tokens.md` | `references/page-patterns.md` |
| 生成/调试组件 | — | `references/components/<组件名>.md` |
| 像素级还原 | — | `references/pages/page-dsl.md` / `implementation.md` |

---

## 输出产物

### 文件结构

```
doc/{projectName}_{projectVersion}_UED/
├── index.html          ← 总入口
├── assets/styles.css   ← 全局样式（CSS 变量）
├── pages/*.html        ← 各页面 HTML Demo
└── README.md           ← UI/UE 设计说明文档（8章结构）
```

### README.md 章节结构（8章）

1. **页面清单**（含覆盖层列）
2. **导航结构**（侧边栏菜单树）
3. **页面导航关系**（Mermaid graph LR）
4. **组件树**（每页含覆盖层子树）
5. **交互规格汇总**（所有覆盖层一张总表）
6. **状态-操作规则**（从PRD状态矩阵映射，含隐藏按钮列）
7. **设计规范摘要**（Token 引用）
8. **文件清单**

> README.md 是下游 skill 的**主要消费入口**，HTML Demo 仅作为视觉辅助。

### 与下游skill衔接

| 下游 | README.md 输入 |
|------|---------------|
| lyspec-detail | 一→页面清单；四→组件树；五→交互规格 |
| lyspec-frontend | 一→页面清单；四→组件树；六→状态规则 |
| lyspec-test-cases | 一→页面清单；五→交互规格；六→状态测试 |

---

## 附录

### A. 用户交互检查点

- [ ] 上游文档已确认（PRD必需）
- [ ] 阶段一完成：页面清单和模板选择已确认
- [ ] 阶段二完成：组件树和布局方案已确认
- [ ] 阶段三完成：HTML Demo 已生成并确认

### B. 质量检查点

**视觉质量基线**：
- [ ] CSS 变量名与 `references/design-tokens.md` 模板完全一致
- [ ] 侧边栏含 Logo 图标 + 菜单图标，非纯文本
- [ ] 每页含 Topbar（面包屑+搜索+通知下拉面板+头像下拉菜单），通知和头像可点击展开
- [ ] 指标卡含图标背景圆圈
- [ ] styles.css 包含所有页面级组件类定义

**覆盖层完整性**：
- [ ] 所有 CRUD 的新增/编辑弹窗已生成（非注释标注）
- [ ] 所有删除有确认弹窗
- [ ] Modal/Drawer 可通过 JS 点击打开和关闭
- [ ] 表单字段与 PRD 交互动作表一致

**操作按钮完整性**：
- [ ] 表格操作列的每个链接/按钮都有 onclick 处理（无 `href="javascript:;"` 空链接）
- [ ] 每个操作按钮有对应的覆盖层（Modal/Drawer/Confirm）或页面跳转

**图表完整性**：
- [ ] 含图表的页面已引入 ECharts CDN（`<script src="...echarts.min.js">`）
- [ ] 所有图表区域使用 ECharts 渲染真实可视化，无空占位框
- [ ] 图表配色使用 design-tokens.md 定义的颜色值
- [ ] 图表数据与 PRD 展示要素清单一致（合理示例数据）

**非 CRUD 页面完整性**：
- [ ] 设置页每个 Tab 有独立表单内容，Tab 切换 JS 可用
- [ ] 分步表单步骤切换 JS 可用，每步有内容
- [ ] 树形联动页节点可点击高亮
- [ ] Switch 开关可点击切换
- [ ] 含导入功能的页面有 upload-area + 模板下载

**产物完整性**：
- [ ] README.md 8章结构完整
- [ ] 所有 HTML 可直接浏览器打开

### C. 目录结构

```
lyspec-ued/
├── SKILL.md                              ← 本文件（主skill，~430行）
└── references/
    ├── design-tokens.md                   ← 设计Token + CSS变量模板（Phase 3 加载）
    ├── page-patterns.md                   ← 页面模板 + 组件决策树 + JS模板（Phase 1/3 加载）
    ├── components/                        ← 19个组件文档（按需加载）
    │   ├── auto-complete.md ... upload.md
    └── pages/                             ← 页面级参考（按需加载）
        ├── shared-tokens.md               ← 精确布局Token
        ├── page-dsl.md                    ← 11张页面JSON DSL
        └── implementation.md              ← React实现代码
```
