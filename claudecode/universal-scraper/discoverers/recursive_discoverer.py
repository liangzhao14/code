"""递归发现器：BFS 遍历同域链接发现文章"""

from collections import deque
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from discoverers.base import BaseDiscoverer, Article
from utils.filename import title_from_url, category_from_url
from utils.logger import get_logger

PARSER = "html.parser"

logger = get_logger("recursive_discoverer")


class RecursiveDiscoverer(BaseDiscoverer):
    """BFS 递归爬取发现文章链接"""

    def discover(self) -> list:
        dc = self.disc_config
        start_url = self.normalize_url(dc.get("start_url", "/"))
        filter_pattern = dc.get("filter_pattern", "")
        max_depth = dc.get("max_depth", 3)
        max_pages = dc.get("max_pages", 500)
        link_selector = dc.get("link_selector", "a[href]")

        logger.info(f"递归发现: {start_url} (最大深度={max_depth}, 最大页数={max_pages})")

        articles = []
        visited = set()
        queue = deque([(start_url, 0)])  # (url, depth)

        while queue and len(visited) < max_pages:
            url, depth = queue.popleft()
            url_key = url.lower().rstrip("/")

            if url_key in visited:
                continue
            visited.add(url_key)

            try:
                html, final_url = self.fetcher.fetch(url)
            except Exception as e:
                logger.warning(f"  请求失败: {url} -> {e}")
                continue

            soup = BeautifulSoup(html, PARSER)

            # 检查当前页面是否匹配文章模式
            if self.filter_url(url, filter_pattern):
                title_tag = soup.find("title")
                title = title_tag.get_text(strip=True) if title_tag else title_from_url(url)

                cat_config = self.config.get("output", {})
                cat_from = cat_config.get("category_from", "url_path")
                if cat_from == "url_path":
                    base_path = cat_config.get("category_base_path", "")
                    cat_depth = cat_config.get("category_depth", 2)
                    category = category_from_url(url, base_path, cat_depth)
                else:
                    category = ""

                articles.append(Article(url=url, title=title, category=category))

            # 如果还没到最大深度，继续发现链接
            if depth < max_depth:
                links = soup.select(link_selector)
                for a in links:
                    href = a.get("href", "").strip()
                    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                        continue

                    full_url = self.normalize_url(href)
                    full_key = full_url.lower().rstrip("/")

                    # 只跟踪同域名链接
                    if not self.is_same_domain(full_url):
                        continue
                    if full_key in visited:
                        continue
                    # 跳过常见的非文章资源
                    if any(full_url.lower().endswith(ext) for ext in
                           ('.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico', '.woff', '.woff2')):
                        continue

                    queue.append((full_url, depth + 1))

            if len(visited) % 20 == 0:
                logger.info(f"  已访问 {len(visited)} 页，发现 {len(articles)} 篇文章")

        logger.info(f"递归发现器完成: 访问 {len(visited)} 页，发现 {len(articles)} 篇文章")
        return articles
