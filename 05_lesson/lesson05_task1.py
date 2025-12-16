from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")
sleep(3)
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(3)
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(3)
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(3)
driver.quit()
