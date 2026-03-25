"""导出器基类"""

import re
from abc import ABC, abstractmethod
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class BaseExporter(ABC):
    """所有导出器的基类

    统一接口: export(html_content, url, filepath) -> bool
    """

    def __init__(self, config: dict):
        self.config = config
        self.clean_selectors = config.get("clean_selectors", [])
        self.content_selector = config.get("content_selector", "")

    def clean_html(self, html: str, url: str) -> str:
        """清理HTML：提取正文、移除干扰元素、修复图片路径"""
        soup = BeautifulSoup(html, "html.parser")

        # 1. 如果配置了 content_selector，尝试提取正文
        if self.content_selector:
            selectors = [s.strip() for s in self.content_selector.split(",")]
            content = None
            for sel in selectors:
                content = soup.select_one(sel)
                if content:
                    break
            if content:
                # 用正文替换整个 body
                new_soup = BeautifulSoup("<html><body></body></html>", "lxml")
                new_soup.body.append(content)
                soup = new_soup

        # 2. 移除干扰元素
        for selector in self.clean_selectors:
            for elem in soup.select(selector):
                elem.decompose()

        # 3. 图片 src 转绝对路径
        for img in soup.find_all("img"):
            src = img.get("src", "")
            if src and not src.startswith(("http://", "https://", "data:")):
                img["src"] = urljoin(url, src)

        # 4. 链接 href 转绝对路径
        for a in soup.find_all("a"):
            href = a.get("href", "")
            if href and not href.startswith(("http://", "https://", "#", "javascript:", "mailto:")):
                a["href"] = urljoin(url, href)

        return str(soup)

    def get_clean_text(self, html: str, url: str) -> str:
        """获取清理后的纯文本"""
        cleaned = self.clean_html(html, url)
        soup = BeautifulSoup(cleaned, "html.parser")
        return soup.get_text(separator="\n", strip=True)

    @abstractmethod
    def export(self, html_content: str, url: str, filepath: str) -> bool:
        """导出内容到文件，返回是否成功"""
        pass

    @abstractmethod
    def file_extension(self) -> str:
        """返回文件扩展名（含点号）"""
        pass

    def close(self):
        """释放资源"""
        pass
