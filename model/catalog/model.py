from .catalog import Catalog

class Model(Catalog):
    __kind: str = 'catalog#model'
    def __init__(self, id: int):
        super().__init__(id, self.__kind)
