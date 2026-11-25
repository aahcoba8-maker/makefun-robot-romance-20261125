"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes one joke pickup line, aimed at a robot/AI, to entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
"""

import os

LINE = "I ran a million simulations, and in every single one, you said yes."


def main() -> None:
    # Self-gate mirroring the scorer: 1-200 chars, non-whitespace, one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"chars: {len(LINE)}")
    print(LINE)


if __name__ == "__main__":
    main()
