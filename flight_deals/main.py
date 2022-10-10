#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager


from_date = datetime.now() + timedelta(days=1)
to_date = datetime.now() + timedelta(days=180)
origin_city_code = 'LON'

datamanger = DataManager()
flight_search = FlightSearch()
google_sheet = datamanger.get_sheet()

for sheet in google_sheet:
    if sheet['iataCode'] == '':
        sheet['iataCode'] = flight_search.get_itacode(sheet['city'])

datamanger.destination_data = google_sheet
datamanger.put_iatacode()

for sheet in google_sheet:
    flight = flight_search.get_flight_data(
        origin_city_code,
        sheet['city'],
        from_date,
        to_date
    )

    if flight.price > sheet['Lowest Price']:
        notification_manager = NotificationManager()
        message = f"Low Price Alert!! from {flight.origin_city} airport {flight.origin_airport} to {flight.destination_city} price is {flight.price}"
        notification_manager.send_sms(message)
#print(datamanger.get_sheet())




