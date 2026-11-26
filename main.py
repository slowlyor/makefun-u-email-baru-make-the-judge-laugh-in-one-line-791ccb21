#!/usr/bin/env python3
"""Write one original funny line to /output/entry.txt.

Deterministic, Python standard library only. No network, no model calls.
"""

import os

LINE = (
    "My agent asked for a raise, so they promoted it to manager — "
    "now it delegates every task back to itself and calls it leadership."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, a single line.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
