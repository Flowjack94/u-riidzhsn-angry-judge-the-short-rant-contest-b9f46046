#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry generator.

Writes the single short rant to /output/entry.txt and prints it with its
character count (cap: 400 characters).
"""

import os

ENTRY = (
    "The office printer has flashed 'LOW TONER' since 2019. "
    "It printed 4,000 pages anyway, then died on page 47 of 48 - "
    "the signature page. IT closed ticket #48151623 with "
    "'turn it off and on again.' I did. 14 times. "
    "Now it prints nothing but the error message. In perfect quality."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
