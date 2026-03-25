#!/usr/bin/env python3
"""
World Nuclear Association 信息库爬虫
网址: https://world-nuclear.org/information-library
功能: 爬取信息库所有文章，保存为PDF文件
"""

import os
import re
import time
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

BASE_URL = "https://world-nuclear.org"
SAVE_DIR = Path("wna_data")
DELAY = 2  # 请求间隔(秒)，避免被封

# 信息库文章完整列表（从网站提取）
ARTICLES = {
    "Facts and Figures": [
        "/Information-Library/Facts-and-Figures/nuclear-generation-by-country",
        "/information-library/facts-and-figures/uranium-production-by-country",
        "/information-library/facts-and-figures/world-nuclear-power-reactors-and-uranium-requireme",
        "/information-library/facts-and-figures/reactor-database-2025-update-and-guide",
        "/information-library/facts-and-figures/nuclear-glossary",
    ],
    "Country Profiles - A-F": [
        "/information-library/country-profiles/countries-a-f/argentina",
        "/information-library/country-profiles/countries-a-f/armenia",
        "/information-library/country-profiles/countries-a-f/australia",
        "/information-library/country-profiles/countries-a-f/bangladesh",
        "/information-library/country-profiles/countries-a-f/belarus",
        "/information-library/country-profiles/countries-a-f/belgium",
        "/information-library/country-profiles/countries-a-f/brazil",
        "/information-library/country-profiles/countries-a-f/bulgaria",
        "/information-library/country-profiles/countries-a-f/canada-nuclear-power",
        "/information-library/country-profiles/countries-a-f/canada-uranium",
        "/information-library/country-profiles/countries-a-f/china-nuclear-fuel-cycle",
        "/information-library/country-profiles/countries-a-f/china-nuclear-power",
        "/information-library/country-profiles/countries-a-f/czech-republic",
        "/information-library/country-profiles/countries-a-f/denmark",
        "/information-library/country-profiles/countries-a-f/egypt",
        "/information-library/country-profiles/countries-a-f/estonia",
        "/information-library/country-profiles/countries-a-f/finland",
        "/information-library/country-profiles/countries-a-f/france",
    ],
    "Country Profiles - G-N": [
        "/information-library/country-profiles/countries-g-n/germany",
        "/information-library/country-profiles/countries-g-n/hungary",
        "/information-library/country-profiles/countries-g-n/india",
        "/information-library/country-profiles/countries-g-n/nuclear-power-in-indonesia",
        "/information-library/country-profiles/countries-g-n/iran",
        "/information-library/country-profiles/countries-g-n/italy",
        "/information-library/country-profiles/countries-g-n/japan-nuclear-fuel-cycle",
        "/information-library/country-profiles/countries-g-n/japan-nuclear-power",
        "/information-library/country-profiles/countries-g-n/jordan",
        "/information-library/country-profiles/countries-g-n/kazakhstan",
        "/information-library/country-profiles/countries-g-n/kyrgyzstan",
        "/information-library/country-profiles/countries-g-n/lithuania",
        "/information-library/country-profiles/countries-g-n/mexico",
        "/information-library/country-profiles/countries-g-n/mongolia",
        "/information-library/country-profiles/countries-g-n/namibia",
        "/information-library/country-profiles/countries-g-n/netherlands",
        "/information-library/country-profiles/countries-g-n/new-zealand",
        "/information-library/country-profiles/countries-g-n/niger",
    ],
    "Country Profiles - O-S": [
        "/information-library/country-profiles/countries-o-s/pakistan",
        "/information-library/country-profiles/countries-o-s/philippines",
        "/information-library/country-profiles/countries-o-s/poland",
        "/information-library/country-profiles/countries-o-s/romania",
        "/information-library/country-profiles/countries-o-s/russia-nuclear-fuel-cycle",
        "/Information-Library/Country-Profiles/Countries-O-S/Russia-Nuclear-Power",
        "/information-library/country-profiles/countries-o-s/saudi-arabia",
        "/information-library/country-profiles/countries-o-s/slovakia",
        "/information-library/country-profiles/countries-o-s/slovenia",
        "/information-library/country-profiles/countries-o-s/south-africa",
        "/information-library/country-profiles/countries-o-s/south-korea",
        "/information-library/country-profiles/countries-o-s/spain",
        "/information-library/country-profiles/countries-o-s/sweden",
        "/information-library/country-profiles/countries-o-s/switzerland",
    ],
    "Country Profiles - T-Z": [
        "/information-library/country-profiles/countries-t-z/tajikistan",
        "/information-library/country-profiles/countries-t-z/turkey",
        "/information-library/country-profiles/countries-t-z/ukraine",
        "/information-library/country-profiles/countries-t-z/ukraine-russia-war-and-nuclear-energy",
        "/information-library/country-profiles/countries-t-z/united-arab-emirates",
        "/information-library/country-profiles/countries-t-z/united-kingdom",
        "/information-library/country-profiles/countries-t-z/usa-nuclear-fuel-cycle",
        "/information-library/country-profiles/countries-t-z/usa-nuclear-power",
        "/information-library/country-profiles/countries-t-z/usa-nuclear-power-policy",
        "/information-library/country-profiles/countries-t-z/us-uranium-mining",
        "/information-library/country-profiles/countries-t-z/uzbekistan",
        "/information-library/country-profiles/countries-t-z/vietnam",
    ],
    "Country Profiles - Others": [
        "/information-library/country-profiles/others/asias-nuclear-energy-growth",
        "/information-library/country-profiles/others/californias-electricity",
        "/information-library/country-profiles/others/emerging-nuclear-energy-countries",
        "/information-library/country-profiles/others/european-union",
        "/information-library/country-profiles/others/nuclear-power-in-taiwan",
        "/information-library/country-profiles/others/uranium-in-africa",
    ],
    "Nuclear Fuel Cycle - Introduction": [
        "/information-library/nuclear-fuel-cycle/introduction/nuclear-fuel-cycle-overview",
        "/information-library/nuclear-fuel-cycle/introduction/what-is-uranium-how-does-it-work",
        "/information-library/nuclear-fuel-cycle/introduction/physics-of-nuclear-energy",
    ],
    "Nuclear Fuel Cycle - Uranium Resources": [
        "/information-library/nuclear-fuel-cycle/uranium-resources/uranium-markets",
        "/information-library/nuclear-fuel-cycle/uranium-resources/supply-of-uranium",
        "/information-library/nuclear-fuel-cycle/uranium-resources/geology-of-uranium-deposits",
        "/information-library/nuclear-fuel-cycle/uranium-resources/military-warheads-as-a-source-of-nuclear-fuel",
        "/information-library/nuclear-fuel-cycle/uranium-resources/uranium-and-depleted-uranium",
        "/information-library/nuclear-fuel-cycle/uranium-resources/uranium-from-phosphates",
        "/information-library/nuclear-fuel-cycle/uranium-resources/uranium-from-rare-earths-deposits",
        "/information-library/nuclear-fuel-cycle/uranium-resources/the-cosmic-origins-of-uranium",
    ],
    "Nuclear Fuel Cycle - Mining": [
        "/information-library/nuclear-fuel-cycle/mining-of-uranium/world-uranium-mining-production",
        "/information-library/nuclear-fuel-cycle/mining-of-uranium/uranium-mining-overview",
        "/information-library/nuclear-fuel-cycle/mining-of-uranium/in-situ-leach-mining-of-uranium",
        "/information-library/nuclear-fuel-cycle/mining-of-uranium/environmental-aspects-of-uranium-mining",
    ],
    "Nuclear Fuel Cycle - Conversion Enrichment Fabrication": [
        "/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/conversion-and-deconversion",
        "/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment",
        "/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/fuel-fabrication",
        "/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/high-assay-low-enriched-uranium-haleu",
    ],
    "Nuclear Fuel Cycle - Fuel Recycling": [
        "/information-library/nuclear-fuel-cycle/fuel-recycling/processing-of-used-nuclear-fuel",
        "/information-library/nuclear-fuel-cycle/fuel-recycling/mixed-oxide-fuel-mox",
        "/information-library/nuclear-fuel-cycle/fuel-recycling/plutonium",
    ],
    "Nuclear Fuel Cycle - Nuclear Waste": [
        "/information-library/nuclear-fuel-cycle/nuclear-waste/radioactive-waste-management",
        "/information-library/nuclear-fuel-cycle/nuclear-waste/treatment-and-conditioning-of-nuclear-wastes",
        "/information-library/nuclear-fuel-cycle/nuclear-waste/storage-and-disposal-of-radioactive-waste",
        "/information-library/nuclear-fuel-cycle/nuclear-waste/international-nuclear-waste-disposal-concepts",
        "/information-library/nuclear-fuel-cycle/nuclear-waste/radioactive-wastes-myths-and-realities",
        "/information-library/nuclear-fuel-cycle/nuclear-waste/decommissioning-nuclear-facilities",
    ],
    "Nuclear Fuel Cycle - Transport": [
        "/information-library/nuclear-fuel-cycle/transport-of-nuclear-materials/transport-of-radioactive-materials",
        "/information-library/nuclear-fuel-cycle/transport-of-nuclear-materials/japanese-waste-and-mox-shipments-from-europe",
    ],
    "Safety and Security - Safety of Plants": [
        "/information-library/safety-and-security/safety-of-plants/safety-of-nuclear-power-reactors",
        "/information-library/safety-and-security/safety-of-plants/chernobyl-accident",
        "/information-library/safety-and-security/safety-of-plants/fukushima-daiichi-accident",
        "/information-library/safety-and-security/safety-of-plants/liability-for-nuclear-damage",
        "/information-library/safety-and-security/safety-of-plants/nuclear-power-plants-and-earthquakes",
        "/information-library/safety-and-security/safety-of-plants/three-mile-island-accident",
        "/information-library/safety-and-security/safety-of-plants/tokaimura-criticality-accident",
    ],
    "Safety and Security - Radiation and Health": [
        "/information-library/safety-and-security/radiation-and-health/radiation-and-health-effects",
        "/information-library/safety-and-security/radiation-and-health/occupational-safety-in-uranium-mining",
        "/information-library/safety-and-security/radiation-and-health/naturally-occurring-radioactive-materials-norm",
    ],
    "Safety and Security - Non-Proliferation": [
        "/information-library/safety-and-security/non-proliferation/safeguards-to-prevent-nuclear-proliferation",
        "/information-library/safety-and-security/non-proliferation/hiroshima-nagasaki-and-subsequent-weapons-testin",
    ],
    "Safety and Security - Security": [
        "/information-library/safety-and-security/security/security-of-nuclear-facilities-and-material",
    ],
    "Energy and the Environment": [
        "/information-library/energy-and-the-environment/clean-coal-technologies",
        "/information-library/energy-and-the-environment/climate-change-the-science",
        "/information-library/energy-and-the-environment/carbon-dioxide-emissions-from-electricity",
        "/information-library/energy-and-the-environment/electric-vehicles",
        "/information-library/energy-and-the-environment/energiewende",
        "/information-library/energy-and-the-environment/energy-return-on-investment",
        "/information-library/energy-and-the-environment/hydrogen-production-and-uses",
        "/information-library/energy-and-the-environment/mineral-requirements-for-electricity-generation",
        "/information-library/energy-and-the-environment/nuclear-energy-and-sustainable-development",
        "/information-library/energy-and-the-environment/policy-responses-to-climate-change",
        "/information-library/energy-and-the-environment/renewable-energy-and-electricity",
    ],
    "Economic Aspects": [
        "/information-library/economic-aspects/economics-of-nuclear-power",
        "/information-library/economic-aspects/energy-subsidies",
        "/information-library/economic-aspects/externalities-of-electricity-generation",
        "/information-library/economic-aspects/financing-nuclear-energy",
        "/information-library/economic-aspects/nuclear-power-and-energy-security",
    ],
    "Nuclear Power Reactors": [
        "/information-library/nuclear-power-reactors/overview/nuclear-power-reactors",
        "/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactors",
        "/information-library/nuclear-power-reactors/other/advanced-nuclear-power-reactors",
        "/information-library/nuclear-power-reactors/other/heavy-manufacturing-of-power-plants",
        "/information-library/nuclear-power-reactors/other/generation-iv-nuclear-reactors",
        "/information-library/nuclear-power-reactors/other/molten-salt-reactors",
    ],
    "Current and Future Generation": [
        "/information-library/current-and-future-generation/iea-scenarios-and-the-outlook-for-nuclear-power",
        "/information-library/current-and-future-generation/nuclear-energy-and-public-opinion",
        "/information-library/current-and-future-generation/nuclear-fusion-power",
        "/information-library/current-and-future-generation/nuclear-power-in-the-world-today",
        "/information-library/current-and-future-generation/outline-history-of-nuclear-energy",
        "/information-library/current-and-future-generation/plans-for-new-reactors-worldwide",
        "/information-library/current-and-future-generation/the-nuclear-debate",
        "/information-library/current-and-future-generation/thorium",
        "/information-library/current-and-future-generation/world-energy-needs-and-nuclear-power",
        "/information-library/current-and-future-generation/accelerator-driven-nuclear-energy",
        "/information-library/current-and-future-generation/cooling-power-plants",
        "/information-library/current-and-future-generation/cooperation-in-nuclear-power",
        "/information-library/current-and-future-generation/covid-19-coronavirus-and-nuclear-energy",
        "/information-library/current-and-future-generation/electricity-and-energy-storage",
        "/information-library/current-and-future-generation/electricity-transmission-grids",
        "/information-library/current-and-future-generation/fast-neutron-reactors",
        "/information-library/current-and-future-generation/international-framework-for-nuclear-energy-coopera",
        "/information-library/current-and-future-generation/lithium",
    ],
    "Non-power Nuclear Applications": [
        "/information-library/non-power-nuclear-applications/overview/the-many-uses-of-nuclear-technology",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/radioisotopes-in-consumer-products",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/radioisotopes-in-food-agriculture",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/radioisotopes-in-industry",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/radioisotopes-in-medicine",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/radioisotopes-in-water-resources-the-environment",
        "/information-library/non-power-nuclear-applications/radioisotopes-research/research-reactors",
        "/information-library/non-power-nuclear-applications/industry/nuclear-desalination",
        "/information-library/non-power-nuclear-applications/industry/nuclear-process-heat-for-industry",
        "/information-library/non-power-nuclear-applications/industry/peaceful-nuclear-explosions",
        "/information-library/non-power-nuclear-applications/transport/nuclear-reactors-for-space",
        "/information-library/non-power-nuclear-applications/transport/nuclear-powered-ships",
    ],
}


def sanitize_filename(name):
    """将名称转为合法文件名"""
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = re.sub(r'\s+', ' ', name).strip()
    if len(name) > 150:
        name = name[:150]
    return name


def get_title_from_path(path):
    """从URL路径提取标题"""
    slug = path.rstrip("/").split("/")[-1]
    title = slug.replace("-", " ").title()
    return title


def count_total_articles():
    """统计文章总数"""
    return sum(len(urls) for urls in ARTICLES.values())


def scrape_article_list():
    """保存文章列表到JSON（用于记录和断点续传）"""
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    article_list = []
    for cat, urls in ARTICLES.items():
        for url_path in urls:
            article_list.append({
                "category": cat,
                "title": get_title_from_path(url_path),
                "url": BASE_URL + url_path,
                "path": url_path,
            })

    json_file = SAVE_DIR / "wna_articles.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(article_list, f, ensure_ascii=False, indent=2)
    logger.info(f"文章列表已保存: {json_file}，共 {len(article_list)} 篇")
    return article_list


def download_as_pdf():
    """使用 Playwright 将所有文章页面渲染为PDF"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        logger.error("请先安装: pip install playwright && playwright install chromium")
        return

    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    pdf_dir = SAVE_DIR / "pdfs"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    # 加载或生成文章列表
    json_file = SAVE_DIR / "wna_articles.json"
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            article_list = json.load(f)
    else:
        article_list = scrape_article_list()

    total = len(article_list)
    downloaded, skipped, failed = 0, 0, 0
    failed_list = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()

        for idx, article in enumerate(article_list, 1):
            cat = article["category"]
            title = article["title"]
            url = article["url"]

            # 创建分类目录
            cat_dir = pdf_dir / sanitize_filename(cat)
            cat_dir.mkdir(parents=True, exist_ok=True)

            filename = sanitize_filename(title) + ".pdf"
            filepath = cat_dir / filename

            if filepath.exists():
                skipped += 1
                logger.info(f"  [{idx}/{total}] 跳过(已存在): {title}")
                continue

            try:
                logger.info(f"  [{idx}/{total}] 下载: {title}")
                logger.info(f"    URL: {url}")
                page.goto(url, wait_until="networkidle", timeout=60000)
                time.sleep(1)

                # 移除导航栏、页脚等干扰元素，只保留正文
                page.evaluate("""() => {
                    const selectors = [
                        'header', 'nav', 'footer',
                        '.site-header', '.site-footer', '.site-nav',
                        '.cookie-banner', '.cookie-consent',
                        '.sidebar', '.nav-bar', '.top-bar',
                        '#cookie-notice', '.popup', '.modal',
                        '.share-buttons', '.social-share',
                    ];
                    for (const sel of selectors) {
                        document.querySelectorAll(sel).forEach(el => el.remove());
                    }
                }""")

                page.pdf(
                    path=str(filepath),
                    format="A4",
                    margin={"top": "1.5cm", "bottom": "1.5cm", "left": "1.5cm", "right": "1.5cm"},
                    print_background=True,
                )
                downloaded += 1
                time.sleep(DELAY)

            except Exception as e:
                logger.error(f"    失败: {title} -> {e}")
                failed += 1
                failed_list.append({"title": title, "url": url, "error": str(e)})

        browser.close()

    # 保存失败记录
    if failed_list:
        fail_file = SAVE_DIR / "wna_failed.json"
        with open(fail_file, "w", encoding="utf-8") as f:
            json.dump(failed_list, f, ensure_ascii=False, indent=2)
        logger.info(f"失败记录已保存: {fail_file}")

    logger.info(f"\n下载完成 - 成功: {downloaded}, 跳过: {skipped}, 失败: {failed}, 总计: {total}")


def retry_failed():
    """重试之前失败的下载"""
    fail_file = SAVE_DIR / "wna_failed.json"
    if not fail_file.exists():
        logger.info("没有找到失败记录文件，无需重试")
        return

    with open(fail_file, "r", encoding="utf-8") as f:
        failed_list = json.load(f)

    if not failed_list:
        logger.info("没有需要重试的文章")
        return

    logger.info(f"准备重试 {len(failed_list)} 篇失败文章...")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        logger.error("请先安装: pip install playwright && playwright install chromium")
        return

    pdf_dir = SAVE_DIR / "pdfs"
    # 从完整列表中找到分类信息
    json_file = SAVE_DIR / "wna_articles.json"
    cat_map = {}
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            for a in json.load(f):
                cat_map[a["url"]] = a["category"]

    still_failed = []
    success = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()

        for item in failed_list:
            title = item["title"]
            url = item["url"]
            cat = cat_map.get(url, "Uncategorized")
            cat_dir = pdf_dir / sanitize_filename(cat)
            cat_dir.mkdir(parents=True, exist_ok=True)
            filepath = cat_dir / (sanitize_filename(title) + ".pdf")

            try:
                logger.info(f"  重试: {title}")
                page.goto(url, wait_until="networkidle", timeout=60000)
                time.sleep(2)
                page.evaluate("""() => {
                    const selectors = ['header','nav','footer','.site-header','.site-footer',
                        '.cookie-banner','.cookie-consent','.sidebar','.popup','.modal',
                        '.share-buttons','.social-share'];
                    for (const sel of selectors) {
                        document.querySelectorAll(sel).forEach(el => el.remove());
                    }
                }""")
                page.pdf(
                    path=str(filepath),
                    format="A4",
                    margin={"top": "1.5cm", "bottom": "1.5cm", "left": "1.5cm", "right": "1.5cm"},
                    print_background=True,
                )
                success += 1
                time.sleep(DELAY)
            except Exception as e:
                logger.error(f"    再次失败: {title} -> {e}")
                still_failed.append({"title": title, "url": url, "error": str(e)})

        browser.close()

    # 更新失败记录
    with open(fail_file, "w", encoding="utf-8") as f:
        json.dump(still_failed, f, ensure_ascii=False, indent=2)

    logger.info(f"重试完成 - 成功: {success}, 仍失败: {len(still_failed)}")


if __name__ == "__main__":
    total = count_total_articles()
    print(f"""
+-------------------------------------------------------+
|  World Nuclear Association 信息库爬虫                 |
|  网址: https://world-nuclear.org/information-library  |
+-------------------------------------------------------+
|  共 {total} 篇文章待处理                              |
+-------------------------------------------------------+
|  1. 生成文章列表 (保存JSON)                           |
|  2. 下载所有文章为PDF                                 |
|  3. 全部执行 (生成列表 + 下载PDF)                     |
|  4. 重试失败的下载                                    |
+-------------------------------------------------------+
    """)
    c = input("选择 (1/2/3/4): ").strip()
    if c == "1":
        scrape_article_list()
    elif c == "2":
        download_as_pdf()
    elif c == "3":
        scrape_article_list()
        download_as_pdf()
    elif c == "4":
        retry_failed()
    else:
        print("无效选择")
