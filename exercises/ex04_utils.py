"""Using abstraction to further understand max, min, slice."""

__author__ = "730699792"


def all(array: list[int], target: int) -> bool:
    """Determines if all array is all the target element."""
    # counter for while loop
    i: int = 0
    # iterate through array
    
    while (i < len(array)):
        # if a number different than target is found, return false
        if (array[i] != target):
            print(f"check\n{array}  {target}  {array[i]}")
            return False
        i = i + 1
    # if exited while loop, without returning, return true
    return True


def max(array: list[int]) -> int:
    """Returns the largest int in an array."""
    # given that the array is not zero
    if (len(array) == 0):
        raise ValueError("max() arg is an empty list")
    # set variable largest to first element and i to the second index
    largest: int = array[0]
    i: int = 1
    # iterate through array
    while (i < len(array)):
        # if a number is larger than largest, set largest equal to it
        if (largest < array[i]):
            largest = array[i]
        i = i + 1
    # return number stored in largest
    return largest


def is_equal(array1: list[int], array2: list[int]) -> bool:
    """Determines if two arrays are identical."""
    # initialize a counter 
    i: int = 0
    # while the end of each array has not been reached
    while (i < len(array1) and i < len(array2)):
        # if two elements are not equal, return false
        if (array1[i] != array2[i]):
            print(f"check\n{array}  {target}  {array[i]}")
            return False
        i = i + 1
    # if exited while loop, without returning, return true
    return True