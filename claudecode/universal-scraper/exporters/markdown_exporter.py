"""Markdown 导出器：将 HTML 转换为 Markdown"""

from datetime import datetime
from pathlib import Path

from exporters.base import BaseExporter
from utils.logger import get_logger

logger = get_logger("markdown_exporter")


class MarkdownExporter(BaseExporter):
    """将 HTML 转换为 Markdown"""

    def export(self, html_content: str, url: str, filepath: str) -> bool:
        try:
            from markdownify import markdownify as md
        except ImportError:
            raise RuntimeError("Markdown 导出需要 markdownify，请运行: pip install markdownify")

        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

        try:
            cleaned = self.clean_html(html_content, url)
            markdown = md(cleaned, heading_style="ATX", strip=["script", "style", "noscript"])

            # 清理多余空行
            lines = markdown.split("\n")
            cleaned_lines = []
            prev_empty = False
            for line in lines:
                is_empty = not line.strip()
                if is_empty and prev_empty:
                    continue
                cleaned_lines.append(line)
                prev_empty = is_empty
            markdown = "\n".join(cleaned_lines).strip()

            # 添加元信息头部
            header = f"""---
source: {url}
downloaded: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
---

"""
            content = header + markdown + "\n"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Markdown 导出失败: {url} -> {e}")
            return False

    def file_extension(self) -> str:
        return ".md"
