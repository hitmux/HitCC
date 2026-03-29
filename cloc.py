#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HAN_RE = re.compile(r"[\u4e00-\u9fff]")


def count_lines(text: str) -> int:
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)


def collect_stats(root: Path) -> tuple[dict, dict[str, dict], list[dict]]:
    files = sorted(path for path in root.rglob("*") if path.is_file())
    total = {"files": 0, "lines": 0, "chars": 0, "bytes": 0, "han": 0}
    by_top: dict[str, dict] = {}
    by_file: list[dict] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(root)
        top = rel.parts[0] if len(rel.parts) > 1 else "."
        lines = count_lines(text)
        chars = len(text)
        bytes_count = len(text.encode("utf-8"))
        han = len(HAN_RE.findall(text))

        total["files"] += 1
        total["lines"] += lines
        total["chars"] += chars
        total["bytes"] += bytes_count
        total["han"] += han

        bucket = by_top.setdefault(top, {"files": 0, "lines": 0, "chars": 0, "bytes": 0, "han": 0})
        bucket["files"] += 1
        bucket["lines"] += lines
        bucket["chars"] += chars
        bucket["bytes"] += bytes_count
        bucket["han"] += han

        by_file.append(
            {
                "path": str(rel),
                "lines": lines,
                "chars": chars,
                "bytes": bytes_count,
                "han": han,
            }
        )

    return total, by_top, by_file


def print_summary(root: Path, total: dict, by_top: dict[str, dict], by_file: list[dict], top_n: int) -> None:
    print(f"Target: {root}")
    print()
    print("TOTAL")
    print(f"  Files: {total['files']}")
    print(f"  Lines: {total['lines']}")
    print(f"  Chars: {total['chars']}")
    print(f"  Hanzi: {total['han']}")
    print(f"  Bytes: {total['bytes']}")
    print()

    print("BY TOP DIRECTORY")
    header = f"{'Directory':<36} {'Files':>7} {'Lines':>10} {'Chars':>10} {'Hanzi':>10}"
    print(header)
    print("-" * len(header))
    for name in sorted(by_top):
        item = by_top[name]
        print(f"{name:<36} {item['files']:>7} {item['lines']:>10} {item['chars']:>10} {item['han']:>10}")
    print()

    print(f"TOP {top_n} FILES BY LINES")
    header = f"{'Path':<72} {'Lines':>10} {'Chars':>10} {'Hanzi':>10}"
    print(header)
    print("-" * len(header))
    for item in sorted(by_file, key=lambda value: (-value["lines"], value["path"]))[:top_n]:
        print(f"{item['path']:<72} {item['lines']:>10} {item['chars']:>10} {item['han']:>10}")
    print()

    print(f"TOP {top_n} FILES BY CHARS")
    header = f"{'Path':<72} {'Chars':>10} {'Lines':>10} {'Hanzi':>10}"
    print(header)
    print("-" * len(header))
    for item in sorted(by_file, key=lambda value: (-value["chars"], value["path"]))[:top_n]:
        print(f"{item['path']:<72} {item['chars']:>10} {item['lines']:>10} {item['han']:>10}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Count files, lines, characters, bytes, and Chinese characters.")
    parser.add_argument("path", nargs="?", default="recovery-docs", help="Target directory to scan.")
    parser.add_argument("--top", type=int, default=10, help="Number of top files to display.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text tables.")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Target is not a directory: {root}")
    if args.top < 0:
        raise SystemExit("--top must be >= 0")

    total, by_top, by_file = collect_stats(root)
    if args.json:
        payload = {
            "target": str(root),
            "total": total,
            "by_top_directory": {key: by_top[key] for key in sorted(by_top)},
            "top_files_by_lines": sorted(by_file, key=lambda value: (-value["lines"], value["path"]))[: args.top],
            "top_files_by_chars": sorted(by_file, key=lambda value: (-value["chars"], value["path"]))[: args.top],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print_summary(root, total, by_top, by_file, args.top)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
