import smtplib
import os
from datetime import datetime
import random

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"

SERVER_ADDRESS = "smtp.office365.com"
USERNAME = input("Please enter your MSN email address: ")
PASSWORD = input("Please enter your password: ")
with open(f"{ROOT}quotes.txt") as quotes_file:
    MESSAGES = quotes_file.readlines()

def send_message(message,to_email):
    if(datetime.now().weekday()!=0):
        print("Sorry. You can only send motivation message on monday")
        exit()
    try:
        with smtplib.SMTP(SERVER_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=USERNAME,password=PASSWORD)
            connection.sendmail(from_addr=USERNAME,to_addrs=to_email,msg=f"Subject:Motivation Message\n\n{message}")
            print(f"Message Sent: {message}")
    except:
        print("Sorry. Email not sent")
        pass
    

send_message(random.choice(MESSAGES),input("Please enter the receivers email address: "))