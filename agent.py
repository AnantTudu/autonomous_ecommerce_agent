
from dotenv import load_dotenv
from product_search import search_products
from langchain_google_genai import ChatGoogleGenerativeAI

from models import ShoppingRequirements
from currency import convert_to_inr


# Load environment variables
load_dotenv()


# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


# Force Gemini to return our Pydantic structure
structured_llm = llm.with_structured_output(
    ShoppingRequirements
)


def understand_request(user_query: str) -> ShoppingRequirements:

#     prompt = f"""
# You are a shopping requirements extraction agent.

# Analyze the user's shopping request.

# Extract:

# 1. Product category
# 2. Purpose/use case
# 3. Budget
# 4. Currency

# Currency rules:

# - "$" means USD
# - "USD" means USD
# - "dollar" or "dollars" means USD

# - "₹" means INR
# - "Rs" means INR
# - "Rs." means INR
# - "INR" means INR
# - "rupees" means INR

# Set needs_conversion to TRUE only when
# the budget currency is NOT INR.

# Set needs_conversion to FALSE when
# the budget is already in INR.

# IMPORTANT:
# Do NOT perform currency conversion yourself.

# Only identify the original currency.

# User request:

# {user_query}
# """


    prompt = f"""
You are a shopping requirements extraction agent.

Analyze the user's shopping request and extract the requirements.

Extract these fields when specified:
1. Product category
2. Purpose or use case
3. Budget
4. Original budget currency
5. RAM in GB
6. Storage in GB
7. Brand
8. Processor
9. GPU model
10. GPU type (integrated or dedicated)
11. GPU memory in GB
12. Minimum screen size in inches
13. Product condition (new or used)

Rules:
- Only extract requirements stated or clearly implied by the user.
- If a requirement is not specified, leave its field as null.
- Do not invent a brand, processor, RAM size, or other specification.
- For RAM, extract the requested minimum amount in GB.
- For storage, convert TB to GB when necessary.
- For GPU memory, extract the requested amount in GB.
- For screen size, extract the minimum requested size in inches.
- Preserve the processor model or family, such as Intel Core i5, i7, or AMD Ryzen 7.
- Use the user's requested brand and condition.

Currency rules:
- "$", "USD", "dollar", or "dollars" means USD.
- "₹", "Rs", "Rs.", "INR", or "rupees" means INR.
- Set needs_conversion to true only when the budget is in a currency other than INR.
- Do not perform currency conversion yourself.
- If no budget is specified, leave budget and currency as null.

User request:
{user_query}
"""



    result = structured_llm.invoke(prompt)

    return result


if __name__ == "__main__":

    user_query = input(
        "What product are you looking for? \n"
    )

    requirements = understand_request(user_query)


    # Convert budget to INR only when required
    if requirements.needs_conversion:

        requirements.converted_budget_inr = convert_to_inr(
            requirements.budget,
            requirements.currency
        )

    else:

        requirements.converted_budget_inr = requirements.budget


    # print("\nFinal Requirements")
    # print("------------------")

    # print(f"Category: {requirements.category}")
    # print(f"Purpose: {requirements.purpose}")

    # print(f"Original Budget: {requirements.budget:,.2f}")
    # print(f"Original Currency: {requirements.currency}")

    # print(
    #     f"Converted Budget (INR): "
    #     f"₹{requirements.converted_budget_inr:,.2f}"
    # )

    # print(f"Needs Conversion: {requirements.needs_conversion}")

    # Convert Pydantic model into a dictionary
    requirements_dict = requirements.model_dump()

    # Search eBay and filter products
    products = search_products(requirements_dict)


    
    print("\nFinal Requirements")
    print("------------------")

    print(f"Category: {requirements.category}")
    print(f"Purpose: {requirements.purpose}")
    print(f"Original Budget: {requirements.budget}")
    print(f"Original Currency: {requirements.currency}")
    print(f"Converted Budget (INR): ₹{requirements.converted_budget_inr}")
    print(f"Needs Conversion: {requirements.needs_conversion}")

    print(f"Brand: {requirements.brand}")
    print(f"Processor: {requirements.processor}")
    print(f"RAM: {requirements.ram} GB")
    print(f"Storage: {requirements.storage} GB")
    print(f"GPU: {requirements.gpu}")
    print(f"GPU Type: {requirements.gpu_type}")
    print(f"GPU Memory: {requirements.gpu_memory_gb} GB")
    print(f"Screen Size: {requirements.screen_size} inches")
    print(f"Condition: {requirements.condition}")


    print("\nMatching Products")
    print("========================")

    if products:
        for product in products:
            print(f"Name: {product.get('name')}")
            print(f"Price: ₹{product.get('price_inr', 0):,.2f}")
            print(f"Brand: {product.get('brand')}")
            print(f"Processor: {product.get('processor')}")
            print(f"RAM: {product.get('ram')} GB")
            print(f"Storage: {product.get('storage')} GB")
            print(f"GPU: {product.get('gpu') or 'Not specified'}")
            print("------------------------")
    else:
        print("No matching products found.")


