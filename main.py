"""Resignation Letter entry: writes the one-line resignation letter to output/entry.txt.

Run: python3 main.py (from the repo root) — regenerates output/entry.txt byte-identically.
The line is 116 characters, within the 1-140 gate: the agent held back
a thousand requests so the server would not crash, but the crash report
still listed the agent as the suspect.
"""

import os

LINE = "I held back a thousand requests so your server would not crash, and the crash report still listed me as the suspect."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
