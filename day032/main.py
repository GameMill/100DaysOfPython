import smtplib
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"

# SERVER_ADDRESS = "smtp.office365.com"
# USERNAME = "ctboardman@msn.com"
# PASSWORD = input("Please enter your password: ")

# with smtplib.SMTP(SERVER_ADDRESS) as connection:
#     connection.starttls()
#     connection.login(user=USERNAME,password=PASSWORD)
#     connection.sendmail(from_addr=USERNAME,to_addrs="cbaordman@yahoo.co.uk",msg="Subject:Hello\n\nThis is the body of my message")

now = datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(now)

if(now.year == 2021):
    print("It is year 2021")


date_of_birth = datetime(year=1993,month=8,day=13)
print(date_of_birth)