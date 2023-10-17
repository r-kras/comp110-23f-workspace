"""Summing the elements of a list using different loops."""

__author__ = "730699792"


def w_sum(vals: list[float]) -> float:
    """Finding the sum of a list using a while loop."""
    # index - a counter for element indices
    # output - storing the total sum being returned
    index: int = 0
    output: float = 0
    # Iterate through vals
    while (index < len(vals)):
        # add current value to output
        output += vals[index]
        index += 1
    return output


def f_sum(vals: list[float]) -> float:
    """Finding the sum of a list using a for-element loop."""
    # output - storing the total sum being returned
    output: float = 0
    # Iterate through values in vals
    for num in vals:
        # add current value to output
        output += num
    return output


def f_range_sum(vals: list[float]) -> float:
    """Finding the sum of a list using a for-range loop."""
    # output - storing the total sum being returned
    output: float = 0
    # Iterate through vals
    for index in range(0, len(vals)):
        # add value at current index to output
        output += vals[index]
    return output