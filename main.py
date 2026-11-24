"""One-Liner Laugh Lab -- make.fun entry.

One funny, original line of at most 200 characters. The program validates
the line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "My smart fridge just filed a complaint: I keep opening it, staring "
    "inside, and closing it like it is a magic trick that stopped working."
)

LIMIT = 200
OUTPUT_PATH = "/output/entry.txt"


def check_line(text):
    """One line, 1 to 200 characters, not blank."""
    if not isinstance(text, str):
        raise ValueError("line must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be blank")
    if len(text) > LIMIT:
        raise ValueError("line is %d characters, over the 200 limit" % len(text))
    return text


def main():
    line = check_line(LINE)
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
