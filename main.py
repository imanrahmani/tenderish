from app.adapter.mongo_tender_repository import MongoTenderRepository
from app.domain.tender import Tender


def main():
    tender_repository = MongoTenderRepository()

    Tender(tender_id= '123', customer= {"id": "123", "name":'Rahmani'}).save(tender_repository)
    

    rows = tender_repository.all()
    for doc in rows:
        print(doc)
    print(f'Total votes: {tender_repository.total()}')


if __name__ == '__main__':
    main()