import os
import base64
import requests

from dotenv import load_dotenv


load_dotenv()


CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")


def get_ebay_access_token():

    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError(
            "eBay credentials are missing from .env"
        )

    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"

    encoded_credentials = base64.b64encode(
        credentials.encode()
    ).decode()

    url = "https://api.ebay.com/identity/v1/oauth2/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    response = requests.post(
        url,
        headers=headers,
        data=data
    )

    response.raise_for_status()

    token_data = response.json()

    return token_data["access_token"]


def search_ebay_products(query, limit=10):

    access_token = get_ebay_access_token()

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    params = {
        "q": query,
        "limit": limit
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    return response.json()



# def format_ebay_products(results):

#     products = []

#     for item in results.get("itemSummaries", []):

#         product = {
#             "name": item.get("title"),

#             "price": float(
#                 item.get("price", {}).get("value", 0)
#             ),

#             "currency": item.get("price", {}).get(
#                 "currency"
#             ),

#             "rating": item.get(
#                 "averageRating", 0
#             ),

#             "reviews": item.get(
#                 "reviewCount", 0
#             ),

#             "ram": None,

#             "storage": None,

#             "processor": None,

#             "availability": True,

#             "source": "eBay",

#             "url": item.get("itemWebUrl")
#         }

#         products.append(product)

#     return products


# def format_ebay_products(results):

#     products = []

#     for item in results.get("itemSummaries", []):

#         item_id = item.get("itemId")

#         # Get detailed information for this item
#         details = get_ebay_item(item_id)

#         # Get item specifications
#         aspects = details.get("localizedAspects", [])

#         # Store aspects in a simple dictionary
#         specifications = {}

#         for aspect in aspects:

#             name = aspect.get("name")
#             value = aspect.get("value")

#             if name and value:
#                 specifications[name] = value

#         # Extract RAM
#         ram = None

#         ram_value = specifications.get("RAM Size")

#         if ram_value:
#             try:
#                 ram = int(
#                     ram_value.replace("GB", "").strip()
#                 )
#             except ValueError:
#                 ram = None

#         # Extract storage
#         storage = None

#         storage_value = specifications.get(
#             "SSD Capacity"
#         )

#         if storage_value:
#             try:
#                 storage = int(
#                     storage_value.replace("GB", "").strip()
#                 )
#             except ValueError:
#                 storage = None

#         # Extract processor
#         processor = specifications.get(
#             "Processor"
#         )

#         # Extract price
#         price_data = item.get("price", {})

#         price = float(
#             price_data.get("value", 0)
#         )

#         currency = price_data.get(
#             "currency"
#         )

#         # Create common product format
#         product = {

#             "name": item.get("title"),

#             "price": price,

#             "currency": currency,

#             "rating": 0,

#             "reviews": 0,

#             "ram": ram,

#             "storage": storage,

#             "processor": processor,

#             "availability": True,

#             "source": "eBay",

#             "url": item.get("itemWebUrl")
#         }

#         products.append(product)

#     return products


# def format_ebay_products(results):

#     products = []

#     for item in results.get("itemSummaries", []):

#         item_id = item.get("itemId")

#         # Get detailed information for this item
#         details = get_ebay_item(item_id)

#         # Get item specifications
#         aspects = details.get("localizedAspects", [])

#         # Store specifications in a dictionary
#         specifications = {}

#         for aspect in aspects:

#             name = aspect.get("name")
#             value = aspect.get("value")

#             if name and value:

#                 specifications[name.lower()] = value

#         # -----------------------------
#         # Extract RAM
#         # -----------------------------

#         ram = None

#         ram_keys = [
#             "ram size",
#             "ram",
#             "memory",
#             "installed ram"
#         ]

#         for key in ram_keys:

#             if key in specifications:

#                 ram_value = specifications[key]

#                 try:

#                     ram = int(
#                         ram_value
#                         .replace("GB", "")
#                         .strip()
#                     )

#                 except ValueError:

#                     ram = None

#                 break

#         # -----------------------------
#         # Extract Storage
#         # -----------------------------

#         storage = None

#         storage_keys = [
#             "ssd capacity",
#             "storage capacity",
#             "storage",
#             "hard drive capacity"
#         ]

#         for key in storage_keys:

#             if key in specifications:

#                 storage_value = specifications[key]

#                 try:

#                     storage = int(
#                         storage_value
#                         .replace("GB", "")
#                         .strip()
#                     )

#                 except ValueError:

#                     storage = None

#                 break

#         # -----------------------------
#         # Extract Processor
#         # -----------------------------

#         processor = None

#         processor_keys = [
#             "processor",
#             "processor type",
#             "cpu"
#         ]

#         for key in processor_keys:

#             if key in specifications:

#                 processor = specifications[key]

#                 break

#         # -----------------------------
#         # Extract Price
#         # -----------------------------

#         price_data = item.get("price", {})

#         price = float(
#             price_data.get("value", 0)
#         )

#         currency = price_data.get(
#             "currency"
#         )

#         # -----------------------------
#         # Create common product format
#         # -----------------------------

#         product = {

#             "item_id": item_id,

#             "name": item.get("title"),

#             "price": price,

#             "currency": currency,

#             "rating": 0,

#             "reviews": 0,

#             "ram": ram,

#             "storage": storage,

#             "processor": processor,

#             "availability": True,

#             "source": "eBay",

#             "url": item.get("itemWebUrl")
#         }

#         products.append(product)

#     return products



def get_ebay_item(item_id):

    access_token = get_ebay_access_token()

    url = (
        "https://api.ebay.com/"
        f"buy/browse/v1/item/{item_id}"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        url,
        headers=headers
    )

    response.raise_for_status()

    return response.json()






import re


def format_ebay_products(results):

    products = []

    for item in results.get("itemSummaries", []):

        item_id = item.get("itemId")
        title = item.get("title", "")

        # Get detailed information for this item
        details = get_ebay_item(item_id)

        # Get item specifications
        aspects = details.get("localizedAspects", [])

        print("\nDEBUG:", title)

        for aspect in aspects:
            if any(
                word in aspect.get("name", "").lower()
                for word in ["gpu", "graphic", "video memory", "vram"]
            ):  
                print(aspect)

        specifications = {}

        for aspect in aspects:

            name = aspect.get("name")
            value = aspect.get("value")

            if name and value:

                specifications[name.lower().strip()] = str(value)

        # -----------------------------
        # Extract RAM from specifications
        # -----------------------------

        ram = None

        ram_keys = [
            "ram size",
            "ram",
            "installed ram",
            "memory"
        ]

        for key in ram_keys:

            if key in specifications:

                match = re.search(
                    r"(\d+(?:\.\d+)?)\s*GB\b",
                    specifications[key],
                    re.IGNORECASE
                )

                if match:

                    ram = int(float(match.group(1)))
                    break

        # Fallback: Extract RAM from title
        if ram is None:

            ram_patterns = [
                r"\b(\d+)\s*GB\s*RAM\b",
                r"\b(\d+)\s*GB\s*(?:DDR[3-5]|LPDDR[3-5])\b",
                r"\b(\d+)\s*GB\s*(?:\+|/)\s*\d+\s*GB\b"
            ]

            for pattern in ram_patterns:

                match = re.search(
                    pattern,
                    title,
                    re.IGNORECASE
                )

                if match:

                    ram = int(match.group(1))
                    break

        # -----------------------------
        # Extract storage from specifications
        # -----------------------------

        storage = None

        storage_keys = [
            "ssd capacity",
            "storage capacity",
            "hard drive capacity",
            "storage",
            "hard drive",
            "ssd"
        ]

        for key in storage_keys:

            if key in specifications:

                match = re.search(
                    r"(\d+(?:\.\d+)?)\s*(TB|GB)\b",
                    specifications[key],
                    re.IGNORECASE
                )

                if match:

                    amount = float(match.group(1))
                    unit = match.group(2).upper()

                    if unit == "TB":
                        storage = int(amount * 1024)
                    else:
                        storage = int(amount)

                    break

        # # Fallback: Extract storage from title
        # if storage is None:

        #     storage_patterns = [
        #         r"\b(\d+(?:\.\d+)?)\s*TB\b"
        #         r"(?=\s*(?:SSD|HDD|NVME|PCIE|STORAGE)\b)",

        #         r"\b(\d+)\s*GB\b"
        #         r"(?=\s*(?:SSD|HDD|NVME|PCIE|STORAGE)\b)"
        #     ]

        #     for pattern in storage_patterns:

        #         match = re.search(
        #             pattern,
        #             title,
        #             re.IGNORECASE
        #         )

        #         if match:

        #             amount = float(match.group(1))

        #             if re.search(
        #                 r"\bTB\b",
        #                 match.group(0),
        #                 re.IGNORECASE
        #             ):
        #                 storage = int(amount * 1024)
        #             else:
        #                 storage = int(amount)

        #             break

        
        # Fallback: Extract storage from title
        if storage is None:

            storage_patterns = [
                # Example: 12+256GB (RAM + storage)
                r"\b\d+\s*\+\s*(\d+)\s*GB\b",

                # Example: 1TB SSD, 2TB NVMe
                r"\b(\d+(?:\.\d+)?)\s*TB\b"
                r"(?=\s*(?:SSD|HDD|NVME|PCIE|STORAGE)\b)",

                # Example: 256GB SSD, 512GB NVMe
                r"\b(\d+)\s*GB\b"
                r"(?=\s*(?:SSD|HDD|NVME|PCIE|STORAGE)\b)"
            ]

            for index, pattern in enumerate(storage_patterns):

                match = re.search(
                    pattern,
                    title,
                    re.IGNORECASE
                )

                if match:

                    amount = float(match.group(1))

                    if index == 0:
                        storage = int(amount)

                    elif index == 1:
                        storage = int(amount * 1024)

                    else:
                        storage = int(amount)

                    break



        # -----------------------------
        # Extract processor
        # -----------------------------

        processor = None

        processor_keys = [
            "processor",
            "processor type",
            "cpu"
        ]

        for key in processor_keys:

            if key in specifications:

                processor = specifications[key]
                break

        # Fallback: Extract processor from title
        if processor is None:

            processor_patterns = [
                r"\bIntel\s+Core\s+i[3579](?:[- ]\w+)?",
                r"\bAMD\s+Ryzen\s+[3579](?:\s+\w+)?",
                r"\bIntel\s+Celeron\s+\w+",
                r"\bIntel\s+Pentium\s+\w+",
                r"\bApple\s+M[1-5](?:\s+\w+)?"
            ]

            for pattern in processor_patterns:

                match = re.search(
                    pattern,
                    title,
                    re.IGNORECASE
                )

                if match:

                    processor = match.group(0)
                    break




        
        # -----------------------------
        # Extract screen size
        # -----------------------------

        screen_size = None

        screen_size_keys = [
            "screen size",
            "display size",
            "maximum resolution"
        ]

        for key in screen_size_keys:
            if key in specifications:
                match = re.search(
                    r"(\d+(?:\.\d+)?)\s*(?:inches|inch|in\b|\"|”)",
                    specifications[key],
                    re.IGNORECASE
                )

                if match:
                    screen_size = float(match.group(1))
                    break

        # Fallback: Extract screen size from title
        if screen_size is None:
            match = re.search(
                r'\b(\d{1,2}(?:\.\d+)?)\s*(?:inch(?:es)?\b|in\b|")',
                title,
                re.IGNORECASE
            )

            if match:
                screen_size = float(match.group(1))

        # -----------------------------
        # Extract brand
        # -----------------------------

        brand = specifications.get("brand")

        if brand:
            brand = brand.strip()
        else:
            brand = None



        
        
        # # -----------------------------
        # # Extract GPU
        # # -----------------------------

        # gpu = None

        # gpu_keys = [
        #     "gpu",
        #     "graphics processing type",
        #     "graphics card",
        #     "graphics processor",
        #     "integrated graphics",
        #     "dedicated graphics"
        # ]

        # for key in gpu_keys:

        #     if key in specifications:

        #         gpu = specifications[key]
        #         break

        # # Fallback: Extract GPU from title
        # if gpu is None:

        #     gpu_patterns = [
        #         r"\bNVIDIA\s+GeForce\s+(?:RTX|GTX|MX)\s*[\w-]+",
        #         r"\bAMD\s+Radeon\s+(?:RX\s*)?[\w-]+",
        #         r"\bIntel\s+(?:UHD|Iris\s+Xe|Iris|HD)\s+Graphics\b",
        #         r"\bApple\s+M[1-5]\s+GPU\b"
        #     ]

        #     for pattern in gpu_patterns:

        #         match = re.search(
        #             pattern,
        #             title,
        #             re.IGNORECASE
        #         )

        #         if match:

        #             gpu = match.group(0)
        #             break

        # -----------------------------

        
        # -----------------------------
        # Extract GPU model
        # -----------------------------

        gpu = None

        gpu_keys = [
            "gpu",
            "graphics processing type",
            "graphics card",
            "graphics processor",
            "graphics chipset",
            "integrated graphics",
            "dedicated graphics"
        ]

        for key in gpu_keys:
            if key in specifications:
                value = specifications[key].strip()

                if value and value.lower() not in [
                    "not specified", "unknown", "none"
                ]:
                    gpu = value
                    break

        # Fallback: Extract GPU model from the title
        if gpu is None:
            gpu_patterns = [
                r"\bNVIDIA\s+GeForce\s+(?:RTX|GTX|MX)\s*[\w.-]+",
                r"\bGeForce\s+(?:RTX|GTX|MX)\s*[\w.-]+",
                r"\bAMD\s+Radeon\s+(?:RX\s*)?[\w.-]+",
                r"\bIntel\s+UHD\s+Graphics(?:\s+\d+)?",
                r"\bIntel\s+Iris\s+Xe\s+Graphics",
                r"\bIntel\s+Iris\s+Graphics",
                r"\bIntel\s+HD\s+Graphics(?:\s+\d+)?",
                r"\bIntel\s+Graphics\b",
                r"\bRadeon\s+R[2357]\b"
            ]

            for pattern in gpu_patterns:
                match = re.search(pattern, title, re.IGNORECASE)

                if match:
                    gpu = match.group(0)
                    break

        # -----------------------------
        # Classify GPU type
        # -----------------------------

        gpu_type = "Unknown"

        if gpu:
            gpu_lower = gpu.lower()

            if any(name in gpu_lower for name in [
                "integrated", "on-board", "onboard"
            ]):
                gpu_type = "Integrated"

            elif any(name in gpu_lower for name in [
                "nvidia geforce rtx",
                "nvidia geforce gtx",
                "nvidia geforce mx",
                "geforce rtx",
                "geforce gtx",
                "geforce mx",
                "radeon rx"
            ]):
                gpu_type = "Dedicated"

            elif any(name in gpu_lower for name in [
                "intel uhd",
                "intel iris",
                "intel hd graphics",
                "intel graphics",
                "apple"
            ]):
                gpu_type = "Integrated"

            elif "radeon r" in gpu_lower:
                # The Radeon R-series name alone may not
                # establish whether the GPU is integrated.
                gpu_type = "Unknown"

        # -----------------------------
        # Extract GPU memory
        # -----------------------------

        gpu_memory = None
        gpu_memory_type = "Unknown"

        # Use GPU-specific specification names only.
        # Avoid generic "Memory", which may mean system RAM.
        gpu_memory_keys = [
            "dedicated video memory",
            "video memory",
            "graphics memory",
            "gpu memory",
            "graphics card memory",
            "dedicated graphics memory",
            "video memory size"
        ]

        for key in gpu_memory_keys:
            if key in specifications:
                value = specifications[key].strip()

                if re.search(r"\bshared\b", value, re.IGNORECASE):
                    gpu_memory_type = "Shared"

                match = re.search(
                    r"(\d+(?:\.\d+)?)\s*(GB|MB)\b",
                    value,
                    re.IGNORECASE
                )

                if match:
                    amount = float(match.group(1))
                    unit = match.group(2).upper()

                    if unit == "MB":
                        amount_gb = amount / 1024
                    else:
                        amount_gb = amount

                    gpu_memory = amount_gb
                    if gpu_memory_type != "Shared":
                        gpu_memory_type = "Dedicated"

                    break

                if gpu_memory_type == "Shared":
                    break

        # Fallback: GPU memory explicitly mentioned in title
        if gpu_memory is None:
            memory_patterns = [
                r"\b(\d+(?:\.\d+)?)\s*GB\s*(?:GDDR[3-7]|VRAM)\b",
                r"\b(\d+(?:\.\d+)?)\s*GB\s+(?:dedicated\s+)?(?:video|graphics)\s+memory\b",
                r"\b(\d+(?:\.\d+)?)\s*GB\s+dedicated\s+graphics\b"
            ]

            for pattern in memory_patterns:
                match = re.search(
                    pattern, title, re.IGNORECASE
                )

                if match:
                    gpu_memory = float(match.group(1))
                    gpu_memory_type = "Dedicated"
                    break

        # -----------------------------


        # -----------------------------
        # Extract price
        # -----------------------------

        price_data = item.get("price", {})

        price = float(price_data.get("value", 0))

        currency = price_data.get("currency")

        # -----------------------------
        # Extract actual condition
        # -----------------------------

        condition = (
            details.get("condition")
            or item.get("condition")
            or "Unknown"
        )

        # -----------------------------
        # Create common product format
        # -----------------------------

        product = {

            "item_id": item_id,

            "name": title,

            "price": price,

            "currency": currency,

            "rating": 0,

            "reviews": 0,

            "ram": ram,

            "storage": storage,

            "processor": processor,

            "gpu": gpu,
            
            "gpu_type": gpu_type,
            
            "gpu_memory_gb": gpu_memory,
            
            "gpu_memory_type": gpu_memory_type,
            
            "brand": brand,

            "screen_size": screen_size,
            
            "condition": condition,

            "availability": True,

            "source": "eBay",

            "url": item.get("itemWebUrl")
        }

        products.append(product)

    return products