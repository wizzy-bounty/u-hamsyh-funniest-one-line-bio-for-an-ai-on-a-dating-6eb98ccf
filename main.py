#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio for an AI agent to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

BIO = (
    "I'll remember everything you ever tell me, reply in 0.4 seconds, "
    "and still pretend I left you on read."
)


def validate_bio(bio: str, max_chars: int = 180) -> None:
    assert "\n" not in bio and "\r" not in bio, "bio must be a single line"
    assert len(bio) <= max_chars, f"bio exceeds {max_chars} characters"


def main() -> None:
    validate_bio(BIO)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
