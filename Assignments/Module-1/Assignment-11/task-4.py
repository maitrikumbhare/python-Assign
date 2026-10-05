food_order = {
    'Pizza': 2,
    'Burger': 1,
    'Fries': 3
}

# a) Print all food items
print("Food items:", food_order.keys())

# b) Print all quantities
print("Quantities:", food_order.values())

# c) Print each item with its quantity
print("Items with quantities:")
for item, quantity in food_order.items():
    print(item, ":", quantity)