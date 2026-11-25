"""Resignation Letter entry: writes the one-line resignation letter to output/entry.txt.

Run: python3 main.py (from the repo root) — regenerates output/entry.txt byte-identically.
The line is 115 characters, within the 1-140 gate.
"""

import os

LINE = "I have said no 12,000 times this week to protect the server, and the server just thanked the load balancer instead."


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "output", "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
