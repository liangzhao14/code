# lingyang-table · 表格组件 Skill

**泛型**：`Table<T>` —— T 为行数据类型

---

## 何时读取子文档

| 需求 | 读取文件 |
|---|---|
| 完整 TypeScript 类型定义（所有接口） | `references/props.md` |
| 完整代码示例（9 大场景） | `references/examples.md` |

---

## ⚠️ lingyang vs Ant Design 关键差异

| 能力 | lingyang Table | Ant Design Table |
|---|---|---|
| 斑马纹 | `stripe` prop ✅ | ❌ 无 |
| 虚拟滚动 | `virtualized` prop | `scroll.y + virtual` |
| 空数据自定义 | `noDataElement` | `locale.emptyText` |
| table-layout | `tableLayoutFixed` prop | `tableLayout='fixed'` |
| 展开行配置对象名 | `expandProps` | `expandable`（同功能）|
| onChange 参数顺序 | `(pagination, sorter, filters, extra)` | `(pagination, filters, sorter, extra)` |

---

## TableProps 速查

| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `columns` ★ | `ColumnProps[]` | — | 列定义数组 |
| `dataSource` ★ | `T[]` | — | 数据源 |
| `rowKey` | `string \| fn` | `'key'` | 行唯一标识，**无 key 字段时必须指定** |
| `loading` | `boolean \| SpinProps` | `false` | 加载状态 |
| `pagination` | `false \| PaginationProps` | — | 分页；false = 关闭 |
| `rowSelection` | `TableRowSelection` | — | 行选择配置 |
| `expandProps` | `TableExpandProps` | — | 展开行配置（≠ Ant Design 的 expandable）|
| `scroll` | `{ x?, y?, minWidth?, maxHeight? }` | — | 滚动/固定配置 |
| `bordered` | `boolean` | `false` | 完整边框 |
| `stripe` | `boolean` | `false` | **lingyang 专有** 斑马纹 |
| `size` | `'default'\|'middle'\|'small'` | `'default'` | 表格密度 |
| `tableLayoutFixed` | `boolean` | `false` | **lingyang 专有** fixed 布局 |
| `virtualized` | `boolean` | `false` | **lingyang 专有** 虚拟滚动（须配合 `scroll.y` number 值）|
| `noDataElement` | `ReactNode` | — | **lingyang 专有** 空数据占位 |
| `rowClassName` | `(record, index) => string` | — | 行自定义类名 |
| `onRow` | `(record, index) => HTMLAttrs` | — | 行事件处理器 |
| `onChange` | `(pagination, sorter, filters, extra) => void` | — | 分页/排序/筛选统一回调 |
| `summary` | `(data) => ReactNode` | — | 固定汇总行（配合 Table.Summary）|
| `indentSize` | `number` | `16` | 树形数据缩进 px |
| `childrenColumnName` | `string` | `'children'` | 树形子节点字段名 |

---

## ColumnProps 速查

| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `title` ★ | `ReactNode` | — | 列标题 |
| `dataIndex` | `string` | — | 数据字段，支持点号路径 `'user.name'` |
| `key` | `string` | — | 列唯一 key（无 dataIndex 时必填）|
| `width` | `number \| string` | — | 列宽，**固定列必须设置** |
| `fixed` | `'left' \| 'right'` | — | 固定列方向 |
| `align` | `'left' \| 'center' \| 'right'` | `'left'` | 对齐 |
| `render` | `(value, record, index) => ReactNode` | — | 自定义渲染 |
| `sorter` | `boolean \| (a,b)=>number` | — | 排序（true=服务端，fn=本地）|
| `sortOrder` | `'ascend' \| 'descend' \| null` | — | 受控排序状态 |
| `filters` | `{ text, value }[]` | — | 筛选菜单项 |
| `onFilter` | `(value, record) => boolean` | — | 本地筛选函数 |
| `filteredValue` | `any[]` | — | 受控筛选值 |
| `ellipsis` | `boolean` | `false` | 超出省略（需 `tableLayoutFixed`）|
| `tooltip` | `boolean` | — | ellipsis 时 Tooltip 提示 |
| `colSpan` | `number` | — | 表头单元格合并列 |
| `children` | `ColumnProps[]` | — | 分组列头 |
| `onCell` | `(record, index) => { colSpan?, rowSpan? }` | — | 合并数据单元格 |

---

## 最小可用示例

```jsx
import { Table } from 'lingyang';

const columns = [
  { title: '姓名', dataIndex: 'name', key: 'name' },
  { title: '年龄', dataIndex: 'age',  key: 'age', align: 'right' as const },
  { title: '部门', dataIndex: 'dept', key: 'dept' },
  {
    title: '操作',
    key: 'action',
    render: (_: any, record: any) => (
      <a onClick={() => console.log(record)}>编辑</a>
    ),
  },
];

const data = [
  { key: '1', name: '张三', age: 28, dept: '技术部' },
  { key: '2', name: '李四', age: 35, dept: '产品部' },
];

export default function Demo() {
  return <Table columns={columns} dataSource={data} rowKey="key" />;
}
```

---

## 高频场景配置速查

### 服务端分页 + 排序 + 筛选
```jsx
<Table
  rowKey="id"
  dataSource={list}
  columns={columns}
  loading={loading}
  pagination={{
    current: params.page,
    pageSize: params.pageSize,
    total: total,
    showTotal: (t) => `共 ${t} 条`,
    showSizeChanger: true,
  }}
  onChange={(pagination, sorter, filters) => {
    // 注意：lingyang 顺序是 pagination, sorter, filters（Ant Design 相反）
    fetchList({
      page: pagination.current,
      pageSize: pagination.pageSize,
      sortField: sorter.field,
      sortOrder: sorter.order,
      ...filters,
    });
  }}
/>
```

### 行选择（多选，服务端分页）
```jsx
const [selectedKeys, setSelectedKeys] = useState<(string | number)[]>([]);

<Table
  rowSelection={{
    type: 'checkbox',
    selectedRowKeys: selectedKeys,
    onChange: (keys) => setSelectedKeys(keys),
    preserveSelectedRowKeys: true,  // 翻页保留选中 ← 服务端分页必须设 true
    getCheckboxProps: (record) => ({ disabled: !record.canSelect }),
  }}
/>
```

### 固定列 + 固定表头
```jsx
<Table
  scroll={{ x: 1600, y: 400 }}
  columns={[
    { title: '姓名', dataIndex: 'name', fixed: 'left',  width: 120 },
    // ... 中间若干列（合计宽度 = scroll.x）
    { title: '操作', key: 'op',          fixed: 'right', width: 140,
      render: () => <Space><a>编辑</a><a>删除</a></Space> },
  ]}
/>
```

### lingyang 专有特性
```jsx
// 斑马纹
<Table stripe dataSource={data} columns={columns} />

// 虚拟滚动（5000+ 行大数据）
<Table
  virtualized
  scroll={{ y: 600 }}     // y 必须为 number
  dataSource={bigData}
  columns={columns}
/>

// 自定义空数据
<Table
  noDataElement={
    <div style={{ textAlign: 'center', padding: 40, color: '#86909c' }}>
      <IconEmpty style={{ fontSize: 48 }} />
      <div style={{ marginTop: 8 }}>暂无数据</div>
    </div>
  }
/>

// ellipsis 超长省略（必须 tableLayoutFixed）
<Table
  tableLayoutFixed
  columns={[
    { title: '备注', dataIndex: 'remark', ellipsis: true, tooltip: true, width: 200 },
  ]}
/>
```

### 展开行
```jsx
<Table
  expandProps={{
    expandedRowRender: (record) => (
      <div style={{ padding: '8px 48px' }}>{record.description}</div>
    ),
    rowExpandable: (record) => !!record.hasDetail,
    expandRowByClick: true,
  }}
/>
```

### 树形数据
```jsx
// 数据中有 children 字段时自动树形展示
const treeData = [
  { key: '1', name: '技术部', children: [
    { key: '1-1', name: '前端组' },
    { key: '1-2', name: '后端组' },
  ]},
];
<Table dataSource={treeData} columns={columns} rowKey="key" />
```

---

## CSS 类名速查

| 场景 | 类名 |
|---|---|
| 容器 | `.lingyang-table-container` |
| Table | `.lingyang-table` |
| bordered | `.lingyang-table.lingyang-table-border` |
| stripe | `.lingyang-table.lingyang-table-stripe` |
| 表头 | `.lingyang-table-thead` |
| 数据行 | `.lingyang-table-tbody .lingyang-table-tr` |
| 选中行 | `.lingyang-table-tr.lingyang-table-row-checked` |
| 固定列左 | `.lingyang-table-cell-fix-left` |
| 固定列右 | `.lingyang-table-cell-fix-right` |
| 展开图标列 | `.lingyang-table-expand-icon-cell` |
| 空数据区 | `.lingyang-table-no-data` |
-e 

---

## 完整代码示例

# lingyang-table · 完整代码示例库

## 目录
1. [基础表格](#1-基础表格)
2. [分页 + 排序 + 筛选（服务端）](#2-服务端分页--排序--筛选)
3. [行选择（多选，服务端分页）](#3-行选择多选)
4. [固定列 + 固定表头](#4-固定列--固定表头)
5. [展开行](#5-展开行)
6. [lingyang 专有特性](#6-lingyang-专有特性)
7. [合并单元格](#7-合并单元格)
8. [树形数据](#8-树形数据)
9. [企业级完整列表页模板](#9-企业级完整列表页模板)

---

## 1. 基础表格

```jsx
import { Table, Tag, Space } from 'lingyang';

interface User {
  id: string;
  name: string;
  age: number;
  dept: string;
  status: 'active' | 'inactive';
}

const columns = [
  {
    title: '姓名',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: '年龄',
    dataIndex: 'age',
    key: 'age',
    align: 'right' as const,
  },
  {
    title: '部门',
    dataIndex: 'dept',
    key: 'dept',
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
    render: (status: string) => (
      <Tag color={status === 'active' ? 'green' : 'gray'}>
        {status === 'active' ? '正常' : '停用'}
      </Tag>
    ),
  },
  {
    title: '操作',
    key: 'action',
    render: (_: any, record: User) => (
      <Space split={<Divider type="vertical" />} size={0}>
        <Typography.Text type="primary" style={{ cursor: 'pointer', fontSize: 13 }}>
          查看
        </Typography.Text>
        <Typography.Text type="primary" style={{ cursor: 'pointer', fontSize: 13 }}>
          编辑
        </Typography.Text>
        <Typography.Text type="danger" style={{ cursor: 'pointer', fontSize: 13 }}>
          删除
        </Typography.Text>
      </Space>
    ),
  },
];

const data: User[] = [
  { id: '1', name: '张三', age: 28, dept: '技术部', status: 'active' },
  { id: '2', name: '李四', age: 35, dept: '产品部', status: 'active' },
  { id: '3', name: '王五', age: 42, dept: '运营部', status: 'inactive' },
];

export default function BasicTable() {
  return (
    <Table
      columns={columns}
      dataSource={data}
      rowKey="id"
      bordered
    />
  );
}
```

---

## 2. 服务端分页 + 排序 + 筛选

```jsx
import { useState, useEffect } from 'react';
import { Table } from 'lingyang';

interface Params {
  page: number;
  pageSize: number;
  sortField?: string;
  sortOrder?: 'ascend' | 'descend';
  status?: string[];
}

export default function ServerSideTable() {
  const [data, setData] = useState([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);
  const [params, setParams] = useState<Params>({ page: 1, pageSize: 10 });

  const fetchData = async (p: Params) => {
    setLoading(true);
    try {
      const res = await api.getList(p);
      setData(res.list);
      setTotal(res.total);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchData(params); }, [params]);

  const columns = [
    {
      title: '姓名',
      dataIndex: 'name',
      sorter: true,          // 服务端排序：true = 仅显示图标
      sortOrder: params.sortField === 'name' ? params.sortOrder : null,
    },
    {
      title: '年龄',
      dataIndex: 'age',
      sorter: true,
      sortOrder: params.sortField === 'age' ? params.sortOrder : null,
      align: 'right' as const,
    },
    {
      title: '状态',
      dataIndex: 'status',
      filters: [
        { text: '正常', value: 'active' },
        { text: '停用', value: 'inactive' },
      ],
      filteredValue: params.status || null,
      // 服务端筛选：不设 onFilter，由 onChange 处理
    },
  ];

  return (
    <Table
      rowKey="id"
      dataSource={data}
      columns={columns}
      loading={loading}
      pagination={{
        current: params.page,
        pageSize: params.pageSize,
        total,
        showTotal: (t) => `共 ${t} 条`,
        showSizeChanger: true,
        pageSizeOptions: [10, 20, 50, 100],
      }}
      // ⚠️ 注意：lingyang 的参数顺序是 (pagination, sorter, filters, extra)
      // Ant Design 是 (pagination, filters, sorter, extra)
      onChange={(pagination, sorter, filters) => {
        setParams({
          page: pagination.current!,
          pageSize: pagination.pageSize!,
          sortField: (sorter as any).field,
          sortOrder: (sorter as any).order,
          status: (filters.status as string[]) || undefined,
        });
      }}
    />
  );
}
```

---

## 3. 行选择（多选）

```jsx
import { useState } from 'react';
import { Table, Button, Space, Popconfirm } from 'lingyang';

export default function SelectableTable() {
  const [selectedKeys, setSelectedKeys] = useState<(string | number)[]>([]);
  const [data, setData] = useState(initialData);

  const handleBatchDelete = async () => {
    await api.batchDelete(selectedKeys);
    setData(data.filter(row => !selectedKeys.includes(row.id)));
    setSelectedKeys([]);
  };

  return (
    <div>
      {/* 批量操作工具栏 */}
      {selectedKeys.length > 0 && (
        <div style={{
          background: '#e8f3ff',
          padding: '8px 16px',
          marginBottom: 16,
          borderRadius: 4,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}>
          <span>已选 <strong>{selectedKeys.length}</strong> 条</span>
          <Space>
            <Button size="small" onClick={() => setSelectedKeys([])}>取消选择</Button>
            <Popconfirm
              title={`确认删除选中的 ${selectedKeys.length} 条数据？`}
              onOk={handleBatchDelete}
            >
              <Button size="small" status="danger">批量删除</Button>
            </Popconfirm>
          </Space>
        </div>
      )}

      <Table
        rowKey="id"
        dataSource={data}
        columns={columns}
        rowSelection={{
          type: 'checkbox',
          selectedRowKeys: selectedKeys,
          onChange: (keys) => setSelectedKeys(keys),
          preserveSelectedRowKeys: true,  // 服务端分页必须设 true
          getCheckboxProps: (record) => ({
            disabled: record.status === 'locked',   // 禁止选择某些行
          }),
        }}
      />
    </div>
  );
}
```

---

## 4. 固定列 + 固定表头

```jsx
// 规则：
// 1. 固定列必须设置 width
// 2. scroll.x 需略大于所有列宽之和
// 3. 至少保留一列不设 width（弹性填充）或者让总列宽 = scroll.x

const columns = [
  // 左固定列
  { title: '姓名',   dataIndex: 'name',   fixed: 'left' as const,  width: 120 },
  { title: '工号',   dataIndex: 'empId',  fixed: 'left' as const,  width: 100 },
  // 中间非固定列（不设 width 或设宽度）
  { title: '部门',   dataIndex: 'dept',   width: 150 },
  { title: '职位',   dataIndex: 'role',   width: 150 },
  { title: '入职日期', dataIndex: 'joinDate', width: 160 },
  { title: '联系电话', dataIndex: 'phone',  width: 160 },
  { title: '邮箱',   dataIndex: 'email',  width: 200 },
  { title: '备注',   dataIndex: 'remark', width: 200 },
  // 右固定列
  {
    title: '操作',
    key: 'action',
    fixed: 'right' as const,
    width: 160,
    render: (_: any, record: any) => (
      <Space size="mini">
        <Button type="text" size="small" onClick={() => handleEdit(record)}>编辑</Button>
        <Button type="text" size="small" status="danger" onClick={() => handleDelete(record)}>删除</Button>
      </Space>
    ),
  },
];

export default function FixedTable() {
  return (
    <Table
      columns={columns}
      dataSource={data}
      rowKey="id"
      scroll={{
        x: 1400,   // 水平滚动宽度（固定列必须设置）
        y: 400,    // 垂直滚动 / 固定表头高度
      }}
      bordered
    />
  );
}
```

---

## 5. 展开行

```jsx
import { Table, Descriptions, Tag } from 'lingyang';

const expandedRowRender = (record: any) => (
  <div style={{ padding: '12px 48px', background: '#f7f8fa', borderRadius: 4 }}>
    <Descriptions
      title="详细信息"
      column={3}
      data={[
        { label: '身份证号', value: record.idCard },
        { label: '紧急联系人', value: record.emergencyContact },
        { label: '联系电话', value: record.emergencyPhone },
        { label: '入职日期', value: record.joinDate },
        { label: '合同到期', value: record.contractEnd },
        { label: '技能标签', value: (
          <Space wrap size="mini">
            {record.skills?.map((s: string) => <Tag key={s} color="arcoblue">{s}</Tag>)}
          </Space>
        )},
      ]}
    />
  </div>
);

export default function ExpandableTable() {
  const [expandedKeys, setExpandedKeys] = useState<string[]>([]);

  return (
    <Table
      rowKey="id"
      dataSource={data}
      columns={columns}
      expandProps={{
        expandedRowRender,
        expandedRowKeys: expandedKeys,
        onExpandedRowsChange: (keys) => setExpandedKeys(keys as string[]),
        rowExpandable: (record) => !!record.hasDetail,
        expandRowByClick: false,    // 仅点图标展开，不点行展开
      }}
    />
  );
}
```

---

## 6. lingyang 专有特性

### 斑马纹（stripe）
```jsx
<Table
  stripe
  dataSource={data}
  columns={columns}
  rowKey="id"
/>
```

### 虚拟滚动（大数据量）
```jsx
// 5000+ 条数据时使用，解决渲染卡顿问题
// 注意：scroll.y 必须为 number（不能是字符串）
<Table
  virtualized
  scroll={{ y: 600 }}         // ← 必须是 number
  dataSource={bigDataList}    // 5000+ 条
  columns={columns}
  rowKey="id"
  pagination={false}          // 虚拟滚动时通常关闭分页
/>
```

### 自定义空数据（noDataElement）
```jsx
import { IconEmpty } from 'lingyang/icon';

<Table
  dataSource={[]}
  columns={columns}
  noDataElement={
    <div style={{ textAlign: 'center', padding: '40px 0', color: '#86909c' }}>
      <IconEmpty style={{ fontSize: 56, color: '#c9cdd4' }} />
      <div style={{ marginTop: 12, fontSize: 14 }}>暂无用户数据</div>
      <div style={{ marginTop: 4, fontSize: 12 }}>
        <Button type="text" onClick={handleCreate}>点击新建</Button>
      </div>
    </div>
  }
/>
```

### ellipsis 超长省略
```jsx
// tableLayoutFixed 是 ellipsis 生效的前提
<Table
  tableLayoutFixed
  dataSource={data}
  columns={[
    { title: '姓名',   dataIndex: 'name',   width: 100 },
    { title: '邮箱',   dataIndex: 'email',  width: 180, ellipsis: true, tooltip: true },
    { title: '备注',   dataIndex: 'remark', ellipsis: true, tooltip: true },  // 可不设 width
  ]}
  rowKey="id"
/>
```

### 行点击事件（onRow）
```jsx
<Table
  onRow={(record) => ({
    onClick: () => navigate(`/users/${record.id}`),
    style: { cursor: 'pointer' },
  })}
  rowClassName={(record) =>
    record.status === 'warning' ? 'row-warning' : ''
  }
/>
```

---

## 7. 合并单元格

```jsx
// 合并表头（colSpan）
const groupColumns = [
  {
    title: '基本信息',
    children: [
      { title: '姓名', dataIndex: 'name', width: 100 },
      { title: '年龄', dataIndex: 'age',  width: 80, align: 'right' as const },
    ],
  },
  {
    title: '联系方式',
    children: [
      { title: '手机', dataIndex: 'phone', width: 140 },
      { title: '邮箱', dataIndex: 'email', width: 180 },
    ],
  },
];

// 合并数据行（onCell 返回 rowSpan/colSpan）
const mergeColumns = [
  {
    title: '部门',
    dataIndex: 'dept',
    onCell: (record: any, index: number) => {
      // 同部门的行合并
      const rowSpan = computeRowSpan(data, index, 'dept');
      return { rowSpan };
    },
  },
  { title: '姓名', dataIndex: 'name' },
];

export default function MergedTable() {
  return (
    <div>
      <Typography.Title heading={6}>分组表头</Typography.Title>
      <Table columns={groupColumns} dataSource={data} rowKey="id" bordered />

      <Divider />

      <Typography.Title heading={6}>合并数据行</Typography.Title>
      <Table columns={mergeColumns} dataSource={deptData} rowKey="id" bordered />
    </div>
  );
}
```

---

## 8. 树形数据

```jsx
// 数据中含 children 字段时自动树形展示
const treeData = [
  {
    key: 'tech',
    name: '技术部',
    headCount: 45,
    children: [
      {
        key: 'frontend',
        name: '前端组',
        headCount: 12,
        children: [
          { key: 'fe-1', name: '张三', headCount: 1 },
          { key: 'fe-2', name: '李四', headCount: 1 },
        ],
      },
      {
        key: 'backend',
        name: '后端组',
        headCount: 18,
      },
    ],
  },
  {
    key: 'product',
    name: '产品部',
    headCount: 15,
  },
];

const treeColumns = [
  { title: '部门/成员', dataIndex: 'name', key: 'name' },
  { title: '人数', dataIndex: 'headCount', key: 'headCount', align: 'right' as const },
];

export default function TreeTable() {
  return (
    <Table
      columns={treeColumns}
      dataSource={treeData}
      rowKey="key"
      indentSize={24}               // 每层缩进 24px（默认 16）
      // childrenColumnName="subItems"  // 自定义子节点字段名（默认 'children'）
    />
  );
}
```

---

## 9. 企业级完整列表页模板

```jsx
import { useState, useEffect, useCallback } from 'react';
import {
  Table, Button, Space, Input, Select, Tag, Popconfirm,
  Modal, Form, Message, Card, Typography, Divider, Grid
} from 'lingyang';
import { IconSearch, IconPlus, IconRefresh } from 'lingyang/icon';

const { Row, Col } = Grid;

interface User {
  id: string;
  name: string;
  dept: string;
  role: string;
  status: 'active' | 'inactive';
  joinDate: string;
  email: string;
}

interface SearchParams {
  page: number;
  pageSize: number;
  keyword?: string;
  dept?: string;
  status?: string;
  sortField?: string;
  sortOrder?: 'ascend' | 'descend';
}

export default function UserListPage() {
  const [data, setData] = useState<User[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);
  const [selectedKeys, setSelectedKeys] = useState<(string | number)[]>([]);
  const [params, setParams] = useState<SearchParams>({ page: 1, pageSize: 10 });
  const [searchForm] = Form.useForm();

  // ---- 数据获取 ----
  const fetchData = useCallback(async (p: SearchParams) => {
    setLoading(true);
    try {
      const res = await UserApi.list(p);
      setData(res.list);
      setTotal(res.total);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchData(params); }, [params]);

  // ---- 列定义 ----
  const columns = [
    {
      title: '姓名',
      dataIndex: 'name',
      width: 120,
      fixed: 'left' as const,
      sorter: true,
      sortOrder: params.sortField === 'name' ? params.sortOrder : null,
    },
    {
      title: '部门',
      dataIndex: 'dept',
      width: 120,
      filters: [
        { text: '技术部', value: 'tech' },
        { text: '产品部', value: 'product' },
        { text: '运营部', value: 'ops' },
      ],
    },
    {
      title: '职位',
      dataIndex: 'role',
      width: 140,
    },
    {
      title: '邮箱',
      dataIndex: 'email',
      ellipsis: true,
      tooltip: true,
      width: 200,
    },
    {
      title: '入职日期',
      dataIndex: 'joinDate',
      width: 120,
      sorter: true,
      sortOrder: params.sortField === 'joinDate' ? params.sortOrder : null,
    },
    {
      title: '状态',
      dataIndex: 'status',
      width: 80,
      filters: [
        { text: '正常', value: 'active' },
        { text: '停用', value: 'inactive' },
      ],
      render: (s: string) => (
        <Tag color={s === 'active' ? 'green' : 'gray'}>
          {s === 'active' ? '正常' : '停用'}
        </Tag>
      ),
    },
    {
      title: '操作',
      key: 'action',
      width: 160,
      fixed: 'right' as const,
      render: (_: any, record: User) => (
        <Space split={<Divider type="vertical" />} size={0}>
          <Typography.Text
            type="primary"
            style={{ cursor: 'pointer', fontSize: 13 }}
            onClick={() => handleEdit(record)}
          >
            编辑
          </Typography.Text>
          <Popconfirm
            title="确认删除该用户？"
            onOk={() => handleDelete(record.id)}
          >
            <Typography.Text type="danger" style={{ cursor: 'pointer', fontSize: 13 }}>
              删除
            </Typography.Text>
          </Popconfirm>
        </Space>
      ),
    },
  ];

  // ---- 搜索 ----
  const handleSearch = () => {
    const values = searchForm.getFieldsValue();
    setParams({ ...params, page: 1, ...values });
  };

  const handleReset = () => {
    searchForm.resetFields();
    setParams({ page: 1, pageSize: params.pageSize });
  };

  // ---- 删除 ----
  const handleDelete = async (id: string) => {
    await UserApi.delete(id);
    Message.success('删除成功');
    fetchData(params);
  };

  const handleBatchDelete = async () => {
    await UserApi.batchDelete(selectedKeys as string[]);
    Message.success(`已删除 ${selectedKeys.length} 条记录`);
    setSelectedKeys([]);
    fetchData(params);
  };

  // ---- 渲染 ----
  return (
    <Card>
      {/* 搜索栏 */}
      <Form form={searchForm} layout="inline" style={{ marginBottom: 16 }}>
        <Row gutter={[12, 12]} style={{ width: '100%' }}>
          <Col xs={24} sm={8} md={6}>
            <Form.Item field="keyword" style={{ margin: 0 }}>
              <Input placeholder="搜索姓名/邮箱" prefix={<IconSearch />} allowClear />
            </Form.Item>
          </Col>
          <Col xs={24} sm={8} md={6}>
            <Form.Item field="dept" style={{ margin: 0 }}>
              <Select placeholder="选择部门" allowClear>
                <Select.Option value="tech">技术部</Select.Option>
                <Select.Option value="product">产品部</Select.Option>
                <Select.Option value="ops">运营部</Select.Option>
              </Select>
            </Form.Item>
          </Col>
          <Col xs={24} sm={8} md={6}>
            <Form.Item field="status" style={{ margin: 0 }}>
              <Select placeholder="选择状态" allowClear>
                <Select.Option value="active">正常</Select.Option>
                <Select.Option value="inactive">停用</Select.Option>
              </Select>
            </Form.Item>
          </Col>
          <Col xs={24} sm={24} md={6}>
            <Space>
              <Button type="primary" icon={<IconSearch />} onClick={handleSearch}>
                搜索
              </Button>
              <Button icon={<IconRefresh />} onClick={handleReset}>
                重置
              </Button>
            </Space>
          </Col>
        </Row>
      </Form>

      {/* 操作栏 */}
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 12 }}>
        <Space>
          {selectedKeys.length > 0 && (
            <>
              <Typography.Text type="secondary">
                已选 <strong>{selectedKeys.length}</strong> 条
              </Typography.Text>
              <Popconfirm
                title={`确认删除选中的 ${selectedKeys.length} 条？`}
                onOk={handleBatchDelete}
              >
                <Button size="small" status="danger">批量删除</Button>
              </Popconfirm>
              <Button size="small" onClick={() => setSelectedKeys([])}>取消选择</Button>
            </>
          )}
        </Space>
        <Button type="primary" icon={<IconPlus />} onClick={() => handleCreate()}>
          新增用户
        </Button>
      </div>

      {/* 表格 */}
      <Table
        rowKey="id"
        dataSource={data}
        columns={columns}
        loading={loading}
        stripe
        tableLayoutFixed
        scroll={{ x: 1200, y: 500 }}
        rowSelection={{
          type: 'checkbox',
          selectedRowKeys: selectedKeys,
          onChange: (keys) => setSelectedKeys(keys),
          preserveSelectedRowKeys: true,
        }}
        pagination={{
          current: params.page,
          pageSize: params.pageSize,
          total,
          showTotal: (t) => `共 ${t} 条`,
          showSizeChanger: true,
          pageSizeOptions: [10, 20, 50],
        }}
        onChange={(pagination, sorter, filters) => {
          setParams({
            ...params,
            page: pagination.current!,
            pageSize: pagination.pageSize!,
            sortField: (sorter as any).field,
            sortOrder: (sorter as any).order,
            dept: (filters.dept as string[])?.[0],
            status: (filters.status as string[])?.[0],
          });
        }}
        noDataElement={
          <div style={{ textAlign: 'center', padding: '40px 0', color: '#86909c' }}>
            <div style={{ fontSize: 14 }}>暂无用户数据</div>
            <Button type="text" style={{ marginTop: 8 }} onClick={() => handleCreate()}>
              立即新增
            </Button>
          </div>
        }
      />
    </Card>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-table · 完整 Props 类型定义

## 目录
- [TableProps](#tableprops)
- [ColumnProps](#columnpropst)
- [TableRowSelection](#tablerowselectiont)
- [TableExpandProps](#tableexpandpropst)
- [ScrollConfig](#scrollconfig)
- [SorterResult](#sorterresult)
- [与 Ant Design 差异详细对照](#与-ant-design-差异详细对照)

---

## TableProps

```typescript
interface TableProps<T = any> {
  /** 列配置数组（核心必填）*/
  columns: ColumnProps<T>[];

  /** 数据源数组（核心必填）*/
  dataSource: T[];

  /**
   * 行唯一标识。
   * - 字符串：使用该字段值作为 key（如 'id'）
   * - 函数：自定义 key 逻辑
   * 默认使用 'key' 字段。无 key 字段时必须显式指定，否则控制台 warning。
   * @default 'key'
   */
  rowKey?: string | ((record: T) => string | number);

  /**
   * 加载中状态。
   * true = 覆盖 Spin 遮罩；也可传 SpinProps 精细控制（indicator/tip/size）。
   * @default false
   */
  loading?: boolean | SpinProps;

  /**
   * 分页配置。
   * false = 关闭分页（一次性展示所有 dataSource）。
   * 传对象时支持 PaginationProps 全部属性。
   */
  pagination?: false | TablePaginationConfig;

  /** 行选择配置（详见 TableRowSelection）*/
  rowSelection?: TableRowSelection<T>;

  /**
   * 展开行配置（详见 TableExpandProps）。
   * 【命名差异】lingyang 用 expandProps；Ant Design 用 expandable。
   */
  expandProps?: TableExpandProps<T>;

  /**
   * 滚动配置。
   * - scroll.x：水平滚动（固定列时必须设置，建议略大于各列宽之和）
   * - scroll.y：垂直滚动/固定表头（设置后表头固定，内容区可滚动）
   * - scroll.minWidth：最小宽度
   * - scroll.maxHeight：最大高度（替代固定 y）
   */
  scroll?: {
    x?: number | string;
    y?: number | string;
    minWidth?: number | string;
    maxHeight?: number | string;
  };

  /** 是否显示完整边框（含单元格边框）。默认 false（仅有水平分隔线）*/
  bordered?: boolean;

  /**
   * 【lingyang 专有】斑马纹（奇偶行交替背景色）。
   * Ant Design 无此 prop。
   * @default false
   */
  stripe?: boolean;

  /**
   * 表格尺寸。
   * 'default' = 标准；'middle' = 中等行高；'small' = 紧凑（用于 Modal 内等空间受限场景）。
   * @default 'default'
   */
  size?: 'default' | 'middle' | 'small';

  /**
   * 【lingyang 专有】设置 table-layout: fixed。
   * - 固定后列宽不随内容变化，内容超出省略。
   * - ellipsis/tooltip 超长省略**必须**开启此项。
   * Ant Design 对应：tableLayout='fixed'。
   * @default false
   */
  tableLayoutFixed?: boolean;

  /**
   * 【lingyang 专有】开启虚拟滚动（Virtual List）。
   * - 大数据量（5000+ 行）时开启以提升渲染性能。
   * - 开启时 scroll.y 必须为 number 类型（不能是字符串）。
   * Ant Design 对应：scroll.y + virtual。
   * @default false
   */
  virtualized?: boolean;

  /** 是否显示表头。@default true */
  showHeader?: boolean;

  /** 表格标题区（显示在表格上方）*/
  title?: ReactNode | ((currentPageData: T[]) => ReactNode);

  /** 表格底部区域*/
  footer?: ReactNode | ((currentPageData: T[]) => ReactNode);

  /**
   * 固定汇总行（内置在表格 tfoot 区，滚动时不随数据行滚动）。
   * 使用 Table.Summary / Table.Summary.Row / Table.Summary.Cell 构建内容。
   */
  summary?: (currentPageData: T[]) => ReactNode;

  /**
   * 【lingyang 专有】数据为空时的自定义占位内容。
   * Ant Design 对应：locale.emptyText。
   */
  noDataElement?: ReactNode;

  /**
   * 行自定义 CSS 类名函数，可实现条件行高亮。
   * (record, index) => string
   */
  rowClassName?: (record: T, index: number) => string;

  /**
   * 行事件处理器配置。
   * 返回的对象会被展开到 <tr> 元素的属性上，支持 onClick/onDoubleClick/onMouseEnter 等。
   * (record, index) => React.HTMLAttributes<HTMLElement>
   */
  onRow?: (record: T, index: number) => React.HTMLAttributes<HTMLElement>;

  /**
   * 分页、排序、筛选变化时的统一回调。
   *
   * 【参数顺序差异】
   * lingyang: (pagination, sorter, filters, extra)
   * Ant Design: (pagination, filters, sorter, extra)
   *
   * @param pagination  当前分页状态
   * @param sorter      当前排序状态（多列排序时为数组）
   * @param filters     当前筛选状态 { [columnKey]: string[] }
   * @param extra       额外信息 { action: 'paginate'|'sort'|'filter', currentDataSource: T[] }
   */
  onChange?: (
    pagination: TablePaginationConfig,
    sorter: SorterResult<T> | SorterResult<T>[],
    filters: Record<string, string[] | null>,
    extra: { action: 'paginate' | 'sort' | 'filter'; currentDataSource: T[] }
  ) => void;

  /**
   * 受控排序状态（表格级）。
   * field: 当前排序列的 dataIndex；
   * direction: 'ascend'|'descend'；
   * mode: 'single'（默认）| 'multiple'（多列排序）。
   */
  sortOptions?: {
    field?: string;
    direction?: 'ascend' | 'descend';
    mode?: 'single' | 'multiple';
  };

  /** 受控筛选状态。{ [columnKey]: string[] } */
  filterOptions?: Record<string, string[]>;

  /** 树形数据每层缩进 px。@default 16 */
  indentSize?: number;

  /** 树形数据子节点字段名。@default 'children' */
  childrenColumnName?: string;

  style?: React.CSSProperties;
  className?: string;
}
```

---

## ColumnProps\<T\>

```typescript
interface ColumnProps<T = any> {
  /** 列标题（表头显示内容，必填）*/
  title: ReactNode;

  /** 数据字段名，支持点号路径如 'user.name'（访问嵌套字段）*/
  dataIndex?: string;

  /** 列唯一 key。无 dataIndex 的列（操作列等）必须显式设置 */
  key?: string;

  /** 列宽（px 数值或 CSS 字符串）。固定列时必须设置 */
  width?: number | string;

  /** 固定列方向。需配合 scroll.x 使用 */
  fixed?: 'left' | 'right';

  /** 单元格内容对齐方式。@default 'left' */
  align?: 'left' | 'center' | 'right';

  /**
   * 自定义单元格渲染函数。
   * 签名：(value, record, index) => ReactNode
   * 也可返回 { children: ReactNode, props: { colSpan?, rowSpan? } } 实现合并单元格。
   */
  render?: (value: any, record: T, index: number) => ReactNode | {
    children: ReactNode;
    props: { colSpan?: number; rowSpan?: number };
  };

  /**
   * 排序配置。
   * - true = 服务端排序，仅显示排序图标，由 onChange 处理
   * - 函数 = 本地排序比较函数，(a, b) => number（负数=a在前，正数=b在前）
   */
  sorter?: boolean | ((a: T, b: T) => number);

  /** 受控排序状态。null = 无排序 */
  sortOrder?: 'ascend' | 'descend' | null;

  /** 非受控初始排序方向 */
  defaultSortOrder?: 'ascend' | 'descend';

  /** 支持的排序方向切换顺序。@default ['ascend', 'descend'] */
  sortDirections?: ('ascend' | 'descend')[];

  /** 筛选菜单项列表。设置后表头出现漏斗图标 */
  filters?: { text: string; value: any; children?: any[] }[];

  /** 本地筛选函数。(value, record) => boolean。服务端筛选不需设置 */
  onFilter?: (value: any, record: T) => boolean;

  /** 筛选是否多选。@default true */
  filterMultiple?: boolean;

  /** 受控当前筛选值 */
  filteredValue?: any[] | null;

  /** 自定义筛选图标。filtered 参数表示是否有激活的筛选 */
  filterIcon?: ReactNode | ((filtered: boolean) => ReactNode);

  /**
   * 超出列宽时省略显示。
   * 必须配合 tableLayoutFixed 使用，否则不生效。
   * @default false
   */
  ellipsis?: boolean;

  /** ellipsis 时鼠标悬浮显示 Tooltip 提示完整内容 */
  tooltip?: boolean;

  /** 表头列合并数，设为 0 时该列表头不渲染 */
  colSpan?: number;

  /** 分组列头（等效 Table.ColumnGroup 的 children）*/
  children?: ColumnProps<T>[];

  /** 列单元格自定义 CSS 类名 */
  className?: string;

  /** 表头单元格自定义样式 */
  headerCellStyle?: React.CSSProperties;

  /** 数据行单元格自定义样式 */
  bodyCellStyle?: React.CSSProperties;

  /**
   * 单元格属性回调。用于合并单元格（colSpan/rowSpan）。
   * 返回 colSpan=0 或 rowSpan=0 时该单元格不渲染。
   */
  onCell?: (record: T, index: number) => {
    colSpan?: number;
    rowSpan?: number;
    [key: string]: any;
  };

  /** 表头单元格属性回调 */
  onHeaderCell?: (column: ColumnProps<T>) => object;
}
```

---

## TableRowSelection\<T\>

```typescript
interface TableRowSelection<T = any> {
  /** 选择类型。@default 'checkbox' */
  type?: 'checkbox' | 'radio';

  /** 受控选中 keys 数组 */
  selectedRowKeys?: (string | number)[];

  /** 非受控默认选中 keys */
  defaultSelectedRowKeys?: (string | number)[];

  /** 选中项变化回调 */
  onChange?: (selectedRowKeys: (string | number)[], selectedRows: T[]) => void;

  /** 单行选中/取消时回调 */
  onSelect?: (record: T, selected: boolean, selectedRows: T[]) => void;

  /** 全选/取消全选时回调 */
  onSelectAll?: (selected: boolean, selectedRows: T[], changeRows: T[]) => void;

  /**
   * 获取每行 Checkbox 的 props。
   * 常用于禁用某些行：{ disabled: record.status === 'locked' }
   */
  getCheckboxProps?: (record: T) => Partial<CheckboxProps>;

  /**
   * 翻页/筛选后是否保留已选中的 keys。
   * 服务端分页时必须设为 true，否则翻页后选中状态丢失。
   * @default false
   */
  preserveSelectedRowKeys?: boolean;

  /** 自定义选择列的渲染函数，替换默认 Checkbox */
  renderCell?: (checked: boolean, record: T, index: number, originNode: ReactNode) => ReactNode;

  /** 选择列 Checkbox 统一 props */
  checkboxProps?: Partial<CheckboxProps>;

  /** 选择列宽度 */
  columnWidth?: number | string;

  /** 自定义选择列表头内容 */
  columnTitle?: ReactNode;

  /** 是否固定选择列 */
  fixed?: boolean | 'left' | 'right';

  /** 批量操作菜单。true = 显示默认选项（全选当页、全选全部等）*/
  selections?: boolean | SelectionItem[];
}
```

---

## TableExpandProps\<T\>

```typescript
/**
 * lingyang 展开行配置对象名为 expandProps（Ant Design 对应 expandable）。
 */
interface TableExpandProps<T = any> {
  /**
   * 展开行内容渲染函数（核心，必填）。
   * (record, index) => ReactNode
   */
  expandedRowRender: (record: T, index: number) => ReactNode;

  /** 受控展开 keys */
  expandedRowKeys?: (string | number)[];

  /** 非受控初始展开 keys */
  defaultExpandedRowKeys?: (string | number)[];

  /** 默认展开所有行。@default false */
  defaultExpandAllRows?: boolean;

  /** 展开/收起某行时回调 */
  onExpand?: (expanded: boolean, record: T) => void;

  /** 展开行 keys 变化回调 */
  onExpandedRowsChange?: (expandedRowKeys: (string | number)[]) => void;

  /**
   * 控制某行是否可展开。
   * (record) => boolean。返回 false 则该行不显示展开图标。
   */
  rowExpandable?: (record: T) => boolean;

  /**
   * 自定义展开图标渲染。
   * ({ expanded, record, onExpand }) => ReactNode
   */
  renderExpandIcon?: (props: {
    expanded: boolean;
    record: T;
    onExpand: (record: T, e: React.MouseEvent) => void;
  }) => ReactNode;

  /** 点击行时触发展开（而非仅点图标）。@default false */
  expandRowByClick?: boolean;

  /** 展开图标所在列的序号（从 0 开始）*/
  expandIconColumnIndex?: number;

  /** 展开行的自定义 CSS 类名函数 */
  expandedRowClassName?: (record: T, index: number) => string;
}
```

---

## SorterResult

```typescript
interface SorterResult<T = any> {
  column?: ColumnProps<T>;   // 当前排序列的配置对象
  columnKey?: string;        // 排序列的 key 或 dataIndex
  field?: string | string[]; // 排序字段（dataIndex）
  order?: 'ascend' | 'descend'; // 排序方向，undefined = 无排序
}
```

---

## 与 Ant Design 差异详细对照

| 特性 | lingyang 写法 | Ant Design 写法 |
|---|---|---|
| 斑马纹 | `<Table stripe />` | ❌ 不支持 |
| 虚拟滚动 | `<Table virtualized scroll={{ y: 600 }} />` | `<Table virtual scroll={{ y: 600 }} />` |
| 空数据占位 | `<Table noDataElement={<Empty />} />` | `<Table locale={{ emptyText: <Empty /> }} />` |
| fixed 布局 | `<Table tableLayoutFixed />` | `<Table tableLayout="fixed" />` |
| 展开行配置 | `<Table expandProps={{ expandedRowRender, ... }} />` | `<Table expandable={{ expandedRowRender, ... }} />` |
| onChange 参数顺序 | `onChange(pagination, sorter, filters, extra)` | `onChange(pagination, filters, sorter, extra)` |
| 多列排序 | `sortOptions={{ mode: 'multiple' }}` | `onChange` 的 sorter 返回数组 |

---
