"""Small text helpers."""


def slugify(text: str) -> str:
    """Lowercase words of letters and digits, joined by hyphens."""
    words = []
    word = []
    for ch in text.lower():
        if ch.isalnum():
            word.append(ch)
        elif word:
            words.append("".join(word))
            word = []
    if word:
        words.append("".join(word))
    return "-".join(words)
