"""发现器模块

支持三种发现方式: selector / sitemap / recursive
可组合使用，结果自动去重合并
"""

from discoverers.base import BaseDiscoverer, Article, deduplicate_articles
from discoverers.selector_discoverer import SelectorDiscoverer
from discoverers.sitemap_discoverer import SitemapDiscoverer
from discoverers.recursive_discoverer import RecursiveDiscoverer
from utils.logger import get_logger

logger = get_logger("discoverer")


def create_discoverers(config: dict, fetcher) -> list:
    """根据配置创建所有发现器"""
    discoverers = []
    for disc_config in config.get("discovery", []):
        dtype = disc_config.get("type", "")
        if dtype == "selector":
            discoverers.append(SelectorDiscoverer(config, fetcher, disc_config))
        elif dtype == "sitemap":
            discoverers.append(SitemapDiscoverer(config, fetcher, disc_config))
        elif dtype == "recursive":
            discoverers.append(RecursiveDiscoverer(config, fetcher, disc_config))
        else:
            logger.warning(f"未知的发现器类型: {dtype}")
    return discoverers


def discover_all(discoverers: list) -> list:
    """运行所有发现器，合并去重"""
    all_articles = []
    for disc in discoverers:
        try:
            articles = disc.discover()
            all_articles.extend(articles)
        except Exception as e:
            logger.error(f"发现器 {disc.__class__.__name__} 出错: {e}")

    unique = deduplicate_articles(all_articles)
    logger.info(f"所有发现器合计: {len(all_articles)} 篇 -> 去重后: {len(unique)} 篇")
    return unique
