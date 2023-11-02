"""Testing my summation funciton."""


from lessons.sum.sum_evens import sum_evens_in_list

def test_empty_sum() -> None:
    """sum_evens_in_list of empty list should be 0."""
    assert sum_evens_in_list([]) == 0


def test_list_length_1() -> None:
    """sum_evens_in_list of list with one even should be that number."""
    assert sum_evens_in_list([2]) == 2


def test_list_positives() -> None:
    """sum_evens_in_list of list with positive integers."""
    assert sum_evens_in_list([1,2,3,4]) == 6


def test_list_negatives() -> None:
    """sum_evens_in_list of list with negative integers."""
    assert sum_evens_in_list([-1,-2,-3,-4]) == -6
