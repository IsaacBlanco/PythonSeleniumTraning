import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("pa")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

for i, country in enumerate(countries):
    if country.text == "Panama":
        # selector = f"(//li[@class='ui-menu-item'])[{i+1}]"
        # driver.find_element(By.XPATH, selector).click()
        country.click()
        break # exit the loop once find the contidion
time.sleep(2)
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Panama"
