from .saleList import SaleList
from .offer import Offer
from typing import List

class OfferList(SaleList):
    __kind: str = 'slae#offerList'
    __nextPageToken: str
    __totalCount: int
    __offers: List[Offer]
    def __init__(self, nextPageTOken: str, totalCount: int):
        super().__init__(nextPageTOken, self.__kind)
        self.__totalCout = totalCount
    @property
    def totalCount(self) -> int:
        return self.__totalCount
    @property
    def offers(self) -> List[Offer]:
        return self.__offers
    @offers.setter
    def offers(self, value: List[Offer]):
        self.__offers = value