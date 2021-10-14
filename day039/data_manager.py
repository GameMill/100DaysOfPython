import requests
import os
import json
from flight_search import FlightSearch


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class DataManager:
    ROOT = os.path.dirname(os.path.abspath(__file__))+"/"
    API_KEY = None
    SHEETY_URL = "https://api.sheety.co/eed3ef0adbd9dc3062ca60078be1df78/flightDeals/prices"
    DATA = None
    FLIGHT_SEARCH = FlightSearch()

    def __init__(self):
        self.read_api_key()
        self.load_data()

    def setup_locations(self,):
        print("Setting up locations")
        for item in range(len(self.DATA)):
            if(self.DATA[item]["iataCode"] == ""):
                print(f"Updating: {self.DATA[item]['city']}")
                data = self.FLIGHT_SEARCH.get_location(self.DATA[item]["city"])
                self.DATA[item]["iataCode"] = data["code"]
                self.update_data(self.DATA[item])

            
        print("Complated Setting up locations")

    def get_valid_flights(self):
        print("Getting Valid Flights")
        citys = []
        for item in self.DATA:
            citys.append(item["iataCode"])
        
        valid_flights = []
        for flight in self.FLIGHT_SEARCH.search(citys):
            max_price = self.get_max_price(flight.city_to)
            if(self.get_max_price(flight.city_to) >= flight.price):
                valid_flights.append(flight)
                print("Flight Found")
        return valid_flights

    def get_max_price(self,city):
        for item in self.DATA:
            if(item["city"].lower() == city.lower()):
                return item["lowestPrice"]
        return 9999999 # error city not found. remove from list
    def load_data(self):
        if(self.DATA == None):
            #self.DATA = self.load_saved_date()
            #return self.DATA
            
            response = requests.get(self.SHEETY_URL,auth=self.API_KEY)
            response.raise_for_status()
            self.DATA = response.json()["prices"]
            #self.save_date(self.DATA)
        return self.DATA

    def update_data(self,row):
        data = {
            "price":{
                "city": row["city"],
                "iataCode": row["iataCode"],
                "lowestPrice": row["lowestPrice"],
            },
        }
        print(data)
        print("Updating data on Google Sheet")
        response = requests.put(self.SHEETY_URL+f"/{row['id']}",json=data,auth=self.API_KEY)
        response.raise_for_status()
        print("Complated updating data on Google Sheet")

    def read_api_key(self):
        with open(f"{self.ROOT}sheety.key") as key_file:
            self.API_KEY = BearerAuth(key_file.read())

    def save_date(self,json_data):
        with open(f"{self.ROOT}SAVED_DATA_SHEETY.json",mode="w") as save_file:
            json.dump(obj=json_data,fp=save_file,indent=4)

    def load_saved_date(self):
        with open(f"{self.ROOT}SAVED_DATA_SHEETY.json") as save_file:
            return json.load(save_file)

