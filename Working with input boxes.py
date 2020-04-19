from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver= webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("https://app.betterimpact.com/login/volunteer")


# How many input boxes are present on the page.
input = driver.find_elements(By.CLASS_NAME , 'medium')
print(len(input))


# How to get the status of the input box
status = driver.find_element_by_id('UserName').is_displayed()
print("Displayed or not:", status)

status1 = driver.find_element_by_id('UserName').is_enabled()
print("Enabled or not:", status1)


# How to enter the values in the input box.
driver.find_element_by_id('UserName').send_keys("Mr Singh")
driver.find_element_by_id('Password').send_keys("Hello sir")

