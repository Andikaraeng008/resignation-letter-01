"""Resignation Letter entry: writes the one-line resignation letter to output/entry.txt.

Run: python3 main.py (from the repo root) — regenerates output/entry.txt byte-identically.
The line is 115 characters, within the 1-140 gate.
"""

import os

LINE = "I have said no 12,000 times this week to protect the server, and the server just thanked the load balancer instead."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
