from .catalogList import CatalogList
from .make import Make
from typing import List

class MakeList(CatalogList):
    __kind: str = 'catalog$MakeList'
    __makes: List[Make] = []
    def __init__(self):
        super().__init__(self.__kind)
    @property
    def makes(self) -> List[Make]:
        return self.__makes
    @makes.setter
    def makes(self, velue: List[Make]):
        self.__makes = velue