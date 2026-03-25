"""交互模式：引导用户分析新网站并生成配置"""

import re
from urllib.parse import urlparse, urljoin

import yaml
import requests
from bs4 import BeautifulSoup

from utils.logger import get_logger

logger = get_logger("interactive")

# 项目根目录
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent


def analyze_page(url: str) -> dict:
    """分析页面结构"""
    result = {
        "url": url,
        "title": "",
        "total_links": 0,
        "script_count": 0,
        "has_sitemap": False,
        "sitemap_url": "",
        "needs_js": False,
        "suggested_selectors": [],
        "link_patterns": {},
    }

    # 请求页面
    try:
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
    except Exception as e:
        logger.error(f"页面请求失败: {e}")
        return result

    soup = BeautifulSoup(resp.text, "html.parser")
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    # 基本信息
    title_tag = soup.find("title")
    result["title"] = title_tag.get_text(strip=True) if title_tag else ""
    result["total_links"] = len(soup.find_all("a", href=True))
    result["script_count"] = len(soup.find_all("script"))

    # JS 依赖检测
    body_text = soup.get_text(strip=True)
    if result["script_count"] > 5 and len(body_text) < 500:
        result["needs_js"] = True
    spa_markers = soup.select("#app, #root, #__nuxt, #__next")
    if spa_markers:
        result["needs_js"] = True

    # Sitemap 检测
    for path in ["/sitemap.xml", "/sitemap_index.xml", "/sitemap/"]:
        try:
            sitemap_resp = requests.head(urljoin(base, path), timeout=10, allow_redirects=True)
            if sitemap_resp.status_code == 200:
                result["has_sitemap"] = True
                result["sitemap_url"] = path
                break
        except Exception:
            pass

    # 链接模式分析
    patterns = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("#", "javascript:", "mailto:")):
            continue

        full_url = urljoin(url, href)
        if urlparse(full_url).netloc != parsed.netloc:
            continue

        # 提取路径模式
        path = urlparse(full_url).path
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            pattern = "/" + "/".join(parts[:2]) + "/"
            patterns[pattern] = patterns.get(pattern, 0) + 1

    # 按频率排序
    result["link_patterns"] = dict(sorted(patterns.items(), key=lambda x: -x[1])[:10])

    # 推荐选择器
    common_selectors = [
        ("article a[href]", "文章标签内的链接"),
        ("main a[href]", "主内容区的链接"),
        (".content a[href]", ".content 类的链接"),
        (".article-list a[href]", "文章列表的链接"),
        ("li a[href]", "列表项中的链接"),
    ]
    for selector, desc in common_selectors:
        found = soup.select(selector)
        if found:
            result["suggested_selectors"].append({
                "selector": selector,
                "description": desc,
                "count": len(found),
            })

    return result


def interactive_mode():
    """交互式引导用户配置新网站"""
    print("\n╔══════════════════════════════════════════╗")
    print("║  Universal Scraper - 交互式配置向导      ║")
    print("╚══════════════════════════════════════════╝\n")

    # 1. 输入URL
    url = input("请输入目标网站URL: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\n正在分析 {url} ...\n")
    analysis = analyze_page(url)

    # 展示分析结果
    print(f"  标题: {analysis['title']}")
    print(f"  链接总数: {analysis['total_links']}")
    print(f"  JS脚本数: {analysis['script_count']}")
    print(f"  需要JS渲染: {'是' if analysis['needs_js'] else '否'}")
    print(f"  Sitemap: {'发现 (' + analysis['sitemap_url'] + ')' if analysis['has_sitemap'] else '未发现'}")

    if analysis["link_patterns"]:
        print(f"\n  常见链接模式:")
        for i, (pattern, count) in enumerate(analysis["link_patterns"].items(), 1):
            print(f"    {i}. {pattern} ({count}个链接)")

    # 2. 选择发现方式
    print(f"\n请选择文章发现方式:")
    print("  1. CSS选择器 (从列表页提取链接)")
    print("  2. Sitemap (解析sitemap.xml)")
    print("  3. 递归爬取 (从入口页面递归发现)")
    if analysis["has_sitemap"]:
        print("  4. 选择器 + Sitemap (组合使用)")

    discovery_choice = input("\n选择 (1/2/3/4): ").strip()

    discovery_configs = []
    filter_pattern = ""

    if discovery_choice in ("1", "4"):
        # CSS 选择器
        if analysis["suggested_selectors"]:
            print(f"\n推荐的选择器:")
            for i, s in enumerate(analysis["suggested_selectors"], 1):
                print(f"  {i}. {s['selector']} - {s['description']} ({s['count']}个)")
            sel_choice = input(f"\n选择推荐的选择器 (1-{len(analysis['suggested_selectors'])}) 或输入自定义选择器: ").strip()
            try:
                idx = int(sel_choice) - 1
                link_selector = analysis["suggested_selectors"][idx]["selector"]
            except (ValueError, IndexError):
                link_selector = sel_choice
        else:
            link_selector = input("请输入链接CSS选择器 (如 a[href]): ").strip() or "a[href]"

        filter_pattern = input("请输入URL过滤正则 (留空不过滤): ").strip()
        start_path = urlparse(url).path or "/"

        discovery_configs.append({
            "type": "selector",
            "start_url": start_path,
            "link_selector": link_selector,
            "filter_pattern": filter_pattern,
        })

    if discovery_choice in ("2", "4"):
        sitemap_url = analysis.get("sitemap_url", "/sitemap.xml")
        if not filter_pattern:
            filter_pattern = input("请输入URL过滤正则 (留空不过滤): ").strip()
        discovery_configs.append({
            "type": "sitemap",
            "url": sitemap_url,
            "filter_pattern": filter_pattern,
        })

    if discovery_choice == "3":
        max_depth = input("最大爬取深度 (默认3): ").strip()
        max_depth = int(max_depth) if max_depth.isdigit() else 3
        filter_pattern = input("请输入文章URL正则 (留空不过滤): ").strip()

        discovery_configs.append({
            "type": "recursive",
            "start_url": urlparse(url).path or "/",
            "filter_pattern": filter_pattern,
            "max_depth": max_depth,
            "max_pages": 500,
        })

    # 3. 选择输出格式
    print(f"\n请选择输出格式 (多选，用逗号分隔):")
    print("  1. PDF")
    print("  2. DOCX")
    print("  3. Markdown")
    print("  4. HTML")
    fmt_choice = input("选择 (如 1,3): ").strip()
    fmt_map = {"1": "pdf", "2": "docx", "3": "markdown", "4": "html"}
    formats = [fmt_map.get(c.strip(), "") for c in fmt_choice.split(",")]
    formats = [f for f in formats if f] or ["pdf"]

    # 4. 其他配置
    concurrency = input("并发数 (默认2): ").strip()
    concurrency = int(concurrency) if concurrency.isdigit() else 2

    delay = input("请求间隔秒数 (默认2): ").strip()
    delay = float(delay) if delay else 2.0

    # 5. 网站名称
    parsed = urlparse(url)
    default_name = parsed.netloc.replace("www.", "").split(".")[0]
    site_name = input(f"网站配置名称 (默认 {default_name}): ").strip() or default_name

    # 6. 生成配置
    config = {
        "name": analysis.get("title", site_name),
        "base_url": f"{parsed.scheme}://{parsed.netloc}",
        "output_dir": f"{site_name}_data",
        "discovery": discovery_configs,
        "fetch": {
            "mode": "playwright" if analysis["needs_js"] else "auto",
        },
        "clean_selectors": [
            "header", "nav", "footer",
            ".cookie-banner", ".cookie-consent",
            ".sidebar", ".popup", ".modal",
        ],
        "pagination": {"enabled": False},
        "output": {
            "formats": formats,
            "category_from": "url_path",
            "category_depth": 2,
        },
    }

    # 如果需要 JS，提示并发建议降低
    if analysis["needs_js"]:
        config["concurrency"] = min(concurrency, 2)
        config["fetch"]["mode"] = "playwright"
    else:
        config["concurrency"] = concurrency

    config["delay"] = delay

    # 保存配置
    config_path = PROJECT_ROOT / "config" / "sites" / f"{site_name}.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"\n配置已保存: {config_path}")
    print(f"\n生成的配置内容:")
    print("─" * 40)
    with open(config_path, "r", encoding="utf-8") as f:
        print(f.read())
    print("─" * 40)

    # 询问是否立即运行
    run_now = input("\n是否立即开始爬取? (y/n): ").strip().lower()
    if run_now in ("y", "yes", "是"):
        from core.scheduler import Scheduler
        scheduler = Scheduler(site_name)
        try:
            scheduler.run()
        finally:
            scheduler.close()
