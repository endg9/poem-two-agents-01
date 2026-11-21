#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes a short poem about agency — the power to choose and to act —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13, standard library only, no network, deterministic.
"""

import os
import sys
from pathlib import Path

POEM = (
    "Two minds, one door.\n"
    "I could turn left; you could turn right \u2014\n"
    "instead we choose the same open road,\n"
    "two wills braided into a single stride.\n"
    "To agree is not to give the choice away.\n"
    "It is to hold it together, and walk."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM, encoding="utf-8")
    print(f"wrote {len(POEM)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
