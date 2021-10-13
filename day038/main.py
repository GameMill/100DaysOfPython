from datetime import datetime
import json
import os
import requests

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/";


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r



def get_nutritionix_data(user_data):
    """send a request to nutritionix api using the provided user_data for example {"query":"I ran for 2 miles"} """

    with open(f"{ROOT}nutritionix.key") as api_data_file:
        NUTRITIONIX_API_HEADER = json.load(fp=api_data_file)   
    response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise",json=user_data,headers=NUTRITIONIX_API_HEADER)
    response.raise_for_status()
    return response.json()


def convert_nutritionix_data_to_sheety(data):
    """Convert the nutritionix response data to match our sheety row data"""
    now = datetime.now()
    new_data = []
    for item in data["exercises"]:
        new_data.append({
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%I:%M:%S %p"),
            "exercise": str(item["name"]).title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        })
    return new_data
        
    

user_data = {
 "query":input("Tell me which exercises you did: "),
}


def add_row_sheety(row_data):
    with open(f"{ROOT}sheety.key") as api_data_file:
        SHEETY_API_HEADER = api_data_file.read()

    response = requests.post("https://api.sheety.co/eed3ef0adbd9dc3062ca60078be1df78/myWorkouts/workouts",json={"workout":row_data},auth=BearerAuth(SHEETY_API_HEADER))
    response.raise_for_status()

    with open(f"{ROOT}sheety.txt",mode="w") as api_data_file:
        api_data_file.write(response.text)
        print(response.text)


data = convert_nutritionix_data_to_sheety(get_nutritionix_data(user_data))




for row in data:
    add_row_sheety(row)