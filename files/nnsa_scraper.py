#!/usr/bin/env python3
"""
国家核安全局 法规标准文件库 爬虫脚本 v3
网址: https://nnsa.mee.gov.cn/ztzl/fgbzwjk/

核心发现:
  1. 文件列表通过 iframe 加载: /govsearch/haqj.jsp?Stype=2&type=1&channelid=XXXXX
  2. 各分类通过 channelid 参数区分
  3. iframe 内翻页通过 JS 函数 goPage(n) 实现

方案: 用 Playwright 直接访问 iframe URL，逐个 channelid 抓取，处理翻页
"""

import os
import re
import time
import json
import logging
from pathlib import Path
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

BASE_URL = "https://nnsa.mee.gov.cn/ztzl/fgbzwjk/"
IFRAME_URL = "https://nnsa.mee.gov.cn/govsearch/haqj.jsp?Stype=2&type=1"
SAVE_DIR = Path("nnsa_data")
DELAY = 2

# 从主页HTML提取的 channelid 映射
CATEGORIES = {
    "国家法律": 33636,
    "行政法规": 33637,
    "规章": 33638,
    "规范性文件": 33639,
    "核安全导则-通用系列导则": 33736,
    "核安全导则-核动力厂系列导则": 33643,
    "核安全导则-研究堆系列导则": 33644,
    "核安全导则-非堆核燃料循环设施系列导则": 33742,
    "核安全导则-放射性废物管理系列导则": 33741,
    "核安全导则-核材料管制系列导则": 33740,
    "核安全导则-民用核安全设备监督管理系列导则": 33739,
    "核安全导则-放射性物品运输管理系列导则": 33743,
    "标准-通用系列": 33729,
    "标准-核动力厂系列": 33730,
    "标准-研究堆系列": 33731,
    "标准-放射性废物管理系列": 33732,
    "标准-放射性物品运输管理系列": 33733,
    "标准-放射性同位素和射线装置监督管理系列": 33734,
    "标准-辐射环境系列": 33735,
    "国际公约": 33642,
}


def scrape_with_playwright():
    """使用 Playwright 逐个访问 iframe URL，提取文件列表并处理翻页。"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        logger.error("请先安装: pip install playwright && playwright install chromium")
        return

    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        page = context.new_page()

        # 先访问主页获取cookies
        logger.info("访问主页获取cookies...")
        page.goto(BASE_URL, wait_until="networkidle", timeout=60000)
        time.sleep(2)

        for cat_name, channel_id in CATEGORIES.items():
            cat_items = []
            page_num = 1
            url = f"{IFRAME_URL}&channelid={channel_id}"
            logger.info(f"\n===== 抓取: {cat_name} (channelid={channel_id}) =====")

            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                time.sleep(DELAY)

                while True:
                    # 提取当前页的文档链接
                    items = page.evaluate("""() => {
                        const results = [];
                        // 查找文档列表中的链接
                        const links = document.querySelectorAll('a[href]');
                        for (const a of links) {
                            const href = a.href || '';
                            const text = (a.textContent || '').trim();
                            if (!text || text.length < 2) continue;
                            // 匹配 PDF 或文章页面
                            if (href.endsWith('.pdf') || /\/t\\d+_\\d+\\.s?html/.test(href)) {
                                results.push({title: text.substring(0, 200), url: href});
                            }
                        }
                        return results;
                    }""")

                    if not items:
                        # 备用: 尝试更宽松的选择器
                        items = page.evaluate("""() => {
                            const results = [];
                            const links = document.querySelectorAll('.xxgk_list a, .list a, .result-list a, table a, li a');
                            for (const a of links) {
                                const href = a.href || '';
                                const text = (a.textContent || '').trim();
                                if (!text || text.length < 2) continue;
                                if (href.includes('nnsa.mee.gov.cn') || href.includes('mee.gov.cn')) {
                                    if (href.endsWith('.pdf') || /\/t\\d+_\\d+\\.s?html/.test(href) || /\\d{6}\//.test(href)) {
                                        results.push({title: text.substring(0, 200), url: href});
                                    }
                                }
                            }
                            return results;
                        }""")

                    if items:
                        for item in items:
                            clean_url = item["url"].split("?")[0]
                            item["type"] = "pdf" if clean_url.endswith(".pdf") else "html"
                        cat_items.extend(items)
                        logger.info(f"  第{page_num}页: 找到 {len(items)} 条")
                    else:
                        if page_num == 1:
                            # 第一页就没数据，保存HTML供调试
                            debug_html = SAVE_DIR / f"debug_{channel_id}.html"
                            with open(debug_html, "w", encoding="utf-8") as f:
                                f.write(page.content())
                            logger.warning(f"  第1页未找到文档，已保存调试HTML: {debug_html}")
                        break

                    # 尝试翻页: 检查 ui-paging-container 中的"下一页"按钮
                    has_next = page.evaluate("""() => {
                        const btn = document.querySelector('.js-page-next');
                        if (btn && !btn.classList.contains('ui-pager-disabled')) {
                            return true;
                        }
                        return false;
                    }""")

                    if not has_next:
                        break

                    page_num += 1
                    # 通过JS点击"下一页"，避免元素遮挡问题
                    page.evaluate("""() => {
                        const btn = document.querySelector('.js-page-next');
                        if (btn) btn.click();
                    }""")

                    time.sleep(DELAY)
                    try:
                        page.wait_for_load_state("networkidle", timeout=15000)
                    except:
                        time.sleep(2)

            except Exception as e:
                logger.error(f"  出错: {e}")

            # 去重
            seen = set()
            unique = []
            for item in cat_items:
                if item["url"] not in seen:
                    seen.add(item["url"])
                    unique.append(item)
            results[cat_name] = unique
            logger.info(f"  {cat_name}: 共 {len(unique)} 个唯一文件")

        browser.close()

    save_results(results)
    return results


def sanitize_filename(title):
    """将标题转为合法文件名"""
    # 移除或替换非法字符
    name = re.sub(r'[\\/:*?"<>|]', '_', title)
    # 移除多余空格
    name = re.sub(r'\s+', ' ', name).strip()
    # 限制长度（Windows路径限制）
    if len(name) > 150:
        name = name[:150]
    return name


def download_all():
    """批量下载所有文件为PDF格式，用标题命名"""
    import requests
    from playwright.sync_api import sync_playwright

    json_file = SAVE_DIR / "nnsa_regulations.json"
    if not json_file.exists():
        logger.error(f"未找到 {json_file}，请先运行抓取")
        return

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    pdf_dir = SAVE_DIR / "pdfs"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0", "Referer": BASE_URL})

    # 统计
    downloaded, skipped, failed = 0, 0, 0

    # 分离 PDF 和 HTML 文件
    pdf_tasks = []
    html_tasks = []
    for cat_name, items in data.items():
        cat_dir = pdf_dir / cat_name.replace("-", "_")
        cat_dir.mkdir(parents=True, exist_ok=True)
        for item in items:
            url = item.get("url", "")
            title = item.get("title", "未命名")
            clean_url = url.split("?")[0]
            filename = sanitize_filename(title) + ".pdf"
            filepath = cat_dir / filename
            if filepath.exists():
                skipped += 1
                continue
            if clean_url.endswith(".pdf"):
                pdf_tasks.append((url, title, filepath))
            else:
                html_tasks.append((url, title, filepath))

    logger.info(f"待下载: PDF {len(pdf_tasks)} 个, HTML转PDF {len(html_tasks)} 个, 已跳过 {skipped} 个")

    # 1. 下载PDF文件（用requests直接下载）
    if pdf_tasks:
        logger.info(f"\n--- 下载PDF文件 ---")
        for url, title, filepath in pdf_tasks:
            try:
                logger.info(f"  下载: {title}")
                resp = session.get(url, timeout=60, stream=True)
                resp.raise_for_status()
                with open(filepath, "wb") as f:
                    for chunk in resp.iter_content(8192):
                        f.write(chunk)
                downloaded += 1
                time.sleep(0.5)
            except Exception as e:
                logger.error(f"  失败: {title} -> {e}")
                failed += 1

    # 2. HTML文章转PDF（用Playwright渲染后导出）
    if html_tasks:
        logger.info(f"\n--- HTML文章转PDF ---")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
                viewport={"width": 1200, "height": 900},
            )
            page = context.new_page()

            for url, title, filepath in html_tasks:
                try:
                    logger.info(f"  转PDF: {title}")
                    page.goto(url, wait_until="networkidle", timeout=30000)
                    time.sleep(1)
                    page.pdf(
                        path=str(filepath),
                        format="A4",
                        margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
                        print_background=True,
                    )
                    downloaded += 1
                    time.sleep(0.5)
                except Exception as e:
                    logger.error(f"  失败: {title} -> {e}")
                    failed += 1

            browser.close()

    logger.info(f"\n下载完成 - 成功: {downloaded}, 跳过: {skipped}, 失败: {failed}")


def save_results(results):
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    with open(SAVE_DIR / "nnsa_regulations.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    total = 0
    with open(SAVE_DIR / "nnsa_regulations.txt", "w", encoding="utf-8") as f:
        for cat, items in results.items():
            f.write(f"\n{'=' * 60}\n分类: {cat} ({len(items)} 项)\n{'=' * 60}\n\n")
            for item in items:
                f.write(f"  {item.get('title', '')}\n  {item.get('url', '')}\n\n")
                total += 1
    logger.info(f"结果已保存到 {SAVE_DIR}/，共 {total} 个文件")


if __name__ == "__main__":
    print("""
+-------------------------------------------------------+
|  国家核安全局 法规标准文件库 爬虫 v3                  |
+-------------------------------------------------------+
|  1. 抓取文件列表 (Playwright, 推荐先运行)             |
|  2. 下载所有文件为PDF (用标题命名)                    |
|  3. 全部执行 (抓取 + 下载)                            |
+-------------------------------------------------------+
    """)
    c = input("选择 (1/2/3): ").strip()
    if c == "1":
        scrape_with_playwright()
    elif c == "2":
        download_all()
    elif c == "3":
        results = scrape_with_playwright()
        if results:
            download_all()
    else:
        print("无效选择")
