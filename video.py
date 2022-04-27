from selenium.common.exceptions import TimeoutException
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

#Chrome driver
def initializeChromedriver():
    logging.info("Initializing the driver for Chrome")
    return webdriver.Chrome()


def getVideoUrl(url):
    return url



def playVideo(driverObj):
    #Finding the video by XPATH
    playVideo = driverObj.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button')
    logging.info("Finding the video by XPATH")

    #Playing the video
    playVideo.click()
    logging.info("Play")

    time.sleep(1)

    #Getting video div using CSS selector
    videoPanel = driverObj.find_element(By.CSS_SELECTOR, '#react-aria-modal-dialog')

    #Playing the video in full screen
    ActionChains(driverObj).move_to_element(videoPanel).double_click().perform()
    logging.info("Full screen mode for video")

    try:
        logging.info("Video in play mode...")
        #Waiting till video end
        WebDriverWait(driverObj, 100000).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]')))
    except TimeoutException as ex:
        logging.error(ex.message)
        


def getVideoDetails(driverObj):

    #Getting title of the video
    getTitle = driverObj.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/h1')
    logging.info("Title of the video: " + getTitle.get_attribute('textContent'))

    #Getting description of the video
    getDescription = driverObj.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]')
    logging.info("Description of the video: " + getDescription.get_attribute('textContent'))

    #Getting cast of the video
    getCast = driverObj.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[2]')
    logging.info("Movie starcast: " + getCast.get_attribute('textContent'))


def main():
    url = getVideoUrl("https://www.netflix.com/in/title/80192098")
    driver = initializeChromedriver()
    driver.get(url)

    #Maximizing the window
    driver.maximize_window()
    logging.info("Maximizing the window")

    playVideo(driver)
    getVideoDetails(driver)
    driver.quit()
    

if __name__ == "__main__":
    main()