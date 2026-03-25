# lingyang Form 表单

**类型**: JSX 组件（推荐配合 `useForm` Hook 使用）

---

## 子组件总览

| 组件 / Hook | 说明 |
|-------------|------|
| `<Form>` | 表单根容器，管理布局、校验时机、初始值等全局配置 |
| `<Form.Item>` | 单个表单项，绑定字段、展示标签和校验信息 |
| `<Form.List>` | 动态表单列表，管理可增删的字段数组 |
| `<Form.Provider>` | 多表单通信的上下文 Provider |
| `useForm()` | 创建表单实例，用于命令式操作 |
| `useFormContext()` | 在子组件内获取当前 Form 实例 |
| `useWatch(field, form?)` | 监听字段值变化 Hook |

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本表单 | `<Form onSubmit={handleSubmit}><Form.Item field="name" label="姓名"><Input /></Form.Item></Form>` |
| 使用实例 | `const [form] = Form.useForm();` → `<Form form={form}>` |
| 必填校验 | `<Form.Item field="name" rules={[{ required: true, message: '请输入' }]}>` |
| 自定义校验 | `rules={[{ validator: (val, cb) => val > 0 ? cb() : cb('须大于0') }]}` |
| 获取全部值 | `form.getFields()` （**注意：不是 getFieldsValue**） |
| 触发校验 | `form.validate()` （**注意：不是 validateFields**） |
| 重置表单 | `form.resetFields()` |
| 监听字段 | `const val = useWatch('username', form)` |
| 垂直布局 | `<Form layout="vertical">` |
| 设置列宽 | `<Form labelCol={{ span: 6 }} wrapperCol={{ span: 18 }}>` |
| 动态列表 | `<Form.List field="items">{(fields, { add, remove }) => ...}</Form.List>` |
| 联动校验 | `<Form.Item field="confirm" dependencies={['password']} rules={[...]}>` |

---

## 与 Ant Design 的 8 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **Form.Item 字段名属性不同**
   - lingyang: `<Form.Item field="username">`
   - Ant Design: `<Form.Item name="username">`

2. **获取全部字段值方法名不同**
   - lingyang: `form.getFields()`
   - Ant Design: `form.getFieldsValue()`

3. **触发校验方法名不同**
   - lingyang: `form.validate()` → 返回 `Promise<values>`
   - Ant Design: `form.validateFields()` → 返回 `Promise<values>`

4. **值属性名配置不同**
   - lingyang: `<Form.Item triggerPropName="checked">` （如 Checkbox）
   - Ant Design: `<Form.Item valuePropName="checked">`

5. **Form.List 字段名属性不同**
   - lingyang: `<Form.List field="items">`
   - Ant Design: `<Form.List name="items">`

6. **useWatch 挂载位置不同**
   - lingyang: `import { useWatch } from 'lingyang'; useWatch('field', form)`（独立 Hook）
   - Ant Design: `Form.useWatch('field', form)`（挂载在 Form 上）

7. **清除错误状态（lingyang 专有）**
   - lingyang: `form.clearFields()` 清除错误但不重置值
   - Ant Design: 无直接对应方法

8. **hasFeedback 属性**
   - lingyang: 无 `hasFeedback`，校验图标由内部控制
   - Ant Design: `<Form.Item hasFeedback>` 控制是否展示校验图标

---

## Form Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| form | FormInstance | — | useForm() 创建的表单实例 |
| initialValues | object | — | 表单初始值（首次渲染生效） |
| layout | `'horizontal'\|'vertical'\|'inline'` | `'horizontal'` | 布局方式 |
| labelAlign | `'left'\|'right'` | `'right'` | 标签对齐方式 |
| labelCol | `{ span?, offset? }` | — | 标签列栅格（全局） |
| wrapperCol | `{ span?, offset? }` | — | 控件列栅格（全局） |
| colon | boolean | `true` | 标签后是否显示冒号 |
| disabled | boolean | `false` | 禁用所有控件 |
| size | `'mini'\|'small'\|'default'\|'large'` | — | 控件统一尺寸 |
| requiredSymbol | `boolean \| { position: 'start'\|'end' }` | `true` | 必填星号显示与位置 |
| scrollToFirstError | boolean | `false` | 校验失败时滚动到首个错误 |
| validateTrigger | `string \| string[]` | `'onChange'` | 全局校验触发时机 |
| onChange | `(value, values) => void` | — | 任意字段变化回调 |
| onSubmit | `(values) => void` | — | 提交且校验通过回调 |
| onSubmitFailed | `(errors) => void` | — | 提交但校验失败回调 |

---

## Form.Item Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| field | `string \| string[]` | — | 字段名（**不是 name**） |
| label | ReactNode | — | 标签内容 |
| rules | `RuleObject[]` | — | 校验规则数组 |
| required | boolean | — | 是否必填（自动添加规则+星号） |
| validateTrigger | `string \| string[]` | — | 触发校验事件（覆盖全局） |
| trigger | string | `'onChange'` | 收集值的事件名 |
| triggerPropName | string | `'value'` | 值属性名（**不是 valuePropName**） |
| validateStatus | `'success'\|'warning'\|'error'\|'validating'` | — | 手动设置校验状态 |
| help | ReactNode | — | 手动设置帮助/错误信息 |
| extra | ReactNode | — | 额外提示（校验信息下方） |
| labelCol | `{ span?, offset? }` | — | 覆盖全局 labelCol |
| wrapperCol | `{ span?, offset? }` | — | 覆盖全局 wrapperCol |
| hidden | boolean | `false` | 隐藏但保留字段数据 |
| noStyle | boolean | `false` | 去除样式（用于嵌套场景） |
| disabled | boolean | — | 覆盖全局 disabled |
| shouldUpdate | `boolean \| function` | — | 自定义更新条件 |
| dependencies | `string[]` | — | 依赖字段（变化时重新校验） |

---

## 表单实例方法速查（useForm）

| 方法 | 说明 | Ant Design 对应 |
|------|------|----------------|
| `form.getFieldValue(field)` | 获取指定字段值 | 同名 |
| `form.getFields()` | 获取全部字段值对象 | `getFieldsValue()` |
| `form.getFieldsValue(fields?)` | 获取指定字段值对象 | `getFieldsValue(fields)` |
| `form.getFieldError(field)` | 获取字段错误信息 | 同名 |
| `form.setFieldValue(field, value)` | 设置指定字段值 | 同名（v5+） |
| `form.setFields(fields)` | 批量设置字段值/状态 | 同名 |
| `form.resetFields(fields?)` | 重置到初始值 | 同名 |
| `form.validate(fields?)` | 触发校验，返回 Promise | `validateFields()` |
| `form.clearFields(fields?)` | 清除错误状态（不重置值） | ❌ 无 |
| `form.scrollToField(field)` | 滚动到指定字段 | 同名 |
| `form.submit()` | 触发表单提交 | 同名 |

---

## RuleObject 校验规则

| 属性 | 类型 | 说明 |
|------|------|------|
| required | boolean | 必填 |
| type | string | 类型（string/number/email/url/ip/array/object） |
| message | string | 校验失败提示 |
| min | number | 最小长度/值/数组个数 |
| max | number | 最大长度/值/数组个数 |
| length | number | 固定长度 |
| pattern | RegExp | 正则匹配 |
| validator | function | 自定义校验函数 |
| whitespace | boolean | 空白视为空值 |
| enum | any[] | 枚举值列表 |

---

## 常用 CSS 类名

`.lingyang-form` / `.lingyang-form-layout-{horizontal|vertical|inline}` / `.lingyang-form-item` / `.lingyang-form-label-item` / `.lingyang-form-item-wrapper` / `.lingyang-form-item-status-{error|success|warning|validating}` / `.lingyang-form-message` / `.lingyang-form-item-symbol` / `.lingyang-form-item-hidden`

---

## 参考文件

- 完整代码示例（8 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Form — 完整代码示例

## 1. 基本登录表单（含校验）

```jsx
import { Form, Input, Button, Checkbox } from 'lingyang';

function LoginForm() {
  // 注意：lingyang 用 Form.useForm()，与 Ant Design 相同
  const [form] = Form.useForm();

  const handleSubmit = (values) => {
    console.log('提交成功', values);
  };

  const handleSubmitFailed = (errors) => {
    console.log('校验失败', errors);
  };

  return (
    <Form
      form={form}
      layout="vertical"
      onSubmit={handleSubmit}
      onSubmitFailed={handleSubmitFailed}
      style={{ width: 360 }}
    >
      {/* 注意：lingyang 用 field，Ant Design 用 name */}
      <Form.Item
        field="username"
        label="用户名"
        rules={[
          { required: true, message: '请输入用户名' },
          { min: 3, max: 20, message: '用户名长度为 3-20 位' },
        ]}
      >
        <Input placeholder="请输入用户名" />
      </Form.Item>

      <Form.Item
        field="password"
        label="密码"
        rules={[
          { required: true, message: '请输入密码' },
          { min: 6, message: '密码至少 6 位' },
        ]}
      >
        <Input.Password placeholder="请输入密码" />
      </Form.Item>

      {/*
        Checkbox 需要设置 triggerPropName="checked"
        注意：lingyang 用 triggerPropName，Ant Design 用 valuePropName
      */}
      <Form.Item field="remember" triggerPropName="checked">
        <Checkbox>记住我</Checkbox>
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" long>
          登录
        </Button>
      </Form.Item>
    </Form>
  );
}
```

## 2. 水平布局 + labelCol/wrapperCol

```jsx
import { Form, Input, Select, Button } from 'lingyang';

function HorizontalForm() {
  const [form] = Form.useForm();

  return (
    <Form
      form={form}
      layout="horizontal"
      labelCol={{ span: 6 }}
      wrapperCol={{ span: 18 }}
      style={{ maxWidth: 600 }}
    >
      <Form.Item field="name" label="姓名" rules={[{ required: true }]}>
        <Input placeholder="请输入" />
      </Form.Item>

      <Form.Item field="department" label="部门">
        <Select placeholder="请选择" options={['技术部', '产品部', '设计部']} />
      </Form.Item>

      {/* wrapperCol offset 跳过标签列，与控件对齐 */}
      <Form.Item wrapperCol={{ offset: 6, span: 18 }}>
        <Button type="primary" htmlType="submit">提交</Button>
      </Form.Item>
    </Form>
  );
}
```

## 3. 表单实例方法（命令式操作）

```jsx
import { Form, Input, Button, Space } from 'lingyang';

function ImperativeForm() {
  const [form] = Form.useForm();

  const handleGetValues = () => {
    // 注意：lingyang 用 getFields()，Ant Design 用 getFieldsValue()
    const values = form.getFields();
    console.log('全部字段值：', values);
  };

  const handleValidate = async () => {
    try {
      // 注意：lingyang 用 validate()，Ant Design 用 validateFields()
      const values = await form.validate();
      console.log('校验通过：', values);
    } catch (errors) {
      console.log('校验失败：', errors);
    }
  };

  const handleReset = () => {
    form.resetFields();
  };

  const handleClearErrors = () => {
    // clearFields 为 lingyang 专有，仅清除错误状态，不重置值
    form.clearFields();
  };

  const handleSetValue = () => {
    form.setFieldValue('username', 'lingyang_user');
  };

  return (
    <Form form={form} layout="vertical" style={{ width: 360 }}>
      <Form.Item field="username" label="用户名" rules={[{ required: true }]}>
        <Input placeholder="请输入" />
      </Form.Item>
      <Form.Item field="email" label="邮箱" rules={[{ type: 'email', message: '格式不正确' }]}>
        <Input placeholder="请输入邮箱" />
      </Form.Item>

      <Space wrap>
        <Button onClick={handleGetValues}>获取全部值</Button>
        <Button onClick={handleValidate} type="primary">触发校验</Button>
        <Button onClick={handleReset}>重置</Button>
        <Button onClick={handleClearErrors}>清除错误</Button>
        <Button onClick={handleSetValue}>设置用户名</Button>
      </Space>
    </Form>
  );
}
```

## 4. 自定义校验 + 联动校验（dependencies）

```jsx
import { Form, Input, Button } from 'lingyang';

function PasswordForm() {
  const [form] = Form.useForm();

  return (
    <Form form={form} layout="vertical" style={{ width: 360 }}>
      <Form.Item
        field="password"
        label="密码"
        rules={[
          { required: true, message: '请输入密码' },
          { min: 8, message: '密码至少 8 位' },
          {
            // 自定义校验：必须包含数字
            validator: (value, callback) => {
              if (value && !/\d/.test(value)) {
                callback('密码必须包含数字');
              } else {
                callback();
              }
            },
          },
        ]}
      >
        <Input.Password placeholder="请输入密码" />
      </Form.Item>

      <Form.Item
        field="confirmPassword"
        label="确认密码"
        // dependencies：password 变化时重新校验 confirmPassword
        dependencies={['password']}
        rules={[
          { required: true, message: '请确认密码' },
          {
            validator: (value, callback) => {
              const password = form.getFieldValue('password');
              if (value && value !== password) {
                callback('两次密码不一致');
              } else {
                callback();
              }
            },
          },
        ]}
      >
        <Input.Password placeholder="请确认密码" />
      </Form.Item>

      <Button type="primary" htmlType="submit">提交</Button>
    </Form>
  );
}
```

## 5. useWatch 监听字段（联动显示）

```jsx
import { Form, Input, Select, useWatch } from 'lingyang';

function WatchForm() {
  const [form] = Form.useForm();
  // 注意：lingyang 为独立 Hook useWatch，Ant Design 用 Form.useWatch
  const type = useWatch('type', form);

  return (
    <Form form={form} layout="vertical" style={{ width: 360 }}>
      <Form.Item field="type" label="类型">
        <Select
          options={[
            { value: 'personal', label: '个人' },
            { value: 'company', label: '企业' },
          ]}
          placeholder="请选择"
        />
      </Form.Item>

      {/* 根据 type 字段值联动显示不同字段 */}
      {type === 'personal' && (
        <Form.Item field="idNumber" label="身份证号" rules={[{ required: true }]}>
          <Input placeholder="请输入身份证号" />
        </Form.Item>
      )}

      {type === 'company' && (
        <Form.Item field="taxNumber" label="税号" rules={[{ required: true }]}>
          <Input placeholder="请输入税号" />
        </Form.Item>
      )}
    </Form>
  );
}
```

## 6. 动态表单列表（Form.List）

```jsx
import { Form, Input, Button, Space } from 'lingyang';
import { IconPlus, IconDelete } from 'lingyang/icon';

function DynamicForm() {
  const [form] = Form.useForm();

  return (
    <Form form={form} layout="vertical" style={{ width: 500 }}>
      {/* 注意：lingyang 用 field，Ant Design 用 name */}
      <Form.List field="members">
        {(fields, { add, remove }) => (
          <>
            {fields.map((item, index) => (
              <Space key={item.key} align="start" style={{ display: 'flex', marginBottom: 8 }}>
                {/* 嵌套字段路径：lingyang 用 field 数组拼接 */}
                <Form.Item
                  field={`${item.field}.name`}
                  label={index === 0 ? '姓名' : ''}
                  rules={[{ required: true, message: '请输入姓名' }]}
                >
                  <Input placeholder="姓名" />
                </Form.Item>

                <Form.Item
                  field={`${item.field}.email`}
                  label={index === 0 ? '邮箱' : ''}
                  rules={[{ type: 'email', message: '格式不正确' }]}
                >
                  <Input placeholder="邮箱" />
                </Form.Item>

                <Button
                  icon={<IconDelete />}
                  status="danger"
                  onClick={() => remove(index)}
                  style={{ marginTop: index === 0 ? 28 : 0 }}
                />
              </Space>
            ))}

            <Button
              type="dashed"
              icon={<IconPlus />}
              onClick={() => add()}
              long
            >
              添加成员
            </Button>
          </>
        )}
      </Form.List>

      <Button type="primary" htmlType="submit" style={{ marginTop: 16 }}>
        提交
      </Button>
    </Form>
  );
}
```

## 7. shouldUpdate 精确控制更新

```jsx
import { Form, Input, Select } from 'lingyang';

function ShouldUpdateForm() {
  return (
    <Form layout="vertical" style={{ width: 360 }}>
      <Form.Item field="country" label="国家">
        <Select
          options={[
            { value: 'CN', label: '中国' },
            { value: 'US', label: '美国' },
          ]}
          placeholder="请选择国家"
        />
      </Form.Item>

      {/*
        shouldUpdate：仅当 country 字段变化时重新渲染此项
        比 dependencies 更灵活（可完全自定义渲染内容）
      */}
      <Form.Item
        shouldUpdate={(prev, next) => prev.country !== next.country}
        noStyle
      >
        {({ getFieldValue }) => {
          const country = getFieldValue('country');
          return country === 'CN' ? (
            <Form.Item field="province" label="省份" rules={[{ required: true }]}>
              <Input placeholder="请输入省份" />
            </Form.Item>
          ) : country === 'US' ? (
            <Form.Item field="state" label="州" rules={[{ required: true }]}>
              <Input placeholder="请输入州" />
            </Form.Item>
          ) : null;
        }}
      </Form.Item>
    </Form>
  );
}
```

## 8. 手动设置校验状态（validateStatus + help）

```jsx
import { useState } from 'react';
import { Form, Input, Button } from 'lingyang';

function ManualValidateForm() {
  const [status, setStatus] = useState(undefined);
  const [help, setHelp] = useState('');

  const checkUsername = async (value) => {
    if (!value) {
      setStatus('error');
      setHelp('请输入用户名');
      return;
    }
    setStatus('validating');
    setHelp('检查中...');
    // 模拟异步检查
    await new Promise(r => setTimeout(r, 1000));
    if (value === 'admin') {
      setStatus('error');
      setHelp('用户名已被占用');
    } else {
      setStatus('success');
      setHelp('用户名可用');
    }
  };

  return (
    <Form layout="vertical" style={{ width: 360 }}>
      <Form.Item
        field="username"
        label="用户名"
        validateStatus={status}
        help={help}
      >
        <Input
          placeholder="请输入用户名"
          onChange={checkUsername}
        />
      </Form.Item>

      <Button type="primary" htmlType="submit">注册</Button>
    </Form>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Form — 完整 TypeScript 接口定义

## FormProps

```typescript
interface FormProps<T = any> {
  /** 表单实例（由 useForm() 创建） */
  form?: FormInstance<T>;
  /** 表单初始值对象（首次渲染时生效，后续更新无效） */
  initialValues?: Partial<T>;
  /** 表单布局方式。默认 'horizontal' */
  layout?: 'horizontal' | 'vertical' | 'inline';
  /** 标签文字对齐方式。默认 'right' */
  labelAlign?: 'left' | 'right';
  /** 标签列栅格配置（24列），全局设置 */
  labelCol?: { span?: number; offset?: number };
  /** 控件列栅格配置（24列），全局设置 */
  wrapperCol?: { span?: number; offset?: number };
  /** 是否在标签后显示冒号。默认 true */
  colon?: boolean;
  /** 是否禁用所有控件。默认 false */
  disabled?: boolean;
  /** 控件统一尺寸 */
  size?: 'mini' | 'small' | 'default' | 'large';
  /** 是否显示必填星号，及其位置。默认 true */
  requiredSymbol?: boolean | { position: 'start' | 'end' };
  /** 提交校验失败时是否自动滚动到首个错误。默认 false */
  scrollToFirstError?: boolean;
  /** 全局校验触发时机。默认 'onChange' */
  validateTrigger?: string | string[];
  /** 任意字段值变化时的回调 */
  onChange?: (value: Partial<T>, values: T) => void;
  /** 提交且校验通过时的回调 */
  onSubmit?: (values: T) => void;
  /** 提交但校验失败时的回调 */
  onSubmitFailed?: (errors: Record<string, FieldError>) => void;
  /** 原生 autocomplete 属性。默认 'off' */
  autoComplete?: string;
  id?: string;
  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

## FormItemProps

```typescript
interface FormItemProps {
  /**
   * 字段名路径。
   * 【命名差异】lingyang 用 field，Ant Design 用 name
   * 支持字符串（如 'a.b'）或数组（如 ['a', 'b']）
   */
  field?: string | string[];
  /** 标签内容（支持 ReactNode） */
  label?: ReactNode;
  /** 校验规则数组 */
  rules?: RuleObject[];
  /** 是否必填（自动添加必填规则并显示星号） */
  required?: boolean;
  /** 触发校验的事件（覆盖 Form 全局 validateTrigger） */
  validateTrigger?: string | string[];
  /** 收集子组件值的事件名。默认 'onChange' */
  trigger?: string;
  /**
   * 子组件值的属性名。默认 'value'。
   * 【命名差异】lingyang 用 triggerPropName，Ant Design 用 valuePropName
   * 例：Checkbox 需设为 'checked'
   */
  triggerPropName?: string;
  /** 手动设置校验状态（配合 help 使用） */
  validateStatus?: 'success' | 'warning' | 'error' | 'validating';
  /** 手动设置帮助/错误信息（覆盖校验产生的信息） */
  help?: ReactNode;
  /** 额外的提示内容，显示在校验信息下方 */
  extra?: ReactNode;
  /** 当前项标签列栅格配置，覆盖 Form 全局 labelCol */
  labelCol?: { span?: number; offset?: number };
  /** 当前项控件列栅格配置，覆盖 Form 全局 wrapperCol */
  wrapperCol?: { span?: number; offset?: number };
  /** 当前项标签对齐，覆盖 Form 全局 labelAlign */
  labelAlign?: 'left' | 'right';
  /** 当前项是否显示冒号，覆盖 Form 全局 colon */
  colon?: boolean;
  /** 是否隐藏该项（字段仍参与表单数据）。默认 false */
  hidden?: boolean;
  /** 是否去除样式（无标签/边距/校验信息）。默认 false */
  noStyle?: boolean;
  /** 是否禁用当前项，覆盖 Form 全局 disabled */
  disabled?: boolean;
  /**
   * 自定义更新条件。
   * true = 任意字段变化都重新渲染；
   * 函数 = 精确控制是否重新渲染
   */
  shouldUpdate?: boolean | ((prevValues: object, nextValues: object) => boolean);
  /** 依赖字段列表，依赖变化时重新触发当前项校验 */
  dependencies?: string[];
  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

## FormListProps

```typescript
interface FormListProps {
  /**
   * 列表字段名。
   * 【命名差异】lingyang 用 field，Ant Design 用 name
   */
  field: string;
  /** 渲染函数 */
  children: (
    fields: FormListField[],
    operation: {
      add: (defaultValue?: any, insertIndex?: number) => void;
      remove: (index: number | number[]) => void;
      move: (fromIndex: number, toIndex: number) => void;
    }
  ) => ReactNode;
  /** 列表级别的校验规则 */
  rules?: RuleObject[];
  /** 列表初始值 */
  initialValue?: any[];
}

interface FormListField {
  key: number;    // 稳定唯一 key（用于 React key prop）
  field: string;  // 字段路径前缀（lingyang 用 field，Ant Design 用 name）
}
```

## FormInstance 完整类型

```typescript
interface FormInstance<T = any> {
  /** 获取指定字段值 */
  getFieldValue: (field: string | string[]) => any;
  /**
   * 获取全部字段值对象。
   * 【差异】Ant Design 用 getFieldsValue()
   */
  getFields: () => T;
  /** 获取指定字段值对象（可传字段名数组） */
  getFieldsValue: (fields?: string[]) => Partial<T>;
  /** 获取指定字段的错误信息 */
  getFieldError: (field: string | string[]) => string[];
  /** 获取多个字段的错误信息 */
  getFieldsError: (fields?: string[]) => Record<string, string[]>;
  /** 设置指定字段值 */
  setFieldValue: (field: string | string[], value: any) => void;
  /** 批量设置字段值和状态 */
  setFields: (fields: FieldState[]) => void;
  /** 重置字段到初始值（不传则重置全部） */
  resetFields: (fields?: string[]) => void;
  /**
   * 触发表单校验，返回 Promise<values>。
   * 【差异】Ant Design 用 validateFields()
   */
  validate: (fields?: string[]) => Promise<T>;
  /**
   * 清除字段错误状态（不重置值）。
   * 【lingyang 专有】Ant Design 无此方法
   */
  clearFields: (fields?: string[]) => void;
  /** 滚动到指定字段 */
  scrollToField: (field: string | string[], options?: ScrollIntoViewOptions) => void;
  /** 触发表单提交 */
  submit: () => void;
}
```

## RuleObject 完整类型

```typescript
interface RuleObject {
  required?: boolean;
  type?: 'string' | 'number' | 'boolean' | 'array' | 'object' | 'email' | 'url' | 'ip';
  message?: string | ReactNode;
  min?: number;
  max?: number;
  length?: number;
  pattern?: RegExp;
  validator?: (value: any, callback: (error?: string) => void) => void | Promise<void>;
  validateTrigger?: string | string[];
  whitespace?: boolean;
  enum?: any[];
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| Form.Item 字段名属性 | `field` | `name` |
| Form.List 字段名属性 | `field` | `name` |
| 值属性名配置 | `triggerPropName` | `valuePropName` |
| 获取全部字段值 | `form.getFields()` | `form.getFieldsValue()` |
| 触发校验 | `form.validate()` | `form.validateFields()` |
| 清除错误状态 | `form.clearFields()` | ❌ 无 |
| useWatch 挂载 | 独立 Hook `useWatch(field, form?)` | `Form.useWatch(name, form?)` |
| hasFeedback | ❌ 无此属性 | `<Form.Item hasFeedback>` |
| FormListField.field | `field` 属性 | `name` 属性 |

---
