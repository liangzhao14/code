# Changelog

所有重要变更记录在此文件中。

## v1.0.0 (2026-03-24)

### 新增
- 项目初始版本
- **发现器**: CSS选择器 / sitemap.xml / 递归爬取，三种方式可组合使用
- **抓取器**: requests / Playwright / 自动判断，按需启动浏览器
- **导出器**: PDF / DOCX / Markdown / HTML 四种输出格式
- **任务管理**: 断点续传、失败重试、内容哈希变更检测
- **交互模式**: 引导式分析新网站，自动生成 YAML 配置
- **CLI**: run / discover / retry / status / report / check-update / interactive / list 八个子命令
- **并发支持**: 可配置并发数和请求间隔
- **预置配置**: WNA (world-nuclear.org)、NNSA (nnsa.mee.gov.cn)
- **文档**: README、使用文档、配置指南、设计文档、CLAUDE.md
