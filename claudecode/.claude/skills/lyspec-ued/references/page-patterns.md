# 页面模板、组件决策树与 JS 交互模板

> 本文件从 SKILL.md 拆分，Phase 1 选模板 + Phase 2 选组件 + Phase 3 生成 HTML 时加载。

## 页面模板选择指引

| 页面功能 | 推荐模板 | 特征 |
|---------|---------|------|
| 数据列表 + CRUD操作 | 查询表格页 | 筛选区 + 操作栏 + 分页表格 |
| 数据卡片网格展示 | 卡片列表页 | 工具栏 + 多列卡片网格 |
| 单条数据详情展示 | 基础详情页 | 面包屑 + Descriptions + 内嵌表格 |
| 表单提交（1~2步） | 基础表单页 | 单步表单 |
| 表单提交（3+步骤） | 分步表单页 | Steps + 分步表单 + 导航 |
| 数据概览 + 图表 | 工作台 | 指标卡 + 图表 + 待办列表 |
| 多维度数据分析 | 多维数据页 | 指标卡 + 图表 + 表格 |
| KPI分析 + 排名 | 分析页 | KPI横幅 + 柱状图 + 排名列表 |
| 个人信息展示/编辑 | 用户信息页 | 用户横幅 + 双栏 + 卡片 |
| 系统配置/偏好设置 | 用户设置页 | 左Tab + 右表单（每个Tab独立内容） |
| 树形导航+列表 | 树形联动页 | 左树面板(240px) + 右表格/详情 |
| 操作成功/失败反馈 | 成功页 | 结果图标 + 标题 + 引导按钮 |

### 覆盖层模板（嵌入宿主页面）

| 交互场景 | 推荐模板 | 特征 |
|---------|---------|------|
| 简单新增/编辑（≤6个字段） | Modal 表单 | 居中 Modal(520px) + Form + 确认/取消 |
| 复杂新增/编辑（>6个字段） | Drawer 表单 | 右侧 Drawer(480px) + Form + 确认/取消 |
| 操作确认（删除/审批） | 确认弹窗 | 小 Modal(400px) + 警告图标 + 双按钮 |
| 快速预览 | Drawer 详情 | 右侧 Drawer + 键值对 + 关闭按钮 |

### 模板变化指引

| 可变元素 | 调整规则 |
|---------|---------|
| 表格列数 | >8列考虑横向滚动 |
| 筛选条件数 | 1~3个单行；4~6个两行（3列×2行）；>6个展开/收起 |
| 卡片数量 | 每行4列 |
| 指标卡数量 | 2~6个等宽，>6个分两行 |
| 图表类型 | 趋势→折线、对比→柱状、占比→饼图 |

## 页面模板必须结构清单

> 每种模板在生成 HTML Demo 时，**必须**包含下表中所有结构和 JS 交互。缺少任何一项视为不合格。

| 页面模板 | 必须包含的 HTML 结构 | 必须包含的 JS 交互 |
|---------|-------------------|-----------------|
| 查询表格页 | 筛选区(toolbar) + 操作栏 + 表格 + 分页 + 覆盖层 | Modal/Drawer 开关 + Switch(若有启用/停用) |
| 卡片列表页 | 工具栏 + 卡片网格(4列) + 卡片内操作按钮 | 卡片按钮 → 覆盖层(若有) |
| 基础详情页 | 面包屑 + 信息卡(desc-grid) + 关联表格 + 状态感知按钮 | 状态控制按钮显隐 + 覆盖层 |
| 分步表单页 | Steps 指示器 + 多个 step-content(.hidden切换) + 导航按钮 | **步骤切换 JS（必须）** |
| 工作台 | 指标卡行 + 多区域布局(ECharts图表+列表) | 指标卡点击 → Modal(若有) + **ECharts 图表渲染（必须）** |
| 多维数据页 | 指标卡 + ECharts 图表区 + 数据表格 | **ECharts 图表渲染（必须）** |
| 分析页 | KPI卡片行 + ECharts 图表区 + 排名列表 + 明细表格 | **ECharts 图表渲染（必须）** |
| **用户设置页** | **左Tab栏(data-tab) + 每个Tab独立表单面板(data-panel, .hidden切换) + 各面板独立"保存"按钮** | **Tab 切换 JS（必须）** |
| 用户信息页 | 头像区 + 双栏(信息+表单) | — |
| **树形联动页** | **左树面板(240px, 节点可点击高亮) + 右表格面板(flex:1)** | **树节点点击 → 右侧切换 JS（必须）** |
| 成功页 | 结果图标 + 描述 + 引导按钮 | — |

## Topbar 标准 HTML 模板（全局组件）

> 每个标准页面（登录页除外）的 Topbar 必须使用以下完整模板，禁止简化为无交互的纯文本。

```html
<div class="topbar">
  <div class="topbar-left">
    <div class="breadcrumb">
      <a href="monitor-dashboard.html">首页</a><span class="separator">/</span>
      <a href="{模块首页文件名}.html">{模块名}</a><span class="separator">/</span>
      <span class="current">{页面名}</span>
    </div>
  </div>
  <div class="topbar-right">
    <input type="text" class="topbar-search" placeholder="搜索...">
    <button class="topbar-icon-btn" onclick="toggleNotifyPanel(event)">🔔<span class="badge-dot"></span>
      <div class="topbar-dropdown topbar-notify-panel" id="notifyPanel">
        <div class="topbar-notify-header"><span>消息通知</span><a href="javascript:;" style="font-size:12px;color:var(--color-primary);">全部已读</a></div>
        <div class="topbar-notify-item unread"><span class="topbar-notify-dot"></span><div class="topbar-notify-content"><div class="topbar-notify-text">{示例通知1}</div><div class="topbar-notify-time">2分钟前</div></div></div>
        <div class="topbar-notify-item unread"><span class="topbar-notify-dot"></span><div class="topbar-notify-content"><div class="topbar-notify-text">{示例通知2}</div><div class="topbar-notify-time">15分钟前</div></div></div>
        <div class="topbar-notify-item"><span class="topbar-notify-dot read"></span><div class="topbar-notify-content"><div class="topbar-notify-text">{示例通知3}</div><div class="topbar-notify-time">1小时前</div></div></div>
        <div class="topbar-notify-footer"><a href="javascript:;">查看全部通知</a></div>
      </div>
    </button>
    <div class="topbar-avatar" onclick="toggleAvatarMenu(event)">张
      <div class="topbar-dropdown topbar-avatar-menu" id="avatarMenu">
        <div class="topbar-avatar-menu-item" onclick="location.href='profile.html'">👤 个人中心</div>
        <div class="topbar-avatar-menu-item">⚙️ 账户设置</div>
        <div class="topbar-avatar-menu-divider"></div>
        <div class="topbar-avatar-menu-item" onclick="location.href='login.html'">🚪 退出登录</div>
      </div>
    </div>
  </div>
</div>
```

> **面包屑链接规则**：
> - 「首页」固定链接到 `monitor-dashboard.html`（或项目定义的首页）
> - 「模块名」链接到该模块的第一个列表页（如 异常报警管理 → `alarm-list.html`）
> - **禁止使用 `href="#"` 占位**，必须填入实际页面文件名
> - 当前页面名用 `<span class="current">` 无链接

**Topbar JS**（每个页面的 `<script>` 中必须包含）：
```javascript
function toggleNotifyPanel(e){e.stopPropagation();document.getElementById('avatarMenu').classList.remove('open');document.getElementById('notifyPanel').classList.toggle('open');}
function toggleAvatarMenu(e){e.stopPropagation();document.getElementById('notifyPanel').classList.remove('open');document.getElementById('avatarMenu').classList.toggle('open');}
document.addEventListener('click',function(){document.querySelectorAll('.topbar-dropdown').forEach(function(d){d.classList.remove('open');});});
```

---

## 标准 JS 交互模板库

> 以下 JS 模板必须嵌入对应类型的页面，禁止省略。

### ① Tab 切换（Settings 页 / Tabs 页）
```javascript
document.querySelectorAll('[data-tab]').forEach(function(tab) {
  tab.addEventListener('click', function() {
    document.querySelectorAll('[data-tab]').forEach(function(t) {
      t.style.background = ''; t.style.color = 'var(--color-text-2)'; t.style.fontWeight = '400';
    });
    document.querySelectorAll('[data-panel]').forEach(function(p) { p.classList.add('hidden'); });
    this.style.background = 'var(--brand-primary-5)';
    this.style.color = 'var(--brand-primary-1)';
    this.style.fontWeight = '500';
    var panel = document.querySelector('[data-panel="' + this.dataset.tab + '"]');
    if (panel) panel.classList.remove('hidden');
  });
});
```

### ② 分步表单导航（Step Form）
```javascript
var currentStep = 1;
var totalSteps = 3;
function goStep(n) {
  if (n < 1 || n > totalSteps) return;
  document.querySelectorAll('[data-step]').forEach(function(s) { s.classList.add('hidden'); });
  var target = document.querySelector('[data-step="' + n + '"]');
  if (target) target.classList.remove('hidden');
  document.querySelectorAll('.step').forEach(function(s, i) {
    s.classList.remove('active', 'done');
    if (i + 1 < n) s.classList.add('done');
    if (i + 1 === n) s.classList.add('active');
  });
  currentStep = n;
}
```

### ③ Switch 行内开关（启用/停用）
```javascript
document.querySelectorAll('.switch').forEach(function(sw) {
  sw.addEventListener('click', function() { this.classList.toggle('on'); });
});
```

### ④ Multi-Select 下拉多选（表单内多选场景）

> 当表单中需要多选且要保持与单选 Select 下拉框一致的视觉风格时使用。
> 已选项以 Tag 形式显示在触发区，下拉面板内含 checkbox 列表。

**HTML 结构**：
```html
<div class="multi-select" id="msXxx">
  <div class="multi-select-trigger" onclick="toggleMultiSelect('msXxx')">
    <span class="ms-placeholder">请选择（可多选）</span>
  </div>
  <div class="multi-select-dropdown">
    <label class="multi-select-option"><input type="checkbox" value="选项A" onchange="updateMultiSelect('msXxx')"> 选项A</label>
    <label class="multi-select-option"><input type="checkbox" value="选项B" onchange="updateMultiSelect('msXxx')"> 选项B</label>
  </div>
</div>
```

**JS 交互**：
```javascript
function toggleMultiSelect(id) {
  document.getElementById(id).classList.toggle('open');
}
function updateMultiSelect(id) {
  var ms = document.getElementById(id);
  var trigger = ms.querySelector('.multi-select-trigger');
  var selected = [];
  ms.querySelectorAll('input[type="checkbox"]').forEach(function(c) {
    if (c.checked) selected.push(c.value);
  });
  if (selected.length === 0) {
    trigger.innerHTML = '<span class="ms-placeholder">请选择（可多选）</span>';
  } else {
    trigger.innerHTML = selected.map(function(v) {
      return '<span class="ms-tag">' + v + ' <span class="ms-tag-close" onclick="removeTag(event,\'' + id + '\',\'' + v + '\')">×</span></span>';
    }).join('');
  }
}
function removeTag(event, id, value) {
  event.stopPropagation();
  var ms = document.getElementById(id);
  ms.querySelectorAll('input[type="checkbox"]').forEach(function(c) {
    if (c.value === value) c.checked = false;
  });
  updateMultiSelect(id);
}
document.addEventListener('click', function(e) {
  document.querySelectorAll('.multi-select.open').forEach(function(ms) {
    if (!ms.contains(e.target)) ms.classList.remove('open');
  });
});
```

**styles.css 必须包含的类**：`.multi-select`, `.multi-select-trigger`, `.ms-tag`, `.ms-tag-close`, `.ms-placeholder`, `.multi-select-dropdown`, `.multi-select.open`, `.multi-select-option`

### ⑤ 树形节点选择（树形联动页）
```javascript
document.querySelectorAll('[data-tree-node]').forEach(function(node) {
  node.addEventListener('click', function() {
    document.querySelectorAll('[data-tree-node]').forEach(function(n) {
      n.style.background = ''; n.style.color = '';
    });
    this.style.background = 'var(--brand-primary-5)';
    this.style.color = 'var(--brand-primary-1)';
    var title = document.querySelector('.tree-panel-title');
    if (title) title.textContent = this.textContent.trim() + ' — 成员列表';
  });
});
```

## 非 CRUD 交互推导规则

> 当 PRD 中的功能不属于标准 CRUD 操作时，按以下规则推导交互形式。

| PRD 中的关键词 | 推导为的交互形式 | UED 输出要求 |
|-------------|--------------|------------|
| "配置""参数""设置" | Tab 切换 + 每 Tab 独立表单 | 每个配置分组一个 Tab，字段从 PRD「配置项清单表」提取 |
| "导入""批量上传" | Modal + Upload 区 + 模板下载 + 结果反馈 | 导入 Modal 含 upload-area + 下载模板 link |
| "导出""下载" | 按钮 + Toast 反馈 | btn-default "导出" → showToast |
| "预览""查看大图" | Modal 大图展示 | modal-form 含大图占位区 + 关闭按钮 |
| "启用/停用""开关" | Switch 组件 + 确认弹窗 | 行内 .switch + 切换前 confirm |
| "统计""分析""趋势" | 指标卡 + 图表 + 筛选工具栏 | 从 PRD「展示要素清单表」提取 |
| "大屏""监控""总览" | 多区域卡片 + 实时滚动 | 指标卡行 + 多卡片 grid + 滚动列表 |
| "查看""详情"（表格操作列） | Drawer 只读展示 或 Modal 展示 | 操作列的每个按钮**必须**有 onclick + 对应覆盖层，禁止生成无交互的空链接 |
| "编辑""修改"（非 CRUD 简单编辑） | Modal 表单（回填行数据） | 从表格行提取数据回填 Modal，保存后 Toast |

## 组件选择决策树

### 选择类
```
用户需要选择 →
  ├── 选项 ≤ 5 且互斥 → Radio
  ├── 选项 ≤ 5 且可多选（独立展示，如权限勾选） → Checkbox 列表
  ├── 选项可多选（表单内，需保持下拉风格一致） → Multi-Select 下拉多选
  ├── 选项 > 5 且单选 → Select
  ├── 选项有层级关系 → Cascader
  └── 允许自由输入 + 联想 → AutoComplete
```

### 输入类
```
用户需要输入 →
  ├── 单行文本 → Input
  ├── 多行文本 → Input.TextArea
  ├── 密码 → Input.Password
  ├── 带搜索图标 → Input.Search
  └── 文件/图片 → Upload
```

### 展示类
```
展示数据 →
  ├── 结构化多行数据 → Table
  ├── 卡片网格 → Grid + Card
  ├── 状态标签 → Tag（带颜色）
  ├── 数量提醒 → Badge
  └── 键值对详情 → Descriptions
```

### 操作类
```
用户需要操作 →
  ├── 主要操作 → Button[type=primary]
  ├── 次要操作 → Button[type=default]
  ├── 危险操作 → Button[type=primary, status=danger]
  ├── 轻量操作 → Button[type=text]
  ├── 信息浮层 → Popover
  └── 全局反馈 → Message
```

### 覆盖层类
```
需要用户操作后再继续 →
  ├── 信息量少（确认/删除） → Modal 确认弹窗（400px）
  ├── 表单（≤6字段） → Modal 表单（520px）
  ├── 表单（>6字段） → Drawer 表单（480px）
  ├── 查看详情不离开列表 → Drawer 详情（480px）
  └── 完整页面体验 → 页面跳转
```

### 布局类
```
页面布局 →
  ├── 整体框架 → Layout
  ├── 栅格排列 → Grid (Row/Col)
  ├── 内联等距 → Space
  ├── 内容分隔 → Divider
  └── 多视图切换 → Tabs
```

### 常见业务场景 → 组件组合

| 业务场景 | 推荐组件组合 | 页面模板 |
|---------|-------------|---------|
| CRUD列表管理 | Form + Input/Select + Button + Table + Tag + Message | 查询表格页 |
| 数据详情展示 | Breadcrumb + Descriptions + Table + Button | 基础详情页 |
| 新建/编辑表单 | Form + Input/Select/Radio/Checkbox/Upload + Button | 表单页 |
| 数据看板 | Grid + 指标卡 + ECharts图表 + Table | 工作台/多维数据页 |
| 系统配置 | Tabs + Form + Switch + Input + Button | 用户设置页 |

## 图表生成规则（ECharts CDN）

> **禁止**生成空的 chart-box 纯文字占位框。凡页面包含图表区域，必须使用 ECharts 渲染真实可视化图表。

### CDN 引入方式

在含图表的 HTML 页面 `<head>` 中添加：
```html
<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
```

### 图表容器 HTML

替代原有的 `.chart-box` 占位框，使用带 `id` 的 div：
```html
<div id="chartXxx" style="width:100%;height:300px;"></div>
```

### 图表初始化 JS 模板

在 `</body>` 前的 `<script>` 中初始化：
```javascript
var chartXxx = echarts.init(document.getElementById('chartXxx'));
chartXxx.setOption({ /* ECharts 配置 */ });
// 响应式
window.addEventListener('resize', function() { chartXxx.resize(); });
```

### 各图表类型的 ECharts 配置模板

#### 折线图（趋势类）
```javascript
{
  tooltip: { trigger: 'axis' },
  legend: { data: ['报警数', '处置数'] },
  grid: { left: 40, right: 20, top: 40, bottom: 30 },
  xAxis: { type: 'category', data: ['3/12','3/13','3/14','3/15','3/16','3/17','3/18'] },
  yAxis: { type: 'value' },
  series: [
    { name: '报警数', type: 'line', smooth: true, data: [15,11,18,9,14,8,12], itemStyle: { color: '#165DFF' } },
    { name: '处置数', type: 'line', smooth: true, data: [14,10,16,9,13,8,11], itemStyle: { color: '#00B42A' } }
  ]
}
```

#### 柱状图（对比类）
```javascript
{
  tooltip: { trigger: 'axis' },
  grid: { left: 80, right: 20, top: 20, bottom: 30 },
  xAxis: { type: 'category', data: ['主变区域','汽轮机房','输煤皮带','配电室','锅炉房'] },
  yAxis: { type: 'value' },
  series: [{
    type: 'bar', barWidth: 24, data: [42,35,28,18,15],
    itemStyle: { color: '#165DFF', borderRadius: [4,4,0,0] }
  }]
}
```

#### 饼图（占比类）
```javascript
{
  tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
  legend: { bottom: 0 },
  series: [{
    type: 'pie', radius: ['40%','70%'], center: ['50%','45%'],
    data: [
      { value: 23, name: '紧急', itemStyle: { color: '#F53F3F' } },
      { value: 41, name: '重要', itemStyle: { color: '#FF7D00' } },
      { value: 36, name: '一般', itemStyle: { color: '#165DFF' } }
    ],
    label: { formatter: '{b}\n{d}%' }
  }]
}
```

### 配色规则

ECharts 图表配色须使用 `references/design-tokens.md` 中的颜色值：
- 主系列色：`#165DFF`（color-primary）
- 辅助系列色依次：`#00B42A`、`#FF7D00`、`#F53F3F`、`#43CC8B`、`#6961FF`、`#FF992F`
- 网格线：`#F2F3F5`（border-1）
- 轴标签文字：`#4E5969`（color-text-2）、字号 12px

### 数据来源

- 从 PRD「展示要素清单表」提取 X 轴/Y 轴含义和数据内容
- 使用**合理的示例数据**填充（数量级与 PRD 描述一致）
- 示例数据须看起来真实自然（有波动、非均匀分布）
