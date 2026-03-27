#!/usr/bin/env python3
"""Copy Word/PDF files that match instrument-related keywords.

Features:
1. Recursively scan multiple source directories.
2. Match by file name and, when possible, file content.
3. Deduplicate by file name.
4. Copy deduplicated files to a destination directory.
5. Write a CSV manifest with the chosen source path and file size in MB.
6. Merge multiple existing manifests without rescanning source files.

Notes:
- .docx content scanning uses only the Python standard library.
- .pdf content scanning requires `pypdf`. If unavailable, PDF files are matched
  by file name only.
- .doc content scanning is best-effort and may miss old binary Word files.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import contextlib
import csv
import html
import importlib.util
import io
import json
import os
import re
import shutil
import shutil as shutil_lib
import subprocess
import sys
import warnings
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


KEYWORD_EXPRESSIONS = [
    # --- 1. 核电/核设施基础核心词 ---
    "核电",
    "核设施",
    "核级",
    "核工程",
    "核动力",
    "核反应堆",
    "压水堆",
    "核电厂",
    "核动力厂",
    "核岛",
    "常规岛",
    # --- 2. 仪表与控制通用基础词 (针对工程类) ---
    "仪控",
    "仪表+控制",
    "仪器仪表",
    "自动化仪表",
    "测量与控制",
    "工业控制系统",
    "控制和监视系统",
    "热工控制",
    "热工测量",
    # --- 3. 核电仪控（I&C）核心专属词汇 (标准中最常出现) ---
    "核仪表",
    "辐射监测",
    "反应堆保护",
    "反应堆控制",
    "控制棒驱动",
    "安全级+仪表",       # 对应 Safety Class I&C
    "安全重要+系统",     # 对应 IEC/GB标准中的 Systems Important to Safety
    "专设安全设施",
    "主控室",
    "盘台",              # 仪控主控室盘台
    "堆芯测量",
    "全数字化控制系统",   # 核电DCS专属词
    "数字化控制系统",
    "核电+DCS",
    "人机接口",          # 核电仪控标准中的高频词 HMI
    # --- 4. 仪表设备与传感器实体词汇 ---
    "变送器",
    "探测器",
    "电磁阀",
    "热电偶",
    "流量计+核",
    "液位计+核",
    "贯穿件",            # 电气与仪控电缆穿越核安全壳的设备
    # --- 5. 核级仪控特有的标准/鉴定审查词汇 (筛选标准极有效) ---
    "环境鉴定",          # EQ (Environmental Qualification)
    "抗震鉴定",          # SQ (Seismic Qualification)
    "电磁兼容+核",       # EMC标准
    "软件验证与确认",    # 核电仪控软件专属高频词 (V&V)
    "纵深防御",
    "单一故障",
    # --- 6. 强关联组合检索表达式 ---
    "核电厂+仪表",
    "反应堆+控制系统",
    "核工业+自动化",
    "辐射+探测"
]
DEFAULT_EXTENSIONS = [".pdf", ".doc", ".docx"]
DEFAULT_EXECUTOR_MODE = "process"
DEFAULT_FALLBACK_EXECUTOR_MODE = "thread"
DEFAULT_WORKERS = 4
DEFAULT_PDF_TIMEOUT_SECONDS = 10


@dataclass
class MatchRecord:
    file_name: str
    source_path: Path
    file_size_bytes: int
    matched_by: str
    matched_keyword: str
    mtime: float

    @property
    def file_size_mb(self) -> float:
        return self.file_size_bytes / 1024 / 1024


@dataclass
class PdfIssueRecord:
    file_name: str
    source_path: Path
    issue_type: str
    issue_message: str


class ProgressBar:
    def __init__(self, total: int, enabled: bool = True) -> None:
        self.total = total
        self.enabled = enabled and total > 0
        self.current = 0

    def update(self, current: int, matched: int, kept: int) -> None:
        if not self.enabled:
            return
        self.current = current
        percent = current / self.total if self.total else 1.0
        term_width = shutil_lib.get_terminal_size(fallback=(100, 20)).columns
        suffix = f" {current}/{self.total} matched={matched} kept={kept}"
        bar_width = max(10, min(40, term_width - len(suffix) - 10))
        filled = int(bar_width * percent)
        bar = "#" * filled + "-" * (bar_width - filled)
        sys.stderr.write(f"\r[{bar}] {percent:6.2%}{suffix}")
        sys.stderr.flush()

    def finish(self) -> None:
        if not self.enabled:
            return
        sys.stderr.write("\n")
        sys.stderr.flush()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="按关键词筛选 Word/PDF 文件，按文件名去重后复制到目标目录。"
    )
    parser.add_argument(
        "--source",
        dest="sources",
        action="append",
        default=[],
        help="源目录。可重复传入多个，例如 --source /a --source /b",
    )
    parser.add_argument(
        "--merge-manifest",
        dest="merge_manifests",
        action="append",
        default=[],
        help="多 manifest 汇总模式：读取已有结果清单 CSV，按文件名合并去重并复制到目标目录。可重复传入。",
    )
    parser.add_argument(
        "--dest",
        default=None,
        help="目标目录。去重后的文件会平铺复制到该目录下。",
    )
    parser.add_argument(
        "--extensions",
        default=",".join(DEFAULT_EXTENSIONS),
        help="需要扫描的扩展名，逗号分隔，默认 .pdf,.doc,.docx",
    )
    parser.add_argument(
        "--dedupe-strategy",
        choices=["first", "largest", "newest"],
        default="largest",
        help="同名文件去重策略：first=首次命中，largest=保留更大文件，newest=保留最新修改文件。",
    )
    parser.add_argument(
        "--manifest",
        default=None,
        help="结果清单 CSV 路径。默认写到 <dest>/matched_files_manifest.csv",
    )
    parser.add_argument(
        "--pdf-issue-log",
        default=None,
        help="PDF 解析问题清单 CSV 路径。默认写到 <dest>/pdf_parse_issues.csv",
    )
    parser.add_argument(
        "--append-manifest",
        action="store_true",
        help="如果目标 manifest 已存在，则读取历史结果并按文件名跨批次合并去重。",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="打印扫描过程和跳过原因。",
    )
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="关闭终端进度条。",
    )
    parser.add_argument(
        "--pdf-worker",
        default=None,
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args()
    if args.pdf_worker:
        return args
    if not args.dest:
        parser.error("必须提供 --dest")
    if not args.sources and not args.merge_manifests:
        parser.error("至少提供一个 --source 或 --merge-manifest")
    return args


def normalize_extensions(raw_extensions: str) -> set[str]:
    result = set()
    for item in raw_extensions.split(","):
        item = item.strip().lower()
        if not item:
            continue
        if not item.startswith("."):
            item = f".{item}"
        result.add(item)
    return result


def parse_keyword_groups(raw_keywords: list[str]) -> list[tuple[str, list[str]]]:
    keyword_groups: list[tuple[str, list[str]]] = []
    for raw_keyword in raw_keywords:
        expression = raw_keyword.strip()
        if not expression:
            continue
        parts = [part.strip() for part in expression.split("+") if part.strip()]
        if not parts:
            continue
        keyword_groups.append((expression, parts))
    return keyword_groups


def find_first_keyword_group(
    text: str, keyword_groups: list[tuple[str, list[str]]]
) -> str | None:
    if not text:
        return None
    for expression, parts in keyword_groups:
        if all(part in text for part in parts):
            return expression
    return None


def iter_files(sources: Iterable[Path], extensions: set[str]) -> Iterable[Path]:
    seen: set[Path] = set()
    for source in sources:
        if not source.exists():
            continue
        if source.is_file():
            candidate = source.resolve()
            if candidate.suffix.lower() in extensions and candidate not in seen:
                seen.add(candidate)
                yield candidate
            continue
        for root, _, files in os.walk(source):
            root_path = Path(root)
            for file_name in files:
                candidate = (root_path / file_name).resolve()
                if candidate.suffix.lower() not in extensions:
                    continue
                if candidate in seen:
                    continue
                seen.add(candidate)
                yield candidate


def extract_docx_text(path: Path) -> str:
    try:
        chunks: list[str] = []
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if not name.startswith("word/") or not name.endswith(".xml"):
                    continue
                data = zf.read(name).decode("utf-8", errors="ignore")
                text = re.sub(r"<[^>]+>", " ", data)
                chunks.append(html.unescape(text))
        return " ".join(chunks)
    except Exception:
        return ""


def extract_doc_text_best_effort(path: Path) -> str:
    try:
        data = path.read_bytes()
    except Exception:
        return ""
    for encoding in ("utf-8", "gb18030", "utf-16-le", "utf-16-be", "latin1"):
        try:
            return data.decode(encoding, errors="ignore")
        except Exception:
            continue
    return ""


def extract_pdf_text(path: Path) -> str:
    if not importlib.util.find_spec("pypdf"):
        return ""
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        text_parts: list[str] = []
        for page in reader.pages:
            try:
                text_parts.append(page.extract_text() or "")
            except Exception:
                continue
        return "\n".join(text_parts)
    except Exception:
        return ""


def extract_pdf_text_safely(path: Path) -> tuple[str, str | None]:
    if not importlib.util.find_spec("pypdf"):
        return "", None

    stderr_buffer = io.StringIO()
    stdout_buffer = io.StringIO()
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with contextlib.redirect_stderr(stderr_buffer), contextlib.redirect_stdout(stdout_buffer):
                text = extract_pdf_text(path)
    except Exception as exc:
        return "", f"exception: {exc}"

    captured = "\n".join(
        part.strip()
        for part in [stderr_buffer.getvalue(), stdout_buffer.getvalue()]
        if part.strip()
    ).strip()

    if captured:
        return text, captured
    return text, None


def run_pdf_worker(path: Path) -> int:
    text, issue = extract_pdf_text_safely(path)
    json.dump(
        {
            "text": text,
            "issue": issue,
        },
        sys.stdout,
        ensure_ascii=False,
    )
    return 0


def extract_pdf_text_with_timeout(
    path: Path, timeout_seconds: int
) -> tuple[str, str | None]:
    worker_cmd = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--pdf-worker",
        str(path),
    ]
    try:
        result = subprocess.run(
            worker_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "", f"timeout: pdf parsing exceeded {timeout_seconds}s"
    except Exception as exc:
        return "", f"worker_exception: {exc}"

    stderr_text = result.stderr.strip()
    if result.returncode != 0:
        issue = stderr_text or f"worker_exit_code: {result.returncode}"
        return "", issue

    try:
        payload = json.loads(result.stdout or "{}")
    except Exception as exc:
        detail = stderr_text or (result.stdout or "").strip()[:200]
        issue = f"worker_invalid_output: {exc}"
        if detail:
            issue = f"{issue}; detail={detail}"
        return "", issue

    text = payload.get("text") or ""
    issue = payload.get("issue")
    if stderr_text:
        issue = f"{issue}; stderr={stderr_text}" if issue else f"stderr={stderr_text}"
    return text, issue


def match_file(
    path: Path, keyword_groups: list[tuple[str, list[str]]]
) -> tuple[MatchRecord | None, PdfIssueRecord | None]:
    file_name = path.name
    file_size = path.stat().st_size
    mtime = path.stat().st_mtime

    matched_keyword = find_first_keyword_group(file_name, keyword_groups)
    if matched_keyword:
        return (
            MatchRecord(
                file_name=file_name,
                source_path=path,
                file_size_bytes=file_size,
                matched_by="filename",
                matched_keyword=matched_keyword,
                mtime=mtime,
            ),
            None,
        )

    suffix = path.suffix.lower()
    content_text = ""
    matched_by = ""
    pdf_issue: PdfIssueRecord | None = None
    if suffix == ".docx":
        content_text = extract_docx_text(path)
        matched_by = "docx_content"
    elif suffix == ".pdf":
        content_text, pdf_issue_message = extract_pdf_text_with_timeout(
            path,
            DEFAULT_PDF_TIMEOUT_SECONDS,
        )
        matched_by = "pdf_content"
        if pdf_issue_message:
            issue_type = "pdf_parser_warning"
            if pdf_issue_message.startswith("timeout:"):
                issue_type = "pdf_parser_timeout"
            elif pdf_issue_message.startswith("worker_"):
                issue_type = "pdf_parser_error"
            pdf_issue = PdfIssueRecord(
                file_name=file_name,
                source_path=path,
                issue_type=issue_type,
                issue_message=pdf_issue_message,
            )
    elif suffix == ".doc":
        content_text = extract_doc_text_best_effort(path)
        matched_by = "doc_content_best_effort"

    matched_keyword = find_first_keyword_group(content_text, keyword_groups)
    if matched_keyword:
        return (
            MatchRecord(
                file_name=file_name,
                source_path=path,
                file_size_bytes=file_size,
                matched_by=matched_by,
                matched_keyword=matched_keyword,
                mtime=mtime,
            ),
            pdf_issue,
        )

    return None, pdf_issue


def process_candidate_file(
    path_str: str, keyword_groups: list[tuple[str, list[str]]]
) -> tuple[MatchRecord | None, PdfIssueRecord | None, str | None]:
    path = Path(path_str)
    try:
        record, pdf_issue = match_file(path, keyword_groups)
        return record, pdf_issue, None
    except Exception as exc:
        return None, None, str(exc)


def should_replace(existing: MatchRecord, candidate: MatchRecord, strategy: str) -> bool:
    if strategy == "first":
        return False
    if strategy == "largest":
        return candidate.file_size_bytes > existing.file_size_bytes
    if strategy == "newest":
        return candidate.mtime > existing.mtime
    return False


def write_manifest(manifest_path: Path, records: list[MatchRecord]) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "file_name",
                "source_path",
                "file_size_mb",
                "matched_by",
                "matched_keyword",
            ]
        )
        for record in records:
            writer.writerow(
                [
                    record.file_name,
                    str(record.source_path),
                    f"{record.file_size_mb:.3f}",
                    record.matched_by,
                    record.matched_keyword,
                ]
            )


def write_pdf_issue_log(issue_log_path: Path, records: list[PdfIssueRecord]) -> None:
    issue_log_path.parent.mkdir(parents=True, exist_ok=True)
    with issue_log_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["file_name", "source_path", "issue_type", "issue_message"])
        for record in records:
            writer.writerow(
                [
                    record.file_name,
                    str(record.source_path),
                    record.issue_type,
                    record.issue_message,
                ]
            )


def load_existing_records(
    manifest_path: Path, dest: Path, verbose: bool = False
) -> dict[str, MatchRecord]:
    if not manifest_path.exists():
        return {}

    records: dict[str, MatchRecord] = {}
    with manifest_path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            file_name = (row.get("file_name") or "").strip()
            source_path_raw = (row.get("source_path") or "").strip()
            if not file_name:
                continue

            source_path = Path(source_path_raw).expanduser() if source_path_raw else dest / file_name
            dest_path = dest / file_name
            file_size_bytes = 0
            mtime = 0.0

            try:
                if dest_path.exists():
                    stat = dest_path.stat()
                    file_size_bytes = stat.st_size
                    mtime = stat.st_mtime
                elif source_path.exists():
                    stat = source_path.stat()
                    file_size_bytes = stat.st_size
                    mtime = stat.st_mtime
                else:
                    file_size_mb = float(row.get("file_size_mb") or 0)
                    file_size_bytes = int(file_size_mb * 1024 * 1024)
            except Exception as exc:
                if verbose:
                    print(f"[WARN] load manifest row failed: {file_name} ({exc})", file=sys.stderr)
                continue

            records[file_name] = MatchRecord(
                file_name=file_name,
                source_path=source_path,
                file_size_bytes=file_size_bytes,
                matched_by=(row.get("matched_by") or "manifest").strip() or "manifest",
                matched_keyword=(row.get("matched_keyword") or "").strip(),
                mtime=mtime,
            )

    return records


def load_merge_manifest_records(
    manifest_paths: Iterable[Path], verbose: bool = False
) -> tuple[dict[str, MatchRecord], int]:
    merged: dict[str, MatchRecord] = {}
    loaded_rows = 0
    for manifest_path in manifest_paths:
        if not manifest_path.exists():
            if verbose:
                print(f"[WARN] merge manifest not found: {manifest_path}", file=sys.stderr)
            continue

        with manifest_path.open("r", newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                file_name = (row.get("file_name") or "").strip()
                source_path_raw = (row.get("source_path") or "").strip()
                if not file_name or not source_path_raw:
                    continue

                source_path = Path(source_path_raw).expanduser().resolve()
                try:
                    if source_path.exists():
                        stat = source_path.stat()
                        file_size_bytes = stat.st_size
                        mtime = stat.st_mtime
                    else:
                        file_size_mb = float(row.get("file_size_mb") or 0)
                        file_size_bytes = int(file_size_mb * 1024 * 1024)
                        mtime = 0.0
                except Exception as exc:
                    if verbose:
                        print(
                            f"[WARN] load merge manifest row failed: {manifest_path} / {file_name} ({exc})",
                            file=sys.stderr,
                        )
                    continue

                merged[file_name] = MatchRecord(
                    file_name=file_name,
                    source_path=source_path,
                    file_size_bytes=file_size_bytes,
                    matched_by=(row.get("matched_by") or f"merge_manifest:{manifest_path.name}").strip()
                    or f"merge_manifest:{manifest_path.name}",
                    matched_keyword=(row.get("matched_keyword") or "").strip(),
                    mtime=mtime,
                )
                loaded_rows += 1
    return merged, loaded_rows


def merge_record_maps(
    base_records: dict[str, MatchRecord],
    new_records: dict[str, MatchRecord],
    strategy: str,
) -> tuple[dict[str, MatchRecord], dict[str, MatchRecord]]:
    merged_records = dict(base_records)
    files_to_copy: dict[str, MatchRecord] = {}
    for file_name, record in new_records.items():
        existing = merged_records.get(file_name)
        if existing is None or should_replace(existing, record, strategy):
            merged_records[file_name] = record
            files_to_copy[file_name] = record
    return merged_records, files_to_copy


def ensure_missing_dest_files_are_copied(
    dest: Path,
    merged_records: dict[str, MatchRecord],
    files_to_copy: dict[str, MatchRecord],
) -> None:
    for file_name, record in merged_records.items():
        if file_name not in files_to_copy and not (dest / file_name).exists() and record.source_path.exists():
            files_to_copy[file_name] = record


def copy_records_to_dest(
    dest: Path,
    records: Iterable[MatchRecord],
    verbose: bool = False,
) -> int:
    copied_count = 0
    for record in records:
        if not record.source_path.exists():
            if verbose:
                print(f"[WARN] source missing, skip copy: {record.source_path}", file=sys.stderr)
            continue
        shutil.copy2(record.source_path, dest / record.file_name)
        copied_count += 1
    return copied_count


def run_merge_manifest_mode(
    args: argparse.Namespace,
    dest: Path,
    manifest_path: Path,
    pdf_issue_log_path: Path,
) -> int:
    merge_manifest_paths = [Path(p).expanduser().resolve() for p in args.merge_manifests]
    existing_records = (
        load_existing_records(manifest_path, dest, verbose=args.verbose)
        if args.append_manifest
        else {}
    )
    merge_records, loaded_rows = load_merge_manifest_records(merge_manifest_paths, verbose=args.verbose)
    merged_records, files_to_copy = merge_record_maps(existing_records, merge_records, args.dedupe_strategy)
    ensure_missing_dest_files_are_copied(dest, merged_records, files_to_copy)
    final_records = sorted(
        merged_records.values(),
        key=lambda x: (x.file_name.casefold(), str(x.source_path)),
    )
    copied_count = copy_records_to_dest(dest, files_to_copy.values(), verbose=args.verbose)
    write_manifest(manifest_path, final_records)
    write_pdf_issue_log(pdf_issue_log_path, [])

    print("模式: 多 manifest 汇总")
    print(f"读取 manifest 文件数: {len(merge_manifest_paths)}")
    print(f"读取 manifest 记录数: {loaded_rows}")
    print(f"去重后文件总数: {len(final_records)}")
    if args.append_manifest:
        print(f"合并历史清单记录数: {len(existing_records)}")
    print(f"本次复制文件数: {copied_count}")
    print(f"目标目录: {dest}")
    print(f"结果清单: {manifest_path}")
    print(f"PDF 问题日志: {pdf_issue_log_path}")
    print("本次存在 PDF 解析告警/错误的文件数: 0")
    print("执行模式: manifest_merge")
    print("并发数: 0")
    return 0


def main() -> int:
    args = parse_args()
    if args.pdf_worker:
        return run_pdf_worker(Path(args.pdf_worker).expanduser().resolve())

    sources = [Path(p).expanduser().resolve() for p in args.sources]
    dest = Path(args.dest).expanduser().resolve()
    keyword_groups = parse_keyword_groups(KEYWORD_EXPRESSIONS)
    extensions = normalize_extensions(args.extensions)
    manifest_path = (
        Path(args.manifest).expanduser().resolve()
        if args.manifest
        else dest / "matched_files_manifest.csv"
    )
    pdf_issue_log_path = (
        Path(args.pdf_issue_log).expanduser().resolve()
        if args.pdf_issue_log
        else dest / "pdf_parse_issues.csv"
    )

    dest.mkdir(parents=True, exist_ok=True)

    if args.merge_manifests and not args.sources:
        return run_merge_manifest_mode(args, dest, manifest_path, pdf_issue_log_path)

    candidate_files = list(iter_files(sources, extensions))
    has_pdf_candidate = any(path.suffix.lower() == ".pdf" for path in candidate_files)

    matched_by_name: dict[str, MatchRecord] = {}
    pdf_issue_records: list[PdfIssueRecord] = []
    scanned_files = 0
    matched_files = 0
    progress = ProgressBar(
        total=len(candidate_files),
        enabled=not args.no_progress and sys.stderr.isatty(),
    )

    def handle_result(
        path: Path,
        record: MatchRecord | None,
        pdf_issue: PdfIssueRecord | None,
        error_message: str | None,
    ) -> None:
        nonlocal scanned_files, matched_files
        scanned_files += 1
        if error_message is not None:
            if args.verbose:
                print(f"[WARN] scan failed: {path} ({error_message})", file=sys.stderr)
            progress.update(scanned_files, matched_files, len(matched_by_name))
            return

        if pdf_issue is not None:
            pdf_issue_records.append(pdf_issue)

        if record is None:
            if args.verbose:
                print(f"[SKIP] no keyword match: {path}")
            progress.update(scanned_files, matched_files, len(matched_by_name))
            return

        matched_files += 1
        existing = matched_by_name.get(record.file_name)
        if existing is None or should_replace(existing, record, args.dedupe_strategy):
            matched_by_name[record.file_name] = record
            if args.verbose:
                print(
                    f"[KEEP] {record.file_name} <- {record.source_path} "
                    f"({record.matched_by}, {record.matched_keyword})"
                )
        elif args.verbose:
            print(
                f"[DROP] duplicate by file name: {record.source_path} "
                f"(kept {existing.source_path})"
            )
        progress.update(scanned_files, matched_files, len(matched_by_name))

    actual_executor_mode = "serial"

    use_process_pool = DEFAULT_EXECUTOR_MODE == "process" and len(candidate_files) > 1
    if use_process_pool:
        try:
            with concurrent.futures.ProcessPoolExecutor(max_workers=DEFAULT_WORKERS) as executor:
                actual_executor_mode = "process"
                future_to_path = {
                    executor.submit(process_candidate_file, str(path), keyword_groups): path
                    for path in candidate_files
                }
                for future in concurrent.futures.as_completed(future_to_path):
                    path = future_to_path[future]
                    record, pdf_issue, error_message = future.result()
                    handle_result(path, record, pdf_issue, error_message)
        except (PermissionError, OSError) as exc:
            if args.verbose:
                print(
                    f"[WARN] process executor unavailable, fallback to {DEFAULT_FALLBACK_EXECUTOR_MODE}: {exc}",
                    file=sys.stderr,
                )

    if actual_executor_mode == "serial" and DEFAULT_FALLBACK_EXECUTOR_MODE == "thread" and len(candidate_files) > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=DEFAULT_WORKERS) as executor:
            actual_executor_mode = "thread"
            future_to_path = {
                executor.submit(process_candidate_file, str(path), keyword_groups): path
                for path in candidate_files
            }
            for future in concurrent.futures.as_completed(future_to_path):
                path = future_to_path[future]
                record, pdf_issue, error_message = future.result()
                handle_result(path, record, pdf_issue, error_message)

    if actual_executor_mode == "serial":
        for path in candidate_files:
            record, pdf_issue, error_message = process_candidate_file(str(path), keyword_groups)
            handle_result(path, record, pdf_issue, error_message)

    progress.finish()

    existing_records = (
        load_existing_records(manifest_path, dest, verbose=args.verbose)
        if args.append_manifest
        else {}
    )
    if args.append_manifest and args.verbose:
        print(f"[INFO] loaded existing manifest records: {len(existing_records)}")

    merged_records, files_to_copy = merge_record_maps(existing_records, matched_by_name, args.dedupe_strategy)
    ensure_missing_dest_files_are_copied(dest, merged_records, files_to_copy)

    final_records = sorted(
        merged_records.values(),
        key=lambda x: (x.file_name.casefold(), str(x.source_path)),
    )

    copied_count = copy_records_to_dest(dest, files_to_copy.values(), verbose=args.verbose)

    write_manifest(manifest_path, final_records)
    write_pdf_issue_log(pdf_issue_log_path, pdf_issue_records)

    print(f"扫描文件数: {scanned_files}")
    print(f"命中文件数（去重前）: {matched_files}")
    print(f"去重后文件总数: {len(final_records)}")
    if args.append_manifest:
        print(f"合并历史清单记录数: {len(existing_records)}")
        print(f"本次复制文件数: {copied_count}")
    else:
        print(f"本次复制文件数: {copied_count}")
    print(f"目标目录: {dest}")
    print(f"结果清单: {manifest_path}")
    print(f"PDF 问题日志: {pdf_issue_log_path}")
    print(f"本次存在 PDF 解析告警/错误的文件数: {len(pdf_issue_records)}")
    print(f"执行模式: {actual_executor_mode}")
    print(f"并发数: {DEFAULT_WORKERS}")

    if has_pdf_candidate and not importlib.util.find_spec("pypdf"):
        print(
            "Note: pypdf is not installed; PDF content matching is skipped, "
            "only PDF file names are matched.",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
