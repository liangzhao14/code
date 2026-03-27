# Universal Scraper - 通用网站文章爬虫

一个模块化、可配置的网站文章爬虫工具。通过 YAML 配置文件适配不同网站，支持多种文章发现方式、抓取方式和输出格式，具备断点续传和变更检测能力。

## 功能特性

- **多种发现方式**: CSS选择器 / sitemap.xml / 递归爬取，可组合使用
- **智能抓取**: 自动判断 requests 或 Playwright，按需启动浏览器
- **多格式导出**: PDF / DOCX / Markdown / HTML，一篇文章可同时导出多种格式
- **断点续传**: 任务状态持久化，中断后继续下载
- **变更检测**: 基于内容哈希，自动识别文章更新
- **失败重试**: 记录失败原因，一键重试
- **交互模式**: 引导式配置新网站，自动分析页面结构
- **并发控制**: 可配置并发数和请求间隔

## 快速开始

### 安装依赖

```bash
cd universal-scraper
pip install -r requirements.txt
playwright install chromium  # PDF导出或JS渲染需要
```

### 运行已有配置

```bash
# 查看所有已配置的网站
python main.py list

# 爬取 World Nuclear Association
python main.py run --site wna

# 爬取所有已配置的网站
python main.py run --site all
```

### 配置新网站

```bash
# 交互式向导（推荐）
python main.py interactive

# 或手动创建配置文件
# 参见 docs/config-guide.md
```

## 命令速查

| 命令 | 说明 |
|------|------|
| `python main.py run --site <name>` | 运行爬取 |
| `python main.py run --site <name> --force` | 强制全量重新下载 |
| `python main.py run --site all` | 爬取所有网站 |
| `python main.py discover --site <name>` | 仅发现文章列表 |
| `python main.py retry --site <name>` | 重试失败任务 |
| `python main.py status --site <name>` | 查看下载状态 |
| `python main.py report --site <name>` | 生成统计报告 |
| `python main.py check-update --site <name>` | 检查文章更新 |
| `python main.py interactive` | 交互式配置新网站 |
| `python main.py list` | 列出所有网站 |

## 目录结构

```
universal-scraper/
├── main.py                 # CLI 入口
├── config/
│   ├── default.yaml        # 全局默认配置
│   └── sites/              # 各网站配置
├── core/
│   ├── scheduler.py        # 调度器
│   ├── task_manager.py     # 任务管理
│   └── interactive.py      # 交互模式
├── fetchers/               # 抓取器 (requests/playwright/auto)
├── discoverers/            # 发现器 (selector/sitemap/recursive)
├── exporters/              # 导出器 (pdf/docx/markdown/html)
├── utils/                  # 工具函数
└── docs/                   # 文档
```

## 技术栈

- Python 3.8+
- requests + BeautifulSoup4 (轻量抓取)
- Playwright (浏览器渲染)
- PyYAML (配置文件)
- python-docx (DOCX导出)
- markdownify (Markdown导出)

## 详细文档

- [使用文档](docs/usage.md) - 详细使用说明和示例
- [配置编写指南](docs/config-guide.md) - YAML 配置文件说明
- [设计文档](docs/design.md) - 架构设计
