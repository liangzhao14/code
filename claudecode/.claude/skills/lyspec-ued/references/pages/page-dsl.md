# lingyang Page DSL — 全量页面结构 JSON

## 页面索引
1. [工作台](#p1) | 2. [多维数据](#p2) | 3. [分析页](#p3) | 4. [查询表格](#p4) | 5. [卡片列表](#p5)
6. [基础详情页](#p6) | 7. [分步表单](#p7) | 8. [用户信息](#p8) | 9. [用户设置](#p9) | 10. [用户设置-2](#p10) | 11. [成功页](#p11)

---

<a name="p1"></a>
## 1. 工作台

```json
{
  "id": "workplace", "title": "工作台", "canvas": "1440×1066",
  "hasSidebar": true, "sidebar": { "x": 8, "y": 64, "w": 204, "h": 84 },
  "hasTopbar": false,
  "sections": [
    {
      "id": "left-main", "type": "Card",
      "rect": { "x": 240, "y": 80, "w": 880, "h": 548 },
      "children": [
        {
          "id": "welcome-banner", "type": "Banner",
          "rect": { "x": 240, "y": 80, "w": 880, "h": 68 },
          "style": { "bg": "linear-gradient(135deg,#DBF0FF,#C1E5FF)" },
          "content": { "greeting": "{{user.greeting}}", "subtitle": "{{user.role}}" }
        },
        {
          "id": "metric-cards", "type": "MetricCardRow",
          "rect": { "x": 240, "y": 151, "w": 904, "h": 94 },
          "gap": 12,
          "cards": [
            { "x": 240, "w": 208, "title": "指标1", "iconColor": "#165DFF", "iconBg": "#E8F3FF" },
            { "x": 471, "w": 208, "title": "指标2", "iconColor": "#7DA2FF", "iconBg": "#EEF3FF" },
            { "x": 702, "w": 208, "title": "指标3", "iconColor": "#FF7D00", "iconBg": "#FFF3E8" },
            { "x": 932, "w": 208, "title": "指标4", "iconColor": "#00B42A", "iconBg": "#E8FFEA" }
          ]
        },
        {
          "id": "line-chart", "type": "MultiSeriesLineChart",
          "rect": { "y": 263, "h": 340 },
          "series": [
            { "stroke": "#117EFF", "gradFrom": "#117EFF", "gradTo": "#1180FF" },
            { "stroke": "#249AFF", "gradFrom": "#1EE7FF", "gradTo": "#6F42FB" }
          ],
          "tooltip": {
            "rect": { "w": 180, "h": 72, "rx": 6 },
            "bg": "linear-gradient(180deg,#FDFEFF,#F4F7FC)"
          }
        }
      ]
    },
    {
      "id": "right-card", "type": "Card",
      "rect": { "x": 1140, "y": 80, "w": 280, "h": 400 },
      "children": [
        { "id": "todo-list", "type": "List", "h": 240 },
        { "id": "map-block", "type": "ImageBlock", "rect": { "x": 1140, "y": 494, "w": 280, "h": 158 } }
      ]
    }
  ]
}
```

---

<a name="p2"></a>
## 2. 多维数据

```json
{
  "id": "multi-data", "title": "多维数据", "canvas": "1440×1196",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 108, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "left-main", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 764, "h": 500 },
      "children": [
        {
          "id": "metric-row", "type": "MetricCardRow", "rect": { "y": 178, "h": 62 },
          "cards": [
            { "x": 260, "w": 178, "title": "内容量",  "iconBg": "#FFE4BA", "iconColor": "#FF7D00" },
            { "x": 442, "w": 177, "title": "点赞量",  "iconBg": "#E8FFFB", "iconColor": "#0FC6C2" },
            { "x": 623, "w": 179, "title": "收藏量",  "iconBg": "#E8F3FF", "iconColor": "#165DFF" },
            { "x": 806, "w": 179, "title": "用户数",  "iconBg": "#F5E8FF", "iconColor": "#722ED1" }
          ]
        },
        {
          "id": "bubble-chart", "type": "BubbleScatterChart",
          "rect": { "y": 270, "h": 290 },
          "series": [
            { "gradFrom": "#64A2FF", "gradTo": "#3469FF" },
            { "gradFrom": "#64FFEC", "gradTo": "#34FFF3" },
            { "gradFrom": "#FFD364", "gradTo": "#FFEB34" },
            { "gradFrom": "#8364FF", "gradTo": "#5034FF" }
          ]
        },
        {
          "id": "legend-selector", "type": "CheckboxLegend",
          "rect": { "x": 730, "y": 326, "w": 180, "h": 180, "rx": 6 },
          "bg": "linear-gradient(180deg,#FDFEFF,#F4F7FC)",
          "itemStyle": { "w": 164, "h": 32, "rx": 4, "bg": "white" }
        }
      ]
    },
    {
      "id": "right-top", "type": "Card",
      "rect": { "x": 1020, "y": 116, "w": 400, "h": 200 },
      "children": [
        {
          "id": "ranking-progress", "type": "RankingProgressList",
          "progressColor": "#4086FF", "progressBg": "#E8F3FF",
          "barH": 8, "barRx": 4
        }
      ]
    },
    {
      "id": "right-bottom", "type": "Card",
      "rect": { "x": 1020, "y": 332, "w": 400, "h": 280 },
      "children": [{ "type": "GroupedBarChart", "colors": ["#4086FF","#33D1C9","#F77234","#722ED1"] }]
    },
    {
      "id": "small-charts", "type": "SmallChartRow",
      "rect": { "y": 628, "h": 200 },
      "gap": 16,
      "cards": [
        { "x": 240,  "w": 283, "chartColor": "#165DFF" },
        { "x": 539,  "w": 283, "chartColor": "#0FC6C2" },
        { "x": 838,  "w": 283, "chartColor": "#FF7D00" },
        { "x": 1137, "w": 283, "chartColor": "#722ED1" }
      ]
    },
    {
      "id": "data-table", "type": "DataTable",
      "rect": { "x": 240, "y": 844, "w": 1180, "h": 312 },
      "pagination": true
    }
  ]
}
```

---

<a name="p3"></a>
## 3. 分析页

```json
{
  "id": "analysis", "title": "分析页", "canvas": "1440×1248",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 108, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "kpi-banner", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 210 },
      "children": [
        { "id": "kpi-1", "x": 260, "y": 172, "w": 270, "h": 134, "rx": 4,
          "bg": "linear-gradient(135deg,#F2F9FE,#E6F4FE)", "accentColor": "#165DFF",
          "title": "访问量", "miniChart": "BarChart", "chartColor": "#249EFF" },
        { "id": "kpi-2", "x": 550, "y": 172, "w": 270, "h": 134, "rx": 4,
          "bg": "linear-gradient(135deg,#F5FEF2,#E6FEEE)", "accentColor": "#00B42A",
          "title": "转化率", "miniChart": "GroupedBar", "chartColors": ["#2CAB40","#86DF6C"] },
        { "id": "kpi-3", "x": 840, "y": 172, "w": 270, "h": 136, "rx": 4,
          "bg": "linear-gradient(135deg,#F2F9FE,#E6F4FE)", "accentColor": "#165DFF",
          "title": "留存率", "miniChart": "BarChart", "chartColor": "#249EFF" },
        { "id": "kpi-4", "x": 1130, "y": 172, "w": 276, "h": 136, "rx": 4,
          "bg": "linear-gradient(135deg,#FEFDF2,#FEF4E6)", "accentColor": "#FF7D00",
          "title": "收入", "miniChart": "AreaLine", "chartColor": "#FFAA00" },
        { "id": "kpi-5", "x": 1130, "y": 172, "w": 270, "h": 136, "rx": 4,
          "bg": "linear-gradient(135deg,#F7F7FF,#ECECFF)", "accentColor": "#722ED1",
          "title": "活跃用户", "miniChart": "BarChart", "chartColor": "#8D4EDA" }
      ]
    },
    {
      "id": "bar-chart", "type": "Card",
      "rect": { "x": 240, "y": 342, "w": 780, "h": 440 },
      "children": [
        {
          "type": "BarChart", "barColor": "#81E2FF", "barW": 16, "barRx": 2,
          "gridLine": "#F2F3F5", "axisLabelColor": "#4E5969"
        },
        {
          "id": "tooltip-normal",
          "type": "FloatingTooltip", "rect": { "x": 594, "y": 890, "w": 180, "h": 144, "rx": 6 },
          "bg": "linear-gradient(180deg,#FDFEFF,#F4F7FC)",
          "itemStyle": { "w": 164, "h": 32, "rx": 4, "bg": "white" }
        },
        {
          "id": "tooltip-active",
          "type": "FloatingTooltip", "rect": { "x": 632, "y": 538, "w": 180, "h": 144, "rx": 6 },
          "bg": "linear-gradient(180deg,#2F88FF,#4963FF)", "textColor": "white",
          "itemStyle": { "w": 164, "h": 32, "rx": 4, "bg": "rgba(255,255,255,0.2)" }
        }
      ]
    },
    {
      "id": "rank-list", "type": "Card",
      "rect": { "x": 1038, "y": 342, "w": 382, "h": 440 },
      "children": [{ "type": "RankedList", "rowH": 44, "zebraOdd": "white", "zebraEven": "#F7F8FA" }]
    },
    {
      "id": "analysis-table", "type": "Card",
      "rect": { "x": 240, "y": 798, "w": 1180, "h": 430 },
      "children": [
        { "type": "TabsBar", "tabs": ["全部","类目1","类目2","类目3"] },
        { "type": "Table", "progressCol": { "color": "#165DFF" } },
        {
          "id": "range-slider", "type": "RangeSlider",
          "rect": { "y": 1119, "w": 1100, "h": 14, "rx": 2 },
          "trackBg": "#F2F3F5",
          "activeBg": "linear-gradient(90deg,white,#CEE0FF,#92BAFF)",
          "handle": { "w": 22, "h": 20, "rx": 10, "bg": "white" }
        }
      ]
    }
  ]
}
```

---

<a name="p4"></a>
## 4. 查询表格

```json
{
  "id": "search-table", "title": "查询表格", "canvas": "1440×900",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 152, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "content", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 768 },
      "children": [
        {
          "id": "filter-bar", "type": "FilterBar",
          "layout": { "cols": 3, "rows": 2, "inputW": 243.3, "inputH": 32, "inputBg": "#F2F3F5", "inputRx": 2 },
          "colXs": [340, 687.3, 1034.7], "rowYs": [176, 228],
          "labelStyle": { "fontSize": 12, "color": "#86909C", "marginBottom": 4 },
          "actionButtons": [
            { "label": "查询", "type": "primary", "x": 1318, "y": 176, "w": 82, "h": 32 },
            { "label": "重置", "type": "default", "x": 1318, "y": 228, "w": 82, "h": 32 }
          ]
        },
        {
          "id": "operation-bar", "type": "OperationBar",
          "rect": { "y": 300, "h": 32 },
          "left": [
            { "label": "新建",     "type": "primary",  "x": 260, "w": 82, "h": 32 },
            { "label": "批量删除", "type": "default",  "x": 350, "w": 88, "h": 32 }
          ],
          "right": [
            { "label": "导出", "type": "default", "x": 1318, "w": 82, "h": 32 }
          ]
        },
        {
          "id": "data-table", "type": "Table",
          "rect": { "y": 348 },
          "rowH": 48, "headerBg": "#F7F8FA",
          "zebra": { "odd": "white", "even": "#F7F8FA" },
          "columns": [
            { "title": "序号",     "dataIndex": "index",     "w": 80 },
            { "title": "名称",     "dataIndex": "name",      "w": 200 },
            { "title": "类型",     "dataIndex": "type",      "w": 120 },
            { "title": "状态",     "dataIndex": "status",    "w": 120, "render": "Tag" },
            { "title": "创建时间", "dataIndex": "createdAt", "w": 180 },
            { "title": "操作",     "dataIndex": "actions",   "w": 160,
              "render": "ActionLinks",
              "links": [{ "label": "编辑", "color": "#165DFF" }, { "label": "删除", "color": "#F53F3F" }]
            }
          ],
          "pagination": { "align": "right", "pageSize": 10 }
        }
      ]
    }
  ]
}
```

---

<a name="p5"></a>
## 5. 卡片列表

```json
{
  "id": "card-list", "title": "卡片列表", "canvas": "1440×900",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 152, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "content", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 764 },
      "children": [
        {
          "id": "toolbar", "type": "Toolbar",
          "rect": { "y": 136, "h": 80 },
          "left": [{ "label": "新建卡片", "type": "primary", "w": 88, "h": 32 }],
          "right": [{ "type": "SearchInput", "w": 200, "h": 32 }, { "type": "ViewToggle" }]
        },
        {
          "id": "card-grid", "type": "CardGrid",
          "rect": { "y": 262 },
          "layout": { "cols": 4, "rows": 3, "gap": 20 },
          "colXs": [260, 552, 842, 1134],
          "rowYs": [262, 452, 642],
          "cardItem": {
            "w": 266, "h": 173, "rx": 3.5, "border": "1px solid #E5E6EB",
            "children": [
              { "id": "cover",  "type": "Image",  "h": 100, "bg": "#F2F3F5" },
              { "id": "title",  "type": "Text",   "font": "14px/600", "color": "#1D2129", "px": 12, "mt": 8 },
              { "id": "desc",   "type": "Text",   "font": "12px", "color": "#86909C", "lines": 2, "px": 12 },
              { "id": "footer", "type": "HStack", "px": 12, "py": 8,
                "children": [
                  { "type": "AvatarGroup", "size": 24 },
                  { "type": "Tag" },
                  { "type": "IconButton", "icon": "more" }
                ]
              }
            ]
          }
        }
      ]
    }
  ]
}
```

---

<a name="p6"></a>
## 6. 基础详情页

```json
{
  "id": "basic-detail", "title": "基础详情页", "canvas": "1440×1202",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 240, "w": 204, "h": 84 },
  "sections": [
    {
      "id": "page-header", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 130 },
      "children": [
        { "type": "Breadcrumb", "y": 136,
          "items": ["首页", "列表", "详情"],
          "style": { "fontSize": 12, "color": "#86909C", "activeColor": "#1D2129" }
        },
        { "type": "PageTitle", "y": 158, "fontSize": 20, "fontWeight": 600 },
        { "type": "ButtonGroup", "align": "right",
          "buttons": [
            { "label": "编辑", "type": "primary" },
            { "label": "下载", "type": "default" },
            { "label": "归档", "type": "default" }
          ]
        }
      ]
    },
    {
      "id": "section-1", "type": "Card", "title": "基本信息",
      "rect": { "x": 240, "y": 262, "w": 1180, "h": 280 },
      "children": [{
        "type": "Descriptions", "columns": 2, "rowH": 48,
        "labelStyle": { "fontSize": 12, "color": "#86909C" },
        "valueStyle": { "fontSize": 14, "color": "#1D2129" },
        "zebra": { "even": "#F2F3F5" }, "itemCount": 12
      }]
    },
    {
      "id": "section-2", "type": "Card", "title": "关联信息",
      "rect": { "x": 240, "y": 558, "w": 1180, "h": 280 },
      "children": [{
        "type": "Descriptions", "columns": 2, "rowH": 48,
        "labelStyle": { "fontSize": 12, "color": "#86909C" },
        "valueStyle": { "fontSize": 14, "color": "#1D2129" },
        "zebra": { "even": "#F2F3F5" }, "itemCount": 10
      }]
    },
    {
      "id": "section-3", "type": "Card", "title": "数据记录",
      "rect": { "x": 240, "y": 854, "w": 1180, "h": 278 },
      "extra": { "type": "Link", "label": "查看更多", "color": "#165DFF" },
      "children": [{
        "type": "Table",
        "rect": { "x": 260, "y": 922, "w": 1140, "h": 550, "rx": 2 },
        "rowH": 48, "pagination": true
      }]
    }
  ]
}
```

---

<a name="p7"></a>
## 7. 分步表单

```json
{
  "id": "step-form", "title": "分步表单", "canvas": "1440×900",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 240, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "content", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 610 },
      "children": [
        {
          "id": "steps", "type": "Steps",
          "rect": { "y": 156, "h": 64 }, "current": 0,
          "items": [
            { "title": "填写基本信息" },
            { "title": "填写详细信息" },
            { "title": "完成" }
          ],
          "style": {
            "active":  { "circle": "#165DFF", "label": "#165DFF", "fontWeight": 500 },
            "done":    { "circle": "#00B42A", "icon": "check", "iconColor": "white" },
            "wait":    { "circle": "#C9CDD4", "label": "#86909C" },
            "line": { "done": "#165DFF", "wait": "#C9CDD4", "h": 2 }
          }
        },
        {
          "id": "form-layout", "type": "TwoColumn",
          "rect": { "y": 260 },
          "left": { "x": 260, "w": 340, "type": "IllustrationArea" },
          "right": {
            "x": 610, "w": 440, "type": "Form",
            "items": [
              { "label": "字段1", "type": "Input",  "rect": { "y": 344, "w": 440, "h": 32 }, "bg": "#F2F3F5" },
              { "label": "字段2", "type": "Input",  "rect": { "y": 396, "w": 440, "h": 32 }, "bg": "#F2F3F5" },
              { "label": "字段3", "type": "Select", "rect": { "y": 448, "w": 440, "h": 32 }, "bg": "#F2F3F5" },
              { "label": "字段4", "type": "Input",  "rect": { "y": 500, "w": 440, "h": 32 }, "bg": "#F2F3F5",
                "activeStyle": { "bg": "white", "border": "1px solid #165DFF" }
              }
            ]
          }
        },
        {
          "id": "step-nav", "type": "StepNavigation",
          "rect": { "y": 658, "h": 68 },
          "borderTop": "1px solid #F2F3F5",
          "buttons": [
            { "label": "上一步", "type": "ghost",   "borderColor": "#165DFF" },
            { "label": "下一步", "type": "primary",  "bg": "#165DFF" }
          ]
        }
      ]
    }
  ]
}
```

---

<a name="p8"></a>
## 8. 用户信息

```json
{
  "id": "user-info", "title": "用户信息", "canvas": "1440×1568",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 372, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "user-banner", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 204 },
      "hasBgImage": true,
      "children": [
        { "type": "Avatar", "size": 72, "shape": "circle" },
        { "type": "VStack", "content": ["姓名(20px/600)", "职位(14px #4E5969)", "标签组(#12D2AC)"] },
        { "type": "StatGroup", "align": "right",
          "stats": [{ "label": "关注" }, { "label": "粉丝" }, { "label": "文章" }]
        }
      ]
    },
    {
      "id": "upper-row", "type": "TwoColumnRow",
      "rect": { "y": 336 }, "gap": 16,
      "left": {
        "type": "Card", "rect": { "x": 240, "w": 832, "h": 356 },
        "title": "个人信息",
        "children": [{
          "type": "CardGrid", "cols": 3, "rows": 2, "gap": 8,
          "colXs": [260, 530, 799], "rowYs": [404, 548],
          "cardItem": { "w": 252, "h": 126, "rx": 3.5, "border": "1px solid #E5E6EB" }
        }]
      },
      "right": {
        "type": "Card", "rect": { "x": 1088, "w": 332, "h": 356 },
        "title": "联系 / 团队",
        "children": [{ "type": "List", "innerCard": { "x": 1108, "y": 392, "w": 292, "h": 288, "rx": 4 } }]
      }
    },
    {
      "id": "lower-row", "type": "TwoColumnRow",
      "rect": { "y": 708 }, "gap": 16,
      "left": {
        "type": "Card", "rect": { "x": 241, "w": 832, "h": 802 },
        "title": "动态 / 作品",
        "children": [{ "type": "Table", "rect": { "x": 241, "y": 776, "w": 812, "h": 714 } }]
      },
      "right": {
        "type": "Card", "rect": { "x": 1088, "w": 332, "h": 356 },
        "title": "关注列表",
        "children": [{ "type": "List" }]
      }
    }
  ]
}
```

---

<a name="p9"></a>
## 9. 用户设置

```json
{
  "id": "user-settings", "title": "用户设置", "canvas": "1440×900",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 372, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "profile-card", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 174 },
      "children": [
        { "type": "Avatar", "size": 64, "shape": "circle" },
        { "type": "VStack", "content": ["姓名(18px/600)", "简介(14px #4E5969)"] },
        { "type": "Button", "label": "修改头像", "type": "default", "align": "right" }
      ]
    },
    {
      "id": "settings-panel", "type": "Card",
      "rect": { "x": 240, "y": 306, "w": 1180, "h": 574 },
      "children": [
        {
          "id": "v-tabs", "type": "VerticalTabs",
          "w": 144,
          "items": ["基本设置", "安全设置", "绑定设置", "通知设置"],
          "activeStyle": { "bg": "#E8F3FF", "color": "#165DFF" }
        },
        {
          "id": "form-area", "x": 385,
          "type": "Form",
          "items": [
            { "label": "用户名",   "type": "Input",    "w": 375, "h": 32, "bg": "#F2F3F5" },
            { "label": "邮箱",     "type": "Input",    "w": 375, "h": 32, "bg": "#F2F3F5" },
            { "label": "地区",     "type": "Select",   "w": 375, "h": 32, "bg": "#F2F3F5" },
            { "label": "个人简介", "type": "TextArea",
              "rect": { "x": 385, "y": 634, "w": 375, "h": 52 }, "bg": "#F2F3F5", "rx": 2 }
          ],
          "footer": [
            { "label": "保存", "type": "primary", "bg": "#165DFF" },
            { "label": "重置", "type": "ghost" }
          ]
        }
      ]
    }
  ]
}
```

---

<a name="p10"></a>
## 10. 用户设置-2（通知/安全设置）

```json
{
  "id": "user-settings-2", "title": "用户设置-2", "canvas": "1440×900",
  "note": "结构同用户设置，右侧内容替换为 Toggle 设置列表",
  "sections": [
    { "id": "profile-card", "$ref": "user-settings.profile-card" },
    {
      "id": "settings-panel", "type": "Card",
      "rect": { "x": 240, "y": 306, "w": 1180, "h": 574 },
      "children": [
        { "id": "v-tabs", "$ref": "user-settings.v-tabs" },
        {
          "id": "toggle-list", "type": "ToggleSettingsList",
          "x": 385,
          "itemStyle": { "h": 48, "borderBottom": "1px solid #F2F3F5" },
          "items": [
            { "title": "通知类型1", "desc": "描述文字", "switch": { "checkedColor": "#12D2AC", "default": true } },
            { "title": "通知类型2", "desc": "描述文字", "switch": { "checkedColor": "#307AF2", "default": false } },
            { "title": "安全验证", "right": { "type": "Link", "label": "去设置", "color": "#165DFF" } }
          ]
        }
      ]
    }
  ]
}
```

---

<a name="p11"></a>
## 11. 成功页

```json
{
  "id": "result-success", "title": "成功页", "canvas": "1440×900",
  "hasSidebar": true, "hasTopbar": true,
  "sidebar": { "x": 8, "y": 284, "w": 204, "h": 128 },
  "sections": [
    {
      "id": "content", "type": "Card",
      "rect": { "x": 240, "y": 116, "w": 1180, "h": 764 },
      "layout": "center-vertical",
      "children": [
        {
          "id": "result-icon", "type": "ResultIcon",
          "centerX": 720, "y": 244,
          "circle": { "r": 56, "fill": "#00B42A" },
          "icon": { "type": "check", "color": "white", "size": 32 }
        },
        { "id": "title", "type": "Text", "content": "提交成功",
          "y": 355, "fontSize": 28, "fontWeight": 600, "color": "#1D2129", "align": "center" },
        { "id": "desc", "type": "Text", "content": "{{result.description}}",
          "y": 399, "fontSize": 14, "color": "#86909C", "align": "center" },
        { "id": "action-btn", "type": "Button",
          "rect": { "x": 824, "y": 424, "w": 116, "h": 32 },
          "label": "返回列表", "buttonType": "primary", "bg": "#165DFF"
        },
        {
          "id": "step-dots", "type": "StepDots",
          "y": 593,
          "dots": [
            { "cx": 490,  "r": 5, "fill": "#165DFF", "status": "done" },
            { "cx": 658,  "r": 5, "fill": "#165DFF", "status": "done" },
            { "cx": 826,  "r": 5, "fill": "#C9CDD4", "status": "current" },
            { "cx": 994,  "r": 5, "fill": "#C9CDD4", "status": "wait" },
            { "cx": 1162, "r": 5, "fill": "#C9CDD4", "status": "wait" }
          ],
          "connector": { "stroke": "#C9CDD4", "strokeW": 1 }
        }
      ]
    }
  ]
}
```

---
