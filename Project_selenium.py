from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

# set uo chromeOptions to disable notifications

chrome_options = Options()
chrome_options.add_argument("--disable-notification")


# service_obj = Service("D:\PYTHON SELENIUM\SELENIUM_PRACTICE_FEB_6TH\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options)

# maximizing the window
driver.maximize_window()

driver.get("https://www.nvidia.com/en-in/geforce/laptops/")

time.sleep(2)

driver.get("https://www.google.com")
