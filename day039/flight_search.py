import os
import requests
from datetime import datetime, timedelta
import json

from flight_data import FlightData

class FlightSearch:
    ROOT = os.path.dirname(os.path.abspath(__file__))+"/"
    API_KEY = None
    SEARCH_URL = "https://tequila-api.kiwi.com/v2/search"
    DATA = None

    def __init__(self):
        self.read_api_key()


    def read_api_key(self):
        with open(f"{self.ROOT}kiwi.key") as key_file:
            self.API_KEY = key_file.read()

    def get_location(self,city):
        data = {
            "term":city,
            "location_types":"city",
            "active_only":True
        }
        response = requests.get("https://tequila-api.kiwi.com/locations/query",params=data,headers=self.get_header())
        response.raise_for_status()
        return response.json()["locations"][0]
    
    def get_header(self):
        return {"apikey":self.API_KEY,"accept":"application/json"}
    
    def setup_flight_data(self,raw_data):
        new_data = []
        for row in raw_data["data"]:
            new_data.append(FlightData(row))
        return new_data

    def search(self,city):
        """Send a request to kiwi and return all flights"""
        
        fly_to = ""
        for item in city:
            if(fly_to != ""):
                fly_to += ","
            fly_to += f"city:{item}"
        print(f"Getting All Flights to {fly_to}")
        #self.DATA = self.setup_flight_data(self.load_saved_date())
        #return self.DATA

        
        data = {
            "fly_from":"city:LON",
            "fly_to":fly_to,
            "curr":"GBP",
            "date_from":(datetime.today()+timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to":(datetime.today()+timedelta(days=183)).strftime("%d/%m/%Y")
        }
        response = requests.get("https://tequila-api.kiwi.com/v2/search",params=data,headers=self.get_header())
        response.raise_for_status()
        self.DATA = self.setup_flight_data(response.json())
        #self.save_date(self.DATA)
        return self.DATA
    
    def save_date(self,json_data):
        with open(f"{self.ROOT}SAVED_DATA_KIWI.json",mode="w") as save_file:
            json.dump(json_data,save_file,indent=4)

    def load_saved_date(self):
        with open(f"{self.ROOT}SAVED_DATA_KIWI.json") as save_file:
            return json.load(save_file)



if __name__ == '__main__':
    test = FlightSearch()
    test.search(["PAR","BER","TYO","SYD","IST","KUL","NYC","SFO","CPT"])