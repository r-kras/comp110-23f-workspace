"""Practice summing over lists."""


def sum_evens_in_list(input_list: list[int]) -> int:
    """Sum all even numbers in this list."""
    list_sum: int = 0
    for integer in input_list:
        if (integer % 2 == 0):
            list_sum += integer
    return list_sum

