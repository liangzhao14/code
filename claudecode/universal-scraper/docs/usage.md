# Universal Scraper 使用文档

## 安装

### 1. 安装 Python 依赖

```bash
cd universal-scraper
pip install -r requirements.txt
```

### 2. 安装 Playwright 浏览器（PDF导出或JS渲染需要）

```bash
playwright install chromium
```

### 3. 验证安装

```bash
python main.py list
```

---

## 命令详解

### `run` - 运行爬取

```bash
# 基本用法
python main.py run --site wna

# 强制全量重新下载（忽略已下载和变更检测）
python main.py run --site wna --force

# 爬取所有已配置的网站
python main.py run --site all
```

**输出示例:**
```
══════════════════════════════════════════════════
  开始爬取: wna
══════════════════════════════════════════════════
[INFO] 加载配置: config/sites/wna.yaml
[INFO] 发现文章: 使用 selector 模式...
[INFO] 所有发现器合计: 170 篇 -> 去重后: 168 篇
[INFO] 待处理: 168 篇
  [1/168] Nuclear Generation By Country
    pdf ✓ | markdown ✓
  [2/168] Uranium Production By Country
    pdf ✓ | markdown ✓
  ...

══════════════════════════════════════════════════
  完成: 168 | 失败: 0 | 待处理: 0 | 待更新: 0
  总文件数: 168
══════════════════════════════════════════════════
```

### `discover` - 仅发现文章列表

不下载任何文件，只列出能找到的文章。适合先预览再决定是否下载。

```bash
python main.py discover --site wna
```

### `retry` - 重试失败任务

```bash
python main.py retry --site wna
```

### `status` - 查看下载状态

```bash
python main.py status --site wna
```

**输出示例:**
```
╔══════════════════════════════════════╗
║  World Nuclear Association
╚══════════════════════════════════════╝
  总文章数:  168
  已完成:    165
  失败:      3
  待处理:    0
  待更新:    0

  分类明细:
    Country Profiles - A-F: 18/18 (8.6MB)
    Country Profiles - G-N: 18/18 (8.4MB)
    ...
```

### `report` - 生成统计报告

生成 Markdown 格式的详细统计报告，保存到输出目录。

```bash
python main.py report --site wna
```

### `check-update` - 检查文章更新

对比已下载文章的内容哈希，找出有更新的文章。

```bash
python main.py check-update --site wna
```

之后运行 `run` 即可自动重新下载有更新的文章。

### `interactive` - 交互式配置新网站

```bash
python main.py interactive
```

按提示输入目标URL，脚本会自动分析页面结构，引导你完成配置。

### `list` - 列出所有网站

```bash
python main.py list
```

---

## 使用场景示例

### 场景1：爬取一个新的信息网站

```bash
# 1. 用交互模式分析并生成配置
python main.py interactive
# 输入: https://example.org/articles
# 按提示选择发现方式、输出格式等

# 2. 预览发现的文章
python main.py discover --site example

# 3. 开始下载
python main.py run --site example

# 4. 查看结果
python main.py status --site example
```

### 场景2：定期更新已有网站

```bash
# 检查是否有文章更新
python main.py check-update --site wna

# 运行下载（只处理新增和更新的文章）
python main.py run --site wna

# 生成最新报告
python main.py report --site wna
```

### 场景3：处理下载失败

```bash
# 查看失败情况
python main.py status --site wna

# 重试失败的文章
python main.py retry --site wna
```

### 场景4：强制全量重新下载

```bash
python main.py run --site wna --force
```

### 场景5：只导出 Markdown（修改配置）

编辑 `config/sites/wna.yaml`，修改 output.formats:

```yaml
output:
  formats:
    - markdown
```

然后运行:

```bash
python main.py run --site wna --force
```

### 场景6：批量爬取所有网站

```bash
python main.py run --site all
```

---

## 输出目录结构

每个网站的数据保存在独立目录中：

```
{site_name}_data/
├── tasks.json          # 任务状态记录
├── scraper.log         # 运行日志
├── 下载统计报告.md      # 统计报告（report命令生成）
├── pdf/                # PDF 文件
│   ├── 分类A/
│   │   ├── 文章1.pdf
│   │   └── 文章2.pdf
│   └── 分类B/
├── markdown/           # Markdown 文件
│   ├── 分类A/
│   └── 分类B/
├── docx/               # DOCX 文件（如果配置了）
└── html/               # HTML 文件（如果配置了）
```

---

## 故障排查

### Playwright 安装问题

```bash
pip install playwright
playwright install chromium
```

Windows 如果提示权限问题，请以管理员身份运行。

### 超时问题

编辑网站配置文件，增大 timeout:

```yaml
timeout: 120  # 秒
```

或降低并发数:

```yaml
concurrency: 1
```

### 被网站封禁

增大请求间隔:

```yaml
delay: 5  # 秒
```

### 中文乱码

确保系统支持 UTF-8。脚本内部所有文件读写均使用 UTF-8 编码。
