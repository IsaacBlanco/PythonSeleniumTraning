from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/client/")
print(driver.current_url)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("hello@123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("hello@123")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
