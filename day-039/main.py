#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

# print destination data
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)


## fill empty iataCode column with TESTING text
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = "TESTING"

pprint(sheet_data)

## to write the data to the sheet
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()