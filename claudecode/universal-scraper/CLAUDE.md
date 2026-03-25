# Universal Scraper - Claude 项目记忆

## 项目定位
通用网站文章爬虫，通过 YAML 配置文件适配不同网站。模块化架构：discoverers 发现文章 → fetchers 抓取内容 → exporters 导出文件，由 core/scheduler.py 统一调度。支持断点续传、变更检测、并发下载。

## 关键路径

| 文件 | 职责 |
|------|------|
| `main.py` | CLI 入口，argparse 子命令 |
| `core/scheduler.py` | 调度器，核心流程编排，`load_config()` 加载配置 |
| `core/task_manager.py` | 任务状态管理，`tasks.json` 读写 |
| `core/interactive.py` | 交互式新网站配置向导 |
| `fetchers/__init__.py` | `create_fetcher()` 工厂 + `AutoFetcher` 自动判断 |
| `fetchers/playwright_fetcher.py` | 浏览器渲染，懒加载，翻页支持 |
| `discoverers/__init__.py` | `create_discoverers()` + `discover_all()` 合并去重 |
| `discoverers/base.py` | `Article` dataclass，`deduplicate_articles()` |
| `exporters/__init__.py` | `create_exporters()` 工厂，EXPORTER_MAP |
| `exporters/base.py` | `clean_html()` 共用清理逻辑 |
| `config/default.yaml` | 全局默认配置 |
| `config/sites/*.yaml` | 各网站配置 |

## 配置结构要点
- `discovery` 是列表，可组合多种发现器
- `fetch.mode`: auto / requests / playwright
- `pagination.type`: click / scroll
- `output.category_from`: url_path / parameter
- 参数化发现: `parameters` 字段展开为多个URL

## 接口约定
- Fetcher: `fetch(url) → (html, final_url)`, `download_file(url, path) → bool`
- Discoverer: `discover() → list[Article]`
- Exporter: `export(html, url, filepath) → bool`, `file_extension() → str`
- TaskManager: 状态流转 `pending → downloading → completed / failed`

## 已有配置
- `wna` - World Nuclear Association (world-nuclear.org)，auto模式
- `nnsa` - 国家核安全局 (nnsa.mee.gov.cn)，playwright模式，带翻页和参数化

## 注意事项
- PDF 导出优先用 page 对象直接渲染（效果最好），失败才 fallback 到 set_content
- PlaywrightFetcher 懒加载，不用时不启动浏览器
- AutoFetcher 缓存 JS 判断结果，同域名不重复检测
- 并发时用 threading.Lock 保护 task_manager 写操作
- 项目根目录通过 `PROJECT_ROOT = Path(__file__).parent.parent` 获取
