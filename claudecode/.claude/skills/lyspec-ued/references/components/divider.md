# lingyang-divider · 分割线组件 Skill

**渲染**：水平 → `<div>`，垂直 → `<span>`

---

## ⚠️ 与 Ant Design 的关键差异

| 能力 | lingyang Divider | Ant Design Divider |
|---|---|---|
| 方向控制 | `type='horizontal'\|'vertical'` | `orientation='vertical'` 或 `vertical` prop |
| 文字位置 | `orientation='left'\|'center'\|'right'` | 同名，行为相同 |
| 上下间距 | `marginTop` / `marginBottom`（专有） | 无，需用 `style` |
| plain 文字 | 不支持 | 支持 `plain` prop |

---

## Props 全览

| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `type` | `'horizontal' \| 'vertical'` | `'horizontal'` | 分割线方向 |
| `orientation` | `'left' \| 'center' \| 'right'` | `'center'` | 内嵌文字位置（仅水平有效）|
| `orientationMargin` | `number \| string` | — | 文字与侧边距离（仅 left/right 时有效）|
| `dashed` | `boolean` | `false` | 是否为虚线 |
| `marginTop` | `number` | — | 上方间距 px（lingyang 专有）|
| `marginBottom` | `number` | — | 下方间距 px（lingyang 专有）|
| `style` | `CSSProperties` | — | 自定义样式（可覆盖颜色/粗细）|
| `className` | `string` | — | 自定义类名 |
| `children` | `ReactNode` | — | 内嵌文字（仅水平有效）|

---

## 核心约束

1. `type='vertical'` 时**不支持** `children`，也不支持 `orientation`、`marginTop`、`marginBottom`
2. `orientationMargin` 仅在 `orientation='left'` 或 `'right'` 时生效，`center` 时无效
3. 竖线高度由**父容器行高**决定，需自定义高度时通过 `style={{ height: '1em' }}` 覆盖
4. 纯装饰性竖线建议加 `aria-hidden="true"`

---

## 高频场景速查

### 基础水平分割线
```jsx
<Divider />
```

### 虚线
```jsx
<Divider dashed />
```

### 带文字（区块标题）
```jsx
<Divider orientation="left">基本信息</Divider>
<Divider>居中标题</Divider>
<Divider orientation="right" dashed>可选配置</Divider>
```

### 竖线（行内分隔）
```jsx
// 常用于 Space 内、表格操作列
<Space>
  <a href="#">编辑</a>
  <Divider type="vertical" />
  <a href="#">复制</a>
  <Divider type="vertical" />
  <a href="#" style={{ color: 'red' }}>删除</a>
</Space>
```

### 自定义颜色 / 粗细
```jsx
<Divider style={{ borderColor: '#13AE68', borderTopWidth: 2 }} />
```

### 自定义间距（lingyang 专有）
```jsx
<Divider marginTop={32} marginBottom={24}>自定义间距分割线</Divider>
```

---

## CSS 类名速查

| 场景 | 类名 |
|---|---|
| 水平分割线 | `.lingyang-divider.lingyang-divider-horizontal` |
| 垂直分割线 | `.lingyang-divider.lingyang-divider-vertical` |
| 虚线 | `.lingyang-divider.lingyang-divider-dashed` |
| 带文字 | `.lingyang-divider.lingyang-divider-with-text` |
| 文字靠左 | `.lingyang-divider.lingyang-divider-with-text-left` |
| 文字靠右 | `.lingyang-divider.lingyang-divider-with-text-right` |
| 文字节点 | `.lingyang-divider-text` |

---

## 默认视觉规格

| 属性 | 水平线 | 竖线 |
|---|---|---|
| 线条颜色 | `#e5e6eb` | `#e5e6eb` |
| 上下外边距 | `16px 0` | `0` |
| 左右外边距 | — | `8px` |
| 线条粗细 | `1px` | `1px` |
| 竖线高度 | — | `0.9em`（随行高）|

> 需要读取完整代码示例请查看 `references/examples.md`
-e 

---

## 完整代码示例

# lingyang-divider · 完整代码示例库

## 目录
1. [基础用法](#1-基础用法)
2. [虚线样式](#2-虚线样式)
3. [带文字的分割线](#3-带文字的分割线)
4. [文字位置与偏移](#4-文字位置与偏移)
5. [竖向分割线](#5-竖向分割线)
6. [自定义样式](#6-自定义样式)
7. [企业级场景模板](#7-企业级场景模板)

---

## 1. 基础用法

```jsx
import { Divider, Typography } from 'lingyang';

export default function BasicDivider() {
  return (
    <div>
      <Typography.Paragraph>
        Lorem ipsum dolor sit amet，消光白日照山色，不令身心染尘埃。
      </Typography.Paragraph>

      {/* 最简用法：无任何 props */}
      <Divider />

      <Typography.Paragraph>
        此生本自无缺欠，当下即是全功圆。莫向心外求玄妙，但将此心向虚空。
      </Typography.Paragraph>

      {/* 显式指定方向（与默认相同） */}
      <Divider type="horizontal" />

      <Typography.Paragraph>
        静观万物皆自得，四时佳兴与人同。道可道，非常道；名可名，非常名。
      </Typography.Paragraph>
    </div>
  );
}
```

---

## 2. 虚线样式

```jsx
import { Divider, Typography } from 'lingyang';

export default function DashedDivider() {
  return (
    <div>
      <Typography.Paragraph>实线分割线（默认）</Typography.Paragraph>
      <Divider />

      <Typography.Paragraph>虚线分割线（视觉权重更低）</Typography.Paragraph>
      <Divider dashed />

      <Typography.Paragraph>
        虚线 + 内嵌文字
      </Typography.Paragraph>
      <Divider dashed orientation="left">虚线带标题</Divider>

      <Typography.Paragraph>内容继续...</Typography.Paragraph>
    </div>
  );
}
```

---

## 3. 带文字的分割线

```jsx
import { Divider, Typography, Button } from 'lingyang';

export default function DividerWithText() {
  return (
    <div>
      {/* 纯文字 */}
      <Divider>居中标题</Divider>

      {/* Typography 样式文字 */}
      <Divider>
        <Typography.Text type="secondary" style={{ fontSize: 12 }}>
          以下为可选配置项
        </Typography.Text>
      </Divider>

      {/* 链接文字（不推荐放可交互内容，仅展示） */}
      <Divider>
        <Typography.Text type="primary" style={{ cursor: 'pointer', fontSize: 13 }}>
          查看更多 ›
        </Typography.Text>
      </Divider>

      {/* 带图标的标题 */}
      <Divider>
        <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <IconSettings style={{ color: '#13AE68' }} />
          <span>系统设置</span>
        </span>
      </Divider>
    </div>
  );
}
```

---

## 4. 文字位置与偏移

```jsx
import { Divider } from 'lingyang';

export default function DividerOrientation() {
  return (
    <div>
      {/* 三种对齐方式 */}
      <Divider orientation="left">左对齐标题</Divider>
      <div style={{ height: 24 }} />
      <Divider orientation="center">居中标题（默认）</Divider>
      <div style={{ height: 24 }} />
      <Divider orientation="right">右对齐标题</Divider>

      <div style={{ height: 32 }} />

      {/* orientationMargin：自定义文字与侧边距 */}
      <Divider orientation="left" orientationMargin={0}>
        紧贴左侧（margin=0）
      </Divider>
      <Divider orientation="left" orientationMargin={20}>
        距左 20px
      </Divider>
      <Divider orientation="left" orientationMargin={80}>
        距左 80px
      </Divider>
      <Divider orientation="right" orientationMargin={0}>
        紧贴右侧（margin=0）
      </Divider>
    </div>
  );
}
```

---

## 5. 竖向分割线

```jsx
import { Divider, Space, Typography } from 'lingyang';

export default function VerticalDivider() {
  return (
    <div>
      {/* 基础竖线：在 Space 中使用 */}
      <Space>
        <a href="#">首页</a>
        <Divider type="vertical" />
        <a href="#">关于</a>
        <Divider type="vertical" />
        <a href="#">联系我们</a>
      </Space>

      <br /><br />

      {/* 表格操作列（最典型场景） */}
      <Space split={<Divider type="vertical" />} size={0}>
        <Typography.Text
          type="primary"
          style={{ cursor: 'pointer', fontSize: 13 }}
        >
          查看
        </Typography.Text>
        <Typography.Text
          type="primary"
          style={{ cursor: 'pointer', fontSize: 13 }}
        >
          编辑
        </Typography.Text>
        <Typography.Text
          type="danger"
          style={{ cursor: 'pointer', fontSize: 13 }}
        >
          删除
        </Typography.Text>
      </Space>

      <br /><br />

      {/* 统计数据分隔 */}
      <Space size="large" align="center">
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 24, fontWeight: 700 }}>12,580</div>
          <div style={{ color: '#86909c', fontSize: 12 }}>总用户</div>
        </div>
        <Divider type="vertical" style={{ height: 40 }} />
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 24, fontWeight: 700 }}>¥156,800</div>
          <div style={{ color: '#86909c', fontSize: 12 }}>本月收入</div>
        </div>
        <Divider type="vertical" style={{ height: 40 }} />
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 24, fontWeight: 700 }}>99.95%</div>
          <div style={{ color: '#86909c', fontSize: 12 }}>系统可用率</div>
        </div>
      </Space>

      <br /><br />

      {/* 纯装饰时添加 aria-hidden */}
      <Space>
        <span>创建于 2024-01-01</span>
        <Divider type="vertical" aria-hidden="true" />
        <span>修改于 2024-06-15</span>
        <Divider type="vertical" aria-hidden="true" />
        <span>作者：张三</span>
      </Space>
    </div>
  );
}
```

---

## 6. 自定义样式

```jsx
import { Divider } from 'lingyang';

export default function CustomStyleDivider() {
  return (
    <div>
      {/* 自定义颜色 */}
      <Divider style={{ borderColor: '#13AE68' }}>绿色分割线</Divider>

      {/* 自定义粗细 */}
      <Divider style={{ borderTopWidth: 2, borderColor: '#165DFF' }}>加粗蓝色</Divider>

      {/* 同时自定义颜色 + 虚线 */}
      <Divider dashed style={{ borderColor: '#FF7D00' }}>橙色虚线</Divider>

      {/* 自定义间距（lingyang 专有 marginTop/marginBottom） */}
      <Divider marginTop={32} marginBottom={8}>上 32px 下 8px</Divider>

      {/* 通过 style 覆盖间距（等效写法） */}
      <Divider style={{ margin: '32px 0 8px' }}>等效写法</Divider>

      {/* 极细的装饰线 */}
      <Divider style={{ borderColor: '#f2f3f5' }} />

      {/* 竖线自定义高度 */}
      <span style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
        <span>左侧内容</span>
        <Divider
          type="vertical"
          style={{ height: 24, borderColor: '#ccc', margin: 0 }}
        />
        <span>右侧内容</span>
      </span>
    </div>
  );
}
```

---

## 7. 企业级场景模板

### 表单分节（最常用后台场景）
```jsx
import { Divider, Form, Input, Select, Grid } from 'lingyang';
const { Row, Col } = Grid;

export default function FormWithDividers() {
  return (
    <Form layout="vertical">

      {/* 第一节：基本信息 */}
      <Divider orientation="left" marginTop={0}>
        基本信息
      </Divider>
      <Row gutter={[24, 0]}>
        <Col xs={24} md={12}>
          <Form.Item label="姓名" field="name" rules={[{ required: true }]}>
            <Input placeholder="请输入姓名" />
          </Form.Item>
        </Col>
        <Col xs={24} md={12}>
          <Form.Item label="工号" field="empId">
            <Input placeholder="请输入工号" />
          </Form.Item>
        </Col>
      </Row>

      {/* 第二节：联系信息 */}
      <Divider orientation="left">联系信息</Divider>
      <Row gutter={[24, 0]}>
        <Col xs={24} md={12}>
          <Form.Item label="手机号" field="phone">
            <Input placeholder="请输入手机号" />
          </Form.Item>
        </Col>
        <Col xs={24} md={12}>
          <Form.Item label="邮箱" field="email">
            <Input placeholder="请输入邮箱" />
          </Form.Item>
        </Col>
      </Row>

      {/* 第三节：可选配置 */}
      <Divider orientation="left" dashed>
        <Typography.Text type="secondary" style={{ fontSize: 13 }}>
          可选配置
        </Typography.Text>
      </Divider>
      <Row gutter={[24, 0]}>
        <Col xs={24} md={12}>
          <Form.Item label="部门" field="dept">
            <Select placeholder="请选择部门" />
          </Form.Item>
        </Col>
      </Row>

    </Form>
  );
}
```

### 详情页区块分节
```jsx
import { Divider, Descriptions, Space, Typography } from 'lingyang';

export default function DetailPageSections() {
  return (
    <div style={{ padding: 24 }}>

      {/* 页面标题区 */}
      <Space align="center" style={{ marginBottom: 0 }}>
        <Typography.Title heading={4} style={{ margin: 0 }}>
          用户详情
        </Typography.Title>
        <Tag color="green">正常</Tag>
      </Space>

      <Divider marginTop={16} marginBottom={24} />

      {/* 基本信息 */}
      <Typography.Title heading={6} style={{ marginBottom: 12 }}>
        基本信息
      </Typography.Title>
      <Descriptions
        data={[
          { label: '姓名', value: '张三' },
          { label: '工号', value: 'EMP-001' },
          { label: '部门', value: '技术部' },
          { label: '职位', value: '高级工程师' },
        ]}
        column={2}
      />

      <Divider dashed marginTop={24} marginBottom={24} />

      {/* 联系信息 */}
      <Typography.Title heading={6} style={{ marginBottom: 12 }}>
        联系信息
      </Typography.Title>
      <Descriptions
        data={[
          { label: '手机', value: '138****8888' },
          { label: '邮箱', value: 'zhang***@example.com' },
        ]}
        column={2}
      />

    </div>
  );
}
```

### 卡片内容分隔
```jsx
import { Card, Divider, Space, Button, Typography, Statistic } from 'lingyang';

export default function CardWithDividers() {
  return (
    <Card style={{ width: 360 }}>

      {/* 卡片标题区 */}
      <Space align="center" style={{ marginBottom: 16 }}>
        <Avatar size={48} style={{ background: '#13AE68' }}>张</Avatar>
        <div>
          <Typography.Text bold>张三</Typography.Text>
          <br />
          <Typography.Text type="secondary" style={{ fontSize: 12 }}>
            高级前端工程师
          </Typography.Text>
        </div>
      </Space>

      <Divider style={{ margin: '0 0 16px' }} />

      {/* 统计数据 */}
      <Space style={{ width: '100%', justifyContent: 'space-around' }}>
        <Statistic title="文章" value={128} />
        <Divider type="vertical" style={{ height: 40 }} />
        <Statistic title="粉丝" value={2456} />
        <Divider type="vertical" style={{ height: 40 }} />
        <Statistic title="关注" value={89} />
      </Space>

      <Divider style={{ margin: '16px 0' }} />

      {/* 底部操作 */}
      <Space style={{ width: '100%', justifyContent: 'flex-end' }}>
        <Button>发消息</Button>
        <Button type="primary">关注</Button>
      </Space>

    </Card>
  );
}
```

### 登录页分隔（"或"字登录）
```jsx
import { Divider, Button, Space } from 'lingyang';

export default function LoginDivider() {
  return (
    <div style={{ width: 320, padding: '24px 0' }}>

      <Button type="primary" long>账号密码登录</Button>

      <Divider style={{ margin: '20px 0', color: '#86909c', fontSize: 13 }}>
        或者
      </Divider>

      <Space direction="vertical" size="small" style={{ width: '100%' }}>
        <Button long icon={<IconWechat />} style={{ borderColor: '#07c160', color: '#07c160' }}>
          微信登录
        </Button>
        <Button long icon={<IconQQ />} style={{ borderColor: '#0085ff', color: '#0085ff' }}>
          QQ 登录
        </Button>
      </Space>

    </div>
  );
}
```

---
