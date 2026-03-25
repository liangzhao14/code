"""调度器：协调发现→抓取→导出的完整流程"""

import os
import sys
import time
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

from core.task_manager import TaskManager
from fetchers import create_fetcher
from discoverers import create_discoverers, discover_all
from exporters import create_exporters
from utils.logger import setup_logging, get_logger
from utils.filename import sanitize_filename, category_from_url
from utils.hash import content_hash

logger = get_logger("scheduler")

# 项目根目录（main.py 所在目录）
PROJECT_ROOT = Path(__file__).parent.parent


def load_config(site_name: str) -> dict:
    """加载并合并配置：default.yaml + sites/{site_name}.yaml"""
    config_dir = PROJECT_ROOT / "config"

    # 加载默认配置
    default_path = config_dir / "default.yaml"
    config = {}
    if default_path.exists():
        with open(default_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}

    # 加载网站配置
    site_path = config_dir / "sites" / f"{site_name}.yaml"
    if not site_path.exists():
        raise FileNotFoundError(f"网站配置文件不存在: {site_path}")

    with open(site_path, "r", encoding="utf-8") as f:
        site_config = yaml.safe_load(f) or {}

    # 合并（网站配置覆盖默认配置，但保留默认值作为 fallback）
    for key, value in site_config.items():
        config[key] = value

    # 确保 output_dir 是绝对路径或相对于项目根目录
    output_dir = config.get("output_dir", f"{site_name}_data")
    if not os.path.isabs(output_dir):
        config["output_dir"] = str(PROJECT_ROOT / output_dir)

    return config


def get_all_sites() -> list:
    """获取所有已配置的网站名"""
    sites_dir = PROJECT_ROOT / "config" / "sites"
    if not sites_dir.exists():
        return []
    return [f.stem for f in sites_dir.glob("*.yaml")]


class Scheduler:
    """调度器：协调发现→抓取→导出的完整流程"""

    def __init__(self, site_name: str, force: bool = False):
        self.site_name = site_name
        self.force = force
        self.config = load_config(site_name)
        self.output_dir = self.config["output_dir"]

        # 初始化日志
        setup_logging(self.output_dir)

        # 初始化各模块
        self.task_manager = TaskManager(self.output_dir, self.config.get("name", site_name))
        self.fetcher = create_fetcher(self.config)
        self.discoverers = create_discoverers(self.config, self.fetcher)
        self.exporters = create_exporters(self.config)

        self._lock = threading.Lock()
        self._completed = 0
        self._failed = 0
        self._skipped = 0
        self._total = 0

    def run(self):
        """主流程：发现 → 过滤 → 并发抓取导出"""
        logger.info(f"开始运行: {self.config.get('name', self.site_name)}")
        logger.info(f"输出目录: {self.output_dir}")

        # 1. 发现文章
        articles = discover_all(self.discoverers)
        if not articles:
            logger.warning("未发现任何文章")
            return

        # 2. 注册到任务管理器
        new_count = 0
        for article in articles:
            if self.task_manager.add_article(article.url, article.title, article.category):
                new_count += 1
        self.task_manager.save()
        logger.info(f"新增 {new_count} 篇，总计 {len(articles)} 篇")

        # 3. 获取待处理列表
        if self.force:
            # 强制模式：所有文章都处理
            pending = [{"url": a.url, "title": a.title, "category": a.category} for a in articles]
        else:
            pending = self.task_manager.get_pending()

        if not pending:
            logger.info("没有待处理的任务")
            self._print_summary()
            return

        self._total = len(pending)
        logger.info(f"待处理: {self._total} 篇")

        # 4. 并发处理
        concurrency = self.config.get("concurrency", 2)
        delay = self.config.get("delay", 2)

        # Playwright Sync API 不支持多线程，使用 PDF 导出或 Playwright 抓取时强制单线程
        has_playwright = any(fmt in ("pdf",) for fmt in
            self.config.get("output", {}).get("formats", self.config.get("output_formats", ["pdf"])))
        fetch_mode = self.config.get("fetch", {}).get("mode", "auto")
        if has_playwright or fetch_mode == "playwright":
            if concurrency > 1:
                logger.info(f"Playwright 不支持多线程，并发数从 {concurrency} 降为 1")
                concurrency = 1

        if concurrency <= 1:
            # 单线程
            for i, task in enumerate(pending):
                self._process_article(task, i + 1)
                if delay and i < len(pending) - 1:
                    time.sleep(delay)
        else:
            # 多线程
            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                futures = {}
                for i, task in enumerate(pending):
                    future = executor.submit(self._process_article_with_delay, task, i + 1, delay)
                    futures[future] = task

                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        task = futures[future]
                        logger.error(f"处理异常: {task.get('title', '?')} -> {e}")

        # 5. 保存并打印结果
        self.task_manager.save()
        self._print_summary()

    def _process_article_with_delay(self, task: dict, index: int, delay: float):
        """带延迟的文章处理（多线程用）"""
        self._process_article(task, index)
        if delay:
            time.sleep(delay)

    def _process_article(self, task: dict, index: int):
        """处理单篇文章：抓取 → 变更检测 → 导出"""
        url = task["url"]
        title = task.get("title", "未命名")
        category = task.get("category", "Uncategorized")

        with self._lock:
            self.task_manager.set_status(url, "downloading")

        try:
            logger.info(f"  [{index}/{self._total}] {title}")

            # 判断是否是直接可下载的文件（如PDF）
            clean_url = url.split("?")[0].lower()
            is_direct_file = clean_url.endswith(('.pdf', '.doc', '.docx'))

            if is_direct_file and clean_url.endswith('.pdf'):
                # 直接下载 PDF 文件
                self._download_direct_file(url, title, category)
                return

            # 抓取HTML内容
            html, final_url = self.fetcher.fetch(url)

            # 变更检测
            new_hash = content_hash(html)
            if not self.force:
                if not self.task_manager.check_update(url, new_hash):
                    with self._lock:
                        self._skipped += 1
                        self.task_manager.set_status(url, "completed")
                    logger.info(f"    内容未变化，跳过")
                    return

            # 导出到各种格式
            file_paths = []
            total_size = 0
            export_results = []

            for exporter in self.exporters:
                ext = exporter.file_extension()
                fmt_name = ext.lstrip(".")

                # 构建输出路径: {output_dir}/{format}/{category}/{filename}{ext}
                cat_dir = sanitize_filename(category) if category else "Uncategorized"
                filename = sanitize_filename(title) + ext
                filepath = Path(self.output_dir) / fmt_name / cat_dir / filename
                filepath.parent.mkdir(parents=True, exist_ok=True)

                try:
                    # PDF 导出特殊处理：优先使用 page 对象直接渲染
                    success = False
                    if fmt_name == "pdf" and hasattr(self.fetcher, 'fetch_with_page'):
                        from exporters.pdf_exporter import PdfExporter
                        if isinstance(exporter, PdfExporter):
                            page = self.fetcher.fetch_with_page(url)
                            success = exporter.export_from_page(page, str(filepath))

                    if not success:
                        success = exporter.export(html, url, str(filepath))

                    if success:
                        file_paths.append(str(filepath))
                        if filepath.exists():
                            total_size += filepath.stat().st_size
                        export_results.append(f"{fmt_name} OK")
                    else:
                        export_results.append(f"{fmt_name} FAIL")
                except Exception as export_err:
                    logger.warning(f"    {fmt_name} 导出失败: {export_err}")
                    export_results.append(f"{fmt_name} FAIL")

            # 更新任务状态
            with self._lock:
                self.task_manager.set_status(
                    url, "completed",
                    file_paths=file_paths,
                    file_size=total_size,
                )
                self.task_manager.update_hash(url, new_hash)
                self._completed += 1

            logger.info(f"    {' | '.join(export_results)}")

        except Exception as e:
            with self._lock:
                self.task_manager.set_status(url, "failed", error=str(e))
                self._failed += 1
            logger.error(f"    失败: {e}")

    def _download_direct_file(self, url: str, title: str, category: str):
        """直接下载文件（如PDF链接）"""
        cat_dir = sanitize_filename(category) if category else "Uncategorized"
        filename = sanitize_filename(title) + ".pdf"
        filepath = Path(self.output_dir) / "pdf" / cat_dir / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)

        success = self.fetcher.download_file(url, str(filepath))

        with self._lock:
            if success:
                size = filepath.stat().st_size if filepath.exists() else 0
                self.task_manager.set_status(
                    url, "completed",
                    file_paths=[str(filepath)],
                    file_size=size,
                )
                self._completed += 1
                logger.info(f"    直接下载 ✓")
            else:
                self.task_manager.set_status(url, "failed", error="下载失败")
                self._failed += 1

    def discover_only(self):
        """仅发现文章列表，不下载"""
        logger.info(f"仅发现模式: {self.config.get('name', self.site_name)}")
        articles = discover_all(self.discoverers)

        for article in articles:
            self.task_manager.add_article(article.url, article.title, article.category)
        self.task_manager.save()

        logger.info(f"共发现 {len(articles)} 篇文章，已保存到 {self.output_dir}/tasks.json")
        return articles

    def retry_failed(self):
        """重试所有失败任务"""
        count = self.task_manager.reset_failed()
        if count == 0:
            logger.info("没有失败的任务需要重试")
            return
        self.task_manager.save()

        pending = self.task_manager.get_pending()
        self._total = len(pending)
        logger.info(f"重试 {self._total} 个失败任务")

        delay = self.config.get("delay", 2)
        for i, task in enumerate(pending):
            self._process_article(task, i + 1)
            if delay and i < len(pending) - 1:
                time.sleep(delay)

        self.task_manager.save()
        self._print_summary()

    def check_updates(self):
        """检查已下载文章是否有更新"""
        logger.info(f"检查更新: {self.config.get('name', self.site_name)}")
        all_tasks = self.task_manager.get_all()
        completed = {url: a for url, a in all_tasks.items() if a["status"] == "completed"}

        if not completed:
            logger.info("没有已下载的文章")
            return

        updated = 0
        delay = self.config.get("delay", 2)

        for i, (url, article) in enumerate(completed.items()):
            try:
                html, _ = self.fetcher.fetch(url)
                new_hash = content_hash(html)

                if self.task_manager.check_update(url, new_hash):
                    self.task_manager.set_status(url, "needs_update")
                    updated += 1
                    logger.info(f"  有更新: {article['title']}")
            except Exception as e:
                logger.warning(f"  检查失败: {article['title']} -> {e}")

            if delay and i < len(completed) - 1:
                time.sleep(delay)

        self.task_manager.save()
        logger.info(f"检查完成: {len(completed)} 篇中有 {updated} 篇有更新")

    def get_status(self) -> dict:
        """获取当前状态统计"""
        return self.task_manager.get_stats()

    def generate_report(self) -> str:
        """生成并保存 Markdown 统计报告"""
        report = self.task_manager.generate_report()
        report_path = Path(self.output_dir) / "下载统计报告.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)
        logger.info(f"统计报告已保存: {report_path}")
        return report

    def _print_summary(self):
        """打印运行摘要"""
        stats = self.task_manager.get_stats()
        print(f"\n{'═' * 50}")
        print(f"  完成: {stats['completed']} | 失败: {stats['failed']} | "
              f"待处理: {stats['pending']} | 待更新: {stats.get('needs_update', 0)}")
        print(f"  总文件数: {stats['total']}")
        print(f"{'═' * 50}")

    def close(self):
        """释放所有资源"""
        self.fetcher.close()
        for exporter in self.exporters:
            exporter.close()
