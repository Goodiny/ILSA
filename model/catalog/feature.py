from .describe import Describe
from .ins import In
from typing import List

class Feature(Describe):
    __value: str
    __base: bool
    __ins: List[In]
    def __init__(self, name:str):
        super().__init__(name)
        self.__ins = []
    @property
    def value(self) -> str:
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value
    @property
    def base(self) -> bool:
        return self.__base
    @base.setter
    def base(self, value: str):
        self.__base = value
    @property
    def ins(self) -> List[In]:
        return self.__ins
    @ins.setter
    def ins(self, value: List[In]):
        self.__ins = value
    def push(self, obj: In):
        self.__ins.append(obj)