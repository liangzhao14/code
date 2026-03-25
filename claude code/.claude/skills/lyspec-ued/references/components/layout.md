# lingyang-layout · 页面布局组件 Skill

**子组件**：`Layout` · `Layout.Header` · `Layout.Sider` · `Layout.Content` · `Layout.Footer`

---

## 何时读取子文档

| 需求 | 读取文件 |
|---|---|
| 需要完整 TypeScript 类型定义 / 所有 Props 枚举 | `references/props.md` |
| 需要完整代码示例（7 种布局模式） | `references/examples.md` |
| 需要 Sider 折叠 / 响应式 / 拖拽的详细说明 | `references/sider-advanced.md` |

---

## 布局模式速查

```
需要搭页面框架？先选模式：

① 顶部导航       Layout > Header + Content + Footer
   适合：内容站、文档、营销页

② 侧边导航 ★最常用  Layout > Sider + Layout(Header + Content + Footer)
   适合：后台管理系统、数据平台

③ 顶部+侧边混合   Layout > Header + Layout(Sider + Content)
   适合：多产品线平台（Header 放一级导航，Sider 放二级）

④ 双侧边          Layout > Sider(一级) + Layout(Sider(二级) + Content)
   适合：超复杂后台，功能层级深
```

---

## 核心约束（生成代码必须遵守）

1. `Header / Sider / Content / Footer` 必须放在 `Layout` 内，不可独立使用
2. `Layout` 检测到直接子节点含 `Sider` 时，**自动**切为水平排列，无需手动设 `hasSider`
3. `Content` 默认 `flex: auto`，自动撑满剩余空间；`Header / Footer` 高度固定
4. **折叠三选一**：受控（`collapsed` + `onCollapse`）/ 非受控（`defaultCollapsed`）/ 断点自动（`breakpoint`）
5. `collapsedWidth={0}` = 零宽模式，触发器渲染在**外侧**边缘
6. `trigger={null}` 隐藏触发器后，**必须**配合外部受控按钮使用
7. `resizeBoxProps` 开启拖拽后，`width` 仅为初始值，拖拽后不受控

---

## Props 快速参考

### Layout
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `hasSider` | `boolean` | `false` | 是否含侧边栏（一般自动检测，SSR 时手动设）|

### Layout.Header / Layout.Content / Layout.Footer
> 仅支持 `style` / `className` / `children`，无业务 props。

### Layout.Sider ← 核心复杂组件
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `collapsed` | `boolean` | — | 受控折叠状态 |
| `defaultCollapsed` | `boolean` | `false` | 非受控默认折叠 |
| `collapsible` | `boolean` | `false` | 显示默认折叠触发器 |
| `width` | `number \| string` | `200` | 展开宽度（px 或 CSS 字符串）|
| `collapsedWidth` | `number` | `48` | 折叠后宽度；`0` = 零宽隐藏 |
| `breakpoint` | `'xs'\|'sm'\|'md'\|'lg'\|'xl'\|'xxl'` | — | 响应式自动折叠断点 |
| `trigger` | `ReactNode \| null` | — | 自定义触发器；`null` 隐藏 |
| `reverseArrow` | `boolean` | `false` | 翻转箭头（右侧侧边栏用）|
| `theme` | `'dark'\|'light'` | `'dark'` | 主题，与内部 Menu 保持一致 |
| `resizeBoxProps` | `Partial<ResizeBoxProps>` | — | **lingyang 专有**：可拖拽宽度 |
| `onCollapse` | `(collapsed, type) => void` | — | 折叠变化回调 |
| `onBreakpoint` | `(broken) => void` | — | 断点触发回调 |

---

## 最小可用示例

### 侧边导航（最常用）
```jsx
import { Layout, Menu } from 'lingyang';
const { Header, Sider, Content, Footer } = Layout;

export default function AdminLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible>
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
          <Menu.Item key="1">Dashboard</Menu.Item>
          <Menu.Item key="2">用户管理</Menu.Item>
        </Menu>
      </Sider>
      <Layout>
        <Header style={{ background: '#fff', padding: '0 16px' }}>页面标题</Header>
        <Content style={{ margin: 16 }}>
          <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>内容区</div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>lingyang ©2024</Footer>
      </Layout>
    </Layout>
  );
}
```

### 受控折叠 + 自定义按钮
```jsx
const [collapsed, setCollapsed] = useState(false);

<Layout style={{ minHeight: '100vh' }}>
  <Sider collapsed={collapsed} trigger={null}>
    <Menu theme="dark" mode="inline">
      <Menu.Item key="1">菜单</Menu.Item>
    </Menu>
  </Sider>
  <Layout>
    <Header style={{ background: '#fff', padding: '0 16px', display: 'flex', alignItems: 'center' }}>
      <Button
        type="text"
        icon={collapsed ? <IconMenuUnfold /> : <IconMenuFold />}
        onClick={() => setCollapsed(c => !c)}
        style={{ fontSize: 18 }}
      />
    </Header>
    <Content style={{ padding: 24 }}>主内容</Content>
  </Layout>
</Layout>
```

---

## CSS 类名速查

| 场景 | 类名 |
|---|---|
| 布局容器 | `.lingyang-layout` |
| 含侧边栏 | `.lingyang-layout-has-sider` |
| 顶部栏 | `.lingyang-layout-header` |
| 侧边栏 | `.lingyang-layout-sider` |
| 侧边栏折叠中 | `.lingyang-layout-sider-collapsed` |
| 侧边栏浅色 | `.lingyang-layout-sider-light` |
| 侧边栏零宽 | `.lingyang-layout-sider-zero-width` |
| 内容区 | `.lingyang-layout-content` |
| 底部栏 | `.lingyang-layout-footer` |
| 折叠触发器 | `.lingyang-layout-sider-trigger` |

---

## 可访问性

- `Layout` → `<section>`，`Header` → `<header>`，`Content` → `<main>`，`Footer` → `<footer>`，`Sider` → `<aside>`
- 折叠触发器按钮需有 `aria-label`（如「折叠侧边栏」/ 「展开侧边栏」）
- 自定义 `trigger={null}` 时，外部按钮须同样标注 `aria-label` 和 `aria-expanded`
-e 

---

## 完整代码示例

# lingyang-layout · 完整代码示例库

## 目录
1. [顶部导航布局](#1-顶部导航布局)
2. [标准侧边导航布局](#2-标准侧边导航布局最常用)
3. [受控折叠自定义触发器](#3-受控折叠--自定义触发器)
4. [响应式断点自动折叠](#4-响应式断点自动折叠)
5. [可拖拽侧边栏](#5-可拖拽侧边栏lingyang-专有)
6. [顶部侧边混合布局](#6-顶部侧边混合布局)
7. [右侧侧边栏](#7-右侧侧边栏reverseArrow)
8. [双侧边布局](#8-双侧边布局)
9. [企业级完整后台模板](#9-企业级完整后台模板)

---

## 1. 顶部导航布局

```jsx
import { Layout, Menu } from 'lingyang';
const { Header, Content, Footer } = Layout;

export default function TopNavLayout() {
  return (
    <Layout>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ color: '#fff', fontSize: 18, marginRight: 40 }}>lingyang Admin</div>
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['home']}
          style={{ flex: 1, minWidth: 0 }}
        >
          <Menu.Item key="home">首页</Menu.Item>
          <Menu.Item key="product">产品</Menu.Item>
          <Menu.Item key="about">关于</Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: '24px 50px', minHeight: 280 }}>
        <div style={{ background: '#fff', padding: 24 }}>页面内容</div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        lingyang Design ©2024 Created by lingyang Team
      </Footer>
    </Layout>
  );
}
```

---

## 2. 标准侧边导航布局（最常用）

```jsx
import { Layout, Menu } from 'lingyang';
import {
  IconDashboard, IconUser, IconSettings,
  IconFile, IconBarChart
} from 'lingyang/icon';
const { Header, Sider, Content, Footer } = Layout;

export default function SidebarLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible>
        {/* Logo 区域 */}
        <div style={{
          height: 32, margin: 16,
          background: 'rgba(255,255,255,0.2)',
          borderRadius: 4
        }} />
        <Menu theme="dark" defaultSelectedKeys={['dashboard']} mode="inline">
          <Menu.Item key="dashboard" icon={<IconDashboard />}>
            Dashboard
          </Menu.Item>
          <Menu.SubMenu key="users" icon={<IconUser />} title="用户管理">
            <Menu.Item key="user-list">用户列表</Menu.Item>
            <Menu.Item key="user-role">角色权限</Menu.Item>
          </Menu.SubMenu>
          <Menu.Item key="report" icon={<IconBarChart />}>数据报表</Menu.Item>
          <Menu.Item key="docs" icon={<IconFile />}>文档中心</Menu.Item>
          <Menu.Item key="settings" icon={<IconSettings />}>系统设置</Menu.Item>
        </Menu>
      </Sider>

      <Layout>
        <Header style={{ background: '#fff', padding: '0 24px', display: 'flex', alignItems: 'center' }}>
          <span style={{ fontSize: 16, fontWeight: 600 }}>Dashboard</span>
        </Header>
        <Content style={{ margin: 16 }}>
          <div style={{ padding: 24, background: '#fff', minHeight: 360, borderRadius: 4 }}>
            主内容区域
          </div>
        </Content>
        <Footer style={{ textAlign: 'center', color: '#666' }}>
          lingyang Admin ©2024
        </Footer>
      </Layout>
    </Layout>
  );
}
```

---

## 3. 受控折叠 + 自定义触发器

```jsx
import { useState } from 'react';
import { Layout, Menu, Button } from 'lingyang';
import { IconMenuFold, IconMenuUnfold } from 'lingyang/icon';
const { Header, Sider, Content } = Layout;

export default function ControlledSider() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* trigger={null} 隐藏默认触发器，由外部按钮控制 */}
      <Sider collapsed={collapsed} trigger={null} collapsedWidth={48}>
        <div style={{ height: 32, margin: 16, background: 'rgba(255,255,255,0.2)' }} />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
          <Menu.Item key="1">菜单项 1</Menu.Item>
          <Menu.Item key="2">菜单项 2</Menu.Item>
        </Menu>
      </Sider>

      <Layout>
        <Header style={{
          background: '#fff',
          padding: '0 16px',
          display: 'flex',
          alignItems: 'center',
          borderBottom: '1px solid #f0f0f0'
        }}>
          {/* 自定义折叠按钮 */}
          <Button
            type="text"
            aria-label={collapsed ? '展开侧边栏' : '折叠侧边栏'}
            aria-expanded={!collapsed}
            icon={collapsed ? <IconMenuUnfold /> : <IconMenuFold />}
            onClick={() => setCollapsed(c => !c)}
            style={{ fontSize: 18, marginRight: 16 }}
          />
          <span>页面标题</span>
        </Header>
        <Content style={{ padding: 24 }}>
          <div style={{ background: '#fff', padding: 24, borderRadius: 4 }}>
            {collapsed ? '侧边栏已折叠' : '侧边栏已展开'}
          </div>
        </Content>
      </Layout>
    </Layout>
  );
}
```

---

## 4. 响应式断点自动折叠

```jsx
import { useState } from 'react';
import { Layout, Menu } from 'lingyang';
const { Header, Sider, Content } = Layout;

export default function ResponsiveSider() {
  const [collapsed, setCollapsed] = useState(false);
  const [broken, setBroken] = useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        breakpoint="lg"        // 窗口 < 1200px 时自动折叠
        collapsedWidth={0}     // 折叠后完全隐藏（零宽模式）
        collapsed={collapsed}
        onBreakpoint={(isBroken) => {
          setBroken(isBroken);
          console.log('断点状态:', isBroken);
        }}
        onCollapse={(isCollapsed, type) => {
          setCollapsed(isCollapsed);
          console.log('折叠来源:', type); // 'responsive' or 'clickTrigger'
        }}
      >
        <Menu theme="dark" mode="inline">
          <Menu.Item key="1">导航项 1</Menu.Item>
          <Menu.Item key="2">导航项 2</Menu.Item>
        </Menu>
      </Sider>

      <Layout>
        <Header style={{ background: '#fff', padding: '0 16px' }}>
          {broken ? '移动端视图' : '桌面端视图'}
        </Header>
        <Content style={{ padding: 24 }}>
          调整窗口宽度至 1200px 以下，侧边栏自动折叠。
        </Content>
      </Layout>
    </Layout>
  );
}
```

---

## 5. 可拖拽侧边栏（lingyang 专有）

```jsx
import { Layout, Menu } from 'lingyang';
const { Header, Sider, Content } = Layout;

export default function ResizableSider() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        width={200}
        // 设置 resizeBoxProps 后，width 仅为初始值
        // 用户可通过拖拽右侧边缘调整宽度
        resizeBoxProps={{
          directions: ['right'],         // 左侧边栏：允许向右拖拽
          style: {
            minWidth: 120,               // 最小拖拽宽度
            maxWidth: 480,               // 最大拖拽宽度
          }
        }}
      >
        <Menu theme="dark" mode="inline" style={{ height: '100%' }}>
          <Menu.Item key="1">可拖拽侧边栏</Menu.Item>
          <Menu.Item key="2">拖动右侧边缘调整宽度</Menu.Item>
        </Menu>
      </Sider>

      <Layout>
        <Content style={{ padding: 24 }}>
          <div style={{ background: '#fff', padding: 24, borderRadius: 4 }}>
            拖动左侧边栏的右边缘即可调整宽度（120px ~ 480px）
          </div>
        </Content>
      </Layout>
    </Layout>
  );
}
```

---

## 6. 顶部侧边混合布局

```jsx
import { Layout, Menu } from 'lingyang';
const { Header, Sider, Content } = Layout;

export default function HybridLayout() {
  return (
    <Layout>
      {/* 全局 Header：Logo + 一级导航 */}
      <Header style={{ display: 'flex', alignItems: 'center', padding: '0 24px' }}>
        <div style={{ color: '#fff', fontSize: 18, fontWeight: 600, marginRight: 40, flexShrink: 0 }}>
          lingyang Admin
        </div>
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['platform']}
          style={{ flex: 1, minWidth: 0 }}
        >
          <Menu.Item key="platform">数据平台</Menu.Item>
          <Menu.Item key="ops">运维中心</Menu.Item>
          <Menu.Item key="market">营销工具</Menu.Item>
        </Menu>
      </Header>

      {/* 内容区：Sider（当前模块二级导航）+ Content */}
      <Layout>
        <Sider width={200} theme="light">
          <Menu
            mode="inline"
            defaultSelectedKeys={['overview']}
            defaultOpenKeys={['data']}
            style={{ height: '100%', borderRight: 0 }}
          >
            <Menu.SubMenu key="data" title="数据概览">
              <Menu.Item key="overview">总览</Menu.Item>
              <Menu.Item key="realtime">实时数据</Menu.Item>
            </Menu.SubMenu>
            <Menu.SubMenu key="report" title="报表中心">
              <Menu.Item key="daily">日报</Menu.Item>
              <Menu.Item key="weekly">周报</Menu.Item>
            </Menu.SubMenu>
          </Menu>
        </Sider>

        <Layout style={{ padding: '16px 24px 24px' }}>
          <Content style={{ background: '#fff', padding: 24, borderRadius: 4, minHeight: 280 }}>
            模块内容区域
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
}
```

---

## 7. 右侧侧边栏（reverseArrow）

```jsx
import { Layout } from 'lingyang';
const { Header, Sider, Content } = Layout;

export default function RightSiderLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* 主内容区在左 */}
      <Layout>
        <Header style={{ background: '#001529', color: '#fff', padding: '0 24px' }}>
          Header
        </Header>
        <Content style={{ padding: 24 }}>
          <div style={{ background: '#fff', padding: 24, borderRadius: 4, minHeight: 360 }}>
            主内容区域
          </div>
        </Content>
      </Layout>

      {/* 右侧边栏：reverseArrow 翻转箭头方向 */}
      <Sider
        collapsible
        reverseArrow          // 右侧边栏必须设置，使箭头语义正确
        theme="light"
        width={240}
        style={{ borderLeft: '1px solid #f0f0f0' }}
      >
        <div style={{ padding: 16 }}>
          <h4 style={{ marginBottom: 12 }}>属性面板</h4>
          <p style={{ color: '#666' }}>右侧辅助内容区域</p>
        </div>
      </Sider>
    </Layout>
  );
}
```

---

## 8. 双侧边布局

```jsx
import { Layout, Menu } from 'lingyang';
const { Sider, Content } = Layout;

export default function DoubleSiderLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* 一级导航：图标模式，宽度固定 */}
      <Sider width={64} collapsedWidth={64} theme="dark">
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['platform']}>
          <Menu.Item key="platform" title="数据平台">📊</Menu.Item>
          <Menu.Item key="ops" title="运维中心">🔧</Menu.Item>
          <Menu.Item key="market" title="营销">📢</Menu.Item>
        </Menu>
      </Sider>

      {/* 二级导航 + 内容 */}
      <Layout>
        <Sider width={180} theme="light">
          <Menu mode="inline" style={{ height: '100%', borderRight: 0 }}>
            <Menu.SubMenu key="sub1" title="数据概览">
              <Menu.Item key="1">总览</Menu.Item>
              <Menu.Item key="2">实时</Menu.Item>
            </Menu.SubMenu>
          </Menu>
        </Sider>
        <Content style={{ padding: 24 }}>
          <div style={{ background: '#fff', padding: 24, borderRadius: 4, minHeight: 360 }}>
            内容区域
          </div>
        </Content>
      </Layout>
    </Layout>
  );
}
```

---

## 9. 企业级完整后台模板

```jsx
import { useState } from 'react';
import {
  Layout, Menu, Breadcrumb, Avatar,
  Button, Dropdown, Space, Tag
} from 'lingyang';
import {
  IconDashboard, IconUser, IconSettings,
  IconMenuFold, IconMenuUnfold, IconNotification, IconDown
} from 'lingyang/icon';

const { Header, Sider, Content, Footer } = Layout;

// 菜单数据
const menuItems = [
  { key: 'dashboard', icon: <IconDashboard />, label: 'Dashboard' },
  {
    key: 'users', icon: <IconUser />, label: '用户管理',
    children: [
      { key: 'user-list', label: '用户列表' },
      { key: 'user-role', label: '角色权限' },
    ]
  },
  { key: 'settings', icon: <IconSettings />, label: '系统设置' },
];

export default function EnterpriseAdmin() {
  const [collapsed, setCollapsed] = useState(false);
  const [selectedKey, setSelectedKey] = useState('dashboard');

  return (
    <Layout style={{ minHeight: '100vh' }}>

      {/* ── 侧边栏 ── */}
      <Sider
        collapsed={collapsed}
        trigger={null}          // 使用自定义触发按钮
        collapsible
        breakpoint="lg"
        onBreakpoint={(broken) => broken && setCollapsed(true)}
        style={{ boxShadow: '2px 0 8px rgba(0,0,0,0.15)' }}
      >
        {/* Logo */}
        <div style={{
          height: 64, display: 'flex', alignItems: 'center',
          justifyContent: collapsed ? 'center' : 'flex-start',
          padding: collapsed ? 0 : '0 20px',
          borderBottom: '1px solid rgba(255,255,255,0.1)'
        }}>
          <span style={{ color: '#13AE68', fontSize: 20 }}>🦌</span>
          {!collapsed && (
            <span style={{ color: '#fff', fontWeight: 700, fontSize: 16, marginLeft: 10 }}>
              羚羊 Admin
            </span>
          )}
        </div>

        {/* 主导航 */}
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[selectedKey]}
          onSelect={({ key }) => setSelectedKey(key)}
          style={{ borderRight: 0, paddingTop: 8 }}
        >
          {menuItems.map(item =>
            item.children ? (
              <Menu.SubMenu key={item.key} icon={item.icon} title={item.label}>
                {item.children.map(child => (
                  <Menu.Item key={child.key}>{child.label}</Menu.Item>
                ))}
              </Menu.SubMenu>
            ) : (
              <Menu.Item key={item.key} icon={item.icon}>{item.label}</Menu.Item>
            )
          )}
        </Menu>
      </Sider>

      {/* ── 右侧主体 ── */}
      <Layout>

        {/* 顶部操作栏 */}
        <Header style={{
          background: '#fff',
          padding: '0 16px 0 0',
          display: 'flex',
          alignItems: 'center',
          borderBottom: '1px solid #f0f0f0',
          boxShadow: '0 1px 4px rgba(0,0,0,0.08)'
        }}>
          {/* 折叠按钮 */}
          <Button
            type="text"
            aria-label={collapsed ? '展开侧边栏' : '折叠侧边栏'}
            icon={collapsed ? <IconMenuUnfold /> : <IconMenuFold />}
            onClick={() => setCollapsed(c => !c)}
            style={{ fontSize: 18, width: 64, height: 64 }}
          />

          {/* 面包屑 */}
          <Breadcrumb style={{ flex: 1 }}>
            <Breadcrumb.Item>首页</Breadcrumb.Item>
            <Breadcrumb.Item>用户管理</Breadcrumb.Item>
            <Breadcrumb.Item>用户列表</Breadcrumb.Item>
          </Breadcrumb>

          {/* 右侧工具栏 */}
          <Space size={8} style={{ marginRight: 16 }}>
            <Tag color="green">在线</Tag>
            <Button type="text" icon={<IconNotification />} />
            <Dropdown
              trigger="click"
              droplist={
                <Menu>
                  <Menu.Item key="profile">个人设置</Menu.Item>
                  <Menu.Item key="logout">退出登录</Menu.Item>
                </Menu>
              }
            >
              <Button type="text">
                <Space>
                  <Avatar size={28} style={{ background: '#13AE68' }}>张</Avatar>
                  <span>张经理</span>
                  <IconDown />
                </Space>
              </Button>
            </Dropdown>
          </Space>
        </Header>

        {/* 内容区 */}
        <Content style={{ margin: 16 }}>
          <div style={{ padding: 24, background: '#fff', borderRadius: 4, minHeight: 360 }}>
            <h2 style={{ marginBottom: 16 }}>用户列表</h2>
            <p style={{ color: '#666' }}>页面主体内容区域</p>
          </div>
        </Content>

        {/* 底部 */}
        <Footer style={{ textAlign: 'center', color: '#999', fontSize: 12 }}>
          lingyang Admin v2.0 ©2024 · 粤ICP备XXXXXXXX号
        </Footer>

      </Layout>
    </Layout>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-layout · 完整 Props 类型定义

## 目录
- [公共类型](#公共类型)
- [LayoutProps](#layoutprops)
- [HeaderProps](#headerprops)
- [SiderProps](#siderprops)  ← 最复杂，重点看这里
- [ContentProps](#contentprops)
- [FooterProps](#footerprops)
- [CSS 类名完整表](#css-类名完整表)

---

## 公共类型

```typescript
type BreakpointType = 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl';
// 断点宽度对照：
// xs  < 576px   手机竖屏
// sm  < 768px   手机横屏
// md  < 992px   平板
// lg  < 1200px  小桌面
// xl  < 1600px  标准桌面
// xxl >= 1600px 大屏

type CollapseType = 'clickTrigger' | 'responsive';
// clickTrigger: 用户点击折叠按钮触发
// responsive:   响应式断点自动触发
```

---

## LayoutProps

```typescript
interface LayoutProps extends HTMLAttributes<HTMLElement> {
  /**
   * 表示子元素中有 Sider，一般不需要指定。
   * 可在服务端渲染时避免样式闪烁（layout 方向在服务端无法自动检测）。
   * @default false
   */
  hasSider?: boolean;

  style?: CSSProperties;
  className?: string;
  children?: ReactNode;
}
```

---

## HeaderProps

```typescript
interface HeaderProps extends HTMLAttributes<HTMLElement> {
  /**
   * Header 无业务专有 props，仅支持 HTML 原生属性 + style/className/children。
   * 默认样式：height: 64px; padding: 0 50px; background: #001529; line-height: 64px;
   */
  style?: CSSProperties;
  className?: string;
  children?: ReactNode;
}
```

---

## SiderProps

```typescript
interface SiderProps extends HTMLAttributes<HTMLElement> {
  /**
   * 当前折叠状态（受控属性）。
   * 设置后组件完全受控，需配合 onCollapse 回调同步外部状态。
   * 设置后 defaultCollapsed 失效。
   */
  collapsed?: boolean;

  /**
   * 默认折叠状态（非受控属性）。
   * 仅首次渲染生效，之后由内部 state 管理。
   * @default false
   */
  defaultCollapsed?: boolean;

  /**
   * 是否可折叠。
   * true 时在侧边栏底部渲染默认折叠触发器（箭头按钮）。
   * @default false
   */
  collapsible?: boolean;

  /**
   * 侧边栏展开宽度。
   * 数字类型单位为 px；字符串可传 CSS 合法值如 '20%'。
   * 设置 resizeBoxProps 时，此值为拖拽的初始宽度。
   * @default 200
   */
  width?: number | string;

  /**
   * 折叠后侧边栏宽度（单位 px）。
   * 设为 0 时进入「零宽模式」：侧边栏完全隐藏，
   * 触发器从侧边栏内部移到外侧边缘（.lingyang-layout-sider-zero-width）。
   * @default 48
   */
  collapsedWidth?: number;

  /**
   * 响应式折叠断点。
   * 窗口宽度低于该断点时，侧边栏自动折叠，同时触发：
   * - onBreakpoint(true)
   * - onCollapse(true, 'responsive')
   * 窗口宽度恢复时，自动展开并触发相应回调。
   */
  breakpoint?: BreakpointType;

  /**
   * 自定义折叠触发器。
   * - 传入 ReactNode：替换默认箭头图标
   * - 传入 null：完全隐藏触发器（此时须用外部按钮受控折叠）
   */
  trigger?: ReactNode | null;

  /**
   * 是否翻转折叠触发器箭头方向。
   * 当侧边栏放置在页面右侧时，需设为 true 使箭头方向语义正确。
   * @default false
   */
  reverseArrow?: boolean;

  /**
   * 侧边栏主题色。
   * 'dark': 深色背景（#001529）— 与 <Menu theme="dark"> 配套
   * 'light': 浅色背景（#fff）— 与 <Menu theme="light"> 配套
   * @default 'dark'
   */
  theme?: 'light' | 'dark';

  /**
   * 【lingyang 专有】可拖拽调整宽度配置，透传给内部 ResizeBox 组件。
   * 设置后侧边栏边缘出现拖拽手柄，用户可自由调整宽度。
   * 常用配置：
   * - directions: ['right']  ← 左侧边栏，向右拖拽
   * - directions: ['left']   ← 右侧边栏，向左拖拽
   * - style.minWidth / style.maxWidth 限制拖拽范围
   */
  resizeBoxProps?: Partial<ResizeBoxProps>;

  /**
   * 折叠/展开状态变化时的回调。
   * @param collapsed 变化后的折叠状态
   * @param type      触发来源
   *   'clickTrigger' - 用户点击折叠按钮
   *   'responsive'   - 响应式断点触发
   */
  onCollapse?: (collapsed: boolean, type: CollapseType) => void;

  /**
   * 触发响应式断点时的回调（比 onCollapse 更细粒度）。
   * @param broken true = 当前宽度已低于断点（即将/已折叠）
   */
  onBreakpoint?: (broken: boolean) => void;

  style?: CSSProperties;
  className?: string;

  /**
   * 侧边栏内容。
   * 通常为 <Menu mode="inline" theme="dark"> 导航菜单。
   */
  children?: ReactNode;
}
```

---

## ContentProps

```typescript
interface ContentProps extends HTMLAttributes<HTMLElement> {
  /**
   * Content 无业务专有 props。
   * 渲染为 <main>，flex: auto 自动填充 Layout 剩余空间。
   */
  style?: CSSProperties;
  className?: string;
  children?: ReactNode;
}
```

---

## FooterProps

```typescript
interface FooterProps extends HTMLAttributes<HTMLElement> {
  /**
   * Footer 无业务专有 props。
   * 默认样式：padding: 24px 50px; background: #f0f2f5; text-align: center;
   */
  style?: CSSProperties;
  className?: string;
  children?: ReactNode;
}
```

---

## CSS 类名完整表

| 状态 / 元素 | CSS 类名 |
|---|---|
| 布局容器 | `.lingyang-layout` |
| 含侧边栏 | `.lingyang-layout.lingyang-layout-has-sider` |
| 顶部栏 | `.lingyang-layout-header` |
| 侧边栏 | `.lingyang-layout-sider` |
| 侧边栏折叠中 | `.lingyang-layout-sider.lingyang-layout-sider-collapsed` |
| 侧边栏浅色主题 | `.lingyang-layout-sider.lingyang-layout-sider-light` |
| 侧边栏零宽模式 | `.lingyang-layout-sider.lingyang-layout-sider-zero-width` |
| 折叠触发器 | `.lingyang-layout-sider-trigger` |
| 内容区 | `.lingyang-layout-content` |
| 底部栏 | `.lingyang-layout-footer` |
-e 

---

## Sider 折叠 / 响应式 / 拖拽详细说明

# lingyang-layout · Sider 高级特性详解

## 目录
1. [折叠三种模式对比](#1-折叠三种模式对比)
2. [collapsedWidth 零宽模式](#2-collapsedwidth-零宽模式)
3. [响应式断点完整说明](#3-响应式断点完整说明)
4. [resizeBoxProps 可拖拽配置](#4-resizeboxprops-可拖拽配置lingyang-专有)
5. [常见问题与陷阱](#5-常见问题与陷阱)

---

## 1. 折叠三种模式对比

| 模式 | 适用场景 | 关键 Props | 状态由谁管理 |
|---|---|---|---|
| **非受控**（最简单）| 无需外部感知折叠状态 | `collapsible` / `defaultCollapsed` | 组件内部 |
| **受控**（最灵活）| 需要外部按钮、面包屑联动等 | `collapsed` + `onCollapse` | 父组件 state |
| **响应式自动**（自适应）| 移动端友好、不需手动干预 | `breakpoint` + `collapsedWidth` | 自动 + 可混合受控 |

### 非受控模式
```jsx
// 最简写法，组件内部管理折叠状态
<Sider collapsible defaultCollapsed={false}>
  <Menu theme="dark" mode="inline">...</Menu>
</Sider>
```

### 受控模式
```jsx
const [collapsed, setCollapsed] = useState(false);

<Sider
  collapsed={collapsed}
  onCollapse={(val, type) => {
    console.log(`触发方式: ${type}`); // 'clickTrigger' | 'responsive'
    setCollapsed(val);
  }}
  collapsible
>
  <Menu theme="dark" mode="inline">...</Menu>
</Sider>
```

### 响应式 + 受控混合
```jsx
const [collapsed, setCollapsed] = useState(false);

<Sider
  collapsed={collapsed}
  breakpoint="md"          // < 992px 自动折叠
  collapsible              // 同时保留手动触发器
  onCollapse={setCollapsed}
>
  <Menu theme="dark" mode="inline">...</Menu>
</Sider>
```

---

## 2. collapsedWidth 零宽模式

`collapsedWidth={0}` 时侧边栏完全隐藏，行为与默认 `48` 有显著区别：

| 对比项 | collapsedWidth=48（默认）| collapsedWidth=0（零宽）|
|---|---|---|
| 折叠后外观 | 显示图标列 | 完全消失 |
| 触发器位置 | 侧边栏内部底部 | 外侧悬浮边缘 |
| CSS 状态类 | `.sider-collapsed` | `.sider-collapsed.sider-zero-width` |
| 适用场景 | 桌面端，保留导航提示 | 移动端，最大化内容区 |

```jsx
// 零宽模式示例：折叠后侧边栏完全隐藏
<Sider
  collapsedWidth={0}
  collapsible
  onCollapse={(collapsed) => console.log('零宽切换:', collapsed)}
>
  <Menu theme="dark" mode="inline">...</Menu>
</Sider>
```

**注意**：零宽模式下悬浮的触发器会叠在内容区上方，需通过 z-index 或绝对定位处理遮挡问题：
```css
.lingyang-layout-sider-zero-width-trigger {
  z-index: 1;
  top: 64px; /* 与 Header 高度对齐 */
}
```

---

## 3. 响应式断点完整说明

### 断点宽度对照表

| 断点值 | 触发折叠的窗口宽度阈值 | 典型设备 |
|---|---|---|
| `xs` | < 576px | 手机竖屏 |
| `sm` | < 768px | 手机横屏 |
| `md` | < 992px | 平板 |
| `lg` | < 1200px | 小桌面 ← 后台系统最常用 |
| `xl` | < 1600px | 标准桌面 |
| `xxl` | ≥ 1600px | 大屏（基本不用于折叠） |

### 回调触发顺序
当窗口宽度**低于断点**时，依次触发：
1. `onBreakpoint(true)` — 断点进入
2. `onCollapse(true, 'responsive')` — 折叠状态变更

当窗口宽度**恢复超过断点**时：
1. `onBreakpoint(false)` — 断点退出
2. `onCollapse(false, 'responsive')` — 展开

### 与受控模式配合的注意事项
```jsx
// ❌ 错误：受控模式下未监听 onCollapse，断点触发不会生效
<Sider collapsed={collapsed} breakpoint="lg">

// ✅ 正确：受控模式必须同时处理 onCollapse
<Sider
  collapsed={collapsed}
  breakpoint="lg"
  onCollapse={(val) => setCollapsed(val)}  // 必须！
>
```

---

## 4. resizeBoxProps 可拖拽配置（lingyang 专有）

`resizeBoxProps` 是 lingyang 设计系统的扩展特性，其他设计系统不具备。

### 基础配置
```jsx
<Sider
  width={200}  // 此时为初始宽度，拖拽后不受控
  resizeBoxProps={{
    directions: ['right'],        // 左侧边栏：向右拖
    style: {
      minWidth: 120,
      maxWidth: 480
    }
  }}
>
```

### 右侧边栏的拖拽配置
```jsx
<Sider
  width={240}
  reverseArrow
  resizeBoxProps={{
    directions: ['left'],         // 右侧边栏：向左拖
    style: { minWidth: 160, maxWidth: 400 }
  }}
>
```

### 监听宽度变化
```jsx
const [siderWidth, setSiderWidth] = useState(200);

<Sider
  width={siderWidth}
  resizeBoxProps={{
    directions: ['right'],
    onMoving: (_, { width }) => setSiderWidth(width),  // 实时监听
    style: { minWidth: 120, maxWidth: 480 }
  }}
>
```

### 与折叠联动
拖拽和折叠可同时启用，但需注意：
- 折叠后 `collapsedWidth` 生效，拖拽手柄隐藏
- 展开后恢复为**上次拖拽的宽度**（而非 `width` 初始值）

```jsx
const [collapsed, setCollapsed] = useState(false);

<Sider
  collapsed={collapsed}
  onCollapse={setCollapsed}
  collapsible
  width={200}
  collapsedWidth={48}
  resizeBoxProps={{
    directions: ['right'],
    style: { minWidth: 120, maxWidth: 480 }
  }}
>
```

---

## 5. 常见问题与陷阱

### Q1: SSR 下侧边栏布局闪烁
**原因**：服务端无法检测子节点是否含 Sider，导致 `flex-direction` 在服务端和客户端不一致。

**解决**：在含 Sider 的最外层 Layout 手动设置 `hasSider`：
```jsx
<Layout hasSider>  {/* ← 明确告知服务端 */}
  <Sider>...</Sider>
  <Layout>...</Layout>
</Layout>
```

---

### Q2: 折叠时 Menu 文字没有隐藏
**原因**：Menu 需要感知 `collapsed` 状态来隐藏文字标签。

**解决**：将 `collapsed` 状态传给 Menu 的 `collapsed` prop：
```jsx
const [collapsed, setCollapsed] = useState(false);

<Sider collapsed={collapsed} onCollapse={setCollapsed} collapsible>
  <Menu
    theme="dark"
    mode="inline"
    inlineCollapsed={collapsed}  // ← 关键：同步给 Menu
  >
    <Menu.Item key="1" icon={<IconDashboard />}>Dashboard</Menu.Item>
  </Menu>
</Sider>
```

---

### Q3: 零宽模式触发器遮挡内容
**原因**：`collapsedWidth=0` 时触发器绝对定位，叠在内容区上方。

**解决**：通过 CSS 调整触发器位置，或隐藏默认触发器改用外部按钮：
```jsx
// 方案 A：CSS 调整位置
.lingyang-layout-sider-zero-width-trigger {
  top: 64px;         /* 跳过 Header 高度 */
  border-radius: 0 4px 4px 0;
}

// 方案 B：隐藏默认触发器，用 Header 内按钮控制（推荐）
<Sider collapsedWidth={0} trigger={null} collapsed={collapsed}>
<Header>
  <Button onClick={() => setCollapsed(c => !c)}>
    {collapsed ? '展开' : '收起'}
  </Button>
</Header>
```

---

### Q4: 响应式折叠后无法手动展开
**原因**：受控模式下响应式折叠了，但没有提供展开入口。

**解决**：确保在小屏下也有可交互的展开按钮（通常用 Drawer 替代）：
```jsx
<Sider
  collapsed={collapsed}
  breakpoint="md"
  collapsedWidth={0}
  trigger={null}
  onCollapse={setCollapsed}
>
// Header 中始终显示菜单按钮
<Header>
  <Button
    type="text"
    icon={<IconMenu />}
    onClick={() => setCollapsed(c => !c)}
  />
</Header>
```

---
