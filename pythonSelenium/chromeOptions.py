import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# add options to chrome to change behaviour using class webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()

#start maximized
chrome_options.add_argument("--start-maximized")
#handlre errors certificates win pages
chrome_options.add_argument("--ignore-certificates-erros")



#to run headless mode (browser wont open, nut execution will continue in background
chrome_options.add_argument("headless")

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
# integreate chrome options to driver
driver = webdriver.Chrome(service=service_obj, options=chrome_options)