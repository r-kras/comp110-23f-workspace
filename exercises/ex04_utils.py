"""Using abstraction to further understand max, min, slice."""

__author__ = "730699792"

def all(array: list[int], target: int) -> bool:
    """Determines if all array is all the target element"""
    i: int = 0
    all_target: bool = True
    while(i < len(array)):
        if (array[i] != target):
            all_target = False
        i = i + 1
    return True


def max(array: list[int]) -> int:
    """Returns the largest int in an array."""
    if(len(array) == 0):
        raise ValueError("max() arg is an empty list")
    largest: int = array[0]
    i: int = 1
    while (i < len(array)):
        if (largest < array[i]):
            largest = array[i]
        i = i + 1
    return largest


def is_equal(array1: list[int], array2: list[int]) -> bool:
    """Determines if two arrays are identical."""
    assert len(array1) == len(array1) and len(array1) != 0 and len(array2) != 0
    i: int = 0
    while (i < len(array1)):
        if (array1[i] != array2[i]):
            return False
        i = i + 1
    return True