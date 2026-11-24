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


def validate_entry() -> None:
    """Assert the entry meets the contest rules: non-empty, under 400
    UTF-8 characters, and one single text (no blank lines / separators)."""
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY.encode("utf-8")) < 400, (
        f"entry is {len(ENTRY.encode('utf-8'))} UTF-8 characters, over the 400 cap"
    )
    assert "\n\n" not in ENTRY, "entry must be a single text, no double blank lines"
    assert not any(
        sep in ENTRY for sep in ("---", "===", "***")
    ), "entry must be a single text, no separators"


def main() -> None:
    validate_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
