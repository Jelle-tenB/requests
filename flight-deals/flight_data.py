from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_search = FlightSearch()
        self.price_data = {}

    def find_cheapest_flight(self, iatacode, known_price):
        data = self.flight_search.search_flights(iatacode=iatacode)
        for item in data["data"]:
            price = float(item["price"]["total"])
            if iatacode not in self.price_data:
                self.price_data.update({iatacode: [price]})
            else:
                self.price_data[f'{iatacode}'].append(price)
        #for dict_item in self.price_data:
        try:
            lowest_price = min(self.price_data[f'{iatacode}'])
            self.price_data[f'{iatacode}'] = lowest_price
        except KeyError:
            print(f"No flights found to {iatacode}")
        try:
            if self.price_data[f'{iatacode}'] < known_price:
                print(f"Found a cheap flight to {iatacode} for {self.price_data[f'{iatacode}']}")
            else:
                print(f"Lowest current offer to {iatacode} is: {self.price_data[f'{iatacode}']}. Which is higher then the lowest known price of {known_price}")
        except KeyError:
            pass
