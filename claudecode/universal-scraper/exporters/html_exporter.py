"""HTML 导出器：保存清理后的原始 HTML"""

from datetime import datetime
from pathlib import Path

from exporters.base import BaseExporter
from utils.logger import get_logger

logger = get_logger("html_exporter")


class HtmlExporter(BaseExporter):
    """保存清理后的原始 HTML"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

        try:
            cleaned = self.clean_html(html_content, url)

            # 注入 base 标签和来源信息
            meta = f"""<!--
  来源: {url}
  下载时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-->
<base href="{url}">
"""
            # 在 <head> 后插入 meta
            if "<head>" in cleaned.lower():
                idx = cleaned.lower().index("<head>") + len("<head>")
                cleaned = cleaned[:idx] + "\n" + meta + cleaned[idx:]
            else:
                cleaned = meta + cleaned

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned)
            return True
        except Exception as e:
            logger.error(f"HTML 导出失败: {url} -> {e}")
            return False

    def file_extension(self) -> str:
        return ".html"
