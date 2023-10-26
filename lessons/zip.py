"""Combining two lists into a dictionary."""

__author__: int = 730699792


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Combines a list of keys and a list of values into a dictionary."""
    # initialize dictionary
    output: dict[str, int] = {}
    # return if lengths are different
    if (len(keys) != len(values)):
        return output
    # iterate through list indexes
    for idx in range(0, len(keys)):
        # add key, value pair to dict
        output[keys[idx]] = values[idx]
    # return dict
    return output