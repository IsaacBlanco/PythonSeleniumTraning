import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# add options to chrome to change behaviour using class webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()

#start maximized
chrome_options.add_argument("--start-maximized")
#handlre errors certificates win pages
chrome_options.add_argument("--ignore-certificates-erros")

# chrome driver create a service to point to where the .exe is located
service_obj = Service("C:/Drivers/chromedriver.exe")
# integreate chrome options to driver
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

#add implicit wait
driver.implicitly_wait(4)
#go to url
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#got o shop using RE to fin the element using href only eith a pice of the string
driver.find_element(By.LINK_TEXT, "Shop").click()

time.sleep(2)
#finding and adding blacberry tp cart
elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(elements))
print(elements[0].text)
print(elements[1].text)
print(elements[2].text)
print(elements[3].text)
for element in elements:
    target_element = element.find_element(By.XPATH, "div/h4/a")
    print(target_element.text)
    if target_element.text == "Blackberry":
        element.find_element(By.XPATH, "div/button").click()

#clicking  checkout button
driver.find_element(By.XPATH, "//a[contains(text(), 'Checkout')]").click()

#clicking checkot
driver.find_element(By.CLASS_NAME, "btn-success").click()

#entering country
driver.find_element(By.ID, "country").send_keys("in")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='suggestions']//a")))

driver.find_element(By.LINK_TEXT, "Spain").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

result = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
expected = "Success! Thank you!"
print(result)
print(expected)
assert expected in result
