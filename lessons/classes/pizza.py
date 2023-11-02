"""Defining a class!"""

from __future__ import annotations

"""
Think of a class definition as 
a "roadmap" for objects that 
belong to the class.
You are defining the underlying 
structure every instance of this 
class will have
"""

class Pizza:

    # attributes:
    # Think of these as the variables 
    # each instance of my class will have
    size: str
    toppings: int
    gluten_free: bool
    
    def __init__(self, inp_size: str, inp_toppings: str, inp_gluten_free: str) -> None:
        """Attribute constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gluten_free
        # 'Returns' a pizza object

    def price (self) -> float:
        """Take in a pizza object and determine the cost."""
        # cost based on size
        cost: float = 5.00
        if self.size == "large":
            cost = 6.25
        # additional toppings cost
        cost += 0.75 * self.toppings
        # additional Gluten Free cost
        if self.gluten_free:
            cost += 1
        # Return cost as string
        return cost

    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to existing pizza."""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.add_toppings + num_toppings, self.gluten_free)
        return new_pizza