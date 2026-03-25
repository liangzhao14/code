# lingyang Tag 标签

**类型**: JSX 组件

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本标签 | `<Tag>标签内容</Tag>` |
| 预设颜色 | `<Tag color="blue">蓝色</Tag>` |
| 自定义颜色 | `<Tag color="#f50">自定义</Tag>` |
| 可关闭 | `<Tag closable onClose={(e) => ...}>关闭</Tag>` |
| 带图标 | `<Tag icon={<IconStar />}>收藏</Tag>` |
| 圆角形状 | `<Tag shape="round">圆角</Tag>` |
| 可选中（非受控） | `<Tag checkable defaultChecked onChange={(v) => ...}>筛选</Tag>` |
| 可选中（受控） | `<Tag checkable checked={checked} onChange={setChecked}>筛选</Tag>` |
| 有边框 | `<Tag bordered color="blue">有边框</Tag>` |
| 受控显隐 | `<Tag visible={visible} closable onClose={() => setVisible(false)}>受控</Tag>` |

---

## 与 Ant Design 的 5 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **可选中 Tag 的实现方式不同**
   - lingyang: 在 `<Tag>` 上设置 `checkable={true}`，配合 `checked` / `defaultChecked` / `onChange`
   - Ant Design: 使用独立组件 `<Tag.CheckableTag checked onChange>`，不在 Tag 本身上配置

2. **icon 属性（lingyang 专有）**
   - lingyang: `<Tag icon={<IconStar />}>` 直接支持 icon 属性
   - Ant Design: 无 icon 属性，需手动将图标写在 children 内部

3. **尺寸枚举不同**
   - lingyang: `size="medium"` 可用（4 个尺寸：small / default / medium / large）
   - Ant Design: 仅 small / default / large（无 medium）

4. **visible 受控（lingyang 支持）**
   - lingyang: `visible` / `defaultVisible` 控制标签显隐
   - Ant Design v5: 已移除 visible，需自行做条件渲染

5. **预设颜色名集合不同**
   - lingyang 有 `arcoblue`（品牌专属）、`pinkpurple`、`orangered` 等
   - 两者均支持任意 CSS 颜色值

---

## Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| color | string | — | 颜色（预设色名或 CSS 色值） |
| size | `'small'\|'default'\|'medium'\|'large'` | `'default'` | 尺寸（含 medium，Ant Design 无） |
| shape | `'square'\|'round'\|'circle'` | `'square'` | 形状 |
| bordered | boolean | `false` | 是否显示边框 |
| icon | ReactNode | — | 左侧图标（**lingyang 专有**） |
| closable | boolean | `false` | 是否显示关闭按钮 |
| closeIcon | ReactNode | — | 自定义关闭图标 |
| onClose | `(e: MouseEvent) => void` | — | 点击关闭回调 |
| visible | boolean | — | 受控：是否显示（**lingyang 专有**，Ant Design v5 无） |
| defaultVisible | boolean | `true` | 非受控：初始是否显示 |
| checkable | boolean | `false` | 是否可选中（**lingyang 专有**，Ant Design 用 Tag.CheckableTag） |
| checked | boolean | — | 受控：是否选中（需 checkable=true） |
| defaultChecked | boolean | `false` | 非受控：初始是否选中（需 checkable=true） |
| onChange | `(checked: boolean) => void` | — | 选中状态变化回调 |
| onClick | `(e: MouseEvent) => void` | — | 点击标签回调 |

### 预设颜色名（color 可选值）

| 色名 | 色调 | 备注 |
|------|------|------|
| `red` | 红 | 危险/错误 |
| `orangered` | 橙红 | — |
| `orange` | 橙 | 警告 |
| `gold` | 金 | — |
| `lime` | 黄绿 | — |
| `green` | 绿 | 成功 |
| `cyan` | 青 | — |
| `blue` | 蓝 | — |
| `arcoblue` | 品牌蓝 | **lingyang 专有** |
| `purple` | 紫 | — |
| `pinkpurple` | 粉紫 | — |
| `magenta` | 品红 | — |
| `gray` | 灰 | 默认/中性 |

### shape 可选值

| 值 | 说明 |
|----|------|
| `square` | 直角矩形（默认） |
| `round` | 圆角胶囊，视觉柔和 |
| `circle` | 圆形，适合图标或单字符 |

---

## 常用 CSS 类名

`.lingyang-tag` / `.lingyang-tag-bordered` / `.lingyang-tag-closable` / `.lingyang-tag-close-btn` / `.lingyang-tag-checkable` / `.lingyang-tag-checked` / `.lingyang-tag-icon` / `.lingyang-tag-round` / `.lingyang-tag-circle` / `.lingyang-tag-size-{small|medium|large}` / `.lingyang-tag-{blue|red|green|...}`

---

## 参考文件

- 完整代码示例（7 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Tag — 完整代码示例

## 1. 基本用法 + 预设颜色

```jsx
import { Tag, Space } from 'lingyang';

function BasicTag() {
  return (
    <Space wrap>
      <Tag>默认标签</Tag>
      <Tag color="red">red</Tag>
      <Tag color="orangered">orangered</Tag>
      <Tag color="orange">orange</Tag>
      <Tag color="gold">gold</Tag>
      <Tag color="lime">lime</Tag>
      <Tag color="green">green</Tag>
      <Tag color="cyan">cyan</Tag>
      <Tag color="blue">blue</Tag>
      {/* arcoblue 为 lingyang 品牌专属色，Ant Design 无此预设 */}
      <Tag color="arcoblue">arcoblue</Tag>
      <Tag color="purple">purple</Tag>
      <Tag color="pinkpurple">pinkpurple</Tag>
      <Tag color="magenta">magenta</Tag>
      <Tag color="gray">gray</Tag>
      {/* 自定义颜色 */}
      <Tag color="#f50">自定义 #f50</Tag>
      <Tag color="rgb(0,128,0)">自定义 rgb</Tag>
    </Space>
  );
}
```

## 2. 形状（shape）

```jsx
import { Tag, Space } from 'lingyang';

function ShapeTag() {
  return (
    <Space>
      {/* 直角（默认） */}
      <Tag color="blue" shape="square">square</Tag>

      {/* 圆角胶囊 */}
      <Tag color="blue" shape="round">round</Tag>

      {/* 圆形，适合单字符/数字/图标 */}
      <Tag color="blue" shape="circle">A</Tag>
    </Space>
  );
}
```

## 3. 带图标（icon — lingyang 专有）

```jsx
import { Tag, Space } from 'lingyang';
import { IconStar, IconCheckCircle, IconCloseCircle } from 'lingyang/icon';

function IconTag() {
  // 注意：icon 属性为 lingyang 专有，Ant Design 需手动把图标写在 children 里
  return (
    <Space>
      <Tag color="gold" icon={<IconStar />}>收藏</Tag>
      <Tag color="green" icon={<IconCheckCircle />}>成功</Tag>
      <Tag color="red" icon={<IconCloseCircle />}>失败</Tag>
      {/* 带图标 + 圆角 */}
      <Tag color="arcoblue" icon={<IconStar />} shape="round">品牌标签</Tag>
    </Space>
  );
}
```

## 4. 可关闭标签

```jsx
import { useState } from 'react';
import { Tag, Space } from 'lingyang';

function ClosableTag() {
  // 方式一：非受控，点击 × 自动隐藏
  // 方式二：受控，通过 visible + onClose 手动控制

  const [tags, setTags] = useState(['标签 A', '标签 B', '标签 C']);

  const handleClose = (removedTag) => {
    setTags(tags.filter(t => t !== removedTag));
  };

  return (
    <Space wrap>
      {tags.map(tag => (
        <Tag
          key={tag}
          color="blue"
          closable
          onClose={(e) => {
            e.preventDefault(); // 阻止默认关闭，使用受控模式
            handleClose(tag);
          }}
        >
          {tag}
        </Tag>
      ))}
    </Space>
  );
}
```

## 5. 可选中标签（checkable — lingyang 专有）

```jsx
import { useState } from 'react';
import { Tag, Space } from 'lingyang';

// 注意：lingyang 直接在 Tag 上设置 checkable
// Ant Design 需用独立组件 <Tag.CheckableTag checked onChange>

function CheckableTag() {
  const filters = ['React', 'Vue', 'Angular', 'Svelte'];
  const [selected, setSelected] = useState(['React']);

  const toggle = (tag) => {
    setSelected(prev =>
      prev.includes(tag) ? prev.filter(t => t !== tag) : [...prev, tag]
    );
  };

  return (
    <Space>
      {filters.map(tag => (
        <Tag
          key={tag}
          checkable
          checked={selected.includes(tag)}
          onChange={() => toggle(tag)}
          color="arcoblue"
        >
          {tag}
        </Tag>
      ))}
    </Space>
  );
}
```

## 6. 有边框 + 尺寸

```jsx
import { Tag, Space } from 'lingyang';

function SizeAndBorderedTag() {
  return (
    <Space direction="vertical">
      {/* 有边框 */}
      <Space>
        <Tag color="blue" bordered>blue bordered</Tag>
        <Tag color="red" bordered>red bordered</Tag>
        <Tag color="green" bordered>green bordered</Tag>
      </Space>

      {/* 4 种尺寸（lingyang 含 medium，Ant Design 无） */}
      <Space align="center">
        <Tag color="arcoblue" size="small">small</Tag>
        <Tag color="arcoblue" size="default">default</Tag>
        <Tag color="arcoblue" size="medium">medium</Tag>
        <Tag color="arcoblue" size="large">large</Tag>
      </Space>
    </Space>
  );
}
```

## 7. 受控显隐（visible — lingyang 专有）

```jsx
import { useState } from 'react';
import { Tag, Button, Space } from 'lingyang';

// 注意：Ant Design v5 已移除 visible，需自行做条件渲染
// lingyang 支持 visible 受控属性

function VisibleTag() {
  const [visible, setVisible] = useState(true);

  return (
    <Space>
      <Tag
        color="blue"
        closable
        visible={visible}
        onClose={(e) => {
          e.preventDefault();
          setVisible(false);
        }}
      >
        受控标签（可关闭）
      </Tag>

      {!visible && (
        <Button size="small" onClick={() => setVisible(true)}>
          重新显示
        </Button>
      )}
    </Space>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Tag — 完整 TypeScript 接口定义

## TagProps

```typescript
interface TagProps {
  /**
   * 标签颜色。
   * 支持预设色名：'red' | 'orangered' | 'orange' | 'gold' | 'lime' | 'green' |
   *   'cyan' | 'blue' | 'arcoblue' | 'purple' | 'pinkpurple' | 'magenta' | 'gray'
   * 或任意 CSS 颜色值，如 '#f50'、'rgb(0,128,0)'
   */
  color?: string;
  /**
   * 标签尺寸。默认 'default'。
   * 【差异】lingyang 有 'medium'，Ant Design 无此尺寸
   */
  size?: 'small' | 'default' | 'medium' | 'large';
  /**
   * 标签形状。默认 'square'。
   * square=直角，round=圆角胶囊，circle=圆形
   */
  shape?: 'square' | 'round' | 'circle';
  /** 是否显示边框。默认 false */
  bordered?: boolean;
  /**
   * 【lingyang 专有】标签内左侧图标。
   * Ant Design 无此属性，需手动将图标写在 children 内
   */
  icon?: ReactNode;
  /** 是否显示关闭按钮（×）。默认 false */
  closable?: boolean;
  /** 自定义关闭图标，替换默认的 × */
  closeIcon?: ReactNode;
  /**
   * 点击关闭按钮的回调。
   * 调用 e.preventDefault() 可阻止默认关闭行为（配合 visible 受控使用）
   */
  onClose?: (e: MouseEvent) => void;
  /**
   * 受控：标签是否显示。
   * 【差异】lingyang 支持 visible 受控；Ant Design v5 已移除，需自行条件渲染
   */
  visible?: boolean;
  /** 非受控：标签初始是否显示。默认 true */
  defaultVisible?: boolean;
  /**
   * 【lingyang 专有】是否可选中（点击切换选中状态）。默认 false。
   * Ant Design 使用独立组件 <Tag.CheckableTag> 实现
   */
  checkable?: boolean;
  /** 受控：是否选中（需 checkable=true） */
  checked?: boolean;
  /** 非受控：初始是否选中（需 checkable=true）。默认 false */
  defaultChecked?: boolean;
  /** 选中状态变化回调（需 checkable=true） */
  onChange?: (checked: boolean) => void;
  /** 点击标签的回调 */
  onClick?: (e: MouseEvent) => void;
  /** 标签内容 */
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| 可选中 Tag | `checkable` + `checked` + `onChange` 在 `<Tag>` 上配置 | 独立 `<Tag.CheckableTag checked onChange>` 组件 |
| 图标属性 | `icon={<IconStar />}` | ❌ 无，需手动放在 children 里 |
| 尺寸枚举 | small / default / **medium** / large（4 个） | small / default / large（3 个） |
| 受控显隐 | `visible` / `defaultVisible` | ❌ v5 已移除，需条件渲染 |
| 品牌色 | `color="arcoblue"`（专属） | 无 arcoblue |
| 预设色名 | 含 pinkpurple / orangered / arcoblue | 有所不同 |

---
