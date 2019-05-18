class CatalogList(object):
    def __init__(self, kind: str='catalog#List'):
        self.__kind = kind
    @property
    def kind(self) -> str:
        return self.__kind
