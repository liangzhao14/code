# lingyang Popover 气泡卡片

**类型**: JSX 组件（浮层触发器，包裹目标元素）

> **与 Tooltip 的区别**：Tooltip 仅适合纯文字提示；Popover 支持 `title`（标题）+ `content`（任意 ReactNode），适合承载更复杂的内容。

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本用法 | `<Popover title="标题" content={<p>内容</p>}><Button>触发</Button></Popover>` |
| 点击触发 | `<Popover trigger="click" ...>` |
| 受控显隐 | `<Popover popupVisible={visible} onVisibleChange={setVisible} ...>` |
| 指定弹出方向 | `<Popover position="bottom" ...>` |
| 禁用弹出 | `<Popover disabled ...>` |
| 隐藏箭头 | `<Popover showArrow={false} ...>` |
| 自定义背景色 | `<Popover color="#1d1d1d" ...>` |
| 右键触发 | `<Popover trigger="contextMenu" ...>` |
| 延迟显示 | `<Popover mouseEnterDelay={500} mouseLeaveDelay={300} ...>` |
| 自定义挂载容器 | `<Popover getPopupContainer={() => document.getElementById('container')} ...>` |

---

## 与 Ant Design 的 5 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **受控显隐属性名不同**
   - lingyang: `popupVisible` / `defaultPopupVisible`
   - Ant Design v5: `open` / `defaultOpen`

2. **显隐回调名不同**
   - lingyang: `onVisibleChange={(visible) => ...}`
   - Ant Design v5: `onOpenChange={(open) => ...}`

3. **箭头属性不同**
   - lingyang: `showArrow={false}`（boolean）
   - Ant Design v5: `arrow={false}` 或 `arrow={{ pointAtCenter: true }}`

4. **getPopupContainer 参数不同**
   - lingyang: `getPopupContainer={() => HTMLElement}`（无参数）
   - Ant Design: `getPopupContainer={(triggerNode) => HTMLElement}`（传入触发节点）

5. **挂载/卸载回调（lingyang 专有）**
   - lingyang: `onMount` / `onUnmount`
   - Ant Design: `afterOpenChange`

---

## Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | ReactNode | — | 气泡卡片标题 |
| content | ReactNode | — | 气泡卡片主体内容 |
| trigger | 见下方 | `'hover'` | 触发方式，可传数组 |
| position | 见下方 | `'top'` | 弹出位置（12 方向） |
| popupVisible | boolean | — | 受控：是否显示 |
| defaultPopupVisible | boolean | `false` | 非受控：初始是否显示 |
| onVisibleChange | `(visible: boolean) => void` | — | 显隐回调 |
| disabled | boolean | `false` | 禁用弹出 |
| showArrow | boolean | `true` | 是否显示箭头 |
| color | string | — | 背景颜色（同时影响箭头） |
| popupOffset | number | — | 浮层与触发元素的间距（px） |
| mouseEnterDelay | number | `100` | hover 触发，移入延迟（ms） |
| mouseLeaveDelay | number | `100` | hover 触发，移出延迟（ms） |
| getPopupContainer | `() => HTMLElement` | — | 指定挂载容器（无参数） |
| unmountOnExit | boolean | `true` | 关闭后是否卸载 DOM |
| autoFitPosition | boolean | `true` | 放不下时是否自动翻转位置 |
| blurToHide | boolean | `true` | focus 触发时，失焦是否隐藏 |
| popupStyle | CSSProperties | — | 浮层自定义样式 |
| popupClassName | string | — | 浮层自定义 className |
| onMount | `() => void` | — | 挂载到 DOM 后回调（lingyang 专有） |
| onUnmount | `() => void` | — | 从 DOM 卸载后回调（lingyang 专有） |

### trigger 可选值

| 值 | 说明 |
|----|------|
| `'hover'` | 鼠标移入触发（默认） |
| `'click'` | 点击触发 |
| `'focus'` | 聚焦触发 |
| `'contextMenu'` | 右键菜单触发 |

### position 12 方向

```
tl    top    tr
lt           rt
lb           rb
bl  bottom   br

left  / right（中间对齐）
```

---

## 常用 CSS 类名

`.lingyang-popover` / `.lingyang-popover-popup` / `.lingyang-popover-arrow` / `.lingyang-popover-title` / `.lingyang-popover-content` / `.lingyang-trigger-placement-{top|bottom|left|right|tl|tr|bl|br|lt|lb|rt|rb}`

---

## 参考文件

- 完整代码示例（7个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Popover — 完整代码示例

## 1. 基本用法（hover 触发）

```jsx
import { Popover, Button } from 'lingyang';

function BasicPopover() {
  const content = (
    <div>
      <p>这是气泡卡片的内容区域</p>
      <p>可以放置任意 ReactNode</p>
    </div>
  );

  return (
    <Popover title="标题" content={content}>
      <Button>鼠标移入触发</Button>
    </Popover>
  );
}
```

## 2. 触发方式（trigger）

```jsx
import { Popover, Button, Space } from 'lingyang';

const content = <div><p>气泡卡片内容</p></div>;

function TriggerPopover() {
  return (
    <Space>
      {/* 默认 hover 触发 */}
      <Popover title="Hover 触发" content={content} trigger="hover">
        <Button>Hover</Button>
      </Popover>

      {/* 点击触发 */}
      <Popover title="Click 触发" content={content} trigger="click">
        <Button>Click</Button>
      </Popover>

      {/* 聚焦触发 */}
      <Popover title="Focus 触发" content={content} trigger="focus">
        <Button>Focus</Button>
      </Popover>

      {/* 右键菜单触发 */}
      <Popover title="右键触发" content={content} trigger="contextMenu">
        <Button>右键点击</Button>
      </Popover>

      {/* 多种触发方式组合 */}
      <Popover title="组合触发" content={content} trigger={['click', 'hover']}>
        <Button>Click + Hover</Button>
      </Popover>
    </Space>
  );
}
```

## 3. 受控显隐

```jsx
import { useState } from 'react';
import { Popover, Button } from 'lingyang';

function ControlledPopover() {
  const [visible, setVisible] = useState(false);

  return (
    <div>
      {/* 注意：lingyang 用 popupVisible + onVisibleChange */}
      {/* Ant Design v5 用 open + onOpenChange */}
      <Popover
        title="受控气泡"
        content={
          <div>
            <p>受控模式下的内容</p>
            <Button size="small" onClick={() => setVisible(false)}>
              关闭
            </Button>
          </div>
        }
        trigger="click"
        popupVisible={visible}
        onVisibleChange={setVisible}
      >
        <Button>点击切换</Button>
      </Popover>

      <Button
        style={{ marginLeft: 8 }}
        onClick={() => setVisible(!visible)}
      >
        外部控制：{visible ? '隐藏' : '显示'}
      </Button>
    </div>
  );
}
```

## 4. 12 个弹出位置

```jsx
import { Popover, Button } from 'lingyang';

const positions = [
  'tl', 'top', 'tr',
  'lt', 'rt',
  'lb', 'rb',
  'bl', 'bottom', 'br',
  'left', 'right',
];

function PositionPopover() {
  return (
    <div style={{ position: 'relative', width: 400, height: 300 }}>
      {positions.map(pos => (
        <Popover
          key={pos}
          position={pos}
          title={`position="${pos}"`}
          content={<span>弹出方向：{pos}</span>}
        >
          <Button style={{ position: 'absolute', /* 根据方向定位 */ }}>
            {pos}
          </Button>
        </Popover>
      ))}
    </div>
  );
}
```

## 5. 自定义样式（颜色 + 隐藏箭头）

```jsx
import { Popover, Button, Space } from 'lingyang';

function StyledPopover() {
  return (
    <Space>
      {/* 自定义背景色（箭头颜色随之改变） */}
      <Popover
        title="深色气泡"
        content={<span style={{ color: '#fff' }}>自定义颜色内容</span>}
        color="#1d1d1d"
        trigger="click"
      >
        <Button>深色主题</Button>
      </Popover>

      {/* 隐藏箭头 */}
      {/* 注意：lingyang 用 showArrow={false}，Ant Design v5 用 arrow={false} */}
      <Popover
        title="无箭头气泡"
        content={<p>没有箭头的气泡卡片</p>}
        showArrow={false}
        trigger="click"
      >
        <Button>无箭头</Button>
      </Popover>
    </Space>
  );
}
```

## 6. 延迟显隐

```jsx
import { Popover, Button } from 'lingyang';

function DelayPopover() {
  return (
    <Popover
      title="延迟气泡"
      content={<p>移入 500ms 后显示，移出 300ms 后隐藏</p>}
      mouseEnterDelay={500}
      mouseLeaveDelay={300}
    >
      <Button>悬停查看（有延迟）</Button>
    </Popover>
  );
}
```

## 7. 指定挂载容器 + 卸载策略

```jsx
import { useRef } from 'react';
import { Popover, Button } from 'lingyang';

function ContainerPopover() {
  const containerRef = useRef(null);

  return (
    <div
      ref={containerRef}
      style={{ position: 'relative', overflow: 'hidden', padding: 40 }}
    >
      {/* 注意：lingyang 的 getPopupContainer 无参数 */}
      {/* Ant Design 的 getPopupContainer 接收 triggerNode 参数 */}
      <Popover
        title="挂载到容器内"
        content={<p>气泡挂载在父容器中，不会溢出</p>}
        trigger="click"
        getPopupContainer={() => containerRef.current}
        unmountOnExit={false}  // 关闭后保留 DOM（不卸载）
      >
        <Button>指定容器</Button>
      </Popover>
    </div>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Popover — 完整 TypeScript 接口定义

## PopoverProps

```typescript
interface PopoverProps {
  /** 气泡卡片的标题区域内容 */
  title?: ReactNode;
  /** 气泡卡片的主体内容区域（支持任意 ReactNode） */
  content?: ReactNode;
  /**
   * 触发弹出的方式。可传数组同时支持多种触发方式
   * 默认: 'hover'
   */
  trigger?: 'hover' | 'click' | 'focus' | 'contextMenu'
           | Array<'hover' | 'click' | 'focus' | 'contextMenu'>;
  /**
   * 气泡弹出位置，共 12 个方向。
   * 缩写：t=top, b=bottom, l=left, r=right，第二字母为对齐方向
   * 默认: 'top'
   */
  position?: 'top' | 'tl' | 'tr'
           | 'bottom' | 'bl' | 'br'
           | 'left' | 'lt' | 'lb'
           | 'right' | 'rt' | 'rb';
  /**
   * 受控：是否显示气泡卡片。
   * 【命名差异】lingyang 用 popupVisible，Ant Design v5 用 open
   */
  popupVisible?: boolean;
  /**
   * 非受控：初始是否显示。默认 false
   * 【命名差异】lingyang 用 defaultPopupVisible，Ant Design v5 用 defaultOpen
   */
  defaultPopupVisible?: boolean;
  /**
   * 显隐状态变化回调。
   * 【命名差异】lingyang 用 onVisibleChange，Ant Design v5 用 onOpenChange
   */
  onVisibleChange?: (visible: boolean) => void;
  /** 是否禁用弹出（禁用后任何触发方式均不生效）。默认 false */
  disabled?: boolean;
  /**
   * 是否显示箭头。默认 true。
   * 【类型差异】lingyang 为 boolean；Ant Design v5 为 boolean | { pointAtCenter: boolean }
   */
  showArrow?: boolean;
  /** 气泡卡片背景颜色（同时影响箭头颜色），支持 CSS 色值 */
  color?: string;
  /** 弹出框距离触发元素的偏移距离（px） */
  popupOffset?: number;
  /** hover 触发时，鼠标移入后延迟显示的时间（ms）。默认 100 */
  mouseEnterDelay?: number;
  /** hover 触发时，鼠标移出后延迟隐藏的时间（ms）。默认 100 */
  mouseLeaveDelay?: number;
  /** 气泡位置的精细对齐配置（优先级高于 position） */
  popupAlign?: object;
  /**
   * 指定气泡挂载的容器节点。
   * 【参数差异】lingyang 无参数；Ant Design 传入 triggerNode: HTMLElement
   */
  getPopupContainer?: () => HTMLElement;
  /** 气泡关闭后是否卸载 DOM 节点。默认 true（关闭后销毁） */
  unmountOnExit?: boolean;
  /** 是否自动调整弹出位置（当指定位置放不下时自动翻转）。默认 true */
  autoFitPosition?: boolean;
  /** 触发方式为 focus 时，失去焦点是否隐藏气泡。默认 true */
  blurToHide?: boolean;
  /** 为触发元素添加的 className 前缀 */
  childrenPrefix?: string;
  /**
   * 【lingyang 专有】气泡挂载到 DOM 后的回调。
   * Ant Design 对应 afterOpenChange(open: true)
   */
  onMount?: () => void;
  /**
   * 【lingyang 专有】气泡从 DOM 卸载后的回调。
   * Ant Design 对应 afterOpenChange(open: false)
   */
  onUnmount?: () => void;
  /** 气泡浮层的自定义样式 */
  popupStyle?: CSSProperties;
  /** 气泡浮层的自定义 className */
  popupClassName?: string;
  /** 触发气泡的目标元素（必填） */
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design v5 |
|------|---------|---------------|
| 受控显示属性 | `popupVisible` | `open` |
| 非受控初始显示 | `defaultPopupVisible` | `defaultOpen` |
| 显隐回调 | `onVisibleChange` | `onOpenChange` |
| 箭头控制 | `showArrow: boolean` | `arrow: boolean \| { pointAtCenter: boolean }` |
| 容器挂载 | `getPopupContainer: () => HTMLElement`（无参数） | `getPopupContainer: (triggerNode) => HTMLElement` |
| 挂载回调 | `onMount` / `onUnmount` | `afterOpenChange(open: boolean)` |
| 偏移距离 | `popupOffset: number` | `align: AlignConfig`（更复杂） |
| 浮层样式 | `popupStyle` / `popupClassName` | `overlayStyle` / `overlayClassName` |

---
