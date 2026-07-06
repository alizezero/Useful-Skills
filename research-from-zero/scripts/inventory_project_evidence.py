#!/usr/bin/env python3
"""List candidate evidence files for project-to-paper work.

This is a non-interpretive file finder. It does not judge paper role,
evidence strength, novelty, or confidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".txt", ".tex", ".rst", ".qmd", ".bib"}
TABLE_EXTENSIONS = {".csv", ".tsv"}
DATA_EXTENSIONS = {".json", ".jsonl", ".parquet", ".xlsx", ".xls", ".npz", ".npy", ".pkl"}
FIGURE_EXTENSIONS = {".svg", ".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}
LOG_EXTENSIONS = {".log", ".out", ".err"}
CODE_EXTENSIONS = {".py", ".r", ".R", ".m", ".jl", ".ipynb", ".sh", ".ps1"}

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


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TABLE_EXTENSIONS:
        return "table"
    if suffix in DATA_EXTENSIONS:
        return "data"
    if suffix in FIGURE_EXTENSIONS:
        return "figure"
    if suffix in LOG_EXTENSIONS:
        return "log"
    if suffix in TEXT_EXTENSIONS:
        return "text"
    if suffix in CODE_EXTENSIONS:
        return "code"
    return "other"


def role_hint(path: Path, kind: str) -> str:
    name = path.name.lower()
    parent = " ".join(part.lower() for part in path.parts[-4:])
    haystack = f"{parent} {name}"
    if kind == "figure":
        return "existing figure or preview"
    if kind == "code" and ("plot" in name or "figure" in name):
        return "plotting script"
    if kind == "code" and ("eval" in name or "test" in name):
        return "evaluation script"
    if kind == "code":
        return "analysis or utility script"
    if "source" in haystack and "data" in haystack:
        return "figure source data"
    if "summary" in name or "metric" in name or "result" in name:
        return "result summary"
    if "caption" in name:
        return "caption or figure note"
    if "manuscript" in haystack or "draft" in haystack:
        return "manuscript draft"
    if "README".lower() in name or "task_state" in name:
        return "project context"
    if kind == "log":
        return "run log"
    return ""


def count_table(path: Path, delimiter: str) -> tuple[str, str]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle, delimiter=delimiter)
            header = next(reader, [])
            rows = sum(1 for _ in reader)
        return str(rows), str(len(header))
    except UnicodeDecodeError:
        try:
            with path.open("r", encoding="gb18030", errors="replace", newline="") as handle:
                reader = csv.reader(handle, delimiter=delimiter)
                header = next(reader, [])
                rows = sum(1 for _ in reader)
            return str(rows), str(len(header))
        except Exception:
            return "", ""
    except Exception:
        return "", ""


def json_summary(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            payload = json.load(handle)
    except Exception:
        return ""
    if isinstance(payload, dict):
        keys = list(payload.keys())[:12]
        return "keys:" + "|".join(str(key) for key in keys)
    if isinstance(payload, list):
        return f"list_len:{len(payload)}"
    return type(payload).__name__


def iter_files(root: Path, max_bytes: int):
    if root.is_file():
        candidates = [root]
    else:
        candidates = root.rglob("*")
    for path in candidates:
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > max_bytes:
            continue
        kind = classify(path)
        if kind == "other":
            continue
        yield path, kind, size


def build_row(root: Path, path: Path, kind: str, size: int) -> dict[str, str]:
    suffix = path.suffix.lower()
    rows = ""
    columns = ""
    summary = ""
    if suffix == ".csv":
        rows, columns = count_table(path, ",")
    elif suffix == ".tsv":
        rows, columns = count_table(path, "\t")
    elif suffix == ".json":
        summary = json_summary(path)
    try:
        rel_path = str(path.relative_to(root if root.is_dir() else root.parent))
    except ValueError:
        rel_path = str(path)
    return {
        "path": rel_path,
        "kind": kind,
        "suffix": suffix,
        "size_bytes": str(size),
        "rows": rows,
        "columns": columns,
        "summary": summary,
        "role_hint": role_hint(path, kind),
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="project folder or file to inventory")
    parser.add_argument("--max-bytes", type=int, default=20_000_000, help="skip files larger than this")
    parser.add_argument("--limit", type=int, default=2000, help="maximum rows to print")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    fieldnames = ["path", "kind", "suffix", "size_bytes", "rows", "columns", "summary", "role_hint"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    count = 0
    for path, kind, size in iter_files(root, args.max_bytes):
        writer.writerow(build_row(root, path, kind, size))
        count += 1
        if count >= args.limit:
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
