import json
import pydantic
from typing import Optional, List

class Tender(pydantic.BaseModel):
    title: str
    start_at: str
    manager: str
    customer: Optional[str]
    business_category: str
    bidders: Optional[str]
    proposals: Optional[str]
    