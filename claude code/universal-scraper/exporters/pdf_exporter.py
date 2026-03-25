"""PDF 导出器：使用 Playwright 渲染页面为 PDF"""

import time
from pathlib import Path

from exporters.base import BaseExporter
from utils.logger import get_logger

logger = get_logger("pdf_exporter")


class PdfExporter(BaseExporter):
    """使用 Playwright 渲染页面为 PDF

    不自行创建 Playwright 实例。由 scheduler 通过 set_fetcher() 注入共享的 fetcher，
    或通过 export_from_page() 直接传入 page 对象。
    """

    def __init__(self, config: dict):
        super().__init__(config)
        self._fetcher = None

    def set_fetcher(self, fetcher):
        """注入共享的 fetcher（由 scheduler 调用）"""
        self._fetcher = fetcher

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        """导出为 PDF —— 使用共享的 fetcher 导航到页面后渲染"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

        if self._fetcher and hasattr(self._fetcher, 'fetch_with_page'):
            # 使用共享的 fetcher 导航并渲染
            try:
                page = self._fetcher.fetch_with_page(url)
                return self._render_pdf(page, filepath)
            except Exception as e:
                logger.error(f"PDF 导出失败: {url} -> {e}")
                return False
        else:
            # 没有 fetcher，尝试自己启动 Playwright
            return self._export_standalone(html_content, url, filepath)

    def export_from_page(self, page, filepath: str) -> bool:
        """直接用已有的 page 对象导出 PDF"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        return self._render_pdf(page, filepath)

    def _render_pdf(self, page, filepath: str) -> bool:
        """从 page 对象渲染 PDF"""
        try:
            clean_js = self._build_clean_js()
            if clean_js:
                page.evaluate(clean_js)

            page.pdf(
                path=filepath,
                format="A4",
                margin={"top": "1.5cm", "bottom": "1.5cm", "left": "1.5cm", "right": "1.5cm"},
                print_background=True,
            )
            return True
        except Exception as e:
            logger.error(f"PDF 渲染失败: {e}")
            return False

    def _export_standalone(self, html_content: str, url: str, filepath: str) -> bool:
        """独立模式：自己创建 Playwright 实例（fallback）"""
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            logger.error("PDF 导出需要 Playwright，请运行: pip install playwright && playwright install chromium")
            return False

        pw = None
        browser = None
        try:
            pw = sync_playwright().start()
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page()

            timeout = self.config.get("timeout", 60) * 1000
            try:
                page.goto(url, wait_until="networkidle", timeout=timeout)
            except Exception:
                page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            time.sleep(0.5)

            return self._render_pdf(page, filepath)
        except Exception as e:
            logger.error(f"PDF 独立导出失败: {url} -> {e}")
            return False
        finally:
            if browser:
                browser.close()
            if pw:
                pw.stop()

    def _build_clean_js(self) -> str:
        """构建清理页面的 JS 代码"""
        selectors = self.clean_selectors
        if not selectors:
            return ""
        selectors_js = ", ".join(f"'{s}'" for s in selectors)
        return f"""() => {{
            const selectors = [{selectors_js}];
            for (const sel of selectors) {{
                document.querySelectorAll(sel).forEach(el => el.remove());
            }}
        }}"""

    def file_extension(self) -> str:
        return ".pdf"
