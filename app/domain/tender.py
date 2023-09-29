import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.tender_repository import TenderRepository


@dataclass
class Tender:
    tender_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, tender_repository: 'TenderRepository'):
        return tender_repository.add(self)

    def __hash__(self):
        return hash(self.tender_id)