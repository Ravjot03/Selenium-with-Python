from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("https://www.makemytrip.com/")

print(driver.title)

driver.get("https://www.expedia.com/")
time.sleep(5)

print(driver.title)

driver.back()
time.sleep(5)

print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)
