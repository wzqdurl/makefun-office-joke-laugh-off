#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one original one-line joke about office life to entry.txt and
prints exactly that line to stdout. Deterministic: no randomness, no
clock, no network, no input — every run produces the same bytes.

The grader reads /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
which must be UTF-8 text of 1 to 200 characters, one line.
"""

import os
import sys

JOKE = (
    "My boss calls it synergy when he takes credit for my work, "
    "and initiative when I do his."
)

# The bounty gate: UTF-8 text of 1 to 200 characters, one line, not only
# whitespace. Fail loudly instead of shipping an entry the gate would refuse.
MAX_CHARS = 200


def validate_joke(joke: str) -> str:
    """Return the joke unchanged if it passes the bounty gate, else fail."""
    if not joke or joke.isspace():
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            f"joke violates the 1-200 character gate: {len(joke)} characters"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    return joke


def resolve_output_path() -> str:
    """Where the grader reads the entry: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    joke = validate_joke(JOKE)
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    print(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
