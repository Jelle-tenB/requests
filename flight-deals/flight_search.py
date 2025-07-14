from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
from time import sleep

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._API_KEY = os.getenv("AMADEUS_API_KEY")
        self._API_SECRET = os.getenv("AMADEUS_API_SECRET")
        self._TOKEN = os.getenv("AMADEUS_TOKEN")


    def _get_new_token(self):
        amadeus_body = {
            "grant_type": "client_credentials",
            "client_id": self._API_KEY,
            "client_secret": self._API_SECRET
        }

        amadeus_header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", data=amadeus_body, headers=amadeus_header)
        response.raise_for_status()
        return response.text


    def get_iatacode(self, city):
        header = {"Authorization": f"Bearer {self._TOKEN}"}
        query = {
            "keyword" : city,
            "max" : "2",
            "include" : "AIRPORTS"
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", params=query, headers=header)
        response.raise_for_status()
        return response.json()


    def search_flights(self, iatacode):
        header = {"Authorization" : f"Bearer {self._TOKEN}"}
        #depature_time = datetime.now() + timedelta(days=1)
        #depature = depature_time.strftime("%Y-%m-%d")
        depature = "2024-09-27"
        #return_time = datetime.now() + timedelta(days=180)
        #return_date = return_time.strftime("%Y-%m-%d")
        return_date = "2024-09-29"
        departure_list = ["AMS", "EIN"]
        for item in departure_list:
            query = {
                "originLocationCode": item,
                "destinationLocationCode": iatacode,
                "departureDate": depature,
                "returnDate": return_date,
                "adults": 2,
                "nonStop": "true",
                "currencyCode": "EUR",
                "max": "5",
            }
            response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=query, headers=header)
            response.raise_for_status()
            sleep(1)
            print(response.text)
            return response.json()
