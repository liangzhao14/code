"""抓取器基类"""

from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    """所有抓取器的基类

    统一接口: fetch(url) -> (html_content, final_url)
    """

    def __init__(self, config: dict):
        self.config = config
        self.user_agent = config.get("user_agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36")
        self.timeout = config.get("timeout", 60)

    @abstractmethod
    def fetch(self, url: str) -> tuple:
        """抓取页面

        Returns:
            (html_content, final_url) 元组
        """
        pass

    @abstractmethod
    def download_file(self, url: str, filepath: str) -> bool:
        """直接下载文件（PDF等二进制文件）

        Returns:
            是否成功
        """
        pass

    def close(self):
        """释放资源"""
        pass
