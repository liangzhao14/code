# lingyang Radio 单选框

**类型**: JSX 组件（受控/非受控均支持）

---

## 子组件

| 组件 | 说明 |
|------|------|
| `<Radio>` | 单个单选框，可独立使用，也可作为 Radio.Group 的子项 |
| `<Radio.Group>` | 单选框组，管理一组互斥的单选状态，支持 button 样式 |

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 单个单选框 | `<Radio value="a">选项 A</Radio>` |
| 受控单体 | `<Radio checked={checked} onChange={(e) => setChecked(e.target.checked)}>` |
| 禁用 | `<Radio disabled>禁用</Radio>` |
| Group（options） | `<Radio.Group options={['A','B','C']} value={val} onChange={(v) => setVal(v)} />` |
| Group（children） | `<Radio.Group value={val} onChange={(v) => setVal(v)}><Radio value="a">A</Radio>...</Radio.Group>` |
| 按钮样式 | `<Radio.Group type="button" options={opts} defaultValue="a" />` |
| 按钮样式 + 尺寸 | `<Radio.Group type="button" size="small" options={opts} />` |
| 纵向排列 | `<Radio.Group direction="vertical" options={opts} />` |
| 自定义图标 | `<Radio icon={<IconHeart />} value="like">喜欢</Radio>` |
| 禁用整组 | `<Radio.Group disabled options={opts} />` |

---

## 与 Ant Design 的 5 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **Radio.Group onChange 参数不同**
   - lingyang: `onChange={(value, e) => setVal(value)}`，**第一参数直接为 value**
   - Ant Design: `onChange={(e) => setVal(e.target.value)}`，需通过 `e.target.value` 获取

2. **按钮样式的类型属性名不同**
   - lingyang: `<Radio.Group type="button">`
   - Ant Design: `<Radio.Group optionType="button">`

3. **按钮填充样式**
   - lingyang: 无 `buttonStyle` 属性，统一为品牌样式
   - Ant Design: `buttonStyle="outline"` 或 `buttonStyle="solid"` 控制描边/填充

4. **排列方向（lingyang 专有）**
   - lingyang: `<Radio.Group direction="vertical">` 直接支持纵向排列
   - Ant Design: 无 `direction`，需手动 `style={{ display: 'flex', flexDirection: 'column' }}`

5. **自定义图标（lingyang 专有）**
   - lingyang: `<Radio icon={<IconHeart />}>` 支持 icon 属性
   - Ant Design: 无 `icon` 属性，需通过 CSS 自定义样式

---

## Radio Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| checked | boolean | — | 受控：是否选中 |
| defaultChecked | boolean | `false` | 非受控：初始是否选中 |
| disabled | boolean | `false` | 是否禁用 |
| value | any | — | 单选框的值（在 Group 中用于标识） |
| onChange | `(e: Event) => void` | — | 状态变化回调（`e.target.checked` 获取选中态，`e.target.value` 获取值） |
| icon | ReactNode | — | 自定义单选图标（**lingyang 专有**，Ant Design 无） |
| children | ReactNode | — | 标签内容（右侧文字） |

---

## Radio.Group Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | any | — | 受控：当前选中的值 |
| defaultValue | any | — | 非受控：初始选中的值 |
| options | `(string \| number \| RadioOption)[]` | — | 选项数据源（与 children 二选一） |
| type | `'radio' \| 'button'` | `'radio'` | 样式类型（**注意：不是 optionType**） |
| direction | `'horizontal' \| 'vertical'` | `'horizontal'` | 排列方向（**lingyang 专有**） |
| size | `'mini' \| 'small' \| 'default' \| 'large'` | — | 按钮尺寸（`type='button'` 时生效） |
| disabled | boolean | `false` | 禁用整个单选框组 |
| onChange | `(value: any, e: Event) => void` | — | 选中值变化回调（**第一参数直接为 value**） |

### RadioOption 对象格式

```typescript
interface RadioOption {
  label: ReactNode;   // 展示标签（必填）
  value: any;         // 选项值（必填）
  disabled?: boolean; // 是否禁用该项
}
```

---

## 常用 CSS 类名

`.lingyang-radio` / `.lingyang-radio-checked` / `.lingyang-radio-disabled` / `.lingyang-radio-inner` / `.lingyang-radio-label` / `.lingyang-radio-group` / `.lingyang-radio-group-type-button` / `.lingyang-radio-group-direction-vertical` / `.lingyang-radio-button` / `.lingyang-radio-button-checked` / `.lingyang-radio-button-size-{mini|small|large}`

---

## 参考文件

- 完整代码示例（7 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Radio — 完整代码示例

## 1. 基本用法（非受控）

```jsx
import { Radio, Space } from 'lingyang';

function BasicRadio() {
  return (
    <Space direction="vertical">
      <Radio>基本单选框</Radio>
      <Radio defaultChecked>默认选中</Radio>
      <Radio disabled>禁用未选中</Radio>
      <Radio disabled defaultChecked>禁用已选中</Radio>
    </Space>
  );
}
```

---

## 2. 受控模式（单体）

```jsx
import { useState } from 'react';
import { Radio } from 'lingyang';

function ControlledRadio() {
  const [checked, setChecked] = useState(false);

  return (
    // Radio 单体 onChange 仍使用事件对象（与 Checkbox 不同）
    // e.target.checked 获取选中状态，e.target.value 获取 value
    <Radio
      checked={checked}
      onChange={(e) => setChecked(e.target.checked)}
    >
      {checked ? '已选中' : '未选中'}
    </Radio>
  );
}
```

---

## 3. Radio.Group — options 方式（最简洁）

```jsx
import { useState } from 'react';
import { Radio } from 'lingyang';

function GroupWithOptions() {
  const [value, setValue] = useState('react');

  const options = [
    { label: 'React', value: 'react' },
    { label: 'Vue', value: 'vue' },
    { label: 'Angular', value: 'angular', disabled: true },
    { label: 'Svelte', value: 'svelte' },
  ];

  return (
    <div>
      {/*
        注意：lingyang Radio.Group onChange 第一参数直接为 value
        Ant Design 需要 e.target.value 才能拿到值
      */}
      <Radio.Group
        value={value}
        onChange={(val) => setValue(val)}
        options={options}
      />
      <p style={{ marginTop: 8 }}>已选：{value}</p>
    </div>
  );
}
```

---

## 4. Radio.Group — children 方式

```jsx
import { useState } from 'react';
import { Radio, Space } from 'lingyang';

function GroupWithChildren() {
  const [value, setValue] = useState('1');

  return (
    <div>
      <Radio.Group value={value} onChange={(val) => setValue(val)}>
        <Radio value="1">选项一</Radio>
        <Radio value="2">选项二</Radio>
        <Radio value="3" disabled>选项三（禁用）</Radio>
        <Radio value="4">选项四</Radio>
      </Radio.Group>
      <p style={{ marginTop: 8 }}>已选：{value}</p>
    </div>
  );
}
```

---

## 5. 按钮样式（type="button"）+ 尺寸

```jsx
import { Radio, Space } from 'lingyang';

const options = ['日', '周', '月', '年'];

function ButtonRadio() {
  return (
    <Space direction="vertical">
      {/*
        注意：lingyang 用 type="button"
        Ant Design 用 optionType="button"（命名不同）
        lingyang 无 buttonStyle="solid/outline" 区分（Ant Design 有）
      */}
      <Radio.Group type="button" defaultValue="周" options={options} />

      {/* 按钮样式 + mini 尺寸（lingyang 专有，Ant Design 无 mini） */}
      <Radio.Group type="button" size="mini" defaultValue="周" options={options} />

      {/* 按钮样式 + small 尺寸 */}
      <Radio.Group type="button" size="small" defaultValue="周" options={options} />

      {/* 按钮样式 + large 尺寸 */}
      <Radio.Group type="button" size="large" defaultValue="周" options={options} />
    </Space>
  );
}
```

---

## 6. 纵向排列（direction="vertical" — lingyang 专有）

```jsx
import { useState } from 'react';
import { Radio } from 'lingyang';

const cities = [
  { label: '北京', value: 'beijing' },
  { label: '上海', value: 'shanghai' },
  { label: '广州', value: 'guangzhou' },
  { label: '深圳', value: 'shenzhen' },
];

function VerticalRadioGroup() {
  const [value, setValue] = useState('beijing');

  return (
    <div>
      {/*
        direction="vertical" 为 lingyang 专有属性
        Ant Design 无此属性，需手动：style={{ display:'flex', flexDirection:'column' }}
      */}
      <Radio.Group
        value={value}
        onChange={(val) => setValue(val)}
        direction="vertical"
        options={cities}
      />
      <p style={{ marginTop: 8 }}>已选城市：{value}</p>
    </div>
  );
}
```

---

## 7. 自定义图标（icon — lingyang 专有）

```jsx
import { Radio, Space } from 'lingyang';
import {
  IconHeart,
  IconHeartFill,
  IconStar,
  IconStarFill,
} from 'lingyang/icon';

function IconRadio() {
  return (
    <Radio.Group defaultValue="like">
      {/* icon 为 lingyang 专有属性，Ant Design 无，需通过 CSS 自定义 */}
      <Radio
        value="like"
        icon={<IconHeartFill style={{ color: '#F53F3F' }} />}
      >
        喜欢
      </Radio>
      <Radio
        value="star"
        icon={<IconStarFill style={{ color: '#FF7D00' }} />}
      >
        收藏
      </Radio>
    </Radio.Group>
  );
}
```

---

## 8. 在 Form 中使用（配合 triggerPropName）

```jsx
import { Form, Radio, Button } from 'lingyang';

function FormWithRadio() {
  const [form] = Form.useForm();

  const handleSubmit = (values) => {
    console.log('提交值：', values);
    // { gender: 'male', plan: 'pro' }
  };

  return (
    <Form form={form} layout="vertical" onSubmit={handleSubmit} style={{ width: 360 }}>
      {/* 普通 Radio.Group，默认 triggerPropName="value" 即可，无需额外配置 */}
      <Form.Item field="gender" label="性别" rules={[{ required: true, message: '请选择性别' }]}>
        <Radio.Group>
          <Radio value="male">男</Radio>
          <Radio value="female">女</Radio>
        </Radio.Group>
      </Form.Item>

      {/* 按钮样式 */}
      <Form.Item field="plan" label="套餐" rules={[{ required: true }]}>
        <Radio.Group
          type="button"
          options={[
            { label: '基础版', value: 'basic' },
            { label: '专业版', value: 'pro' },
            { label: '企业版', value: 'enterprise' },
          ]}
        />
      </Form.Item>

      <Button type="primary" htmlType="submit">提交</Button>
    </Form>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Radio — 完整 TypeScript 接口定义

## RadioProps

```typescript
interface RadioProps {
  /** 受控：是否选中 */
  checked?: boolean;
  /** 非受控：初始是否选中。默认 false */
  defaultChecked?: boolean;
  /** 是否禁用。默认 false */
  disabled?: boolean;
  /**
   * 单选框的值。
   * 在 Radio.Group 中用于标识该项（对应 Group 的 value）
   */
  value?: any;
  /**
   * 状态变化回调。
   * - e.target.checked：获取当前是否选中（boolean）
   * - e.target.value：获取当前 value
   *
   * 注意：与 Checkbox 的 onChange 不同，Radio 仍使用事件对象
   */
  onChange?: (e: Event) => void;
  /**
   * 【lingyang 专有】自定义单选图标（替换默认圆形图标）。
   * Ant Design 无此属性，需通过 CSS 自定义
   */
  icon?: ReactNode;
  /** 单选框标签内容（右侧文字，支持 ReactNode） */
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## RadioGroupProps

```typescript
interface RadioGroupProps {
  /** 受控：当前选中的值 */
  value?: any;
  /** 非受控：初始选中的值 */
  defaultValue?: any;
  /**
   * 选项数据源（快捷用法，替代手动写多个 <Radio>）。
   * 支持字符串数组、数字数组或对象数组
   */
  options?: Array<string | number | RadioOption>;
  /**
   * 单选框组样式类型。默认 'radio'。
   * 【命名差异】lingyang 用 type，Ant Design 用 optionType
   * 'radio'  = 普通圆形单选框
   * 'button' = 按钮样式单选框组
   */
  type?: 'radio' | 'button';
  /**
   * 【lingyang 专有】排列方向。默认 'horizontal'。
   * Ant Design 无此属性，需手动用 style 控制排列方向
   */
  direction?: 'horizontal' | 'vertical';
  /**
   * 按钮尺寸（仅 type='button' 时生效）。
   * 注意：lingyang 含 'mini'，Ant Design 无此尺寸
   */
  size?: 'mini' | 'small' | 'default' | 'large';
  /** 是否禁用整个单选框组。默认 false */
  disabled?: boolean;
  /**
   * 选中值变化回调。
   * 【差异】lingyang 第一参数直接为 value；
   * Ant Design 为 event，需通过 e.target.value 获取
   */
  onChange?: (value: any, e: Event) => void;
  /** 子 <Radio> 节点（与 options 二选一，children 方式更灵活） */
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## RadioOption 对象格式

```typescript
interface RadioOption {
  /** 选项展示标签（支持 ReactNode，必填） */
  label: ReactNode;
  /** 选项值（必填，对应 Group 的 value） */
  value: any;
  /** 是否禁用该选项 */
  disabled?: boolean;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| Group onChange 参数 | `(value, e)` 第一参数直接为 value | `(e)` 需 `e.target.value` |
| 按钮样式类型属性 | `type="button"` | `optionType="button"` |
| 按钮填充样式 | ❌ 无 `buttonStyle` | `buttonStyle="outline"` 或 `"solid"` |
| 排列方向 | `direction="vertical"` | ❌ 无属性，需 style |
| 自定义图标 | `icon={<ReactNode />}` | ❌ 需 CSS 自定义 |
| 最小尺寸 | `size="mini"` 可用 | 最小为 `size="small"` |

---
