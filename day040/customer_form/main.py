
import json
import requests
import os


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

ROOT = os.path.dirname(os.path.abspath(__file__))+"/"
with open(f"{ROOT}sheety.key") as key_file:
        API_KEY = BearerAuth(key_file.read())

def safe_input(input_message):
    data = input(input_message)
    if(data == ""):
        return safe_input(input_message)
    return data

def get_user_email_address():
    email1 = safe_input("What is your email? ")
    if(email1.__contains__("@") == False or email1.__contains__(".") == False):
        print("Sorry. your emails address is not valid")
        return get_user_email_address()

    email2 = safe_input("Type your email again? ")
    
    if(email1 == email2):
        return email1
    print("Sorry. your emails did not match")
    return get_user_email_address()



response = requests.post("https://api.sheety.co/eed3ef0adbd9dc3062ca60078be1df78/flightDeals/users",auth=API_KEY,json={
    "user":{
        "firstName": safe_input("What is your first name? ").lower().title(),
        "lastName": safe_input("What is your last name? ").lower().title(),
        "email":get_user_email_address()
    }
})
response.raise_for_status()


print("You`re in the club!")