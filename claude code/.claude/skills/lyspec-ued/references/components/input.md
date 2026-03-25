# lingyang-input · 输入框组件 Skill

**子组件**：`Input` / `Input.TextArea` / `Input.Password` / `Input.Search` / `Input.Group`

---

## 何时读取子文档

| 需求 | 读取文件 |
|---|---|
| 完整 TypeScript 类型定义（所有接口） | `references/props.md` |
| 完整代码示例（8 大场景） | `references/examples.md` |

---

## ⚠️ lingyang vs Ant Design 关键差异

| 能力 | lingyang Input | Ant Design Input |
|---|---|---|
| 尺寸 | `mini / small / default / large`（4 档）| `small / middle / large`（3 档，无 mini）|
| onChange 参数 | `(value: string, event)` 第一个是**字符串** | `(event)` 需自行 `e.target.value` |
| 格式化输入值 | `normalize` prop | ❌ 无 |
| 前置/后置 | `addBefore` / `addAfter` | `addonBefore` / `addonAfter`（命名不同）|
| 搜索按钮 | `searchButton` | `enterButton`（命名不同）|

---

## Input Props 速查

| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `value` | `string` | — | 受控值 |
| `defaultValue` | `string` | — | 非受控默认值 |
| `placeholder` | `string` | — | 占位提示文字 |
| `disabled` | `boolean` | `false` | 禁用 |
| `readOnly` | `boolean` | `false` | 只读 |
| `maxLength` | `number \| { length, errorOnly? }` | — | 最大长度；errorOnly=true 仅标红不截断 |
| `showWordLimit` | `boolean` | `false` | 显示字数统计（配合 maxLength）|
| `allowClear` | `boolean \| { clearIcon? }` | `false` | 清除按钮 |
| `size` | `'mini'\|'small'\|'default'\|'large'` | `'default'` | 尺寸（**mini 为 lingyang 专有**）|
| `status` | `'error'\|'warning'` | — | 校验状态（Form 自动注入）|
| `prefix` | `ReactNode` | — | 框内前置图标 |
| `suffix` | `ReactNode` | — | 框内后置图标 |
| `addBefore` | `ReactNode` | — | 框外前置内容（灰色区域）|
| `addAfter` | `ReactNode` | — | 框外后置内容（灰色区域）|
| `normalize` | `(value: string) => string` | — | **lingyang 专有** 输入值格式化 |
| `autoFocus` | `boolean` | `false` | 自动聚焦 |
| `autoWidth` | `boolean \| { minWidth?, maxWidth? }` | `false` | 宽度自适应内容 |
| `onChange` | `(value: string, event) => void` | — | 值变化回调（**第一参数为字符串**）|
| `onPressEnter` | `(event) => void` | — | Enter 键回调 |
| `onClear` | `() => void` | — | 清除按钮点击回调 |

---

## 子组件专有 Props

### Input.TextArea
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `autoSize` | `boolean \| { minRows?, maxRows? }` | `false` | 高度自适应 |
| `rows` | `number` | `4` | 固定行数（autoSize 优先）|
| `showWordLimit` | `boolean` | `false` | 字数统计 |
| `wrapperStyle` | `CSSProperties` | — | 包裹层样式 |

### Input.Password
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `visibilityToggle` | `boolean` | `true` | 是否显示眼睛图标 |
| `visibility` | `boolean` | — | 受控明文/密文状态 |
| `defaultVisibility` | `boolean` | `false` | 非受控初始可见状态 |
| `onVisibilityChange` | `(visible: boolean) => void` | — | 切换可见回调 |

### Input.Search
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `searchButton` | `boolean \| ReactNode` | `false` | 搜索按钮（**非 Ant Design 的 enterButton**）|
| `loading` | `boolean` | `false` | 搜索 loading |
| `onSearch` | `(value: string) => void` | — | 点击搜索/Enter 回调 |

### Input.Group
| Prop | 类型 | 默认 | 说明 |
|---|---|---|---|
| `compact` | `boolean` | `false` | 紧凑模式（边框合并）|

---

## 高频场景速查

### 基础用法
```jsx
// 非受控
<Input placeholder="请输入用户名" allowClear />

// 受控
<Input value={value} onChange={(v) => setValue(v)} placeholder="请输入" />
```

### 前缀/后缀 vs 前置/后置
```jsx
// prefix/suffix：在边框内部，适合图标
<Input prefix={<IconUser />} suffix={<IconSearch />} />

// addBefore/addAfter：在边框外，灰色背景区域，适合固定文字或下拉
<Input addBefore="https://" addAfter=".com" placeholder="输入域名" />
<Input addBefore={<Select defaultValue="86" style={{ width: 70 }}><Option value="86">+86</Option></Select>} placeholder="手机号" />
```

### normalize 格式化（lingyang 专有）
```jsx
// 自动转大写
<Input normalize={(v) => v.toUpperCase()} placeholder="自动转大写" />

// 只允许数字
<Input normalize={(v) => v.replace(/[^0-9]/g, '')} placeholder="只能输入数字" />
```

### 字数限制
```jsx
<Input maxLength={50} showWordLimit placeholder="最多50字" />
// errorOnly=true：超出时标红但不截断
<Input maxLength={{ length: 100, errorOnly: true }} showWordLimit />
```

### 四种尺寸
```jsx
<Input size="mini"    placeholder="mini（24px）" />
<Input size="small"   placeholder="small（28px）" />
<Input size="default" placeholder="default（32px）" />
<Input size="large"   placeholder="large（36px）" />
```

### TextArea 自适应高度
```jsx
<Input.TextArea
  autoSize={{ minRows: 3, maxRows: 8 }}
  placeholder="请输入描述（最少3行，最多8行自动扩展）"
  showWordLimit
  maxLength={500}
/>
```

### Password 密码框
```jsx
<Input.Password placeholder="请输入密码" visibilityToggle />
```

### Search 搜索框
```jsx
// 仅搜索图标（无按钮）
<Input.Search placeholder="搜索..." onSearch={(v) => handleSearch(v)} />

// 带默认搜索按钮
<Input.Search searchButton placeholder="搜索..." onSearch={(v) => handleSearch(v)} />

// 自定义搜索按钮
<Input.Search
  searchButton={<Button type="primary">搜索</Button>}
  placeholder="搜索..."
  onSearch={(v) => handleSearch(v)}
/>

// 搜索中 loading 状态
<Input.Search searchButton loading={searching} onSearch={handleSearch} />
```

### 在 Form 中使用
```jsx
// Form.Item 通过 field 绑定（不是 Ant Design 的 name）
// Form 自动注入 value/onChange/status，无需手动传
<Form.Item field="username" label="用户名" rules={[{ required: true, message: '请输入用户名' }]}>
  <Input placeholder="请输入用户名" />
</Form.Item>

<Form.Item field="password" label="密码">
  <Input.Password placeholder="请输入密码" />
</Form.Item>

<Form.Item field="bio" label="简介">
  <Input.TextArea autoSize={{ minRows: 2, maxRows: 6 }} maxLength={200} showWordLimit />
</Form.Item>
```

---

## CSS 类名速查

| 状态/场景 | 类名 |
|---|---|
| 输入框容器 | `.lingyang-input-wrapper` |
| 聚焦 | `.lingyang-input-wrapper.lingyang-input-focus` |
| 禁用 | `.lingyang-input-wrapper.lingyang-input-disabled` |
| error 状态 | `.lingyang-input-wrapper.lingyang-input-status-error` |
| warning 状态 | `.lingyang-input-wrapper.lingyang-input-status-warning` |
| mini 尺寸 | `.lingyang-input-wrapper.lingyang-input-size-mini` |
| prefix 区域 | `.lingyang-input-prefix` |
| suffix 区域 | `.lingyang-input-suffix` |
| 清除按钮 | `.lingyang-input-clear-btn` |
| addBefore | `.lingyang-input-addbefore` |
| addAfter | `.lingyang-input-addafter` |
| 字数统计 | `.lingyang-input-word-limit` |
| TextArea | `.lingyang-textarea` |
| Search 按钮 | `.lingyang-input-search-btn` |
| Password 眼睛 | `.lingyang-input-password-icon` |
-e 

---

## 完整代码示例

# lingyang-input · 完整代码示例库

## 目录
1. [基础用法（Input）](#1-基础用法)
2. [前缀/后缀 & 前置/后置](#2-前缀后缀--前置后置)
3. [normalize 格式化输入（lingyang 专有）](#3-normalize-格式化输入)
4. [字数限制与统计](#4-字数限制与统计)
5. [Input.TextArea 多行输入](#5-inputtextarea-多行输入)
6. [Input.Password 密码框](#6-inputpassword-密码框)
7. [Input.Search 搜索框](#7-inputsearch-搜索框)
8. [Input.Group 组合输入](#8-inputgroup-组合输入)
9. [在 Form 中使用（完整表单示例）](#9-在-form-中使用)

---

## 1. 基础用法

```jsx
import { Input } from 'lingyang';
import { useState } from 'react';

// 非受控（简单场景）
<Input placeholder="请输入用户名" allowClear />

// 受控（推荐，配合状态管理）
function ControlledDemo() {
  const [value, setValue] = useState('');

  return (
    <Input
      value={value}
      // ⚠️ lingyang onChange 第一个参数直接是字符串，无需 e.target.value
      onChange={(v) => setValue(v)}
      placeholder="请输入内容"
      allowClear
    />
  );
}

// 四种尺寸（mini 为 lingyang 专有，Ant Design 无）
<Input size="mini"    placeholder="mini（24px）" style={{ marginBottom: 8 }} />
<Input size="small"   placeholder="small（28px）" style={{ marginBottom: 8 }} />
<Input size="default" placeholder="default（32px）" style={{ marginBottom: 8 }} />
<Input size="large"   placeholder="large（36px）" />

// 禁用 / 只读
<Input disabled value="禁用状态" />
<Input readOnly value="只读状态，可复制" />

// 校验状态（通常由 Form 自动注入，也可手动控制）
<Input status="error"   placeholder="错误状态（红色边框）" />
<Input status="warning" placeholder="警告状态（橙色边框）" />
```

---

## 2. 前缀/后缀 & 前置/后置

```jsx
import { Input, Select } from 'lingyang';
import { IconUser, IconSearch, IconInfoCircle, IconPhone } from 'lingyang/icon';

// prefix/suffix：在边框【内部】，适合放图标
<Input prefix={<IconUser />}   placeholder="用户名" />
<Input suffix={<IconInfoCircle style={{ color: '#86909c' }} />} placeholder="带提示图标" />
<Input prefix={<IconUser />} suffix={<IconInfoCircle />} placeholder="前后都有图标" />

// addBefore/addAfter：在边框【外部】，灰色背景区域
// ⚠️ 命名差异：lingyang 用 addBefore/addAfter；Ant Design 用 addonBefore/addonAfter
<Input addBefore="https://" addAfter=".com" placeholder="输入域名" />

// addBefore 为下拉选择（经典电话号码输入）
<Input
  addBefore={
    <Select defaultValue="+86" style={{ width: 80 }} bordered={false}>
      <Select.Option value="+86">+86</Select.Option>
      <Select.Option value="+1">+1</Select.Option>
      <Select.Option value="+81">+81</Select.Option>
    </Select>
  }
  placeholder="输入手机号"
  style={{ width: 280 }}
/>

// addAfter 为按钮
<Input
  placeholder="输入验证码"
  addAfter={
    <Button type="text" size="small">获取验证码</Button>
  }
  style={{ width: 300 }}
/>

// prefix + addBefore 同时使用
<Input
  addBefore={<Select defaultValue="http" style={{ width: 80 }}><Select.Option value="http">http://</Select.Option><Select.Option value="https">https://</Select.Option></Select>}
  prefix={<IconSearch />}
  placeholder="输入地址"
/>
```

---

## 3. normalize 格式化输入

```jsx
// 【lingyang 专有】Ant Design 无 normalize，需在 onChange 里手动处理

// 自动转大写（适合证件号、编码输入）
<Input
  normalize={(v) => v.toUpperCase()}
  placeholder="自动转大写（如：ABCDEF）"
/>

// 只允许数字（适合 ID / 金额）
<Input
  normalize={(v) => v.replace(/[^0-9]/g, '')}
  placeholder="只能输入数字"
/>

// 只允许数字和小数点（适合金额输入）
<Input
  normalize={(v) => {
    // 移除非数字和小数点
    let val = v.replace(/[^0-9.]/g, '');
    // 只保留第一个小数点
    const dotIndex = val.indexOf('.');
    if (dotIndex !== -1) {
      val = val.slice(0, dotIndex + 1) + val.slice(dotIndex + 1).replace(/\./g, '');
    }
    // 最多两位小数
    const parts = val.split('.');
    if (parts[1]?.length > 2) val = `${parts[0]}.${parts[1].slice(0, 2)}`;
    return val;
  }}
  placeholder="金额输入（如：99.99）"
  prefix="¥"
/>

// 去除首尾空格（适合用户名、邮箱等）
// 注意：onChange 触发时已格式化，与 onBlur 的 trim 效果不同（实时格式化）
<Input
  normalize={(v) => v.trimStart()}  // 禁止起始空格（允许中间空格）
  placeholder="禁止起始空格"
/>

// 限制最大长度并格式化（搭配 normalize）
<Input
  normalize={(v) => v.replace(/[^a-zA-Z0-9_]/g, '').slice(0, 20)}
  placeholder="用户名（字母/数字/下划线，最多20位）"
  showWordLimit
  maxLength={20}
/>
```

---

## 4. 字数限制与统计

```jsx
// 基础字数限制（超出自动截断）
<Input maxLength={50} showWordLimit placeholder="最多50字" />

// errorOnly：超出时标红边框，但不截断输入内容
<Input
  maxLength={{ length: 100, errorOnly: true }}
  showWordLimit
  placeholder="超出100字时标红（不截断）"
/>

// TextArea 字数限制（最常用）
<Input.TextArea
  maxLength={200}
  showWordLimit
  autoSize={{ minRows: 3, maxRows: 6 }}
  placeholder="请输入备注（最多200字）"
/>
```

---

## 5. Input.TextArea 多行输入

```jsx
import { Input } from 'lingyang';

// 固定行数
<Input.TextArea rows={4} placeholder="请输入内容（固定4行）" />

// 高度完全自适应
<Input.TextArea autoSize placeholder="高度跟随内容自动增长" />

// 限制最小/最大行数（推荐方式）
<Input.TextArea
  autoSize={{ minRows: 3, maxRows: 8 }}
  placeholder="请输入描述（最少3行，最多8行）"
/>

// 带字数统计的多行输入（表单常用）
<Input.TextArea
  autoSize={{ minRows: 3, maxRows: 6 }}
  maxLength={500}
  showWordLimit
  placeholder="请输入详细描述（最多500字）"
/>

// 受控 TextArea
function ControlledTextArea() {
  const [value, setValue] = useState('');
  return (
    <Input.TextArea
      value={value}
      onChange={(v) => setValue(v)}
      autoSize={{ minRows: 2, maxRows: 10 }}
      placeholder="请输入..."
      allowClear
    />
  );
}
```

---

## 6. Input.Password 密码框

```jsx
import { Input } from 'lingyang';
import { useState } from 'react';

// 基础密码框（默认显示眼睛图标）
<Input.Password placeholder="请输入密码" />

// 隐藏眼睛图标（不允许查看明文）
<Input.Password placeholder="请输入密码" visibilityToggle={false} />

// 受控明文/密文切换（配合外部按钮）
function ControlledPassword() {
  const [visible, setVisible] = useState(false);

  return (
    <Space>
      <Input.Password
        visibility={visible}
        onVisibilityChange={setVisible}
        placeholder="请输入密码"
      />
      <Button
        type="text"
        onClick={() => setVisible(!visible)}
      >
        {visible ? '隐藏' : '显示'}
      </Button>
    </Space>
  );
}

// 密码强度示例（结合 normalize + status）
function PasswordStrength() {
  const [pwd, setPwd] = useState('');
  const getStatus = (v: string) => {
    if (!v) return undefined;
    if (v.length < 6) return 'error' as const;
    if (v.length < 10) return 'warning' as const;
    return undefined;
  };
  return (
    <Input.Password
      value={pwd}
      onChange={(v) => setPwd(v)}
      status={getStatus(pwd)}
      placeholder="请输入密码（至少10位）"
    />
  );
}
```

---

## 7. Input.Search 搜索框

```jsx
import { Input, Button } from 'lingyang';
import { useState } from 'react';

// 仅搜索图标（点击或 Enter 触发 onSearch）
<Input.Search
  placeholder="搜索..."
  onSearch={(value) => console.log('搜索:', value)}
  allowClear
/>

// 带默认搜索按钮（蓝色）
// ⚠️ 命名差异：lingyang 用 searchButton；Ant Design 用 enterButton
<Input.Search
  searchButton
  placeholder="输入关键词搜索"
  onSearch={(value) => handleSearch(value)}
/>

// 自定义搜索按钮（ReactNode）
<Input.Search
  searchButton={<Button type="primary" icon={<IconSearch />}>搜索</Button>}
  placeholder="输入关键词"
  onSearch={(value) => handleSearch(value)}
/>

// loading 状态
function SearchWithLoading() {
  const [loading, setLoading] = useState(false);

  const handleSearch = async (value: string) => {
    setLoading(true);
    try {
      await searchApi(value);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Input.Search
      searchButton
      loading={loading}
      placeholder="搜索用户..."
      onSearch={handleSearch}
      style={{ width: 300 }}
    />
  );
}

// 受控搜索框（带清除后重置列表）
function ControlledSearch() {
  const [keyword, setKeyword] = useState('');

  return (
    <Input.Search
      value={keyword}
      onChange={(v) => {
        setKeyword(v);
        if (!v) resetList(); // 清空时重置列表
      }}
      searchButton
      onSearch={handleSearch}
      placeholder="搜索..."
      allowClear
      onClear={() => resetList()}
    />
  );
}
```

---

## 8. Input.Group 组合输入

```jsx
import { Input, Select, Button, Cascader } from 'lingyang';

// 紧凑模式：Input + Select 横向组合（经典场景）
<Input.Group compact>
  <Select defaultValue="手机号" style={{ width: 90 }}>
    <Select.Option value="手机号">手机号</Select.Option>
    <Select.Option value="邮箱">邮箱</Select.Option>
  </Select>
  <Input placeholder="请输入" style={{ width: 220 }} />
</Input.Group>

// Input + Button 组合
<Input.Group compact>
  <Input placeholder="请输入邀请码" style={{ width: 200 }} />
  <Button type="primary">验证</Button>
</Input.Group>

// 地址三级联动（Cascader + Input）
<Input.Group compact>
  <Cascader
    placeholder="省/市/区"
    style={{ width: 200 }}
    options={regionOptions}
  />
  <Input placeholder="详细地址" style={{ width: 300 }} />
</Input.Group>

// 金额区间（双 Input）
<Input.Group compact>
  <Input placeholder="最低金额" style={{ width: 130 }} prefix="¥" />
  <div style={{
    width: 30,
    lineHeight: '32px',
    textAlign: 'center',
    background: '#f2f3f5',
    border: '1px solid var(--color-border)',
    borderLeft: 0,
    borderRight: 0,
  }}>~</div>
  <Input placeholder="最高金额" style={{ width: 130 }} prefix="¥" />
</Input.Group>
```

---

## 9. 在 Form 中使用

```jsx
import { Form, Input, Button, Grid } from 'lingyang';

const { Row, Col } = Grid;

// ⚠️ lingyang Form.Item 用 field 绑定字段（Ant Design 用 name）
// Form 会自动向 Input 注入 value、onChange、status，无需手动传

function UserForm() {
  const [form] = Form.useForm();

  const handleSubmit = async () => {
    try {
      const values = await form.validate();
      console.log('表单值:', values);
      await submitApi(values);
    } catch (e) {
      console.log('校验失败:', e);
    }
  };

  return (
    <Form form={form} layout="vertical" autoComplete="off">
      <Row gutter={16}>
        <Col span={12}>
          {/* field 对应字段名，不是 name */}
          <Form.Item
            field="username"
            label="用户名"
            rules={[
              { required: true, message: '请输入用户名' },
              { minLength: 3, message: '至少3个字符' },
              { maxLength: 20, message: '最多20个字符' },
            ]}
          >
            <Input placeholder="请输入用户名" allowClear />
          </Form.Item>
        </Col>

        <Col span={12}>
          <Form.Item
            field="email"
            label="邮箱"
            rules={[
              { required: true, message: '请输入邮箱' },
              { type: 'email', message: '请输入有效的邮箱格式' },
            ]}
          >
            <Input
              placeholder="请输入邮箱"
              prefix={<IconEmail />}
              allowClear
            />
          </Form.Item>
        </Col>

        <Col span={12}>
          <Form.Item
            field="phone"
            label="手机号"
            rules={[
              { required: true, message: '请输入手机号' },
              { match: /^1[3-9]\d{9}$/, message: '请输入正确的手机号格式' },
            ]}
          >
            <Input
              placeholder="请输入手机号"
              normalize={(v) => v.replace(/[^0-9]/g, '').slice(0, 11)}
              maxLength={11}
            />
          </Form.Item>
        </Col>

        <Col span={12}>
          <Form.Item
            field="password"
            label="密码"
            rules={[
              { required: true, message: '请输入密码' },
              { minLength: 8, message: '密码至少8位' },
            ]}
          >
            <Input.Password placeholder="请输入密码（至少8位）" />
          </Form.Item>
        </Col>

        <Col span={24}>
          <Form.Item
            field="bio"
            label="个人简介"
            rules={[{ maxLength: 200, message: '简介不超过200字' }]}
          >
            <Input.TextArea
              autoSize={{ minRows: 3, maxRows: 6 }}
              maxLength={200}
              showWordLimit
              placeholder="请输入个人简介（选填）"
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

# lingyang-input · 完整 Props 类型定义

## 目录
- [InputProps（基础单行）](#inputprops)
- [TextAreaProps（多行）](#textareaprops)
- [PasswordProps（密码）](#passwordprops)
- [SearchProps（搜索）](#searchprops)
- [InputGroupProps（组合容器）](#inputgroupprops)
- [与 Ant Design 差异详细对照](#与-ant-design-差异详细对照)

---

## InputProps

```typescript
interface InputProps
  extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'onChange' | 'prefix' | 'size'> {

  /** 受控值 */
  value?: string;

  /** 非受控默认值 */
  defaultValue?: string;

  /** 占位提示文字 */
  placeholder?: string;

  /** 是否禁用 @default false */
  disabled?: boolean;

  /** 是否只读 @default false */
  readOnly?: boolean;

  /**
   * 最大输入长度。
   * - number：超出后自动截断
   * - { length, errorOnly?: boolean }：errorOnly=true 时超出仅标红，不截断输入
   */
  maxLength?: number | { length: number; errorOnly?: boolean };

  /**
   * 显示字数统计。需配合 maxLength 使用。
   * @default false
   */
  showWordLimit?: boolean;

  /**
   * 是否显示清除按钮。
   * - boolean：true = 显示默认清除图标
   * - { clearIcon: ReactNode }：自定义清除图标
   * @default false
   */
  allowClear?: boolean | { clearIcon?: ReactNode };

  /**
   * 输入框尺寸。
   * mini（24px）→ small（28px）→ default（32px）→ large（36px）
   * 【lingyang 专有】mini 档为 lingyang 新增，Ant Design 无此档位。
   * @default 'default'
   */
  size?: 'mini' | 'small' | 'default' | 'large';

  /**
   * 校验状态。通常由 Form.Item 根据校验规则自动注入，无需手动设置。
   * 'error' = 红色边框；'warning' = 橙色边框
   */
  status?: 'error' | 'warning';

  /** 框内前置内容（在边框内部左侧，适合放图标）*/
  prefix?: ReactNode;

  /** 框内后置内容（在边框内部右侧，适合放图标）*/
  suffix?: ReactNode;

  /**
   * 框外前置内容（在边框左侧外部，灰色背景区域）。
   * 【命名差异】lingyang 用 addBefore；Ant Design 用 addonBefore。
   */
  addBefore?: ReactNode;

  /**
   * 框外后置内容（在边框右侧外部，灰色背景区域）。
   * 【命名差异】lingyang 用 addAfter；Ant Design 用 addonAfter。
   */
  addAfter?: ReactNode;

  /**
   * 【lingyang 专有】输入值格式化函数。
   * 在 onChange 触发前对输入值进行转换。Ant Design 无此功能。
   * 示例：自动转大写 `normalize={(v) => v.toUpperCase()}`
   * 示例：只允许数字 `normalize={(v) => v.replace(/[^0-9]/g, '')}`
   */
  normalize?: (value: string) => string;

  /** 自动聚焦 @default false */
  autoFocus?: boolean;

  /**
   * 宽度自适应内容。
   * - boolean：true = 自适应
   * - { minWidth?: number, maxWidth?: number }：限制最小/最大宽度
   * @default false
   */
  autoWidth?: boolean | { minWidth?: number; maxWidth?: number };

  /** 自定义内联样式 */
  style?: React.CSSProperties;

  /** 自定义类名 */
  className?: string;

  /** 原生 input 元素的 ref */
  inputRef?: React.Ref<HTMLInputElement>;

  /**
   * 值变化回调。
   * 【参数差异】lingyang 第一个参数为纯字符串 value，Ant Design 为原生 Event。
   * @param value 当前输入的字符串值
   * @param event 原生输入事件
   */
  onChange?: (value: string, event: React.ChangeEvent<HTMLInputElement>) => void;

  /** 按下 Enter 键的回调 */
  onPressEnter?: (event: React.KeyboardEvent<HTMLInputElement>) => void;

  /** 点击清除按钮的回调 */
  onClear?: () => void;

  /** 聚焦回调 */
  onFocus?: (event: React.FocusEvent<HTMLInputElement>) => void;

  /** 失焦回调 */
  onBlur?: (event: React.FocusEvent<HTMLInputElement>) => void;
}
```

---

## TextAreaProps

```typescript
/**
 * 继承 InputProps 大部分属性，以下是 TextArea 特有属性。
 * 注意：TextArea 不支持 prefix / suffix / addBefore / addAfter / size。
 */
interface TextAreaProps
  extends Omit<InputProps, 'prefix' | 'suffix' | 'addBefore' | 'addAfter' | 'size'> {

  /**
   * 高度自适应内容。
   * - boolean：true = 完全自适应，无滚动条
   * - { minRows?: number, maxRows?: number }：限制最小/最大行数
   * 与 rows 互斥，autoSize 优先级更高。
   * @default false
   */
  autoSize?: boolean | { minRows?: number; maxRows?: number };

  /**
   * 固定显示行数（textarea 原生 rows 属性）。
   * autoSize 设置时本属性无效。
   * @default 4
   */
  rows?: number;

  /**
   * 包裹层 div 的自定义样式。
   * showWordLimit 为 true 时，外层会有一个包裹 div，可通过此属性控制其样式。
   */
  wrapperStyle?: React.CSSProperties;

  /** 原生 textarea 元素的 ref */
  textAreaRef?: React.Ref<HTMLTextAreaElement>;

  /** 值变化回调（第一参数仍为字符串 value）*/
  onChange?: (value: string, event: React.ChangeEvent<HTMLTextAreaElement>) => void;

  /** 按下 Enter 键的回调 */
  onPressEnter?: (event: React.KeyboardEvent<HTMLTextAreaElement>) => void;
}
```

---

## PasswordProps

```typescript
/** 继承 InputProps 全部属性，以下是 Password 特有属性 */
interface PasswordProps extends InputProps {

  /**
   * 是否显示切换明文/密文的眼睛图标。
   * @default true
   */
  visibilityToggle?: boolean;

  /**
   * 初始是否显示明文（非受控）。
   * @default false
   */
  defaultVisibility?: boolean;

  /**
   * 受控的明文/密文可见状态。
   * 与 onVisibilityChange 配合使用实现完全受控。
   */
  visibility?: boolean;

  /** 切换可见状态时的回调 */
  onVisibilityChange?: (visible: boolean) => void;
}
```

---

## SearchProps

```typescript
/** 继承 InputProps 全部属性，以下是 Search 特有属性 */
interface SearchProps extends InputProps {

  /**
   * 搜索按钮配置。
   * - false：只显示搜索图标（默认）
   * - true：显示默认样式的搜索按钮（蓝色）
   * - ReactNode：完全自定义按钮内容
   *
   * 【命名差异】lingyang 用 searchButton；Ant Design 用 enterButton。
   * @default false
   */
  searchButton?: boolean | ReactNode;

  /**
   * 是否显示搜索中的 loading 状态。
   * @default false
   */
  loading?: boolean;

  /**
   * 搜索触发回调。
   * 在以下情况触发：点击搜索按钮 / 按下 Enter 键。
   */
  onSearch?: (value: string) => void;
}
```

---

## InputGroupProps

```typescript
/** Input.Group 输入框组合容器 */
interface InputGroupProps {

  /**
   * 紧凑模式。
   * true = 子组件之间无间距，相邻边框合并（视觉上连成一体）。
   * 通常用于 Input + Select / Input + Button 的横向组合。
   * @default false
   */
  compact?: boolean;

  style?: React.CSSProperties;
  className?: string;
  children?: React.ReactNode;
}
```

---

## 尺寸规格（size）

| 值 | 高度 | 字号 | 说明 |
|---|---|---|---|
| `mini` | 24px | 12px | **lingyang 专有**，Ant Design 无此档位 |
| `small` | 28px | 14px | 小尺寸 |
| `default` | 32px | 14px | 默认（推荐） |
| `large` | 36px | 14px | 大尺寸 |

---

## 与 Ant Design 差异详细对照

| 特性 | lingyang 写法 | Ant Design 写法 |
|---|---|---|
| 尺寸档位 | `size="mini"` ✅ | ❌ 无 mini，最小为 `small` |
| onChange 第一参数 | `(value: string, event)` → 直接是字符串 | `(event)` → 需 `e.target.value` |
| 输入格式化 | `normalize={(v) => v.toUpperCase()}` | ❌ 无，需在 onChange 中手动处理 |
| 前置外部内容 | `addBefore="https://"` | `addonBefore="https://"` |
| 后置外部内容 | `addAfter=".com"` | `addonAfter=".com"` |
| 搜索按钮 prop | `searchButton={true}` | `enterButton={true}` |
| 密码切换 | `visibilityToggle` | `visibilityToggle`（同名）|
| 多行自适应 | `autoSize={{ minRows: 2, maxRows: 6 }}` | 同（写法一致）|
| Form 字段绑定 | `<Form.Item field="name">` | `<Form.Item name="name">` |

---
