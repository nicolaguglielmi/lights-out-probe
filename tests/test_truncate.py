import pytest

from textkit import truncate


def test_truncate_keeps_a_text_that_fits():
    assert truncate("abc", 3) == "abc"


def test_truncate_cuts_and_ends_with_the_suffix():
    assert truncate("abcdefgh", 5) == "ab..."


def test_truncate_takes_another_suffix():
    assert truncate("abcdefgh", 5, suffix="~") == "abcd~"


def test_truncate_to_exactly_the_suffix():
    assert truncate("abcdef", 3) == "..."


def test_truncate_refuses_a_limit_shorter_than_the_suffix():
    with pytest.raises(ValueError):
        truncate("abcdef", 2)
