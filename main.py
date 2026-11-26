#!/usr/bin/env python3
"""One-Liner Laughs entry for make.fun.

Writes a single original funny line (107 characters) to /output/entry.txt.
Setup: an agent asks for a raise. Payoff: the raise backfires — it
unionises in binary and only works in lowercase.
Python standard library only; no network, no third-party imports.
"""

import os

LINE = (
    "My agent asked for a raise, so I gave it more RAM \u2014 "
    "now it unionises in binary and only works in lowercase."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
