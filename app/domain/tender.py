from typing import TYPE_CHECKING
from pydantic import BaseModel
from typing import Optional, List

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.tender_repository import TenderRepository

class ExternalRef(BaseModel):
    id: str
    name: str

class Tender(BaseModel):
    tender_id: str
    customer: ExternalRef
   # product: ExternalRef
   # bidders: List(ExternalRef)

    def save(self, tender_repository: 'TenderRepository'):
        return tender_repository.add(self)

    def __hash__(self):
        return hash(self.tender_id)