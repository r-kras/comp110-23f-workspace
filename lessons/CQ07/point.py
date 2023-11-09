"""Defining the 'Point' class."""

# imports
# from typing import Self
from __future__ import annotations

__author__ = "730699792"


class Point:
    """A class creating the a class for points on xy plane."""
    # attrubutes
    x: float
    y: float
    
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Attribute constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Shifts the point by a given factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new point beased on a scale."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Converting a point to a string."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Overloading the multiplication operator."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, addend: int | float) -> Point:
        """Overloading the addition operator."""
        return Point(self.x + addend, self.y + addend)