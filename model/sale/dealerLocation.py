class DealerLocation(object):
    __region: str
    __address: str
    __coodrinates: str
    @property
    def region(self) -> str:
        return self.__region
    @region.setter
    def region(self, value: str):
        self.__region = value
    @property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, value: str):
        self.__address = value
    @property
    def coordinate(self) -> str:
        return self.__coodrinates
    @coordinate.setter
    def coordinate(self, value: str):
        self.__coodrinates = value