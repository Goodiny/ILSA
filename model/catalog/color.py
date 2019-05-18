from .catalog import Catalog

class Color(Catalog):
    __kind: str = 'catalog#color'
    __code: str
    __metalic: bool
    __base: str
    __baseColorId: int
    def __init__(self, id):
        super().__init__(id, self.__kind)
    @property
    def code(self) -> str:
        return self.__code
    @code.setter
    def code(self, value: str):
        self.__code = value
    @property
    def metalic(self) -> bool:
        return self.__metalic
    @metalic.setter
    def metalic(self, value: bool):
        self.__metalic = value
    @property
    def base(self) -> str:
        return self.__base
    @property
    def baseColorId(self) -> int:
        return self.__baseColorId
    @baseColorId.setter
    def baseColorId(self, value: int):
        self.__baseColorId = value