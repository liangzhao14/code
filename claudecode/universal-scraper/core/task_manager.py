"""任务管理器：状态记录、断点续传、变更检测"""

import json
from datetime import datetime
from pathlib import Path

from utils.logger import get_logger

logger = get_logger("task_manager")


class TaskManager:
    """管理爬取任务状态

    数据存储在 {output_dir}/tasks.json
    状态流转: pending → downloading → completed / failed
              completed → needs_update → downloading → completed
    """

    def __init__(self, output_dir: str, site_name: str):
        self.output_dir = Path(output_dir)
        self.site_name = site_name
        self.db_path = self.output_dir / "tasks.json"
        self.data = {
            "site": site_name,
            "last_run": None,
            "articles": {},
        }
        self.load()

    def load(self):
        """加载现有任务记录"""
        if self.db_path.exists():
            try:
                with open(self.db_path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                logger.info(f"加载任务记录: {self.db_path} (已有{len(self.data.get('articles', {}))}条)")
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"任务记录加载失败，将创建新记录: {e}")

    def save(self):
        """保存任务记录"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.data["last_run"] = datetime.now().isoformat()
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def add_article(self, url: str, title: str, category: str = ""):
        """添加新文章，已存在的不覆盖"""
        articles = self.data.setdefault("articles", {})
        if url not in articles:
            articles[url] = {
                "title": title,
                "category": category,
                "status": "pending",
                "content_hash": "",
                "last_downloaded": None,
                "file_paths": [],
                "file_size": 0,
                "error": None,
                "retry_count": 0,
            }
            return True
        return False

    def get_status(self, url: str) -> str:
        """获取任务状态"""
        article = self.data.get("articles", {}).get(url)
        return article["status"] if article else "unknown"

    def set_status(self, url: str, status: str, **kwargs):
        """更新任务状态"""
        article = self.data.get("articles", {}).get(url)
        if not article:
            return
        article["status"] = status
        if status == "completed":
            article["last_downloaded"] = datetime.now().isoformat()
            article["error"] = None
        elif status == "failed":
            article["retry_count"] = article.get("retry_count", 0) + 1
        for key, value in kwargs.items():
            if key in article:
                article[key] = value

    def update_hash(self, url: str, new_hash: str):
        """更新内容哈希"""
        article = self.data.get("articles", {}).get(url)
        if article:
            article["content_hash"] = new_hash

    def check_update(self, url: str, new_hash: str) -> bool:
        """对比哈希，返回是否有变更"""
        article = self.data.get("articles", {}).get(url)
        if not article:
            return True  # 新文章，视为有变更
        old_hash = article.get("content_hash", "")
        if not old_hash:
            return True  # 没有历史哈希，视为有变更
        return old_hash != new_hash

    def get_pending(self) -> list:
        """获取待处理任务（pending + failed + needs_update）"""
        result = []
        for url, article in self.data.get("articles", {}).items():
            if article["status"] in ("pending", "failed", "needs_update"):
                result.append({"url": url, **article})
        return result

    def get_stats(self) -> dict:
        """统计信息"""
        stats = {"total": 0, "completed": 0, "failed": 0, "pending": 0, "needs_update": 0}
        category_stats = {}

        for url, article in self.data.get("articles", {}).items():
            stats["total"] += 1
            status = article["status"]
            stats[status] = stats.get(status, 0) + 1

            cat = article.get("category", "Uncategorized")
            if cat not in category_stats:
                category_stats[cat] = {"total": 0, "completed": 0, "failed": 0, "size": 0}
            category_stats[cat]["total"] += 1
            if status == "completed":
                category_stats[cat]["completed"] += 1
                category_stats[cat]["size"] += article.get("file_size", 0)
            elif status == "failed":
                category_stats[cat]["failed"] += 1

        stats["categories"] = category_stats
        return stats

    def get_all(self) -> dict:
        """获取所有任务记录"""
        return self.data.get("articles", {})

    def reset_failed(self):
        """将所有failed重置为pending"""
        count = 0
        for url, article in self.data.get("articles", {}).items():
            if article["status"] == "failed":
                article["status"] = "pending"
                article["error"] = None
                count += 1
        if count:
            logger.info(f"已将 {count} 个失败任务重置为待处理")
        return count

    def generate_report(self) -> str:
        """生成 Markdown 格式的统计报告"""
        stats = self.get_stats()
        lines = []
        lines.append(f"# {self.site_name} 下载统计报告\n")
        lines.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"> 数据目录: `{self.output_dir}`\n")
        lines.append("---\n")

        # 总览
        lines.append("## 总览\n")
        lines.append("| 项目 | 数值 |")
        lines.append("|------|------|")
        lines.append(f"| 文章总数 | {stats['total']} |")
        lines.append(f"| 下载成功 | {stats['completed']} |")
        lines.append(f"| 下载失败 | {stats['failed']} |")
        lines.append(f"| 待处理 | {stats['pending']} |")
        lines.append(f"| 待更新 | {stats.get('needs_update', 0)} |")
        lines.append("")

        # 分类统计
        categories = stats.get("categories", {})
        if categories:
            lines.append("## 分类统计\n")
            lines.append("| 分类 | 总数 | 成功 | 失败 | 大小 |")
            lines.append("|------|------|------|------|------|")
            for cat, cs in sorted(categories.items()):
                size_mb = cs['size'] / (1024 * 1024)
                size_str = f"{size_mb:.1f} MB" if size_mb >= 1 else f"{cs['size'] / 1024:.0f} KB"
                lines.append(f"| {cat} | {cs['total']} | {cs['completed']} | {cs['failed']} | {size_str} |")
            lines.append("")

        # 失败列表
        failed = [(url, a) for url, a in self.get_all().items() if a["status"] == "failed"]
        if failed:
            lines.append("## 失败列表\n")
            lines.append("| 标题 | 错误信息 |")
            lines.append("|------|----------|")
            for url, a in failed:
                lines.append(f"| {a['title']} | {a.get('error', 'unknown')} |")
            lines.append("")

        return "\n".join(lines)
