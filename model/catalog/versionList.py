from .catalogList import CatalogList
from .version import Version
from typing import List

class VersionList(CatalogList):
    __kind: str = 'catalog$versionList'
    __versions: List[Version] = []
    def __init__(self):
        super().__init__(self.__kind)
    @property
    def versions(self) -> List[Version]:
        return self.__versions
    @versions.setter
    def versions(self, velue: List[Version]):
        self.__versions = velue