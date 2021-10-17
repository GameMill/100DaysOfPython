import requests
from bs4 import BeautifulSoup
import lxml

class Amazon:
    def __init__(self):
        pass

    def get_price(self,url):
        response = requests.get(url=url,
            headers={
                "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
            }
        )
        response.raise_for_status()
        self.save_html(response.text)
        soup = BeautifulSoup(response.text,"lxml")
        title = soup.find(id="productTitle").string
        price = soup.find(id="priceblock_ourprice")
        if(price == None):
            price = soup.select_one(".a-price span")
            if(price == None):
                return 999999999;
        return (title,float(price.string[1:]))


    def save_html(self,html):
        with open("data.html",mode="w",encoding="utf8") as file:
            file.write(html)

#Amazon().get_price("https://www.amazon.co.uk/gp/product/B01B2OR2TY/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&th=1")
        