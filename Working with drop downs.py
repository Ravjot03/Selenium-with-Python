from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("http://www.practiceselenium.com/practice-form.html")

# Checking whether the drop down is enabled or not
element_status = driver.find_element_by_xpath("//*[@id='continents']").is_enabled()
print(element_status)

 
# Selecting the dop down
drop = Select(driver.find_element_by_xpath("//*[@id='continents']"))  



# Selecting the options from the drop down
drop.select_by_visible_text('Asia')  #we can either select by passing the visible text

drop.select_by_index(5) # or we can select by passing the index value

