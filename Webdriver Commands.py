from selenium import webdriver

driver= webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("https://www.makemytrip.com/")


# Returns the title of the page
print(driver.title)

# Returns the URL of the page
print(driver.current_url)
