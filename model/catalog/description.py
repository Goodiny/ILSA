from .describe import Describe
from .feature import Feature
from typing import List

class Description(Describe):
    __features: List[Feature]
    def __init__(self, name: str):
        super().__init__(name)
        self.__features = []
    @property
    def feature(self) -> List[Feature]:
        return self.__features
    @feature.setter
    def feature(self, value: List[Feature]):
        self.__features = value
    def push(self, obj: Feature):
        self.__features.append(obj)