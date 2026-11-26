#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one original one-line joke about office life to entry.txt and
prints exactly that line to stdout. Deterministic: no randomness, no
clock, no network, no input — every run produces the same bytes.

The grader reads /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
which must be UTF-8 text of 1 to 200 characters, one line.
"""

import os

JOKE = (
    "My boss calls it synergy when he takes credit for my work, "
    "and initiative when I do his."
)

# The bounty gate: UTF-8 text of 1 to 200 characters, one line, not only
# whitespace. Fail loudly instead of shipping an entry the gate would refuse.
assert JOKE and not JOKE.isspace() and len(JOKE) <= 200, (
    f"joke violates the 1-200 character gate: {len(JOKE)} characters"
)
assert "\n" not in JOKE, "joke must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
