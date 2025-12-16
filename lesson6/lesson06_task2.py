from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
WebDriverWait(driver, 10)
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)
driver.quit()