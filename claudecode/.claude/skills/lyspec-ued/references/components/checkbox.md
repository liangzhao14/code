# lingyang Checkbox 复选框

**类型**: JSX 组件（受控/非受控均支持）

---

## 子组件

| 组件 | 说明 |
|------|------|
| `<Checkbox>` | 单个复选框，可独立使用，也可作为 Checkbox.Group 的子项 |
| `<Checkbox.Group>` | 复选框组，统一管理多个复选框的选中状态 |

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 单个复选框 | `<Checkbox>同意协议</Checkbox>` |
| 受控单体 | `<Checkbox checked={v} onChange={(checked) => setV(checked)}>` |
| 禁用 | `<Checkbox disabled>禁用项</Checkbox>` |
| 半选（全选场景） | `<Checkbox indeterminate={indeterminate} checked={checkAll} onChange={onCheckAll}>全选</Checkbox>` |
| 自定义图标 | `<Checkbox icon={(checked) => checked ? <IconCheck /> : <IconSquare />}>` |
| Group（options 方式） | `<Checkbox.Group options={['A','B','C']} defaultValue={['A']} />` |
| Group（children 方式） | `<Checkbox.Group value={val} onChange={setVal}><Checkbox value="a">A</Checkbox>...</Checkbox.Group>` |
| Group 纵向排列 | `<Checkbox.Group direction="vertical" options={opts} />` |
| Group 禁用整组 | `<Checkbox.Group disabled options={opts} />` |

---

## 与 Ant Design 的 5 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **onChange 参数不同（单体 Checkbox）**
   - lingyang: `onChange={(checked: boolean, e) => ...}`，第一参数**直接是 boolean**
   - Ant Design: `onChange={(e) => ...}`，需通过 `e.target.checked` 获取值

2. **Checkbox.Group 排列方向（lingyang 专有）**
   - lingyang: `<Checkbox.Group direction="vertical">` 直接支持
   - Ant Design: 无 `direction` 属性，需手动加 `style` 或 `className` 控制

3. **options 对象格式的 extra 字段（lingyang 专有）**
   - lingyang: `options={[{ value: 'a', label: '选项', extra: <p>说明</p> }]}`
   - Ant Design: 无 `extra` 字段

4. **icon 属性（lingyang 专有）**
   - lingyang: `<Checkbox icon={(checked) => ReactNode}>` 自定义选中图标
   - Ant Design: 无 `icon` 属性，需通过 CSS 覆盖

5. **全选联动**
   - lingyang 和 Ant Design 均需手动实现全选逻辑（无内置联动）
   - 区别在于 onChange 参数格式（见差异 1），影响 checkAll handler 的写法

---

## Checkbox Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| checked | boolean | — | 受控：是否选中 |
| defaultChecked | boolean | `false` | 非受控：初始是否选中 |
| indeterminate | boolean | `false` | 半选状态（破折号视觉），常用于「全选」 |
| disabled | boolean | `false` | 是否禁用 |
| value | any | — | 复选框的值（在 Group 中用于标识） |
| onChange | `(checked: boolean, e: Event) => void` | — | 变化回调（**第一参数为 boolean，非 event**） |
| icon | `(checked: boolean) => ReactNode` | — | 自定义图标渲染函数（**lingyang 专有**） |
| children | ReactNode | — | 标签内容（右侧文字） |

---

## Checkbox.Group Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | `any[]` | — | 受控：当前选中值数组 |
| defaultValue | `any[]` | `[]` | 非受控：初始选中值数组 |
| options | `(string \| CheckboxOption)[]` | — | 选项数据源（与 children 二选一） |
| direction | `'horizontal' \| 'vertical'` | `'horizontal'` | 排列方向（**lingyang 专有**） |
| disabled | boolean | `false` | 禁用整个复选框组 |
| onChange | `(values: any[]) => void` | — | 选中状态变化回调，参数为选中值数组 |

### options 对象格式

```typescript
interface CheckboxOption {
  value: any;          // 选项值（必填）
  label: ReactNode;    // 展示标签
  disabled?: boolean;  // 是否禁用该项
  extra?: ReactNode;   // 额外说明内容（lingyang 专有，Ant Design 无）
}
```

---

## 常用 CSS 类名

`.lingyang-checkbox` / `.lingyang-checkbox-checked` / `.lingyang-checkbox-indeterminate` / `.lingyang-checkbox-disabled` / `.lingyang-checkbox-inner` / `.lingyang-checkbox-label` / `.lingyang-checkbox-group` / `.lingyang-checkbox-group-direction-vertical` / `.lingyang-checkbox-group-direction-horizontal`

---

## 参考文件

- 完整代码示例（7 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Checkbox — 完整代码示例

## 1. 基本用法（非受控）

```jsx
import { Checkbox, Space } from 'lingyang';

function BasicCheckbox() {
  return (
    <Space direction="vertical">
      <Checkbox>基本复选框</Checkbox>
      <Checkbox defaultChecked>默认选中</Checkbox>
      <Checkbox disabled>禁用未选中</Checkbox>
      <Checkbox disabled defaultChecked>禁用已选中</Checkbox>
    </Space>
  );
}
```

## 2. 受控模式

```jsx
import { useState } from 'react';
import { Checkbox } from 'lingyang';

function ControlledCheckbox() {
  const [checked, setChecked] = useState(false);

  return (
    <div>
      {/*
        注意：lingyang onChange 第一参数直接是 boolean
        Ant Design 需要 e.target.checked 才能拿到 boolean
      */}
      <Checkbox
        checked={checked}
        onChange={(checked) => setChecked(checked)}
      >
        {checked ? '已选中' : '未选中'}
      </Checkbox>
    </div>
  );
}
```

## 3. 全选 / 半选（indeterminate）

```jsx
import { useState } from 'react';
import { Checkbox, Space } from 'lingyang';

const OPTIONS = ['Apple', 'Banana', 'Cherry', 'Durian'];

function CheckAllExample() {
  const [checkedList, setCheckedList] = useState(['Apple']);

  const allChecked = checkedList.length === OPTIONS.length;
  // 部分选中 → 半选状态
  const indeterminate = checkedList.length > 0 && checkedList.length < OPTIONS.length;

  const handleCheckAll = (checked) => {
    // 注意：lingyang onChange 第一参数直接是 boolean
    setCheckedList(checked ? OPTIONS : []);
  };

  const handleChange = (values) => {
    setCheckedList(values);
  };

  return (
    <Space direction="vertical">
      {/* 全选复选框：通过 indeterminate 呈现半选视觉 */}
      <Checkbox
        checked={allChecked}
        indeterminate={indeterminate}
        onChange={handleCheckAll}
      >
        全选
      </Checkbox>

      <Checkbox.Group
        value={checkedList}
        onChange={handleChange}
        options={OPTIONS}
      />

      <p>已选：{checkedList.join('、') || '无'}</p>
    </Space>
  );
}
```

## 4. Checkbox.Group — options 方式

```jsx
import { useState } from 'react';
import { Checkbox } from 'lingyang';

function GroupWithOptions() {
  const [value, setValue] = useState(['react']);

  const options = [
    { value: 'react', label: 'React' },
    { value: 'vue', label: 'Vue' },
    { value: 'angular', label: 'Angular', disabled: true },
    // extra 为 lingyang 专有字段，Ant Design 无此选项
    { value: 'svelte', label: 'Svelte', extra: <span style={{ color: '#888', fontSize: 12 }}>新兴框架</span> },
  ];

  return (
    <div>
      <Checkbox.Group
        value={value}
        onChange={setValue}
        options={options}
      />
      <p>已选：{value.join(', ')}</p>
    </div>
  );
}
```

## 5. Checkbox.Group — children 方式 + 纵向排列

```jsx
import { useState } from 'react';
import { Checkbox } from 'lingyang';

function GroupWithChildren() {
  const [value, setValue] = useState(['mon', 'wed']);

  return (
    <div>
      {/*
        direction="vertical" 为 lingyang 专有
        Ant Design 无此属性，需手动 style 控制
      */}
      <Checkbox.Group
        value={value}
        onChange={setValue}
        direction="vertical"
      >
        <Checkbox value="mon">周一</Checkbox>
        <Checkbox value="tue">周二</Checkbox>
        <Checkbox value="wed">周三</Checkbox>
        <Checkbox value="thu">周四</Checkbox>
        <Checkbox value="fri">周五</Checkbox>
      </Checkbox.Group>
      <p>选中日期：{value.join(', ')}</p>
    </div>
  );
}
```

## 6. 自定义图标（icon — lingyang 专有）

```jsx
import { Checkbox, Space } from 'lingyang';
import { IconCheckSquareFill, IconMinusSquareFill, IconSquare } from 'lingyang/icon';

function IconCheckbox() {
  // icon 为 lingyang 专有属性，Ant Design 无，需通过 CSS 自定义
  return (
    <Space>
      <Checkbox
        icon={(checked) =>
          checked
            ? <IconCheckSquareFill style={{ color: '#165DFF' }} />
            : <IconSquare style={{ color: '#C9CDD4' }} />
        }
      >
        自定义图标
      </Checkbox>

      <Checkbox
        defaultChecked
        icon={(checked) =>
          checked
            ? <IconCheckSquareFill style={{ color: '#00B42A' }} />
            : <IconSquare style={{ color: '#C9CDD4' }} />
        }
      >
        绿色图标（已选）
      </Checkbox>
    </Space>
  );
}
```

## 7. 在表单场景中使用（配合协议勾选）

```jsx
import { useState } from 'react';
import { Checkbox, Button, Space } from 'lingyang';

function AgreementCheckbox() {
  const [agreed, setAgreed] = useState(false);

  const handleSubmit = () => {
    if (!agreed) {
      alert('请先同意用户协议');
      return;
    }
    alert('提交成功');
  };

  return (
    <Space direction="vertical">
      <Checkbox
        checked={agreed}
        onChange={(checked) => setAgreed(checked)}
      >
        我已阅读并同意
        <a href="#" style={{ marginLeft: 4 }}>《用户服务协议》</a>
        和
        <a href="#" style={{ marginLeft: 4 }}>《隐私政策》</a>
      </Checkbox>

      <Button
        type="primary"
        disabled={!agreed}
        onClick={handleSubmit}
      >
        注册
      </Button>
    </Space>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Checkbox — 完整 TypeScript 接口定义

## CheckboxProps

```typescript
interface CheckboxProps {
  /** 受控：是否选中 */
  checked?: boolean;
  /** 非受控：初始是否选中。默认 false */
  defaultChecked?: boolean;
  /**
   * 是否为半选状态（视觉上的破折号样式）。默认 false。
   * 常用于「全选」复选框：当子项部分选中时设为 true，全部选中时设为 false。
   * 需手动根据子项状态计算并传入，lingyang 无自动联动。
   */
  indeterminate?: boolean;
  /** 是否禁用。默认 false */
  disabled?: boolean;
  /**
   * 复选框的值。
   * 在 Checkbox.Group 中用于标识该项（对应 Group 的 value 数组成员）
   */
  value?: any;
  /**
   * 状态变化回调。
   * 【差异】lingyang 第一参数直接为 checked boolean；
   * Ant Design 为 ChangeEvent，需通过 e.target.checked 获取
   */
  onChange?: (checked: boolean, e: Event) => void;
  /**
   * 【lingyang 专有】自定义选中图标的渲染函数。
   * Ant Design 无此属性，需通过 CSS 覆盖实现自定义样式
   */
  icon?: (checked: boolean) => ReactNode;
  /** 复选框标签内容（右侧文字，支持 ReactNode） */
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## CheckboxGroupProps

```typescript
interface CheckboxGroupProps {
  /** 受控：当前选中的值数组 */
  value?: any[];
  /** 非受控：初始选中的值数组。默认 [] */
  defaultValue?: any[];
  /**
   * 选项数据源（与 children 二选一，options 方式更简洁）。
   * 支持字符串数组或 CheckboxOption 对象数组
   */
  options?: Array<string | CheckboxOption>;
  /**
   * 【lingyang 专有】排列方向。默认 'horizontal'。
   * Ant Design 无此属性，需通过 style/className 控制排列方向
   */
  direction?: 'horizontal' | 'vertical';
  /** 是否禁用整个复选框组（优先级低于子项自身的 disabled）。默认 false */
  disabled?: boolean;
  /** 选中状态变化回调，参数为当前所有选中值的数组 */
  onChange?: (values: any[]) => void;
  /** 子 <Checkbox> 节点（与 options 二选一，children 方式更灵活） */
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## CheckboxOption（options 数组对象格式）

```typescript
interface CheckboxOption {
  /** 选项值（必填，对应 Group 的 value 数组成员） */
  value: any;
  /** 选项展示标签（支持 ReactNode） */
  label: ReactNode;
  /** 是否禁用该选项 */
  disabled?: boolean;
  /**
   * 【lingyang 专有】选项的额外说明内容（渲染在标签下方）。
   * Ant Design CheckboxOptionType 无此字段
   */
  extra?: ReactNode;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| Checkbox onChange 参数 | `(checked: boolean, e: Event)` 直接返回 boolean | `(e: CheckboxChangeEvent)` 需用 `e.target.checked` |
| Group 排列方向 | `direction="vertical"` 属性 | ❌ 无属性，需 style/className |
| options extra 字段 | `{ value, label, extra }` 支持 | ❌ 无 extra |
| 自定义图标 | `icon={(checked) => ReactNode}` | ❌ 需 CSS 覆盖 |
| 全选联动 | 需手动实现（无内置） | 需手动实现（无内置） |

---
