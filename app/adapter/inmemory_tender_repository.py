from typing import List

from app.domain.tender import Tender
from app.domain.tender_repository import TenderRepository


class InMemoryTenderRepository(TenderRepository):
    def __init__(self):
        self.tenders = []

    def add(self, tender: Tender) -> Tender:
        self.tenders.append(tender)
        return tender

    def all(self) -> List[Tender]:
        return self.tenders

    def total(self) -> int:
        return len(self.tenders)