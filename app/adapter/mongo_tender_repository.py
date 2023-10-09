from pymongo import MongoClient
from typing import List

from app.domain.tender import Tender
from app.domain.tender_repository import TenderRepository

class MongoTenderRepository(TenderRepository):
    def __init__(self, mongo_uri: str = "mongodb://127.0.0.1:27017/"):
        self.client = MongoClient(mongo_uri)
        self.db = self.client.tenderish
        self.collection = self.db.tenders

    def add(self, tender: Tender) -> Tender:
        result = self.collection.insert_one(tender.model_dump())
        return tender

    def all(self) -> List[Tender]:
        results = self.collection.find()
        tenders_list: List[Tender] = []

        for document in results:
            tender = Tender(**document)
            tenders_list.append(tender)

        return tenders_list


    def total(self) -> int:
        result = self.collection.count_documents(filter={})
        return result
