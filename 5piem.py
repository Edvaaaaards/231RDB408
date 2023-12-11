import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ebay.com"
driver.get(url)
time.sleep(2)

# find=driver.find_element(By.ID, "gdpr-banner-accept")
# find.click()

# find=driver.find_element(By.LINK_TEXT, "Electronics")
# find.click()
# time.sleep(2)

# find=driver.find_element(By.CLASS_NAME, "gh-tb")
# find.send_keys("laptop")

# find=driver.find_element(By.ID, "gh-btn")
# find.click()
input()