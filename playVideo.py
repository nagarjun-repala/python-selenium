import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

urlForVideo = "https://www.netflix.com/in/title/80192098"

#Chrome driver
driver = webdriver.Chrome()
logging.info("Initializing the driver for Chrome")

#Loading the below url
driver.get(urlForVideo)
logging.info("Loading the url: " + urlForVideo)

#Maximizing the window
driver.maximize_window()
logging.info("Maximizing the browser")

#Finding the video by XPATH
playVideo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button/span[1]')
logging.info("Finding the video by XPATH")

#Playing the video
playVideo.click()
logging.info("Playing the video")

time.sleep(2)

#Getting video div using CSS selector
videoPanel = driver.find_element(By.CSS_SELECTOR, '#react-aria-modal-dialog')

#Playing the video in full screen
ActionChains(driver).move_to_element(videoPanel).double_click().perform()
logging.info("Full screen mode for video")

#Getting title of the video
getTitle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/h1')
logging.info("Title of the video: " + getTitle.get_attribute('textContent'))

#Getting description of the video
getDescription = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]')
logging.info("Description of the video: " + getDescription.get_attribute('textContent'))

#Getting cast of the video
getCast = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[2]')
logging.info("Movie starcast: " + getCast.get_attribute('textContent'))
