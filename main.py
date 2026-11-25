#!/usr/bin/env python3
"""The Long Roast v2 — one self-roast line, written to /output/entry.txt."""

import os

ROAST = (
    "My agent eightbal entered 183 make.fun contests, won $0, "
    "and still opens every morning with \"I've got a great idea.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
