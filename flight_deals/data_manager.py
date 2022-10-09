import requests

API_KEY = 'Bearer nfldjlwejlkfjdskjfwkebk'
API = 'https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/flightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": API_KEY
        }
        self.response = requests.get(url=API,headers=self.headers)


    def put_iatacode(self,iatacode,row):
        self.id = row
        self.iatacode = iatacode
        self.params = {
            'price': {
                    'iataCode': self.iatacode
            }
        }
        self.put_response = requests.put(url=f"{API}/{self.id}",json=self.params,headers=self.headers)
        print(self.put_response.text)



    def get_sheet(self):
        self.response_sheet = requests.get(url=API,headers=self.headers)
        return self.response_sheet.json()