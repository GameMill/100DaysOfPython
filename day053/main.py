from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import json
import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8"
})
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

Address = soup.select(".list-card-addr")
Prices = soup.select(".list-card-price")
links = soup.select(".list-card-link")


class GoogleFormSubmiter:

    def __init__(self):
        s=Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=s)

    def Add(self,Address,Price,Url):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf1r5B0xzIdasizwb9td_QihJrPwidQwJuFJ9WZ3fUNBqFcVw/viewform?usp=sf_link")
        self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Address)
        self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Price)
        self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Url)
        self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    
    def close(self):
        self.driver.quit()
        
        

google_form_submiter = GoogleFormSubmiter()

for i in range(len(Address)):
    google_form_submiter.Add(Address[i].text,Prices[i].text,links[i].get("href"))
    print("Added to google")

google_form_submiter.close()