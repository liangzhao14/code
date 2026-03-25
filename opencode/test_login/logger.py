import logging
import os
from logging.handlers import RotatingFileHandler
from config import LOG_CONFIG

def setup_logger(name):
    """设置日志记录器"""
    # 创建logger
    logger = logging.getLogger(name)
    
    if logger.hasHandlers():  # 避免重复添加handler
        return logger
    
    logger.setLevel(getattr(logging, LOG_CONFIG['log_level']))
    
    # 创建formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 控制台handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件handler (带日志轮转)
    log_file_path = os.path.join(os.path.dirname(__file__), LOG_CONFIG['log_file'])
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=LOG_CONFIG['max_file_size'],
        backupCount=LOG_CONFIG['backup_count'],
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# 创建通用logger
logger = setup_logger(__name__)