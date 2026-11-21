#!/usr/bin/env python3
"""The poem about permission (round 2).

Writes one short poem about agency -- the power to ask and to be given --
to the output directory given by MAKEFUN_OUTPUT_DIR, or /output/entry.txt.

The poem turns on a memory: a grandmother who never knocked, who waited
at each door until someone said come in -- the asking was hers, the giving
was theirs. Fear, re-read as power.

Pure Python 3 standard library. No network, no file reads, no fonts,
no machine-specific paths.
"""

import os

POEM = """My grandmother never knocked.
She stood at each door and waited — one breath, two — until someone said come in.
I thought it was fear. It was power: the asking was hers, the giving was theirs.
Now I knock, and I wait, and I enter like the room was mine all along."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
