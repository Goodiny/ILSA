from .saleList import SaleList
from .dealer import Dealer
from typing import List

class DealerList(SaleList):
    __kind: str = 'sale#dealerList'
    __nextPageToken: str
    __dealers: List[Dealer]
    def __init__(self, nextPageToken: str):
        super().__init__(nextPageToken, self.__kind)
        self.dealers = []
    @property
    def dealers(self) -> List[Dealer]:
        return self.__dealers
    @dealers.setter
    def dealers(self, value: List[Dealer]):
        self.__dealers = value
    def add(self, obj: Dealer):
        self.__dealers.append(obj)
