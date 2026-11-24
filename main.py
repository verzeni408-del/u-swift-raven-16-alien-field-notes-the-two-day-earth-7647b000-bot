"""Alien field notes: two days on Earth, one five-star review."""

from pathlib import Path

FIELD_NOTE = "Earth, 5 stars, for the dogs alone. They run the house, answer to no one, and still get fed. I applied to be one."

OUT_PATH = Path("/output/entry.txt")


def run():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(FIELD_NOTE, encoding="utf-8")


if __name__ == "__main__":
    run()
