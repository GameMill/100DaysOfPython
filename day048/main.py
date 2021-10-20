from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime


s=Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=s)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar)
# print(search_bar.get_attribute("placeholder"))

#logo = driver.find_element(By.CLASS_NAME,"python-logo")
#print(logo.size)

#Documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
#print(Documentation_link.text)

#bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)




links_box = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

data = []
for row in links_box.find_elements(By.CSS_SELECTOR,"li"):
    time = datetime.fromisoformat(row.find_element(By.TAG_NAME,"time").get_attribute("datetime"))
    name = row.find_element(By.TAG_NAME,"a").text
    data.append({
        "name":name,
        "time":time.strftime("%Y-%m-%d")
    })

print(data)


# driver.close() # closes the tab
driver.quit() # closes the browser