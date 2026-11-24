"""Cat Reviews Its Human - one-star review entry.

Running this script writes the single review line to /output/entry.txt.
"""

import os

REVIEW = "One star. He woke me from a nap to show me a photo of me napping. My bowl was empty. I have reported him to the dog."


def main():
    line = REVIEW.strip()
    assert "\n" not in line, "review must be a single line"
    assert 1 <= len(line) <= 200, "review must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
