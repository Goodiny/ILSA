class Sale(object):
    __kind: str
    __id: int
    def __init__(self, id:int, kind:str='sale#sale'):
        self.__kind = kind
        self.__id = id
    @property
    def kind(self) -> str:
        return self.__kind
    @property
    def id(self) -> int:
        return self.__id