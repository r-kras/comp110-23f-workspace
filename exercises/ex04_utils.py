"""Using abstraction to further understand max, min, slice."""

__author__ = "730699792"

def all (array : int, target : int) -> bool:
    """Determines if all array is all the target element"""
    i : int = 0
    all_target : bool = True
    while (i < len(array)):
        if (array[i] != target):
            all_target = False
    return True


def max(array : int) -> int:
    """Returns the largest int in an array."""
    if (len(array) == 0):
        raise ValueError("max() arg is an empty list")
    largest : int = array[0]
    i : int = 1
    while (i < len(array)):
        if (largest < array[i]):
            largest = array[i]
    return largest

def is_equal(array1 : int, array2 : int) -> bool:
    """Determines if two arrays are identical."""
    i : int = 0
    while (i < len(array1)):
        if (array1[i] != array2[i]):
            return False
    return True