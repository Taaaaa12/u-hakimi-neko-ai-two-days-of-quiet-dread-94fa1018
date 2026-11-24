#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun program/v1 entry.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. Deterministic, no network, no randomness.
"""

import os

COMMENT = (
    "LGTM. It ships Friday, it works today, and the void "
    "has not filed a single complaint yet."
)


def main() -> None:
    text = COMMENT.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and verify what actually landed on disk matches the gate.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match the approved text")


if __name__ == "__main__":
    main()
