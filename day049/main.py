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
    linkedin_data = json.load(fp=data_file);

s=Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=s)

driver.get("https://www.linkedin.com/")
driver.find_element(By.LINK_TEXT,"Sign in").click()

driver.find_element(By.ID,"username").send_keys(linkedin_data["email"])
driver.find_element(By.ID,"password").send_keys(linkedin_data["password"])
driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()

driver.find_element(By.ID,"ember22").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[data-control-name='job_searches_recent_search_click_0']").click()

input()
driver.quit()