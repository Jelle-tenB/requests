import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/ea31ee1ae79ebcbb30879676130a9d51/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.SHEETY_AUTH = {"Authorization": os.getenv("SHEETY_AUTH")}
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.SHEETY_AUTH)
        response.raise_for_status()
        self.destination_data = response.json()
        return self.destination_data["prices"]

    def post_data(self, sheet_data):
        for item in sheet_data:
            id = item['id']
            code = {
                "price": {
                    "iataCode": f"{item['iataCode']}"
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", json=code, headers=self.SHEETY_AUTH)
            response.raise_for_status()
