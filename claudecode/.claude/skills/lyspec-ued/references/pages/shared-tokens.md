# lingyang Page DSL — 共用设计 Token & 组件规格

## 全局布局

```
画布宽度:        1440px
页面背景色:       #F7F8FA
侧边栏:          x=8, w=204, bg=white, rx=4(radius-2), shadow=0 2px 5px rgba(0,0,0,.1)
侧边栏激活项:     bg=#F2F3F5, rx=4(radius-2), h=40, color=#165DFF
Topbar:          h=60, bg=white (部分页面无独立 Topbar)
内容区 x 起点:   240px
内容区宽度:       1180px
内容区 y 起点:   116px (有 Topbar) / 80px (工作台)
内容区内边距:     20~24px
卡片间距:         16px
```

## 卡片 Card

```css
background: #FFFFFF;
border-radius: 8px; /* radius-3 */
box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
padding: 20px;
```

内嵌子卡片（如详情页表格容器）: `rx=4(radius-2), bg=white`

## 颜色系统

### 品牌 & 功能色
```
--primary:    #165DFF   /* 主色按钮/链接/激活 */
--success:    #00B42A   /* 成功/完成 */
--warning:    #FF7D00   /* 警告 */
--danger:     #F53F3F   /* 错误/删除 */
--cyan:       #12D2AC   /* Toggle 开启/特殊标签 */
--blue2:      #307AF2   /* Toggle 备用色 */
```

### 文字色
```
--text-1:  #1D2129   /* 主要文字 */
--text-2:  #4E5969   /* 次要文字 */
--text-3:  #86909C   /* 占位/说明/Label */
--text-4:  #C9CDD4   /* 禁用/未激活步骤 */
--link:    #165DFF   /* 链接 */
```

### 背景 & 填充
```
--bg-page:      #F7F8FA   /* 页面底色 */
--bg-card:      #FFFFFF   /* 卡片 */
--bg-input:     #F2F3F5   /* 输入框默认 */
--bg-table-h:   #F7F8FA   /* 表头/偶数行 */
--bg-nav-act:   #F2F3F5   /* 侧边栏激活 */
--bg-settings:  #E8F3FF   /* 设置页 Tab 激活 */
```

### 边框
```
--border-1:  #F2F3F5   /* 轻分隔线 */
--border-2:  #E5E6EB   /* 常规边框 */
--border-3:  #C9CDD4   /* 输入框默认边框 */
--border-f:  #165DFF   /* 聚焦边框 */
```

## 组件规格

### Button
| 类型 | bg | color | height | padding | rx |
|------|----|-------|--------|---------|-----|
| primary | #165DFF | white | 32px | 0 16px | 8px(radius-3) |
| default | #F2F3F5 | #1D2129 | 32px | 0 16px | 8px(radius-3) |
| ghost | transparent | #165DFF | 32px | 0 16px | 8px(radius-3), border 1px solid #165DFF |
| danger | #F53F3F | white | 32px | 0 16px | 8px(radius-3) |
| link | transparent | #165DFF | auto | 0 | 0 |

### Input / Select / TextArea
```
默认: bg=#F2F3F5, h=32px, rx=4(radius-2), border=none, padding=0 12px, color=#1D2129
激活: bg=white, border=1px solid #165DFF
禁用: bg=#F2F3F5, color=#C9CDD4
TextArea: 同上，h=52px，可多行
placeholder: color=#C9CDD4
label: font-size=12px, color=#86909C, margin-bottom=4px
```

### Table
```
表头:    bg=#F7F8FA, h=48px, font=14px/500, color=#1D2129, border-bottom=1px solid #E5E6EB
数据行:  h=48px, 奇数 bg=white, 偶数 bg=#F7F8FA
行边框:  border-bottom=1px solid #F2F3F5
操作列:  编辑 color=#165DFF, 删除 color=#F53F3F, font=14px
分页:    h=32px, 激活页 bg=#E8F3FF color=#165DFF rx=4(radius-2)
```

### Tag
| 状态 | color | background |
|------|-------|-----------|
| 成功 | #00B42A | #E8FFEA |
| 警告 | #FF7D00 | #FFF3E8 |
| 错误 | #F53F3F | #FFECE8 |
| 信息 | #165DFF | #E8F3FF |
| 默认 | #4E5969 | #F2F3F5 |

### Steps 步骤条
```
激活步骤:  圆圈 fill=#165DFF, label color=#165DFF, font-weight=500
已完成:    圆圈 fill=#00B42A, 图标=✓ white
待完成:    圆圈 stroke=#C9CDD4 fill=white, label color=#86909C
连接线:    done=#165DFF, wait=#C9CDD4 or #F2F3F5, h=2px
```

### Switch
```
轨道: w=40px, h=20px, rx=10
开启: bg=#12D2AC (通知) 或 #307AF2 (安全/蓝色)
关闭: bg=#C9CDD4
手柄: white circle
```

### Descriptions (详情描述列表)
```
label:   font=12px, color=#86909C
value:   font=14px, color=#1D2129
行高:    48px
斑马纹:  偶数行 bg=#F2F3F5
列数:    通常 2 列
```

### Card (卡片列表的子卡片)
```
CardItem: w=266px, h=173px, rx=4(radius-2), border=1px solid #E5E6EB, bg=white
封面图区: h=100px, bg=#F2F3F5
标题:     font=14px/600, color=#1D2129, padding-x=12px
描述:     font=12px, color=#86909C, max-lines=2
底部:     padding=8px 12px, flex space-between
```

### Topbar（标准版）
```
height: 60px, bg: white
搜索框: x=916, w=220, h=32, rx=16, bg=#F2F3F5
图标按钮: x=1152/1200/1248/1296/1344, 32×32, rx=16, bg=#F2F3F5
头像: x=1392, 32×32, rx=16
```

## 指标卡 Icon 背景（多维数据页）

| 图标色 | 背景色 | 主题 |
|--------|--------|------|
| #FF7D00 | #FFE4BA | 橙 |
| #0FC6C2 | #E8FFFB | 青 |
| #165DFF | #E8F3FF | 蓝 |
| #722ED1 | #F5E8FF | 紫 |
| #13AE68 | #E7F6EF | 绿（品牌） |
| #F53F3F | #FFF0F0 | 红 |

## 图表专用配色

```
series-blue:   #165DFF / #81E2FF / grad(#64A2FF→#3469FF)
series-cyan:   #0FC6C2 / grad(#64FFEC→#34FFF3)
series-orange: #FF7D00 / grad(#FFD364→#FFEB34)
series-purple: #722ED1 / grad(#8364FF→#5034FF)
series-green:  #2CAB40 / #86DF6C
grid-line:     #F2F3F5
axis-label:    #4E5969, 12px
```

KPI 卡渐变背景：
```
蓝: #F2F9FE → #E6F4FE
绿: #F5FEF2 → #E6FEEE
橙: #FEFDF2 → #FEF4E6
紫: #F7F7FF → #ECECFF
```

Tooltip 浮层卡:
```
默认: linear(#FDFEFF→#F4F7FC), rx=6, shadow
激活: linear(#2F88FF→#4963FF), rx=6, color=white
```

---
