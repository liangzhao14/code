# Universal Scraper 实现计划

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 实现一个通用网站文章爬虫，支持配置驱动、多种发现/抓取/导出方式、断点续传和变更检测。

**Architecture:** 模块化设计，core 负责调度和任务管理，fetchers/discoverers/exporters 各自独立，通过统一接口由 scheduler 协调。配置文件驱动，YAML 格式。

**Tech Stack:** Python 3, requests, beautifulsoup4, pyyaml, playwright, python-docx, markdownify

**项目根目录:** `C:\Users\iflytek\Desktop\code\claude code\universal-scraper`

**设计文档:** `docs/design.md`

---

## Chunk 1: 项目脚手架 + 工具模块

### Task 1: 项目基础结构

**Files:**
- Create: `requirements.txt`
- Create: `utils/__init__.py`
- Create: `utils/logger.py`
- Create: `utils/filename.py`
- Create: `utils/hash.py`
- Create: `core/__init__.py`
- Create: `fetchers/__init__.py`
- Create: `discoverers/__init__.py`
- Create: `exporters/__init__.py`
- Create: `config/default.yaml`

- [ ] **Step 1: 创建 requirements.txt**

```
requests>=2.28.0
beautifulsoup4>=4.12.0
pyyaml>=6.0
lxml>=4.9.0
playwright>=1.40.0
python-docx>=0.8.11
markdownify>=0.11.0
```

- [ ] **Step 2: 创建所有 `__init__.py` 文件**

`utils/__init__.py`, `core/__init__.py`, `fetchers/__init__.py`, `discoverers/__init__.py`, `exporters/__init__.py` — 均为空文件。

- [ ] **Step 3: 实现 `utils/logger.py`**

统一日志模块，支持彩色输出和文件日志：

```python
# 提供 get_logger(name) 函数
# 日志格式: "%(asctime)s [%(levelname)s] %(message)s"
# 同时输出到控制台和文件（{output_dir}/scraper.log）
# 提供 setup_logging(output_dir, level) 初始化函数
```

- [ ] **Step 4: 实现 `utils/filename.py`**

文件名清理工具：

```python
# sanitize_filename(name: str, max_length: int = 150) -> str
#   - 移除/替换非法字符 [\\/:*?"<>|]
#   - 压缩多余空格
#   - 限制长度
#
# title_from_url(url: str) -> str
#   - 从URL路径提取标题
#   - 例: "/info/china-nuclear-power" -> "China Nuclear Power"
```

- [ ] **Step 5: 实现 `utils/hash.py`**

内容哈希工具：

```python
# content_hash(html: str) -> str
#   - 提取纯文本（去除标签和空白）
#   - 计算 SHA256 返回十六进制字符串
```

- [ ] **Step 6: 创建 `config/default.yaml`**

```yaml
concurrency: 2
delay: 2
timeout: 60
retry: 3
output_formats:
  - pdf
user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36"
```

- [ ] **Step 7: 创建 `config/sites/` 目录（空目录放一个 `.gitkeep`）**

---

## Chunk 2: 任务管理器

### Task 2: 实现 `core/task_manager.py`

**Files:**
- Create: `core/task_manager.py`

- [ ] **Step 1: 实现 TaskManager 类**

```python
class TaskManager:
    """管理爬取任务状态，支持断点续传和变更检测。

    数据存储在 {output_dir}/tasks.json
    """

    def __init__(self, output_dir: str, site_name: str)
    def load(self)                                    # 加载现有任务记录
    def save(self)                                    # 保存任务记录到JSON
    def add_article(self, url, title, category)       # 添加新文章（状态=pending）
    def get_status(self, url) -> str                  # 获取任务状态
    def set_status(self, url, status, **kwargs)       # 更新状态（completed/failed/needs_update）
    def update_hash(self, url, content_hash)          # 更新内容哈希
    def check_update(self, url, new_hash) -> bool     # 对比哈希，返回是否有变更
    def get_pending(self) -> list                     # 获取待处理任务（pending + failed + needs_update）
    def get_stats(self) -> dict                       # 统计信息（按状态/分类）
    def get_all(self) -> dict                         # 获取所有任务记录
    def reset_failed(self)                            # 将所有failed重置为pending
```

任务状态流转：`pending → downloading → completed / failed`，`completed → needs_update → downloading → completed`

- [ ] **Step 2: 实现 tasks.json 的读写逻辑**

JSON 结构：
```json
{
  "site": "wna",
  "last_run": "2026-03-24T10:00:00",
  "articles": {
    "<url>": {
      "title": "...",
      "category": "...",
      "status": "completed",
      "content_hash": "...",
      "last_downloaded": "...",
      "file_paths": ["pdfs/.../x.pdf", "markdown/.../x.md"],
      "file_size": 0,
      "error": null,
      "retry_count": 0
    }
  }
}
```

- [ ] **Step 3: 实现统计报告生成方法**

```python
def generate_report(self) -> str:
    """生成 Markdown 格式的统计报告"""
    # 总览表格（总数/成功/失败/跳过）
    # 按分类统计表格
    # 失败列表（如有）
    # 文件大小排行 TOP 10
```

---

## Chunk 3: 抓取器

### Task 3: 实现抓取器模块

**Files:**
- Create: `fetchers/base.py`
- Create: `fetchers/requests_fetcher.py`
- Create: `fetchers/playwright_fetcher.py`
- Create: `fetchers/__init__.py`（更新，导出工厂函数）

- [ ] **Step 1: 实现 `fetchers/base.py` 基类**

```python
from abc import ABC, abstractmethod

class BaseFetcher(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.user_agent = config.get("user_agent", "...")
        self.timeout = config.get("timeout", 60)

    @abstractmethod
    def fetch(self, url: str) -> tuple[str, str]:
        """抓取页面，返回 (html_content, final_url)"""
        pass

    @abstractmethod
    def download_file(self, url: str, filepath: str) -> bool:
        """直接下载文件（PDF等），返回是否成功"""
        pass

    def close(self):
        """释放资源"""
        pass
```

- [ ] **Step 2: 实现 `fetchers/requests_fetcher.py`**

```python
class RequestsFetcher(BaseFetcher):
    # 使用 requests.Session 保持 cookies
    # fetch(): GET请求，返回 response.text 和 final url
    # download_file(): 流式下载保存到文件
    # 支持自定义请求头
    # 支持 pre_visit（先访问某个URL获取cookies）
```

- [ ] **Step 3: 实现 `fetchers/playwright_fetcher.py`**

```python
class PlaywrightFetcher(BaseFetcher):
    # 懒加载 Playwright（首次 fetch 时才启动浏览器）
    # fetch(): 导航到URL，等待 networkidle，返回 page.content()
    # download_file(): 对于直接链接的PDF，用 requests 下载
    # 支持 pre_visit
    # 支持等待特定选择器
    # 提供 get_page() 方法供 PDF 导出器使用（需要 page 对象）
    # close(): 关闭浏览器

    # 翻页支持：
    # paginate(page, pagination_config) -> bool
    #   type=click: 点击下一页按钮
    #   type=scroll: 滚动到底部
    #   type=url_param: 修改URL参数
```

- [ ] **Step 4: 更新 `fetchers/__init__.py` 添加自动判断工厂函数**

```python
def create_fetcher(config: dict) -> BaseFetcher:
    """根据配置创建抓取器"""
    mode = config.get("fetch", {}).get("mode", "auto")
    if mode == "requests":
        return RequestsFetcher(config)
    elif mode == "playwright":
        return PlaywrightFetcher(config)
    else:  # auto
        return AutoFetcher(config)

class AutoFetcher(BaseFetcher):
    """自动判断模式：先 requests，检测到 JS 依赖则切换 Playwright"""
    # fetch() 逻辑：
    # 1. 先用 requests 获取
    # 2. 检查 JS 依赖信号（见设计文档 5.4）
    # 3. 需要 JS → 切换 playwright
    # 4. 缓存判断结果，同域名后续请求复用
```

---

## Chunk 4: 发现器

### Task 4: 实现发现器模块

**Files:**
- Create: `discoverers/base.py`
- Create: `discoverers/selector_discoverer.py`
- Create: `discoverers/sitemap_discoverer.py`
- Create: `discoverers/recursive_discoverer.py`
- Create: `discoverers/__init__.py`（更新，导出工厂函数）

- [ ] **Step 1: 实现 `discoverers/base.py` 基类**

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Article:
    url: str
    title: str
    category: str = ""

class BaseDiscoverer(ABC):
    def __init__(self, config: dict, fetcher):
        self.config = config
        self.fetcher = fetcher
        self.base_url = config.get("base_url", "")

    @abstractmethod
    def discover(self) -> list[Article]:
        """发现文章列表"""
        pass

    def _normalize_url(self, url: str) -> str:
        """将相对URL转为绝对URL"""
        pass

    def _filter_url(self, url: str, pattern: str) -> bool:
        """用正则过滤URL"""
        pass
```

- [ ] **Step 2: 实现 `discoverers/selector_discoverer.py`**

```python
class SelectorDiscoverer(BaseDiscoverer):
    """通过 CSS 选择器从列表页提取文章链接"""

    def discover(self) -> list[Article]:
        # 1. 获取 discovery 配置中 type=selector 的条目
        # 2. 如果有 parameters，展开为多个 URL（如 channelid 循环）
        # 3. 对每个 start_url：
        #    a. 用 fetcher 抓取页面
        #    b. BeautifulSoup 解析，用 link_selector 提取链接
        #    c. 用 filter_pattern 正则过滤
        #    d. 从URL或页面提取标题
        #    e. 如果有翻页配置，循环翻页继续提取
        # 4. 去重合并返回
```

- [ ] **Step 3: 实现 `discoverers/sitemap_discoverer.py`**

```python
class SitemapDiscoverer(BaseDiscoverer):
    """解析 sitemap.xml 发现文章"""

    def discover(self) -> list[Article]:
        # 1. 获取 discovery 配置中 type=sitemap 的条目
        # 2. 请求 sitemap.xml（或 sitemap index）
        # 3. 解析 XML，提取 <loc> 中的 URL
        # 4. 如果是 sitemap index，递归解析子 sitemap
        # 5. 用 filter_pattern 过滤
        # 6. 从URL提取标题
        # 7. 去重返回
```

- [ ] **Step 4: 实现 `discoverers/recursive_discoverer.py`**

```python
class RecursiveDiscoverer(BaseDiscoverer):
    """BFS 递归爬取发现文章链接"""

    def discover(self) -> list[Article]:
        # 1. 从 start_url 开始 BFS
        # 2. 提取页面中所有同域链接
        # 3. 用 filter_pattern 判断是否为文章链接（加入结果）
        # 4. 非文章链接且深度未达上限的加入队列继续爬
        # 5. 安全限制：max_depth(默认3)、max_pages(默认500)、同域名
        # 6. 去重返回
```

- [ ] **Step 5: 更新 `discoverers/__init__.py` 添加工厂函数**

```python
def create_discoverers(config: dict, fetcher) -> list[BaseDiscoverer]:
    """根据配置创建所有发现器（可组合）"""
    discoverers = []
    for disc_config in config.get("discovery", []):
        dtype = disc_config["type"]
        if dtype == "selector":
            discoverers.append(SelectorDiscoverer(config, fetcher, disc_config))
        elif dtype == "sitemap":
            discoverers.append(SitemapDiscoverer(config, fetcher, disc_config))
        elif dtype == "recursive":
            discoverers.append(RecursiveDiscoverer(config, fetcher, disc_config))
    return discoverers

def discover_all(discoverers: list) -> list[Article]:
    """运行所有发现器，合并去重"""
    pass
```

---

## Chunk 5: 导出器

### Task 5: 实现导出器模块

**Files:**
- Create: `exporters/base.py`
- Create: `exporters/pdf_exporter.py`
- Create: `exporters/docx_exporter.py`
- Create: `exporters/markdown_exporter.py`
- Create: `exporters/html_exporter.py`
- Create: `exporters/__init__.py`（更新，导出工厂函数）

- [ ] **Step 1: 实现 `exporters/base.py` 基类**

```python
from abc import ABC, abstractmethod

class BaseExporter(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.clean_selectors = config.get("clean_selectors", [])
        self.content_selector = config.get("content_selector", "")

    @abstractmethod
    def export(self, html_content: str, url: str, filepath: str) -> bool:
        """导出内容到文件，返回是否成功"""
        pass

    def clean_html(self, html: str, url: str) -> str:
        """清理HTML：移除导航/页脚等干扰元素，图片URL转绝对路径"""
        # 1. BeautifulSoup 解析
        # 2. 如果有 content_selector，提取正文区域
        # 3. 按 clean_selectors 移除元素
        # 4. img[src] 转绝对路径
        # 5. 返回清理后的 HTML 字符串
        pass

    @abstractmethod
    def file_extension(self) -> str:
        """返回文件扩展名"""
        pass

    def close(self):
        pass
```

- [ ] **Step 2: 实现 `exporters/pdf_exporter.py`**

```python
class PdfExporter(BaseExporter):
    """使用 Playwright 渲染页面为 PDF"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        # 方案A：如果 scheduler 传入了 playwright_fetcher，复用其 page 对象
        #   page.goto(url) → 执行 clean JS → page.pdf(path=filepath)
        # 方案B：如果只有 html_content（requests 抓取的），
        #   启动 playwright，page.set_content(cleaned_html) → page.pdf()
        # PDF 设置: A4, margin 1.5cm, print_background=True

    def file_extension(self) -> str:
        return ".pdf"
```

- [ ] **Step 3: 实现 `exporters/docx_exporter.py`**

```python
class DocxExporter(BaseExporter):
    """将 HTML 转换为 DOCX"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        # 1. clean_html() 清理
        # 2. 用 python-docx 创建文档
        # 3. 解析 HTML 结构，转换为 docx 元素：
        #    h1-h6 → Heading, p → Paragraph, table → Table
        #    img → 尝试下载并插入图片
        #    a → 超链接
        # 4. 保存到 filepath

    def file_extension(self) -> str:
        return ".docx"
```

- [ ] **Step 4: 实现 `exporters/markdown_exporter.py`**

```python
class MarkdownExporter(BaseExporter):
    """将 HTML 转换为 Markdown"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        # 1. clean_html() 清理
        # 2. 用 markdownify 转换
        # 3. 在文件头部添加元信息（标题、来源URL、下载日期）
        # 4. 保存到 filepath（UTF-8）

    def file_extension(self) -> str:
        return ".md"
```

- [ ] **Step 5: 实现 `exporters/html_exporter.py`**

```python
class HtmlExporter(BaseExporter):
    """保存清理后的原始 HTML"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        # 1. clean_html() 清理
        # 2. 注入 <base href="..."> 确保相对路径可用
        # 3. 注入 <meta> 来源信息
        # 4. 保存到 filepath（UTF-8）

    def file_extension(self) -> str:
        return ".html"
```

- [ ] **Step 6: 更新 `exporters/__init__.py` 添加工厂函数**

```python
def create_exporters(config: dict) -> list[BaseExporter]:
    """根据配置创建所有需要的导出器"""
    formats = config.get("output", {}).get("formats", ["pdf"])
    exporters = []
    for fmt in formats:
        if fmt == "pdf":
            exporters.append(PdfExporter(config))
        elif fmt == "docx":
            exporters.append(DocxExporter(config))
        elif fmt == "markdown":
            exporters.append(MarkdownExporter(config))
        elif fmt == "html":
            exporters.append(HtmlExporter(config))
    return exporters
```

---

## Chunk 6: 调度器

### Task 6: 实现 `core/scheduler.py`

**Files:**
- Create: `core/scheduler.py`

- [ ] **Step 1: 实现配置加载**

```python
def load_config(site_name: str) -> dict:
    """加载并合并配置：default.yaml + sites/{site_name}.yaml"""
    # 1. 读取 config/default.yaml 作为基础
    # 2. 读取 config/sites/{site_name}.yaml
    # 3. 深度合并（网站配置覆盖默认配置）
    # 4. 返回合并后的配置字典
```

- [ ] **Step 2: 实现分类提取逻辑**

```python
def extract_category(url: str, config: dict) -> str:
    """根据配置从URL或参数提取分类名"""
    # category_from == "url_path": 从URL路径提取，depth控制层级
    #   例: /info-library/country/argentina → "country" (depth=1)
    # category_from == "parameter": 从参数映射中查找分类名
```

- [ ] **Step 3: 实现 Scheduler 类核心逻辑**

```python
class Scheduler:
    def __init__(self, site_name: str, force: bool = False):
        self.config = load_config(site_name)
        self.task_manager = TaskManager(...)
        self.fetcher = create_fetcher(self.config)
        self.discoverers = create_discoverers(self.config, self.fetcher)
        self.exporters = create_exporters(self.config)
        self.force = force

    def run(self):
        """主流程：发现 → 过滤 → 并发抓取导出"""
        # 1. 发现文章
        # 2. 注册到任务管理器
        # 3. 获取待处理列表（新增 + 失败 + 需更新）
        # 4. ThreadPoolExecutor 并发处理
        # 5. 每完成一篇更新任务状态
        # 6. 生成统计报告

    def _process_article(self, article: Article):
        """处理单篇文章：抓取 → 变更检测 → 导出"""
        # 1. 标记 downloading
        # 2. 抓取内容
        # 3. 计算哈希，检测变更（非force模式）
        # 4. 对每个导出器执行导出
        # 5. 标记 completed 并记录文件信息
        # 6. 异常时标记 failed

    def discover_only(self):
        """仅发现文章列表，不下载"""

    def retry_failed(self):
        """重试所有失败任务"""

    def check_updates(self):
        """检查已下载文章是否有更新"""

    def get_status(self) -> dict:
        """获取当前状态统计"""

    def generate_report(self) -> str:
        """生成并保存 Markdown 统计报告"""

    def close(self):
        """释放所有资源"""
```

- [ ] **Step 4: 实现并发控制和进度显示**

```python
# 使用 concurrent.futures.ThreadPoolExecutor
# 并发数从 config["concurrency"] 读取
# 每完成一篇打印进度: [n/total] 标题 ... 格式1 ✓ 格式2 ✓
# 请求间隔通过 time.sleep(config["delay"]) 控制
# 用 threading.Lock 保护任务管理器的写操作
```

---

## Chunk 7: 交互模式

### Task 7: 实现 `core/interactive.py`

**Files:**
- Create: `core/interactive.py`

- [ ] **Step 1: 实现页面分析功能**

```python
def analyze_page(url: str) -> dict:
    """分析页面结构，返回分析结果"""
    # 1. requests 获取页面
    # 2. 统计：标题、链接数、script标签数、表单数
    # 3. 尝试发现 sitemap.xml（/sitemap.xml, /sitemap_index.xml）
    # 4. 分析常见的文章链接模式
    # 5. 推荐 CSS 选择器（基于链接密度分析）
    # 6. 判断是否需要 JS 渲染
    # 7. 返回分析结果字典
```

- [ ] **Step 2: 实现交互引导流程**

```python
def interactive_mode():
    """交互式引导用户配置新网站"""
    # 1. 输入目标URL
    # 2. 自动分析页面，展示结果
    # 3. 选择发现方式（selector/sitemap/recursive）
    # 4. 如果是 selector：展示推荐选择器，让用户确认或修改
    # 5. 选择输出格式（多选）
    # 6. 设置并发数和延迟
    # 7. 输入网站名称（用于配置文件名）
    # 8. 生成 YAML 配置并保存到 config/sites/
    # 9. 询问是否立即运行
```

- [ ] **Step 3: 实现配置文件生成**

```python
def generate_config(analysis: dict, user_choices: dict) -> str:
    """根据分析结果和用户选择生成 YAML 配置"""
    # 组装配置字典
    # yaml.dump() 输出
    # 保存到 config/sites/{name}.yaml
```

---

## Chunk 8: CLI 入口

### Task 8: 实现 `main.py`

**Files:**
- Create: `main.py`

- [ ] **Step 1: 实现 CLI 命令解析**

```python
import argparse

# 子命令:
#   run          --site NAME [--force]    运行爬取
#   discover     --site NAME              仅发现文章列表
#   retry        --site NAME              重试失败任务
#   status       --site NAME              查看状态统计
#   report       --site NAME              生成统计报告
#   check-update --site NAME              检查文章更新
#   interactive                           交互式模式
#   list                                  列出所有已配置的网站
```

- [ ] **Step 2: 实现依赖检测**

```python
def check_dependencies(formats: list):
    """检查所需依赖是否安装，缺少的给出提示"""
    # pdf → 检查 playwright
    # docx → 检查 python-docx
    # markdown → 检查 markdownify
    # 缺少时打印安装命令，但不崩溃（只有用到时才报错）
```

- [ ] **Step 3: 实现各子命令的入口函数**

```python
def cmd_run(args):
    if args.site == "all":
        # 遍历 config/sites/ 下所有 yaml 文件
    else:
        scheduler = Scheduler(args.site, force=args.force)
        scheduler.run()
        scheduler.close()

def cmd_interactive(args):
    interactive_mode()

# ... 其他子命令类似
```

- [ ] **Step 4: 实现 `--site all` 批量运行**

```python
def get_all_sites() -> list[str]:
    """扫描 config/sites/ 目录，返回所有网站名"""
    pass
```

---

## Chunk 9: 配置文件

### Task 9: 为现有网站编写配置

**Files:**
- Create: `config/sites/wna.yaml`
- Create: `config/sites/nnsa.yaml`

- [ ] **Step 1: 编写 `config/sites/wna.yaml`**

完整的 World Nuclear Association 配置，参考设计文档 4.2 节。

- [ ] **Step 2: 编写 `config/sites/nnsa.yaml`**

完整的国家核安全局配置，参考设计文档 4.3 节，包含所有 channelid 映射（从 nnsa_scraper.py 迁移）。

---

## Chunk 10: 文档

### Task 10: 编写项目文档

**Files:**
- Create: `README.md`
- Create: `CLAUDE.md`
- Create: `CHANGELOG.md`
- Create: `docs/usage.md`
- Create: `docs/config-guide.md`

- [ ] **Step 1: 编写 `README.md` 项目介绍**

内容：
- 项目简介（一句话说明）
- 功能特性列表
- 快速开始（安装 + 第一次运行）
- 目录结构概览
- 命令列表速查
- 技术栈

- [ ] **Step 2: 编写 `CLAUDE.md`**

面向 Claude 的项目记忆文件，内容：
- 项目定位和核心架构（一段话）
- 关键文件路径及职责映射
- 配置文件格式要点
- 模块间接口约定
- 注意事项和已知限制

- [ ] **Step 3: 编写 `CHANGELOG.md`**

```markdown
# Changelog

## v1.0.0 (2026-03-24)

### 新增
- 项目初始版本
- 支持 CSS选择器 / sitemap / 递归 三种文章发现方式
- 支持 requests / Playwright / 自动判断 三种抓取方式
- 支持 PDF / DOCX / Markdown / HTML 四种导出格式
- 任务管理：断点续传、失败重试、变更检测
- 交互模式：引导分析新网站并生成配置
- CLI 命令行界面
- 预置配置：WNA (world-nuclear.org)、NNSA (nnsa.mee.gov.cn)
```

- [ ] **Step 4: 编写 `docs/usage.md` 使用文档**

内容：
- 安装步骤（详细）
- 快速开始示例
- 各命令详细说明 + 输出示例
- 常见使用场景（6-8个示例场景）
- 故障排查

- [ ] **Step 5: 编写 `docs/config-guide.md` 配置编写指南**

内容：
- 配置文件结构总览
- 每个字段的含义、类型、默认值、示例
- 三种发现器的配置方式详解
- 翻页配置详解
- 输出配置详解
- 完整配置模板
- 从零配置一个新网站的教程
