
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

userNameelement = driver.find_element(By.ID, "email")
element = driver.find_element(By.CLASS_NAME, "element_class")
userNameelement.send_keys("Narine")
userNameelement.send_keys(Keys.ENTER)
userPasswordelement = driver.find_element(By.ID, "pass")
userPasswordelement.send_keys("aaaa")
userPasswordelement.send_keys(Keys.ENTER)