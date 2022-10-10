import requests
from datetime import datetime, timedelta
from flight_data import FlightData

SEARCH_API_KEY = 'nWnDKerL8BxuMpJ8UVxd3TPYjqtBKFcX'
LOCATION_END_POINT = 'https://api.tequila.kiwi.com/locations/query'
FLIGHT_DATA_END_POINT = 'https://api.tequila.kiwi.com/v2/search'

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
        self.response = requests.get(url=LOCATION_END_POINT, params=self.params, headers=self.headers)
        self.itacode = self.response.json()['locations'][0]['code']
        return self.itacode

    def get_flight_data(self,origin_city_code,destination_city_code,from_time,to_time):
        query = {
           'fly_from': origin_city_code,
           'fly_to': destination_city_code,
           'date_from': from_time.strftime('%d/%m/%Y'),
           'date_to': to_time.strftime('%d/%m/%Y'),
           'return_from': 7,
           'return_to': 28,
           'flight_type': 'round',
           'one_for_city': 1,
           'max_stopovers': 0,
           'curr': 'GBP'
        }
        self.response = requests.get(url=FLIGHT_DATA_END_POINT, params=query, headers=self.headers)

        try:
            data = self.response.json()['data'][0]
            print(f'{destination_city_code}: {data["price"]}')
        except IndexError:
            query['max_stopovers'] = 1

            response = requests.get(url=FLIGHT_DATA_END_POINT, params=query, headers=self.headers)
            data = response.json()['data'][0]

            flight_data = FlightData(
                data['price'],
                data['route']['cityFrom'],
                data['route']['flyFrom'],
                data['route']['cityTo'],
                data['route']['flyTo'],
                data['route'][0]['local_departure'].split('T')[0],
                data['route'][1]['local_departure'].split('T')[0],
                max_stopovers=1,
                via_city=data["route"][0]["cityTo"],
            )

            return flight_data
        else:
            flight_data = FlightData(
                data['price'],
                data['route']['cityFrom'],
                data['route']['flyFrom'],
                data['route']['cityTo'],
                data['route']['flyTo'],
                data['route'][0]['local_departure'].split('T')[0],
                data['route'][1]['local_departure'].split('T')[0],
            )
            return flight_data



