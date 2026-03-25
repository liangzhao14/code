"""导出器模块

支持四种格式: pdf / docx / markdown / html
"""

from exporters.base import BaseExporter
from exporters.pdf_exporter import PdfExporter
from exporters.docx_exporter import DocxExporter
from exporters.markdown_exporter import MarkdownExporter
from exporters.html_exporter import HtmlExporter
from utils.logger import get_logger

logger = get_logger("exporter")

EXPORTER_MAP = {
    "pdf": PdfExporter,
    "docx": DocxExporter,
    "markdown": MarkdownExporter,
    "html": HtmlExporter,
}


def create_exporters(config: dict) -> list:
    """根据配置创建所有需要的导出器"""
    formats = config.get("output", {}).get("formats", config.get("output_formats", ["pdf"]))
    exporters = []
    for fmt in formats:
        fmt = fmt.lower().strip()
        cls = EXPORTER_MAP.get(fmt)
        if cls:
            exporters.append(cls(config))
            logger.info(f"导出格式: {fmt}")
        else:
            logger.warning(f"未知的导出格式: {fmt}，可选: {', '.join(EXPORTER_MAP.keys())}")
    return exporters
