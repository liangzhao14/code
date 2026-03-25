# lingyang-space · 间距组件 Skill

**渲染**：`<div class="lingyang-space">`（每个子元素被包裹在 `.lingyang-space-item` 中）

---

## 何时读取子文档

| 需求 | 读取文件 |
|---|---|
| 需要完整 TypeScript 类型定义 | `references/props.md` |
| 需要完整代码示例（10 个场景） | `references/examples.md` |

---

## Props 全览

| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `size` | `SpaceSizeType` | `'small'` | 间距大小，见下方尺寸表 |
| `direction` | `'horizontal' \| 'vertical'` | `'horizontal'` | 排列方向 |
| `align` | `'start' \| 'end' \| 'center' \| 'baseline'` | — | 交叉轴对齐（CSS align-items）|
| `wrap` | `boolean` | `false` | 是否自动换行 |
| `split` | `ReactNode` | — | 元素间分隔符 |
| `style` | `CSSProperties` | — | 自定义样式 |
| `className` | `string` | — | 自定义类名 |
| `children` | `ReactNode` | — | 子节点 |

---

## 尺寸预设（lingyang 专有 4 档）

| 枚举值 | 间距 px | 适用场景 |
|---|---|---|
| `mini` | 4px | 极紧凑：图标组、行内标签 |
| `small` | 8px | **默认**：大多数内联元素 |
| `medium` | 16px | 按钮组、工具栏 |
| `large` | 24px | 卡片间距、区块分隔 |
| `{number}` | 自定义 | 任意像素值如 `size={12}` |
| `[h, v]` | 双向自定义 | `size={[8, 16]}` 分别控制水平/垂直 |

---

## 核心约束

1. Space 为每个子元素增加 `.lingyang-space-item` 包裹，不建议在性能敏感场景使用
2. `split` 分隔符只出现在元素**之间**，首尾不渲染
3. `wrap=true` 时**强烈建议**使用 `size={[h, v]}` 数组，分别控制换行前后的间距
4. `direction='vertical'` 时，`align` 控制**水平**对齐（align-items 在 column 方向）
5. 子节点不应为 `null/undefined`，会产生空白占位 item，应在外部过滤

---

## 高频场景速查

### 按钮组（最常用）
```jsx
<Space size="small">
  <Button type="primary">确认</Button>
  <Button>取消</Button>
</Space>
```

### 垂直表单
```jsx
<Space direction="vertical" size="medium" style={{ width: '100%' }}>
  <Input placeholder="用户名" />
  <Input.Password placeholder="密码" />
  <Button type="primary" long>登录</Button>
</Space>
```

### 标签云（自动换行）
```jsx
<Space wrap size={[8, 8]}>
  {tags.map(tag => <Tag key={tag}>{tag}</Tag>)}
</Space>
```

### 分隔符列表
```jsx
<Space split={<Divider type="vertical" />}>
  <span>作者：张三</span>
  <span>发布于 2024-01-01</span>
  <span>阅读 1.2k</span>
</Space>
```

### 混合高度居中对齐
```jsx
<Space align="center" size="medium">
  <Avatar size={48}>张</Avatar>
  <div>
    <div>张三</div>
    <div style={{ color: '#666' }}>高级工程师</div>
  </div>
  <Button type="primary">关注</Button>
</Space>
```

### 工具栏图标组（mini 间距）
```jsx
<Space size="mini" align="center">
  <Button type="text" icon={<IconEdit />} />
  <Button type="text" icon={<IconCopy />} />
  <Button type="text" icon={<IconDelete />} status="danger" />
</Space>
```

---

## CSS 类名速查

| 场景 | 类名 |
|---|---|
| 根节点 | `.lingyang-space` |
| 水平方向 | `.lingyang-space-horizontal` |
| 垂直方向 | `.lingyang-space-vertical` |
| align-center | `.lingyang-space-align-center` |
| align-start | `.lingyang-space-align-start` |
| align-end | `.lingyang-space-align-end` |
| align-baseline | `.lingyang-space-align-baseline` |
| 每个子项 | `.lingyang-space-item` |

---

## Space vs 其他间距方案对比

| 方案 | 适用场景 | 优点 | 缺点 |
|---|---|---|---|
| `Space` | 内联元素等距排列 | 声明式、自动处理换行 | 每个子节点多一层 DOM |
| `Row + Col` | 复杂栅格布局 | 精确列宽控制 | 配置复杂 |
| `CSS gap` | 现代浏览器，简单布局 | 无额外 DOM | 不支持分隔符 |
| `margin` | 个别元素间距 | 精确控制 | 需手动处理首尾 |

> **经验法则**：3 个及以上内联元素等距排列 → 用 `Space`；复杂二维布局 → 用 `Grid`；单个元素偏移 → 用 `margin`
-e 

---

## 完整代码示例

# lingyang-space · 完整代码示例库

## 目录
1. [基础水平间距](#1-基础水平间距)
2. [预设四档尺寸](#2-预设四档尺寸)
3. [自定义间距（数字）](#3-自定义间距数字)
4. [水平+垂直间距元组](#4-水平垂直间距元组--wrap)
5. [垂直排列](#5-垂直排列)
6. [分隔符 split](#6-分隔符-split)
7. [自动换行（标签云）](#7-自动换行标签云)
8. [交叉轴对齐](#8-交叉轴对齐-align)
9. [工具栏图标组](#9-工具栏图标组mini-间距)
10. [嵌套复杂排版](#10-嵌套复杂排版)
11. [企业级场景模板](#11-企业级场景模板)

---

## 1. 基础水平间距

```jsx
import { Space, Button } from 'lingyang';

// 默认 small（8px）水平间距
<Space>
  <Button type="primary">确认</Button>
  <Button>取消</Button>
  <Button type="text">更多操作</Button>
</Space>
```

---

## 2. 预设四档尺寸

```jsx
import { Space, Button, Divider } from 'lingyang';

export default function SizeDemo() {
  const sizes = ['mini', 'small', 'medium', 'large'] as const;

  return (
    <Space direction="vertical" size="large">
      {sizes.map(size => (
        <div key={size}>
          <div style={{ color: '#666', marginBottom: 8, fontSize: 12 }}>
            size="{size}" ({size === 'mini' ? 4 : size === 'small' ? 8 : size === 'medium' ? 16 : 24}px)
          </div>
          <Space size={size}>
            <Button type="primary">Button</Button>
            <Button>Button</Button>
            <Button>Button</Button>
          </Space>
          <Divider style={{ margin: '12px 0' }} />
        </div>
      ))}
    </Space>
  );
}
```

---

## 3. 自定义间距（数字）

```jsx
// 固定 20px 间距
<Space size={20}>
  <Tag color="arcoblue">设计</Tag>
  <Tag color="green">前端</Tag>
  <Tag color="orange">后端</Tag>
</Space>

// 配合 Tokens 使用
const GAP = 12; // 自定义间距常量
<Space size={GAP}>
  <Avatar>A</Avatar>
  <Avatar>B</Avatar>
  <Avatar>C</Avatar>
</Space>
```

---

## 4. 水平+垂直间距元组 + wrap

```jsx
// wrap 时强烈推荐元组形式，分别控制行内间距和行间距
<Space size={[8, 12]} wrap style={{ maxWidth: 400 }}>
  <Tag>JavaScript</Tag>
  <Tag>TypeScript</Tag>
  <Tag>React</Tag>
  <Tag>Vue</Tag>
  <Tag>Node.js</Tag>
  <Tag>Python</Tag>
  <Tag>Go</Tag>
  <Tag>Docker</Tag>
  <Tag>Kubernetes</Tag>
</Space>
```

---

## 5. 垂直排列

```jsx
// 表单竖向堆叠
<Space direction="vertical" size="medium" style={{ width: 300 }}>
  <Input placeholder="用户名" />
  <Input.Password placeholder="密码" />
  <Button type="primary" long>登录</Button>
  <Typography.Text type="secondary" style={{ textAlign: 'center', display: 'block' }}>
    还没有账号？<Typography.Text type="primary">立即注册</Typography.Text>
  </Typography.Text>
</Space>

// 卡片列表竖向排列
<Space direction="vertical" size="medium" style={{ width: '100%' }}>
  <Card>卡片内容 1</Card>
  <Card>卡片内容 2</Card>
  <Card>卡片内容 3</Card>
</Space>
```

---

## 6. 分隔符 split

```jsx
import { Space, Divider, Typography } from 'lingyang';

// 竖线分隔（最常用）
<Space split={<Divider type="vertical" />}>
  <Typography.Text>创建于 2024-01-01</Typography.Text>
  <Typography.Text>修改于 2024-06-15</Typography.Text>
  <Typography.Text>作者：张三</Typography.Text>
</Space>

// 点号分隔
<Space split={<span style={{ color: '#ccc', padding: '0 4px' }}>·</span>}>
  <span>首页</span>
  <span>新闻中心</span>
  <span>行业动态</span>
</Space>

// 斜线分隔（面包屑风格）
<Space split={<span style={{ color: '#86909c' }}>/</span>} size="small">
  <a href="/">工作台</a>
  <a href="/users">用户管理</a>
  <span>用户详情</span>
</Space>
```

---

## 7. 自动换行（标签云）

```jsx
import { useState } from 'react';
import { Space, Tag, Button } from 'lingyang';
import { IconPlus } from 'lingyang/icon';

export default function TagCloud() {
  const [tags, setTags] = useState(['React', 'TypeScript', '设计系统', '前端架构', '组件库', '性能优化']);

  const removeTag = (tag: string) => setTags(t => t.filter(x => x !== tag));

  return (
    <Space wrap size={[8, 8]} style={{ maxWidth: '100%' }}>
      {tags.map(tag => (
        <Tag
          key={tag}
          closable
          onClose={() => removeTag(tag)}
        >
          {tag}
        </Tag>
      ))}
      <Tag
        icon={<IconPlus />}
        style={{ cursor: 'pointer', borderStyle: 'dashed' }}
        onClick={() => {/* 添加标签逻辑 */}}
      >
        添加标签
      </Tag>
    </Space>
  );
}
```

---

## 8. 交叉轴对齐 align

```jsx
// center：混合高度元素垂直居中（最常用）
<Space align="center" size="medium">
  <Avatar size={48} style={{ background: '#13AE68' }}>张</Avatar>
  <div>
    <div style={{ fontWeight: 600, marginBottom: 4 }}>张三</div>
    <div style={{ color: '#86909c', fontSize: 12 }}>高级前端工程师</div>
  </div>
  <Button type="primary" size="small">关注</Button>
</Space>

// baseline：文字和图标混排时基线对齐
<Space align="baseline" size="small">
  <Typography.Title heading={4} style={{ margin: 0 }}>¥12,580</Typography.Title>
  <Typography.Text type="secondary">元 / 月</Typography.Text>
</Space>

// start：顶部对齐（适合内容高度差异大的场景）
<Space align="start" size="large">
  <Card style={{ width: 160 }}>
    <Typography.Title heading={6}>简短标题</Typography.Title>
  </Card>
  <Card style={{ width: 160 }}>
    <Typography.Title heading={6}>这是一个很长的多行标题文字内容</Typography.Title>
    <Typography.Text type="secondary">附加描述</Typography.Text>
  </Card>
</Space>
```

---

## 9. 工具栏图标组（mini 间距）

```jsx
import { Space, Button, Tooltip } from 'lingyang';
import { IconEdit, IconCopy, IconDelete, IconMore } from 'lingyang/icon';

// 表格行操作栏
function TableActions({ record }: { record: any }) {
  return (
    <Space size="mini" align="center">
      <Tooltip content="编辑">
        <Button
          type="text"
          icon={<IconEdit />}
          onClick={() => handleEdit(record)}
        />
      </Tooltip>
      <Tooltip content="复制">
        <Button
          type="text"
          icon={<IconCopy />}
          onClick={() => handleCopy(record)}
        />
      </Tooltip>
      <Tooltip content="删除">
        <Button
          type="text"
          icon={<IconDelete />}
          status="danger"
          onClick={() => handleDelete(record)}
        />
      </Tooltip>
    </Space>
  );
}
```

---

## 10. 嵌套复杂排版

```jsx
// 卡片头部：左侧标题 + 右侧操作按钮
<Space
  style={{ width: '100%', justifyContent: 'space-between' }}
  align="center"
>
  <Space align="center" size="small">
    <IconBarChart style={{ fontSize: 18, color: '#13AE68' }} />
    <Typography.Title heading={6} style={{ margin: 0 }}>数据概览</Typography.Title>
    <Tag color="green" size="small">实时</Tag>
  </Space>
  <Space size="small">
    <Button size="small" icon={<IconDownload />}>导出</Button>
    <Button type="primary" size="small" icon={<IconRefresh />}>刷新</Button>
  </Space>
</Space>
```

---

## 11. 企业级场景模板

### 表格操作列（带 Divider）
```jsx
// 表格 columns 操作列的 render 函数
{
  title: '操作',
  render: (_, record) => (
    <Space split={<Divider type="vertical" />} size={0}>
      <Typography.Text
        type="primary"
        style={{ cursor: 'pointer' }}
        onClick={() => handleView(record)}
      >
        查看
      </Typography.Text>
      <Typography.Text
        type="primary"
        style={{ cursor: 'pointer' }}
        onClick={() => handleEdit(record)}
      >
        编辑
      </Typography.Text>
      <Typography.Text
        type="danger"
        style={{ cursor: 'pointer' }}
        onClick={() => handleDelete(record)}
      >
        删除
      </Typography.Text>
    </Space>
  )
}
```

### 搜索过滤 Tag 组
```jsx
// 已选过滤条件展示
<Space wrap size={[8, 8]} align="center">
  <Typography.Text type="secondary">已筛选：</Typography.Text>
  {activeFilters.map(filter => (
    <Tag
      key={filter.key}
      closable
      color="arcoblue"
      onClose={() => removeFilter(filter.key)}
    >
      {filter.label}：{filter.value}
    </Tag>
  ))}
  {activeFilters.length > 0 && (
    <Button type="text" size="mini" onClick={clearAllFilters}>
      清除全部
    </Button>
  )}
</Space>
```

### 用户信息展示行
```jsx
// 个人资料页：头像 + 信息 + 操作
<Space align="center" size="large">
  <Avatar size={64} src={user.avatar}>
    {user.name[0]}
  </Avatar>
  <Space direction="vertical" size="mini">
    <Space align="baseline" size="small">
      <Typography.Title heading={5} style={{ margin: 0 }}>
        {user.name}
      </Typography.Title>
      <Tag color={user.isVip ? 'gold' : 'gray'}>
        {user.isVip ? 'VIP' : '普通用户'}
      </Tag>
    </Space>
    <Space split={<Divider type="vertical" />} size={0}>
      <Typography.Text type="secondary">{user.dept}</Typography.Text>
      <Typography.Text type="secondary">{user.position}</Typography.Text>
      <Typography.Text type="secondary">{user.email}</Typography.Text>
    </Space>
  </Space>
  <Space size="small">
    <Button>发消息</Button>
    <Button type="primary">编辑资料</Button>
  </Space>
</Space>
```

### 底部操作栏（表单提交区）
```jsx
// 表单底部固定操作栏
<div style={{
  position: 'sticky',
  bottom: 0,
  background: '#fff',
  padding: '16px 24px',
  borderTop: '1px solid #f0f0f0',
  display: 'flex',
  justifyContent: 'flex-end'
}}>
  <Space size="small">
    <Button onClick={handleReset}>重置</Button>
    <Button onClick={handleSaveDraft}>保存草稿</Button>
    <Button type="primary" loading={submitting} onClick={handleSubmit}>
      提交审核
    </Button>
  </Space>
</div>
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-space · 完整 Props 类型定义

---

## 类型别名

```typescript
// 预设尺寸枚举（lingyang 专有 4 档，比 Ant Design 多 mini 档）
type SpaceSizeEnum = 'mini' | 'small' | 'medium' | 'large';
// 对应 px 值：mini=4, small=8, medium=16, large=24

// 单方向尺寸：枚举或自定义 px
type SpaceSizeValue = SpaceSizeEnum | number;

// 完整尺寸类型：单值 或 [水平, 垂直] 元组
type SpaceSizeType = SpaceSizeValue | [SpaceSizeValue, SpaceSizeValue];
```

---

## SpaceProps

```typescript
interface SpaceProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * 间距大小。
   *
   * 三种写法：
   * 1. 预设枚举：'mini'(4px) | 'small'(8px) | 'medium'(16px) | 'large'(24px)
   * 2. 自定义数字（px）：如 size={12} = 12px 间距
   * 3. [水平, 垂直] 元组：如 size={[8, 16]} = 水平 8px、垂直 16px
   *    ← 使用 wrap={true} 时强烈推荐元组形式
   *
   * @default 'small'  // 8px
   */
  size?: SpaceSizeType;

  /**
   * 排列方向。
   * 'horizontal': 水平排列（flex-direction: row），子元素左右并列
   * 'vertical':   垂直排列（flex-direction: column），子元素上下堆叠
   *
   * @default 'horizontal'
   */
  direction?: 'horizontal' | 'vertical';

  /**
   * 交叉轴对齐方式（CSS align-items）。
   * - horizontal 方向时：控制子元素的垂直对齐
   * - vertical 方向时：控制子元素的水平对齐
   *
   * 'start':    flex-start，靠上/靠左
   * 'end':      flex-end，靠下/靠右
   * 'center':   居中对齐（混合高度时最常用）
   * 'baseline': 基线对齐（文字和图标混排时推荐）
   *
   * 不设置时默认 stretch（子元素拉伸填满交叉轴）
   */
  align?: 'start' | 'end' | 'center' | 'baseline';

  /**
   * 是否自动换行（flex-wrap: wrap）。
   * true 时子元素超出容器宽度自动折行。
   * 推荐配合 size={[h, v]} 分别控制水平和垂直间距。
   *
   * @default false
   */
  wrap?: boolean;

  /**
   * 分隔符节点。
   * 在每两个相邻子元素之间插入，不出现在首尾。
   * 分隔符由 Space 内部处理对齐，无需额外样式。
   *
   * 常见用法：
   * - split={<Divider type="vertical" />}  // 竖线分隔
   * - split={<span style={{ color: '#ccc' }}>·</span>}
   * - split={<span>/</span>}
   */
  split?: ReactNode;

  /** 自定义内联样式（React CSSProperties） */
  style?: CSSProperties;

  /** 自定义 CSS 类名 */
  className?: string;

  /**
   * 子节点。
   * 每个子节点被 Space 包裹在 .lingyang-space-item 中。
   * 注意：不应传入 null/undefined（会产生空 item），请在外部过滤：
   * {condition && <Button>按钮</Button>}
   */
  children?: ReactNode;
}
```

---

## 尺寸预设值对照

| SpaceSizeEnum | px 值 | 等价写法 | 适用场景 |
|---|---|---|---|
| `'mini'` | 4px | `size={4}` | 极紧凑场景：图标按钮组、行内标签内部间距 |
| `'small'` | 8px | `size={8}` | **默认值**，大多数内联元素间距 |
| `'medium'` | 16px | `size={16}` | 按钮组、工具栏、操作区 |
| `'large'` | 24px | `size={24}` | 卡片间距、内容区块分隔 |

> lingyang 的 `mini`（4px）是相对 Ant Design 的专属扩展档位，Ant Design 只有 small/middle/large 三档。

---

## 内部 DOM 结构

```html
<!-- <Space size="small"> <Button>A</Button> <Button>B</Button> </Space> -->
<div class="lingyang-space lingyang-space-horizontal lingyang-space-align-center"
     style="column-gap: 8px; row-gap: 8px;">
  <div class="lingyang-space-item">
    <!-- Button A -->
  </div>
  <div class="lingyang-space-item">
    <!-- Button B -->
  </div>
</div>
```

**注意**：每个子节点多一层 `.lingyang-space-item` div 包裹。在以下场景需注意：
- 子节点使用 `:first-child` / `:last-child` CSS 选择器时会失效（需改用 `.lingyang-space-item:first-child > *`）
- 对 DOM 层级有严格要求时，考虑直接使用 CSS gap 方案

---

## 与 SpaceItem（内部实现细节）

`Space` 不对外暴露 `Space.Item`，内部包裹层通过 `React.Children.map` 自动生成。若需要单独控制某个子元素的间距，可以直接给子元素添加 `style={{ marginRight/marginBottom }}` 覆盖。

---
