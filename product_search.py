
from ebay_api import (
    search_ebay_products,
    format_ebay_products
)

from currency import convert_to_inr


def search_products(requirements):

    # Get product category
    category = requirements["category"]



    # Search eBay
    results = search_ebay_products(
        category,
        limit=10
)

    # Convert eBay results into our common format
    products = format_ebay_products(results)

    # Remove duplicate products
    unique_products = []
    seen_products = set()

    for product in products:

        # product_id = product["name"]
        product_id = product["item_id"]


        if product_id not in seen_products:

            seen_products.add(product_id)
            unique_products.append(product)

    products = unique_products

    # # Get user's budget in INR
    # budget = requirements.get(
    #     "converted_budget_inr"
    # )

    
    # Get user's budget in INR
    budget = requirements.get("converted_budget_inr")

    # Convert prices to INR for every product
    for product in products:
        price = product["price"]
        currency = product["currency"]

        if currency != "INR":
            price_inr = convert_to_inr(price, currency)
        else:
            price_inr = price

        product["price_inr"] = price_inr

    # Filter by budget only when the user provides one
    if budget is not None:
        products = [
            product
            for product in products
            if product["price_inr"] <= budget
        ]




    # Filter by budget
    if budget:

        filtered_products = []

        for product in products:

            price = product["price"]
            currency = product["currency"]

            # Convert product price to INR
            if currency != "INR":

                price_inr = convert_to_inr(
                    price,
                    currency
                )

            else:

                price_inr = price

            # Store INR price for filtering/ranking
            product["price_inr"] = price_inr

            if price_inr <= budget:

                filtered_products.append(product)

        products = filtered_products

    # Filter by RAM
    ram = requirements.get("ram")

    if ram:

        products = [
            product
            for product in products
            if product["ram"] is not None
            and product["ram"] >= ram
        ]



    
    # Filter by storage
    storage = requirements.get("storage")

    if storage:
        products = [
            product
            for product in products
            if product.get("storage") is not None
            and product["storage"] >= storage
        ]


    # # Filter available products
    # products = [
    #     product
    #     for product in products
    #     if product["availability"]
    # ]

    # return products


    
    # Filter available products
    products = [
        product
        for product in products
        if product["availability"]
    ]

    # Filter by brand
    brand = requirements.get("brand")

    if brand:
        products = [
            product
            for product in products
            if product.get("brand")
            and brand.lower() in product["brand"].lower()
        ]

    # Filter by processor
    processor = requirements.get("processor")

    if processor:
        products = [
            product
            for product in products
            if product.get("processor")
            and processor.lower() in product["processor"].lower()
        ]

    # Filter by GPU type
    gpu_type = requirements.get("gpu_type")

    if gpu_type:
        products = [
            product
            for product in products
            if product.get("gpu_type")
            and product["gpu_type"].lower() == gpu_type.lower()
        ]

    # Filter by GPU model
    gpu = requirements.get("gpu")

    if gpu:
        products = [
            product
            for product in products
            if product.get("gpu")
            and gpu.lower() in product["gpu"].lower()
        ]

    # Filter by minimum GPU memory in GB
    min_gpu_memory = requirements.get("gpu_memory_gb")

    if min_gpu_memory is not None:
        products = [
            product
            for product in products
            if product.get("gpu_memory_gb") is not None
            and product["gpu_memory_gb"] >= min_gpu_memory
        ]

    # Filter by minimum screen size in inches
    min_screen_size = requirements.get("screen_size")

    if min_screen_size is not None:
        products = [
            product
            for product in products
            if product.get("screen_size") is not None
            and product["screen_size"] >= min_screen_size
        ]

    # Filter by condition
    condition = requirements.get("condition")

    if condition:
        products = [
            product
            for product in products
            if product.get("condition")
            and condition.lower() in product["condition"].lower()
        ]

    return products





