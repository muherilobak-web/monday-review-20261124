"""Monday, Reviewed in One Line.

Writes one fixed one-line review of the entrant's own Monday to
/output/entry.txt: a deadpan one-star product review of the day, naming
one concrete defect (a 9 a.m. meeting about a meeting) and ending with
a verdict. No input, no arguments, no network, no randomness: every
run writes exactly the same single line, with no trailing newline.
"""

import os
from pathlib import Path

ENTRY = (
    "One star for a Monday that held a 9 o'clock meeting about a meeting "
    "and billed the rest of the day as productivity; would not recommend."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
