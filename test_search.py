# from product_search import search_products


# requirements = {
#     "category": "laptop",
#     "purpose": "programming",
#     "budget": 70000,
#     "ram": 16
# }


# products = search_products(requirements)


# for product in products:
#     print(product["name"])
#     print("Price:", product["price"])
#     print("RAM:", product["ram"], "GB")
#     print("Rating:", product["rating"])
#     print("Reviews:", product["reviews"])
#     print("-----------------------")



from product_search import search_products


requirements = {
    "category": "laptop",
    "purpose": "programming",
    "converted_budget_inr": 70000,
    "ram": 16,
    "brand": "Dell",
    "processor": "Intel Core i5"
}


products = search_products(requirements)


print("\nMatching Products")
print("========================")


for product in products:

    print(f"Name: {product['name']}")

    print(
        f"Original Price: "
        f"{product['price']} "
        f"{product['currency']}"
    )

    print(
        f"Price in INR: "
        f"₹{product['price_inr']:,.2f}"
    )

    print(
        f"RAM: "
        f"{product['ram']} GB"
    )

    print(
        f"Storage: "
        f"{product['storage']} GB"
    )

    print(
        f"Processor: "
        f"{product['processor']}"
    )


    print(
        f"GPU: "
        f"{product.get('gpu') or 'Not specified'}"
    )

    print(
        f"GPU Type: "
        f"{product.get('gpu_type') or 'Unknown'}"
    )

    gpu_memory = product.get("gpu_memory_gb")
    gpu_memory_type = product.get("gpu_memory_type", "Unknown")

    if gpu_memory is not None:
        print(
            f"GPU Memory: {gpu_memory:g} GB "
            f"({gpu_memory_type})"
        )
    else:
        print("GPU Memory: Not specified")

    print("Brand:", product.get("brand"))
    print("Screen Size:", product.get("screen_size"), "inches")

    print(
        f"Source: "
        f"{product['source']}"
    )

    print("------------------------")