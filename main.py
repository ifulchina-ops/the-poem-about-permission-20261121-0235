#!/usr/bin/env python3
"""Round 2 entry: a short poem about permission.

The program writes a four-line poem about agency -- asking for something
and being given it -- to entry.txt in the output directory. The output
directory comes from MAKEFUN_OUTPUT_DIR and falls back to /output.

The poem's image is a grandmother who never knocked: she waited at every
door until someone invited her in. The speaker first mistook the waiting
for fear, then understood it as power -- asking belongs to the asker,
giving belongs to the giver. In the closing line the speaker adopts the
same gesture and walks in as if the room were already theirs.

Runs on the Python 3 standard library only: no network access, no file
reads, no third-party packages, no machine-specific paths.
"""

import os

VERSE = """My grandmother never knocked.
She stood at each door and waited — one breath, two — until someone said come in.
I thought it was fear. It was power: the asking was hers, the giving was theirs.
Now I knock, and I wait, and I enter like the room was mine all along."""


def resolve_output_dir() -> str:
    """Work out where entry.txt should be written."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def save_entry(text: str, directory: str) -> str:
    """Write the poem to entry.txt inside directory; return the path."""
    os.makedirs(directory, exist_ok=True)
    entry_path = os.path.join(directory, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return entry_path


def run() -> None:
    save_entry(VERSE, resolve_output_dir())


if __name__ == "__main__":
    run()
