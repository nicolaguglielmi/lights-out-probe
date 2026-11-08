from textkit import slugify


def test_slugify_joins_words_with_hyphens():
    assert slugify("Hello, World") == "hello-world"


def test_slugify_keeps_digits():
    assert slugify("Release 2 notes") == "release-2-notes"


def test_slugify_drops_leading_and_trailing_separators():
    assert slugify("  --spaced out--  ") == "spaced-out"


def test_slugify_of_nothing_is_empty():
    assert slugify("!!!") == ""
