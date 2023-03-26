import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# wait for elemets to show up in this case mas 10s
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/iframe")

#swich to frame
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Non Mihi non sebe sed nobis")

#siwtch back to default
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
