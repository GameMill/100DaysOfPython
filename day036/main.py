import os
import requests
from datetime import datetime, timedelta
import json
import smtplib
from email.header import Header


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

with open(f"{ROOT}stock_api.key") as stock_api_file:
    STOCK_API_KEY = stock_api_file.read()

with open(f"{ROOT}news.key") as news_api_file:
    NEWS_API_KEY = news_api_file.read()

with open(f"{ROOT}email.key") as email_file:
    EMAIL_DATA = json.load(fp=email_file)



YESTERDAY = datetime.today() - timedelta(days=3) # -3 day for demo key
DAY_BEFORE_YESTERDAY = datetime.today() - timedelta(days=4)

## STEP 1: Use
# When STOCK pri https://www.alphavantage.coce increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_date_formatted(date: datetime):
    year = date.year
    if(date.month < 10):
        month = f"0{date.month}"
    else:
         month = date.month

    if(date.day < 10):
            day = f"0{date.day}"
    else:
         day = date.day

    return f"{year}-{month}-{day}"



def get_stock_diff(stock):
    """check yestaday close with the day before to see the diff"""

    parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":stock,
        "apikey":STOCK_API_KEY,
    }
    response = requests.get("https://www.alphavantage.co/query",params=parameters)
    response.raise_for_status()
    data = response.json()
    yesterday_data = float(data["Time Series (Daily)"][get_date_formatted(YESTERDAY)]["4. close"])
    day_before_data = float(data["Time Series (Daily)"][get_date_formatted(DAY_BEFORE_YESTERDAY)]["4. close"])
    diff = yesterday_data-day_before_data
    diff_precentage = (yesterday_data/day_before_data-1)*100
    if(diff_precentage > 0):
        type_diff = "increase"
        message = f"UP {diff_precentage:.02f}%"
    else:
        type_diff = "decreace"
        message = f"DOWN {diff_precentage:.02f}%"

    return (diff,diff_precentage,type_diff,message)

diff = get_stock_diff(STOCK)

#if(diff[1] > 5):
#    print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news(company_name,date :datetime):
    parameters = {
        "q":company_name,
        "from":get_date_formatted(date),
        "sortBy":"popularity",
        "apiKey":NEWS_API_KEY
    }
    response = requests.get("https://newsapi.org/v2/everything",params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["articles"]

if(abs(diff[1] > 5)): # if diff["Precentage"] if > 5
    data = get_news(COMPANY_NAME,YESTERDAY)

    # for i in range(3):
    #     print(f"""Headline: {Data[i]["title"]}
    # Brief:{Data[i]["description"]}""")
        

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 

    news = ""
    for i in range(3):
        news += (f"""\r\n\r\nHeadline: {data[i]["title"]}\nBrief:{data[i]["description"]}""")

    with smtplib.SMTP(EMAIL_DATA["Host"]) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_DATA["Username"],EMAIL_DATA["Password"])
        message = f"""From: {EMAIL_DATA["Username"]}
To: {EMAIL_DATA["ToEmail"]}
Subject: {COMPANY_NAME} Stock {Header(diff[3].replace("UP","🔺").replace("DOWN","🔻"),"utf-8").encode()}

{STOCK}: {diff[3]}
{news}
"""

        smtp.sendmail(EMAIL_DATA["Username"],EMAIL_DATA["ToEmail"],message.encode("ascii","ignore").decode("ascii"))

