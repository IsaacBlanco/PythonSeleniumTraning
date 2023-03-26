import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# wait for elemets to show up in this case mas 10s
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

veg_list = driver.find_elements(By.XPATH, "//tbody//td[1]")
sorted_list = []
for veg in veg_list:
    sorted_list.append(veg.text)
sorted_list.sort()

driver.find_element(By.CSS_SELECTOR, "th[role='columnheader'] ").click()
veg_list = driver.find_elements(By.XPATH, "//tbody//td[1]")
actual_list = []
for veg in veg_list:
    actual_list.append(veg.text)

print(sorted_list)
print(actual_list)

assert sorted_list == actual_list






