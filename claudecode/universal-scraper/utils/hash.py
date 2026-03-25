"""内容哈希工具，用于变更检测"""

import hashlib
import re


def content_hash(html: str) -> str:
    """计算HTML内容的哈希值

    先提取纯文本（去除标签和多余空白），再计算SHA256。
    这样即使页面模板微调（不影响正文），哈希也不会变。
    """
    if not html:
        return ""
    # 去除HTML标签
    text = re.sub(r'<[^>]+>', ' ', html)
    # 去除多余空白
    text = re.sub(r'\s+', ' ', text).strip()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
