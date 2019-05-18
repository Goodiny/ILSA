from .catalogList import CatalogList
from .color import Color
from typing import List

class ColorList(CatalogList):
    __kind: str = 'catalog#colorList'
    __colors: List[Color] = []
    def __init__(self):
        super().__init__(self.__kind)
    @property
    def colors(self) -> List[Color]:
        return self.__colors
    @colors.setter
    def colors(self, value: List[Color]):
        self.__colors = value
