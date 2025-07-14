import requests
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_data = FlightData()
flight_search = FlightSearch()
data_manager = DataManager()

# Getting flight prices ----------------------------------------#
sheet_data = data_manager.get_data()
for item in sheet_data:
    iatacode = item['iataCode']
    known_price = item['lowestPrice']
    flight_data.find_cheapest_flight(iatacode, known_price)

# Getting Amadeus auth token -----------------------------------#
#print(flight_search._get_new_token())
#--------------------------------------------------------------------#

# Getting aitaCodes--------------------------------------------------#
# sheet_data = data_manager.get_data()
# for item in sheet_data:
#     if item['iataCode'] == "":
#         city = item['city']
#         data = flight_search.get_iatacode(city)
#         iatacode = data['data'][0]['iataCode']
#         item['iataCode'] = iatacode
#     else:
#         pass

# data_manager.post_data(sheet_data)
#--------------------------------------------------------------------#
