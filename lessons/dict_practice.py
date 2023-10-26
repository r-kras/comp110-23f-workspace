"""Practice with Dictionaries."""

# Constructing a dictionary
ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary")
print(ice_cream)

# Adding a key, value pair
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

# Removing a key, value pair
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

# Accessing and modifying values
print(f"I have {ice_cream['chocolate']} orders of chocolate")
ice_cream["vanilla"] = 10

# Checking if element in dict
if ("chocolate" in ice_cream and "mint" in ice_cream):
    print(ice_cream["mint"])
else:
    print("No orders of mint")