from .catalog import Catalog

class Make(Catalog):
    __kind: str = 'catalog#make'
    __country: str
    def __init__(self, id):
        super().__init__(id, self.__kind)
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, value: str):
        self.__country = value