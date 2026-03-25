# lingyang Select 选择器

**类型**: JSX 组件（受控/非受控均支持）

---

## 子组件

| 组件 | 说明 |
|------|------|
| `<Select>` | 主选择器，管理选中状态、下拉弹层等全局配置 |
| `<Select.Option>` | 单个选项（children 方式使用） |
| `<Select.OptGroup>` | 选项分组容器 |

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本单选（options） | `<Select options={['A','B','C']} placeholder="请选择" />` |
| 基本单选（children） | `<Select><Option value="a">A</Option></Select>` |
| 受控单选 | `<Select value={val} onChange={(v) => setVal(v)} options={opts} />` |
| 多选 | `<Select mode="multiple" value={arr} onChange={setArr} options={opts} />` |
| 标签输入 | `<Select mode="tags" tokenSeparators={[',']} />` |
| 带搜索 | `<Select showSearch options={opts} />` |
| 远程搜索 | `<Select showSearch filterOption={false} onSearch={fetchOpts} loading={loading} />` |
| 允许创建 | `<Select allowCreate showSearch options={opts} />` |
| 分组选项 | `<Select><OptGroup label="组A"><Option value="a">A</Option></OptGroup></Select>` |
| 多选限制数量 | `<Select mode="multiple" maxTagCount={3} options={opts} />` |
| 自定义空状态 | `<Select noDataElement={<p>暂无数据</p>} />` |
| 自定义下拉 | `<Select dropdownRender={(menu) => <>{menu}<Divider /><Button>新增</Button></>} />` |
| 虚拟滚动 | `<Select virtualListProps={{ height: 200 }} options={largeList} />` |
| 受控下拉显隐 | `<Select popupVisible={vis} onVisibleChange={setVis} />` |

---

## 与 Ant Design 的 10 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **受控显隐属性名不同**
   - lingyang: `popupVisible` / `defaultPopupVisible`
   - Ant Design: `open` / `defaultOpen`

2. **显隐回调名不同**
   - lingyang: `onVisibleChange={(visible) => ...}`
   - Ant Design: `onDropdownVisibleChange={(open) => ...}`

3. **空状态属性名不同**
   - lingyang: `noDataElement={<ReactNode />}`
   - Ant Design: `notFoundContent={<ReactNode />}`

4. **尺寸枚举不同**
   - lingyang: `size="mini"` 可用（4 种：mini/small/default/large）
   - Ant Design: `size="middle"` 替代中间尺寸（3 种：small/middle/large，无 mini）

5. **getPopupContainer 参数不同**
   - lingyang: `getPopupContainer={() => HTMLElement}`（无参数）
   - Ant Design: `getPopupContainer={(triggerNode) => HTMLElement}`

6. **虚拟滚动配置方式不同**
   - lingyang: `virtualListProps={{ height: 200, itemHeight: 36 }}`（配置对象）
   - Ant Design: `virtual={true}`（布尔开关）

7. **allowCreate（lingyang 专有）**
   - lingyang: `allowCreate={true}` 允许用户输入并创建新选项
   - Ant Design: 无直接等价（需 tags 模式或动态注入实现）

8. **triggerElement（lingyang 专有）**
   - lingyang: `triggerElement={<Button />}` 自定义触发元素
   - Ant Design: 无直接等价

9. **filterOption 的 option 参数类型不同**
   - lingyang: `filterOption={(input, option) => ...}` option 为 **ReactElement**
   - Ant Design: option 为 **OptionType 对象**（直接有 .value .label 属性）

10. **maxTagCount 类型不同**
    - lingyang: 仅支持 `number`
    - Ant Design: 支持 `number | 'responsive'`

---

## Select Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | `any \| any[]` | — | 受控：当前选中值（多选为数组） |
| defaultValue | `any \| any[]` | — | 非受控：初始值 |
| options | `(string \| number \| SelectOption)[]` | — | 选项数据源 |
| mode | `'multiple' \| 'tags'` | — | 多选/标签模式（不传则为单选） |
| placeholder | string | — | 占位文本 |
| disabled | boolean | `false` | 是否禁用 |
| allowClear | boolean | `false` | 是否显示清除按钮 |
| allowCreate | `boolean \| object` | `false` | 允许创建新选项（**lingyang 专有**） |
| showSearch | boolean | `false` | 是否显示搜索框（单选时） |
| filterOption | `boolean \| function` | `true` | 过滤逻辑（function 的 option 为 ReactElement） |
| loading | boolean | `false` | 是否显示 loading |
| error | boolean | `false` | 是否为错误状态 |
| size | `'mini'\|'small'\|'default'\|'large'` | `'default'` | 尺寸（含 mini，**不是 middle**） |
| popupVisible | boolean | — | 受控：是否显示下拉（**不是 open**） |
| defaultPopupVisible | boolean | `false` | 非受控：初始是否显示下拉 |
| onVisibleChange | `(visible: boolean) => void` | — | 显隐回调（**不是 onDropdownVisibleChange**） |
| onChange | `(value, option) => void` | — | 值变化回调 |
| onSearch | `(inputValue: string) => void` | — | 搜索回调（用于动态更新 options） |
| onSelect | `(value, option) => void` | — | 选中某项回调 |
| onDeselect | `(value, option) => void` | — | 取消选中回调（多选） |
| onClear | `() => void` | — | 点击清除回调 |
| maxTagCount | number | — | 多选时最多展示标签数（仅 number） |
| maxTagTextLength | number | — | 标签文字最大长度 |
| renderTag | function | — | 自定义标签渲染 |
| tokenSeparators | `string[]` | — | tags 模式的分隔符 |
| noDataElement | ReactNode | — | 空状态（**不是 notFoundContent**） |
| triggerElement | ReactNode | — | 自定义触发元素（**lingyang 专有**） |
| dropdownRender | `(menu) => ReactNode` | — | 自定义下拉内容 |
| dropdownMenuStyle | CSSProperties | — | 下拉菜单样式 |
| getPopupContainer | `() => HTMLElement` | — | 指定挂载容器（**无参数**） |
| virtualListProps | `{ height?, itemHeight?, threshold? }` | — | 虚拟滚动配置（**不是 virtual: boolean**） |
| prefix | ReactNode | — | 选择框左侧前缀 |
| suffixIcon | ReactNode | — | 自定义后缀图标 |
| arrowIcon | ReactNode | — | 自定义箭头图标 |
| removeIcon | ReactNode | — | 多选标签的自定义删除图标 |

### SelectOption 对象格式

```typescript
interface SelectOption {
  value: string | number | boolean;  // 必填
  label?: ReactNode;                  // 展示标签
  disabled?: boolean;                 // 是否禁用
  extra?: any;                        // 附加自定义数据
}
```

---

## 常用 CSS 类名

`.lingyang-select` / `.lingyang-select-view` / `.lingyang-select-view-focus` / `.lingyang-select-error` / `.lingyang-select-disabled` / `.lingyang-select-dropdown` / `.lingyang-select-option` / `.lingyang-select-option-selected` / `.lingyang-select-option-disabled` / `.lingyang-select-group-title` / `.lingyang-select-tag` / `.lingyang-select-size-{mini|small|large}` / `.lingyang-select-prefix`

---

## 参考文件

- 完整代码示例（8 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Select — 完整代码示例

## 1. 基本用法（单选 — options 方式）

```jsx
import { Select } from 'lingyang';

function BasicSelect() {
  return (
    <Select
      placeholder="请选择城市"
      style={{ width: 240 }}
      options={[
        { value: 'beijing', label: '北京' },
        { value: 'shanghai', label: '上海' },
        { value: 'guangzhou', label: '广州', disabled: true },
        { value: 'shenzhen', label: '深圳' },
      ]}
    />
  );
}
```

---

## 2. 受控模式 + onChange

```jsx
import { useState } from 'react';
import { Select } from 'lingyang';

function ControlledSelect() {
  const [value, setValue] = useState('');

  return (
    <Select
      value={value}
      onChange={(val, option) => {
        setValue(val);
        console.log('选中选项：', option); // { value, label, ... }
      }}
      allowClear
      placeholder="请选择"
      style={{ width: 240 }}
      options={['React', 'Vue', 'Angular', 'Svelte']}
    />
  );
}
```

---

## 3. 多选（mode="multiple"）+ maxTagCount

```jsx
import { useState } from 'react';
import { Select } from 'lingyang';

function MultipleSelect() {
  const [value, setValue] = useState(['react']);

  const options = [
    { value: 'react', label: 'React' },
    { value: 'vue', label: 'Vue' },
    { value: 'angular', label: 'Angular' },
    { value: 'svelte', label: 'Svelte' },
    { value: 'solid', label: 'Solid' },
  ];

  return (
    <Select
      mode="multiple"
      value={value}
      onChange={(vals) => setValue(vals)}
      // 最多展示 2 个标签，超出显示 +N
      // 注意：lingyang maxTagCount 只支持 number，Ant Design 还支持 'responsive'
      maxTagCount={2}
      allowClear
      placeholder="请选择框架（多选）"
      style={{ width: 300 }}
      options={options}
    />
  );
}
```

---

## 4. 带搜索（showSearch）+ 自定义空状态

```jsx
import { Select, Empty } from 'lingyang';

function SearchSelect() {
  return (
    <Select
      showSearch
      placeholder="搜索并选择"
      style={{ width: 240 }}
      options={[
        { value: 'apple', label: '苹果' },
        { value: 'banana', label: '香蕉' },
        { value: 'cherry', label: '樱桃' },
        { value: 'durian', label: '榴莲' },
      ]}
      // 注意：lingyang 用 noDataElement，Ant Design 用 notFoundContent
      noDataElement={<Empty description="未找到匹配项" />}
    />
  );
}
```

---

## 5. 远程搜索（服务端过滤）

```jsx
import { useState } from 'react';
import { Select } from 'lingyang';

function RemoteSearchSelect() {
  const [options, setOptions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (keyword) => {
    if (!keyword) { setOptions([]); return; }
    setLoading(true);
    await new Promise(r => setTimeout(r, 600)); // 模拟请求
    setOptions(
      ['javascript', 'typescript', 'java', 'python', 'go', 'rust']
        .filter(s => s.includes(keyword.toLowerCase()))
        .map(s => ({ value: s, label: s }))
    );
    setLoading(false);
  };

  return (
    // filterOption={false}：禁用前端过滤，完全由 onSearch 返回的 options 决定
    <Select
      showSearch
      filterOption={false}
      loading={loading}
      onSearch={handleSearch}
      options={options}
      placeholder="输入关键词搜索语言"
      style={{ width: 280 }}
      // 注意：lingyang 用 noDataElement，Ant Design 用 notFoundContent
      noDataElement={loading ? null : <span>无匹配结果</span>}
    />
  );
}
```

---

## 6. 分组选项（OptGroup）

```jsx
import { Select } from 'lingyang';
const { Option, OptGroup } = Select;

function GroupedSelect() {
  return (
    <Select placeholder="请选择" style={{ width: 240 }}>
      <OptGroup label="前端框架">
        <Option value="react">React</Option>
        <Option value="vue">Vue</Option>
        <Option value="angular">Angular</Option>
      </OptGroup>
      <OptGroup label="后端框架">
        <Option value="express">Express</Option>
        <Option value="django">Django</Option>
        <Option value="spring">Spring</Option>
      </OptGroup>
    </Select>
  );
}
```

---

## 7. 允许创建新选项（allowCreate — lingyang 专有）

```jsx
import { useState } from 'react';
import { Select } from 'lingyang';

function AllowCreateSelect() {
  const [options, setOptions] = useState([
    { value: 'react', label: 'React' },
    { value: 'vue', label: 'Vue' },
  ]);
  const [value, setValue] = useState(undefined);

  const handleChange = (val, option) => {
    // 如果是新创建的选项，可以保存到 options 中
    if (option && !options.find(o => o.value === val)) {
      setOptions([...options, { value: val, label: val }]);
    }
    setValue(val);
  };

  return (
    // allowCreate 为 lingyang 专有，Ant Design 无直接对应
    <Select
      showSearch
      allowCreate
      value={value}
      onChange={handleChange}
      options={options}
      placeholder="选择或输入创建新选项"
      style={{ width: 280 }}
    />
  );
}
```

---

## 8. 自定义下拉内容（dropdownRender）+ 虚拟滚动

```jsx
import { useState } from 'react';
import { Select, Divider, Button, Input } from 'lingyang';
import { IconPlus } from 'lingyang/icon';

// 生成大量选项测试虚拟滚动
const largeOptions = Array.from({ length: 1000 }, (_, i) => ({
  value: `item-${i}`,
  label: `选项 ${i + 1}`,
}));

function DropdownRenderSelect() {
  const [inputVal, setInputVal] = useState('');
  const [options, setOptions] = useState(largeOptions.slice(0, 20));

  const handleAddOption = () => {
    if (inputVal) {
      setOptions([{ value: inputVal, label: inputVal }, ...options]);
      setInputVal('');
    }
  };

  return (
    <Select
      placeholder="选择或新增"
      style={{ width: 300 }}
      options={options}
      // 虚拟滚动：lingyang 用配置对象，Ant Design 用 virtual: boolean
      virtualListProps={{ height: 200, itemHeight: 36 }}
      dropdownRender={(menu) => (
        <>
          <div style={{ padding: '8px 12px', display: 'flex', gap: 8 }}>
            <Input
              size="small"
              value={inputVal}
              onChange={setInputVal}
              placeholder="输入新选项"
            />
            <Button size="small" icon={<IconPlus />} onClick={handleAddOption}>
              新增
            </Button>
          </div>
          <Divider style={{ margin: '4px 0' }} />
          {menu}
        </>
      )}
    />
  );
}
```

---

## 9. 在 Form 中使用

```jsx
import { Form, Select, Button } from 'lingyang';

function FormWithSelect() {
  const [form] = Form.useForm();

  const handleSubmit = (values) => {
    console.log('提交值：', values);
  };

  return (
    // 注意：Form.Item 用 field（不是 name），lingyang 专有
    <Form form={form} layout="vertical" onSubmit={handleSubmit} style={{ width: 360 }}>
      <Form.Item
        field="city"
        label="城市"
        rules={[{ required: true, message: '请选择城市' }]}
      >
        <Select
          placeholder="请选择城市"
          options={[
            { value: 'beijing', label: '北京' },
            { value: 'shanghai', label: '上海' },
            { value: 'guangzhou', label: '广州' },
          ]}
        />
      </Form.Item>

      <Form.Item
        field="tags"
        label="标签（多选）"
        rules={[{ required: true, message: '请至少选择一个标签' }]}
      >
        <Select
          mode="multiple"
          placeholder="请选择标签"
          maxTagCount={3}
          options={['技术', '产品', '设计', '运营', '市场']}
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

# lingyang Select — 完整 TypeScript 接口定义

## SelectProps

```typescript
type SelectValue = string | number | boolean;

interface SelectProps {
  /** 受控：当前选中值。单选为单值，多选为数组 */
  value?: SelectValue | SelectValue[];
  /** 非受控：初始选中值 */
  defaultValue?: SelectValue | SelectValue[];
  /**
   * 选项数据源（与 children 方式二选一）。
   * 支持字符串/数字数组或 SelectOption 对象数组
   */
  options?: Array<string | number | SelectOption>;
  /**
   * 多选模式。不传则为单选。
   * 'multiple' = 标准多选（只能选已有选项）
   * 'tags'     = 标签输入模式（可输入任意值创建新标签）
   */
  mode?: 'multiple' | 'tags';
  /** 选择框占位提示文本 */
  placeholder?: string;
  /** 是否禁用。默认 false */
  disabled?: boolean;
  /** 是否显示清除按钮。默认 false */
  allowClear?: boolean;
  /**
   * 【lingyang 专有】是否允许通过输入创建新选项。默认 false。
   * 传对象时可自定义新选项的格式：{ formatter: (inputValue, creating) => SelectOption }
   * Ant Design 无直接对应，需通过 tags 模式或动态注入实现
   */
  allowCreate?: boolean | {
    formatter: (inputValue: string, creating: boolean) => SelectOption;
  };
  /** 是否在单选模式下显示搜索输入框。默认 false */
  showSearch?: boolean;
  /**
   * 搜索过滤逻辑。
   * - true（默认）：内置 contains 模糊匹配
   * - false：不过滤（用于远程搜索场景）
   * - 函数：自定义过滤逻辑
   * 【差异】lingyang 的函数参数 option 为 ReactElement；Ant Design 为 OptionType 对象
   */
  filterOption?: boolean | ((inputValue: string, option: React.ReactElement) => boolean);
  /** 是否显示加载状态。默认 false */
  loading?: boolean;
  /** 是否为错误状态（红色边框）。默认 false */
  error?: boolean;
  /**
   * 选择器尺寸。默认 'default'。
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
   * 选中值变化回调。
   * 第二参数为选中的选项对象（多选时为数组）
   */
  onChange?: (value: SelectValue | SelectValue[], option: SelectOption | SelectOption[]) => void;
  /** 搜索值变化回调（用于动态更新 options） */
  onSearch?: (inputValue: string) => void;
  /** 选中某个选项时的回调 */
  onSelect?: (value: SelectValue, option: SelectOption) => void;
  /** 取消选中某个选项时的回调（仅多选模式） */
  onDeselect?: (value: SelectValue, option: SelectOption) => void;
  /** 点击清除按钮时的回调 */
  onClear?: () => void;
  /** 聚焦回调 */
  onFocus?: (e: FocusEvent) => void;
  /** 失焦回调 */
  onBlur?: (e: FocusEvent) => void;
  /**
   * 多选时最多展示的标签数量，超出显示 +N。
   * 【差异】lingyang 仅支持 number；Ant Design 还支持 'responsive'
   */
  maxTagCount?: number;
  /** 多选标签文字的最大显示长度（超出截断加省略号） */
  maxTagTextLength?: number;
  /** 自定义多选标签的渲染函数 */
  renderTag?: (props: TagProps, index: number, values: SelectOption[]) => ReactNode;
  /** 在 tags 模式下，按指定分隔符自动分割粘贴文本 */
  tokenSeparators?: string[];
  /**
   * 无匹配选项时的自定义空状态。
   * 【命名差异】lingyang 用 noDataElement，Ant Design 用 notFoundContent
   */
  noDataElement?: ReactNode;
  /**
   * 【lingyang 专有】自定义触发元素（替换默认输入框）。
   * Ant Design 无直接等价
   */
  triggerElement?: ReactNode;
  /** 自定义下拉菜单内容（可在菜单前/后追加内容） */
  dropdownRender?: (menu: ReactNode) => ReactNode;
  /** 下拉菜单的自定义样式 */
  dropdownMenuStyle?: CSSProperties;
  /** 下拉菜单的自定义 className */
  dropdownMenuClassName?: string;
  /**
   * 指定下拉弹层挂载的容器节点。
   * 【差异】lingyang 无参数；Ant Design 传入 triggerNode: HTMLElement
   */
  getPopupContainer?: () => HTMLElement;
  /**
   * 虚拟滚动配置（大数据量时开启以提升性能）。
   * 【差异】lingyang 用配置对象；Ant Design 用 virtual: boolean
   */
  virtualListProps?: {
    height?: number;
    itemHeight?: number;
    threshold?: number;
  };
  /** 弹层关闭后是否卸载 DOM。默认 true */
  unmountOnExit?: boolean;
  /** 是否在下拉菜单顶部显示搜索框（多选时将搜索框移入弹层） */
  showHeader?: boolean;
  /** 选择框左侧前缀 */
  prefix?: ReactNode;
  /** 自定义后缀图标（替换默认箭头区域） */
  suffixIcon?: ReactNode;
  /** 自定义箭头图标 */
  arrowIcon?: ReactNode;
  /** 多选标签的自定义删除图标 */
  removeIcon?: ReactNode;
  /** 受控：搜索输入框的值 */
  inputValue?: string;
  className?: string;
  style?: CSSProperties;
  children?: ReactNode;
}
```

## SelectOption 对象格式

```typescript
interface SelectOption {
  /** 选项值（必填） */
  value: string | number | boolean;
  /** 展示标签（支持 ReactNode，默认与 value 相同） */
  label?: ReactNode;
  /** 是否禁用该选项 */
  disabled?: boolean;
  /** 自定义附加数据，可在 onChange 等回调的 option 参数中获取 */
  extra?: any;
}
```

## Select.OptGroup Props

```typescript
interface OptGroupProps {
  /** 分组标题（必填，支持 ReactNode） */
  label: ReactNode;
  children?: ReactNode;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| 受控显示属性 | `popupVisible` | `open` |
| 非受控初始显示 | `defaultPopupVisible` | `defaultOpen` |
| 显隐回调 | `onVisibleChange` | `onDropdownVisibleChange` |
| 空状态属性 | `noDataElement` | `notFoundContent` |
| 尺寸枚举 | mini / small / default / large | small / middle / large |
| getPopupContainer | `() => HTMLElement`（无参数） | `(triggerNode) => HTMLElement` |
| 虚拟滚动 | `virtualListProps: { height, itemHeight, threshold }` | `virtual: boolean` |
| 允许创建新选项 | `allowCreate` | ❌ 无直接等价 |
| 自定义触发元素 | `triggerElement` | ❌ 无直接等价 |
| filterOption option 参数 | `ReactElement` | `OptionType 对象` |
| maxTagCount 类型 | `number` 仅此 | `number \| 'responsive'` |

---
