from pathlib import Path
import string


SAMPLE_PATH = Path(__file__).with_name("sample.txt")


def load_text(file_path: Path) -> str:
    """Read and return a UTF-8 text file."""
    raise NotImplementedError


def normalize_text(text: str) -> list[str]:
    """Return lowercase words with punctuation treated as separators."""
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    """Return a mapping from each word to its number of occurrences."""
    raise NotImplementedError


def display_report(word_counts: dict[str, int], total_words: int) -> None:
    """Print total and unique word counts, then the five most frequent words."""
    raise NotImplementedError


def main() -> None:
    text = load_text(SAMPLE_PATH)
    words = normalize_text(text)
    word_counts = count_words(words)
    display_report(word_counts, len(words))


if __name__ == "__main__":
    main()