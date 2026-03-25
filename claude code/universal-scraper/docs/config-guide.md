# 配置编写指南

本文档说明如何为新网站编写 YAML 配置文件。

## 配置文件位置

- 全局默认配置: `config/default.yaml`
- 各网站配置: `config/sites/{网站名}.yaml`

网站配置会与全局默认配置合并，网站配置优先。

---

## 完整字段说明

### 基本信息

```yaml
name: "网站名称"          # 显示用的名称
base_url: "https://example.com"  # 网站基础URL（不带路径）
output_dir: "example_data"       # 输出目录名
```

### 发现配置 `discovery`

`discovery` 是一个列表，可配置多种发现方式组合使用。

#### selector - CSS选择器模式

```yaml
discovery:
  - type: selector
    start_url: "/articles"              # 起始页路径（相对于 base_url）
    link_selector: "a[href]"            # CSS选择器，提取文章链接
    filter_pattern: "/articles/.+"      # URL正则过滤（可选）
```

**带参数展开:**

适用于列表页通过参数区分分类的情况（如 channelid）。

```yaml
discovery:
  - type: selector
    start_url: "/list?category={cat_id}"
    link_selector: "a.article-link"
    filter_pattern: "/article/\\d+"
    parameters:
      cat_id:
        "科技新闻": 101
        "国际要闻": 102
        "财经频道": 103
```

脚本会展开为 3 个请求，分别替换 `{cat_id}` 为 101/102/103。

#### sitemap - 解析 sitemap.xml

```yaml
discovery:
  - type: sitemap
    url: "/sitemap.xml"                # sitemap路径
    filter_pattern: "/articles/"       # URL正则过滤（可选）
```

支持 sitemap index（自动递归解析子 sitemap）。

#### recursive - 递归爬取

```yaml
discovery:
  - type: recursive
    start_url: "/articles"
    link_selector: "a[href]"           # 提取链接的选择器
    filter_pattern: "/article/\\d+"    # 文章URL正则
    max_depth: 3                       # 最大爬取深度（默认3）
    max_pages: 500                     # 最大访问页数（默认500）
```

#### 组合使用

```yaml
discovery:
  - type: selector
    start_url: "/articles"
    link_selector: ".article-list a"
    filter_pattern: "/article/.+"

  - type: sitemap
    url: "/sitemap.xml"
    filter_pattern: "/article/"
```

结果会自动去重合并。

### 抓取配置 `fetch`

```yaml
fetch:
  mode: auto                           # auto / requests / playwright
  js_check: true                       # auto模式下是否检测JS依赖
  pre_visit: "https://example.com/"    # 预访问URL（获取cookies，可选）
```

| mode | 说明 |
|------|------|
| `auto` | 先用 requests，检测到 JS 依赖自动切 Playwright |
| `requests` | 始终用 requests（静态网站） |
| `playwright` | 始终用 Playwright（JS渲染网站） |

### 页面清理 `clean_selectors`

导出前移除的页面元素（CSS选择器列表）:

```yaml
clean_selectors:
  - "header"
  - "nav"
  - "footer"
  - ".sidebar"
  - ".cookie-banner"
  - ".ads"
  - ".share-buttons"
```

### 正文选择器 `content_selector`

可选。如果配置了，只保留匹配的正文区域，忽略其他内容。多个选择器用逗号分隔，取第一个匹配的。

```yaml
content_selector: "article, .article-content, main, .post-body"
```

### 翻页配置 `pagination`

```yaml
pagination:
  enabled: true
  type: "click"                     # click / scroll
  next_selector: ".next-page"       # 下一页按钮选择器（click模式）
  disabled_class: "disabled"        # 禁用状态的CSS类名
  wait_after: 2                     # 翻页后等待秒数
```

| type | 说明 |
|------|------|
| `click` | 点击下一页按钮 |
| `scroll` | 滚动到底部加载更多 |

### 输出配置 `output`

```yaml
output:
  formats:                          # 输出格式列表
    - pdf
    - markdown
  category_from: "url_path"         # 分类提取方式
  category_base_path: "/articles"   # URL基础路径（提取分类时去除）
  category_depth: 2                 # 取几级路径作为分类
```

**`category_from` 选项:**

| 值 | 说明 |
|----|------|
| `url_path` | 从URL路径提取分类 |
| `parameter` | 从参数化发现的标签提取分类 |

**`category_depth` 示例:**

URL: `/articles/tech/ai/article-name`，base_path: `/articles`

- depth=1 → 分类: `Tech`
- depth=2 → 分类: `Tech - Ai`

### 其他配置

```yaml
concurrency: 2        # 并发下载数
delay: 2              # 请求间隔（秒）
timeout: 60           # 页面超时（秒）
retry: 3              # 失败重试次数
```

---

## 完整配置模板

```yaml
# ========== 基本信息 ==========
name: "网站名称"
base_url: "https://example.com"
output_dir: "example_data"

# ========== 文章发现 ==========
discovery:
  - type: selector
    start_url: "/articles"
    link_selector: "a.article-link"
    filter_pattern: "/article/.+"

# ========== 抓取设置 ==========
fetch:
  mode: auto

# ========== 页面清理 ==========
clean_selectors:
  - "header"
  - "nav"
  - "footer"
  - ".sidebar"
  - ".cookie-banner"

# 正文选择器（可选）
content_selector: "article, main"

# ========== 翻页（可选）==========
pagination:
  enabled: false

# ========== 输出设置 ==========
output:
  formats:
    - pdf
    - markdown
  category_from: "url_path"
  category_depth: 2

# ========== 性能设置 ==========
concurrency: 2
delay: 2
timeout: 60
```

---

## 从零配置一个新网站

### 步骤1：分析目标网站

先用浏览器打开目标网站，观察：
1. 文章列表页在哪？URL 是什么？
2. 文章链接的 HTML 结构是什么？（右键→检查元素）
3. 是否有分页？分页方式是什么？
4. 页面是否需要 JS 渲染？

### 步骤2：使用交互模式

```bash
python main.py interactive
```

脚本会自动分析并给出建议，你只需确认或调整。

### 步骤3：测试配置

```bash
# 先只发现文章，确认列表正确
python main.py discover --site mysite

# 确认无误后开始下载
python main.py run --site mysite
```

### 步骤4：调优

根据实际效果调整配置：
- 发现的文章太多/太少 → 调整 `filter_pattern`
- 页面加载超时 → 增大 `timeout`，切换到 `playwright` 模式
- 被封禁 → 增大 `delay`，降低 `concurrency`
