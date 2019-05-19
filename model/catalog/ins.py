class In(object):
    __base: bool
    __description: str
    def __init__(self, desc:str='', base:bool=False):
        self.__base = base
        self.__description = desc
    @property
    def base(self) -> bool:
        return self.__base
    @base.setter
    def base(self, value: bool):
        self.__base = value
    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, value: str):
        self.__description = value
    