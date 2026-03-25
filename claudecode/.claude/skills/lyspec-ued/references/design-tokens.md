# 设计 Token 与 CSS 变量规范

> 本文件从 SKILL.md 拆分，Phase 3 生成 styles.css 和 HTML 页面时加载。
> 生成所有 UI 代码时，颜色/字体/间距/圆角/阴影必须严格使用以下值，禁止使用规范外的任意值。

## 品牌主色

| Token | 值 | 用途 |
|---|---|---|
| `brand-primary-1` | `#13AE68` | 主品牌色，CTA 按钮、主要强调 |
| `brand-primary-2` | `#42BE86` | hover 状态 |
| `brand-primary-3` | `#0F8B53` | active/pressed 状态 |
| `brand-primary-4` | `#A1DFC3` | 标签背景、浅强调 |
| `brand-primary-5` | `#E7F6EF` | 页面背景强调区域 |

## 功能色/状态色

| Token | 值 | 用途 |
|---|---|---|
| `color-primary` | `#165DFF` | 链接、激活态、功能性主色 |
| `status-success` | `#00B42A` | 成功、完成 |
| `status-warning` | `#FF7D00` | 警告、注意 |
| `status-danger` | `#F53F3F` | 错误、危险、删除 |
| `status-info` | `#165DFF` | 信息、提示 |

> **Token 层次说明**：
> - `brand-primary-*` 是品牌色，用于品牌强调元素（Logo区域、CTA按钮、品牌标识）
> - `color-primary` 是功能色，用于交互元素（链接、激活态、Focus边框）

## 文字色

| Token | 值 | 用途 |
|---|---|---|
| `color-text-1` | `#1D2129` | 强调/正文标题 |
| `color-text-2` | `#4E5969` | 次强调/正文标题 |
| `color-text-3` | `#86909C` | 次要信息、Label |
| `color-text-4` | `#C9CDD4` | 置灰信息、禁用文字 |
| `color-text-5` | `#FFFFFF` | 纯白文字（深色背景上） |

## 背景填充

| Token | 值 | 用途 |
|---|---|---|
| `bg-fill-1` | `#FFFFFF` | 页面/卡片主背景 |
| `bg-fill-2` | `#F7F8FA` | 页面底色、表头、列表行间隔 |
| `bg-fill-3` | `#F2F3F5` | 输入框背景、侧边栏激活、次级区块 |
| `bg-fill-4` | `#E5E6EB` | 分割线、骨架屏 |
| `bg-fill-5` | `#C9CDD4` | 禁用背景 |
| `bg-fill-6` | `#4E5969` | 深色区块背景 |

## 边框

| Token | 值 | 用途 |
|---|---|---|
| `border-1` | `#F2F3F5` | 最浅边框、轻分隔线 |
| `border-2` | `#E5E6EB` | 常规边框 |
| `border-3` | `#C9CDD4` | 中等强调边框、输入框默认 |
| `border-4` | `#86909C` | 深色边框 |
| `border-focus` | `#165DFF` | 聚焦边框（= color-primary） |

## 图表 / Icon 辅助色

仅用于数据可视化、图表系列色、图标配色，**不用于交互元素**。

| Token | 值 | 色相 |
|---|---|---|
| `chart-color-1` | `#FE5B5A` | 红 |
| `chart-color-2` | `#1EDEF0` | 青 |
| `chart-color-3` | `#FFC933` | 黄 |
| `chart-color-4` | `#43CC8B` | 绿 |
| `chart-color-5` | `#3491FA` | 蓝 |
| `chart-color-6` | `#D91AD9` | 紫红 |
| `chart-color-7` | `#6961FF` | 紫 |
| `chart-color-8` | `#FF992F` | 橙 |

## 字体

**字体族**: `PingFang SC, "Microsoft YaHei", sans-serif`

| Token | 值 (px) | 用途 |
|---|---|---|
| `font-size-h1` | `28` | 页面主标题 |
| `font-size-h2` | `24` | 区块标题 |
| `font-size-h3` | `20` | 卡片标题 |
| `font-size-h4` | `18` | 小节标题 |
| `font-size-h5` | `16` | 强调正文 |
| `font-size-h6` | `14` | 辅助标题 |
| `font-size-h7` | `12` | 小标题/标签/Label |
| `font-size-body` | `14` | 正文 |
| `font-size-small` | `12` | 说明文字、辅助信息 |

字重: `400` 正文 / `500` 强调 / `600` 标题
行高: `1.2` 标题 / `1.5` 正文默认 / `1.8` 长文阅读

## 间距

所有 padding / margin / gap 只能取以下值（px）：

`4` / `8` / `12` / `16` / `20` / `24` / `32` / `40` / `48`

| 场景 | 推荐值 |
|---|---|
| 卡片内边距 | `16` 或 `24` |
| 列表行间距 | `8` 或 `12` |
| 页面区块间距 | `32` 或 `40` |
| 小组件内间距 | `4` 或 `8` |

## 圆角

| Token | 值 (px) | 用途 |
|---|---|---|
| `radius-1` | `0` | 无圆角 |
| `radius-2` | `4` | 小组件（标签、输入框） |
| `radius-3` | `8` | 卡片、按钮默认 |
| `radius-4` | `16` | 大卡片、Modal |
| `radius-5` | `24` | 大型胶囊按钮 |
| `radius-6` | `9999` | 完全圆形（头像、徽标） |

## 阴影

| Token | 值 | 用途 |
|---|---|---|
| `shadow-special` | `0px 0px 0px rgba(0,0,0,0.3)` | 无阴影/重置 |
| `shadow1-center` | `0px 2px 5px rgba(0,0,0,0.1)` | 卡片默认轻阴影 |
| `shadow2-center` | `0px 0px 10px rgba(0,0,0,0.1)` | 浮层、下拉菜单 |
| `shadow3-center` | `0px 8px 20px rgba(0,0,0,0.1)` | Modal、Drawer、强浮层 |

## CSS 变量命名规范（强制）

> **这是最高优先级的约束规则，违反将导致 HTML Demo 样式全面失效。**

- CSS 变量名**必须**与下方「CSS 变量模板」中的名称**完全一致**，一个字符都不能改
- **禁止**添加任何前缀（如 `ly-`、`lingyang-`）或修改命名格式
- `styles.css` 和所有 HTML 页面**必须**使用相同的变量名
- 示例：Token 表格中 `brand-primary-1` → CSS 变量 `--brand-primary-1` → HTML 引用 `var(--brand-primary-1)`
- **委托给子 agent 时，必须在 prompt 中明确引用下方完整的 CSS 变量模板**

## CSS 变量模板

```css
:root {
  /* 品牌色 */
  --brand-primary-1: #13AE68; --brand-primary-2: #42BE86;
  --brand-primary-3: #0F8B53; --brand-primary-4: #A1DFC3; --brand-primary-5: #E7F6EF;
  /* 功能色 */
  --color-primary: #165DFF;
  --status-success: #00B42A; --status-warning: #FF7D00;
  --status-danger: #F53F3F; --status-info: #165DFF;
  /* 文字色 */
  --color-text-1: #1D2129; --color-text-2: #4E5969;
  --color-text-3: #86909C; --color-text-4: #C9CDD4; --color-text-5: #FFFFFF;
  /* 背景 */
  --bg-fill-1: #FFFFFF; --bg-fill-2: #F7F8FA; --bg-fill-3: #F2F3F5;
  --bg-fill-4: #E5E6EB; --bg-fill-5: #C9CDD4; --bg-fill-6: #4E5969;
  /* 边框 */
  --border-1: #F2F3F5; --border-2: #E5E6EB; --border-3: #C9CDD4;
  --border-4: #86909C; --border-focus: #165DFF;
  /* 图表色 */
  --chart-color-1: #FE5B5A; --chart-color-2: #1EDEF0; --chart-color-3: #FFC933;
  --chart-color-4: #43CC8B; --chart-color-5: #3491FA; --chart-color-6: #D91AD9;
  --chart-color-7: #6961FF; --chart-color-8: #FF992F;
  /* 字体 */
  --font-family: PingFang SC, "Microsoft YaHei", sans-serif;
  --font-size-h1: 28px; --font-size-h2: 24px; --font-size-h3: 20px;
  --font-size-h4: 18px; --font-size-h5: 16px; --font-size-h6: 14px;
  --font-size-h7: 12px; --font-size-body: 14px; --font-size-small: 12px;
  /* 间距 */
  --spacing-4: 4px; --spacing-8: 8px; --spacing-12: 12px; --spacing-16: 16px;
  --spacing-20: 20px; --spacing-24: 24px; --spacing-32: 32px;
  --spacing-40: 40px; --spacing-48: 48px;
  /* 圆角 */
  --radius-1: 0px; --radius-2: 4px; --radius-3: 8px;
  --radius-4: 16px; --radius-5: 24px; --radius-6: 9999px;
  /* 阴影 */
  --shadow-special: 0px 0px 0px rgba(0,0,0,0.3);
  --shadow1-center: 0px 2px 5px rgba(0,0,0,0.1);
  --shadow2-center: 0px 0px 10px rgba(0,0,0,0.1);
  --shadow3-center: 0px 8px 20px rgba(0,0,0,0.1);
}
```
