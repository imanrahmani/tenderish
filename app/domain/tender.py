from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.tender_repository import TenderRepository

class Tender(BaseModel):
    tender_id: str
    customer: str 

    def save(self, tender_repository: 'TenderRepository'):
        return tender_repository.add(self)

    def __hash__(self):
        return hash(self.tender_id)