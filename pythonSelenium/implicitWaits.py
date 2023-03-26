import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# wait for elemets to show up in this case mas 10s
driver.implicitly_wait(10)

# open de brwoser and got to url
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products_results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products_results)
assert count > 0
for product in products_results:
    # chaining of elements
    # "[parent].find_element()" this find the element starting from the parent element specified
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "imd[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text='PROCEED TO CHECKOUT']").click()

#apply promo coade
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
