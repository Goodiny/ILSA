import requests
from datetime import datetime

class Connect(object):
    _key = 'key=5FXADBFzJEBwJch96AHtUzJdoL7wjoFKn1-UXJQ'
    _sale = 'https://api.ilsa.ru/sale/v2/'
    _catalog = 'https://api.ilsa.ru/catalog/v1/'

    @classmethod
    def getOffers(self, token='', size=100):

        link = self._sale + 'offers'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + self._key + query_string)
        except ConnectionError:
            print('Connection Error in class Connect')

    @classmethod
    def getDealers(self, token='', size=100):

        link = self._sale + 'dealers'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + self._key + query_string)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getMakes(self):

        link = self._catalog + 'makes'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + self._key)
        except ConnectionError:
            print('Connection Error')
    
    @classmethod
    def getModels(self, makeId):

        link = self._catalog + 'makes/' + str(makeId) + '/models'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + self._key)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getVersions(self, makeId, modelId):

        link = self._catalog + 'makes/' + str(makeId) + '/models/' + str(modelId) + '/versions'

        print('Connect to {link}at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + self._key)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getEditions(self, editionId):
        
        link = self._catalog + 'editions/' + str(editionId)

        print('Connect to {link} ast {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + self._key)
        except ConnectionError:
            print('Connection Error')
    
    @classmethod
    def getModifications(self, token='', size=100):

        link = self._catalog + 'modifications'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + self._key + query_string)
        except ConnectionError:
            print('Connection Error')
