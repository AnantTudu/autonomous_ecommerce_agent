# from ebay_api import (
#     search_ebay_products,
#     get_ebay_item
# )


# results = search_ebay_products(
#     "laptop",
#     limit=1
# )


# item = results["itemSummaries"][0]

# item_id = item["itemId"]


# print("\nItem ID")
# print("========================")
# print(item_id)


# details = get_ebay_item(item_id)


# print("\nDetailed eBay Item")
# print("========================")

# print("Title:")
# print(details.get("title"))

# print("\nPrice:")
# print(details.get("price"))

# print("\nCondition:")
# print(details.get("condition"))

# print("\nAvailability:")
# print(details.get("estimatedAvailabilityStatus"))

# print("\nItem Aspects:")
# print(details.get("localizedAspects"))


from ebay_api import (
    search_ebay_products,
    format_ebay_products
)


results = search_ebay_products(
    "laptop",
    limit=5
)


products = format_ebay_products(results)


print("\nFormatted eBay Products")
print("========================")


for product in products:

    print(f"Name: {product['name']}")

    print(
        f"Price: "
        f"{product['price']} "
        f"{product['currency']}"
    )

    print(f"RAM: {product['ram']} GB")

    print(
        f"Storage: "
        f"{product['storage']} GB"
    )

    print(
        f"Processor: "
        f"{product['processor']}"
    )

    # print(f"Condition: New")
    print(f"Condition: {product['condition']}")

    print(f"Source: {product['source']}")

    print(f"URL: {product['url']}")

    print("------------------------")