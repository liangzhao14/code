# code

用 AI 编程工具探索、实践、构建的项目集合。涵盖全栈应用、数据爬虫、小工具等，记录与 Claude Code、Codex、OpenCode 协作开发的过程。

---

## 目录结构

```
code/
├── claudecode/       # 使用 Claude Code 构建的项目
├── codex/            # 使用 Codex 构建的项目
├── opencode/         # 使用 OpenCode 构建的项目
├── Agent/            # Agent 相关实验
└── files/            # 数据文件与爬虫
```

---

## claudecode

> 使用 [Claude Code](https://claude.ai/code) 开发的项目

### 信用卡账单管理系统

全栈 Web 应用，帮助个人管理多张信用卡、账单、收支记录。

**技术栈**: Spring Boot 3 · MyBatis Plus · MySQL · Vue 3 · Element Plus · ECharts

**功能**:
- 多卡管理，账单录入与追踪
- 收入 / 支出分类统计
- 月度报表与可视化图表
- JWT 登录鉴权

```
claudecode/credit-card-manager/
├── backend/    # Spring Boot 后端
├── frontend/   # Vue 3 前端
└── sql/        # 数据库初始化脚本
```

---

### Universal Scraper - 通用网站爬虫

模块化、可配置的文章爬虫框架，通过 YAML 配置适配任意网站。

**技术栈**: Python 3 · Playwright · BeautifulSoup4 · requests

**功能**:
- 多种发现方式：CSS 选择器 / Sitemap / 递归爬取
- 智能渲染：自动判断是否需要浏览器
- 多格式导出：PDF / DOCX / Markdown / HTML
- 断点续传、变更检测、失败重试

```bash
python main.py run --site wna      # 爬取指定网站
python main.py interactive         # 交互式配置新网站
```

```
claudecode/universal-scraper/
```

---

### 每日新闻查看器

纯前端新闻阅览页面，展示北京新闻与 AI 科技资讯，支持日期切换与响应式布局。

**技术栈**: HTML5 · CSS3 · Vanilla JavaScript

```
claudecode/news-viewer/
```

---

### 文件下载器

```
claudecode/file-downloader/
```

---

## codex

> 使用 Codex 构建的项目

### 测试用例生成 API

基于 AI 的自动化测试用例生成服务，输入需求描述，输出结构化测试用例。

- PRD 文档：`codex/docs/`
- UED 设计稿：`codex/docs/test_case_generation_api_v1.0_UED/`

---

## opencode

> 使用 OpenCode 构建的项目

### 贪吃蛇游戏

经典贪吃蛇，单文件 HTML 实现，开箱即玩。

```
opencode/snake/snake.html
```

### 登录测试页

```
opencode/test_login/
```

---

## files

### 核安全法规文件爬虫

爬取国家核安全局（NNSA）法规标准文件库与世界核协会（WNA）文章，支持 PDF 批量下载。

```
files/
├── nnsa_scraper.py        # 国家核安全局爬虫
├── wna_scraper.py         # 世界核协会爬虫
├── nnsa_data/             # 爬取数据输出
└── wna_data/              # 爬取数据输出
```

---

## Agent

AI Agent 相关实验与探索。

---

## 关于

本仓库是学习与实验 AI 辅助编程的记录，项目从想法到实现基本全程与 AI 协作完成。

---

## 最近变更

## 2026-03-25 12:13

- 删除: "files/README_\344\275\277\347\224\250\346\214\207\345\215\227.md"
- 删除: files/nnsa_data/api_requests.json
- 删除: files/nnsa_data/debug_paging.html
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963873.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963881.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963883.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963901.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963911.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963919.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963926.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963930.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963960.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211213_963963.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964015.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964017.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964019.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964021.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964040.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964041.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964042.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964050.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964057.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964075.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211214_964123.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211215_964144.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211215_964148.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20211215_964187.txt"
- 删除: "files/nnsa_data/html_articles/\350\247\204\347\253\240/t20240802_1083222.txt"
- 删除: files/nnsa_data/nnsa_regulations.json
- 删除: files/nnsa_data/nnsa_regulations.txt

