import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)
name  = "Valac"
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert

alert_text = alert.text
assert name in alert_text
alert.accept()
#to cancel
#alert.dismiss()