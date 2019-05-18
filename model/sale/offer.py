from datetime import datetime
from enum import Enum
from decimal import Decimal
from typing import List
from .offerPromotion import OfferPromotion
from .offerConfiguration import OfferConfiguration

class AvailebilityEnum(Enum):
    INSTOCK = 'IN_STOCK'
    OUTOFSTOCK = 'OUT_OF_STOCK'
    PREORDER = 'PRE_ORDER' 

class Offer(object):
    kind: str
    id: int
    updateTime: datetime
    year: int
    availability: AvailebilityEnum
    promotion: OfferPromotion
    sku: str
    dealer: int
    price: Decimal
    retailPrice: Decimal
    installEquipment: str
    configuration: OfferConfiguration
    photoLinks: List[str] = []