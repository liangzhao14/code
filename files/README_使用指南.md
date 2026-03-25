# 国家核安全局 法规标准文件库 爬虫使用指南

## 网站分析

**目标网址**: https://nnsa.mee.gov.cn/ztzl/fgbzwjk/

该网站是国家核安全局的法规标准文件库，内容通过 JavaScript 动态加载。
左侧有分类导航，包括：国家法律、行政法规、规章、规范性文件、核安全导则、标准、国际公约等。

### 技术特点

- 页面内容通过 JS 动态渲染，直接用 requests 访问只能拿到空壳 HTML
- 文件多为 PDF 格式，链接格式类似: `.../202304/P020230415379872799144.pdf`
- 需要浏览器自动化工具或找到后端 AJAX 接口

---

## 快速开始

### 1. 安装依赖

```bash
pip install playwright beautifulsoup4 requests
playwright install chromium
```

### 2. 运行爬虫

```bash
python nnsa_scraper.py
```

选择方案 1（Playwright）获得最佳效果。

---

## 两种方案对比

| 特性      | 方案一: Playwright | 方案二: Requests |
| ------- | --------------- | ------------- |
| 安装复杂度   | 较高（需要下载浏览器）     | 低             |
| 能否抓动态内容 | ✅ 是             | ❌ 可能不行        |
| 速度      | 较慢              | 快             |
| 稳定性     | 高               | 取决于页面结构       |
| 推荐场景    | 首选方案            | 页面是静态渲染时      |

---

## 实用技巧：手动抓包找接口

如果你想用更轻量的 requests 方案，可以先手动找到后端接口：

### 步骤：

1. 打开 Chrome 浏览器，访问 https://nnsa.mee.gov.cn/ztzl/fgbzwjk/
2. 按 `F12` 打开开发者工具
3. 切换到 `Network`（网络）标签页
4. 点击左侧分类菜单（如"国家法律"）
5. 观察 Network 面板中新出现的 XHR/Fetch 请求
6. 找到返回 JSON 或 HTML 列表数据的请求
7. 右键该请求 → "Copy as cURL" → 可以转换为 Python requests 代码

### 常见的接口模式：

```
# 政府网站常见的列表接口格式
GET /cms/channel/list?channelId=xxx&pageNo=1&pageSize=20
POST /api/articles/query  (body: {category: "xxx", page: 1})
```

---

## 输出说明

爬虫会在 `nnsa_data/` 目录下生成：

```
nnsa_data/
├── nnsa_regulations.json      # 结构化数据（JSON格式）
├── nnsa_regulations.txt       # 可读的文本清单
└── pdfs/                      # 下载的PDF文件（运行方案3后）
    ├── 国家法律/
    ├── 行政法规/
    └── ...
```

---

## 注意事项

1. **请求频率**: 脚本默认每次请求间隔 2 秒，请勿降低此值
2. **数据用途**: 这些是公开的政府法规文件，用于学习研究一般没有问题
3. **网站变更**: 如果网站改版，选择器可能需要更新
4. **网络环境**: 如果在海外访问，可能需要考虑网络连通性

---

## 如果脚本不工作？

1. **Playwright 方案不工作**：
   
   - 检查是否正确安装了 chromium: `playwright install chromium`
   - 尝试设置 `headless=False` 看看浏览器实际行为

2. **Requests 方案抓不到数据**：
   
   - 说明页面是动态渲染的，请切换到 Playwright 方案
   - 或者按上面的"手动抓包"步骤找到真实接口

3. **PDF 下载失败**：
   
   - 检查网络连接
   - 部分文件可能需要特定的 Referer 头
