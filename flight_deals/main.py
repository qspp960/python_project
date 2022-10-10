#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from user_manager import UserManager


from_date = datetime.now() + timedelta(days=1)
to_date = datetime.now() + timedelta(days=180)
origin_city_code = 'LON'

datamanager = DataManager()
flight_search = FlightSearch()
user_manager = UserManager()
notification_manager = NotificationManager()

google_sheet = datamanager.get_sheet()

for sheet in google_sheet:
    if sheet['iataCode'] == '':
        sheet['iataCode'] = flight_search.get_itacode(sheet['city'])

datamanager.destination_data = google_sheet
datamanager.put_iatacode()

for sheet in google_sheet:
    flight = flight_search.get_flight_data(
        origin_city_code,
        sheet['city'],
        from_date,
        to_date
    )
    if flight == None:
        continue
    if flight.price > sheet['Lowest Price']:

        users = datamanager.user_get_data()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)
#print(datamanger.get_sheet())




