from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Или другой браузер
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.ID, "landscape")))
wait.until(EC.visibility_of_element_located((By.ID, "compass")))
wait.until(EC.visibility_of_element_located((By.ID, "award")))
wait.until(EC.visibility_of_element_located((By.ID, "calendar")))
images = driver.find_elements(By.TAG_NAME, "img")
img = len((images))
src_txt = images[3].get_attribute("src")
print(src_txt)