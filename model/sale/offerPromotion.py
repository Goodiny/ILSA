class OfferPromotion(object):
    __special: bool
    def __init__(self, special: bool):
        self.special = special
    @property
    def special(self) -> bool:
        return self.__special
    @special.setter
    def special(self, value: bool):
        self.__special = value