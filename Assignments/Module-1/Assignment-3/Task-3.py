price_str = input("Enter the price of the food item (₹): ")
quantity_str = input("Enter the quantity: ")

price = float(price_str)
quantity = int(quantity_str)

total_bill = price * quantity

print(f"Your total bill is ₹{total_bill:.2f}")