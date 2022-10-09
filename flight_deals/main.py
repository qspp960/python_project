#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
datamanger = DataManager()
flight_search = FlightSearch()
google_sheet = datamanger.get_sheet()
print(google_sheet)
for sheet in google_sheet['prices']:
    row = sheet['id']
    if sheet['iataCode'] == '':
        iatacode = flight_search.get_itacode(sheet['city'])

        datamanger.put_iatacode(iatacode,row)

print(datamanger.get_sheet())




