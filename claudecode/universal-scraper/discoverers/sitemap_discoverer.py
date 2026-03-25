"""Sitemap发现器：解析 sitemap.xml 发现文章"""

import re
import xml.etree.ElementTree as ET

import requests as req

from discoverers.base import BaseDiscoverer, Article
from utils.filename import title_from_url, category_from_url
from utils.logger import get_logger

logger = get_logger("sitemap_discoverer")

# sitemap XML 命名空间
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class SitemapDiscoverer(BaseDiscoverer):
    """解析 sitemap.xml 发现文章"""

    def discover(self) -> list:
        dc = self.disc_config
        sitemap_url = self.normalize_url(dc.get("url", "/sitemap.xml"))
        filter_pattern = dc.get("filter_pattern", "")

        logger.info(f"解析 sitemap: {sitemap_url}")
        articles = self._parse_sitemap(sitemap_url, filter_pattern)
        logger.info(f"Sitemap 发现器共找到 {len(articles)} 篇文章")
        return articles

    def _fetch_xml(self, url: str) -> str:
        """直接用 requests 获取 XML 文本（避免浏览器渲染干扰）"""
        try:
            resp = req.get(url, timeout=30, headers={
                "User-Agent": self.config.get("user_agent", "Mozilla/5.0"),
                "Accept": "application/xml, text/xml, */*",
            })
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            logger.error(f"  sitemap 请求失败: {url} -> {e}")
            return ""

    def _parse_sitemap(self, url: str, filter_pattern: str) -> list:
        """解析 sitemap（支持 sitemap index 递归）"""
        articles = []
        xml_text = self._fetch_xml(url)
        if not xml_text:
            return articles

        # 清理可能导致解析失败的内容
        # 去除 XML 声明前的非法字符
        xml_text = xml_text.strip()
        if not xml_text.startswith("<?xml") and not xml_text.startswith("<"):
            idx = xml_text.find("<")
            if idx > 0:
                xml_text = xml_text[idx:]

        try:
            root = ET.fromstring(xml_text.encode("utf-8"))
        except ET.ParseError:
            # 备用方案：用正则提取 <loc> 标签
            logger.warning(f"  sitemap XML 标准解析失败，使用正则提取")
            return self._parse_with_regex(xml_text, filter_pattern)

        tag = root.tag.lower()

        # sitemap index: 递归解析子 sitemap
        if "sitemapindex" in tag:
            for sitemap in root.findall("sm:sitemap", NS) or root.findall("sitemap"):
                loc = sitemap.find("sm:loc", NS)
                if loc is None:
                    loc = sitemap.find("loc")
                if loc is not None and loc.text:
                    sub_articles = self._parse_sitemap(loc.text.strip(), filter_pattern)
                    articles.extend(sub_articles)
            return articles

        # 普通 sitemap: 提取 URL
        for url_elem in root.findall("sm:url", NS) or root.findall("url"):
            loc = url_elem.find("sm:loc", NS)
            if loc is None:
                loc = url_elem.find("loc")
            if loc is None or not loc.text:
                continue

            page_url = loc.text.strip()
            if not self.filter_url(page_url, filter_pattern):
                continue

            title = title_from_url(page_url)

            cat_config = self.config.get("output", {})
            cat_from = cat_config.get("category_from", "url_path")
            if cat_from == "url_path":
                base_path = cat_config.get("category_base_path", "")
                depth = cat_config.get("category_depth", 2)
                category = category_from_url(page_url, base_path, depth)
            else:
                category = ""

            articles.append(Article(url=page_url, title=title, category=category))

        return articles

    def _parse_with_regex(self, xml_text: str, filter_pattern: str) -> list:
        """备用方案：用正则从 XML 文本中提取 URL"""
        articles = []
        # 匹配 <loc>...</loc> 中的 URL
        urls = re.findall(r'<loc>\s*(https?://[^<]+?)\s*</loc>', xml_text, re.IGNORECASE)
        logger.info(f"  正则提取到 {len(urls)} 个 URL")

        for page_url in urls:
            page_url = page_url.strip()
            if not self.filter_url(page_url, filter_pattern):
                continue

            title = title_from_url(page_url)

            cat_config = self.config.get("output", {})
            cat_from = cat_config.get("category_from", "url_path")
            if cat_from == "url_path":
                base_path = cat_config.get("category_base_path", "")
                depth = cat_config.get("category_depth", 2)
                category = category_from_url(page_url, base_path, depth)
            else:
                category = ""

            articles.append(Article(url=page_url, title=title, category=category))

        return articles
