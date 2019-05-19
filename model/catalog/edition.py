from .catalogList import CatalogList
from .description import Description
from .specification import Specification
from .headline import Headline
from typing import List

class Edition(CatalogList):
    __kind: str = 'catalog#edition'
    __modelCode: str
    __descriptions: List[Description]
    __specifications: List[Specification]
    __headlines: List[Headline]
    def __init__(self, modelCode):
        super().__init__(self.__kind)
        self.__modelCode = modelCode
        self.__descriptions = []
        self.__specifications = []
        self.__headlines = []
    @property
    def modelCode(self) -> str:
        return self.__modelCode
    @property
    def descriptions(self) -> List[Description]:
        return self.__descriptions
    @descriptions.setter
    def descriptions(self, value: List[Description]):
        self.__descriptions = value
    @property
    def specifications(self) -> List[Specification]:
        return self.__specifications
    @specifications.setter
    def specifications(self, value: List[Specification]):
        self.__specifications = value
    @property
    def headlines(self) -> List[Headline]:
        return self.__headlines
    @headlines.setter
    def headlines(self, value: List[Headline]):
        self.__headlines = value
    def add_description(self, obj: Description):
        self.__descriptions.append(obj)
    def add_specification(self, obj: Specification):
        self.__specifications.append(obj)
    def add_headline(self, obj: Headline):
        self.__headlines.append(obj)