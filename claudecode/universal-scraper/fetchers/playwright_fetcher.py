"""基于 Playwright 的浏览器抓取器"""

import time

from fetchers.base import BaseFetcher
from utils.logger import get_logger

logger = get_logger("playwright_fetcher")


class PlaywrightFetcher(BaseFetcher):
    """使用 Playwright 渲染 JS 页面"""

    def __init__(self, config: dict):
        super().__init__(config)
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None
        self._started = False

    def _ensure_started(self):
        """懒加载：首次使用时才启动浏览器"""
        if self._started:
            return
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise RuntimeError("Playwright 未安装，请运行: pip install playwright && playwright install chromium")

        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=True)
        self._context = self._browser.new_context(
            user_agent=self.user_agent,
            viewport={"width": 1280, "height": 900},
        )
        self._page = self._context.new_page()
        self._started = True

        # 预访问
        pre_visit = self.config.get("fetch", {}).get("pre_visit")
        if pre_visit:
            logger.info(f"预访问获取cookies: {pre_visit}")
            try:
                self._page.goto(pre_visit, wait_until="networkidle", timeout=self.timeout * 1000)
                time.sleep(1)
            except Exception as e:
                logger.warning(f"预访问失败: {e}")

    @property
    def page(self):
        """获取当前 page 对象（供 PDF 导出器使用）"""
        self._ensure_started()
        return self._page

    def fetch(self, url: str) -> tuple:
        """导航到URL并获取渲染后的HTML"""
        self._ensure_started()
        try:
            self._page.goto(url, wait_until="networkidle", timeout=self.timeout * 1000)
        except Exception:
            # networkidle 超时时，尝试用 domcontentloaded
            logger.warning(f"networkidle 超时，尝试 domcontentloaded: {url}")
            self._page.goto(url, wait_until="domcontentloaded", timeout=self.timeout * 1000)
        time.sleep(0.5)
        html = self._page.content()
        final_url = self._page.url
        return html, final_url

    def fetch_with_page(self, url: str):
        """导航到URL，返回 page 对象（用于需要直接操作页面的场景）"""
        self._ensure_started()
        try:
            self._page.goto(url, wait_until="networkidle", timeout=self.timeout * 1000)
        except Exception:
            logger.warning(f"networkidle 超时，尝试 domcontentloaded: {url}")
            self._page.goto(url, wait_until="domcontentloaded", timeout=self.timeout * 1000)
        time.sleep(0.5)
        return self._page

    def paginate(self, pagination_config: dict) -> bool:
        """执行翻页操作

        Returns:
            是否成功翻到下一页
        """
        self._ensure_started()
        ptype = pagination_config.get("type", "click")

        if ptype == "click":
            return self._paginate_click(pagination_config)
        elif ptype == "scroll":
            return self._paginate_scroll(pagination_config)
        return False

    def _paginate_click(self, config: dict) -> bool:
        """点击翻页"""
        next_sel = config.get("next_selector", "")
        disabled_class = config.get("disabled_class", "")
        if not next_sel:
            return False

        has_next = self._page.evaluate(f"""() => {{
            const btn = document.querySelector('{next_sel}');
            if (!btn) return false;
            if ('{disabled_class}' && btn.classList.contains('{disabled_class}')) return false;
            return true;
        }}""")

        if not has_next:
            return False

        self._page.evaluate(f"""() => {{
            const btn = document.querySelector('{next_sel}');
            if (btn) btn.click();
        }}""")

        wait_after = config.get("wait_after", 2)
        time.sleep(wait_after)
        try:
            self._page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            time.sleep(2)
        return True

    def _paginate_scroll(self, config: dict) -> bool:
        """滚动翻页"""
        prev_height = self._page.evaluate("document.body.scrollHeight")
        self._page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(config.get("wait_after", 2))
        new_height = self._page.evaluate("document.body.scrollHeight")
        return new_height > prev_height

    def download_file(self, url: str, filepath: str) -> bool:
        """下载文件（用 requests，不需要浏览器）"""
        import requests
        try:
            resp = requests.get(url, timeout=self.timeout, stream=True,
                                headers={"User-Agent": self.user_agent})
            resp.raise_for_status()
            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(8192):
                    f.write(chunk)
            return True
        except Exception as e:
            logger.error(f"文件下载失败: {url} -> {e}")
            return False

    def close(self):
        """关闭浏览器"""
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
        self._started = False
