import requests
from bs4 import BeautifulSoup
import lxml

class Top100Songs:
    URL = "https://www.billboard.com/charts/hot-100/"
    def get_top_100(self,date):
        """Date is YYYY-MM-DD """
        response = requests.get(self.URL+date)
        response.raise_for_status()

        return self.purge_titles(response.text)
        

    def purge_titles(self,data):
        soup = BeautifulSoup(data,"lxml")
        spans = soup.find_all("span",class_="color--primary")
        songs = [item.string for item in spans]
        return songs


