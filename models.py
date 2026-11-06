# from typing import Optional

# from pydantic import BaseModel


# class ShoppingRequirements(BaseModel):
#     category: str
#     purpose: Optional[str] = None

#     budget: Optional[float] = None
#     currency: Optional[str] = None

#     converted_budget_inr: Optional[float] = None

#     needs_conversion: bool = False




from typing import Optional

from pydantic import BaseModel


class ShoppingRequirements(BaseModel):
    # Basic product requirements
    category: str
    purpose: Optional[str] = None

    # Budget and currency
    budget: Optional[float] = None
    currency: Optional[str] = None
    converted_budget_inr: Optional[float] = None
    needs_conversion: bool = False

    # Product specifications
    ram: Optional[int] = None
    storage: Optional[float] = None
    brand: Optional[str] = None
    processor: Optional[str] = None

    # Graphics specifications
    gpu: Optional[str] = None
    gpu_type: Optional[str] = None
    gpu_memory_gb: Optional[float] = None

    # Other preferences
    screen_size: Optional[float] = None
    condition: Optional[str] = None
