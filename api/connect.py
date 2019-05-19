import requests
from datetime import datetime

class Connect(object):
    _key = 'key=5FXADBFzJEBwJch96AHtUzJdoL7wjoFKn1-UXJQ'
    _sale = 'https://api.ilsa.ru/sale/v2/'
    _catalog = 'https://api.ilsa.ru/catalog/v1/'

    @classmethod
    def getOffers(cls, token='', size=100):

        link = cls._sale + 'offers'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + cls._key + query_string)
        except ConnectionError:
            print('Connection Error in class Connect')

    @classmethod
    def getDealers(cls, token='', size=100):

        link = cls._sale + 'dealers'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + cls._key + query_string)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getMakes(cls):

        link = cls._catalog + 'makes'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + cls._key)
        except ConnectionError:
            print('Connection Error')
    
    @classmethod
    def getModels(cls, makeId):

        link = cls._catalog + 'makes/' + str(makeId) + '/models'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + cls._key)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getVersions(cls, makeId, modelId):

        link = cls._catalog + 'makes/' + str(makeId) + '/models/' + str(modelId) + '/versions'

        print('Connect to {link}at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + cls._key)
        except ConnectionError:
            print('Connection Error')

    @classmethod
    def getEditions(cls, editionId):
        
        link = cls._catalog + 'editions/' + str(editionId)

        print('Connect to {link} ast {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        try:
            return requests.get(link + '?' + cls._key)
        except ConnectionError:
            print('Connection Error')
    
    @classmethod
    def getModifications(cls, token='', size=100):

        link = cls._catalog + 'modifications'

        print('Connect to {link} at {time}'.format(link=link, time=datetime.now().strftime('%H:%M:%S%Z%z %a %d %b %Y')))

        query_string = '&pageSize=' + str(size)
        query_string += '&pageToken=' + token if token != '' else ''

        print(query_string)

        try:
            return requests.get(link + '?' + cls._key + query_string)
        except ConnectionError:
            print('Connection Error')
