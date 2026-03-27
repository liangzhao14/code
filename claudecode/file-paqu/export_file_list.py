#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import argparse
from datetime import datetime

try:
    from openpyxl import Workbook
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False


def format_size(size_bytes):
    """将字节大小格式化为易读形式"""
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024


def parse_extensions(ext_string):
    """
    解析后缀参数
    输入示例: ".txt,.pdf,.docx" 或 "txt,pdf,docx"
    输出: {".txt", ".pdf", ".docx"}
    """
    if not ext_string:
        return None

    exts = set()
    for ext in ext_string.split(","):
        ext = ext.strip().lower()
        if not ext:
            continue
        if not ext.startswith("."):
            ext = "." + ext
        exts.add(ext)

    return exts if exts else None


def collect_files(folder_path, recursive=True, extensions=None):
    """采集文件信息"""
    file_list = []
    total_size = 0
    total_count = 0

    if recursive:
        walker = os.walk(folder_path)
        for root, dirs, files in walker:
            for file_name in files:
                full_path = os.path.join(root, file_name)

                if extensions:
                    _, ext = os.path.splitext(file_name)
                    if ext.lower() not in extensions:
                        continue

                try:
                    stat = os.stat(full_path)
                    size = stat.st_size
                    mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

                    file_list.append({
                        "文件名": file_name,
                        "完整路径": full_path,
                        "所在目录": root,
                        "文件大小(B)": size,
                        "文件大小(可读)": format_size(size),
                        "修改时间": mtime
                    })

                    total_count += 1
                    total_size += size

                except Exception as e:
                    file_list.append({
                        "文件名": file_name,
                        "完整路径": full_path,
                        "所在目录": root,
                        "文件大小(B)": "获取失败",
                        "文件大小(可读)": "获取失败",
                        "修改时间": f"获取失败: {e}"
                    })
    else:
        for file_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(full_path):
                continue

            if extensions:
                _, ext = os.path.splitext(file_name)
                if ext.lower() not in extensions:
                    continue

            try:
                stat = os.stat(full_path)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

                file_list.append({
                    "文件名": file_name,
                    "完整路径": full_path,
                    "所在目录": folder_path,
                    "文件大小(B)": size,
                    "文件大小(可读)": format_size(size),
                    "修改时间": mtime
                })

                total_count += 1
                total_size += size

            except Exception as e:
                file_list.append({
                    "文件名": file_name,
                    "完整路径": full_path,
                    "所在目录": folder_path,
                    "文件大小(B)": "获取失败",
                    "文件大小(可读)": "获取失败",
                    "修改时间": f"获取失败: {e}"
                })

    return file_list, total_count, total_size


def export_to_csv(file_list, output_file):
    """导出 CSV"""
    headers = ["文件名", "完整路径", "所在目录", "文件大小(B)", "文件大小(可读)", "修改时间"]
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(file_list)


def export_to_xlsx(file_list, output_file):
    """导出 XLSX"""
    if not OPENPYXL_AVAILABLE:
        raise ImportError("未安装 openpyxl，请先执行: pip install openpyxl")

    wb = Workbook()
    ws = wb.active
    ws.title = "文件列表"

    headers = ["文件名", "完整路径", "所在目录", "文件大小(B)", "文件大小(可读)", "修改时间"]
    ws.append(headers)

    for item in file_list:
        ws.append([
            item["文件名"],
            item["完整路径"],
            item["所在目录"],
            item["文件大小(B)"],
            item["文件大小(可读)"],
            item["修改时间"]
        ])

    # 简单设置列宽
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 80
    ws.column_dimensions["C"].width = 50
    ws.column_dimensions["D"].width = 15
    ws.column_dimensions["E"].width = 18
    ws.column_dimensions["F"].width = 22

    wb.save(output_file)


def main():
    parser = argparse.ArgumentParser(description="扫描文件夹内文件并导出为 Excel 或 CSV")
    parser.add_argument("folder", help="要扫描的目录，例如: /data/files")
    parser.add_argument("-o", "--output", default="file_list.xlsx", help="输出文件名，默认 file_list.xlsx")
    parser.add_argument(
        "-f", "--format",
        choices=["xlsx", "csv"],
        default="xlsx",
        help="输出格式：xlsx 或 csv，默认 xlsx"
    )
    parser.add_argument(
        "-e", "--extensions",
        help='按后缀筛选，例如: ".txt,.pdf,.docx" 或 "txt,pdf,docx"'
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="不递归子目录，只扫描当前目录"
    )

    args = parser.parse_args()

    folder_path = os.path.abspath(args.folder)
    recursive = not args.no_recursive
    extensions = parse_extensions(args.extensions)

    if not os.path.exists(folder_path):
        print(f"错误：目录不存在 -> {folder_path}")
        return

    if not os.path.isdir(folder_path):
        print(f"错误：这不是一个目录 -> {folder_path}")
        return

    print(f"开始扫描目录: {folder_path}")
    print(f"是否递归: {'是' if recursive else '否'}")
    if extensions:
        print(f"后缀筛选: {', '.join(sorted(extensions))}")
    else:
        print("后缀筛选: 无")

    file_list, total_count, total_size = collect_files(
        folder_path=folder_path,
        recursive=recursive,
        extensions=extensions
    )

    if args.format == "csv":
        if not args.output.lower().endswith(".csv"):
            args.output += ".csv"
        export_to_csv(file_list, args.output)
    else:
        if not args.output.lower().endswith(".xlsx"):
            args.output += ".xlsx"
        export_to_xlsx(file_list, args.output)

    print("\n导出完成")
    print(f"文件总数: {total_count}")
    print(f"文件总大小: {total_size} Bytes ({format_size(total_size)})")
    print(f"输出文件: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()