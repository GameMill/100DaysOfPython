import requests
from bs4 import BeautifulSoup
import lxml
import os
from requests_html import HTMLSession  

ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

  
def render_JS(URL):
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()
    return r.html.html

response = render_JS("https://www.empireonline.com/movies/features/best-movies-2/")


data = []
soup = BeautifulSoup(response,'lxml')
for item in soup.find_all("h3"):
    data.append(item.string)
data = data[::-1]
data[0] = "1) "+data[0]
lines = [line+"\n" for line in data]

with open(f"{ROOT}Movies.txt",mode="w") as file:
    response = file.writelines(lines)