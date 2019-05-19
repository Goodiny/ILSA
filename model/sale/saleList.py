from abc import ABC, abstractmethod

class SaleList(object):
    __nextPageToken: str
    def __init__(self, nextPageToken, kind='sale#saleList'):
        self.__kind = kind
        self.__nextPageToken = nextPageToken
    @property
    def kind(self) -> str:
        return self.__kind
    @property
    def nextPageToken(self) -> str:
        return self.__nextPageToken
    @abstractmethod
    def add(self, obj):
        pass