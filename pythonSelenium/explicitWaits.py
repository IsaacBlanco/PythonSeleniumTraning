import time

from selenium import webdriver
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

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []
# open de brwoser and got to url
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

products_results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products_results)
assert count > 0
for product in products_results:
    # chaining of elements
    # "[parent].find_element()" this find the element starting from the parent element specified
    actual_list .append(driver.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()

assert expected_list == actual_list

driver.find_element(By.CSS_SELECTOR, "imd[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text='PROCEED TO CHECKOUT']").click()

# sun validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

total_amount = int(driver.find_element(By.CLASS_NAME, ".totAmt").text)

assert sum == total_amount

#apply promo coade
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#create a wait object
wait = WebDriverWait(driver, 15)
# specify conditions untill when the wait obecject is going to wait before proceding or finding the element
wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoInfo"))# inf fails add nother () afte located
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert  total_amount > discounted_amount
