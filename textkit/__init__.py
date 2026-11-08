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


def truncate(text: str, limit: int, suffix: str = "...") -> str:
    """At most limit characters; when the text is cut, the suffix ends it."""
    if limit < len(suffix):
        raise ValueError("limit is shorter than the suffix")
    if len(text) <= limit:
        return text
    return text[: limit - len(suffix)] + suffix
