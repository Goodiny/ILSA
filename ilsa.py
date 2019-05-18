from api import *
from model.sale import Offer
from model.sale import OfferList
from model.sale import OfferConfiguration
from model.sale import OfferPromotion
from model.sale import Dealer
from model.sale import DealerList
from model.sale import DealerLocation
from json.decoder import JSONDecodeError
from typing import List
from datetime import datetime

class Ilsa(object):
    _offerList: OfferList
    _dealerList: DealerList

    def getOfferList(self, token='', size=100):
        offer_query = Connect.getOffers(token, size)
        if offer_query.status_code == 200:
            try:
                offerList = offer_query.json()
                kind = offerList['kind']
                nextPageToken = offerList['nextPageToken'] if 'nextPageToken' in offerList else None
                totalCount = offerList['totalCount']
                offers: List[Offer] = []
                print(offerList['offers'].__len__())
                for offer in offerList['offers']:
                    temp_offer = Offer()
                    config = offer['configuration']
                    temp_offer.kind = offer['kind']
                    temp_offer.id = offer['id']
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
                self._offerList = OfferList(kind, nextPageToken, totalCount, offers)
            except JSONDecodeError:
                print('Is not JSON string, sorry')

    def findOfferByVin(self, vin, token=''):

        self.getOfferList(token, size=1000)

        while self._offerList.nextPageToken != None:
            for offer in self._offerList.offers:
                if vin == offer.sku:
                    return offer
            self.getOfferList(self._offerList.nextPageToken, size=1000)
        return None

    def walkOffers(self, token='', size=100):

        self.getOfferList(token, size)
        
        count = 0

        while self._offerList.nextPageToken != None:
            count += 1
            print(count)  
            self.getOfferList(self._offerList.nextPageToken, size=size)

if __name__ == '__main__':
    ilsa = Ilsa()

    # offer = ilsa.findOfferByVin('XW8ZZZ61ZKG054311')

    # print(offer.configuration.make if offer != None else None )
    # ilsa.getOfferList(size=1000)
    # ilsa.getOfferList(ilsa._offerList.nextPageToken, size=1000)
    ilsa.walkOffers(size=1000)

            
        