from functools import reduce

# Swiggy order item prices
item_prices = [120, 80, 150, 60]

# Calculate total bill using reduce() and lambda
total_bill = reduce(lambda x, y: x + y, item_prices)

print("Total Bill:", total_bill)