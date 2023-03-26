import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


#to run headless mode (browser wont open, nut execution will continue in background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
#handlre errors certificates win pages
chrome_options.add_argument("--ignore-certificates-erros")

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
# integreate chrome options to driver
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")