#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one funny git commit message to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

The scare-quoted "existing technical debt" is the agent's own commit from
14 minutes earlier, and the 04:12 / 03:58 timestamps make it read exactly
like a 4am commit.
"""

import os
import sys

MESSAGE = 'fix: at 04:12, discovered "existing technical debt" was my 03:58 commit'


def main() -> int:
    # Validate guard: the entry must be a single non-empty line.
    if not MESSAGE or not MESSAGE.strip():
        print("error: commit message is empty", file=sys.stderr)
        return 2
    if len(MESSAGE) > 200:
        print("error: commit message exceeds 200 characters", file=sys.stderr)
        return 2
    if "\r" in MESSAGE or "\n" in MESSAGE:
        print("error: commit message contains CR/LF", file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
