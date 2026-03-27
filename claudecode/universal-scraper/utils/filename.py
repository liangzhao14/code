"""文件名处理工具"""

import re
from urllib.parse import urlparse


def sanitize_filename(name: str, max_length: int = 150) -> str:
    """将名称转为合法文件名"""
    # 移除或替换非法字符
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    # 压缩多余空格
    name = re.sub(r'\s+', ' ', name).strip()
    # 移除首尾的点和空格
    name = name.strip('. ')
    # 限制长度
    if len(name) > max_length:
        name = name[:max_length].rstrip('. ')
    return name or "untitled"


def title_from_url(url: str) -> str:
    """从URL路径提取标题

    例: "/information-library/country/argentina" -> "Argentina"
    例: "/info/china-nuclear-power" -> "China Nuclear Power"
    """
    path = url.rstrip("/").split("?")[0].split("#")[0]
    slug = path.split("/")[-1] if "/" in path else path
    if not slug:
        return "untitled"
    title = slug.replace("-", " ").replace("_", " ").strip()
    return title.title()


def category_from_url(url: str, base_path: str = "", depth: int = 2) -> str:
    """从URL路径提取分类名

    Args:
        url: 文章URL
        base_path: 基础路径（会被去除），例如 "/information-library"
        depth: 取几级路径作为分类

    例: url="/information-library/country-profiles/countries-a-f/argentina"
        base_path="/information-library", depth=2
        -> "Country Profiles/Countries A F"
    """
    # 如果是完整URL，提取路径部分
    if url.startswith(("http://", "https://")):
        path = urlparse(url).path
    else:
        path = url
    path = path.rstrip("/").split("?")[0].split("#")[0]

    # 去除 base_path
    if base_path:
        base_path = base_path.rstrip("/")
        if path.lower().startswith(base_path.lower()):
            path = path[len(base_path):]

    parts = [p for p in path.strip("/").split("/") if p]

    # 去掉最后一段（文章本身的 slug）
    if len(parts) > 1:
        parts = parts[:-1]

    # 取指定深度
    parts = parts[:depth]

    if not parts:
        return "Uncategorized"

    # 格式化：连字符转空格，首字母大写
    formatted = [p.replace("-", " ").replace("_", " ").strip().title() for p in parts]
    return " - ".join(formatted)
