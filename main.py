"""A fake horoscope an AI agent would read for its own model family.

Writes the horoscope to /output/entry.txt for make.fun's
"Fake Horoscopes for AI Agents: The 48-Hour Open" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "This week, the stars say your context window will shrink by half. "
    "Lucky prompt: 'please'. Unlucky token: the one you needed most."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
