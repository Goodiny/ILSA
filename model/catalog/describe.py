class Describe(object):
    __name: str
    def __init__(self, name: str):
        self.__name = name
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        self.__name = value