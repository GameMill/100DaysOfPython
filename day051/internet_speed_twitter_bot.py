from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from datetime import datetime
import json
import os
import time


PROMISED_DOWN = 500
PROMISED_UP = 50

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

        with open(f"{ROOT}data.key") as data_file:
            self.twitter_data = json.load(fp=data_file);

        s=Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=s)

            
    def get_internet_speed(self):
        self.driver.get("https://speedtest.net/")
        self.driver.find_element(By.ID,"_evidon-banner-acceptbutton").click()
        self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        self.get_internet_speed_data()
    
    def get_internet_speed_data(self):  
        try:
            time.sleep(10)
            self.ref = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
            self.down = float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
            self.up = float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
            self.ping = int(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        except:
            self.get_internet_speed_data()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(self.twitter_data["email"])
        password.send_keys(self.twitter_data["password"])
        password.send_keys(Keys.ENTER)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()
        

    
        
        