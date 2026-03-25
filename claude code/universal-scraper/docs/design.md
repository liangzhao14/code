# Universal Scraper 通用网站爬虫 - 设计文档

> 日期：2026-03-24
> 项目路径：`C:\Users\iflytek\Desktop\code\claude code\universal-scraper`

---

## 一、项目目标

构建一个通用的网站文章/文档爬虫工具，能通过 YAML 配置文件适配不同网站，支持多种文章发现方式、抓取方式和输出格式，具备断点续传和变更检测能力。

### 核心需求

- 以文章/文档类内容为主，兼顾灵活配置
- 支持配置文件驱动（重复爬取）和交互式引导（探索新网站）
- 自动判断请求方式：先尝试 requests，需要 JS 渲染时自动切换 Playwright
- 输出格式：PDF / DOCX / Markdown / 原始HTML
- 文章发现：CSS选择器 / sitemap.xml / 递归爬取，可组合
- 可配置并发数，内置请求间隔控制
- 完整的任务记录、断点续传、失败重试、变更检测

---

## 二、目录结构

```
universal-scraper/
├── main.py                     # 入口：CLI交互 + 配置文件模式
├── requirements.txt            # 依赖清单
├── docs/
│   └── design.md               # 本设计文档
├── config/
│   ├── default.yaml            # 全局默认配置
│   └── sites/                  # 各网站配置文件
│       ├── nnsa.yaml
│       └── wna.yaml
├── core/
│   ├── __init__.py
│   ├── scheduler.py            # 调度器：协调发现→抓取→导出流程
│   ├── task_manager.py         # 任务管理：状态记录、断点续传、变更检测
│   └── interactive.py          # 交互模式：引导用户分析新网站并生成配置
├── fetchers/
│   ├── __init__.py
│   ├── base.py                 # 抓取器基类
│   ├── requests_fetcher.py     # 轻量请求（requests + BeautifulSoup）
│   └── playwright_fetcher.py   # 浏览器渲染（Playwright）
├── discoverers/
│   ├── __init__.py
│   ├── base.py                 # 发现器基类
│   ├── selector_discoverer.py  # CSS选择器提取文章链接
│   ├── sitemap_discoverer.py   # 解析 sitemap.xml
│   └── recursive_discoverer.py # 递归爬取发现链接
├── exporters/
│   ├── __init__.py
│   ├── base.py                 # 导出器基类
│   ├── pdf_exporter.py         # 网页→PDF
│   ├── docx_exporter.py        # 网页→DOCX
│   ├── markdown_exporter.py    # 网页→Markdown
│   └── html_exporter.py        # 保存原始HTML
└── utils/
    ├── __init__.py
    ├── logger.py               # 统一日志
    ├── filename.py             # 文件名清理
    └── hash.py                 # 内容哈希（变更检测用）
```

---

## 三、核心流程

```
配置加载 → 文章发现 → 自动判断抓取方式 → 抓取内容 → 导出为指定格式
                ↕                                    ↕
           任务管理器（记录状态、断点续传、变更检测）
```

---

## 四、配置文件格式

### 4.1 全局默认配置 `default.yaml`

```yaml
concurrency: 2
delay: 2
timeout: 60
retry: 3
output_formats:
  - pdf
user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

### 4.2 网站配置示例 `sites/wna.yaml`

```yaml
name: "World Nuclear Association"
base_url: "https://world-nuclear.org"
output_dir: "wna_data"

discovery:
  - type: selector
    start_url: "/information-library"
    link_selector: "a[href*='/information-library/']"
    filter_pattern: "/information-library/.+/.+"

  - type: sitemap
    url: "/sitemap.xml"
    filter_pattern: "/information-library/"

fetch:
  mode: auto
  js_check: true

clean_selectors:
  - "header"
  - "nav"
  - "footer"
  - ".cookie-banner"
  - ".sidebar"

content_selector: "article, .article-content, main"

pagination:
  enabled: false

output:
  formats:
    - pdf
    - markdown
  category_from: "url_path"
  category_depth: 2
```

### 4.3 复杂场景示例 `sites/nnsa.yaml`

```yaml
name: "国家核安全局法规标准文件库"
base_url: "https://nnsa.mee.gov.cn"
output_dir: "nnsa_data"

discovery:
  - type: selector
    start_url: "/govsearch/haqj.jsp?Stype=2&type=1&channelid={channel_id}"
    link_selector: "a[href]"
    filter_pattern: "\\.(pdf|shtml?)$|/t\\d+_\\d+"
    parameters:
      channel_id:
        "国家法律": 33636
        "行政法规": 33637
        "规章": 33638

fetch:
  mode: playwright
  pre_visit: "https://nnsa.mee.gov.cn/ztzl/fgbzwjk/"

pagination:
  enabled: true
  type: "click"
  next_selector: ".js-page-next"
  disabled_class: "ui-pager-disabled"
  wait_after: 2

output:
  formats:
    - pdf
  category_from: "parameter"
  category_key: "channel_id"
```

---

## 五、模块设计

### 5.1 调度器 `scheduler.py`

整个流程的指挥中心：

1. 加载全局配置 + 网站配置（合并）
2. 初始化任务管理器
3. 根据配置选择发现器，发现文章列表
4. 过滤已完成且未变更的任务
5. 创建任务队列，通过 `concurrent.futures.ThreadPoolExecutor` 并发调度
6. 对每篇文章：抓取 → 清理 → 导出 → 更新任务状态
7. 错误处理和重试逻辑
8. 生成最终的 Markdown 统计报告

### 5.2 任务管理器 `task_manager.py`

维护 `{output_dir}/tasks.json` 数据库：

```json
{
  "site": "wna",
  "last_run": "2026-03-24T10:00:00",
  "articles": {
    "https://world-nuclear.org/...argentina": {
      "title": "Argentina",
      "category": "Country Profiles - A-F",
      "status": "completed",
      "content_hash": "a3f2b8c1...",
      "last_downloaded": "2026-03-24T10:19:35",
      "file_path": "pdfs/Country Profiles - A-F/Argentina.pdf",
      "file_size": 382363
    }
  }
}
```

任务状态流转：`pending → downloading → completed / failed`

功能：

- 断点续传：pending/failed 的任务继续执行
- 变更检测：对比 content_hash（SHA256），不同则标记 needs_update
- 失败重试：记录失败原因和重试次数
- 统计查询：按状态/分类统计

### 5.3 交互模式 `interactive.py`

用户输入新网站URL后的引导流程：

1. 访问URL，展示页面基本信息（标题、链接数等）
2. 尝试自动发现 sitemap.xml
3. 让用户选择文章发现方式
4. 选择器模式下，自动分析页面推荐选择器，用户确认
5. 尝试 requests 请求，对比 Playwright 渲染结果，判断是否需要 JS
6. 让用户选择输出格式
7. 生成 YAML 配置文件保存到 config/sites/
8. 询问是否立即开始爬取

### 5.4 抓取器（Fetchers）

统一接口：`fetch(url) → (html_content, final_url)`

**自动判断逻辑**（`mode: auto`）：

1. 先用 requests 获取页面 HTML
2. 检查 JS 依赖信号：
   - 响应体很小但有大量 `<script>` 标签
   - 包含 SPA 框架标记（`<div id="app">`、`<div id="root">`）
   - content_selector 匹配到的内容为空
3. 检测到 JS 依赖 → 切换 Playwright
4. requests 能拿到完整内容 → 继续用 requests

**Playwright 抓取器**额外支持：

- 页面预访问（获取 cookies）
- 等待特定元素加载
- 翻页操作（点击/滚动/URL参数）
- 弹窗/cookie提示自动关闭

**requests 抓取器**额外支持：

- Session 保持
- 自定义请求头
- 直接下载 PDF/文件流

### 5.5 发现器（Discoverers）

统一接口：`discover() → List[Article]`

三种发现器可组合使用，结果自动去重合并：

| 发现器       | 适用场景             | 工作方式            |
| --------- | ---------------- | --------------- |
| selector  | 列表页有明确的链接结构      | CSS选择器提取链接，支持翻页 |
| sitemap   | 网站提供 sitemap.xml | 解析XML，按URL正则过滤  |
| recursive | 无明确列表页，需递归发现     | BFS遍历同域链接，深度可控  |

**recursive 发现器**安全限制：

- 最大深度默认 3 层
- 最大链接数默认 500
- 只爬同域名
- filter_pattern 正则过滤

### 5.6 导出器（Exporters）

统一接口：`export(html_content, url, filepath)`

| 格式       | 实现方式                       | 依赖          |
| -------- | -------------------------- | ----------- |
| PDF      | Playwright `page.pdf()`    | playwright  |
| DOCX     | html2docx / python-docx 转换 | python-docx |
| Markdown | markdownify 转换             | markdownify |
| HTML     | 直接保存清理后的HTML               | 无额外依赖       |

导出前清理流程（所有格式共用）：

1. 根据 content_selector 提取正文
2. 根据 clean_selectors 移除干扰元素
3. 图片URL转绝对路径
4. 传给导出器

一篇文章可同时导出多种格式。

---

## 六、CLI 命令设计

```bash
# 交互模式
python main.py interactive

# 用配置文件爬取
python main.py run --site wna
python main.py run --site wna --force
python main.py run --site all

# 仅发现文章列表
python main.py discover --site wna

# 重试失败任务
python main.py retry --site wna

# 查看状态统计
python main.py status --site wna

# 生成统计报告
python main.py report --site wna

# 检查文章更新
python main.py check-update --site wna
```

---

## 七、依赖

```
必须:
  - requests
  - beautifulsoup4
  - pyyaml

按需（使用对应功能时才需要）:
  - playwright          # PDF导出 / JS渲染
  - python-docx         # DOCX导出
  - markdownify         # Markdown导出
```

启动时自动检测依赖，缺少的给出安装提示，不会崩溃。
