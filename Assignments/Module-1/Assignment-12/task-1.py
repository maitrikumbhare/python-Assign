def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

# Test the function
price = 500
discount_percent = 10

result = get_discounted_price(price, discount_percent)
print("Final Price:", result)