"""抓取器模块

提供三种模式: requests / playwright / auto
auto 模式会先尝试 requests，检测到 JS 依赖时自动切换 Playwright
"""

from bs4 import BeautifulSoup

from fetchers.base import BaseFetcher
from fetchers.requests_fetcher import RequestsFetcher
from fetchers.playwright_fetcher import PlaywrightFetcher
from utils.logger import get_logger

logger = get_logger("fetcher")


class AutoFetcher(BaseFetcher):
    """自动判断模式：先 requests，检测到 JS 依赖则切换 Playwright"""

    def __init__(self, config: dict):
        super().__init__(config)
        self._requests = RequestsFetcher(config)
        self._playwright = None
        self._needs_js_cache = {}  # 域名 -> bool 缓存
        self.content_selector = config.get("content_selector", "")

    def _get_playwright(self):
        if not self._playwright:
            self._playwright = PlaywrightFetcher(self.config)
        return self._playwright

    def _needs_js(self, html: str, url: str) -> bool:
        """检测页面是否需要 JS 渲染"""
        from urllib.parse import urlparse
        domain = urlparse(url).netloc

        # 缓存命中
        if domain in self._needs_js_cache:
            return self._needs_js_cache[domain]

        needs = False
        soup = BeautifulSoup(html, "html.parser")

        # 信号1: 响应体很小但有大量 script 标签
        scripts = soup.find_all("script")
        body_text = soup.get_text(strip=True)
        if len(scripts) > 5 and len(body_text) < 500:
            needs = True

        # 信号2: SPA 框架标记
        spa_markers = soup.select("#app, #root, #__nuxt, #__next, [data-reactroot]")
        if spa_markers and len(body_text) < 500:
            needs = True

        # 信号3: content_selector 匹配到的内容为空
        if self.content_selector and not needs:
            content = soup.select_one(self.content_selector)
            if content and len(content.get_text(strip=True)) < 100:
                needs = True

        self._needs_js_cache[domain] = needs
        if needs:
            logger.info(f"检测到 {domain} 需要 JS 渲染，切换到 Playwright")
        return needs

    def fetch(self, url: str) -> tuple:
        """自动判断并抓取"""
        from urllib.parse import urlparse
        domain = urlparse(url).netloc

        # 如果已知需要 JS
        if self._needs_js_cache.get(domain):
            return self._get_playwright().fetch(url)

        # 先用 requests 尝试
        try:
            html, final_url = self._requests.fetch(url)
            if self._needs_js(html, url):
                return self._get_playwright().fetch(url)
            return html, final_url
        except Exception:
            # requests 失败，尝试 Playwright
            logger.info(f"requests 请求失败，切换 Playwright: {url}")
            self._needs_js_cache[domain] = True
            return self._get_playwright().fetch(url)

    def download_file(self, url: str, filepath: str) -> bool:
        return self._requests.download_file(url, filepath)

    @property
    def page(self):
        """获取 Playwright page 对象"""
        return self._get_playwright().page

    def fetch_with_page(self, url: str):
        """使用 Playwright 导航并返回 page"""
        return self._get_playwright().fetch_with_page(url)

    def paginate(self, pagination_config: dict) -> bool:
        """翻页（委托给 Playwright）"""
        return self._get_playwright().paginate(pagination_config)

    def close(self):
        self._requests.close()
        if self._playwright:
            self._playwright.close()


def create_fetcher(config: dict) -> BaseFetcher:
    """根据配置创建抓取器"""
    mode = config.get("fetch", {}).get("mode", "auto")
    if mode == "requests":
        logger.info("抓取模式: requests")
        return RequestsFetcher(config)
    elif mode == "playwright":
        logger.info("抓取模式: playwright")
        return PlaywrightFetcher(config)
    else:
        logger.info("抓取模式: auto (自动判断)")
        return AutoFetcher(config)
