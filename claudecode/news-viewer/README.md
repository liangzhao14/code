# 每日新闻查看器

一个展示北京新闻和AI科技新闻的前端页面应用。

## 功能特性

- 📰 北京新闻展示（政治、经济、文化、民生等）
- 🤖 AI科技新闻展示（大模型、企业动态、行业趋势等）
- 📅 支持选择过去7天内的日期
- 🔄 一键刷新新闻
- 📱 响应式设计，支持桌面端和移动端
- ✨ 流畅的动画效果

## 项目结构

```
news-viewer/
├── index.html          # 主页面
├── css/
│   └── style.css       # 样式文件
├── js/
│   ├── app.js          # 主应用逻辑
│   └── data.js         # 新闻数据模块
└── README.md           # 说明文档
```

## 使用方法

直接在浏览器中打开 `index.html` 即可使用。

### 本地运行

```bash
# 使用Python
python -m http.server 8080

# 或使用Node.js
npx serve .
```

然后访问 http://localhost:8080

## 技术栈

- HTML5
- CSS3 (自定义属性、Grid布局、Flexbox)
- Vanilla JavaScript (ES6+)
- Google Fonts (Noto Serif SC, Noto Sans SC, Inter)

## 浏览器支持

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## 许可证

MIT License
