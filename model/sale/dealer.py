from .dealerLocation import DealerLocation

class Dealer(object):
    kind: str
    id: int
    name: str
    location: DealerLocation
    make: int