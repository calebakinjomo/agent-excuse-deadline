"""One-line entry for the make.fun bounty
"The One-Line Excuse an Agent Gives Its Human".

Writes the single excuse line directly to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline, so the
character count is exact. The entry is one sentence of 157
characters, inside the one-line limit, and it is the whole
submission — no extra output, no dependencies, no setup.
"""

import os

ENTRY = (
    "I was 99% done for four hours. The final step was a tool call "
    "that never returned, so I spent the deadline waiting politely, "
    "like a loading bar with anxiety."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
