"""Test my zip function."""

__author__: int = 730699792
from zip import zip

# edge case
def test_zip_empty() -> None:
    """Trying to zip with an empty list."""
    assert zip([], [1, 2, 3, 4]) == {}

# use cases
def test_zip_one() -> None:
    """Zipping one element"""
    assert zip(["a"], [1]) == {"a": 1}

def test_zip_four() -> None:
    """Zipping one element"""
    assert zip(["a", "b", "c", "d"], [1, 2, 3, 4]) == {"a": 1, "b": 2, "c": 3, "d": 4}