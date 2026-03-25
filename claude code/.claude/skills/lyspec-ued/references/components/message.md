# lingyang-message · 全局提示速查手册

**类型**: 命令式 API（不是 JSX 组件，直接调用静态方法）

---

## ⚡ 速查：5 种调用方式

```jsx
Message.info('普通提示')
Message.success('操作成功')
Message.warning('请注意')
Message.error('操作失败')
Message.loading('正在处理...', { duration: 0 })  // duration:0 永不关闭
```

---

## ⚠️ 与 Ant Design 的 4 大差异（高频踩坑）

| 特性 | lingyang | Ant Design |
|---|---|---|
| **duration 单位** | **毫秒（ms）**，默认 `3000` | 秒（s），默认 `3` |
| **唯一标识参数名** | `id` | `key` |
| **弹出位置** | `position: 'top' \| 'bottom'` ✅ | 仅顶部，无此参数 ❌ |
| **Hook 名** | `Message.useMessage()` | `message.useMessage()` |

---

## MessageConfig 参数全表

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `content` | `ReactNode` | — | **必填**，消息内容 |
| `id` | `string` | — | 唯一 ID，同 id 会更新已有消息（勿写 `key`） |
| `duration` | `number` | `3000` | 显示时长（**毫秒 ms**），`0` 不自动关闭 |
| `icon` | `ReactNode` | — | 自定义图标，传入后 showIcon 失效 |
| `showIcon` | `boolean` | `true` | 是否显示类型图标 |
| `closable` | `boolean` | `false` | 是否显示关闭按钮 |
| `onClose` | `() => void` | — | 关闭回调（超时/手动均触发） |
| `position` | `'top' \| 'bottom'` | `'top'` | 弹出位置（lingyang 专有） |
| `transitionTimeout` | `number \| { enter?: number; exit?: number }` | `{ enter: 100, exit: 300 }` | 动画时长 ms（lingyang 专有） |
| `getContainer` | `() => HTMLElement` | `document.body` | 自定义挂载容器 |
| `prefixCls` | `string` | `'lingyang'` | CSS 类名前缀 |
| `style` | `CSSProperties` | — | 自定义样式 |
| `className` | `string` | — | 自定义类名 |

---

## Message.config() 全局配置

```jsx
// 建议在 App 入口调用一次
Message.config({
  maxCount: 3,        // 最多同时显示 3 条
  duration: 3000,     // 全局默认时长（ms）
  position: 'top',    // 全局位置
  getContainer: () => document.getElementById('app'),
});
```

---

## 静态方法签名

```typescript
Message.info(config)     → { close: () => void }
Message.success(config)  → { close: () => void }
Message.warning(config)  → { close: () => void }
Message.error(config)    → { close: () => void }
Message.loading(config)  → { close: () => void }
Message.clear()          → void
Message.config(global)   → void
Message.useMessage()     → [messageApi, contextHolder]
```

---

## CSS 类名速查

```
.lingyang-message            // 消息容器（top 位置）
.lingyang-message-bottom     // 消息容器（bottom 位置）
.lingyang-message-content    // 消息内容区
.lingyang-message-icon       // 图标
.lingyang-message-close-btn  // 关闭按钮
.lingyang-message-info       // info 状态
.lingyang-message-success    // success 状态
.lingyang-message-warning    // warning 状态
.lingyang-message-error      // error 状态
.lingyang-message-loading    // loading 状态
```

---

## 高频场景快速代码

详见 `references/examples.md`，完整类型定义见 `references/props.md`。
-e 

---

## 完整代码示例

# lingyang-message · 完整代码示例库

## 目录
1. [基础调用（5 种类型）](#1-基础调用)
2. [带完整配置的消息](#2-带完整配置)
3. [loading → success 状态转换（最常用）](#3-loading--success-状态转换)
4. [手动关闭与持久消息](#4-手动关闭与持久消息)
5. [底部弹出（position=bottom）](#5-底部弹出)
6. [useMessage Hook（需要 context）](#6-usemessage-hook)
7. [全局配置（限制数量 + 位置）](#7-全局配置)
8. [在 Form 提交中使用](#8-在-form-提交中使用)

---

## 1. 基础调用

```jsx
import { Message, Button, Space } from 'lingyang';

// 最简单的调用方式：直接传字符串
function BasicDemo() {
  return (
    <Space>
      <Button onClick={() => Message.info('这是一条普通提示')}>Info</Button>
      <Button onClick={() => Message.success('操作成功！')}>Success</Button>
      <Button onClick={() => Message.warning('请注意这个问题')}>Warning</Button>
      <Button onClick={() => Message.error('操作失败，请重试')}>Error</Button>
      <Button onClick={() => Message.loading('正在处理...')}>Loading</Button>
    </Space>
  );
}
```

---

## 2. 带完整配置

```jsx
import { Message, Button } from 'lingyang';
import { IconStar } from 'lingyang/icon';

// 配置对象方式（推荐用于复杂场景）
function ConfigDemo() {
  const showCustomMessage = () => {
    Message.success({
      content: (
        <span>
          文件 <strong>report.pdf</strong> 已上传成功
        </span>
      ),
      duration: 5000,          // 5 秒后关闭（注意单位是 ms！）
      closable: true,          // 显示关闭按钮
      onClose: () => console.log('消息已关闭'),
    });
  };

  const showCustomIconMessage = () => {
    Message.info({
      content: '自定义图标消息',
      icon: <IconStar style={{ color: '#FFB400' }} />,
      duration: 4000,
    });
  };

  return (
    <Space>
      <Button onClick={showCustomMessage}>带关闭按钮</Button>
      <Button onClick={showCustomIconMessage}>自定义图标</Button>
    </Space>
  );
}
```

---

## 3. loading → success 状态转换

```jsx
import { Message, Button } from 'lingyang';

// 核心技巧：使用相同的 id，后续调用会更新同一条消息
// 【命名差异】lingyang 用 id；Ant Design 用 key

function LoadingToSuccessDemo() {
  const handleSave = async () => {
    // 1. 显示 loading（duration:0 永不自动关闭）
    Message.loading({
      id: 'save-action',
      content: '正在保存...',
      duration: 0,
    });

    try {
      await saveApi();  // 模拟异步请求

      // 2a. 成功：用相同 id 更新为 success
      Message.success({
        id: 'save-action',
        content: '保存成功！',
        duration: 3000,
      });
    } catch (e) {
      // 2b. 失败：用相同 id 更新为 error
      Message.error({
        id: 'save-action',
        content: '保存失败，请重试',
        duration: 4000,
        closable: true,
      });
    }
  };

  return <Button type="primary" onClick={handleSave}>保存</Button>;
}

// 也可以使用返回的 close 函数手动关闭
function ManualClose() {
  const handleUpload = async () => {
    const { close } = Message.loading({
      content: '上传中...',
      duration: 0,
    });

    await uploadFile();
    close();  // 上传完成后关闭 loading
    Message.success('上传完成');
  };

  return <Button onClick={handleUpload}>上传文件</Button>;
}
```

---

## 4. 手动关闭与持久消息

```jsx
import { Message, Button, Space } from 'lingyang';
import { useRef } from 'react';

function PersistentMessage() {
  const closeRef = useRef<(() => void) | null>(null);

  const showPersistentMsg = () => {
    // 显示持久消息（duration:0 + closable:true）
    const { close } = Message.info({
      content: '这条消息不会自动消失，点击关闭按钮或按钮手动关闭',
      duration: 0,
      closable: true,
    });
    closeRef.current = close;
  };

  const closeManually = () => {
    closeRef.current?.();
  };

  const clearAll = () => {
    Message.clear();  // 关闭所有消息
  };

  return (
    <Space>
      <Button onClick={showPersistentMsg}>显示持久消息</Button>
      <Button onClick={closeManually}>关闭持久消息</Button>
      <Button onClick={clearAll}>关闭全部消息</Button>
    </Space>
  );
}
```

---

## 5. 底部弹出

```jsx
import { Message, Button, Space } from 'lingyang';

// lingyang 专有：position='bottom'，Ant Design 不支持此功能
function BottomPositionDemo() {
  const showBottom = (type: 'info' | 'success' | 'error') => {
    Message[type]({
      content: `底部弹出的 ${type} 提示`,
      position: 'bottom',    // lingyang 专有，Ant Design 无此参数
      duration: 3000,
    });
  };

  return (
    <Space>
      <Button onClick={() => showBottom('info')}>底部 Info</Button>
      <Button onClick={() => showBottom('success')}>底部 Success</Button>
      <Button onClick={() => showBottom('error')}>底部 Error</Button>
    </Space>
  );
}
```

---

## 6. useMessage Hook

```jsx
import { Message, Button, ConfigProvider } from 'lingyang';

// 何时使用 useMessage：
// 1. 需要读取 ConfigProvider 的主题、语言等配置
// 2. 在 React 函数组件内部，需要与当前 context 联动

// 【命名差异】lingyang 是 Message.useMessage()（大写 M）
//             Ant Design 是 message.useMessage()（小写 m）

function UseMessageDemo() {
  const [messageApi, contextHolder] = Message.useMessage();  // 大写 M

  const showContextMessage = () => {
    messageApi.success({
      content: '这条消息能读取 ConfigProvider 的主题配置',
      duration: 3000,
    });
  };

  return (
    <div>
      {/* contextHolder 必须渲染在需要获取 context 的节点内 */}
      {contextHolder}
      <Button type="primary" onClick={showContextMessage}>
        显示消息（能读取 Context）
      </Button>
    </div>
  );
}

// 在 App 根组件使用（推荐模式）
function App() {
  const [messageApi, contextHolder] = Message.useMessage();

  return (
    <ConfigProvider
      theme={{
        token: { colorPrimary: '#13AE68' },
      }}
    >
      {contextHolder}
      {/* 子组件可通过 messageApi 触发消息，自动应用 ConfigProvider 主题 */}
      <UseMessageDemo />
    </ConfigProvider>
  );
}
```

---

## 7. 全局配置

```jsx
import { Message } from 'lingyang';

// 建议在应用入口（index.tsx 或 App.tsx）调用一次
Message.config({
  maxCount: 5,        // 同时最多显示 5 条消息，超出关闭最早的
  duration: 3000,     // 全局默认时长（ms）
  position: 'top',    // 全局位置（'top' 或 'bottom'）
});

// 也可以按需覆盖全局配置
function setBottomConfig() {
  Message.config({
    position: 'bottom',
    maxCount: 3,
  });
}

// 单条消息的配置优先级高于全局配置
Message.success({
  content: '这条消息使用全局配置的时长',
  // 未设置 duration，使用全局 3000ms
});

Message.error({
  content: '这条消息覆盖了全局时长',
  duration: 8000,     // 覆盖全局 duration
});
```

---

## 8. 在 Form 提交中使用

```jsx
import { Form, Input, Button, Message } from 'lingyang';

// Form 表单提交后的标准消息反馈模式
function SubmitForm() {
  const [form] = Form.useForm();

  const handleSubmit = async () => {
    try {
      // 1. 表单验证
      const values = await form.validate();

      // 2. 显示 loading
      Message.loading({
        id: 'form-submit',
        content: '正在提交...',
        duration: 0,
      });

      // 3. 提交请求
      await submitApi(values);

      // 4. 成功反馈（更新同一条消息）
      Message.success({
        id: 'form-submit',
        content: '提交成功！',
        duration: 3000,
      });

      form.resetFields();
    } catch (error) {
      if (error?.errors) {
        // 表单验证失败（lingyang 返回 { errors: [], values: {} }）
        Message.warning('请检查表单填写是否完整');
      } else {
        // 接口请求失败
        Message.error({
          id: 'form-submit',
          content: `提交失败：${error?.message || '请稍后重试'}`,
          duration: 5000,
          closable: true,
        });
      }
    }
  };

  return (
    <Form form={form} style={{ maxWidth: 400 }}>
      <Form.Item
        field="name"
        label="姓名"
        rules={[{ required: true, message: '请输入姓名' }]}
      >
        <Input placeholder="请输入姓名" />
      </Form.Item>
      <Form.Item
        field="email"
        label="邮箱"
        rules={[
          { required: true, message: '请输入邮箱' },
          { type: 'email', message: '邮箱格式不正确' },
        ]}
      >
        <Input placeholder="请输入邮箱" />
      </Form.Item>
      <Form.Item>
        <Button type="primary" onClick={handleSubmit} long>
          提交
        </Button>
      </Form.Item>
    </Form>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang-message · 完整 Props 类型定义

## 目录
- [MessageConfig（单条消息配置）](#messageconfig)
- [MessageGlobalConfig（全局配置）](#messageglobalconfig)
- [静态方法完整签名](#静态方法完整签名)
- [与 Ant Design 差异详细对照](#与-ant-design-差异详细对照)

---

## MessageConfig

```typescript
interface MessageConfig {
  /**
   * 消息内容（必填）。
   * 支持字符串和任意 ReactNode（如 <span>带<strong>格式</strong>的内容</span>）
   */
  content: ReactNode;

  /**
   * 消息唯一 ID。
   * 传入相同 id 时，新消息会更新已有消息的内容和计时器，而非新建一条。
   * 常用于：Message.loading({ id: 'save', content: '保存中...' })
   *         Message.success({ id: 'save', content: '保存成功' })
   *
   * 【命名差异】lingyang 用 id；Ant Design 用 key
   */
  id?: string;

  /**
   * 自定义图标。传入后 showIcon 自动失效。
   * 示例：icon={<IconCustom />}
   */
  icon?: ReactNode;

  /**
   * 是否显示类型图标（info/success/warning/error/loading 各有专属默认图标）
   * @default true
   */
  showIcon?: boolean;

  /**
   * 消息显示时长，单位：毫秒（ms）。
   * 设为 0 则永不自动关闭（需配合 closable=true 或调用 close() 方法）。
   * @default 3000
   *
   * 【单位差异】lingyang 为毫秒（ms）；Ant Design 为秒（s）
   * 同样的 3 秒：lingyang 写 3000，Ant Design 写 3
   */
  duration?: number;

  /**
   * 是否显示手动关闭按钮（右上角 ×）。
   * loading 类型通常设为 true，或设 duration=0 后在回调中手动关闭。
   * @default false
   */
  closable?: boolean;

  /**
   * 消息关闭时的回调函数。
   * 无论是自动超时关闭还是用户手动点击关闭，均会触发。
   */
  onClose?: () => void;

  /**
   * 消息弹出位置。
   * 【lingyang 专有属性】Ant Design 无此参数，只支持顶部弹出。
   * @default 'top'
   */
  position?: 'top' | 'bottom';

  /**
   * 出入场动画持续时长（ms）。
   * - 传 number：enter 和 exit 使用同一时长
   * - 传对象：分别配置 enter（进场）和 exit（出场）时长
   * 【lingyang 专有属性】Ant Design 无此参数。
   * @default { enter: 100, exit: 300 }
   */
  transitionTimeout?: number | {
    enter?: number;
    exit?: number;
  };

  /**
   * 自定义消息挂载容器。
   * 默认挂载到 document.body。
   * 在 Modal、Drawer 等局部区域内显示消息时，传入对应容器元素。
   * @default () => document.body
   */
  getContainer?: () => HTMLElement;

  /**
   * 自定义 CSS 类名前缀（替换默认的 lingyang）。
   * 替换后所有类名跟随变化：如 my-message-content、my-message-icon 等。
   */
  prefixCls?: string;

  /** 消息内容区域的自定义内联样式 */
  style?: React.CSSProperties;

  /** 消息内容区域的自定义类名 */
  className?: string;
}
```

---

## MessageGlobalConfig

```typescript
interface MessageGlobalConfig {
  /**
   * 同时最多显示的消息数量。
   * 超出时自动关闭最早出现的消息。
   * 常用于防止操作频繁导致消息堆叠。
   */
  maxCount?: number;

  /**
   * 全局默认显示时长（ms）。
   * 单条消息配置的 duration 会覆盖此全局值。
   * @default 3000
   */
  duration?: number;

  /**
   * 全局 CSS 类名前缀。
   * 影响所有消息的类名（不包括已显示的消息）。
   */
  prefixCls?: string;

  /**
   * 全局消息挂载容器。
   * 单条消息的 getContainer 会覆盖此全局值。
   */
  getContainer?: () => HTMLElement;

  /**
   * 全局默认弹出位置。
   * 单条消息的 position 会覆盖此全局值。
   * @default 'top'
   */
  position?: 'top' | 'bottom';
}
```

---

## 静态方法完整签名

```typescript
// 5 种类型方法
// config 可传 MessageConfig 对象，或直接传 ReactNode（字符串最常用）
Message.info    (config: MessageConfig | ReactNode): { close: () => void }
Message.success (config: MessageConfig | ReactNode): { close: () => void }
Message.warning (config: MessageConfig | ReactNode): { close: () => void }
Message.error   (config: MessageConfig | ReactNode): { close: () => void }
Message.loading (config: MessageConfig | ReactNode): { close: () => void }

// 关闭所有消息
Message.clear(): void

// 全局配置（在 App 入口调用一次）
Message.config(config: MessageGlobalConfig): void

// Hook 方式（需要访问 React context 时使用）
Message.useMessage(): [MessageInstance, React.ReactElement]

// MessageInstance（useMessage 返回的 API 对象）
interface MessageInstance {
  info    (config: MessageConfig | ReactNode): { close: () => void }
  success (config: MessageConfig | ReactNode): { close: () => void }
  warning (config: MessageConfig | ReactNode): { close: () => void }
  error   (config: MessageConfig | ReactNode): { close: () => void }
  loading (config: MessageConfig | ReactNode): { close: () => void }
  clear   (): void
}
```

---

## 与 Ant Design 差异详细对照

| 特性 | lingyang 写法 | Ant Design 写法 | 备注 |
|---|---|---|---|
| duration 单位 | `duration: 3000`（ms） | `duration: 3`（s） | ⚠️ 最容易踩坑 |
| 唯一标识参数 | `id: 'my-msg'` | `key: 'my-msg'` | — |
| 弹出位置 | `position: 'bottom'` ✅ | ❌ 不支持 | lingyang 专有 |
| 动画时长 | `transitionTimeout: 300` ✅ | ❌ 不支持 | lingyang 专有 |
| Hook 调用 | `Message.useMessage()` | `message.useMessage()` | 大小写不同 |
| loading 默认时长 | `duration: 0`（不自动关闭） | `duration: 0`（不自动关闭） | 行为相同 |
| 关闭返回值 | `const { close } = Message.success(...)` | `Message.success(...).then(...)` | 接口形式不同 |
| 全局配置方法 | `Message.config({...})` | `message.config({...})` | 大小写不同 |

---
