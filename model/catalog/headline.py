from .describe import Describe

class Headline(Describe):
    __id: int
    __base: bool
    def __init__(self, id: int, name: str):
        super().__init__(name)
        self.__id = id
    @property
    def id(self) -> int:
        return self.__id
    @property
    def base(self) -> bool:
        return self.__base
    @base.setter
    def base(self, value: bool):
        self.__base = value