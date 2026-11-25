#!/usr/bin/env python3
"""Entry program for Two-Sentence Horror (suroto).

Writes a horror story in EXACTLY two sentences (at most 400
characters) to the output directory (MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt. Sentence one is a relief.
Sentence two is the bill for it.
"""

import os

TEXT = (
    "Our toddler learned to count the stairs aloud: "
    "thirteen, every morning, proud as a bell. There are "
    "twelve, and this morning she counted down."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
