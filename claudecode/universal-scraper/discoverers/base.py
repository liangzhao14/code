"""发现器基类"""

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse


@dataclass
class Article:
    """文章信息"""
    url: str
    title: str
    category: str = ""


class BaseDiscoverer(ABC):
    """所有发现器的基类

    统一接口: discover() -> list[Article]
    """

    def __init__(self, config: dict, fetcher, disc_config: dict):
        self.config = config
        self.fetcher = fetcher
        self.disc_config = disc_config
        self.base_url = config.get("base_url", "")

    @abstractmethod
    def discover(self) -> list:
        """发现文章列表"""
        pass

    def normalize_url(self, url: str) -> str:
        """将相对URL转为绝对URL"""
        if url.startswith(("http://", "https://")):
            return url
        return urljoin(self.base_url, url)

    def filter_url(self, url: str, pattern: str) -> bool:
        """用正则过滤URL"""
        if not pattern:
            return True
        return bool(re.search(pattern, url, re.IGNORECASE))

    def is_same_domain(self, url: str) -> bool:
        """判断URL是否与基础URL同域名"""
        base_domain = urlparse(self.base_url).netloc.lower()
        url_domain = urlparse(url).netloc.lower()
        return url_domain == base_domain or not url_domain


def deduplicate_articles(articles: list) -> list:
    """文章去重（按URL去重，保留第一个）"""
    seen = set()
    unique = []
    for article in articles:
        # URL 统一小写比较
        key = article.url.lower().rstrip("/")
        if key not in seen:
            seen.add(key)
            unique.append(article)
    return unique
