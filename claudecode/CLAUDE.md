# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

这是一个包含多个独立子项目的工作目录：

- **`news-viewer/`** — 每日新闻查看器单页应用（北京新闻 + AI科技新闻）
- **`file-downloader/`** — Python CLI 批量文件下载工具，支持断点续传
- **`credit-card-manager/`** — 信用卡还款与收支管理系统（Spring Boot + Vue 3 前后端分离），详见其目录下 `CLAUDE.md`
- **`cc-Cowork/`** — 当前为空

## 运行方式

### news-viewer（无需构建）

```bash
cd news-viewer

# 使用 Python 本地服务
python -m http.server 8080

# 或使用 Node.js
npx serve .
```

访问 http://localhost:8080

### file-downloader

```bash
# 下载单个或多个 URL
python file-downloader/downloader.py <URL> [URL2 ...]

# 从文件读取 URL 列表（每行一个，# 开头为注释）
python file-downloader/downloader.py -f links.txt

# 指定输出目录（默认 downloads/）
python file-downloader/downloader.py -o ./output <URL>
```

## 架构说明

### news-viewer

纯前端应用，无框架、无构建工具、无需安装依赖。

**数据流：**
`App.loadNews()` → `NewsData.getNewsByDate(date)` → 并行发起各 RSS 源请求 → 渲染为卡片

- **`js/data.js`**（`NewsData` 模块）：通过 `rss2json.com` 代理 API 获取 RSS，内存缓存 5 分钟。所有新闻源在 `beijingSources` / `aiSources` 数组中配置。今日日期不过滤直接返回最新条目，历史日期按 `pubDate` 字段过滤。
- **`js/app.js`**（`App` 模块）：管理 DOM 元素缓存、事件绑定、骨架屏加载态、新闻卡片渲染。卡片输出使用 `escapeHtml()` 防 XSS，链接使用 `sanitizeUrl()` 限制为 http/https。
- **`css/style.css`**：深色主题，使用 CSS 自定义属性；Grid + Flexbox 实现响应式布局（断点 768px / 1024px）。

### file-downloader

单文件 Python 脚本，仅依赖标准库（`urllib`、`argparse`、`pathlib`）。下载时使用 `.part` 临时文件，通过 HTTP `Range` 头实现断点续传，`Ctrl+C` 中断后下次自动续传。
