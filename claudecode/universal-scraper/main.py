#!/usr/bin/env python3
"""
Universal Scraper - 通用网站文章爬虫
用法: python main.py <command> [options]
"""

import sys
import os
import argparse

# 将项目根目录加入 Python 路径
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)


def check_dependencies(formats: list = None):
    """检查所需依赖是否安装"""
    missing = []

    # 必须依赖
    for pkg, import_name in [("requests", "requests"), ("beautifulsoup4", "bs4"), ("pyyaml", "yaml")]:
        try:
            __import__(import_name)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"[错误] 缺少必要依赖: {', '.join(missing)}")
        print(f"请运行: pip install {' '.join(missing)}")
        sys.exit(1)

    # 可选依赖（仅提示）
    optional_checks = {
        "pdf": ("playwright", "playwright"),
        "docx": ("python-docx", "docx"),
        "markdown": ("markdownify", "markdownify"),
    }

    if formats:
        for fmt in formats:
            if fmt in optional_checks:
                pkg, import_name = optional_checks[fmt]
                try:
                    __import__(import_name)
                except ImportError:
                    print(f"[提示] {fmt} 格式需要 {pkg}，请运行: pip install {pkg}")


def cmd_run(args):
    """运行爬取"""
    from core.scheduler import Scheduler, get_all_sites

    sites = get_all_sites() if args.site == "all" else [args.site]

    if not sites:
        print("[错误] 没有找到任何网站配置。请先创建配置文件或运行 interactive 命令。")
        return

    for site_name in sites:
        print(f"\n{'═' * 50}")
        print(f"  开始爬取: {site_name}")
        print(f"{'═' * 50}")

        try:
            scheduler = Scheduler(site_name, force=args.force)
            check_dependencies(
                scheduler.config.get("output", {}).get("formats",
                    scheduler.config.get("output_formats", ["pdf"]))
            )
            scheduler.run()
        except FileNotFoundError as e:
            print(f"[错误] {e}")
        except KeyboardInterrupt:
            print("\n[中断] 用户取消")
        except Exception as e:
            print(f"[错误] {e}")
        finally:
            if 'scheduler' in locals():
                scheduler.close()


def cmd_discover(args):
    """仅发现文章列表"""
    from core.scheduler import Scheduler

    try:
        scheduler = Scheduler(args.site)
        articles = scheduler.discover_only()

        print(f"\n发现的文章列表:")
        for i, (url, article) in enumerate(scheduler.task_manager.get_all().items(), 1):
            print(f"  {i}. [{article.get('category', '')}] {article['title']}")
            print(f"     {url}")
    except FileNotFoundError as e:
        print(f"[错误] {e}")
    finally:
        if 'scheduler' in locals():
            scheduler.close()


def cmd_retry(args):
    """重试失败任务"""
    from core.scheduler import Scheduler

    try:
        scheduler = Scheduler(args.site)
        scheduler.retry_failed()
    except FileNotFoundError as e:
        print(f"[错误] {e}")
    finally:
        if 'scheduler' in locals():
            scheduler.close()


def cmd_status(args):
    """查看状态统计"""
    from core.scheduler import Scheduler

    try:
        scheduler = Scheduler(args.site)
        stats = scheduler.get_status()

        name = scheduler.config.get("name", args.site)
        print(f"\n╔══════════════════════════════════════╗")
        print(f"║  {name}")
        print(f"╚══════════════════════════════════════╝")
        print(f"  总文章数:  {stats['total']}")
        print(f"  已完成:    {stats['completed']}")
        print(f"  失败:      {stats['failed']}")
        print(f"  待处理:    {stats['pending']}")
        print(f"  待更新:    {stats.get('needs_update', 0)}")

        categories = stats.get("categories", {})
        if categories:
            print(f"\n  分类明细:")
            for cat, cs in sorted(categories.items()):
                size_mb = cs['size'] / (1024 * 1024)
                size_str = f"{size_mb:.1f}MB" if size_mb >= 1 else f"{cs['size'] / 1024:.0f}KB"
                print(f"    {cat}: {cs['completed']}/{cs['total']} ({size_str})")
    except FileNotFoundError as e:
        print(f"[错误] {e}")
    finally:
        if 'scheduler' in locals():
            scheduler.close()


def cmd_report(args):
    """生成统计报告"""
    from core.scheduler import Scheduler

    try:
        scheduler = Scheduler(args.site)
        report = scheduler.generate_report()
        print(report)
    except FileNotFoundError as e:
        print(f"[错误] {e}")
    finally:
        if 'scheduler' in locals():
            scheduler.close()


def cmd_check_update(args):
    """检查文章更新"""
    from core.scheduler import Scheduler

    try:
        scheduler = Scheduler(args.site)
        scheduler.check_updates()
    except FileNotFoundError as e:
        print(f"[错误] {e}")
    finally:
        if 'scheduler' in locals():
            scheduler.close()


def cmd_interactive(args):
    """交互式模式"""
    from core.interactive import interactive_mode
    interactive_mode()


def cmd_list(args):
    """列出所有已配置的网站"""
    from core.scheduler import get_all_sites
    import yaml
    from pathlib import Path

    sites = get_all_sites()
    if not sites:
        print("没有找到任何网站配置。")
        print(f"配置文件目录: {os.path.join(PROJECT_ROOT, 'config', 'sites')}")
        return

    print(f"\n已配置的网站 ({len(sites)}个):")
    print("─" * 50)

    config_dir = os.path.join(PROJECT_ROOT, "config", "sites")
    for site in sorted(sites):
        config_path = os.path.join(config_dir, f"{site}.yaml")
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        name = config.get("name", site)
        base_url = config.get("base_url", "")
        formats = config.get("output", {}).get("formats", ["pdf"])
        print(f"  {site}")
        print(f"    名称: {name}")
        print(f"    URL:  {base_url}")
        print(f"    格式: {', '.join(formats)}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Universal Scraper - 通用网站文章爬虫",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python main.py interactive              # 交互式配置新网站
  python main.py run --site wna           # 爬取 WNA
  python main.py run --site all           # 爬取所有网站
  python main.py run --site wna --force   # 强制重新下载
  python main.py discover --site wna      # 仅发现文章列表
  python main.py retry --site wna         # 重试失败任务
  python main.py status --site wna        # 查看状态
  python main.py report --site wna        # 生成统计报告
  python main.py check-update --site wna  # 检查文章更新
  python main.py list                     # 列出所有网站
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # run
    p_run = subparsers.add_parser("run", help="运行爬取")
    p_run.add_argument("--site", required=True, help="网站名称 (对应 config/sites/ 下的文件名) 或 'all'")
    p_run.add_argument("--force", action="store_true", help="强制重新下载所有文章")
    p_run.set_defaults(func=cmd_run)

    # discover
    p_discover = subparsers.add_parser("discover", help="仅发现文章列表")
    p_discover.add_argument("--site", required=True, help="网站名称")
    p_discover.set_defaults(func=cmd_discover)

    # retry
    p_retry = subparsers.add_parser("retry", help="重试失败任务")
    p_retry.add_argument("--site", required=True, help="网站名称")
    p_retry.set_defaults(func=cmd_retry)

    # status
    p_status = subparsers.add_parser("status", help="查看下载状态")
    p_status.add_argument("--site", required=True, help="网站名称")
    p_status.set_defaults(func=cmd_status)

    # report
    p_report = subparsers.add_parser("report", help="生成统计报告")
    p_report.add_argument("--site", required=True, help="网站名称")
    p_report.set_defaults(func=cmd_report)

    # check-update
    p_update = subparsers.add_parser("check-update", help="检查文章是否有更新")
    p_update.add_argument("--site", required=True, help="网站名称")
    p_update.set_defaults(func=cmd_check_update)

    # interactive
    p_interactive = subparsers.add_parser("interactive", help="交互式配置新网站")
    p_interactive.set_defaults(func=cmd_interactive)

    # list
    p_list = subparsers.add_parser("list", help="列出所有已配置的网站")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    check_dependencies()
    args.func(args)


if __name__ == "__main__":
    main()
