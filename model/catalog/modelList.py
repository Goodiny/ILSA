from .catalogList import CatalogList
from .model import Model
from typing import List

class ModelList(CatalogList):
    __kind: str = 'catalog#modelList'
    __models: List[Model]
    def __init__(self):
        super().__init__(self.__kind)
    @property
    def models(self) -> List[Model]:
        return self.__models
    @models.setter
    def models(self, value: List[Model]):
        self.__models = value
