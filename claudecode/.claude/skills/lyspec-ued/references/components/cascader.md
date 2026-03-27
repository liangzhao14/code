# lingyang-cascader · 级联选择器组件 Skill

---

## 何时读取子文档

| 需求 | 读取文件 |
|---|---|
| 完整 TypeScript 类型定义 | `references/props.md` |
| 完整代码示例（7 大场景）| `references/examples.md` |

---

## ⚠️ lingyang vs Ant Design 关键差异

| 能力 | lingyang Cascader | Ant Design Cascader |
|---|---|---|
| 开启搜索 | `allowSearch` | `showSearch`（支持服务端搜索配置对象）|
| 自定义展示格式 | `renderFormat` | `displayRender` |
| 异步懒加载 | `loadMore(option, done)` | `loadData(selectedOptions)`（签名不同）|
| 下拉显隐受控 | `popupVisible` / `onVisibleChange` | `open` / `onDropdownVisibleChange` |
| 尺寸 | `mini/small/default/large`（4 档）| `small/middle/large`（3 档，无 mini）|
| 空子节点控制 | `showEmptyChildren` ✅ | ❌ 无 |

---

## CascaderProps 速查

| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `options` ★ | `CascaderOption[]` | `[]` | 选项数据源 |
| `value` | `CascaderValue` | — | 受控选中值 |
| `defaultValue` | `CascaderValue` | — | 非受控默认值 |
| `placeholder` | `string` | — | 占位文字 |
| `disabled` | `boolean` | `false` | 禁用 |
| `allowClear` | `boolean` | `false` | 清除按钮 |
| `allowSearch` | `boolean \| { retainInputValue? }` | `false` | 开启搜索（**≠ Ant Design 的 showSearch**）|
| `multiple` | `boolean` | `false` | 多选模式（默认开启搜索）|
| `checkStrictly` | `boolean` | `false` | 严格模式，可选中任意非叶子节点 |
| `pathMode` | `boolean` | `false` | value 是否为路径形式 |
| `expandTrigger` | `'click' \| 'hover'` | `'click'` | 展开下一级触发方式 |
| `size` | `'mini'\|'small'\|'default'\|'large'` | `'default'` | 尺寸（**mini 为 lingyang 专有**）|
| `status` | `'error'\|'warning'` | — | 校验状态（Form 自动注入）|
| `loading` | `boolean` | `false` | 加载中状态 |
| `fieldNames` | `{ label?, value?, children? }` | 见注① | 自定义字段名 |
| `renderFormat` | `(valueShow, value, pathValue) => ReactNode` | — | 自定义选中项展示（**≠ Ant Design 的 displayRender**）|
| `maxTagCount` | `number \| { count, render? }` | `0` | 多选最多显示标签数 |
| `showEmptyChildren` | `boolean` | `false` | **lingyang 专有** 是否渲染空 children 节点 |
| `loadMore` | `(option, done) => void` | — | 异步懒加载（**签名 ≠ Ant Design 的 loadData**）|
| `filterOption` | `false \| fn` | 按 label 匹配 | 自定义搜索过滤 |
| `dropdownRender` | `(menu) => ReactNode` | — | 自定义下拉面板 |
| `dropdownMenuColumnStyle` | `CSSProperties` | — | 每列菜单样式 |
| `popupVisible` | `boolean` | — | 受控下拉显隐（**≠ Ant Design 的 open**）|
| `getPopupContainer` | `(node) => HTMLElement` | — | 弹层挂载容器 |
| `onChange` | `(value, selectedOptions) => void` | — | 选中值变化回调 |
| `onSearch` | `(inputValue) => void` | — | 搜索回调 |
| `onClear` | `() => void` | — | 清除回调 |
| `onVisibleChange` | `(visible) => void` | — | 下拉显隐回调（**≠ Ant Design 的 onDropdownVisibleChange**）|

> ① fieldNames 默认值：`{ label: 'label', value: 'value', children: 'children' }`

---

## CascaderOption 结构

```typescript
interface CascaderOption {
  value: string | number;       // 选项值（必填）
  label: ReactNode;             // 显示文字（必填）
  children?: CascaderOption[];  // 子选项
  disabled?: boolean;           // 是否禁用
  isLeaf?: boolean;             // 标记叶子节点（loadMore 模式必用）
  tagProps?: TagProps;          // 多选时标签的 props
}
```

---

## value 格式说明

| 模式 | pathMode=false（默认） | pathMode=true |
|---|---|---|
| 单选 | `['province', 'city', 'district']`（完整路径） | `'district'`（仅叶子值）|
| 多选 | `[['province','city'],['p2','c2']]` | `['city1','city2']` |

---

## 高频场景速查

### 基础省市区选择
```jsx
const options = [
  { value: 'beijing', label: '北京', children: [
    { value: 'chaoyang', label: '朝阳区' },
    { value: 'haidian',  label: '海淀区' },
  ]},
  { value: 'shanghai', label: '上海', children: [
    { value: 'pudong',   label: '浦东新区' },
  ]},
];

<Cascader options={options} placeholder="请选择地区" allowClear />
```

### 受控用法
```jsx
const [value, setValue] = useState<string[]>([]);

<Cascader
  value={value}
  options={options}
  onChange={(v) => setValue(v as string[])}
  placeholder="请选择"
/>
```

### 多选
```jsx
<Cascader
  multiple
  options={options}
  placeholder="请选择（可多选）"
  maxTagCount={3}
  allowClear
/>
```

### 搜索
```jsx
// ⚠️ lingyang 用 allowSearch，Ant Design 用 showSearch
<Cascader allowSearch options={options} placeholder="可输入搜索" />
```

### checkStrictly — 选择任意层级
```jsx
<Cascader
  checkStrictly
  expandTrigger="hover"
  options={options}
  placeholder="可选任意层级"
/>
```

### loadMore 异步懒加载
```jsx
// ⚠️ 签名与 Ant Design loadData 不同：lingyang 是 (option, done)
const initialOptions = [
  { value: 'beijing', label: '北京', isLeaf: false },
];

const loadMore = (option, done) => {
  setTimeout(() => {
    done([
      { value: 'chaoyang', label: '朝阳区', isLeaf: true },
      { value: 'haidian',  label: '海淀区', isLeaf: true },
    ]);
  }, 500);
};

<Cascader
  options={options}
  loadMore={loadMore}
  placeholder="选择地区（动态加载）"
/>
```

### renderFormat 自定义展示
```jsx
// ⚠️ lingyang 用 renderFormat，Ant Design 用 displayRender
<Cascader
  options={options}
  renderFormat={(valueShow) => valueShow.map(v =>
    typeof v === 'string' ? v : v.label
  ).join(' / ')}
  placeholder="自定义显示格式"
/>

// 仅显示最后一级（常用场景）
<Cascader
  options={options}
  renderFormat={(valueShow) => {
    const last = valueShow[valueShow.length - 1];
    return typeof last === 'string' ? last : last?.label;
  }}
/>
```

### fieldNames 自定义字段名
```jsx
// 后端数据字段名不是 label/value/children 时使用
const regionData = [
  { id: 'bj', name: '北京', subList: [
    { id: 'cy', name: '朝阳区', subList: [] },
  ]},
];

<Cascader
  options={regionData}
  fieldNames={{ value: 'id', label: 'name', children: 'subList' }}
  placeholder="请选择地区"
/>
```

### 在 Form 中使用
```jsx
// lingyang Form.Item 用 field 绑定（非 Ant Design 的 name）
<Form.Item
  field="address"
  label="所在地区"
  rules={[{ required: true, message: '请选择地区' }]}
>
  <Cascader
    options={regionOptions}
    placeholder="请选择省/市/区"
    allowClear
  />
</Form.Item>
```

---

## CSS 类名速查

| 场景 | 类名 |
|---|---|
| 容器 | `.lingyang-cascader` |
| 下拉弹窗 | `.lingyang-cascader-popup` |
| 面板 | `.lingyang-cascader-panel` |
| 每列菜单 | `.lingyang-cascader-panel-column` |
| 选项 | `.lingyang-cascader-option` |
| 选中选项 | `.lingyang-cascader-option-selected` |
| 禁用选项 | `.lingyang-cascader-option-disabled` |
| 多选标签 | `.lingyang-cascader-tag` |
| 搜索框 | `.lingyang-cascader-search-input` |
| 无结果 | `.lingyang-cascader-not-found` |
-e 

---

## 完整代码示例

# lingyang-cascader · 完整代码示例库

## 目录
1. [基础用法](#1-基础用法)
2. [多选模式](#2-多选模式)
3. [allowSearch 搜索](#3-allowsearch-搜索)
4. [checkStrictly 选择任意层级](#4-checkstrictly-选择任意层级)
5. [loadMore 异步懒加载](#5-loadmore-异步懒加载)
6. [renderFormat 自定义展示](#6-renderformat-自定义展示)
7. [fieldNames 自定义字段名](#7-fieldnames-自定义字段名)
8. [在 Form 中使用（完整表单）](#8-在-form-中使用)

---

## 1. 基础用法

```jsx
import { Cascader } from 'lingyang';
import { useState } from 'react';

const regionOptions = [
  {
    value: 'beijing',
    label: '北京',
    children: [
      { value: 'chaoyang', label: '朝阳区' },
      { value: 'haidian',  label: '海淀区' },
      { value: 'dongcheng',label: '东城区' },
    ],
  },
  {
    value: 'shanghai',
    label: '上海',
    children: [
      { value: 'pudong',   label: '浦东新区' },
      { value: 'huangpu',  label: '黄浦区' },
    ],
  },
  {
    value: 'guangzhou',
    label: '广州',
    children: [
      { value: 'tianhe',   label: '天河区' },
      { value: 'haizhu',   label: '海珠区' },
    ],
  },
];

// 非受控（简单只读场景）
<Cascader options={regionOptions} placeholder="请选择省/市/区" allowClear />

// 受控（推荐，配合表单状态管理）
function RegionSelect() {
  const [value, setValue] = useState<(string | number)[]>([]);

  return (
    <Cascader
      value={value}
      options={regionOptions}
      onChange={(v) => setValue(v as (string | number)[])}
      placeholder="请选择省/市/区"
      allowClear
    />
  );
}

// hover 展开子菜单（层级多时体验更好）
<Cascader
  options={regionOptions}
  expandTrigger="hover"
  placeholder="悬停展开"
/>
```

---

## 2. 多选模式

```jsx
import { Cascader } from 'lingyang';
import { useState } from 'react';

const categoryOptions = [
  {
    value: 'electronics',
    label: '电子产品',
    children: [
      { value: 'phone',    label: '手机' },
      { value: 'laptop',   label: '笔记本' },
      { value: 'tablet',   label: '平板' },
    ],
  },
  {
    value: 'clothing',
    label: '服装',
    children: [
      { value: 'menswear', label: '男装' },
      { value: 'womenswear', label: '女装' },
      { value: 'kids',     label: '童装' },
    ],
  },
];

// 基础多选（多选时自动开启搜索）
<Cascader
  multiple
  options={categoryOptions}
  placeholder="请选择商品分类（可多选）"
  allowClear
/>

// 多选 + 限制标签显示数量
function MultiSelect() {
  const [value, setValue] = useState<(string | number)[][]>([]);

  return (
    <Cascader
      multiple
      value={value}
      options={categoryOptions}
      onChange={(v) => setValue(v as (string | number)[][])}
      maxTagCount={3}  // 最多展示3个标签，其余折叠
      placeholder="请选择分类"
      allowClear
    />
  );
}

// 多选 + 自定义折叠展示
<Cascader
  multiple
  options={categoryOptions}
  maxTagCount={{
    count: 2,
    render: (count) => <span style={{ color: '#165DFF' }}>+{count}项</span>,
  }}
  placeholder="选择分类"
/>
```

---

## 3. allowSearch 搜索

```jsx
// ⚠️ 命名差异：lingyang 用 allowSearch，Ant Design 用 showSearch

// 单选 + 搜索
<Cascader
  allowSearch
  options={regionOptions}
  placeholder="输入关键词搜索"
  allowClear
/>

// 关闭下拉后保留搜索输入值（适合频繁搜索场景）
<Cascader
  allowSearch={{ retainInputValue: true }}
  options={regionOptions}
  placeholder="关闭后保留搜索词"
/>

// 多选时默认开启搜索，无需显式设置 allowSearch
<Cascader
  multiple
  options={regionOptions}
  placeholder="多选（自动开启搜索）"
/>

// 自定义搜索匹配逻辑（按 value 和 label 双向匹配）
<Cascader
  allowSearch
  options={regionOptions}
  filterOption={(inputValue, option) =>
    String(option.value).toLowerCase().includes(inputValue.toLowerCase()) ||
    String(option.label).toLowerCase().includes(inputValue.toLowerCase())
  }
  placeholder="按值或标签搜索"
/>

// 服务端搜索（onSearch 触发接口）
function ServerSearch() {
  const [options, setOptions] = useState(initialOptions);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (keyword: string) => {
    if (!keyword) return;
    setLoading(true);
    try {
      const result = await searchApi(keyword);
      setOptions(result);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Cascader
      allowSearch
      filterOption={false}     // 禁用前端过滤，全部交给后端
      loading={loading}
      options={options}
      onSearch={handleSearch}
      placeholder="输入关键词服务端搜索"
    />
  );
}
```

---

## 4. checkStrictly 选择任意层级

```jsx
// 常用场景：组织架构（只需选到部门，不必选到具体人）、
//           商品大类（只选大类，不选具体SKU）

// 基础 checkStrictly（可选任意层级）
<Cascader
  checkStrictly
  options={regionOptions}
  placeholder="可选省/市/区任意层级"
/>

// checkStrictly + hover 展开（推荐组合）
// 原因：click 展开时，点击非叶子节点会立即选中并关闭，用户无法展开子级
// hover 展开时，悬停即展开，点击才选中，体验更好
<Cascader
  checkStrictly
  expandTrigger="hover"
  options={orgOptions}
  placeholder="选择部门（可选任意层级）"
  allowClear
/>

// checkStrictly + 多选（各层级独立打勾）
<Cascader
  multiple
  checkStrictly
  options={categoryOptions}
  placeholder="多选任意层级"
/>
```

---

## 5. loadMore 异步懒加载

```jsx
// ⚠️ 签名差异：
// lingyang：loadMore(option, done) → done(children)
// Ant Design：loadData(selectedOptions) → selectedOptions 最后一项.loading = false

import { useState } from 'react';
import { Cascader } from 'lingyang';

function LazyLoadCascader() {
  const [options, setOptions] = useState([
    { value: 'beijing',  label: '北京',  isLeaf: false },
    { value: 'shanghai', label: '上海',  isLeaf: false },
    { value: 'tianjin',  label: '天津',  isLeaf: false },
  ]);

  const loadMore = (option: any, done: (children?: any[]) => void) => {
    // 模拟异步请求，实际替换为 API 调用
    setTimeout(() => {
      // 根据父节点 value 加载对应子节点
      const childrenMap: Record<string, any[]> = {
        beijing:  [
          { value: 'chaoyang', label: '朝阳区', isLeaf: true },
          { value: 'haidian',  label: '海淀区', isLeaf: true },
        ],
        shanghai: [
          { value: 'pudong',   label: '浦东新区', isLeaf: true },
          { value: 'huangpu',  label: '黄浦区',   isLeaf: true },
        ],
        tianjin:  [
          { value: 'binhai',   label: '滨海新区', isLeaf: true },
        ],
      };
      done(childrenMap[option.value] || []);
    }, 600);
  };

  return (
    <Cascader
      options={options}
      loadMore={loadMore}
      placeholder="选择地区（动态加载）"
      allowClear
    />
  );
}

// 多级懒加载（省 → 市 → 区，每级都异步加载）
function MultiLevelLazy() {
  const [options, setOptions] = useState([
    { value: 'bj', label: '北京', isLeaf: false },
    { value: 'sh', label: '上海', isLeaf: false },
  ]);

  const loadMore = async (option: any, done: (children?: any[]) => void) => {
    try {
      // 真实场景：根据 option.value（父节点ID）请求接口
      const children = await regionApi.getChildren(option.value);
      done(children.map(item => ({
        value: item.code,
        label: item.name,
        isLeaf: item.level >= 3,   // 第3级为叶子节点
      })));
    } catch {
      done([]);  // 加载失败时传空数组
    }
  };

  return (
    <Cascader
      options={options}
      loadMore={loadMore}
      placeholder="省/市/区（逐级加载）"
    />
  );
}
```

---

## 6. renderFormat 自定义展示

```jsx
// ⚠️ 命名差异：lingyang 用 renderFormat，Ant Design 用 displayRender

// 仅显示最后一级（最常用场景，避免显示完整路径过长）
<Cascader
  options={regionOptions}
  renderFormat={(valueShow) => {
    const last = valueShow[valueShow.length - 1];
    return typeof last === 'string' ? last : (last as any)?.label;
  }}
  placeholder="仅显示最后一级"
/>

// 自定义分隔符
<Cascader
  options={regionOptions}
  renderFormat={(valueShow) =>
    valueShow.map(v => typeof v === 'string' ? v : (v as any).label).join(' > ')
  }
  placeholder="用 > 分隔"
/>

// 多选时自定义标签样式（通过 CascaderOption.tagProps）
const optionsWithTags = [
  {
    value: 'tech',
    label: '技术部',
    children: [
      {
        value: 'frontend',
        label: '前端组',
        tagProps: { color: 'arcoblue' },  // 标签蓝色
        isLeaf: true,
      },
      {
        value: 'backend',
        label: '后端组',
        tagProps: { color: 'green' },      // 标签绿色
        isLeaf: true,
      },
    ],
  },
];

<Cascader multiple options={optionsWithTags} placeholder="选择团队" />
```

---

## 7. fieldNames 自定义字段名

```jsx
// 后端返回的数据字段名不是 label/value/children 时使用
// （与 Ant Design 同名，行为一致）

// 场景1：后端返回 id/name/subList
const deptData = [
  {
    id: 'tech',
    name: '技术部',
    subList: [
      { id: 'fe', name: '前端组', subList: [] },
      { id: 'be', name: '后端组', subList: [] },
    ],
  },
  {
    id: 'product',
    name: '产品部',
    subList: [
      { id: 'pm', name: '产品经理组', subList: [] },
    ],
  },
];

<Cascader
  options={deptData}
  fieldNames={{ value: 'id', label: 'name', children: 'subList' }}
  placeholder="请选择部门"
/>

// 场景2：后端返回 code/text/nextLevel（三字段均不同）
const classifyData = [
  {
    code: '01',
    text: '食品饮料',
    nextLevel: [
      { code: '0101', text: '饮料', nextLevel: [] },
      { code: '0102', text: '零食', nextLevel: [] },
    ],
  },
];

<Cascader
  options={classifyData}
  fieldNames={{ value: 'code', label: 'text', children: 'nextLevel' }}
  placeholder="请选择商品分类"
  allowSearch
/>
```

---

## 8. 在 Form 中使用

```jsx
import { Form, Cascader, Grid, Button, Message } from 'lingyang';
import { useState } from 'react';

const { Row, Col } = Grid;

// ⚠️ lingyang Form.Item 用 field 绑定（不是 Ant Design 的 name）
// Form 自动向 Cascader 注入 value、onChange、status，无需手动传

const regionOptions = [/* ... 省市区数据 ... */];
const categoryOptions = [/* ... 分类数据 ... */];

function AddressForm() {
  const [form] = Form.useForm();

  const handleSubmit = async () => {
    try {
      const values = await form.validate();
      console.log('表单数据:', values);
      // values.region  => ['beijing', 'chaoyang']
      // values.categories => [['electronics','phone'], ['clothing','menswear']]
      Message.success('提交成功');
    } catch (e) {
      Message.error('请检查表单');
    }
  };

  return (
    <Form form={form} layout="vertical">
      <Row gutter={16}>
        {/* 单选地区 */}
        <Col span={12}>
          <Form.Item
            field="region"
            label="所在地区"
            rules={[{ required: true, message: '请选择地区' }]}
          >
            <Cascader
              options={regionOptions}
              placeholder="请选择省/市/区"
              allowClear
            />
          </Form.Item>
        </Col>

        {/* 多选商品分类 */}
        <Col span={12}>
          <Form.Item
            field="categories"
            label="商品分类"
            rules={[
              { required: true, message: '请选择分类' },
              {
                validator: (v, cb) => {
                  if (v && v.length > 5) return cb('最多选择5个分类');
                  cb();
                },
              },
            ]}
          >
            <Cascader
              multiple
              options={categoryOptions}
              placeholder="请选择（可多选）"
              maxTagCount={3}
              allowClear
            />
          </Form.Item>
        </Col>

        {/* 仅显示最后一级 */}
        <Col span={12}>
          <Form.Item field="dept" label="所属部门">
            <Cascader
              options={orgOptions}
              checkStrictly
              expandTrigger="hover"
              renderFormat={(valueShow) => {
                const last = valueShow[valueShow.length - 1];
                return typeof last === 'string' ? last : (last as any)?.label;
              }}
              placeholder="选择部门（可选任意层级）"
              allowClear
            />
          </Form.Item>
        </Col>

        {/* 异步加载 + 自定义字段名 */}
        <Col span={12}>
          <Form.Item field="location" label="配送地址">
            <Cascader
              options={[
                { areaCode: 'bj', areaName: '北京', children: [] },
              ]}
              fieldNames={{ value: 'areaCode', label: 'areaName' }}
              loadMore={(option, done) => {
                regionApi.getChildren(option.areaCode).then(list => {
                  done(list.map(item => ({
                    areaCode: item.code,
                    areaName: item.name,
                    isLeaf: item.isLeaf,
                  })));
                });
              }}
              placeholder="选择配送地址"
            />
          </Form.Item>
        </Col>
      </Row>

      <Form.Item>
        <Button type="primary" onClick={handleSubmit}>提交</Button>
        <Button style={{ marginLeft: 8 }} onClick={() => form.resetFields()}>重置</Button>
      </Form.Item>
    </Form>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-cascader · 完整 Props 类型定义

## 目录
- [CascaderProps（主组件）](#cascaderprops)
- [CascaderOption（选项数据）](#cascaderoption)
- [CascaderValue（值类型）](#cascadervalue)
- [与 Ant Design 差异详细对照](#与-ant-design-差异详细对照)

---

## CascaderProps

```typescript
interface CascaderProps {
  // ─── 数据 ────────────────────────────────────────────
  /**
   * 级联选项数据源（必填）
   * @default []
   */
  options: CascaderOption[];

  /**
   * 受控选中值。
   * - 单选 pathMode=false（默认）：string[]，如 ['beijing', 'chaoyang']
   * - 单选 pathMode=true：string，如 'chaoyang'
   * - 多选 pathMode=false：(string[])[]，如 [['bj','cy'],['sh','pd']]
   * - 多选 pathMode=true：string[]，如 ['cy', 'pd']
   */
  value?: CascaderValue;

  /** 非受控默认值，格式同 value */
  defaultValue?: CascaderValue;

  /**
   * 自定义字段名。默认 { label: 'label', value: 'value', children: 'children' }。
   * 后端数据字段名不符合默认规范时使用，与 Ant Design 同名。
   */
  fieldNames?: {
    label?: string;
    value?: string;
    children?: string;
    disabled?: string;
    isLeaf?: string;
  };

  // ─── 选择模式 ─────────────────────────────────────────
  /**
   * 是否为多选模式。多选时默认自动开启 allowSearch。
   * @default false
   */
  multiple?: boolean;

  /**
   * 严格模式：父子节点选中互不关联，可选中任意非叶子节点（中间层级）。
   * 单选时常配合 expandTrigger="hover" 使用。
   * @default false
   */
  checkStrictly?: boolean;

  /**
   * 绑定值是否为路径形式。
   * - false（默认）：value 为完整路径数组，如 ['beijing', 'chaoyang']
   * - true：value 仅为叶子节点值，如 'chaoyang'
   * @default false
   */
  pathMode?: boolean;

  /**
   * 展开下一级的触发方式。
   * - 'click'：点击展开（默认，适合大多数场景）
   * - 'hover'：悬停展开（适合数据层级多、操作频繁的场景）
   * @default 'click'
   */
  expandTrigger?: 'click' | 'hover';

  // ─── 搜索 ────────────────────────────────────────────
  /**
   * 是否允许搜索。
   * - false（默认，单选时）
   * - true（多选时自动开启）
   * - { retainInputValue?: boolean }：retainInputValue=true 时关闭下拉后保留搜索输入值
   *
   * 【命名差异】lingyang 用 allowSearch；Ant Design 用 showSearch（支持服务端搜索配置对象）
   */
  allowSearch?: boolean | { retainInputValue?: boolean };

  /**
   * 自定义搜索过滤函数。
   * - false：禁用过滤（所有选项均显示）
   * - 函数：自定义过滤逻辑
   * @default 按各级 label 进行模糊匹配
   * @param inputValue 搜索输入值
   * @param option 当前选项
   * @param level 当前层级（从 0 开始）
   */
  filterOption?: false | ((inputValue: string, option: CascaderOption, level: number) => boolean);

  // ─── 展示 ────────────────────────────────────────────
  /** 占位提示文字 */
  placeholder?: string;

  /**
   * 自定义选中项展示格式。
   * 【命名差异】lingyang 用 renderFormat；Ant Design 用 displayRender。
   *
   * @param valueShow 当前展示值数组（每项为 string 或 CascaderOption）
   * @param value 当前选中路径数组
   * @param pathValue 当前选中路径对应的完整 CascaderOption 数组
   */
  renderFormat?: (
    valueShow: (string | CascaderOption)[],
    value: (string | number)[],
    pathValue: CascaderOption[]
  ) => ReactNode;

  /**
   * 多选模式下最多显示的标签数量，超出部分折叠显示。
   * - number：最大数量，0 表示不限制
   * - { count: number, render?: (invisibleTagCount: number) => ReactNode }：自定义折叠展示
   * @default 0（不限制）
   */
  maxTagCount?: number | { count: number; render?: (invisibleTagCount: number) => ReactNode };

  /**
   * 【lingyang 专有】是否渲染空 children 的节点（Ant Design 无此属性）。
   * - false（默认）：有 children 字段但为空数组时，节点被视为叶子节点
   * - true：即使 children 为空数组，也渲染展开箭头
   * @default false
   */
  showEmptyChildren?: boolean;

  // ─── 状态 ────────────────────────────────────────────
  /** 是否禁用 @default false */
  disabled?: boolean;

  /** 是否显示清除按钮 @default false */
  allowClear?: boolean;

  /**
   * 是否显示加载中状态
   * @default false
   * @version 2.15.0
   */
  loading?: boolean;

  /**
   * 校验状态（通常由 Form.Item 根据校验结果自动注入，无需手动设置）
   * - 'error'：红色边框
   * - 'warning'：橙色边框
   */
  status?: 'error' | 'warning';

  /** 组件尺寸。mini 为 lingyang 专有，Ant Design 无此档位。 @default 'default' */
  size?: 'mini' | 'small' | 'default' | 'large';

  // ─── 异步加载 ─────────────────────────────────────────
  /**
   * 异步懒加载函数。传入时开启懒加载模式。
   * 点击非叶子节点（isLeaf=false）时调用，done 回调传入子选项列表。
   *
   * 【签名差异】lingyang loadMore(option, done) ≠ Ant Design loadData(selectedOptions)
   * - lingyang：直接传入当前点击节点 + done 回调
   * - Ant Design：传入已选路径数组（需取最后一项）
   *
   * @param option 当前被点击（展开）的选项
   * @param done 数据加载完毕后调用，传入子选项数组；不传则清空子级
   */
  loadMore?: (
    option: CascaderOption,
    done: (children?: CascaderOption[]) => void
  ) => void;

  // ─── 弹窗控制 ─────────────────────────────────────────
  /**
   * 受控的下拉框显示状态。
   * 【命名差异】lingyang 用 popupVisible；Ant Design 用 open。
   */
  popupVisible?: boolean;

  /**
   * 非受控的下拉框初始显示状态。
   * @default false
   */
  defaultPopupVisible?: boolean;

  /**
   * 弹出层挂载的父节点。
   * 用于避免弹层被遮挡（如在 Modal、Drawer 内部使用时传入容器元素）。
   */
  getPopupContainer?: (triggerNode: HTMLElement) => HTMLElement;

  /** 触发器的额外 props（控制弹窗动画、定位等） */
  triggerProps?: TriggerProps;

  // ─── 自定义渲染 ───────────────────────────────────────
  /**
   * 自定义下拉菜单内容（包裹整个弹出面板）。
   * 可在面板顶部/底部注入自定义操作按钮。
   */
  dropdownRender?: (menu: ReactNode) => ReactNode;

  /** 每列菜单的自定义样式（用于统一各级面板列宽）*/
  dropdownMenuColumnStyle?: React.CSSProperties;

  /** 选择框前缀图标 */
  prefix?: ReactNode;

  /** 自定义后缀图标（替换默认下拉箭头）*/
  suffixIcon?: ReactNode;

  /** 自定义清除按钮图标 */
  clearIcon?: ReactNode;

  /** 搜索无结果时的占位内容 @default '无匹配选项' */
  notFoundContent?: ReactNode;

  // ─── 样式 ────────────────────────────────────────────
  style?: React.CSSProperties;
  className?: string;

  // ─── 事件 ────────────────────────────────────────────
  /**
   * 选中值改变时触发。
   * value 格式受 pathMode 影响；selectedOptions 为每条路径的完整选项对象数组。
   */
  onChange?: (value: CascaderValue, selectedOptions: CascaderOption[][]) => void;

  /** 用户输入搜索内容时触发 */
  onSearch?: (inputValue: string) => void;

  /** 点击清除按钮时触发 */
  onClear?: () => void;

  /**
   * 下拉框显隐状态变化时触发。
   * 【命名差异】lingyang 用 onVisibleChange；Ant Design 用 onDropdownVisibleChange。
   */
  onVisibleChange?: (visible: boolean) => void;

  /** 聚焦时触发 */
  onFocus?: (event: React.FocusEvent) => void;

  /** 失焦时触发 */
  onBlur?: (event: React.FocusEvent) => void;
}
```

---

## CascaderOption

```typescript
interface CascaderOption {
  /** 选项唯一标识值（对应 fieldNames.value，默认字段名为 'value'）*/
  value: string | number;

  /** 选项展示文字（对应 fieldNames.label，默认字段名为 'label'）*/
  label: ReactNode;

  /** 子选项数组（对应 fieldNames.children，默认字段名为 'children'）*/
  children?: CascaderOption[];

  /** 是否禁用该选项 @default false */
  disabled?: boolean;

  /**
   * 标记为叶子节点（仅在 loadMore 懒加载模式中有效）。
   * - true：显示为叶子节点，点击不展开、不触发 loadMore
   * - false（或未设置）：有展开箭头，点击触发 loadMore 加载子数据
   */
  isLeaf?: boolean;

  /**
   * 多选模式下该选项对应 Tag 标签的 props。
   * 可自定义标签颜色、图标等样式。
   * @version 2.8.0
   */
  tagProps?: TagProps;
}
```

---

## CascaderValue

```typescript
/** 单选 pathMode=false（默认）：完整路径数组 */
type SingleValue = (string | number)[];

/** 单选 pathMode=true：仅叶子节点值 */
type SinglePathValue = string | number;

/** 多选 pathMode=false：多条完整路径 */
type MultipleValue = (string | number)[][];

/** 多选 pathMode=true：多个叶子节点值 */
type MultiplePathValue = (string | number)[];

type CascaderValue =
  | SingleValue
  | SinglePathValue
  | MultipleValue
  | MultiplePathValue
  | undefined;
```

---

## 与 Ant Design 差异详细对照

| 特性 | lingyang 写法 | Ant Design 写法 |
|---|---|---|
| 开启搜索 | `allowSearch={true}` | `showSearch={true}` |
| 自定义选中展示 | `renderFormat={(v) => ...}` | `displayRender={(labels) => ...}` |
| 懒加载函数 | `loadMore={(option, done) => { done(children) }}` | `loadData={(selectedOptions) => { 最后一项.loading = false }}` |
| 受控下拉 | `popupVisible={open}` | `open={open}` |
| 下拉显隐回调 | `onVisibleChange={(v) => ...}` | `onDropdownVisibleChange={(v) => ...}` |
| 尺寸 | `size="mini"` ✅ | ❌ 无 mini |
| 空子节点 | `showEmptyChildren` ✅ | ❌ 无 |
| Form 绑定 | `<Form.Item field="addr">` | `<Form.Item name="addr">` |

---
