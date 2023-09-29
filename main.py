from app.adapter.inmemory_tender_repository import InMemoryTenderRepository
from app.domain.tender import Tender


def main():
    tender_repository = InMemoryTenderRepository()

    Tender().save(tender_repository)
    Tender().save(tender_repository)

    print(tender_repository.all())
    print(f'Total votes: {tender_repository.total()}')


if __name__ == '__main__':
    main()