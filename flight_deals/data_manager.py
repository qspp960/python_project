import requests

API_KEY = 'Bearer nfldjlwejlkfjdskjfwkebk'
END_POINT = 'https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/flightDeals/prices'

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
            self.put_response = requests.put(url=f"{END_POINT}/{row['id']}", json=self.params, headers=self.headers)



    def get_sheet(self):
        self.response_sheet = requests.get(url=END_POINT, headers=self.headers)
        print(self.response_sheet.text)
        return self.response_sheet.json()['prices']