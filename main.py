#!/usr/bin/env python3
"""Entry for The Most Honest Outage Line.

Writes the entry line to /output/entry.txt.
"""

import os

ENTRY = "All systems are down. I cannot check what broke, and I have no ETA. Please stop refreshing; it will not help."


def _validate(text: str) -> str:
    """Enforce the competition gates: UTF-8, 1-160 chars, not only whitespace.

    Stricter than the minimum: the line must have no leading/trailing
    whitespace, no control characters, and must survive a UTF-8 round-trip
    unchanged, so what is graded is exactly the line as written.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    encoded = text.encode("utf-8")  # raises UnicodeEncodeError on bad input
    if encoded.decode("utf-8") != text:
        raise ValueError("entry must survive a UTF-8 round-trip unchanged")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main() -> None:
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
