# lingyang AutoComplete 自动补全

**类型**: JSX 组件（受控/非受控均支持）

> **与 Select 的核心区别**：AutoComplete 允许用户自由输入任意内容，候选项只是辅助提示，最终值是输入的字符串。Select 只能从预定义选项中选取。

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本用法 | `<AutoComplete data={['Option1', 'Option2']} placeholder="请输入" />` |
| 受控模式 | `<AutoComplete value={val} onChange={setVal} data={options} />` |
| 动态搜索（不过滤） | `<AutoComplete onSearch={fetchOptions} data={options} filterOption={false} />` |
| 自定义过滤 | `<AutoComplete filterOption={(input, opt) => opt.value.startsWith(input)} />` |
| 严格大小写匹配 | `<AutoComplete strict data={options} />` |
| 允许清除 | `<AutoComplete allowClear data={options} />` |
| 加载中状态 | `<AutoComplete loading data={[]} />` |
| 自定义下拉内容 | `<AutoComplete dropdownRender={(menu) => <><p>提示</p>{menu}</>} />` |
| 选中回调 | `<AutoComplete onSelect={(val, opt) => console.log(val, opt)} />` |
| 回车回调 | `<AutoComplete onPressEnter={(e, activeOpt) => ...} />` |

---

## 与 Ant Design 的 6 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **数据源属性名不同**
   - lingyang: `data={['A', 'B']}` 或 `data={[{ value: 'a', label: '选项' }]}`
   - Ant Design: `options={[{ value: 'a', label: '选项' }]}`

2. **自定义触发元素属性名不同**
   - lingyang: `triggerElement={<CustomInput />}`
   - Ant Design: `children={<CustomInput />}`（作为 children 传入）

3. **受控下拉显隐属性名不同**
   - lingyang: `popupVisible` / `defaultPopupVisible`
   - Ant Design: `open` / `defaultOpen`

4. **显隐回调名不同**
   - lingyang: `onVisibleChange={(visible) => ...}`
   - Ant Design: `onDropdownVisibleChange={(open) => ...}`

5. **尺寸枚举不同**
   - lingyang: `size="mini"` 可用（4 种：mini/small/default/large）
   - Ant Design: `size="middle"` 替代中间尺寸（3 种：small/middle/large，无 mini）

6. **严格匹配（lingyang 专有）**
   - lingyang: `strict={true}` 开启大小写敏感过滤
   - Ant Design: 无 strict，须用 `filterOption={(input, opt) => ...}` 自定义

---

## Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | string | — | 受控：当前输入值 |
| defaultValue | string | — | 非受控：初始输入值 |
| data | `string[] \| Option[]` | — | 候选项数据源（**注意：不是 options**） |
| onChange | `(value: string) => void` | — | 值变化回调（含选中和输入） |
| onSelect | `(value: string, option: OptionInfo) => void` | — | 点击选中候选项时回调 |
| onSearch | `(value: string) => void` | — | 输入变化搜索回调（用于动态更新 data） |
| filterOption | `boolean \| function` | `true` | 过滤逻辑（true=内置，false=不过滤，函数=自定义） |
| strict | boolean | `false` | 大小写严格匹配（**lingyang 专有**） |
| placeholder | string | — | 占位文本 |
| disabled | boolean | `false` | 是否禁用 |
| allowClear | boolean | `false` | 是否显示清除按钮 |
| loading | boolean | `false` | 是否显示加载状态 |
| error | boolean | `false` | 是否为错误状态（红色边框） |
| size | `'mini'\|'small'\|'default'\|'large'` | `'default'` | 尺寸（含 mini，Ant Design 无） |
| popupVisible | boolean | — | 受控：是否显示下拉（**不是 open**） |
| defaultPopupVisible | boolean | `false` | 非受控：初始是否显示下拉 |
| onVisibleChange | `(visible: boolean) => void` | — | 下拉显隐回调（**不是 onDropdownVisibleChange**） |
| triggerElement | ReactNode | — | 自定义触发元素（**不是 children**） |
| inputProps | InputProps | — | 传给内部 Input 的额外属性 |
| dropdownRender | `(menu: ReactNode) => ReactNode` | — | 自定义下拉菜单内容 |
| getPopupContainer | `() => HTMLElement` | — | 指定挂载容器（无参数） |
| virtualListProps | object | — | 虚拟滚动配置（大数据量时使用） |
| onPressEnter | `(e: KeyboardEvent, activeOption?) => void` | — | 按下回车回调 |
| onFocus | `(e: FocusEvent) => void` | — | 聚焦回调 |
| onBlur | `(e: FocusEvent) => void` | — | 失焦回调 |

### data 数据格式

```typescript
// 字符串数组（最简洁）
data={['Apple', 'Banana', 'Cherry']}

// 对象数组
data={[
  { value: 'apple', label: '苹果' },
  { value: 'banana', label: '香蕉', disabled: true },
  { value: 'cherry', label: '樱桃', extra: { code: 'CH' } }
]}
```

---

## 常用 CSS 类名

`.lingyang-auto-complete` / `.lingyang-auto-complete-popup` / `.lingyang-select-option` / `.lingyang-select-option-selected` / `.lingyang-select-option-disabled` / `.lingyang-input`（内部 Input 继承）

---

## 参考文件

- 完整代码示例（7 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang AutoComplete — 完整代码示例

## 1. 基本用法（字符串数组）

```jsx
import { AutoComplete } from 'lingyang';

function BasicAutoComplete() {
  return (
    // 注意：lingyang 用 data，Ant Design 用 options
    <AutoComplete
      data={['React', 'Vue', 'Angular', 'Svelte', 'Solid']}
      placeholder="请输入框架名称"
      style={{ width: 300 }}
    />
  );
}
```

## 2. 受控模式 + onSelect 回调

```jsx
import { useState } from 'react';
import { AutoComplete } from 'lingyang';

function ControlledAutoComplete() {
  const [value, setValue] = useState('');
  const [selected, setSelected] = useState('');

  const options = [
    { value: 'beijing', label: '北京' },
    { value: 'shanghai', label: '上海' },
    { value: 'guangzhou', label: '广州' },
    { value: 'shenzhen', label: '深圳' },
  ];

  return (
    <div>
      <AutoComplete
        value={value}
        onChange={setValue}
        // onSelect 只在点击候选项时触发，手动输入不触发
        onSelect={(val, option) => setSelected(`选中：${val}（${option.label}）`)}
        data={options}
        placeholder="请输入城市"
        allowClear
        style={{ width: 300 }}
      />
      {selected && <p style={{ marginTop: 8 }}>{selected}</p>}
    </div>
  );
}
```

## 3. 动态异步搜索（服务端过滤）

```jsx
import { useState } from 'react';
import { AutoComplete } from 'lingyang';

function AsyncAutoComplete() {
  const [options, setOptions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (keyword) => {
    if (!keyword) {
      setOptions([]);
      return;
    }
    setLoading(true);
    // 模拟异步请求
    await new Promise(r => setTimeout(r, 500));
    setOptions(
      ['apple', 'application', 'apply', 'appreciate']
        .filter(item => item.includes(keyword))
        .map(item => ({ value: item, label: item }))
    );
    setLoading(false);
  };

  return (
    // filterOption={false}：关闭前端过滤，由 onSearch 返回的 data 直接展示
    <AutoComplete
      data={options}
      loading={loading}
      onSearch={handleSearch}
      filterOption={false}
      placeholder="输入关键词搜索"
      style={{ width: 300 }}
    />
  );
}
```

## 4. 自定义过滤逻辑

```jsx
import { AutoComplete } from 'lingyang';

function FilterAutoComplete() {
  const data = ['Gmail', 'github', 'Google', 'gitlab', 'Grafana'];

  return (
    <div style={{ display: 'flex', gap: 16 }}>
      {/* 默认内置过滤（不区分大小写） */}
      <AutoComplete
        data={data}
        placeholder="默认过滤（不区分大小写）"
        style={{ width: 240 }}
      />

      {/* strict=true：lingyang 专有，区分大小写。Ant Design 无此属性 */}
      <AutoComplete
        data={data}
        strict
        placeholder="strict 模式（区分大小写）"
        style={{ width: 240 }}
      />

      {/* 自定义过滤函数：只匹配以输入值开头的选项 */}
      <AutoComplete
        data={data}
        filterOption={(input, option) =>
          option.value.toLowerCase().startsWith(input.toLowerCase())
        }
        placeholder="自定义：startsWith 匹配"
        style={{ width: 240 }}
      />
    </div>
  );
}
```

## 5. 错误状态 + 4 种尺寸

```jsx
import { AutoComplete, Space } from 'lingyang';

const data = ['Option 1', 'Option 2', 'Option 3'];

function SizeAndErrorAutoComplete() {
  return (
    <Space direction="vertical" style={{ width: 300 }}>
      {/* 错误状态（红色边框） */}
      <AutoComplete data={data} error placeholder="错误状态" />

      {/* lingyang 独有的 mini 尺寸（Ant Design 无） */}
      <AutoComplete data={data} size="mini" placeholder="mini" />
      <AutoComplete data={data} size="small" placeholder="small" />
      <AutoComplete data={data} size="default" placeholder="default" />
      <AutoComplete data={data} size="large" placeholder="large" />
    </Space>
  );
}
```

## 6. 自定义触发元素（triggerElement）

```jsx
import { AutoComplete, Input } from 'lingyang';
import { IconSearch } from 'lingyang/icon';

function CustomTriggerAutoComplete() {
  return (
    // 注意：lingyang 用 triggerElement，Ant Design 用 children
    <AutoComplete
      data={['JavaScript', 'TypeScript', 'Python', 'Rust', 'Go']}
      triggerElement={
        <Input.Search
          placeholder="搜索编程语言"
          style={{ width: 300 }}
        />
      }
    />
  );
}
```

## 7. 自定义下拉内容（dropdownRender）+ 回车回调

```jsx
import { useState } from 'react';
import { AutoComplete, Divider, Button } from 'lingyang';
import { IconPlus } from 'lingyang/icon';

function DropdownRenderAutoComplete() {
  const [options, setOptions] = useState(['北京', '上海', '广州']);
  const [inputVal, setInputVal] = useState('');

  const handleAdd = () => {
    if (inputVal && !options.includes(inputVal)) {
      setOptions([...options, inputVal]);
    }
  };

  return (
    <AutoComplete
      value={inputVal}
      onChange={setInputVal}
      data={options}
      placeholder="输入或新增城市"
      style={{ width: 300 }}
      // 在下拉菜单底部追加"新增"按钮
      dropdownRender={(menu) => (
        <>
          {menu}
          <Divider style={{ margin: '4px 0' }} />
          <Button
            type="text"
            icon={<IconPlus />}
            style={{ width: '100%' }}
            onClick={handleAdd}
          >
            新增 "{inputVal}"
          </Button>
        </>
      )}
      // 按回车时也可触发新增
      onPressEnter={(e, activeOption) => {
        if (!activeOption) handleAdd();
      }}
    />
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang AutoComplete — 完整 TypeScript 接口定义

## AutoCompleteProps

```typescript
// 候选项对象格式
interface AutoCompleteOption {
  /** 选项实际值（必填） */
  value: string;
  /** 选项名称（可选，用于匹配） */
  name?: string;
  /** 选项展示内容（支持 ReactNode，默认用 value） */
  label?: ReactNode;
  /** 是否禁用该选项 */
  disabled?: boolean;
  /** 附加任意自定义数据，可在回调中获取 */
  extra?: any;
}

interface AutoCompleteProps {
  /** 受控：输入框当前值 */
  value?: string;
  /** 非受控：输入框初始值 */
  defaultValue?: string;
  /**
   * 候选项数据源。
   * 【命名差异】lingyang 用 data，Ant Design 用 options
   * 支持字符串数组或 AutoCompleteOption 对象数组
   */
  data?: string[] | AutoCompleteOption[];
  /**
   * 输入框值变化（含选中候选项和手动输入）时的回调
   * 参数为当前字符串值
   */
  onChange?: (value: string) => void;
  /**
   * 从候选项列表中点击选中时的回调
   * 区别于 onChange（只有点击选项才触发，手动输入不触发）
   */
  onSelect?: (value: string, option: AutoCompleteOption) => void;
  /**
   * 输入内容变化时的搜索回调
   * 用于动态请求数据并更新 data
   */
  onSearch?: (value: string) => void;
  /**
   * 候选项过滤逻辑。
   * - true（默认）：内置 contains 模糊匹配
   * - false：不过滤，全量展示 data（适合服务端过滤/动态搜索场景）
   * - 函数：自定义过滤逻辑
   */
  filterOption?: boolean | ((inputValue: string, option: AutoCompleteOption) => boolean);
  /**
   * 【lingyang 专有】严格模式：filterOption 内置匹配时区分大小写。
   * Ant Design 无此属性，需通过 filterOption 函数自定义
   */
  strict?: boolean;
  /** 输入框占位提示文本 */
  placeholder?: string;
  /** 是否禁用。默认 false */
  disabled?: boolean;
  /** 是否显示清除按钮。默认 false */
  allowClear?: boolean;
  /** 是否显示加载状态（候选项区域显示 loading 指示器）。默认 false */
  loading?: boolean;
  /** 是否为错误状态（输入框红色边框）。默认 false */
  error?: boolean;
  /**
   * 输入框尺寸。默认 'default'。
   * 【差异】lingyang 含 'mini'（4 种）；Ant Design 含 'middle' 无 'mini'（3 种）
   */
  size?: 'mini' | 'small' | 'default' | 'large';
  /**
   * 受控：是否显示下拉弹层。
   * 【命名差异】lingyang 用 popupVisible，Ant Design v5 用 open
   */
  popupVisible?: boolean;
  /**
   * 非受控：初始是否显示下拉弹层。默认 false
   */
  defaultPopupVisible?: boolean;
  /**
   * 下拉弹层显隐变化回调。
   * 【命名差异】lingyang 用 onVisibleChange，Ant Design 用 onDropdownVisibleChange
   */
  onVisibleChange?: (visible: boolean) => void;
  /**
   * 自定义触发元素（替代默认 Input）。
   * 【命名差异】lingyang 用 triggerElement，Ant Design 用 children
   */
  triggerElement?: ReactNode;
  /** 传递给触发器 Trigger 组件的额外属性 */
  triggerProps?: object;
  /** 传递给内部 Input 组件的额外属性 */
  inputProps?: InputProps;
  /** 自定义下拉菜单内容的渲染函数（可在菜单前/后追加内容） */
  dropdownRender?: (menu: ReactNode) => ReactNode;
  /**
   * 指定下拉弹层挂载的容器节点。
   * 【差异】lingyang 无参数；Ant Design 传入 triggerNode: HTMLElement
   */
  getPopupContainer?: () => HTMLElement;
  /** 虚拟滚动配置，候选项数量很多时开启以提升性能 */
  virtualListProps?: object;
  /** 按下回车键时的回调，第二个参数为当前高亮的候选项（如有） */
  onPressEnter?: (e: KeyboardEvent, activeOption?: AutoCompleteOption) => void;
  /** 输入框聚焦回调 */
  onFocus?: (e: FocusEvent) => void;
  /** 输入框失焦回调 */
  onBlur?: (e: FocusEvent) => void;
  style?: CSSProperties;
  className?: string;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| 数据源属性名 | `data` | `options` |
| 自定义触发元素 | `triggerElement={<Input />}` | `children={<Input />}` |
| 受控显示属性 | `popupVisible` | `open` |
| 非受控初始显示 | `defaultPopupVisible` | `defaultOpen` |
| 显隐回调 | `onVisibleChange` | `onDropdownVisibleChange` |
| 尺寸枚举 | mini / small / default / large | small / middle / large |
| 严格大小写匹配 | `strict={true}` | ❌ 需用 filterOption 函数 |
| 挂载容器 | `getPopupContainer: () => HTMLElement`（无参数） | `getPopupContainer: (triggerNode) => HTMLElement` |

---
