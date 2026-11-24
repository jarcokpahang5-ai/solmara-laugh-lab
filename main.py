"""One-Liner Laugh Lab -- make.fun entry.

One funny, original line of at most 200 characters: a smart fridge files a
complaint about being opened, stared into, and closed like a magic trick
that stopped working. The program validates the line, prints it, and writes
it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "My smart fridge just filed a complaint: I keep opening it, staring "
    "inside, and closing it like it is a magic trick that stopped working."
)

MAX_LENGTH = 200
DESTINATION = "/output/entry.txt"


def validate(text):
    """Require one non-blank line of at most 200 characters."""
    if not isinstance(text, str):
        raise ValueError("line must be text")
    if text != text.strip() or not text:
        raise ValueError("line must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("line is %d characters, over the 200 limit" % len(text))
    return text


def emit(text):
    """Print the line and write it to /output/entry.txt."""
    print(text)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")


def main():
    # Validate first, so only a well-formed line ever reaches the file.
    emit(validate(TEXT))


if __name__ == "__main__":
    main()
