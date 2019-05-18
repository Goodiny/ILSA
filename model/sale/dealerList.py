from .dealer import Dealer
from typing import List

class DealerList(object):
    kind: str
    nextPageToken: str
    dealers: List[Dealer]
    def __init__(self, kind: str, nextPageToken: str, dealers: List[Dealer]):
        self.kind = kind
        self.nextPageToken = nextPageToken
        self.dealers = dealers
