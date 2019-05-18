from .offer import Offer
from typing import List

class OfferList(object):
    kind: str
    nextPageToken: str
    totalCount: int
    offers: List[Offer]
    def __init__(self, kind: str, nextPageTOken: str, totalCount: int, offers: List[Offer]):
        self.kind = kind
        self.nextPageToken = nextPageTOken
        self.totalCout = totalCount
        self.offers = offers
    