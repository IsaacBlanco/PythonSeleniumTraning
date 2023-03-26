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

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windows_open = driver.window_handles
driver.switch_to.window(windows_open[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
driver.close()
driver.switch_to.window(windows_open[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)