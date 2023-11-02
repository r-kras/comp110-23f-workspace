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
    
    def __init__(self, x_init: float, y_init: float) -> None:
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