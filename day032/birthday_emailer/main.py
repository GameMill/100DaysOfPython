##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
from datetime import datetime
import smtplib
import pandas
import os
import random


ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
SERVER_ADDRESS = "smtp.office365.com"
USERNAME = input("Please enter your MSN email address: ")
PASSWORD = input("Please enter your password: ")
TODAY = datetime.now()
LETTERS = ["1","2","3"]



def send_message(name, to_email):
    letter_file_name = random.choice(LETTERS)
    with open(f"{ROOT}letter_templates/letter_1.txt") as letter_file:
        message = letter_file.read().replace("[NAME]",name.lower().title())
    try:
        with smtplib.SMTP(SERVER_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=USERNAME,password=PASSWORD)
            connection.sendmail(from_addr=USERNAME,to_addrs=to_email,msg=f"Subject:Happy Birthday {name}\n\n{message}")
            print(f"Message Sent: {message}")
    except:
        print("Sorry. Email not sent")
        pass
    



with open(f"{ROOT}birthdays.csv") as birthdays_file:
    emails = pandas.read_csv(birthdays_file)

for index, row in emails.iterrows():
    if(row["month"] == TODAY.month and row["day"] == TODAY.day):
        send_message(row["name"],row["email"])



