# lingyang Badge 徽标数字

**类型**: JSX 组件（包裹模式 / 独立模式均支持）

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 数字徽标 | `<Badge count={5}><Avatar /></Badge>` |
| 圆点模式（不显示数字） | `<Badge dot><IconBell /></Badge>` |
| 超出最大值 | `<Badge count={120} maxCount={99}>` → 显示 99+ |
| 0 时也显示 | `<Badge count={0} showZero>` |
| 独立状态点 | `<Badge status="processing" text="进行中" />` |
| 自定义颜色 | `<Badge color="#f50" count={3}>` |
| 缎带标签 | `<Badge.Ribbon text="推荐"><Card /></Badge.Ribbon>` |
| 关闭动画 | `<Badge count={num} animation={false}>` |
| 偏移徽标 | `<Badge count={5} offset={[5, -5]}>` |

---

## 与 Ant Design 的 4 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **status 枚举值不同**
   - lingyang: `'normal' | 'processing' | 'success' | 'warning' | 'error'`
   - Ant Design: `'default' | 'processing' | 'success' | 'warning' | 'error'`（无 `normal`，有 `default`）

2. **Badge.Ribbon 位置属性名不同**
   - lingyang: `<Badge.Ribbon position="start">`
   - Ant Design: `<Badge.Ribbon placement="start">`

3. **animation 属性（lingyang 专有）**
   - lingyang: `animation={false}` 可关闭数字滚动动画
   - Ant Design: 无此属性，需通过 CSS 控制

4. **独立状态点**
   - lingyang 和 Ant Design 写法相似，但 `status="normal"` 仅在 lingyang 可用

---

## Badge Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| count | number \| ReactNode | — | 显示的数字或自定义内容 |
| text | ReactNode | — | 独立状态点旁的文字（配合 status 使用） |
| status | 见下方 | — | 状态类型，决定颜色 |
| color | string | — | 自定义颜色（预设色名或 CSS 色值） |
| maxCount | number | `99` | 超出后显示 maxCount+ |
| dot | boolean | `false` | 只显示圆点，不显示数字 |
| showZero | boolean | `false` | count=0 时是否显示徽标 |
| animation | boolean | `true` | 数字切换动画（lingyang 专有） |
| offset | [number, number] | — | 徽标偏移量 [x, y]（px） |
| countStyle | CSSProperties | — | 徽标数字区域自定义样式 |

### status 可选值

| 值 | 颜色/效果 | 来源 |
|----|----------|------|
| `normal` | 灰色 | lingyang 专有（Ant Design 无） |
| `processing` | 蓝色 + 脉冲动画 | 通用 |
| `success` | 绿色 | 通用 |
| `warning` | 橙色 | 通用 |
| `error` | 红色 | 通用 |

---

## Badge.Ribbon Props

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| text | ReactNode | — | 缎带上的文字 |
| color | string | — | 缎带颜色 |
| position | `'start' \| 'end'` | `'end'` | 缎带位置（**注意：不是 placement**） |
| children | ReactNode | ✅ | 被包裹的目标元素（必填） |

---

## 常用 CSS 类名

`.lingyang-badge` / `.lingyang-badge-number` / `.lingyang-badge-dot` / `.lingyang-badge-status-dot` / `.lingyang-badge-status-text` / `.lingyang-badge-status-processing` / `.lingyang-badge-status-{success|error|warning|normal}` / `.lingyang-ribbon-wrapper` / `.lingyang-ribbon` / `.lingyang-ribbon-corner` / `.lingyang-ribbon-{start|end}`

---

## 参考文件

- 完整代码示例（7个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Badge — 完整代码示例

## 1. 基本数字徽标

```jsx
import { Badge, Avatar, Space } from 'lingyang';

function BasicBadge() {
  return (
    <Space size="large">
      {/* 包裹头像，显示未读数 */}
      <Badge count={5}>
        <Avatar shape="square" />
      </Badge>

      {/* 超出 maxCount 显示 99+ */}
      <Badge count={120} maxCount={99}>
        <Avatar shape="square" />
      </Badge>

      {/* count=0 时不显示（默认） */}
      <Badge count={0}>
        <Avatar shape="square" />
      </Badge>

      {/* count=0 但 showZero，仍显示 */}
      <Badge count={0} showZero>
        <Avatar shape="square" />
      </Badge>
    </Space>
  );
}
```

## 2. 圆点模式（dot）

```jsx
import { Badge } from 'lingyang';
import { IconBell, IconMessage } from 'lingyang/icon';

function DotBadge() {
  return (
    <Space>
      {/* 只显示圆点，不显示数字 */}
      <Badge dot>
        <IconBell style={{ fontSize: 24 }} />
      </Badge>

      <Badge dot color="red">
        <IconMessage style={{ fontSize: 24 }} />
      </Badge>
    </Space>
  );
}
```

## 3. 独立状态点（不包裹子元素）

```jsx
import { Badge, Space } from 'lingyang';

function StatusBadge() {
  return (
    <Space direction="vertical">
      {/* 注意：lingyang 用 'normal'，Ant Design 用 'default' */}
      <Badge status="normal" text="普通" />
      <Badge status="processing" text="处理中" />
      <Badge status="success" text="成功" />
      <Badge status="warning" text="警告" />
      <Badge status="error" text="错误" />
    </Space>
  );
}
```

## 4. 自定义颜色

```jsx
import { Badge, Avatar, Space } from 'lingyang';

function ColorBadge() {
  return (
    <Space>
      {/* 预设色名 */}
      <Badge count={3} color="blue">
        <Avatar shape="square" />
      </Badge>

      {/* CSS 色值 */}
      <Badge count={3} color="#f50">
        <Avatar shape="square" />
      </Badge>

      {/* 独立状态点自定义颜色 */}
      <Badge color="purple" text="自定义颜色" />
    </Space>
  );
}
```

## 5. 偏移位置（offset）

```jsx
import { Badge, Avatar } from 'lingyang';

function OffsetBadge() {
  return (
    // offset: [x偏移, y偏移]，单位 px
    // 正 x 向右，正 y 向下（注意：y 轴正方向向下）
    <Badge count={5} offset={[6, -6]}>
      <Avatar shape="square" size={40} />
    </Badge>
  );
}
```

## 6. 动态数字 + 关闭动画（animation）

```jsx
import { useState } from 'react';
import { Badge, Button, Space } from 'lingyang';
import { IconPlus, IconMinus } from 'lingyang/icon';

function AnimationBadge() {
  const [count, setCount] = useState(5);

  return (
    <Space direction="vertical" align="center">
      {/* animation 为 lingyang 专有属性，Ant Design 无 */}
      <Badge count={count} animation={true}>
        <div style={{ width: 40, height: 40, background: '#ccc', borderRadius: 4 }} />
      </Badge>

      <Space>
        <Button icon={<IconMinus />} onClick={() => setCount(Math.max(0, count - 1))} />
        <Button icon={<IconPlus />} onClick={() => setCount(count + 1)} />
      </Space>
    </Space>
  );
}
```

## 7. Badge.Ribbon 缎带标签

```jsx
import { Badge, Card, Space } from 'lingyang';

function RibbonBadge() {
  return (
    <Space>
      {/* 注意：lingyang 用 position，Ant Design 用 placement */}
      <Badge.Ribbon text="推荐" color="blue">
        <Card style={{ width: 200 }}>
          <p>卡片内容</p>
        </Card>
      </Badge.Ribbon>

      {/* 左侧缎带 */}
      <Badge.Ribbon text="NEW" color="green" position="start">
        <Card style={{ width: 200 }}>
          <p>新功能卡片</p>
        </Card>
      </Badge.Ribbon>

      {/* 自定义颜色 */}
      <Badge.Ribbon text="HOT" color="#f50">
        <Card style={{ width: 200 }}>
          <p>热门内容</p>
        </Card>
      </Badge.Ribbon>
    </Space>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Badge — 完整 TypeScript 接口定义

## BadgeProps

```typescript
interface BadgeProps {
  /** 徽标显示的数字或自定义内容。为 0 时默认不显示（可用 showZero 覆盖） */
  count?: number | ReactNode;
  /** 独立状态点旁边的文字说明（配合 status 使用，不包裹 children 时常用） */
  text?: ReactNode;
  /**
   * 徽标状态类型，决定颜色。
   * 【差异】lingyang 有 'normal'，Ant Design 对应 'default'
   */
  status?: 'normal' | 'processing' | 'success' | 'warning' | 'error';
  /** 自定义徽标颜色，支持预设色名或任意 CSS 颜色值（如 '#f00'、'red'、'blue'） */
  color?: string;
  /** 最大显示数字，超出后显示 maxCount+（如 99+）。默认 99 */
  maxCount?: number;
  /** 是否只显示圆点，不显示数字。默认 false */
  dot?: boolean;
  /** count 为 0 时是否显示徽标。默认 false */
  showZero?: boolean;
  /**
   * 【lingyang 专有】数字切换时是否开启滚动动画。默认 true。
   * Ant Design 无此属性，需通过 CSS 控制动画
   */
  animation?: boolean;
  /** 徽标偏移量 [x, y]，相对于默认位置（右上角）的像素偏移 */
  offset?: [number, number];
  /** 被徽标包裹的目标元素。不传时 Badge 作为独立状态点渲染 */
  children?: ReactNode;
  /** 徽标数字区域的自定义样式 */
  countStyle?: CSSProperties;
  className?: string;
  style?: CSSProperties;
}
```

## BadgeRibbonProps

```typescript
interface BadgeRibbonProps {
  /** 缎带上显示的文字内容 */
  text?: ReactNode;
  /** 缎带颜色，支持预设色名或任意 CSS 颜色值 */
  color?: string;
  /**
   * 缎带位置。【命名差异】lingyang 用 position，Ant Design 用 placement
   * 'start' = 左上角，'end' = 右上角（默认，支持 RTL）
   */
  position?: 'start' | 'end';
  /** 被缎带包裹的目标元素（必填） */
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| status 枚举 | `normal \| processing \| success \| warning \| error` | `default \| processing \| success \| warning \| error` |
| Ribbon 位置属性名 | `position` | `placement` |
| 数字切换动画控制 | `animation={false}` | ❌ 无属性，需 CSS |
| 独立状态点灰色 | `status="normal"` | `status="default"` |

---
