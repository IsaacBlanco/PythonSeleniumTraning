import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)


# dinamically handling radios or check in case they change positions later
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for check in checkboxes:
    if check.get_attribute("value") == "option2":
        check.click()
        assert check.is_selected()
        break

# static selecting of check and raios if we are sure they wont change positions
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio_buttons[1].click()
assert radio_buttons[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
