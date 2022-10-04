'''

Selenium Script using Google Maps as ressource for current location

'''

# Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep




# Note: chromedriver.exe must be in same directory as this script
# Note: Download from: https://sites.google.com/chromium.org/driver/downloads
driver = webdriver.Chrome()

# Open URL
driver.get("https://google.com/maps")

# Wait until cookies can be accepted and click accept
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button'))).click()

sleep(5)
# Wait until "Meinen Standort anzeigen" can be clicked and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[9]/div[23]/div[1]/div[3]/div[5]/div/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[9]/div[23]/div[1]/div[3]/div[5]/div/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[9]/div[23]/div[1]/div[3]/div[5]/div/button'))).click()

sleep(4)

# Get Lat-Long coordinates by the current url after finding current location
current_url = driver.current_url
print(current_url)


