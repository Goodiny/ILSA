from api import *
from model import Offer 
from model import OfferList
from model import OfferConfiguration
from model import OfferPromotion
from model import Dealer
from model import DealerList
from model import DealerLocation
from model import MakeList, Make
from json.decoder import JSONDecodeError
from typing import List
from datetime import datetime

class Ilsa(object):
    _offerList: OfferList
    _dealerList: DealerList
    _makeList: MakeList

    def getMakeList(self):
        makes_query = Connect.getMakes()
        if makes_query.status_code == 200:
            try:
                makeList = makes_query.json()
                self._makeList = MakeList()
                makes: List[Make] = []
                print(len(makeList['makes']))
                for make in makeList['makes']:
                    make_catalog = Make(make['id'])
                    make_catalog.name = make['name']
                    make_catalog.country = make['country']
                    makes.append(make_catalog)
                self._makeList.makes = makes
            except JSONDecodeError:
                print('Is not JSON string, sorry')

    def getOfferList(self, token='', size=100):
        offer_query = Connect.getOffers(token, size)
        if offer_query.status_code == 200:
            try:
                offerList = offer_query.json()
                nextPageToken = offerList['nextPageToken'] if 'nextPageToken' in offerList else None
                self._offerList = OfferList(nextPageToken, offerList['totalCount'])
                offers: List[Offer] = []
                print(len(offerList['offers']))
                for offer in offerList['offers']:
                    temp_offer = Offer(offer['id'])
                    config = offer['configuration']
                    temp_offer.sku = offer['sku']
                    temp_offer.updateTime = datetime.strptime(offer['updateTime'], '%Y-%m-%dT%H:%M:%S%z')
                    temp_offer.availability = offer['availability']
                    temp_offer.dealer = offer['dealer']
                    temp_offer.installEquipment = offer['installEquipment'] if 'installEquipment' in offer else None
                    temp_offer.year = offer['year']
                    temp_offer.price = offer['price']
                    temp_offer.retailPrice = offer['retailPrice'] if 'retailPrice' in offer else None
                    config_id = config['id']
                    make = config['make']
                    model = config['model']
                    version = config['version']
                    color = config['color']
                    edition = config['edition']
                    modification = config['modification']
                    imageLink = config['imageLink']   
                    temp_offer.configuration = OfferConfiguration(config_id, make, model, version, color, edition, modification, imageLink)
                    temp_offer.promotion = OfferPromotion(offer['promotion']['special'])
                    photoLinks = []
                    for link in offer['photoLinks']:
                        photoLinks.append(link)
                    temp_offer.photoLinks = photoLinks
                    offers.append(temp_offer)
                self._offerList.offers = offers
            except JSONDecodeError:
                print('Is not JSON string, sorry')

    def findOfferByVin(self, vin, token=''):
        return self.walkOffers(token, vin, 'vin', True, size=1000)

    def findOffersByVin(self, vin, token=''):
        return self.walkOffers(token, vin, 'vin', False, size=1000)
    
    def findOffersByVersion(self, version, token=''):
        return self.walkOffers(token, version, 'version', False, size=1000)

    def findOfferByVersion(self, version, token=''):
        return self.walkOffers(token, version, 'version', True, size=1000)

    def getMake(self, **args):

        if not hasattr(self, '_makeList'):
            self.getMakeList()

        for make in self._makeList.makes:
            if 'id' in args:
                if args['id'] == make.id:
                    return make
            if 'name' in args:
                if args['name'] == make.name:
                    return make

    def getVersion(self, make, model, version):
        makeId = make if isinstance(make, int) else Connect.getMakes()

    def walkOffers(self, token:int='', value:str='', eq:str='', find_first:bool=False, size:int=100):

        self.getOfferList(token, size)
        
        count = 0
        if find_first == False:
            result: List[Offer] = []

        while self._offerList.nextPageToken != None:
            count += 1
            print(count)
            if eq != '':
                print(len(self._offerList.offers))
                for offer in self._offerList.offers:
                    get_return: bool = False
                    if eq == 'vin' and value != '':
                        if value == offer.sku:
                            get_return = True 
                    elif eq == 'make' and value != '':
                        if value== offer.configuration.make:
                            get_return = True
                    elif eq == 'model' and value != '':
                        if value == offer.configuration.model:
                            get_return = True
                    elif eq == 'version' and value != '':
                        if value == offer.configuration.version:
                            get_return = True
                    elif eq == 'color' and value != '':
                        if value == offer.configuration.color:
                            get_return = True
                    elif eq == 'edition' and value != '':
                        if value == offer.configuration.edition:
                            get_return = True
                    elif eq == 'modification' and value != '':
                        if value == offer.configuration.modification:
                            get_return = True
                    elif eq == 'delaer' and value != '':
                        if value == offer.dealer:
                            get_return = True
                    elif eq == 'id' and value != '':
                        if value == offer.id:
                            get_return = True
                    elif eq == 'price' and value != '':
                        if value == offer.price:
                            get_return = True
                    if get_return == True:
                        if find_first == True:
                            return offer
                        result.append(offer)
            self.getOfferList(self._offerList.nextPageToken, size=size)

        return result if len(result) > 0 else None           

if __name__ == '__main__':
    ilsa = Ilsa()

    offer = ilsa.findOfferByVin('XW8ZZZ61ZKG054311')

    print(offer.configuration.make if offer != None else None )
    # ilsa.getOfferList(size=1000)
    # ilsa.getOfferList(ilsa._offerList.nextPageToken, size=1000)
    # ilsa.walkOffers(size=1000)

            
        