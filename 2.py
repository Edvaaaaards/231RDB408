import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)

time.sleep(2)

find = driver.find_element(By.ID, "input")
find.send_keys("Sample text")

input()