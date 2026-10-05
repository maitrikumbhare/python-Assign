def update_cart(cart, item, qty):
    cart[item] = qty
    return cart


cart = {
    "Mobile": 1,
    "Laptop": 2
}

cart = update_cart(cart, "Headphones", 3)
print(cart)

cart = update_cart(cart, "Mobile", 2)
print(cart)