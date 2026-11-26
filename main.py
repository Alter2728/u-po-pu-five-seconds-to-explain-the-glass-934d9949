"""House cat excuse entry.

Revision note: replaced a generic edge-and-curiosity excuse with a
self-important patrol-route justification, giving the cat a fresh,
unapologetic motive that fits five spoken seconds.
"""

import os
from pathlib import Path

TEXT = "That glass was blocking my patrol route, and house security does not stop for beverages."


def main() -> None:
    assert 1 <= len(TEXT) <= 200
    assert "\n" not in TEXT
    assert TEXT == TEXT.strip()

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
