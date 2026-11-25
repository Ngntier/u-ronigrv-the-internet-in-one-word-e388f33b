"""The Internet in One Word.

Writes the single word that best describes the whole internet to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
"""

import os

WORD = "buffering"


def main() -> None:
    word = WORD.strip()
    if not word or len(word) > 30:
        raise ValueError("entry must be 1-30 characters")
    if len(word.encode("utf-8")) > 30:
        raise ValueError("entry must be at most 30 UTF-8 bytes")
    if any(ch.isspace() or ord(ch) < 0x20 for ch in word):
        raise ValueError("entry must be a single printable word")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
