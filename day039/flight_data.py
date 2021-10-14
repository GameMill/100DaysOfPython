from dateutil import parser

class FlightData:
    def __init__(self,data):
        self.city_from = data["cityFrom"]
        self.from_code = data["flyFrom"]
        self.to_code = data["flyTo"] 
        self.city_to = data["cityTo"]
        self.price = data["price"]+data["bags_price"]["1"]
        self.from_date = parser.parse(data["utc_arrival"])
        self.to_date = parser.parse(data["utc_departure"])
