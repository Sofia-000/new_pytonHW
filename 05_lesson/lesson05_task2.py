from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")
sleep(3)
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()
sleep(3)
button.click()
sleep(3)
button.click()
sleep(3)
driver.quit()