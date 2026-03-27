# 羚羊 Button 组件 Skill

**Figma**: https://www.figma.com/design/YDAvxSboqxxSbzQsa15q4X/?node-id=8253-44145

> 本 skill 与 `lyspec-ued` skill 配合使用。生成 Button 相关 UI 时，同时遵守设计系统的颜色、间距、圆角 Token 约束。

---

## Props 速查

| Prop | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `type` | `'default' \| 'primary' \| 'secondary' \| 'dashed' \| 'text' \| 'outline'` | `'default'` | 按钮视觉风格 |
| `size` | `'mini' \| 'small' \| 'default' \| 'large'` | `'default'` | 按钮尺寸 |
| `status` | `'warning' \| 'danger' \| 'error' \| 'success'` | — | 语义状态颜色 |
| `shape` | `'circle' \| 'round' \| 'square'` | — | 按钮形状 |
| `disabled` | `boolean` | `false` | 禁用状态 |
| `loading` | `boolean` | `false` | 加载中状态（自动禁用） |
| `long` | `boolean` | `false` | 撑满父容器宽度（100%） |
| `iconOnly` | `boolean` | `false` | 纯图标按钮（宽高相等） |
| `icon` | `ReactNode` | — | 按钮左侧图标 |
| `href` | `string (uri)` | — | 设置后渲染为 `<a>` 标签 |
| `target` | `string` | — | `<a>` 的 target，仅 href 时有效 |
| `htmlType` | `'button' \| 'submit' \| 'reset'` | `'button'` | 原生 button type |
| `anchorProps` | `HTMLProps<HTMLAnchorElement>` | — | href 模式下额外 a 标签属性 |
| `className` | `string` | — | 自定义 CSS 类名 |
| `style` | `CSSProperties` | — | 自定义内联样式 |
| `onClick` | `(e: MouseEvent) => void` | — | 点击回调（禁用/加载时不触发） |

---

## 选型决策树

### 1. 选择 `type`（视觉层级）

```
页面最核心操作（提交、确认、创建）      → type="primary"
次要操作（取消、返回）                  → type="secondary"
弱操作、不干扰阅读的辅助操作            → type="text"
需要边框但不填充背景                    → type="outline"
虚线风格（上传区、添加区占位）          → type="dashed"
```

### 2. 选择 `status`（语义色）

```
删除、不可恢复操作                      → status="danger"
警告提示性操作                          → status="warning"
表示完成/完成态按钮                     → status="success"
无语义特殊含义                          → 不传 status
```

### 3. 选择 `size`

```
表格行内操作、紧凑列表                  → size="mini" 或 size="small"
普通表单、弹窗操作                      → size="default"
页面级主 CTA、移动端底部按钮            → size="large"
```

### 4. 选择 `shape`

```
纯图标按钮（无文字）                    → shape="circle" + iconOnly
大圆角胶囊风格                          → shape="round"
无圆角直角                              → shape="square"
默认中等圆角                            → 不传 shape
```

---

## 代码示例

```jsx
// 主按钮（最常用）
<Button type="primary">立即提交</Button>

// 危险操作
<Button type="primary" status="danger">删除</Button>

// 加载状态（防重复提交）
<Button type="primary" loading>提交中...</Button>

// 带左侧图标
<Button type="primary" icon={<IconPlus />}>新建</Button>

// 纯图标圆形按钮（必须加 aria-label）
<Button shape="circle" icon={<IconSearch />} iconOnly aria-label="搜索" />

// 链接按钮（渲染为 <a> 标签）
<Button type="text" href="https://lingyang.design" target="_blank">查看文档</Button>

// 禁用状态
<Button type="primary" disabled>不可操作</Button>

// 全宽按钮（移动端底部 CTA）
<Button type="primary" long>登 录</Button>

// 小尺寸次要按钮
<Button type="secondary" size="small">取消</Button>

// 表单提交按钮
<Button type="primary" htmlType="submit">提交表单</Button>

// 按钮组（消除间距、合并边框）
import { Button } from 'lingyang';
const { Group } = Button;
<Group>
  <Button>左</Button>
  <Button>中</Button>
  <Button>右</Button>
</Group>
```

---

## Figma → Code 变体映射

| Figma 变体维度 | Figma 值 | 对应 Prop |
|---|---|---|
| Type | Primary / Secondary / Dashed / Text / Outline | `type` |
| Size | Mini / Small / Default / Large | `size` |
| Status | Default / Warning / Danger / Success | `status` |
| State | Disabled | `disabled={true}` |
| State | Loading | `loading={true}` |
| Shape | Circle / Round / Square | `shape` |
| Has Icon | Icon Left | `icon={<IconXxx />}` |
| Has Icon | Icon Only | `icon={<IconXxx />} iconOnly` |

---

## 无障碍访问注意事项

- `iconOnly` 按钮**必须**提供 `aria-label` 或 `title`，否则屏幕阅读器无法识别
- `disabled` 状态自动添加 `aria-disabled="true"`，无需手动设置
- `loading` 状态建议补充 `aria-label="提交中，请稍候"` 描述当前状态
- 键盘触发：`Enter` 和 `Space` 均可触发点击

---

## 与设计系统 Token 的对应关系

| 场景 | 按钮配置 | 设计 Token |
|---|---|---|
| 主 CTA 背景色 | `type="primary"` | `brand-primary-1 (#13AE68)` |
| 主 CTA hover | — | `brand-primary-2 (#42BE86)` |
| 主 CTA active | — | `brand-primary-3 (#0F8B53)` |
| 危险按钮背景 | `status="danger"` | `status-danger (#F53F3F)` |
| 警告按钮背景 | `status="warning"` | `status-warning (#FF7D00)` |
| 成功按钮背景 | `status="success"` | `status-success (#00B42A)` |
| 禁用背景色 | `disabled` | `bg-fill-5 (#C9CDD4)` |
| 禁用文字色 | `disabled` | `text-disabled (rgba(0,0,0,0.25))` |
| 默认按钮圆角 | 默认 | `radius-3 (8px)` |
| 默认字号 | `size="default/large"` | `font-size-body (14px)` |
| 小尺寸字号 | `size="small/mini"` | `font-size-small (12px)` |

---

## 常见错误与纠正

| ❌ 错误用法 | ✅ 正确用法 | 原因 |
|---|---|---|
| `<Button type="danger">` | `<Button status="danger">` | `type` 控制样式，`status` 控制语义色 |
| `<Button shape="circle">` 无 `iconOnly` | `<Button shape="circle" iconOnly icon={<Icon />}>` | circle 形状应配合 iconOnly 使用 |
| iconOnly 按钮无 aria-label | `<Button ... aria-label="操作名称" />` | 无障碍访问要求 |
| loading 时仍绑定 onClick 期望触发 | 改用状态管理控制 loading 状态 | loading 时自动禁用，onClick 不触发 |
| 随意使用 style 覆盖颜色 | 使用 `status` prop 或设计 Token | 保持视觉一致性 |

---
