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

driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.XPATH, "//a[@class]").click()

# handling secon windows
window = driver.window_handles
driver.switch_to.window(window[1])

mail = driver.find_element(By.XPATH, "//a[contains(text(),'mentor')]").text
#closing window
driver.close()

#moving back to parent window
driver.switch_to.window(window[0])
driver.find_element(By.ID, "username").send_keys(mail)
driver.find_element(By.CSS_SELECTOR, "#password"). send_keys("123456789")
driver.find_element(By.ID, "signInBtn").click()

#waiting to element to be clickeable
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.element_to_be_clickable(
    driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']")))
print(driver.find_element(By.XPATH, ".//div[@class='alert alert-danger col-md-12']").text)