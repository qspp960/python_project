import requests

API_KEY = 'Bearer nfldjlwejlkfjdskjfwkebk'
PRICE_END_POINT = 'https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/flightDeals/prices'
USER_END_POINT = 'https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/flightDeals/users'
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": API_KEY
        }

    def put_iatacode(self):
        for row in self.destination_data:
            self.params = {
                'price': {
                    'iataCode': row['iataCode']
                }
            }
            self.put_response = requests.put(url=f"{PRICE_END_POINT}/{row['id']}", json=self.params, headers=self.headers)



    def get_sheet(self):
        self.response_sheet = requests.get(url=PRICE_END_POINT, headers=self.headers)
        print(self.response_sheet.text)
        return self.response_sheet.json()['prices']


    def user_get_data(self):
        response = requests.get(url=USER_END_POINT,headers=self.headers)
        data = response.json()
        self.consumer_data = data['users']
        return self.consumer_data