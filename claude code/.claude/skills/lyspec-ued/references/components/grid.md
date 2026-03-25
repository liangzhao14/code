# lingyang-grid · 栅格布局组件 Skill

**来源**: 羚羊设计系统 Grid 组件  
**覆盖组件**: `Row` · `Col` · `Grid` · `Grid.Item`  
**版本说明**: `Grid / Grid.Item` 为自适应布局 API（v2.36+），`Row / Col` 为经典 24 列栅格 API

---

## 何时读取子文档

| 场景 | 读取 |
|---|---|
| 需要完整 Props 类型定义或枚举值 | `references/props.md` |
| 需要完整代码示例（含响应式、企业场景） | `references/examples.md` |
| 需要断点系统详细说明 | `references/breakpoints.md` |

---

## 组件选型决策

```
需要布局？
│
├─ 需要响应式自动均分（等宽卡片、列表）
│   └─ 用 Grid + Grid.Item     ← cols / colGap / rowGap / span / suffix
│
└─ 需要精确的 24 列比例控制
    └─ 用 Row + Col             ← gutter / justify / align / span / offset / push / pull / flex
```

---

## 核心约束规则（生成代码时必须遵守）

1. `Col` 必须是 `Row` 的**直接子节点**，不能脱离 `Row` 单独使用
2. 单行所有 `Col` 的 `span` 之和**超过 24** 时，超出部分自动换行（需 `Row wrap={true}`）
3. `offset` 不计入 `span` 之和，但 `offset + span` 超过 24 同样触发换行
4. `push / pull` 只改变**视觉位置**，不改变 DOM 顺序；`order` 通过 CSS flex order 改变视觉顺序
5. 响应式属性（`xs/sm/md/lg/xl/xxl`）**后者覆盖前者**，未设置的断点继承上一个已设置的值
6. `Grid / Grid.Item` 不依赖 24 列，`cols` 可自由设定（如 2、3、4、12 等）
7. `Grid.Item suffix={true}` 时自动推送到行末，无需手动计算 `offset`

---

## Props 快速参考

### Row
| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `gutter` | `number \| [h,v] \| {xs..xxl}` | `0` | 列间距（推荐 8n+8 系列） |
| `justify` | `'start'\|'end'\|'center'\|'space-around'\|'space-between'\|'space-evenly'` | `'start'` | 水平对齐 |
| `align` | `'start'\|'end'\|'center'\|'stretch'\|'baseline'` | `'stretch'` | 垂直对齐 |
| `wrap` | `boolean` | `true` | 是否允许换行 |
| `div` | `boolean` | `false` | 渲染为普通 div（禁用 flex） |

### Col
| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `span` | `1-24 \| 'auto'` | — | 列宽跨度 |
| `offset` | `0-23` | `0` | 向右偏移列数 |
| `push` | `0-23` | `0` | 向右视觉偏移 |
| `pull` | `0-23` | `0` | 向左视觉偏移 |
| `order` | `number` | `0` | flex order，越小越靠前 |
| `flex` | `number \| string` | — | CSS flex 值（如 `1`、`'200px'`、`'auto'`） |
| `xs/sm/md/lg/xl/xxl` | `number \| {span,offset,push,pull,order}` | — | 响应式配置 |

### Grid
| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `cols` | `number \| {xs..xxl}` | `24` | 每行列数 |
| `colGap` | `number \| string \| {xs..xxl}` | `0` | 列间距 |
| `rowGap` | `number \| string \| {xs..xxl}` | `0` | 行间距 |

### Grid.Item
| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `span` | `number \| {xs..xxl}` | `1` | 占据列数（相对于父 Grid.cols） |
| `offset` | `number \| {xs..xxl}` | `0` | 偏移列数 |
| `suffix` | `boolean` | `false` | 是否推送到行末 |

---

## 高频场景代码模板

### 1 · 等宽 N 列（24列）
```jsx
// 三等列
<Row gutter={16}>
  <Col span={8}>内容</Col>
  <Col span={8}>内容</Col>
  <Col span={8}>内容</Col>
</Row>
```

### 2 · 响应式：手机单列 → 平板双列 → 桌面四列
```jsx
<Row gutter={[16, 16]}>
  <Col xs={24} sm={12} lg={6}>卡片</Col>
  <Col xs={24} sm={12} lg={6}>卡片</Col>
  <Col xs={24} sm={12} lg={6}>卡片</Col>
  <Col xs={24} sm={12} lg={6}>卡片</Col>
</Row>
```

### 3 · 主侧栏布局
```jsx
<Row gutter={24}>
  <Col xs={24} lg={18}>主内容区</Col>
  <Col xs={24} lg={6}>侧边栏</Col>
</Row>
```

### 4 · 表单两列布局
```jsx
<Row gutter={[24, 16]}>
  <Col xs={24} md={12}><Form.Item /></Col>
  <Col xs={24} md={12}><Form.Item /></Col>
</Row>
```

### 5 · Flex 弹性分配
```jsx
<Row>
  <Col flex={1}>自动填充</Col>
  <Col flex="200px">固定 200px</Col>
  <Col flex={2}>占比 2</Col>
</Row>
```

### 6 · Grid 自适应卡片网格（推荐用于 Dashboard）
```jsx
<Grid cols={{ xs: 1, sm: 2, md: 3, lg: 4 }} colGap={16} rowGap={16}>
  <Grid.Item>卡片</Grid.Item>
  <Grid.Item span={2}>宽卡片（占 2 列）</Grid.Item>
  <Grid.Item suffix>右对齐操作项</Grid.Item>
</Grid>
```

### 7 · push / pull 调换视觉顺序（SEO 友好）
```jsx
<Row>
  <Col span={18} push={6}>主内容（DOM 在前）</Col>
  <Col span={6} pull={18}>侧边栏（视觉在前）</Col>
</Row>
```

---

## 引入方式

```jsx
// Row / Col
import { Row, Col } from 'lingyang';

// Grid / Grid.Item
import { Grid } from 'lingyang';
const { Item } = Grid;
// 或直接用 <Grid.Item>
```

---

## 可访问性注意事项

- `Row / Col` 为纯布局容器，**不添加任何 ARIA 属性**，无语义角色
- `push / pull` 改变视觉顺序但**不改变 DOM 顺序**，Tab 焦点仍按 DOM 顺序，需注意键盘可访问性
- `order` 属性同样只影响视觉顺序，屏幕阅读器按 DOM 顺序读取
-e 

---

## 完整代码示例

# lingyang-grid · 完整代码示例库

> 按场景分类，涵盖基础用法到企业级复杂布局。

---

## 一、基础栅格（Row + Col）

### 1.1 基础等宽布局
```jsx
// 三等列（各占 1/3）
<Row>
  <Col span={8}><div className="demo-col">col-8</div></Col>
  <Col span={8}><div className="demo-col">col-8</div></Col>
  <Col span={8}><div className="demo-col">col-8</div></Col>
</Row>

// 四等列（各占 1/4）
<Row>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
</Row>
```

### 1.2 不等宽布局
```jsx
// 黄金比例分割
<Row>
  <Col span={16}><div className="demo-col">col-16（主内容）</div></Col>
  <Col span={8}><div className="demo-col">col-8（侧边栏）</div></Col>
</Row>

// 二八分割
<Row>
  <Col span={4}><div className="demo-col">col-4（导航）</div></Col>
  <Col span={20}><div className="demo-col">col-20（内容）</div></Col>
</Row>
```

---

## 二、间距（gutter）

### 2.1 水平间距
```jsx
<Row gutter={16}>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
</Row>
```

### 2.2 水平 + 垂直间距
```jsx
<Row gutter={[16, 24]}>
  <Col span={12}><div className="demo-col">col-12</div></Col>
  <Col span={12}><div className="demo-col">col-12</div></Col>
  <Col span={12}><div className="demo-col">col-12</div></Col>
  <Col span={12}><div className="demo-col">col-12</div></Col>
</Row>
```

### 2.3 响应式间距
```jsx
<Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32, xl: 40 }}>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
  <Col span={6}><div className="demo-col">col-6</div></Col>
</Row>
```

---

## 三、对齐（justify / align）

### 3.1 水平对齐
```jsx
// 居中
<Row justify="center" gutter={16}>
  <Col span={4}>center</Col>
</Row>

// 两端对齐
<Row justify="space-between" gutter={16}>
  <Col span={4}>left</Col>
  <Col span={4}>center</Col>
  <Col span={4}>right</Col>
</Row>

// 均匀间距
<Row justify="space-around">
  <Col span={4}>item</Col>
  <Col span={4}>item</Col>
  <Col span={4}>item</Col>
</Row>
```

### 3.2 垂直对齐
```jsx
// 顶部对齐（默认 stretch）
<Row align="start" style={{ height: 80, background: '#f2f3f5' }}>
  <Col span={6}><div style={{ height: 40 }}>top</div></Col>
  <Col span={6}><div style={{ height: 60 }}>tall</div></Col>
</Row>

// 居中对齐
<Row align="center" style={{ height: 80, background: '#f2f3f5' }}>
  <Col span={6}>middle</Col>
  <Col span={6}>middle</Col>
</Row>

// 底部对齐
<Row align="end" style={{ height: 80, background: '#f2f3f5' }}>
  <Col span={6}>bottom</Col>
  <Col span={6}>bottom</Col>
</Row>
```

---

## 四、偏移与排序

### 4.1 列偏移（offset）
```jsx
<Row>
  <Col span={8}>col-8</Col>
  <Col span={8} offset={8}>col-8 offset-8（左边空出 8 列）</Col>
</Row>

<Row>
  <Col span={6} offset={6}>col-6 offset-6</Col>
  <Col span={6} offset={6}>col-6 offset-6</Col>
</Row>
```

### 4.2 push / pull（调换视觉顺序，保持 DOM 顺序）
```jsx
// SEO 友好：主内容在 DOM 前面，但侧边栏视觉上在左
<Row>
  <Col span={18} push={6}>
    <div className="demo-col">主内容（DOM 第一位，视觉右侧）</div>
  </Col>
  <Col span={6} pull={18}>
    <div className="demo-col">侧边栏（DOM 第二位，视觉左侧）</div>
  </Col>
</Row>
```

### 4.3 order（Flex 排序）
```jsx
// 响应式调换顺序
<Row>
  <Col span={6} xs={{ order: 4 }} lg={{ order: 1 }}>1</Col>
  <Col span={6} xs={{ order: 3 }} lg={{ order: 2 }}>2</Col>
  <Col span={6} xs={{ order: 2 }} lg={{ order: 3 }}>3</Col>
  <Col span={6} xs={{ order: 1 }} lg={{ order: 4 }}>4</Col>
</Row>
```

---

## 五、Flex 弹性布局

### 5.1 flex 属性
```jsx
// 比例分配
<Row>
  <Col flex={2}>占 2/5</Col>
  <Col flex={3}>占 3/5</Col>
</Row>

// 固定 + 自动填充
<Row>
  <Col flex="120px">固定 120px</Col>
  <Col flex={1}>自动填充剩余</Col>
  <Col flex="80px">固定 80px</Col>
</Row>

// 内容自适应
<Row>
  <Col flex="auto">自适应内容宽度</Col>
  <Col flex={1}>填充剩余</Col>
</Row>
```

---

## 六、响应式布局

### 6.1 基础响应式（简写）
```jsx
<Row gutter={[16, 16]}>
  {/* 手机1列 → 平板2列 → 桌面4列 */}
  <Col xs={24} sm={12} lg={6}>卡片 1</Col>
  <Col xs={24} sm={12} lg={6}>卡片 2</Col>
  <Col xs={24} sm={12} lg={6}>卡片 3</Col>
  <Col xs={24} sm={12} lg={6}>卡片 4</Col>
</Row>
```

### 6.2 断点内嵌对象（细粒度控制）
```jsx
<Row>
  <Col
    xs={{ span: 24 }}
    sm={{ span: 12, offset: 0 }}
    md={{ span: 8, offset: 2 }}
    lg={{ span: 6, offset: 1 }}
  >
    带断点细粒度控制的列
  </Col>
</Row>
```

### 6.3 响应式 + 排序
```jsx
<Row>
  <Col xs={{ span: 24, order: 2 }} lg={{ span: 18, order: 1 }}>
    主内容（移动端在下方）
  </Col>
  <Col xs={{ span: 24, order: 1 }} lg={{ span: 6, order: 2 }}>
    摘要卡片（移动端在上方）
  </Col>
</Row>
```

---

## 七、Grid 自适应布局（新 API）

### 7.1 等宽自适应网格
```jsx
// 固定 3 列
<Grid cols={3} colGap={16} rowGap={16}>
  <Grid.Item>卡片 1</Grid.Item>
  <Grid.Item>卡片 2</Grid.Item>
  <Grid.Item>卡片 3</Grid.Item>
  <Grid.Item>卡片 4</Grid.Item>
</Grid>
```

### 7.2 响应式自适应网格
```jsx
<Grid
  cols={{ xs: 1, sm: 2, md: 3, lg: 4, xl: 4 }}
  colGap={16}
  rowGap={16}
>
  {list.map(item => (
    <Grid.Item key={item.id}>
      <StatCard {...item} />
    </Grid.Item>
  ))}
</Grid>
```

### 7.3 Grid.Item span 跨列
```jsx
<Grid cols={4} colGap={16} rowGap={16}>
  <Grid.Item>1列宽</Grid.Item>
  <Grid.Item span={2}>2列宽（横跨 2 列）</Grid.Item>
  <Grid.Item>1列宽</Grid.Item>
  <Grid.Item span={4}>通栏（横跨全部 4 列）</Grid.Item>
</Grid>
```

### 7.4 Grid.Item suffix 右对齐
```jsx
// 搜索表单：条件在左，按钮组在右
<Grid cols={4} colGap={16}>
  <Grid.Item><Input placeholder="关键词" /></Grid.Item>
  <Grid.Item><Select placeholder="状态" /></Grid.Item>
  <Grid.Item><DatePicker placeholder="日期" /></Grid.Item>
  <Grid.Item suffix>
    <Space>
      <Button type="primary">搜索</Button>
      <Button>重置</Button>
    </Space>
  </Grid.Item>
</Grid>
```

---

## 八、企业级场景模板

### 8.1 后台管理页面标准布局
```jsx
// 顶部搜索区 + 下方表格
<>
  {/* 搜索条件区 */}
  <Card style={{ marginBottom: 16 }}>
    <Row gutter={[16, 16]}>
      <Col xs={24} sm={12} md={8} lg={6}>
        <Input placeholder="名称" />
      </Col>
      <Col xs={24} sm={12} md={8} lg={6}>
        <Select placeholder="状态" style={{ width: '100%' }} />
      </Col>
      <Col xs={24} sm={12} md={8} lg={6}>
        <RangePicker style={{ width: '100%' }} />
      </Col>
      <Col xs={24} sm={12} md={8} lg={6}>
        <Space>
          <Button type="primary" icon={<IconSearch />}>搜索</Button>
          <Button icon={<IconRefresh />}>重置</Button>
        </Space>
      </Col>
    </Row>
  </Card>

  {/* 数据表格 */}
  <Table columns={columns} data={data} />
</>
```

### 8.2 Dashboard 统计卡片
```jsx
<Grid
  cols={{ xs: 1, sm: 2, lg: 4 }}
  colGap={16}
  rowGap={16}
  style={{ marginBottom: 24 }}
>
  <Grid.Item>
    <StatCard title="总用户" value={12580} trend={+8.5} />
  </Grid.Item>
  <Grid.Item>
    <StatCard title="本月收入" value="¥156,800" trend={+12.3} />
  </Grid.Item>
  <Grid.Item>
    <StatCard title="待处理工单" value={42} trend={-3.2} />
  </Grid.Item>
  <Grid.Item>
    <StatCard title="系统可用率" value="99.95%" trend={+0.1} />
  </Grid.Item>
</Grid>
```

### 8.3 详情页面双栏布局
```jsx
<Row gutter={24}>
  {/* 左侧主信息 */}
  <Col xs={24} lg={16}>
    <Card title="基本信息" style={{ marginBottom: 16 }}>
      <Row gutter={[16, 16]}>
        <Col span={12}>
          <Descriptions.Item label="姓名">张三</Descriptions.Item>
        </Col>
        <Col span={12}>
          <Descriptions.Item label="部门">技术部</Descriptions.Item>
        </Col>
      </Row>
    </Card>
    <Card title="操作记录">
      <Table columns={logColumns} data={logs} />
    </Card>
  </Col>

  {/* 右侧附属信息 */}
  <Col xs={24} lg={8}>
    <Card title="状态信息" style={{ marginBottom: 16 }}>
      <Statistic title="当前状态" value="正常" />
    </Card>
    <Card title="快捷操作">
      <Space direction="vertical" style={{ width: '100%' }}>
        <Button type="primary" long>编辑信息</Button>
        <Button long>查看报表</Button>
        <Button status="danger" long>停用账号</Button>
      </Space>
    </Card>
  </Col>
</Row>
```

### 8.4 多级表单（复杂信息录入）
```jsx
<Form layout="vertical">
  {/* 第一区块：基本信息 */}
  <Card title="基本信息" style={{ marginBottom: 16 }}>
    <Row gutter={[24, 0]}>
      <Col xs={24} md={12} lg={8}>
        <Form.Item label="姓名" field="name" rules={[{ required: true }]}>
          <Input placeholder="请输入姓名" />
        </Form.Item>
      </Col>
      <Col xs={24} md={12} lg={8}>
        <Form.Item label="手机号" field="phone">
          <Input placeholder="请输入手机号" />
        </Form.Item>
      </Col>
      <Col xs={24} md={12} lg={8}>
        <Form.Item label="邮箱" field="email">
          <Input placeholder="请输入邮箱" />
        </Form.Item>
      </Col>
      <Col xs={24} md={12}>
        <Form.Item label="所属部门" field="dept">
          <TreeSelect placeholder="请选择部门" />
        </Form.Item>
      </Col>
      <Col xs={24} md={12}>
        <Form.Item label="职位" field="position">
          <Select placeholder="请选择职位" />
        </Form.Item>
      </Col>
    </Row>
  </Card>

  {/* 第二区块：地址信息 */}
  <Card title="地址信息">
    <Row gutter={[24, 0]}>
      <Col xs={24} sm={12} md={8}>
        <Form.Item label="省份" field="province">
          <Select placeholder="请选择省份" />
        </Form.Item>
      </Col>
      <Col xs={24} sm={12} md={8}>
        <Form.Item label="城市" field="city">
          <Select placeholder="请选择城市" />
        </Form.Item>
      </Col>
      <Col xs={24} sm={12} md={8}>
        <Form.Item label="区县" field="district">
          <Select placeholder="请选择区县" />
        </Form.Item>
      </Col>
      <Col xs={24}>
        <Form.Item label="详细地址" field="address">
          <Input.TextArea placeholder="请输入详细地址" />
        </Form.Item>
      </Col>
    </Row>
  </Card>
</Form>
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-grid · 完整 Props 类型定义

> 本文档包含所有组件的完整 Props 类型、枚举值、类型别名定义。

---

## 类型别名（Type Aliases）

### `ColSpanType`
```typescript
type ColSpanType = number | 'auto';
// number: 1-24 的整数，表示占 24 列中的几列
// 'auto': 由内容宽度决定，不参与 24 列计算
```

### `ColResponsiveObject`
```typescript
interface ColResponsiveObject {
  span?:   ColSpanType;   // 该断点下的列宽
  offset?: number;        // 该断点下向右偏移列数（0-23）
  push?:   number;        // 该断点下向右视觉偏移（0-23）
  pull?:   number;        // 该断点下向左视觉偏移（0-23）
  order?:  number;        // 该断点下排列顺序（>=0，越小越前）
}
```

### `GutterType`
```typescript
type ResponsiveObject = {
  xs?:  number;
  sm?:  number;
  md?:  number;
  lg?:  number;
  xl?:  number;
  xxl?: number;
};

type GutterType =
  | number                          // 纯水平间距，如 16
  | [number | ResponsiveObject,     // [水平间距, 垂直间距]
     number | ResponsiveObject]
  | ResponsiveObject;               // 响应式水平间距
```

---

## RowProps

```typescript
interface RowProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * 栅格间距
   * 推荐使用 (16+8n)px 系列数值，如 8、16、24、32
   * 支持三种形式：
   *   - number: 仅水平间距
   *   - [h, v]: 水平 + 垂直间距
   *   - ResponsiveObject: 响应式水平间距
   * @default 0
   */
  gutter?: GutterType;

  /**
   * 水平对齐方式 → CSS justify-content
   * @default 'start'
   */
  justify?: 'start' | 'end' | 'center' | 'space-around' | 'space-between' | 'space-evenly';

  /**
   * 垂直对齐方式 → CSS align-items
   * @default 'stretch'
   */
  align?: 'start' | 'end' | 'center' | 'stretch' | 'baseline';

  /**
   * 是否允许折行
   * false = 单行模式，超出不换行
   * @default true
   */
  wrap?: boolean;

  /**
   * 渲染为普通 div（禁用 flex 栅格行为）
   * @default false
   */
  div?: boolean;

  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

---

## ColProps

```typescript
interface ColProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * 列宽跨度，1-24 或 'auto'
   * span={8} → 占 8/24 = 1/3 宽度
   * 不设置时继承父级或为 auto
   */
  span?: ColSpanType;

  /**
   * 向右偏移列数（左 margin），0-23
   * 不计入 span 之和，但 span+offset 超过 24 会触发换行
   * @default 0
   */
  offset?: number;

  /**
   * 向右视觉偏移（position relative + left），0-23
   * 不改变 DOM 顺序，配合 pull 调换列视觉位置
   * @default 0
   */
  push?: number;

  /**
   * 向左视觉偏移（position relative + right），0-23
   * @default 0
   */
  pull?: number;

  /**
   * Flex order，越小越靠前
   * 仅影响视觉顺序，不改变 DOM 顺序
   * @default 0
   */
  order?: number;

  /**
   * CSS flex 属性（直接设置 flex 比例或宽度）
   * 设置后 span 失效
   * 示例: flex={1} | flex="200px" | flex="auto" | flex="none" | flex="50%"
   */
  flex?: number | string;

  /** 屏幕 < 576px（手机竖屏）时的列配置 */
  xs?: number | ColResponsiveObject;

  /** 屏幕 ≥ 576px（手机横屏）时的列配置 */
  sm?: number | ColResponsiveObject;

  /** 屏幕 ≥ 768px（平板）时的列配置 */
  md?: number | ColResponsiveObject;

  /** 屏幕 ≥ 992px（小桌面）时的列配置 */
  lg?: number | ColResponsiveObject;

  /** 屏幕 ≥ 1200px（标准桌面）时的列配置 */
  xl?: number | ColResponsiveObject;

  /** 屏幕 ≥ 1600px（大屏桌面）时的列配置 */
  xxl?: number | ColResponsiveObject;

  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

---

## GridProps

```typescript
interface GridProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * 每行列数
   * 支持固定数值或响应式对象
   * Grid.Item 的 span 基于此值计算
   * @default 24
   */
  cols?: number | {
    xs?: number;
    sm?: number;
    md?: number;
    lg?: number;
    xl?: number;
    xxl?: number;
  };

  /**
   * 列间距（水平方向）
   * 支持: number | CSS字符串 | 响应式对象
   * @default 0
   */
  colGap?: number | string | {
    xs?: number; sm?: number; md?: number;
    lg?: number; xl?: number; xxl?: number;
  };

  /**
   * 行间距（垂直方向）
   * 语法同 colGap
   * @default 0
   */
  rowGap?: number | string | {
    xs?: number; sm?: number; md?: number;
    lg?: number; xl?: number; xxl?: number;
  };

  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

---

## GridItemProps

```typescript
interface GridItemProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * 占据的列数（相对于父 Grid 的 cols）
   * 示例: Grid cols={4}, Item span={2} → 占 50% 宽度
   * 支持响应式对象
   * @default 1
   */
  span?: number | {
    xs?: number; sm?: number; md?: number;
    lg?: number; xl?: number; xxl?: number;
  };

  /**
   * 向右偏移的列数（相对于父 Grid 的 cols）
   * 支持响应式对象
   * @default 0
   */
  offset?: number | {
    xs?: number; sm?: number; md?: number;
    lg?: number; xl?: number; xxl?: number;
  };

  /**
   * 是否为尾部元素（自动右对齐到行末）
   * 常用于在搜索表单中将"搜索/重置"按钮固定到右侧
   * @default false
   */
  suffix?: boolean;

  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

---

## CSS 类名参考

| 组件 | 根节点类名 | 示例子类名 |
|---|---|---|
| Row | `.lingyang-row` | `.lingyang-row-rtl` |
| Col | `.lingyang-col` | `.lingyang-col-8`、`.lingyang-col-offset-4` |
| Grid | `.lingyang-grid` | — |
| Grid.Item | `.lingyang-grid-item` | `.lingyang-grid-item-suffix` |
-e 

---

## 断点系统详细说明

# lingyang-grid · 响应式断点系统

---

## 断点定义表

| 断点 | 变量名 | 宽度范围 | 典型设备 | 建议列数 |
|---|---|---|---|---|
| `xs` | `--breakpoint-xs` | `< 576px` | 手机竖屏 | 1 列（span=24） |
| `sm` | `--breakpoint-sm` | `≥ 576px` | 手机横屏、小平板 | 2 列（span=12） |
| `md` | `--breakpoint-md` | `≥ 768px` | 平板竖屏 | 2-3 列 |
| `lg` | `--breakpoint-lg` | `≥ 992px` | 小桌面、平板横屏 | 3-4 列 |
| `xl` | `--breakpoint-xl` | `≥ 1200px` | 标准桌面 | 4-6 列 |
| `xxl` | `--breakpoint-xxl` | `≥ 1600px` | 大屏桌面、外接显示器 | 6+ 列 |

---

## 断点继承规则

响应式属性按从小到大的断点**后者覆盖前者**，未设置的断点**向上继承**最近一个已设置的值。

```jsx
// 示例：只设置了 xs 和 lg
<Col xs={24} lg={8}>

// 等价于：
// xs  (< 576px)  → span=24（手机：单列）
// sm  (≥ 576px)  → span=24（继承 xs）
// md  (≥ 768px)  → span=24（继承 xs）
// lg  (≥ 992px)  → span=8（新设置）
// xl  (≥ 1200px) → span=8（继承 lg）
// xxl (≥ 1600px) → span=8（继承 lg）
```

---

## 媒体查询 CSS 变量

```css
/* 可在项目 CSS 中通过媒体查询使用 */
@media (max-width: 575px)   { /* xs */ }
@media (min-width: 576px)   { /* sm */ }
@media (min-width: 768px)   { /* md */ }
@media (min-width: 992px)   { /* lg */ }
@media (min-width: 1200px)  { /* xl */ }
@media (min-width: 1600px)  { /* xxl */ }
```

---

## 常见响应式布局配方

### 内容卡片网格

| 断点 | 每行列数 | Col span |
|---|---|---|
| xs (手机) | 1 | 24 |
| sm (小屏) | 2 | 12 |
| md (平板) | 2 | 12 |
| lg (小桌面) | 3 | 8 |
| xl (标准) | 4 | 6 |
| xxl (大屏) | 6 | 4 |

```jsx
<Row gutter={[16, 16]}>
  <Col xs={24} sm={12} lg={8} xl={6} xxl={4}>卡片</Col>
</Row>

// 等价 Grid 写法：
<Grid cols={{ xs: 1, sm: 2, lg: 3, xl: 4, xxl: 6 }} colGap={16} rowGap={16}>
  <Grid.Item>卡片</Grid.Item>
</Grid>
```

### 主侧栏布局

| 断点 | 主内容 | 侧边栏 |
|---|---|---|
| xs / sm | 24（叠加） | 24（叠加） |
| md | 16 | 8 |
| lg+ | 18 | 6 |

```jsx
<Row gutter={24}>
  <Col xs={24} md={16} lg={18}>主内容</Col>
  <Col xs={24} md={8} lg={6}>侧边栏</Col>
</Row>
```

### 表单多列

| 断点 | 每行表单项数 |
|---|---|
| xs | 1（span=24） |
| sm | 2（span=12） |
| md | 2-3（span=12 或 8） |
| lg+ | 3-4（span=8 或 6） |

```jsx
<Row gutter={[24, 0]}>
  <Col xs={24} sm={12} lg={8}>
    <Form.Item label="字段1"><Input /></Form.Item>
  </Col>
  <Col xs={24} sm={12} lg={8}>
    <Form.Item label="字段2"><Input /></Form.Item>
  </Col>
  <Col xs={24} sm={12} lg={8}>
    <Form.Item label="字段3"><Input /></Form.Item>
  </Col>
</Row>
```

---

## useBreakpoint Hook（获取当前断点）

```jsx
import { Grid } from 'lingyang';
const { useBreakpoint } = Grid;

function MyComponent() {
  const breakpoint = useBreakpoint();
  // breakpoint: { xs: true, sm: true, md: false, lg: false, xl: false, xxl: false }
  // 表示当前屏幕宽度在 sm 范围内（≥ 576px 但 < 768px）

  const isMobile = !breakpoint.md; // 平板以下视为移动端

  return (
    <Row>
      <Col span={isMobile ? 24 : 12}>
        {isMobile ? '移动端内容' : '桌面端内容'}
      </Col>
    </Row>
  );
}
```

---
