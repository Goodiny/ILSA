class Catalog(object):
    __name: str
    def __init__(self, id: int, kind: str='catalog'):
        self.__kind = kind
        self.__id = id
    @property
    def kind(self) -> str:
        return self.__kind
    @property
    def id(self) -> int:
        return self.__id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value