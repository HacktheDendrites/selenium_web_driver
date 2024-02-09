from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up chromeOptions to disable notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Maximize the window
driver.maximize_window()

# Navigate to the desired URL
driver.get("https://careers.servicenow.com/careers/jobs?page=1")

time.sleep(3)




# cookie handling

Cookie_Button = driver.find_element(By.XPATH,"//button[@id='truste-consent-button']")

Cookie_Button.click()

job_search_box = driver.find_element(By.XPATH,"//input[@id='keyword-search']")
time.sleep(3)
job_search_box.send_keys("Software Engineer")

time.sleep(5)

find_jobs_button = driver.find_element(By.XPATH, "//button[@type='submit'][1]")

time.sleep(4)

find_jobs_button.click()

time.sleep(15)

# Scroll down the page using JavaScript
Scroll_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
print(Scroll_height)
driver.execute_script("window.scrollTo(0,2000)")


Items_arrow = driver.find_element(By.XPATH,"//mat-select[@id='mat-select-32']")

Items_arrow.click()

Max_items = driver.find_element(By.XPATH,"//div[@id='mat-select-32-panel']/child::mat-option[4]")

Max_items.click()


# job_results_accordion = driver.find_elements(By.XPATH, "//mat-accordion[@class='mat-accordion cards']/child::mat-expansion-panel")


# i=1
# for accordion in job_results_accordion:
#     #find the header element and extracts its text
#     header_text = accordion.find_element(By.XPATH, "//mat-panel-title[contains(@class,'mat-expansion-panel-header-title')]")
#     JOB_TITILE = header_text.text
#     print("JOB TITLE :", JOB_TITILE)
#     i +=1
#     print(i)

# Find all mat-accordion elements containing 100 elements
accordion_elements = driver.find_elements(By.XPATH, "//mat-accordion[@class='mat-accordion cards']")

# Iterate through each accordion element
for accordion in accordion_elements:
    # Find all mat-expansion-panel elements within the accordion
    expansion_panels = accordion.find_elements(By.TAG_NAME, "mat-expansion-panel")
    
    # Iterate through each mat-expansion-panel element
    for panel in expansion_panels:
        # Extract and print the text from each panel
        JOB_TITLE = panel.find_element(By.CLASS_NAME, "mat-expansion-panel-header-title").text
        description_text = panel.find_element(By.CLASS_NAME, "mat-expansion-panel-header-description").text
        print("JOB TITLE:", JOB_TITLE)

        # IF YOU WANT DESCRIPTION THEN GO FOR THIS CODE
        # print("Description:", description_text)


                                
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                


# Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# print(last_height)