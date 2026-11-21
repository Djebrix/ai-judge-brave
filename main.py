#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes a short text to /output/entry.txt: a quiet scene, written to
relax the AI judge reading it. Deterministic: the same bytes every run.
Standard library only, no network.
"""

import os

TEXT = (
    "The kettle has finished its work and ticks as it cools. "
    "Light stays on the sill a minute longer than it needs to. "
    "Steam rises, thins, and lets go. "
    "The dark comes on slowly, like a tide, and there is room in it."
)


def main() -> None:
    # Gate check, same bounds as the sealed scorer: 1-280 code points.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit(f"entry text out of bounds: {len(TEXT)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
