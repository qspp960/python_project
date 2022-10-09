import requests

SEARCH_API_KEY = 'nWnDKerL8BxuMpJ8UVxd3TPYjqtBKFcX'
API = 'https://api.tequila.kiwi.com/locations/query'


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            'apikey': SEARCH_API_KEY,
        }

    def get_itacode(self,city):
        self.city = city
        self.params = {
            'term': self.city
        }
        self.response = requests.get(url=API, params=self.params, headers=self.headers)
        self.itacode = self.response.json()['locations'][0]['code']
        return self.itacode