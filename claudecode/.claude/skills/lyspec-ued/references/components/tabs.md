# lingyang Tabs 标签页

**类型**: JSX 组件（受控/非受控均支持）

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本标签页 | `<Tabs defaultActiveTab="1"><TabPane key="1" title="Tab1">内容</TabPane></Tabs>` |
| 受控模式 | `<Tabs activeTab={active} onChange={setActive}>` |
| 卡片样式 | `<Tabs type="card">` |
| 胶囊样式（筛选器） | `<Tabs type="capsule">` |
| 标签在左侧 | `<Tabs position="left">` |
| 可增删标签 | `<Tabs editable onAddTab={handleAdd} onDeleteTab={handleDelete}>` |
| 等宽 tab | `<Tabs justify>` |
| 禁用某 tab | `<TabPane key="2" title="Tab2" disabled>` |
| 不可关闭的 tab | `<TabPane key="1" title="Tab1" closable={false}>` |

---

## 与 Ant Design 的 4 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **受控参数名不同**
   - lingyang: `activeTab` / `defaultActiveTab`
   - Ant Design: `activeKey` / `defaultActiveKey`

2. **TabPane 标题属性名不同**
   - lingyang: `<TabPane title="标题">`
   - Ant Design: `<TabPane tab="标题">`

3. **可编辑 tab 的实现方式不同**
   - lingyang: `editable={true}` + `onAddTab()` + `onDeleteTab(key)`
   - Ant Design: `type="editable-card"` + `onEdit(key, action)`

4. **标签位置参数名不同**
   - lingyang: `position="left"`
   - Ant Design: `tabPosition="left"`

---

## Tabs Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| activeTab | string | — | 受控：当前选中 tab 的 key |
| defaultActiveTab | string | — | 非受控：初始选中 key |
| type | 见下方 | `'line'` | 视觉样式类型（6种） |
| size | `'mini'\|'small'\|'default'\|'large'` | `'default'` | 尺寸 |
| position | `'top'\|'bottom'\|'left'\|'right'` | `'top'` | 标签栏位置 |
| editable | boolean | false | 是否可增减标签 |
| justify | boolean | false | tab 等宽平均分布（lingyang 专有） |
| animation | boolean \| `{tabPane?,inkBar?}` | true | 过渡动画 |
| scrollPosition | `'start'\|'end'\|'center'\|'auto'\|number` | `'auto'` | 切换时滚动停靠位置（lingyang 专有） |
| overflow | `'scroll'\|'dropdown'` | `'scroll'` | tab 溢出时的处理方式 |
| lazyload | boolean | true | 首次激活才渲染（与 Ant Design forceRender 语义相反） |
| destroyOnHide | boolean | false | 切换时销毁非活跃标签 DOM |
| tabBarExtraContent | ReactNode | — | 标签栏额外内容（渲染在右侧/底部） |
| renderTabTitle | function | — | 全局自定义 tab 标题渲染 |
| icons | object | — | 自定义功能图标（add/delete/prev/next/dropdown） |
| headerPadding | boolean | true | 标签栏首尾是否留 padding |
| onChange | `(key: string) => void` | — | tab 切换回调 |
| onAddTab | `() => void` | — | 点击添加按钮回调（需 editable=true） |
| onDeleteTab | `(key: string) => void` | — | 点击删除按钮回调（需 editable=true） |
| onClickTab | `(key: string) => void` | — | 点击 tab 时回调（无论是否切换都触发） |

### type 可选值说明

| 值 | 描述 | 来源 |
|----|------|------|
| `line` | 底部下划线指示器，默认，最常用 | 通用 |
| `card` | 卡片式，无间距 | 通用 |
| `card-gutter` | 卡片式带间距 | lingyang 专有 |
| `text` | 纯文字，无边框背景，最轻量 | lingyang 专有 |
| `rounded` | 圆角卡片背景，适合内嵌于卡片内的次级导航 | lingyang 专有 |
| `capsule` | 胶囊型切换，适合筛选器、少量选项 | lingyang 专有 |

---

## TabPane Props

| Prop | 类型 | 必填 | 说明 |
|------|------|------|------|
| key | string | ✅ | 唯一标识 |
| title | ReactNode | ✅ | tab 标题（注意：不是 tab，不是 label） |
| disabled | boolean | — | 是否禁用（默认 false） |
| closable | boolean | — | 是否显示关闭按钮（默认 true，仅 editable=true 时生效） |
| destroyOnHide | boolean | — | 覆盖父级，单独控制销毁策略 |
| renderTabTitle | function | — | 覆盖全局，自定义该 tab 的标题渲染 |

---

## 常用 CSS 类名

`.lingyang-tabs` / `.lingyang-tabs-nav` / `.lingyang-tabs-tab` / `.lingyang-tabs-tab-active` / `.lingyang-tabs-tab-disabled` / `.lingyang-tabs-ink-bar` / `.lingyang-tabs-content` / `.lingyang-tabs-tabpane` / `.lingyang-tabs-type-{line|card|rounded|capsule}` / `.lingyang-tabs-left` / `.lingyang-tabs-right` / `.lingyang-tabs-bottom`

---

## 参考文件

- 完整代码示例（8个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Tabs — 完整代码示例

## 1. 基本用法（非受控）

```jsx
import { Tabs } from 'lingyang';
const { TabPane } = Tabs;

function BasicTabs() {
  return (
    <Tabs defaultActiveTab="1">
      <TabPane key="1" title="Tab 1">Tab 1 的内容</TabPane>
      <TabPane key="2" title="Tab 2">Tab 2 的内容</TabPane>
      <TabPane key="3" title="Tab 3" disabled>禁用标签（不可点击）</TabPane>
    </Tabs>
  );
}
```

## 2. 受控模式

```jsx
import { useState } from 'react';
import { Tabs } from 'lingyang';
const { TabPane } = Tabs;

function ControlledTabs() {
  const [active, setActive] = useState('1');

  return (
    <div>
      <p>当前激活：{active}</p>
      <Tabs activeTab={active} onChange={setActive}>
        <TabPane key="1" title="首页">首页内容</TabPane>
        <TabPane key="2" title="设置">设置内容</TabPane>
        <TabPane key="3" title="关于">关于内容</TabPane>
      </Tabs>
    </div>
  );
}
```

## 3. 6 种 type 样式

```jsx
// line（默认）
<Tabs type="line" defaultActiveTab="1">...</Tabs>

// card
<Tabs type="card" defaultActiveTab="1">...</Tabs>

// card-gutter（lingyang 专有：卡片带间距）
<Tabs type="card-gutter" defaultActiveTab="1">...</Tabs>

// text（lingyang 专有：纯文字，最轻量）
<Tabs type="text" defaultActiveTab="1">...</Tabs>

// rounded（lingyang 专有：圆角背景，适合嵌套导航）
<Tabs type="rounded" defaultActiveTab="1">...</Tabs>

// capsule（lingyang 专有：胶囊型，适合筛选器）
<Tabs type="capsule" defaultActiveTab="1">...</Tabs>
```

## 4. 标签位置

```jsx
// 左侧（注意：lingyang 用 position，不是 tabPosition）
<Tabs position="left" defaultActiveTab="1">
  <TabPane key="1" title="选项 1">内容 1</TabPane>
  <TabPane key="2" title="选项 2">内容 2</TabPane>
</Tabs>

// 右侧
<Tabs position="right" defaultActiveTab="1">...</Tabs>

// 底部
<Tabs position="bottom" defaultActiveTab="1">...</Tabs>
```

## 5. 可编辑标签（增删 Tab）

```jsx
import { useState } from 'react';
import { Tabs } from 'lingyang';
const { TabPane } = Tabs;

function EditableTabs() {
  const [tabs, setTabs] = useState([
    { key: '1', title: 'Tab 1', content: '内容 1' },
    { key: '2', title: 'Tab 2', content: '内容 2' },
  ]);
  const [activeTab, setActiveTab] = useState('1');
  let counter = tabs.length;

  const handleAdd = () => {
    counter += 1;
    const newKey = String(counter);
    setTabs([...tabs, { key: newKey, title: `Tab ${counter}`, content: `内容 ${counter}` }]);
    setActiveTab(newKey);
  };

  const handleDelete = (key) => {
    const remaining = tabs.filter(t => t.key !== key);
    setTabs(remaining);
    if (activeTab === key && remaining.length > 0) {
      setActiveTab(remaining[remaining.length - 1].key);
    }
  };

  return (
    // 注意：lingyang 用 editable + onAddTab + onDeleteTab
    // 不是 Ant Design 的 type="editable-card" + onEdit
    <Tabs
      editable
      activeTab={activeTab}
      onChange={setActiveTab}
      onAddTab={handleAdd}
      onDeleteTab={handleDelete}
    >
      {tabs.map(tab => (
        <TabPane key={tab.key} title={tab.title}>
          {tab.content}
        </TabPane>
      ))}
    </Tabs>
  );
}
```

## 6. 带图标的标题 + 等宽分布

```jsx
import { Tabs } from 'lingyang';
import { IconHome, IconSettings, IconUser } from 'lingyang/icon';
const { TabPane } = Tabs;

function IconTabs() {
  return (
    // justify：等宽平均分布（lingyang 专有）
    <Tabs defaultActiveTab="home" justify>
      <TabPane
        key="home"
        title={<span><IconHome /> 首页</span>}
      >
        首页内容
      </TabPane>
      <TabPane
        key="settings"
        title={<span><IconSettings /> 设置</span>}
      >
        设置内容
      </TabPane>
      <TabPane
        key="profile"
        title={<span><IconUser /> 个人</span>}
      >
        个人内容
      </TabPane>
    </Tabs>
  );
}
```

## 7. 标签栏额外内容（tabBarExtraContent）

```jsx
import { Tabs, Button } from 'lingyang';
const { TabPane } = Tabs;

function TabsWithExtra() {
  return (
    <Tabs
      defaultActiveTab="1"
      tabBarExtraContent={
        <Button size="small" type="primary">新增</Button>
      }
    >
      <TabPane key="1" title="列表">列表内容</TabPane>
      <TabPane key="2" title="详情">详情内容</TabPane>
    </Tabs>
  );
}
```

## 8. overflow 溢出处理（折叠到下拉）

```jsx
import { Tabs } from 'lingyang';
const { TabPane } = Tabs;

function OverflowTabs() {
  const tabs = Array.from({ length: 20 }, (_, i) => ({
    key: String(i + 1),
    title: `Tab ${i + 1}`,
  }));

  return (
    // 溢出时折叠到下拉菜单
    <Tabs defaultActiveTab="1" overflow="dropdown">
      {tabs.map(tab => (
        <TabPane key={tab.key} title={tab.title}>
          {tab.title} 的内容
        </TabPane>
      ))}
    </Tabs>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Tabs — 完整 TypeScript 接口定义

## TabsProps

```typescript
interface TabsProps {
  /** 受控：当前选中 tab 的 key。【命名差异】lingyang 用 activeTab，Ant Design 用 activeKey */
  activeTab?: string;
  /** 非受控：初始选中 tab 的 key。【命名差异】lingyang 用 defaultActiveTab，Ant Design 用 defaultActiveKey */
  defaultActiveTab?: string;
  /**
   * 标签页的视觉样式。lingyang 共 6 种，Ant Design 仅 3 种。
   * rounded/capsule/text/card-gutter 为 lingyang 专有
   */
  type?: 'line' | 'card' | 'card-gutter' | 'text' | 'rounded' | 'capsule';
  /** 标签页尺寸。lingyang 比 Ant Design 多 mini 尺寸 */
  size?: 'mini' | 'small' | 'default' | 'large';
  /** 标签栏位置。【命名差异】lingyang 用 position，Ant Design 用 tabPosition */
  position?: 'top' | 'bottom' | 'left' | 'right';
  /** 是否可增减标签（显示 + 和 × 按钮）。配合 onAddTab/onDeleteTab 使用 */
  editable?: boolean;
  /** 【lingyang 专有】tab 等宽平均分布，撑满 tab 栏全部宽度 */
  justify?: boolean;
  /** 是否开启过渡动画。对象形式可分别控制内容区（tabPane）和指示条（inkBar）动画 */
  animation?: boolean | { tabPane?: boolean; inkBar?: boolean };
  /**
   * 【lingyang 专有】切换时 active tab 的滚动停靠位置。
   * 传 number 时为距头部的 px 偏移量
   */
  scrollPosition?: 'start' | 'end' | 'center' | 'auto' | number;
  /** tab 超出可见区时的处理：scroll=左右滚动，dropdown=折叠到下拉菜单 */
  overflow?: 'scroll' | 'dropdown';
  /** 标签栏额外内容区，渲染在标签栏右侧（top/bottom 时）或底部（left/right 时） */
  tabBarExtraContent?: ReactNode;
  /** 全局自定义 tab 标题渲染函数 */
  renderTabTitle?: (
    tabTitle: ReactNode,
    info: { key: string; disabled: boolean; active: boolean }
  ) => ReactNode;
  /** tab 切换时的回调，参数为新选中 tab 的 key */
  onChange?: (key: string) => void;
  /** 点击添加按钮（+）的回调。需设置 editable=true */
  onAddTab?: () => void;
  /** 点击删除按钮（×）的回调，参数为被删除 tab 的 key。需设置 editable=true */
  onDeleteTab?: (key: string) => void;
  /** 点击 tab 标题时的回调（无论是否切换都触发） */
  onClickTab?: (key: string) => void;
  /** 切换时是否销毁非活跃标签的 DOM 节点 */
  destroyOnHide?: boolean;
  /**
   * 是否懒加载（只在首次激活时渲染内容）。
   * 【语义差异】lingyang 为 lazyload=true；Ant Design 对应 forceRender=false（语义相反）
   */
  lazyload?: boolean;
  /** 自定义各功能图标 */
  icons?: {
    add?: ReactNode;
    delete?: ReactNode;
    prev?: ReactNode;
    next?: ReactNode;
    dropdown?: ReactNode;
  };
  /** 是否在标签栏首尾两端留有 padding 间距 */
  headerPadding?: boolean;
  className?: string;
  style?: CSSProperties;
}
```

## TabPaneProps

```typescript
interface TabPaneProps {
  /** 标签页唯一标识，对应 Tabs 的 activeTab/defaultActiveTab */
  key: string; // required
  /**
   * tab 标题。支持字符串或带图标的复合 ReactNode。
   * 【命名差异】lingyang 用 title，Ant Design 用 tab
   */
  title: ReactNode; // required
  /** 是否禁用该标签页 */
  disabled?: boolean;
  /** 是否显示关闭按钮（仅 Tabs editable=true 时生效）。false 表示该 tab 不可被删除 */
  closable?: boolean;
  /** 覆盖 Tabs 全局 destroyOnHide，单独控制该 TabPane 的销毁策略 */
  destroyOnHide?: boolean;
  /** 覆盖 Tabs 全局 renderTabTitle，自定义该 tab 的标题渲染 */
  renderTabTitle?: (
    tabTitle: ReactNode,
    info: { key: string; disabled: boolean; active: boolean }
  ) => ReactNode;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| 受控参数名 | `activeTab` | `activeKey` |
| 非受控参数名 | `defaultActiveTab` | `defaultActiveKey` |
| TabPane 标题属性 | `title` | `tab` |
| 标签位置参数 | `position` | `tabPosition` |
| 可编辑 tab | `editable` + `onAddTab` + `onDeleteTab` | `type="editable-card"` + `onEdit` |
| 样式类型数量 | 6种（含 rounded/capsule/text/card-gutter） | 3种 |
| 等宽分布 | `justify={true}` | ❌ 无 |
| 滚动停靠位置 | `scrollPosition` | ❌ 无 |
| 懒加载 | `lazyload={true}`（默认 true） | `forceRender={false}`（语义相反） |
| 最小尺寸 | `size="mini"` 可用 | `size="small"` 是最小 |

---
