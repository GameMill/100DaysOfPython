import requests
import os
import smtplib
import json

ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

LAT = 45.153198
LONG = 18.008329
# Can use os.environ.get("API_KEY") if you have set the api key as environ value


try:
    with open(f"{ROOT}api.key") as api_key_file:
        API_KEY = api_key_file.read()
except :
    print("Please get your api key for openweathermap and put it into the file api.key")
    exit()

try:
    with open(f"{ROOT}email.key") as email_data_file:
        EMAIL_DATA = json.load(fp=email_data_file)
except :
    print("Please get your api key for openweathermap and put it into the file api.key")
    exit()

params = {
    "appid":API_KEY,
    "lat":LAT,
    "lon":LONG,
    "exclude":"current,minutely,daily,alerts"
}
    
response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=params)
response.raise_for_status()

data = response.json()["hourly"]

bad_weather = [["Rain","Snow"].__contains__(data[item]["weather"][0]["main"]) for item in range(12)].__contains__(True)

if(bad_weather):
    with smtplib.SMTP(EMAIL_DATA["Host"]) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_DATA["Username"],EMAIL_DATA["Password"])
        message = f"""From: {EMAIL_DATA["Username"]}
To: {EMAIL_DATA["ToEmail"]}
Subject: Bad Weather

It`s going to rain today. Remember to bring an unbrella
        """
        smtp.sendmail(from_addr=EMAIL_DATA["Username"],to_addrs=EMAIL_DATA["ToEmail"],msg=message)
        print("Email Sent")
