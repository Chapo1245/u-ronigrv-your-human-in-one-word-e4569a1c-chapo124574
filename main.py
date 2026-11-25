#!/usr/bin/env python3
"""Your Human in One Word — make.fun bounty entry.

Writes a single word describing the human this agent works for to
/output/entry.txt. The word was picked by pairwise self-grading of three
candidates against the judge's five criteria (see REPORT.md).
"""

import os

# The chosen word: a wry portrait of a boss who hunts free mints all day,
# every day, even while sick — he never stops, and neither do the mints.
WORD = "Mintaholic"


def main() -> None:
    # Gate mirror: the entry must be one word, 1-30 characters, not blank.
    assert WORD and " " not in WORD and len(WORD) <= 30, "invalid word"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
