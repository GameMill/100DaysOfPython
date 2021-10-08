import requests
import time
import datetime as dt
import smtplib

LAT = 53.416570
LONG = -3.033540
SERVER_ADDRESS = "smtp.office365.com"
USERNAME = input("Please enter your MSN email address: ")
PASSWORD = input("Please enter your password: ")


def send_message():
    connection = smtplib.SMTP(SERVER_ADDRESS)
    connection.starttls()
    connection.login(USERNAME,PASSWORD)

def check_is_above():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    if(data["message"] == "success"):
        longitude = float(data["iss_position"]["longitude"])
        latitude = float(data["iss_position"]["latitude"])

        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={LAT}&lng={LONG}&formatted=0")
        response.raise_for_status()
        data = response.json()

        sunrise = dt.datetime.fromisoformat(data["results"]["sunrise"]).hour # 4
        sunset = dt.fromisoformat(data["results"]["sunset"]).hour # 16
        now = dt.datetime.now().hour # 18
        if now <= sunrise or now >= sunset:
            long_diff = LONG-longitude
            lat_diff = LAT-latitude
            if((long_diff  < 5 and long_diff > -5) and (lat_diff < 5 and lat_diff > -5)):
                send_message()

while True:
    check_is_above()
    time.sleep(60)