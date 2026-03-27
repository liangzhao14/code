#!/usr/bin/env python3
"""
文件下载脚本
用法:
  python downloader.py <URL> [URL2] [URL3] ...
  python downloader.py -f links.txt         # 从文件读取链接
  python downloader.py -o ./downloads <URL> # 指定输出目录
"""

import sys
import os
import argparse
import urllib.request
import urllib.parse
from pathlib import Path


def get_filename_from_url(url: str, response_headers=None) -> str:
    """从 URL 或响应头中提取文件名"""
    # 优先从 Content-Disposition 头获取
    if response_headers:
        content_disposition = response_headers.get("Content-Disposition", "")
        if "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[-1].strip().strip('"').strip("'")
            if filename:
                return filename

    # 从 URL 路径提取
    parsed = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(parsed.path)
    filename = os.path.basename(path)

    if not filename or "." not in filename:
        filename = "downloaded_file"

    return filename


def print_progress(downloaded: int, total: int):
    """打印进度条"""
    if total:
        percent = downloaded / total * 100
        bar_len = 40
        filled = int(bar_len * downloaded / total)
        bar = "#" * filled + "-" * (bar_len - filled)
        size_str = f"{downloaded/1024/1024:.2f}/{total/1024/1024:.2f} MB"
        print(f"\r  [{bar}] {percent:5.1f}%  {size_str}", end="", flush=True)
    else:
        print(f"\r  已下载: {downloaded/1024/1024:.2f} MB", end="", flush=True)


def supports_range(url: str) -> bool:
    """发送 HEAD 请求，检查服务器是否支持 Range 断点续传"""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.headers.get("Accept-Ranges", "none").lower() != "none"
    except Exception:
        return False


def download_file(url: str, output_dir: Path) -> bool:
    """下载单个文件，支持断点续传，显示进度"""
    print(f"\n正在下载: {url}")

    try:
        # 先用 HEAD 请求获取文件名和是否支持续传
        head_req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(head_req, timeout=10) as head_resp:
            filename = get_filename_from_url(url, dict(head_resp.headers))
            can_resume = head_resp.headers.get("Accept-Ranges", "none").lower() != "none"

        dest = output_dir / filename
        part = dest.with_suffix(dest.suffix + ".part")

        # 已完成的文件直接跳过
        if dest.exists():
            print(f"  已存在，跳过: {dest}")
            return True

        # 计算已下载的字节数（续传起点）
        resume_pos = part.stat().st_size if (can_resume and part.exists()) else 0

        headers = {"User-Agent": "Mozilla/5.0"}
        if resume_pos:
            headers["Range"] = f"bytes={resume_pos}-"
            print(f"  从 {resume_pos/1024/1024:.2f} MB 处续传...")

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            # 206 Partial Content 表示服务器接受了 Range 请求
            status = response.status
            if resume_pos and status != 206:
                # 服务器不支持续传，重头下载
                resume_pos = 0
                print("  服务器不支持续传，重新下载...")

            total_in_response = int(response.headers.get("Content-Length", 0))
            total = resume_pos + total_in_response  # 文件完整大小
            downloaded = resume_pos
            chunk_size = 65536  # 64 KB

            open_mode = "ab" if resume_pos else "wb"
            with open(part, open_mode) as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    print_progress(downloaded, total)

        # 下载完成，将 .part 重命名为正式文件
        part.rename(dest)
        print(f"\n  保存至: {dest}")
        return True

    except urllib.error.HTTPError as e:
        print(f"\n  HTTP 错误 {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"\n  连接失败: {e.reason}")
    except KeyboardInterrupt:
        print(f"\n  已暂停，下次运行将从断点续传")
        raise
    except Exception as e:
        print(f"\n  下载出错: {e}")

    return False


def main():
    parser = argparse.ArgumentParser(description="文件下载工具")
    parser.add_argument("urls", nargs="*", help="要下载的 URL")
    parser.add_argument("-f", "--file", help="包含 URL 列表的文本文件（每行一个）")
    parser.add_argument("-o", "--output", default="downloads", help="保存目录（默认 downloads/）")
    args = parser.parse_args()

    urls = list(args.urls)

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"错误: 找不到文件 {args.file}")
            sys.exit(1)
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    urls.append(line)

    if not urls:
        parser.print_help()
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    success, fail = 0, 0
    for url in urls:
        if download_file(url, output_dir):
            success += 1
        else:
            fail += 1

    print(f"\n完成: 成功 {success} 个，失败 {fail} 个")


if __name__ == "__main__":
    main()
