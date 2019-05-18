from .model import Model

class Version(Model):
    __kind: str = 'catalog#version'
    def __init__(self, id):
        super().__init__(id, self.__kind)