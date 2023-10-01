import abc
from typing import List

from app.domain.tender import Tender
#comment

class TenderRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, vote: Tender) -> Tender:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Tender]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError