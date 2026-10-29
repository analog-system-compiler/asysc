#!/usr/bin/env python3
# Copyright (C) 2006-2026 The Analog System Compiler project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <https://www.gnu.org/licenses/>


import argparse
from datetime import date
from pathlib import Path
import re
import sys


SOURCE_SUFFIXES = {
    "hash": {".py"},
    "c": {".c", ".cc", ".cpp", ".h", ".hpp"},
}


def format_header(license_text: str, style: str) -> str:
    current_year = date.today().year
    lines = [
        re.sub(r"(\d{4}-)\d{4}", rf"\g<1>{current_year}", line).rstrip()
        if "Copyright (C)" in line
        else line.rstrip()
        for line in license_text.rstrip().splitlines()
    ]
    if style == "hash":
        return "\n".join(f"# {line}" if line else "#" for line in lines)
    return "\n".join(["/*", *(f" * {line}" if line else " *" for line in lines), " */"])


def update_file(path: Path, header: str) -> bool:
    original = path.read_bytes()
    newline = "\r\n" if b"\r\n" in original else "\n"
    text = original.decode("utf-8")
    copyright_line = re.search(
        r"(?m)^\s*(?:#\s*|//\s*|/\*\s*\*?\s*|\*\s*)Copyright \(C\)[^\r\n]*",
        text[:2048],
    )
    if copyright_line:
        current_year = date.today().year
        line = copyright_line.group()
        updated_line = re.sub(r"(\d{4}-)\d{4}", rf"\g<1>{current_year}", line).rstrip()
        if updated_line == line:
            return False
        text = text[: copyright_line.start()] + updated_line + text[copyright_line.end() :]
        path.write_bytes(text.encode("utf-8"))
        return True

    header = header.replace("\n", newline)
    if text.startswith("#!"):
        first_line_end = text.find(newline)
        if first_line_end >= 0:
            shebang_end = first_line_end + len(newline)
            updated = text[:shebang_end] + header + newline + newline + text[shebang_end:]
        else:
            updated = text + newline + header + newline
    else:
        updated = header + newline + newline + text
    path.write_bytes(updated.encode("utf-8"))
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Add project license headers to source files.")
    parser.add_argument("--license", required=True, type=Path, help="Path to the license text")
    parser.add_argument("--style", required=True, choices=SOURCE_SUFFIXES, help="Source comment style")
    parser.add_argument("directories", nargs="+", type=Path, help="Directories to scan")
    args = parser.parse_args()

    try:
        license_text = args.license.read_text(encoding="utf-8")
        header = format_header(license_text, args.style)
        paths = sorted(
            path
            for directory in args.directories
            for path in directory.rglob("*")
            if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES[args.style]
        )
        updated_count = sum(update_file(path, header) for path in paths)
    except (OSError, UnicodeError) as error:
        print(f"add_license_headers.py: {error}", file=sys.stderr)
        return 1

    print(f"Updated license headers in {updated_count} of {len(paths)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
