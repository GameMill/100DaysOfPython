from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import json
import os
import time

ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

with open(f"{ROOT}data.key") as data_file:
    facebook_data = json.load(fp=data_file);

s=Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=s)

driver.get("https://tinder.com/")
driver.find_element(By.XPATH,'//*[@id="q-1565082725"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="q-1343742289"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

Tinder_Window = driver.window_handles[0]
Facebook_Window = driver.window_handles[1]
driver.switch_to.window(Facebook_Window)

print(driver.title)
time.sleep(1)

driver.find_element(By.ID,"u_0_8_Pj").click()

driver.find_element(By.ID,"email").send_keys(facebook_data["email"])

driver.find_element(By.ID,"pass").send_keys(facebook_data["password"])
#driver.find_element(By.NAME,"login").click()
input()