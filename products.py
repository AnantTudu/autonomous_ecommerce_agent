from models import Product


PRODUCTS = [
    Product("p001", "Wireless Headphones", "audio", 149.99, "Noise-cancelling headphones."),
    Product("p002", "Mechanical Keyboard", "computer accessories", 89.99, "Compact tactile keyboard."),
    Product("p003", "Travel Camera", "photography", 329.00, "Lightweight camera for travel."),
]


def search_products(query):
    query = query.lower().strip()
    return [
        product
        for product in PRODUCTS
        if query in f"{product.name} {product.category} {product.description}".lower()
    ]
