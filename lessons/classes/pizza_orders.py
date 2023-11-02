"""Instantiating a class."""

"""
This is where we instantiate the class
we defined in classes.py.
In other words, we're creating objects
that belong to that class.
"""

# import the class 
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # CONSTRUCTOR

sals_pizza: Pizza = Pizza("medium", 5, False)

# accessing/setting attributes
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

# printing out some values
print("my_pizza: ")
print(my_pizza)

print("Pizza: ")
print(Pizza)

print("Size attribute: ")
print(my_pizza.size)

def price (inp_pizza: Pizza) -> float:
        """Take in a pizza object and determine the cost."""
        # cost based on size
        cost: float = 5.00
        if inp_pizza.size == "large":
            cost = 6.25
        # additional toppings cost
        cost += 0.75 * inp_pizza.toppings
        # additional Gluten Free cost
        if inp_pizza.gluten_free:
            cost += 1
        # Return cost as string
        return cost

# Calling the price function
print(price(my_pizza))
print(price(sals_pizza))

# calling the price method
print(my_pizza.price())
print(sals_pizza.price())


my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = make_new_pizza_add_toppings(2)
