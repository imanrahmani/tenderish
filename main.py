from fastapi import FastAPI
from app.adapter.mongo_tender_repository import MongoTenderRepository
from app.domain.tender import Tender

app = FastAPI()
tender_repository = MongoTenderRepository()

@app.get("/")
async def root():
    return {"message": "Tenderish"}

@app.get("/tenders/")
async def get_tenders():
    rows = tender_repository.all()
    return rows

@app.post("/tenders/")
async def post_tenders(tender: Tender):
    rows = tender_repository.add(tender)
    return rows
