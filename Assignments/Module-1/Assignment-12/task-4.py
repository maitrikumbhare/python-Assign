# Flipkart-style product list
products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

# Filter products starting with 'M'
m_products = list(filter(lambda product: product.startswith('M'), products))

print(m_products)