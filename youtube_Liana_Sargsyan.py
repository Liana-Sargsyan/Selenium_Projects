from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

searchFieldElement = driver.find_element(By.NAME, "search_query")
searchFieldElement.clear()
time.sleep(10)
searchFieldElement.send_keys("psychology")
searchFieldElement.send_keys(Keys.ENTER)

time.sleep(5)

firstVideoElement = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
firstVideoElement.click()

time.sleep(10)

time.sleep(30)

pauseButton = driver.find_element(By.XPATH, "//*[@id='movie_player']/div[31]/div[2]/div[1]/button")
pauseButton.click()

driver.quit()
