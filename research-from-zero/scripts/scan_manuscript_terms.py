#!/usr/bin/env python3
"""Scan manuscript/project text for internal names and report-like phrasing."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".tex",
    ".rst",
    ".qmd",
    ".bib",
}

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "env",
}

PATTERNS = [
    ("date_or_run_stamp", re.compile(r"\b20\d{6,8}\b")),
    ("version_model_name", re.compile(r"\b(?:latest|forward|inverse|raw|final|mixed)\d+\b", re.I)),
    ("solver_status_code", re.compile(r"\b(?:accepted|status|ok)\d+\b", re.I)),
    ("dataset_nickname", re.compile(r"\b(?:test|all|lhs|outer|expand|external)\d+(?:[_-]\d+)?\b", re.I)),
    ("named_ablation_code", re.compile(r"\bS\d+_[A-Za-z][A-Za-z0-9]*\b")),
    ("local_path", re.compile(r"(?:[A-Za-z]:\\[^\s]+|/home/[^\s]+|/Users/[^\s]+|\\\\[A-Za-z0-9._$-]+\\[^\s]+)")),
    ("figure_as_subject", re.compile(r"^\s*(?:Figure|Fig\.|图)\s*\d+[^。.!?]{0,80}(?:show|shows|display|displays|展示|显示|比较|给出)", re.I)),
    ("report_transition", re.compile(r"(?:然后|接下来|我们先|本文先|该图用于|可以看出|it can be seen)", re.I)),
    ("provenance_word", re.compile(r"\b(?:checkpoint|provenance|script|folder|package|source_data|preview|debug)\b", re.I)),
]


def iter_files(root: Path, recursive: bool, max_bytes: int):
    if root.is_file():
        paths = [root]
    elif recursive:
        paths = [p for p in root.rglob("*") if p.is_file()]
    else:
        paths = [p for p in root.iterdir() if p.is_file()]

    for path in paths:
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            if path.stat().st_size > max_bytes:
                continue
        except OSError:
            continue
        yield path


def scan_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            text = path.read_text(encoding="gb18030", errors="replace")

    for lineno, line in enumerate(text.splitlines(), start=1):
        for category, pattern in PATTERNS:
            for match in pattern.finditer(line):
                context = line.strip()
                if len(context) > 180:
                    start = max(match.start() - 60, 0)
                    context = context[start : start + 180]
                yield {
                    "file": str(path),
                    "line": lineno,
                    "category": category,
                    "match": match.group(0),
                    "context": context,
                }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="manuscript file or project folder to scan")
    parser.add_argument("--no-recursive", action="store_true", help="only scan top-level files")
    parser.add_argument("--max-bytes", type=int, default=2_000_000, help="skip files larger than this")
    parser.add_argument("--limit", type=int, default=500, help="maximum findings to print")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    writer = csv.DictWriter(sys.stdout, fieldnames=["file", "line", "category", "match", "context"])
    writer.writeheader()
    count = 0
    for file_path in iter_files(root, recursive=not args.no_recursive, max_bytes=args.max_bytes):
        for row in scan_file(file_path):
            writer.writerow(row)
            count += 1
            if count >= args.limit:
                return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
