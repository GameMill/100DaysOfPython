from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(EdgeChromiumDriverManager().install());

driver = webdriver.Edge(service=s)



driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")
money = driver.find_element(By.ID,"money")


def get_cost(element):
    test = element.find_element(By.TAG_NAME,'b')
    return int(test.text.split(" - ")[1].replace(',',''))
    


def buy_up_grade():
    current_money = int(money.text.replace(',',''))
    upgrades = driver.find_elements(By.CSS_SELECTOR,"#store div[id^=\"buy\"]")
    best_upgrade = upgrades[0]
    for item in upgrades[:-1]:
        print("Element: "+item.text)
        cost = get_cost(item)
        if cost > current_money:
            break
        else:
            best_upgrade = item
    best_upgrade.click()



timeout = time.time() + 5   # 5 minutes from now
stoptimeout = time.time() + 60*5   # 5 minutes from now


while time.time() < stoptimeout:
    if time.time() > timeout:
        buy_up_grade()
        timeout = time.time() + 5
        print("\n\n")

    cookie.click()

cps = driver.find_element(By.ID,"cps")

print(cps.text)
driver.quit()
input("Press any key to exit")
    

