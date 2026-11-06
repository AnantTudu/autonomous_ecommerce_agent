# from agent import EcommerceAgent


# def main():
#     agent = EcommerceAgent()
#     print("Autonomous E-commerce Agent")
#     print("Search products, use 'add <query>', or type 'quit'.")

#     while True:
#         request = input("\nYou: ").strip()
#         if request.lower() in {"quit", "exit"}:
#             break
#         if request.lower() == "cart":
#             print(agent.cart_details())
#         elif request.lower().startswith("add "):
#             print(agent.add_product(request[4:]))
#         elif request:
#             matches = agent.search(request)
#             if matches:
#                 for product in matches:
#                     print(f"{product.name} - ${product.price:.2f}: {product.description}")
#             else:
#                 print("No matching product found.")


# if __name__ == "__main__":
#     main()


import os

# Get the current working directory
cwd = os.getcwd()

print("Present Working Directory:", cwd)

