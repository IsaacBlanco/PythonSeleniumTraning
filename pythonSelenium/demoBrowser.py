from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)

driver.get("http://google.com")
driver.maximize_window()
driver.get("http://www.udemy.com")
print(driver.title)
print(driver.current_url)
driver.back()
driver.forward()
driver.minimize_window()
# close the driver
driver.close()
