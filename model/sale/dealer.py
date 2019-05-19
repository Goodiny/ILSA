from .sale import Sale
from .dealerLocation import DealerLocation

class Dealer(Sale):
    __kind: str = 'sale#dealer'
    __name: str
    __location: DealerLocation
    __make: int
    def __init__(self, id:int):
        super().__init__(id, self.__kind)
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        self.__name = value
    @property
    def location(self) -> DealerLocation:
        return self.__location
    @location.setter
    def location(self, value: DealerLocation):
        self.__location = value
    @property
    def make(self) -> int:
        return self.__make
    @make.setter
    def make(self, value: int):
        self.__make = value