class OfferConfiguration(object):
    __id: int
    __make: int
    __model: int
    __version: int
    __color: int
    __edition: int
    __modification: int
    __imageLink: str
    def __init__(self, id: int):
        self.__id = id
    @property
    def id(self) -> int:
        return self.__id
    @property
    def make(self) -> int:
        return self.__make
    @make.setter
    def make(self, value: int):
        self.__make = value
    @property
    def model(self) -> int:
        return self.__model
    @model.setter
    def model(self, value: int):
        self.__model = value
    @property
    def version(self) -> int:
        return self.__version
    @version.setter
    def version(self, value: int):
        self.__version = value
    @property
    def color(self) -> int:
        return self.__color
    @color.setter
    def color(self, value: int):
        self.__color = value
    @property
    def edition(self) -> int:
        return self.__edition
    @edition.setter
    def edition(self, value: int):
        self.__edition = value
    @property
    def modification(self) -> int:
        return self.__modification
    @modification.setter
    def modification(self, value: int):
        self.__modification = value
    @property
    def imageLink(self) -> str:
        return self.__imageLink
    @imageLink.setter
    def imageLink(self, value: str):
        self.__imageLink = value