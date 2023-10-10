from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

sighInButton = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
sighInButton.click()

emailField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ap_email")))
emailField.clear()
emailField.send_keys("lianasargsyan020@gmail.com")
emailField.send_keys(Keys.ENTER)

passwordField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ap_password")))
passwordField.send_keys("tracemalloc23")

sighIn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "signInSubmit")))
sighIn.click()

time.sleep(5)
driver.quit()




