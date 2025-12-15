from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("Https://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")
button_login = driver.find_element(By.CSS_SELECTOR, ".radius")
button_login.click()
green_bar = driver.find_element(By.CSS_SELECTOR, "#flash")
print(green_bar.text)
sleep(10)
driver.quit()