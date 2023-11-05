"""The unit tests for ex06."""

__author__ = "730699792"


# importing dictionary
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Invert test cases
# Use cases 
def test_invert_one() -> None:
    """Testing invert dictionary of a dict with one pair."""
    assert invert({"train": "rain"}) == {"rain": "train"}


def test_invert_four() -> None:
    """Testing invert dictionary of a dict with four pairs."""
    assert invert({"train": "rain", "car": "far", "heat": "seat", "glare": "pear"}) == {"rain": "train", "far": "car", "seat": "heat", "pear": "glare"}


# edge case
def test_invert_empty() -> None:
    """Returns an empty dict because it was given an empty dict."""
    assert invert({}) == {}


# testing key error
def test_invert_error() -> None:
    """Testing invert with two of the same name."""
    with pytest.raises(KeyError):
        invert({"train": "rain", "car": "rain", "heat": "seat", "glare": "pear"})


# favorite_color test cases
# use cases
def test_favorite_color() -> None:
    """Testing favorite color dictionary of a dict with one pair."""
    assert favorite_color({"Mary": "green", "Cary": "green", "Harry": "red", "Terry": "blue", "Larry": "red", "Barry": "red", "Perry": "blue", "Darry": "yellow", "Jerry": "brown"}) == "green"


def test_favorite_color_capital() -> None:
    """Testing favorite color with strings of varying cases."""
    assert favorite_color({"Mary": "GrEeN", "Samuel": "blUE", "Jesse": "red", "Malachi": "GREEN"}) == "green"


# edge case
def test_favorite_color_empty() -> None:
    """Finding the favorite color of an empty dict."""
    assert favorite_color({}) == ""


# count test cases
# use cases
def test_count_one() -> None:  
    """Determines the occurances of each value in a list of length 1."""
    assert count(["5"]) == {"5": 1}


def test_count_long() -> None:
    """Determines the occurances of each value in a long list."""
    assert count(["5", "4", "2", "8", "4", "4", "8", "4", "2"]) == {"5": 1, "4": 4, "2": 2, "8": 2}


# edge case    
def test_count_empty() -> None:  
    """Counting occuances in an empty dict."""
    assert count([]) == {}


# alphabetizer test cases
# use cases
def test_alphabetizer_one() -> None:
    """Sorts string in a list of length 1 based on the first letter."""
    assert alphabetizer(["small"]) == {"s": ["small"]}


def test_alphabetizer_long() -> None:
    """Sorts strings in a list of length 5 based on the first letter."""
    assert alphabetizer(["small", "Hall", "Ball", "call", "Shall"]) == {"s": ["small", "Shall"], "h": ["Hall"], "b": ["Ball"], "c": ["call"]}


# edge cases
def test_alphabetizer_empty() -> None:
    """Alphabetizing an empty dict."""
    assert alphabetizer([]) == {}


# update_attendance test cases
# use cases
def test_update_attendance_new() -> None:
    """Inserts a new day-list pair into the dict."""
    update_attendance({"Monday": ["Halli", "Faith", "Zac"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"]}, "Thursday", "Denny") == {"Monday": ["Halli", "Faith", "Zac"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"], "Thursday": ["Denny"]}
    

def test_update_attendance_update() -> None:
    """Updates an existing day-list pair in the dict."""
    update_attendance({"Monday": ["Halli", "Faith", "Zac"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"]}, "Monday", "Denny") == {"Monday": ["Halli", "Faith", "Zac", "Denny"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"]}


# edge cases
def test_update_attendance_empty() -> None:
    """Adding empty strings to the dict."""
    update_attendance({"Monday": ["Halli", "Faith", "Zac"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"]}, "", "") == {"Monday": ["Halli", "Faith", "Zac"], "Tuesday": ["Megumi", "Yuji", "Nobara"], "Wednesday": ["RJ", "Armando", "Elliot"]}