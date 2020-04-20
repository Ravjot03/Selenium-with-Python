from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("http://www.practiceselenium.com/practice-form.html")


# Checking whether the given radio button is selected or not
driver.find_element_by_id("sex-0").click()  ## this deselects the Male radio button
time.sleep(5)

driver.find_element_by_id("sex-1").click()  ## this selects the Female radio button
status = driver.find_element_by_id("sex-1").is_selected()
print(status)
time.sleep(5)

# Clicking the check boxes

driver.find_element_by_id("tea1").click()
driver.find_element_by_id("tea2").click()
time.sleep(5)


# This will click on the Submit button to get the results.
driver.find_element_by_name("submit").click()
