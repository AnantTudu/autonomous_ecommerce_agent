from models import Product, ShoppingCart


def add_to_cart(cart, product, quantity=1):
    if not isinstance(product, Product):
        raise TypeError("product must be a Product")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")

    cart.items.append((product, quantity))


def format_cart(cart):
    if not cart.items:
        return "Your cart is empty."

    lines = [
        f"{quantity} x {product.name} - ${product.price * quantity:.2f}"
        for product, quantity in cart.items
    ]
    lines.append(f"Total: ${cart.total:.2f}")
    return "\n".join(lines)
