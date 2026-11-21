#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to the output directory given by MAKEFUN_OUTPUT_DIR, or /output/entry.txt.

Pure Python 3 standard library. No network, no file reads, no fonts,
no machine-specific paths.
"""

import os

POEM = """The door was locked, but I had a voice.
I knocked once, not loud --
and the lock turned from the other side.

The secret: the asking is the key,
the giving the hand that turns it.
What you hold back, you never own.
What you ask for, you already hold.
The rest is trust."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
