"""CSS选择器发现器：通过选择器从列表页提取文章链接"""

from bs4 import BeautifulSoup

from discoverers.base import BaseDiscoverer, Article
from utils.filename import title_from_url, category_from_url
from utils.logger import get_logger

logger = get_logger("selector_discoverer")


class SelectorDiscoverer(BaseDiscoverer):
    """通过 CSS 选择器从列表页提取文章链接"""

    def discover(self) -> list:
        dc = self.disc_config
        start_url = dc.get("start_url", "")
        link_selector = dc.get("link_selector", "a[href]")
        filter_pattern = dc.get("filter_pattern", "")
        parameters = dc.get("parameters", {})

        articles = []

        if parameters:
            # 参数化模式：展开参数循环
            for param_name, param_values in parameters.items():
                for label, value in param_values.items():
                    url = self.normalize_url(start_url.replace(f"{{{param_name}}}", str(value)))
                    logger.info(f"发现文章: {label} (参数 {param_name}={value})")
                    found = self._discover_from_page(url, link_selector, filter_pattern, category=label)
                    articles.extend(found)
        else:
            # 普通模式
            url = self.normalize_url(start_url)
            logger.info(f"发现文章: {url}")
            articles = self._discover_from_page(url, link_selector, filter_pattern)

        logger.info(f"Selector 发现器共找到 {len(articles)} 篇文章")
        return articles

    def _discover_from_page(self, url: str, link_selector: str, filter_pattern: str,
                            category: str = "") -> list:
        """从单个页面提取文章链接"""
        articles = []
        page_num = 1
        pagination = self.config.get("pagination", {})
        has_pagination = pagination.get("enabled", False)

        while True:
            try:
                html, _ = self.fetcher.fetch(url) if page_num == 1 or not has_pagination else (self._get_current_html(), url)
                if page_num == 1:
                    html, _ = self.fetcher.fetch(url)
            except Exception as e:
                logger.error(f"  页面请求失败: {url} -> {e}")
                break

            soup = BeautifulSoup(html, "html.parser")
            links = soup.select(link_selector)

            found = 0
            for a in links:
                href = a.get("href", "").strip()
                if not href or href.startswith(("#", "javascript:", "mailto:")):
                    continue

                full_url = self.normalize_url(href)
                if not self.filter_url(full_url, filter_pattern):
                    continue

                title = a.get_text(strip=True)
                if not title or len(title) < 2:
                    title = title_from_url(full_url)

                if not category:
                    cat_config = self.config.get("output", {})
                    cat_from = cat_config.get("category_from", "url_path")
                    if cat_from == "url_path":
                        base_path = cat_config.get("category_base_path", "")
                        depth = cat_config.get("category_depth", 2)
                        cat = category_from_url(full_url, base_path, depth)
                    else:
                        cat = ""
                else:
                    cat = category

                articles.append(Article(url=full_url, title=title, category=cat))
                found += 1

            logger.info(f"  第{page_num}页: 找到 {found} 条")

            if not found and page_num == 1:
                break

            # 翻页
            if has_pagination and hasattr(self.fetcher, 'paginate'):
                if not self.fetcher.paginate(pagination):
                    break
                page_num += 1
                # 翻页后重新获取HTML
                try:
                    html = self.fetcher.page.content() if hasattr(self.fetcher, 'page') else ""
                    soup = BeautifulSoup(html, "html.parser")
                    links = soup.select(link_selector)
                    found = 0
                    for a in links:
                        href = a.get("href", "").strip()
                        if not href or href.startswith(("#", "javascript:", "mailto:")):
                            continue
                        full_url = self.normalize_url(href)
                        if not self.filter_url(full_url, filter_pattern):
                            continue
                        title = a.get_text(strip=True)
                        if not title or len(title) < 2:
                            title = title_from_url(full_url)
                        cat = category if category else ""
                        articles.append(Article(url=full_url, title=title, category=cat))
                        found += 1
                    logger.info(f"  第{page_num}页: 找到 {found} 条")
                    if not found:
                        break
                except Exception as e:
                    logger.error(f"  翻页后获取失败: {e}")
                    break
            else:
                break

        return articles
