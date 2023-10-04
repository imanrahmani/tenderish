from pymongo import MongoClient
from typing import List

from app.domain.tender import Tender
from app.domain.tender_repository import TenderRepository

class MongoTenderRepository(TenderRepository):
    def __init__(self):
        self.tenders = []
        
        client = MongoClient("mongodb://127.0.0.1:27017/")
        self.db = client.tenderish

    def add(self, tender: Tender) -> Tender:
        result = self.db.tenders.insert_one(tender.model_dump())
        return result

    def all(self) -> List[Tender]:
        result = self.db.tenders.find()
        return result

    def total(self) -> int:
        result = self.db.tenders.count_documents(filter={})
        return result