from amazon import Amazon
from email_system import EmailSysten
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

with open(f"{ROOT}products.json") as products_file: # json list of amazon urls and target price
    data = json.load(products_file)

email_system = EmailSysten()
amazon = Amazon()

for (url,price) in data:
    amazon_price = amazon.get_price(url)
    if(amazon_price[1] <= price):
        email_system.send(amazon_price)

