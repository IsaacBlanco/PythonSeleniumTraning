from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver create a service to point to where the .exe is located

service_obj = Service("C:/Drivers/chromedriver.exe")
# open de brwoser and got to url
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# CSS_SELECTOR  --> tagname[attribute='value']   input[name='name'] if more than 1 then (CSS_selector)[index]
#                   #id, .class                  #name
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Valac Shiro")
driver.find_element(By.NAME, "email").send_keys("valac@shiro.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1223456")
driver.find_element(By.ID, "exampleCheck1").click()

# selectos static

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
print(dropdown.options[0])
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success" in message
