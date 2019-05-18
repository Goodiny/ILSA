from datetime import datetime
from enum import Enum
from decimal import Decimal
from typing import List
from .offerPromotion import OfferPromotion
from .offerConfiguration import OfferConfiguration
from .sale import Sale

class AvailebilityEnum(Enum):
    INSTOCK = 'IN_STOCK'
    OUTOFSTOCK = 'OUT_OF_STOCK'
    PREORDER = 'PRE_ORDER' 

class Offer(Sale):
    __kind: str = 'slae#offer'
    __updateTime: datetime
    __year: int
    __availability: AvailebilityEnum
    __promotion: OfferPromotion
    __sku: str
    __dealer: int
    __price: Decimal
    __retailPrice: Decimal
    __installEquipment: str
    __configuration: OfferConfiguration
    __photoLinks: List[str]
    def __init__(self, id):
        super().__init__(id, self.__kind)
    @property
    def updateTime(self) -> datetime:
        return self.__updateTime
    @updateTime.setter
    def updateTime(self, value: datetime):
        self.__updateTime = value
    @property
    def year(self) -> int:
        return self.__year
    @year.setter
    def year(self, value: int):
        self.__year = value
    @property
    def availability(self) -> AvailebilityEnum:
        return self.__availability
    @availability.setter
    def availability(self, value: AvailebilityEnum):
        self.__availability = value
    @property
    def promotion(self) -> OfferPromotion:
        return self.__promotion
    @promotion.setter
    def promotion(self, value: OfferPromotion):
        self.__promotion = value
    @property
    def sku(self) -> str:
        return self.__sku
    @sku.setter
    def sku(self, value: str):
        self.__sku = value
    @property
    def dealer(self) -> int:
        return self.__dealer
    @dealer.setter
    def dealer(self, value: int):
        self.__dealer = value
    @property
    def price(self) -> int:
        return self.__dealer
    @price.setter
    def price(self, value: Decimal):
        self.__price = value
    @property
    def retailPrice(self) -> Decimal:
        return self.__retailPrice
    @retailPrice.setter
    def retailPrice(self, value: Decimal):
        self.__retailPrice = value
    @property
    def installEquipment(self) -> str:
        return self.__installEquipment
    @installEquipment.setter
    def installEquipment(self, value: str):
        self.__installEquipment = value
    @property
    def configuarion(self) -> OfferConfiguration:
        return self.__configuration
    @configuarion.setter
    def configuarion(self, value: OfferConfiguration):
        self.__configuration = value
    @property
    def photoLinks(self) -> List[str]:
        return self.__photoLinks
    @photoLinks.setter
    def photoLinks(self, value: List[str]):
        self.__photoLinks = value