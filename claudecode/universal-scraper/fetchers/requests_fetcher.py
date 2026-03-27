"""基于 requests 的轻量抓取器"""

import requests

from fetchers.base import BaseFetcher
from utils.logger import get_logger

logger = get_logger("requests_fetcher")


class RequestsFetcher(BaseFetcher):
    """使用 requests + Session 抓取静态页面"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        })
        # 预访问（获取cookies）
        pre_visit = config.get("fetch", {}).get("pre_visit")
        if pre_visit:
            try:
                logger.info(f"预访问获取cookies: {pre_visit}")
                self.session.get(pre_visit, timeout=self.timeout)
            except Exception as e:
                logger.warning(f"预访问失败: {e}")

    def fetch(self, url: str) -> tuple:
        """GET请求获取页面内容"""
        resp = self.session.get(url, timeout=self.timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text, resp.url

    def download_file(self, url: str, filepath: str) -> bool:
        """流式下载文件"""
        try:
            resp = self.session.get(url, timeout=self.timeout, stream=True)
            resp.raise_for_status()
            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(8192):
                    f.write(chunk)
            return True
        except Exception as e:
            logger.error(f"文件下载失败: {url} -> {e}")
            return False

    def close(self):
        self.session.close()
