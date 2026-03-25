"""统一日志模块"""

import logging
import sys
from pathlib import Path


_initialized = False


def setup_logging(output_dir: str = None, level: int = logging.INFO):
    """初始化日志系统，同时输出到控制台和文件"""
    global _initialized
    if _initialized:
        return

    root_logger = logging.getLogger("scraper")
    root_logger.setLevel(level)
    root_logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    # 控制台输出
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)
    console.setFormatter(fmt)
    root_logger.addHandler(console)

    # 文件输出
    if output_dir:
        log_dir = Path(output_dir)
        log_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "scraper.log", encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(fmt)
        root_logger.addHandler(file_handler)

    _initialized = True


def get_logger(name: str = None) -> logging.Logger:
    """获取日志实例"""
    if name:
        return logging.getLogger(f"scraper.{name}")
    return logging.getLogger("scraper")
