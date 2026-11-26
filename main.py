#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the funniest one-line git commit message an AI coding agent types
at 3am after a long night of fixing its own bugs to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 139

LINE = "fix: the tests pass now. I changed one character. I have no idea which. Merging anyway."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-139 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
