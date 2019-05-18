from .catalogList import CatalogList

from typing import List


class Edition(CatalogList):
    __kind: str = 'catalog#edition'
    __modelCode: str
    __descriptions: List[str]
    __specifications: List[str]
    __headlines: List[str]
    def __init__(self):
        super().__init__(self.__kind)
    @property
    def modelCode(self) -> str:
        return self.__modelCode
    @modelCode.setter
    def modelCode(self, value: str):
        self.__modelCode