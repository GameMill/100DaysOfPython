from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service(EdgeChromiumDriverManager().install());

driver = webdriver.Edge(service=s)

# driver.get("https://en.wikipedia.org/wiki/Main_Page");

# count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")

# #print(count.text)
# #count.click()

# #all_portals = driver.find_element(By.LINK_TEXT,"All portals")
# #all_portals.click()

# search_bar = driver.find_element(By.NAME,"search");
# search_bar.send_keys("Python")


# search_bar.send_keys(Keys.ENTER)


driver.get("http://secure-retreat-92358.herokuapp.com/");


fName = driver.find_element(By.NAME,"fName")
fName.send_keys("Hello")

lName = driver.find_element(By.NAME,"lName")
lName.send_keys("World")

email = driver.find_element(By.NAME,"email")
email.send_keys("email@Fakeemails.com")


button = driver.find_element(By.XPATH,"/html/body/form/button")
button.click()

input()