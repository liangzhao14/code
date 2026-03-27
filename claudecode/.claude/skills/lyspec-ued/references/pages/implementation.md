# lingyang Page DSL — React 实现参考

## 通用页面框架

```tsx
// StandardPageWrapper.tsx — 适用于所有标准后台页面
import { Layout } from 'lingyang';
const { Sider, Header, Content } = Layout;

export const StandardPageWrapper = ({ children, sidebarActiveKey }) => (
  <Layout style={{ minHeight: '100vh', background: '#F7F8FA' }}>
    <Sider style={{ position: 'fixed', left: 8, top: 60, width: 204, background: '#fff', borderRadius: 4 /* radius-2 */ }}>
      {/* NavMenu — 激活项: bg=#F2F3F5, rx=2, color=#165DFF */}
    </Sider>
    <Layout style={{ marginLeft: 232 }}>
      <Header style={{ height: 60, background: '#fff', padding: '0 20px', display: 'flex', alignItems: 'center' }}>
        {/* 面包屑 | 搜索(x=916,w=220,h=32,rx=16,bg=#F2F3F5) | 图标组(32×32,rx=16) | 头像 */}
      </Header>
      <Content style={{ padding: '16px 20px', marginTop: 60 }}>
        <div style={{ background: '#fff', borderRadius: 8 /* radius-3 */, boxShadow: '0 2px 5px rgba(0,0,0,.1)', padding: 20 }}>
          {children}
        </div>
      </Content>
    </Layout>
  </Layout>
);
```

---

## 查询表格页

```tsx
import { Form, Grid, Input, Button, Table, Tag, Space } from 'lingyang';
const { Row, Col } = Grid;

// 3列×2行筛选区（每列w=243, h=32, bg=#F2F3F5, rx=2）
// colXs: [340, 687, 1034] | rowYs: [176, 228] | 列间距≈48px
const FILTERS = ['筛选项1','筛选项2','筛选项3','筛选项4','筛选项5','筛选项6'];

const SearchTablePage = () => {
  const [form] = Form.useForm();
  const columns = [
    { title: '序号', dataIndex: 'index', width: 80 },
    { title: '名称', dataIndex: 'name', width: 200 },
    { title: '类型', dataIndex: 'type', width: 120 },
    {
      title: '状态', dataIndex: 'status', width: 120,
      render: (s) => {
        const map = { '进行中': ['#165DFF','#E8F3FF'], '已完成': ['#00B42A','#E8FFEA'],
                      '已暂停': ['#FF7D00','#FFF3E8'], '已取消': ['#F53F3F','#FFECE8'] };
        const [color, bg] = map[s] ?? ['#4E5969','#F2F3F5'];
        return <Tag style={{ color, background: bg, border: 'none' }}>{s}</Tag>;
      }
    },
    { title: '创建时间', dataIndex: 'createdAt', width: 180 },
    { title: '操作', dataIndex: 'id', width: 160,
      render: (_, rec) => (
        <Space>
          <a style={{ color: '#165DFF' }}>编辑</a>
          <a style={{ color: '#F53F3F' }}>删除</a>
        </Space>
      )
    },
  ];
  return (
    <div>
      <Form form={form}>
        <Row gutter={[48, 20]} style={{ padding: '20px 80px' }}>
          {FILTERS.map((label, i) => (
            <Col key={i} span={8}>
              <Form.Item label={label} field={`field${i}`}
                labelCol={{ style: { fontSize: 12, color: '#86909C' } }}>
                <Input style={{ height: 32, background: '#F2F3F5', borderRadius: 4 /* radius-2 */ }} />
              </Form.Item>
            </Col>
          ))}
        </Row>
        {/* 右侧按钮：查询(#165DFF 82×32) + 重置(#F2F3F5 82×32) */}
      </Form>
      {/* 操作栏：新建(primary) + 批量删除 | 右：导出 */}
      <Table columns={columns} data={[]} rowKey="index" rowHeight={48}
        pagination={{ pageSize: 10, style: { justifyContent: 'flex-end' } }} />
    </div>
  );
};
```

---

## 卡片列表页

```tsx
// 4列×3行，col起始x=[260,552,842,1134]，row起始y=[262,452,642]
// gap=20px，CardItem(266×173, rx=3.5, border=1px solid #E5E6EB)
const CardListPage = ({ items = [] }) => (
  <div>
    <div style={{ display: 'flex', justifyContent: 'space-between', padding: '20px' }}>
      <Button type="primary" style={{ height: 32 }}>新建卡片</Button>
      <Input style={{ width: 200, height: 32, background: '#F2F3F5', borderRadius: 4 /* radius-2 */ }} placeholder="搜索" />
    </div>
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 266px)', gap: 20, padding: '0 20px 20px' }}>
      {items.map(item => (
        <div key={item.id} style={{ width: 266, borderRadius: 4 /* radius-2 */, border: '1px solid #E5E6EB', background: '#fff', overflow: 'hidden' }}>
          <div style={{ height: 100, background: item.coverBg || '#F2F3F5' }} />
          <div style={{ padding: '8px 12px' }}>
            <div style={{ fontSize: 14, fontWeight: 600, color: '#1D2129' }}>{item.title}</div>
            <div style={{ fontSize: 12, color: '#86909C', WebkitLineClamp: 2, display: '-webkit-box', WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{item.desc}</div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px' }}>
            <Avatar.Group size={24}>{/* avatars */}</Avatar.Group>
            <Tag style={{ border: 'none' }}>{item.status}</Tag>
          </div>
        </div>
      ))}
    </div>
  </div>
);
```

---

## 分步表单

```tsx
// Steps: active=#165DFF / done=#00B42A / wait=#C9CDD4
// 表单区: x=610, w=440, 4×Input(h=32,bg=#F2F3F5,rx=2), y=344/396/448/500
// 步骤导航: border-top=#F2F3F5, 上一步(ghost) + 下一步(primary)
import { Steps, Form, Input, Select, Button } from 'lingyang';

const StepFormPage = () => {
  const [current, setCurrent] = React.useState(0);
  return (
    <div style={{ padding: 40 }}>
      <Steps current={current} style={{ marginBottom: 40 }}>
        {['填写基本信息','填写详细信息','完成'].map((t, i) => <Steps.Step key={i} title={t} />)}
      </Steps>
      <div style={{ display: 'flex', gap: 40 }}>
        <div style={{ width: 340 }}{/* 左侧插画区 */} />
        <Form style={{ width: 440 }}>
          {[344,396,448,500].map((y, i) => (
            <Form.Item key={i} label={`字段${i+1}`} labelCol={{ style: { fontSize:12, color:'#86909C' } }}>
              <Input style={{ height: 32, background: '#F2F3F5', borderRadius: 4 /* radius-2 */ }} />
            </Form.Item>
          ))}
        </Form>
      </div>
      <div style={{ marginTop: 40, paddingTop: 20, borderTop: '1px solid #F2F3F5', display: 'flex', justifyContent: 'flex-end', gap: 12 }}>
        {current > 0 && <Button style={{ border: '1px solid #165DFF', color: '#165DFF' }} onClick={() => setCurrent(c => c-1)}>上一步</Button>}
        <Button type="primary" style={{ background: '#165DFF' }} onClick={() => setCurrent(c => c+1)}>
          {current < 2 ? '下一步' : '提交'}
        </Button>
      </div>
    </div>
  );
};
```

---

## 成功页

```tsx
// 结果图标: 绿圆(#00B42A,r≈56) + 白色✓
// StepDots: cx=[490,658,826,994,1162], r=5
//   done=#165DFF (前2个), wait=#C9CDD4 (后3个), y=593
const SuccessPage = () => (
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '120px 40px' }}>
    <div style={{ width: 112, height: 112, borderRadius: '50%', background: '#00B42A', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 32 }}>
      <IconCheck style={{ fontSize: 48, color: '#fff' }} />
    </div>
    <div style={{ fontSize: 28, fontWeight: 600, color: '#1D2129', marginBottom: 12 }}>提交成功</div>
    <div style={{ fontSize: 14, color: '#86909C', marginBottom: 32 }}>描述文字</div>
    <Button type="primary" style={{ width: 116, height: 32, background: '#165DFF' }}>返回列表</Button>
    {/* StepDots SVG — 5个点，间距168px */}
    <svg width="700" height="20" style={{ marginTop: 80 }}>
      {[0,168,336,504,672].map((offset, i) => (
        <circle key={i} cx={offset + 14} cy={10} r={5} fill={i < 2 ? '#165DFF' : '#C9CDD4'} />
      ))}
      {[0,168,336,504].map((offset, i) => (
        <line key={i} x1={offset+19} y1={10} x2={offset+177} y2={10} stroke="#C9CDD4" strokeWidth={1} />
      ))}
    </svg>
  </div>
);
```

---

## 用户设置-2（Toggle 设置列表）

```tsx
// Toggle 列表: itemH=48, borderBottom=1px solid #F2F3F5
// Switch: 开启色 #12D2AC (通知) / #307AF2 (安全)
import { Switch } from 'lingyang';

const TOGGLES = [
  { title: '邮件通知', desc: '接收系统邮件提醒', checked: true,  color: '#12D2AC' },
  { title: '短信通知', desc: '接收手机短信提醒', checked: false, color: '#307AF2' },
  { title: '站内消息', desc: '接收站内信通知',   checked: true,  color: '#12D2AC' },
];

const ToggleList = () => (
  <div>
    {TOGGLES.map((item, i) => (
      <div key={i} style={{ height: 48, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 16px', borderBottom: '1px solid #F2F3F5' }}>
        <div>
          <div style={{ fontSize: 14, fontWeight: 500, color: '#1D2129' }}>{item.title}</div>
          <div style={{ fontSize: 12, color: '#86909C' }}>{item.desc}</div>
        </div>
        <Switch defaultChecked={item.checked} style={{ '--color-primary': item.color } as any} />
      </div>
    ))}
  </div>
);
```

---

## 基础详情页

```tsx
// PageHeader (1180×130): 面包屑 + 标题 + 操作按钮
// Section 3次 (1180×280 each): Descriptions 2列 偶数行bg=#F2F3F5
// 内嵌Table (1140×550, x=260, rx=2)
import { Breadcrumb, Descriptions, Table, Button, Space } from 'lingyang';

const BasicDetailPage = () => (
  <div>
    {/* PageHeader */}
    <div style={{ background: '#fff', borderRadius: 8 /* radius-3 */, padding: '20px 24px', marginBottom: 16, boxShadow: '0 2px 5px rgba(0,0,0,.1)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <div>
          <Breadcrumb style={{ marginBottom: 8 }}>
            <Breadcrumb.Item>首页</Breadcrumb.Item>
            <Breadcrumb.Item>列表</Breadcrumb.Item>
            <Breadcrumb.Item>详情</Breadcrumb.Item>
          </Breadcrumb>
          <div style={{ fontSize: 20, fontWeight: 600, color: '#1D2129' }}>详情标题</div>
        </div>
        <Space>
          <Button type="primary">编辑</Button>
          <Button>下载</Button>
          <Button>归档</Button>
        </Space>
      </div>
    </div>
    {/* 基本信息 Descriptions */}
    {['基本信息','关联信息'].map(title => (
      <div key={title} style={{ background: '#fff', borderRadius: 8 /* radius-3 */, padding: 24, marginBottom: 16, boxShadow: '0 2px 5px rgba(0,0,0,.1)' }}>
        <div style={{ fontSize: 16, fontWeight: 600, marginBottom: 16 }}>{title}</div>
        <Descriptions column={2}
          labelStyle={{ color: '#86909C', fontSize: 12 }}
          valueStyle={{ color: '#1D2129', fontSize: 14 }}
          data={Array.from({ length: 10 }, (_, i) => ({ label: `字段${i+1}`, value: `内容${i+1}` }))}
        />
      </div>
    ))}
    {/* 数据记录 */}
    <div style={{ background: '#fff', borderRadius: 8 /* radius-3 */, padding: 24, boxShadow: '0 2px 5px rgba(0,0,0,.1)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 16 }}>
        <div style={{ fontSize: 16, fontWeight: 600 }}>数据记录</div>
        <a style={{ color: '#165DFF', fontSize: 14 }}>查看更多</a>
      </div>
      <Table columns={[]} data={[]} style={{ borderRadius: 4 /* radius-2 */ }} />
    </div>
  </div>
);
```
